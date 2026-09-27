#!/usr/bin/env python3
"""Verifica a navegação; --preservacao audita a reorganização contra os hashes originais."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
BEGIN = '<!-- wiki:original:inicio -->\n'
END = '<!-- wiki:original:fim -->'
OLD_ROOTS = {'3 semestre', '4 semestre', '5 semestre', '6 semestre', 'Eletivas', 'Mestrado'}


def digest(data):
    return hashlib.sha256(data.encode('utf-8') if isinstance(data, str) else data).hexdigest()


def visible_lines(text):
    fence = None
    for line in text.splitlines():
        match = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)', line)
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


def anchors(text):
    body = '\n'.join(visible_lines(without_metadata(text)))
    explicit = re.findall(r'<a\s+id="([^"]+)"\s*></a>', body)
    result = set(explicit)
    for label in re.findall(r'^#{1,6} (.+)$', body, re.M):
        base = re.sub(r'[^\w\- ]', '', label.lower()).replace(' ', '-')
        result.add(base)
    return result, len(explicit) != len(set(explicit))


def check(preservation=False):
    errors = []
    manifest = json.loads((ROOT / 'manutencao/reorganizacao.json').read_text())
    pages = {p: p.read_text() for p in ROOT.rglob('*.md')
             if not any(part.startswith('.') for part in p.relative_to(ROOT).parts)
             and p.relative_to(ROOT).parts[0] not in OLD_ROOTS}
    targets = {}
    for p, text in pages.items():
        try:
            ids, duplicate = anchors(text)
            targets[p.resolve()] = ids
            if duplicate:
                errors.append(f'{p.relative_to(ROOT)}: âncora explícita duplicada')
        except ValueError as exc:
            errors.append(f'{p.relative_to(ROOT)}: {exc}')
        if p.name != 'README.md' and not text.startswith('---\n'):
            errors.append(f'{p.relative_to(ROOT)}: metadados ausentes')
    count = 0
    edges = {p.resolve(): set() for p in pages}
    for p, text in pages.items():
        for line in visible_lines(without_metadata(text)):
            inline = [(m.start(), m.end()) for m in re.finditer(r'(`+).*?\1', line)]
            for match in re.finditer(r'\]\(([^\n)]*)\)', line):
                if any(a <= match.start() < b for a, b in inline):
                    continue
                url = match[1].strip('<>')
                if re.match(r'^[a-zA-Z][\w+.-]*:', url) or url.startswith('//'):
                    continue
                parts = urlsplit(url)
                dest = (p.parent / unquote(parts.path)).resolve() if parts.path else p.resolve()
                count += 1
                if not dest.is_relative_to(ROOT):
                    errors.append(f'{p.relative_to(ROOT)}: destino fora da wiki {url}')
                elif not dest.is_file():
                    errors.append(f'{p.relative_to(ROOT)}: arquivo ausente {url}')
                elif parts.fragment and dest.suffix == '.md' and unquote(parts.fragment) not in targets.get(dest, set()):
                    errors.append(f'{p.relative_to(ROOT)}: âncora ausente {url}')
                if dest in edges:
                    edges[p.resolve()].add(dest)
    # Every study page and every track must be reachable from the homepage.
    seen = set()
    pending = [(ROOT / 'index.md').resolve()]
    while pending:
        page = pending.pop()
        if page in seen:
            continue
        seen.add(page)
        pending.extend(edges.get(page, set()) - seen)
    for doc in manifest['documents']:
        for segment in doc['segments']:
            if (ROOT / segment['page']).resolve() not in seen:
                errors.append(f"Página sem caminho a partir do início: {segment['page']}")
    if preservation:
        for doc in manifest['documents']:
            recovered = []
            cursor = 0
            for segment in doc['segments']:
                path = ROOT / segment['page']
                try:
                    text = path.read_bytes().decode('utf-8')
                    assert text.count(BEGIN) == text.count(END) == 1, 'marcadores ausentes/duplicados'
                    body = text.split(BEGIN, 1)[1].split(END, 1)[0]
                    for edit in reversed(segment['edits']):
                        at = edit['at']
                        assert body[at:at+len(edit['after'])] == edit['after'], 'edição estrutural divergente'
                        body = body[:at] + edit['before'] + body[at+len(edit['after']):]
                    assert digest(body) == segment['original_sha256'], 'conteúdo original alterado'
                    assert segment['start'] == cursor, 'lacuna ou sobreposição de trechos'
                    cursor = segment['end']
                    assert len(body) == segment['end'] - segment['start'], 'tamanho divergente'
                    recovered.append(body)
                except (AssertionError, FileNotFoundError) as exc:
                    errors.append(f'{segment["page"]}: {exc}')
            if digest(''.join(recovered)) != doc['sha256']:
                errors.append(f'{doc["source"]}: reconstrução integral divergente')
        for asset in manifest['assets']:
            p = ROOT / asset['path']
            if not p.is_file() or digest(p.read_bytes()) != asset['sha256']:
                errors.append(f'{asset["path"]}: anexo ausente ou alterado')
    result = {'paginas_verificadas': len(pages), 'links_locais_verificados': count,
              'documentos_originais': len(manifest['documents']),
              'paginas_de_conteudo': sum(len(d['segments']) - 1 for d in manifest['documents']),
              'anexos': len(manifest['assets']), 'preservacao_verificada': preservation,
              'erros': errors}
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preservacao', action='store_true', help='Compara textos e anexos à versão anterior à reorganização.')
    parser.add_argument('--relatorio', type=Path, help='Grava o resultado em JSON.')
    args = parser.parse_args()
    result = check(args.preservacao)
    output = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    print(output, end='')
    if args.relatorio:
        args.relatorio.write_text(output)
    raise SystemExit(bool(result['erros']))
