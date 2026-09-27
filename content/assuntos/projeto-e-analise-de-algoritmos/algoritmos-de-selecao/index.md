---
layout: "default"
title: "Algoritmos de Seleção"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A1.md"
trilha: "../../../trilhas/projeto-e-analise-de-algoritmos/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
revisao: "Thalis Ambrosim Falqueto"
ano_original: 2025
ordem_na_trilha: 25
---

[Projeto e Análise de Algoritmos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-30"></a>

# Algoritmos de Seleção

------------------------------------------------------------------------

Dada uma sequência não ordenada,

1.  como retornar a mediana do conjunto sem ordenar a sequência?

2.  como retornar o i-ésimo elemento sem ordenar a sequência?

Se pudessemos ordenar… Bastaria:

1.  acessar `v[n/2]` se $n$ ímpar ou (`v[n/2]` + `v[n/2 + 1]`)/2 se $n$ par;

2.  apenas acessar o elemento `v[i]`.

Infelizmente, esse não é o caso. Então vamos aprender alguns algoritmos que descobrem isso sem ordenar a lista!

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Quickselect](quickselect/index.md)
2. [Mediana das Medianas](mediana-das-medianas/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Bucket Sort](../algoritmos-de-ordenacao/bucket-sort/index.md)
- Próximo: [Quickselect](quickselect/index.md)
