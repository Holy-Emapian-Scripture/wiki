---
layout: default
title: Organização da wiki
parent: Guias
nav_order: 3
tipo: guia
---

# Organização da wiki

Os arquivos de conteúdo são organizados por disciplina e assunto. Trilhas e hubs por semestre apontam para essas mesmas páginas, sem duplicar as explicações.

```text
index.md
assuntos/
  index.md
  catalogo.md
  aprendizado-profundo/
    index.md
    segmentacao-semantica/
      index.md
      arquiteturas.md        <-- Contém U-Net, SegNet, FCN, etc. consolidadas
    assets/
    referencias/
trilhas/
  index.md
  aprendizado-profundo/
    a1.md
semestres/
  index.md
  6-semestre.md
guias/
manutencao/
```

## Assuntos

Os tópicos de conteúdo são salvos diretamente como arquivos Markdown (`topico.md`) dentro da pasta da respectiva disciplina ou subcategoria temática (ex.: `assuntos/aprendizado-profundo/segmentacao-semantica/arquiteturas.md`). Pastas são reservadas para categorias e agrupamentos conceituais (pastas com `index.md`), evitando pastas redundantes que conteriam apenas um único arquivo `index.md`.

Os arquivos reúnem tópicos temáticos consolidados em páginas completas, evitando notas excessivamente curtas ou fragmentadas. Cada subtópico possui um título de nível 2 (`##`) acompanhado de âncora explícita (`<a id="..."></a>`), facilitando a citação pontual de seções e transclusões no Obsidian.

A sequência interna dos subtópicos preserva estritamente a ordem cronológica e pedagógica dos materiais de estudo originais. Exercícios mantêm suas soluções na mesma página. Figuras, fórmulas matemáticas em LaTeX, referências e códigos permanecem junto do trecho a que pertencem.

## Trilhas

As revisões A1, A2 e A3 se tornaram percursos com etapas na ordem original. Os demais documentos têm percursos de exercícios, notas de aula ou revisão geral.

Cada página oferece acesso aos tópicos subordinados, à trilha e às páginas anterior e seguinte. A apresentação da fonte permanece na trilha, incluindo avisos e premissas presentes antes do conteúdo.

## Semestres

Os hubs do 3º ao 6º semestre usam o agrupamento das pastas recebidas. Eletivas e Mestrado permanecem como grupos separados. O ano informado na capa não foi usado para mudar a classificação de semestre.

## Metadados e fontes

- `title`: título usado para identificar a página.
- `tipo`: conteúdo, exercício, revisão, notas ou hub.
- `disciplina`: disciplina à qual a página pertence.
- `autores` e `revisao`: atribuições presentes na fonte, quando disponíveis.
- `semestre` ou `grupo`: agrupamento original.
- `ano_original` e `data_original`: informações da fonte, sem inferir datas ausentes.
- `origem`: caminho histórico do documento antes da reorganização.
- `trilha`: caminho relativo para o percurso de leitura.
- `ordem_na_trilha`: posição do conteúdo na sequência original.

`origem` é um registro histórico, não um link para um arquivo atual. Os links navegáveis ficam no corpo das páginas.

## Preservação das anotações

A reorganização alterou títulos de nível, metadados, caminhos e navegação. Não corrigiu redação, erros conceituais, ortografia, fórmulas nem trechos incompletos.

Os comentários HTML `wiki:original:inicio` e `wiki:original:fim` delimitam o trecho importado de cada página. Eles não aparecem na leitura e permitem auditar a reorganização. A navegação adicionada fica fora desses trechos.

O [registro da reorganização](https://github.com/Holy-Emapian-Scripture/wiki/blob/main/content/manutencao/reorganizacao.md) documenta a verificação e as divergências encontradas nas fontes.

[Voltar aos guias](index.md)
