---
layout: "default"
title: "Gram-Schmidt como Ortonormalização Triangular — Ortonormalização de Gram-Schmidt"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 27
---

[Álgebra Linear Numérica](../../index.md) · [Ortonormalização de Gram-Schmidt](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-27"></a>

# Gram-Schmidt como Ortonormalização Triangular

Podemos interpretar cada passo do algoritmo de Gram-Schmidt como uma multiplicação à direita por uma matriz triangular superior quadrada. Espere, o quê? Por quê? Pegue a matriz $R$: $$\begin{pmatrix} r_{11} & r_{12} & \ldots & r_{1n} \\ & r_{22} & & \vdots \\ & & \ddots & \vdots \\ & & & r_{nn} \end{pmatrix}$$

Você pode separá-la como: $$\begin{pmatrix} r_{11} & r_{12} & \ldots & r_{1n} \\ & 1 & & \vdots \\ & & \ddots & \vdots \\ & & & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 & \ldots & 0 \\ & r_{22} & & \vdots \\ & & \ddots & \vdots \\ & & & 1 \end{pmatrix}\ldots$$

Então, podemos ver facilmente que, para a $j$-ésima matriz, a inversa dela é:

$$\begin{pmatrix} \ddots & \\ & 1 \\ & & r_{jj} & r_{j(j + 1)} & \ldots \\ & & & \ddots \end{pmatrix}^{- 1} = \begin{pmatrix} \ddots & \\ & 1 \\ & & \frac{1}{r_{jj}} & - \frac{r_{j(j + 1)}}{r_{jj}} & \ldots \\ & & & \ddots \end{pmatrix}$$

Isso significa que podemos entender o algoritmo de Gram-Schmidt como uma ortonormalização por matrizes triangulares

$$AR_{1}R_{2.}..R_{n} = \widehat{Q}$$ $$R_{1}R_{2.}..R_{n} = R^{- 1}$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Algoritmo de Gram-Schmidt Modificado](../algoritmo-de-gram-schmidt-modificado/index.md)
- Próximo: [Triangularização de Householder](../../triangularizacao-de-householder/index.md)
