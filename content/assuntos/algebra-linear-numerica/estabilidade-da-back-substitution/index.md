---
layout: "default"
title: "Estabilidade da Back Substitution"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 5
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Estabilidade da Back Substitution

------------------------------------------------------------------------

Só para esclarecer, o termo **back substitution** se refere ao algoritmo de resolver um sistema triangular superior

$$\begin{pmatrix} r_{11} & r_{12} & \ldots & r_{1m} \\ & r_{22} & \ldots & r_{2m} \\ & & \ddots & \vdots \\ & & & r_{mm} \end{pmatrix}\begin{pmatrix} x_{1} \\ \vdots \\ x_{m} \end{pmatrix} = \begin{pmatrix} b_{1} \\ \vdots \\ b_{m} \end{pmatrix}$$

E é aquele esquema, a gente vai resolvendo de baixo para cima, o que resulta nesse algoritmo (A gente escreve como uma sequência de fórmulas por conveniência, mas é o mesmo que escrever um loop):

<a id="back-substitution"></a>

1.  **function** BackSubstitution($R \in {\mathbb{C}}^{m \times m}$, $b \in {\mathbb{C}}^{m \times 1}$) {

    1.  $x_{m} = b_{m}/r_{mm}$

    2.  $x_{m - 1} = \left( b_{m - 1} - x_{m}r_{m - 1,m} \right)/r_{m - 1,m - 1}$

    3.  $x_{m - 2} = \left( b_{m - 2} - x_{m - 1}r_{m - 2,m - 1} - x_{m}r_{m - 2,m} \right)/r_{m - 2,m - 2}$

    4.  $\vdots$

    5.  $x_{j} = \left( b_{j} - \sum_{k = j + 1}^{m}x_{k}r_{jk} \right)/r_{jj}$

2.  }

*Figura 2. Algoritmo de **Back Substitution***

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Teorema da Estabilidade Retroativa (Backward Stability)](teorema-da-estabilidade-retroativa-backward-stability/index.md)

## Percurso de estudo

[Trilha: A2](../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Algoritmo para resolver $Ax = b$](../estabilidade-da-triangularizacao-de-householder/algoritmo-para-resolver-ax-b/index.md)
- Próximo: [Teorema da Estabilidade Retroativa (Backward Stability)](teorema-da-estabilidade-retroativa-backward-stability/index.md)
