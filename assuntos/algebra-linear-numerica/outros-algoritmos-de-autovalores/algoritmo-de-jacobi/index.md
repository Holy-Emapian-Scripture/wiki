---
layout: "default"
title: "Algoritmo de Jacobi — Outros algoritmos de Autovalores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 57
---

[Álgebra Linear Numérica](../../index.md) · [Outros algoritmos de Autovalores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-57"></a>

# Algoritmo de Jacobi

A gente pode imaginar uma matriz $A$ como uma representação de um elipsóide num plano. Tente imaginar no plano $3$D. Se a gente conseguir rotacionar essa matriz $A$ (Rotacionar a elipe) até o ponto de que os eixos da elipse se alinhem com os eixos do plano, então $A$ seria diagonal (Ou seja, a gente obteria uma diagonalização de $A$).

Para uma melhor vizualisação desse conceito, veja <u>[esse vídeo](https://youtu.be/dQQ2PXo2maM?si=zsqU_lXXAm8mig0O)</u>

Ok, então o que podemos fazer pra ir fazendo isso? Vamos aplicando pequenas rotações $2 \times 2$ até obter o resultado designado, as rotações são do tipo: $$\begin{pmatrix} c & s \\ - s & c \end{pmatrix}$$

onde $c = \cos(\theta)$ e $s = \sin(\theta)$ para algum $\theta$. Vale dizer também que essa rotação é para o caso de $A \in {\mathbb{R}}^{2 \times 2}$. Se $A$ é uma matriz de dimensão maior, então a matriz de rotação é a identidade com um bloco do tipo que apresentei antes em algum lugar (Qualquer lugar da matriz). No final a gente teria uma matriz $J$ tal que: $$J^{T}AJ = \text{ Diagonal }$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Outros algoritmos de Autovalores](../index.md)
- Próximo: [Bisection](../bisection/index.md)
