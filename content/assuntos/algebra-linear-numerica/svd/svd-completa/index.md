---
layout: "default"
title: "SVD completa — SVD"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 9
---

[Álgebra Linear Numérica](../../index.md) · [SVD](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-9"></a>

# SVD completa

Ok, se $v_{j} \in {\mathbb{C}}^{n}$ e $Av_{j} = \sigma_{j}u_{j}$, então $u_{j} \in {\mathbb{C}}^{m}$! Isso significa que, além dos vetores $u$ que adicionamos em $\widehat{U}$, temos mais $m - n$ vetores ortonormais para as colunas de $\widehat{U}$, ao encontrar esses vetores, podemos construir outra matriz $U$ cujas colunas são uma base ortonormal de ${\mathbb{C}}^{m}$, o que significa que a nova matriz $U$ é ortogonal!

$V = \begin{pmatrix} \vert  & & \vert  \\ v_{1} & \ldots & v_{n} \\ \vert  & & ~\vert ~ \end{pmatrix},U = \begin{pmatrix} \vert  & & \vert  \\ u_{1} & \ldots & u_{m} \\ \vert  & & ~\vert ~ \end{pmatrix}$

Legal! Mas e a matriz $\widehat{\Sigma}$? Como ela muda? Bem, queremos manter $V$ e $U$ como queríamos, certo? Bem, o que fizemos foi adicionar colunas a $\widehat{U}$, então, na multiplicação, só precisamos que essas colunas desapareçam, como fazemos isso? Multiplicando por 0! Então, antes, $\widehat{\Sigma}$ era uma matriz quadrada com os valores singulares na diagonal, especificamente, $n$ valores singulares. Se adicionamos $m - n$ vetores em $U$, podemos adicionar $m - n$ zeros em $\widehat{\Sigma}$, então nossa nova multiplicação matricial é

$A = U\Sigma V^{\ast}$

$\begin{pmatrix} \vert  & & \vert  \\ a_{1} & \ldots & a_{n} \\ \vert  & & ~\vert ~ \end{pmatrix} = \begin{pmatrix} \vert  & & \vert  \\ u_{1} & \ldots & u_{m} \\ \vert  & & ~\vert ~ \end{pmatrix}\begin{pmatrix} \sigma_{1} & & \\ & \ddots & \\ & & \sigma_{n} \\ - & 0 & - \\ & \vdots & \end{pmatrix}\begin{pmatrix} - v_{1} - \\ \ldots \\ - v_{n} - \end{pmatrix}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Forma reduzida](../forma-reduzida/index.md)
- Próximo: [Definição formal](../definicao-formal/index.md)
