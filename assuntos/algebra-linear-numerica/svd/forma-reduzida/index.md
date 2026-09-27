---
layout: "default"
title: "Forma reduzida — SVD"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 8
---

[Álgebra Linear Numérica](../../index.md) · [SVD](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-8"></a>

# Forma reduzida

Podemos reescrever esta equação como um produto matricial!

$AV = \widehat{U}\widehat{\Sigma}$

Onde

$V = \begin{pmatrix} \vert  & & \vert  \\ v_{1} & \ldots & v_{n} \\ \vert  & & ~\vert ~ \end{pmatrix},\Sigma = \begin{pmatrix} \sigma_{1} & & & \\ & \sigma_{2} & & \\ & & \ddots & \\ & & & \sigma_{n} \end{pmatrix},U = \begin{pmatrix} \vert  & & \vert  \\ u_{1} & \ldots & u_{n} \\ \vert  & & ~\vert ~ \end{pmatrix}$

Isso é conhecido como a fatoração SVD **reduzida**. Podemos ver que $V$ é uma matriz ortogonal quadrada (para $Av_{j}$ ser uma multiplicação válida, $v_{j} \in {\mathbb{C}}^{n}$), então podemos reescrever $A$ como:

$A = \widehat{U}\widehat{\Sigma}V^{\ast}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [SVD](../index.md)
- Próximo: [SVD completa](../svd-completa/index.md)
