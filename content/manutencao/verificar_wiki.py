#!/usr/bin/env python3
"""Audita a wiki atual; --site confere o HTML e --preservacao a revisão histórica."""
import argparse
import hashlib
from html.parser import HTMLParser
import io
import json
import re
import subprocess
import tarfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
BEGIN = '<!-- wiki:original:inicio -->\n'
END = '<!-- wiki:original:fim -->'
HISTORICAL_REF = '1fe4ea2a4af9523d92c1af77fe8a4761889ee72b'
WIKILINK = re.compile(r'(?<!!)\[\[([^\]\n]+)\]\]')
MARKDOWN_LINK = re.compile(r'\]\(([^\n)]*)\)')


def digest(data):
    return hashlib.sha256(data.encode('utf-8') if isinstance(data, str) else data).hexdigest()


def ignored_paths():
    config = (REPO / 'quartz.config.yaml').read_text()
    block = re.search(r'(?m)^  ignorePatterns:\n((?:    - [^\n]+\n)+)', config)
    if not block:
        raise ValueError('ignorePatterns não encontrado em quartz.config.yaml')
    return {line.removeprefix('    - ').strip().strip('"\'') for line in block[1].splitlines()}


def visible_lines(text):
    fence = None
    for line in text.splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})(.*)', line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= fence[1] and not match[2].strip():
                fence = None
        elif match:
            fence = (match[1][0], len(match[1]))
        else:
            yield line
    if fence:
        raise ValueError('Bloco de código sem fechamento')


def without_metadata(text):
    return text.split('\n---\n', 1)[1] if text.startswith('---\n') else text


def slug(label):
    return re.sub(r'[^\w\- ]', '', label.lower()).replace(' ', '-')


def anchors(text):
    body = '\n'.join(visible_lines(without_metadata(text)))
    explicit = re.findall(r'<a\s+id="([^"]+)"\s*></a>', body)
    result = set(explicit)
    for label in re.findall(r'^#{1,6} (.+)$', body, re.M):
        result.add(slug(label))
    return result, len(explicit) != len(set(explicit))


def resolve_wikilink(source, target, pages):
    path = target.split('#', 1)[0]
    if not path:
        return source
    path = unquote(path)
    root_names = {'assuntos', 'trilhas', 'semestres', 'guias', 'disciplinas', 'index'}
    first = path.split('/', 1)[0]
    base = ROOT if first in root_names and not path.startswith(('./', '../')) else source.parent
    candidate = (base / path).resolve()
    if candidate.suffix == '':
        md = candidate.with_suffix('.md')
        index = candidate / 'index.md'
        if md in pages:
            return md
        if index in pages:
            return index
        candidate = md
    return candidate


def source_check():
    errors = []
    ignored = ignored_paths()
    pages = {p.resolve(): p.read_text() for p in ROOT.rglob('*.md')
             if not any(part.startswith('.') or part in ignored for part in p.relative_to(ROOT).parts)}
    targets = {}
    for p, text in pages.items():
        rel = p.relative_to(ROOT)
        try:
            ids, duplicate = anchors(text)
            targets[p] = ids
            if duplicate:
                errors.append(f'{rel}: âncora explícita duplicada')
        except ValueError as exc:
            errors.append(f'{rel}: {exc}')
        if not text.startswith('---\n'):
            errors.append(f'{rel}: metadados ausentes')

    edges = {p: set() for p in pages}
    count = 0
    for p, text in pages.items():
        try:
            lines = visible_lines(without_metadata(text))
            for line in lines:
                inline = [(m.start(), m.end()) for m in re.finditer(r'(`+).*?\1', line)]
                for match in MARKDOWN_LINK.finditer(line):
                    if any(a <= match.start() < b for a, b in inline):
                        continue
                    url = match[1].strip('<>')
                    if re.match(r'^[a-zA-Z][\w+.-]*:', url) or url.startswith('//'):
                        continue
                    parts = urlsplit(url)
                    dest = (p.parent / unquote(parts.path)).resolve() if parts.path else p
                    count += 1
                    if not dest.is_relative_to(ROOT):
                        errors.append(f'{p.relative_to(ROOT)}: destino fora da wiki {url}')
                    elif not dest.is_file():
                        errors.append(f'{p.relative_to(ROOT)}: arquivo ausente {url}')
                    elif parts.fragment and dest.suffix == '.md' and unquote(parts.fragment) not in targets.get(dest, set()):
                        errors.append(f'{p.relative_to(ROOT)}: âncora ausente {url}')
                    if dest in edges:
                        edges[p].add(dest)
                for match in WIKILINK.finditer(line):
                    if any(a <= match.start() < b for a, b in inline):
                        continue
                    raw = match[1].split('|', 1)[0]
                    dest = resolve_wikilink(p, raw, pages)
                    fragment = raw.split('#', 1)[1] if '#' in raw else ''
                    count += 1
                    if not dest.is_relative_to(ROOT) or dest not in pages:
                        errors.append(f'{p.relative_to(ROOT)}: wikilink sem página {raw}')
                    elif fragment and unquote(fragment) not in targets[dest] and slug(unquote(fragment)) not in targets[dest]:
                        errors.append(f'{p.relative_to(ROOT)}: wikilink sem âncora {raw}')
                    if dest in edges:
                        edges[p].add(dest)
        except ValueError as exc:
            errors.append(f'{p.relative_to(ROOT)}: {exc}')

    seen = set()
    pending = [(ROOT / 'index.md').resolve()]
    while pending:
        page = pending.pop()
        if page in seen:
            continue
        seen.add(page)
        pending.extend(edges.get(page, set()) - seen)
    for page in pages:
        if page not in seen:
            errors.append(f'Página sem caminho a partir do início: {page.relative_to(ROOT)}')
    return errors, len(pages), count


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if data.get('id'):
            self.ids.add(data['id'])
        if tag == 'a' and data.get('data-slug'):
            self.links.append((data['data-slug'], data.get('href', '')))
        if tag == 'img' and data.get('src'):
            self.images.append(data['src'])


def site_check(site):
    if not (site / 'index.html').is_file():
        return [f'HTML não encontrado em {site}; execute a compilação antes de --site'], 0
    cache = {}

    def parse(path):
        if path not in cache:
            parser = SiteParser()
            parser.feed(path.read_text())
            cache[path] = parser
        return cache[path]

    errors = []
    count = 0
    for page in site.rglob('*.html'):
        if 'static' in page.relative_to(site).parts:
            continue
        rel = page.relative_to(site)
        parsed = parse(page)
        for slug_name, href in parsed.links:
            count += 1
            route = unquote(urlsplit(href).path)
            route_exists = True
            if route:
                local = (site / route.lstrip('/')) if route.startswith('/') else page.parent / route
                route_exists = local.is_file() or local.with_suffix('.html').is_file() or (local / 'index.html').is_file()
            # Quartz também atribui data-slug a anexos, como arquivos .bib.
            attachment = site / slug_name
            if Path(slug_name).suffix and attachment.is_file():
                continue
            target = site / (slug_name + '.html')
            if not target.is_file():
                target = site / slug_name / 'index.html'
            if not target.is_file():
                errors.append(f'{rel}: página publicada ausente {href}')
                continue
            if not route_exists:
                errors.append(f'{rel}: rota publicada ausente {href}')
            fragment = unquote(urlsplit(href).fragment)
            if fragment and fragment not in parse(target).ids:
                errors.append(f'{rel}: âncora publicada ausente {href}')
        for src in parsed.images:
            parts = urlsplit(src)
            if parts.scheme or src.startswith('//'):
                continue
            target = (site / unquote(parts.path).lstrip('/')) if parts.path.startswith('/') else page.parent / unquote(parts.path)
            if not target.is_file():
                errors.append(f'{rel}: imagem publicada ausente {src}')
    return errors, count


def historical_check():
    """Reconstrói os 35 documentos na revisão anterior à consolidação."""
    try:
        archive = subprocess.run(['git', 'archive', HISTORICAL_REF, 'content'], cwd=REPO,
                                 capture_output=True, check=True).stdout
    except subprocess.CalledProcessError as exc:
        return [f'Revisão histórica indisponível ({HISTORICAL_REF}); obtenha o histórico Git completo: {exc.stderr.decode().strip()}']
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        files = {m.name: tar.extractfile(m).read() for m in tar.getmembers() if m.isfile()}
    manifest_bytes = files.get('content/manutencao/reorganizacao.json')
    if not manifest_bytes:
        return ['Manifesto histórico ausente na revisão de referência']
    errors = []
    if digest(manifest_bytes) != digest((ROOT / 'manutencao/reorganizacao.json').read_bytes()):
        errors.append('O manifesto histórico mudou; mantenha-o como registro imutável')
    manifest = json.loads(manifest_bytes)
    for doc in manifest['documents']:
        recovered = []
        cursor = 0
        for segment in doc['segments']:
            name = 'content/' + segment['page']
            if name not in files:
                errors.append(f'{segment["page"]}: página ausente na revisão histórica')
                continue
            text = files[name].decode('utf-8')
            if text.count(BEGIN) != 1 or text.count(END) != 1:
                errors.append(f'{segment["page"]}: marcadores históricos ausentes/duplicados')
                continue
            body = text.split(BEGIN, 1)[1].split(END, 1)[0]
            try:
                for edit in reversed(segment['edits']):
                    at = edit['at']
                    assert body[at:at + len(edit['after'])] == edit['after']
                    body = body[:at] + edit['before'] + body[at + len(edit['after']):]
                assert digest(body) == segment['original_sha256']
                assert segment['start'] == cursor
                cursor = segment['end']
                assert len(body) == segment['end'] - segment['start']
            except AssertionError:
                errors.append(f'{segment["page"]}: trecho histórico divergente')
            recovered.append(body)
        if digest(''.join(recovered)) != doc['sha256']:
            errors.append(f'{doc["source"]}: reconstrução histórica divergente')
    for asset in manifest['assets']:
        name = 'content/' + asset['path']
        if name not in files or digest(files[name]) != asset['sha256']:
            errors.append(f'{asset["path"]}: anexo histórico ausente ou alterado')
    return errors


def check(preservation=False, site=None):
    errors, pages, links = source_check()
    site_links = 0
    if site is not None:
        site_errors, site_links = site_check(site)
        errors.extend(site_errors)
    if preservation:
        errors.extend(historical_check())
    return {'paginas_verificadas': pages, 'links_locais_verificados': links,
            'links_publicados_verificados': site_links,
            'preservacao_verificada': preservation,
            'revisao_historica': HISTORICAL_REF if preservation else None,
            'erros': errors}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preservacao', action='store_true', help='Audita a reorganização na revisão histórica imutável.')
    parser.add_argument('--site', action='store_true', help='Confere links e imagens no HTML já compilado em public/.')
    parser.add_argument('--relatorio', type=Path, help='Grava o resultado em JSON.')
    args = parser.parse_args()
    result = check(args.preservacao, REPO / 'public' if args.site else None)
    output = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    print(output, end='')
    if args.relatorio:
        args.relatorio.write_text(output)
    raise SystemExit(bool(result['erros']))
