---
layout: "default"
title: "Uma boa ideia — Redução à forma de Hessenberg"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 34
---

[Álgebra Linear Numérica](../../index.md) · [Redução à forma de Hessenberg](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-34"></a>

# Uma boa ideia

A gente vai fazer o seguinte: Vamos multiplicar $A$ por um refletor de householder $Q_{1}^{\ast}$ que mantém as duas primeiras linhas inalteradas, ou seja, vamos fazer combinações lineares das duas primeiras linhas de forma que todas as outras fiquem com 0 na primeira entrada, depois, ao multiplicar $Q_{1}^{\ast}A$ por $Q_{1}$, a primeira coluna se mantém **inalterada**: $$\begin{pmatrix} x & x & x & x & x \\ x & x & x & x & x \\ x & x & x & x & x \\ x & x & x & x & x \\ x & x & x & x & x \end{pmatrix} \rightarrow \begin{pmatrix} x & x & x & x & x \\ \mathbf{x} & \mathbf{x} & \mathbf{x} & \mathbf{x} & \mathbf{x} \\ 0 & \mathbf{x} & \mathbf{x} & \mathbf{x} & \mathbf{x} \\ 0 & \mathbf{x} & \mathbf{x} & \mathbf{x} & \mathbf{x} \\ 0 & \mathbf{x} & \mathbf{x} & \mathbf{x} & \mathbf{x} \end{pmatrix} \rightarrow \begin{pmatrix} x & \mathbf{x} & \mathbf{x} & \mathbf{x} & \mathbf{x} \\ x & \mathbf{x} & \mathbf{x} & \mathbf{x} & \mathbf{x} \\ & \mathbf{x} & \mathbf{x} & \mathbf{x} & \mathbf{x} \\ & \mathbf{x} & \mathbf{x} & \mathbf{x} & \mathbf{x} \\ & \mathbf{x} & \mathbf{x} & \mathbf{x} & \mathbf{x} \end{pmatrix}$$

Essa ideia continua a ser repetida para colunas subsequentes. Temos um algoritmo da forma:

<a id="householder-reduction-to-hessenberg-form"></a>

1.  **function** HessenbergReduction($A \in {\mathbb{C}}^{m \times m}$) {

    1.  **for** $k = 1$ **to** $m - 2$

        1.  $x = A_{k + 1:m,k}$

        2.  $v_{k} = \text{ sign}\left( x_{1} \right)\| x\|_{2}e_{1} + x$

        3.  $v_{k} = v_{k}/\| v_{k}\|$

        4.  $A_{k + 1:m,k:m} = A_{k + 1:m,k:m} - 2v_{k}\left( v_{k}^{\ast}A_{k + 1:m,k:m} \right)$

        5.  $A_{1:m,k + 1:m} = A_{1:m,k + 1:m} - 2\left( A_{1:m,k + 1:m}v_{k} \right)v_{k}^{\ast}$

2.  }

*Figura 6. Redução de Householder para forma de Hessenberg*

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Uma ideia de Girico](../uma-ideia-de-girico/index.md)
- Próximo: [Hermitiana](../hermitiana/index.md)
