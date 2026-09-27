---
layout: "default"
title: "A ideia da fatoração reduzida — Fatoração QR"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 21
---

[Álgebra Linear Numérica](../../index.md) · [Fatoração QR](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-21"></a>

# A ideia da fatoração reduzida

Seja $\left\{ a_{j} \right\}$ as colunas de $A \in {\mathbb{C}}^{m \times n},\ m \geq n$. Em algumas aplicações, estamos interessados nos espaços das colunas de $A$, ou seja, os espaços sequenciais gerados pelas colunas de $A$:

span$\left\{ a_{1} \right\} \subseteq$ span$\left\{ a_{1},a_{2} \right\} \subseteq$ span$\left\{ a_{1},a_{2},a_{3} \right\} \subseteq \ldots$

Por enquanto, assumiremos que $A$ tem posto completo $n$. Primeiro, queremos obter um conjunto de vetores ortonormais com a seguinte propriedade:

span$\left\{ a_{1},\ldots,a_{j} \right\} =$ span$\left\{ q_{1},\ldots,q_{j} \right\}$ com $j = 1,\ldots,n$

Bem, acho que uma boa ideia para fazer isso é usar vetores tais que possamos expressar $a_{j}$ como uma combinação linear de $\left\{ q_{1},\ldots,q_{j} \right\}$. Isso significa: $$a_{1} = r_{11}q_{1}$$ $$a_{2} = r_{12}q_{1} + r_{22}q_{2}$$ $$\vdots$$ $$a_{n} = r_{1n}q_{1} + r_{2n}q_{2} + \ldots + r_{nn}q_{n}$$

Podemos expressar essas equações como um produto matricial!

$$\begin{pmatrix} \vert  & \vert  & & \vert  \\ a_{1} & a_{2} & \ldots & a_{n} \\ \vert  & \vert  & & \vert \end{pmatrix} = \begin{pmatrix} \vert  & \vert  & & \vert  \\ q_{1} & q_{2} & \ldots & q_{n} \\ \vert  & \vert  & & \vert \end{pmatrix}\begin{pmatrix} r_{11} & r_{12} & \ldots & r_{1n} \\ & r_{22} & & \vdots \\ & & \ddots & \vdots \\ & & & r_{nn} \end{pmatrix}$$

Então temos $A = \widehat{Q}\widehat{R}$, onde $Q \in {\mathbb{C}}^{m \times n}$ e $R \in {\mathbb{C}}^{n \times n}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Fatoração QR](../index.md)
- Próximo: [Fatoração QR completa](../fatoracao-qr-completa/index.md)
