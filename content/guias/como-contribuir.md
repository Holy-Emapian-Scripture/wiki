---
layout: default
title: Como contribuir
parent: Guias
nav_order: 1
---

# Como contribuir

Uma contribuição pode ser pequena: corrigir uma explicação, acrescentar uma referência ou escrever um exemplo já ajuda.

## Crie uma página

1. Copie o arquivo `guias/modelo-de-pagina.md` para uma pasta em `assuntos/<disciplina>/<assunto>/` e salve-o como `index.md`.
2. Escolha nomes curtos para as pastas, em minúsculas e com hífens, como `algebra-linear`.
3. Ajuste o título e a seção no cabeçalho do arquivo.
4. Substitua os campos entre colchetes pelo conteúdo da nota e remova seções vazias.
5. Adicione um link para a nova página no índice da seção.

O cabeçalho entre `---` guarda os metadados da página. `title` define o título, `parent` indica a seção no menu e `nav_order` define a ordem dentro dela. Os índices de disciplinas usam `parent: Assuntos`. As páginas de conteúdo usam `nav_exclude: true` e são acessadas pelos índices e trilhas, mantendo o menu principal compacto.

Registre `disciplina`, `autores` e, quando conhecidos, `semestre` e `origem`. Não deduza autoria ou datas ausentes. Consulte a [organização da wiki](organizacao-da-wiki.md) para a estrutura completa.

## Conecte as notas

Use links Markdown com caminhos relativos ao arquivo atual. Por exemplo, de uma página dentro de `guias/`:

```markdown
[Página inicial](../index.md)
[Disciplinas](../disciplinas/index.md)
[Como contribuir](como-contribuir.md)
```

Ao mover ou renomear um arquivo, confira os links que apontam para ele.

## Edite no Obsidian

Abra a pasta da wiki como um vault. Nas configurações de arquivos e links, prefira links Markdown, caminhos relativos e atualização automática de links ao renomear arquivos.

Salve as imagens em `assuntos/<disciplina>/assets/`. Em uma nota em `assuntos/<disciplina>/<assunto>/index.md`, a sintaxe seria:

```markdown
![Descrição do conteúdo da imagem](../assets/nome-da-imagem.png)
```

Esse exemplo exige que a imagem correspondente exista.

## Escreva para quem está aprendendo

- Apresente a ideia antes da notação ou dos detalhes.
- Explique os passos de uma resolução e por que eles funcionam.
- Diferencie uma definição, um exemplo e uma opinião pessoal.
- Cite a origem dos materiais e indique quando uma informação depende do período ou da turma.

## Use tabelas e equações

Uma tabela simples:

```markdown
| Material | Assunto | Observação |
|----------|---------|------------|
| Nota de estudo | Vetores | Introdução com exemplos |
```

No Obsidian, escreva matemática dentro de frases com `$...$` e equações destacadas com `$$...$$`:

```text
A função $f(x) = x^2$ tem derivada $f'(x) = 2x$.

$$
\int_0^1 x^2\,dx = \frac{1}{3}
$$
```

## Antes de publicar

Confira se o texto está claro, se os links abrem e se as fontes estão identificadas. Compartilhe arquivos de terceiros apenas quando houver permissão; quando possível, faça um link para a fonte original.

Nesta etapa, a wiki está estruturada em Markdown. A publicação no GitHub Pages, a conversão de links `.md` e a exibição de equações no site ainda serão configuradas.

[Voltar aos guias](index.md)
