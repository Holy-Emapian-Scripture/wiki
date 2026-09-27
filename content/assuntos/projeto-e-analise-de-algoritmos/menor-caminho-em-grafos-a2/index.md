---
layout: "default"
title: "Menor caminho em Grafos"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A2.md"
trilha: "../../../trilhas/projeto-e-analise-de-algoritmos/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 14
---

[Projeto e Análise de Algoritmos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-24"></a>

# Menor caminho em Grafos

------------------------------------------------------------------------

Na seção anterior, tentamos verificar que o caminho existe. Agora, temos um novo problema:

Dados dois vértices $v_{i}$ e $v_{j}$ em um grafo $G = (V,E)$, encontre o caminho mínimo $P$ que começa em $v_{i}$ e termina em $v_{j}$.

Se o grafo for tiver mais de uma componente conexa, pode não existir um caminho entre $v_{i}$ e $v_{j}$ (podemos dizer que a distância é infinita). Além disso, se o grafo for orientado, a distância entre $v_{i}$ e $v_{j}$ pode ser diferente de $v_{j}$ para $v_{i}$.

Para encontrar o caminho mais curto entre $v_{i}$ e $v_{j}$ é inevitável encontrar todos os caminhos que iniciam em $v_{i}$. A árvore produzida pela busca do menor caminho é chamada de Árvore de caminhos mais curtos (SPT - Shortest Path Tree).

A árvore SPT é uma sub-árvore radicada de $G$:

- Todos os vértices de $G$ estão presentes na SPT.

- Todo caminho na SPT a partir da raiz é mínimo no grafo $G$.

Um grafo possui uma SPT caso todos os vértices sejam acessíveis a partir de $v_{i}$. Caso não exista uma SPT para um grafo $G$ a partir de um grafo $v_{i}$, existe uma SPT para um sub-grafo induzido de $G$ com os vértices acessíveis a partir de $v_{i}$.

Portanto, para encontrar o menor caminho entre $v_{i}$ e $v_{j}$ precisamos encontrar a árvore radicada desse sub-grafo com raiz em $v_{i}$.

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Caminho mais curto em um DAG](caminho-mais-curto-em-um-dag/index.md)
2. [Caminho mais curto em grafos não-dirigidos/ciclo](caminho-mais-curto-em-grafos-nao-dirigidos-ciclo/index.md)
3. [Caminho mais barato em grafos](caminho-mais-barato-em-grafos/index.md)

## Percurso de estudo

[Trilha: A2](../../../trilhas/projeto-e-analise-de-algoritmos/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/projeto-e-analise-de-algoritmos/a2.md#apresentacao-original)

- Anterior: [Busca em Grafos](../busca-em-grafos-a2/index.md)
- Próximo: [Árvore Geradora Minima](../arvore-geradora-minima/index.md)
