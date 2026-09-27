import tempfile
import unittest
from pathlib import Path

from verificar_wiki import anchors, resolve_wikilink, site_check, visible_lines


class WikiVerifierTests(unittest.TestCase):
    def test_nested_fenced_examples_are_not_links(self):
        text = 'antes\n     ```markdown\n     [exemplo](ausente.md)\n     ```\ndepois\n'
        self.assertEqual(list(visible_lines(text)), ['antes', 'depois'])

    def test_heading_link_resolves_to_markdown_page(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'index.md'
            target = Path(directory) / 'tema.md'
            pages = {source, target}
            self.assertEqual(resolve_wikilink(source, 'tema#Atrous Convolution', pages), target)
            ids, duplicate = anchors('---\ntitle: Teste\n---\n\n### Atrous Convolution\n')
            self.assertIn('atrous-convolution', ids)
            self.assertFalse(duplicate)

    def test_site_check_detects_broken_links_and_images(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / 'index.html').write_text('<a data-slug="tema" href="./tema#certo">ok</a>'
                                             '<a data-slug="ausente" href="./ausente">erro</a>'
                                             '<img src="imagem.png">')
            (site / 'tema.html').write_text('<h2 id="certo">Tema</h2>')
            errors, count = site_check(site)
            self.assertEqual(count, 2)
            self.assertTrue(any('página publicada ausente' in e for e in errors))
            self.assertTrue(any('imagem publicada ausente' in e for e in errors))
            self.assertFalse(any('certo' in e for e in errors))

    def test_site_check_detects_wrong_route_to_existing_page(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / 'index.html').write_text('<a data-slug="tema" href="./errado">Tema</a>')
            (site / 'tema.html').write_text('<h1>Tema</h1>')
            errors, _ = site_check(site)
            self.assertTrue(any('rota publicada ausente' in e for e in errors))


if __name__ == '__main__':
    unittest.main()
