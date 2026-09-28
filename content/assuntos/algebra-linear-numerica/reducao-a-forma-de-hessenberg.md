---
layout: "default"
title: "Redução à forma de Hessenberg"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 32
---

[Álgebra Linear Numérica](index.md)

<!-- wiki:original:inicio -->

<a id="secao-32"></a>

# Redução à forma de Hessenberg


<a id="secao-33"></a>

## Uma ideia de Girico

A gente pode começar pensando “Macho, essa fatoração é mamão com açúcar, só eu multiplicar pelo refletor de [Householder](triangularizacao-de-householder.md) que eu vou ter 0 abaixo da diagonal que eu quiser”. Só que isso tem um problema, a gente precisa que o refletor multiplique de ambos os lados, ou seja: $$Q_{1}^{\ast}AQ_{1}$$ Isso faz com que os zeros que a gente colocou antes se percam, e a gente obtem uma matriz que a gente não queria :(.

<a id="secao-34"></a>

## Uma boa ideia

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

<a id="secao-35"></a>

## Hermitiana

É bem tranquilo de ver que o [algoritmo de redução de Householder à forma de Hessenberg](#householder-reduction-to-hessenberg-form) gera uma matriz tri-diagonal no caso em que $A$ é hermitiana, já que $QAQ^{\ast}$ é hermitiana. Inclusive, essa propriedade pose gerar uma redução de custo, tendo em vista que podemos realizar as operações apenas da diagonal para cima, ignorando a parte de baixo das operações.

<a id="secao-36"></a>

## Estabilidade

Assim como o algoritmo de Householder, para a [fatoração QR](fatoracao-qr.md), esse algoritmo é **backward stable**. Seja $\widetilde{H}$ a matriz de Hessenberg computada pelo computador ideal, $\widetilde{Q}$ seja a matriz exatamente unitária que reflete os vetores $v_{k}$, então o resultado a seguir pode ser demonstrado:

<a id="householder-stability-and-precision"></a>

**Teorema**

Deixe a redução de Hessenberg $A = QTQ^{\ast}$ de uma matriz $A$ ser computada pelo [algoritmo de redução de Householder à forma de Hessenberg](#householder-reduction-to-hessenberg-form) em um computador ideal e sejam as matrizes $\widetilde{Q}$ e $\widetilde{H}$ definidas como falamos anteriormente, então: $$\widetilde{Q}\widetilde{H}{\widetilde{Q}}^{\ast} = A + \delta A,\text{ tal que  }\frac{\|\delta A\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$ para algum $\delta A \in {\mathbb{C}}^{m \times m}$

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Algoritmos de Autovalores](algoritmos-de-autovalores.md)
- Próximo: [Quociente de Rayleigh e Iteração Inversa](quociente-de-rayleigh-e-iteracao-inversa.md)
