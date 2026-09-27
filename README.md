# Holy Emapian Wiki

Acervo em Markdown para edição no Obsidian e futura publicação no GitHub Pages.

Comece pela **[página inicial](index.md)** ou navegue por [assuntos](assuntos/index.md), [trilhas](trilhas/index.md) e [semestres](semestres/index.md).

## Estrutura

- `assuntos/`: 19 disciplinas, com 688 páginas de conteúdo organizadas por assunto e seus anexos.
- `trilhas/`: 35 percursos a partir das revisões A1/A2/A3, exercícios e notas de aula.
- `semestres/`: hubs do 3º ao 6º semestre, Eletivas e Mestrado.
- `guias/`: orientações e modelo de página.
- `manutencao/`: registros de origem, mapa da reorganização e verificador.

As explicações, fórmulas, códigos, legendas e referências das 35 anotações recebidas foram preservados. Apenas a estrutura, os metadados e os destinos dos links foram reorganizados. Os 292 arquivos de imagem e as duas bibliografias foram mantidos byte a byte.

## Edição

Abra esta pasta como um vault do Obsidian. Use links Markdown relativos; mantenha as imagens na pasta `assets/` da disciplina. Consulte [como contribuir](guias/como-contribuir.md) e a [organização da wiki](guias/organizacao-da-wiki.md).

Os metadados estão preparados para o Jekyll. O build e a publicação no GitHub Pages, incluindo a conversão dos links `.md` e o suporte matemático, ainda precisam ser configurados.

## Verificação

Requer apenas Python 3.9 ou superior:

```sh
python3 manutencao/verificar_wiki.py
```

Para auditar a preservação integral em relação à versão importada:

```sh
python3 manutencao/verificar_wiki.py --preservacao
```

A opção `--preservacao` reconstrói cada documento original em memória, desfazendo apenas as mudanças estruturais registradas, e compara os hashes. Ela também confere os hashes dos anexos. Alterações futuras nas explicações farão essa auditoria histórica apontar diferenças; a verificação comum de navegação continua disponível sem essa opção.

Veja o [registro da reorganização](manutencao/reorganizacao.md), o [registro da conversão anterior](manutencao/conversao-original.md) e a [licença](LICENSE).
