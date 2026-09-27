---
layout: "default"
title: "Notações — Graph Neural Networks"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 15
---

[Aprendizado de Máquina](../../index.md) · [Graph Neural Networks](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-18"></a>

# Notações

Para facilitar a compreensão, vamos definir algumas notações comuns usadas em GNNs:

- $G = (V,E)$: Um grafo onde $V$ é o conjunto de nós e $E$ é o conjunto de arestas.

- $A$: Matriz de adjacência do grafo, onde $A_{\left\{ ij \right\}} = 1$ se houver uma aresta entre os nós $i$ e $j$, e $0$ caso contrário.

- $X$: Matriz de características dos nós, onde cada linha representa as características de um nó. (Por exemplo, $x_{i}$ pode ser o conjunto **idade**, **peso**, **altura** de uma pessoa representada pelo nó $i$).

- Normalmente, é utilizada a matriz de adjacência normalizada com self loops, dada por $A' = (D + I)^{- \frac{1}{2}}(A + I)(D + I)^{- \frac{1}{2}}$, onde $D$ é a matriz diagonal de grau dos nós e $I$ é a matriz identidade onde $D_{ii} = \sum_{j}A_{ij} = \delta(v_{i}) = \text{ Grau de }v_{i}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Introdução](../introducao/index.md)
- Próximo: [Usos de GNNs](../usos-de-gnns/index.md)
