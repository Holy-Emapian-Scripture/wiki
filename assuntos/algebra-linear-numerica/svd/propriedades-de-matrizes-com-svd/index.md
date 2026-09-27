---
layout: "default"
title: "Propriedades de matrizes com SVD — SVD"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 13
---

[Álgebra Linear Numérica](../../index.md) · [SVD](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-13"></a>

# Propriedades de matrizes com SVD

Para as próximas propriedades, seja $A \in {\mathbb{C}}^{m \times n}$ e $r \leq \min(m,n)$ o número de valores singulares não nulos

**Teorema**

rank$(A) = r$

**Demonstração**

O posto de uma matriz diagonal é o número de entradas não nulas, bem, se $A = U\Sigma V^{\ast}$, sabemos que $U$ e $V$ têm posto completo, então o posto de $A$ deve ser o mesmo que o de $\Sigma$, ou seja, $r$

**Teorema**

$C(A) = \text{ span}\left\{ u_{1},\ldots,u_{r} \right\}$, $C\left( A^{\ast} \right) = \text{ span}\left\{ v_{1},\ldots v_{r} \right\},N(A) = \text{ span}\left\{ v_{r + 1},\ldots,v_{n} \right\},N\left( A^{\ast} \right) = \text{ span}\left\{ u_{r + 1},\ldots,u_{m} \right\}$

**Demonstração**

Vamos lembrar como cada matriz é estruturada:

$A = \begin{pmatrix} \vert  & & \vert  \\ u_{1} & \ldots & u_{m} \\ \vert  & & \vert \end{pmatrix}\begin{pmatrix} \sigma_{1} \\ & \ddots \\ & & \sigma_{r} \\ & & & 0 \\ & & & & \ddots \end{pmatrix}\begin{pmatrix} - v_{1}^{\ast} - \\ \vdots \\ - v_{n}^{\ast} - \end{pmatrix}$

É fácil ver por que $C(A) = \text{ span}\left\{ u_{1},\ldots,u_{r} \right\}$, porque as entradas de $\Sigma$ só permitem abranger as primeiras $r$ colunas de $U$.

Sobre $N(A) = \text{ span}\left\{ v_{r + 1},\ldots,v_{n} \right\}$, observe como, se fizermos $Av_{j}\ r + 1 \leq j \leq n$, as primeiras $r$ linhas se tornarão 0 (todos os $v_{k}$ são ortonormais entre si) e, como as entradas diagonais após a $r$-ésima são 0, então temos $U$ vezes a matriz 0

Para ver as propriedades de $A^{\ast}$, vamos transpor $A$

$A^{\ast} = \begin{pmatrix} \vert  & & \vert  \\ v_{1} & \ldots & v_{n} \\ \vert  & & \vert \end{pmatrix}\begin{pmatrix} \sigma_{1} \\ & \ddots \\ & & \sigma_{r} \\ & & & 0 \\ & & & & \ddots \end{pmatrix}\begin{pmatrix} - u_{1}^{\ast} - \\ \vdots \\ - u_{m}^{\ast} - \end{pmatrix}$

Então, novamente, é fácil ver que $C\left( A^{\ast} \right) = \text{ span}\left\{ v_{1},\ldots v_{r} \right\}$ e, usando o mesmo argumento mostrado antes, $N\left( A^{\ast} \right) = \text{ span}\left\{ u_{r + 1},\ldots,u_{m} \right\}$

**Teorema**

$\| A\|_{2} = \sigma_{1}$ e $\| A\|_{F} = \sqrt{\sigma_{1}^{2} + \ldots + \sigma_{r}^{2}}$

**Demonstração**

1.  $\| A\|_{2} = \| U\Sigma V\|_{2} = \|\Sigma\|_{2}$, como denotamos antes, de todas as entradas, $\sigma_{1}$ é a maior, isso significa $\| A\|_{2} = \|\Sigma\|_{2} = \sigma_{1}$

2.  Sabemos que $\| A\|_{F} = \sqrt{\operatorname{tr}(A^{\ast}A)} = \sqrt{\operatorname{tr}(V\Sigma^{\ast}U^{\ast}U\Sigma V^{\ast})} = \sqrt{\operatorname{tr}(V\Sigma^{\ast}\Sigma V^{\ast})}$. Também sabemos que $\operatorname{tr}(A) = \lambda_{1} + \ldots + \lambda_{n}$ com $\lambda_{j}$ sendo os autovalores de $A$, e podemos ver claramente que os autovalores de $V\Sigma^{\ast}\Sigma V^{\ast}$ são $\sigma_{j}^{2}$, portanto $\| A\|_{F} = \sqrt{\sigma_{1}^{2} + \ldots + \sigma_{r}^{2}}$

**Teorema**

$\sigma_{j} = \sqrt{\lambda_{j}}$ com $\sigma_{j}$ sendo os valores singulares de $A$ e $\lambda_{j}$ os autovalores de $A^{\ast}A$

**Demonstração**

$A^{\ast}A = V\Sigma^{\ast}U^{\ast}U\Sigma V^{\ast} = V\Sigma^{\ast}\Sigma V^{\ast}$

**Teorema**

se $A = A^{\ast}$, então os valores singulares de $A$ são os valores absolutos dos autovalores de $A$

**Demonstração**

Pelo Teorema Espectral, sabemos que $A$ tem uma decomposição por autovalores

$A = Q\Lambda Q^{\ast}$

Podemos reescrevê-la como

$A = Q\vert \Lambda\vert$sign$(\Lambda)Q^{\ast}$

Onde as entradas de $\vert \Lambda\vert$ são $\vert \lambda_{j}\vert$ e as entradas de sign$(\Lambda)$ são sign$\left( \lambda_{j} \right)$. Podemos mostrar que, se $Q$ é unitária, sign$(\Lambda)Q$ é unitária, o que significa que $Q\vert \Lambda\vert$sign$(\Lambda)Q^{\ast}$ é uma SVD de $A$

**Teorema**

Para $A \in {\mathbb{C}}^{m \times m}$, $\vert \det(A)\vert  = \prod_{i = 1}^{m}\sigma_{i}$

**Demonstração**

$\vert \det(A)\vert  = \vert \det(U\Sigma V^{\ast})\vert  = \vert \det(U)\det(\Sigma)\det(V)\vert  = \vert \det(\Sigma)\vert$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [S.V.D vs Decomposição por Autovalores](../s-v-d-vs-decomposicao-por-autovalores/index.md)
- Próximo: [Projetores](../../projetores/index.md)
