---
layout: "default"
title: "Normas"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 1
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-1"></a>

# Normas


<a id="normas-de-vetores"></a>
<a id="secao-2"></a>

## Normas de vetores

**Definição: Norma**

Uma **norma** é uma função $\| \cdot \|:{\mathbb{C}}^{m} \rightarrow {\mathbb{R}}$ que satisfaz 3 propriedades:

1.  $\| x\| \geq 0$, e $\| x\| = 0 \Leftrightarrow x = 0$

2.  $\| x + y\| \leq \| x\| + \| y\|$

3.  $\|\alpha x\| = \vert \alpha\|\vert x\|$

Normalmente vemos a norma-2, ou a **Norma Euclidiana**, que representa o **tamanho** de um vetor. Com base nisso, podemos definir uma **norma-p**.

**Definição: Norma-p**

A **norma-p** de $x \in {\mathbb{C}}^{n}$ (ou $\| x\|_{p}$) é definida como:

$\| x\|_{p} = \left( \sum_{i = 1}^{n}\vert x_{i}\vert ^{p} \right)^{\frac{1}{p}}$

Então, podemos ter vários tipos de normas, de 1 até $\infty$, e também definimos isso!

**Definição: Norma infinita**

A **norma infinita** de $x \in {\mathbb{C}}^{n}$ (ou $\| x\|_{\infty}$) é definida como:

$\| x\|_{\infty} = \max\vert x_{i}\vert$

Você provavelmente está se perguntando “por que eu precisaria de algo assim”? Mas acredite, será útil no futuro! Existe um tipo de norma muito útil (de acordo com o livro), chamada **norma ponderada**.

**Definição: Norma ponderada**

A **norma ponderada** de $x \in {\mathbb{C}}^{n}$ é:

$\| x\|_{W} = \| Wx\| = \left( \sum_{i = 1}^{n}\vert w_{ii}x_{i}\vert ^{p} \right)^{\frac{1}{p}}$

Onde $W$ é uma **matriz diagonal** e $p$ é um número arbitrário

<a id="normas-de-matrizes"></a>
<a id="secao-3"></a>

## Normas de matrizes

O QUÊ?? MATRIZES TÊM NORMAS???? Sim, meu jovem Padawan! O livro diz que podemos ver uma matriz como um vetor em um espaço $m \times n$, e podemos usar qualquer norma $mn$ para medi-la, mas algumas normas são mais úteis do que as já discutidas.

**Definição: Norma induzida**

Dada $A \in {\mathbb{C}}^{m \times n}$, a norma induzida $\| A\|_{m \rightarrow n}$ é o menor inteiro para o qual a desigualdade é válida:

$\| Ax\|_{m} \leq C\| x\|_{n}$

Em outras palavras:

$\| A\|_{m \rightarrow n} = \sup\limits_{x \neq 0}\frac{\| Ax\|_{m}}{\| x\|_{n}}$

Essa definição pode parecer inútil e estúpida por enquanto, mas será muito útil quando falarmos sobre erros e condicionamento.

Uma norma útil que podemos mencionar é a norma $\infty$ de uma matriz.

**Definição: Norma infinita de uma matriz**

Dada $A \in {\mathbb{C}}^{m \times n}$, se $a_{j}$ é a $j^{th}$ linha de $A$, $\| A\|_{\infty}$ é definida por:

$\| A\|_{\infty} = \max\limits_{1 \leq i \leq m}\| a_{i}\|_{1}$

<a id="desigualdades-de-cauchy-schwarz-e-holder"></a>
<a id="secao-4"></a>

## Desigualdades de Cauchy-Schwarz e Hölder

Quando usamos normas, geralmente é difícil calcular normas-p com valores altos de $p$, então as gerenciamos usando desigualdades! Uma desigualdade muito útil é a de Hölder:

**Definição: Desigualdade de Hölder**

Dados $1 \leq p,q \leq \infty$, e $\frac{1}{p} + \frac{1}{q} = 1$, então, para quaisquer vetores $x,y$:

$\vert x^{\ast}y\vert  \leq \| x\|_{p}\| y\|_{q}$

E a desigualdade de Cauchy-Schwarz é um caso especial onde $p = q = 2$.

<a id="limitando-ab"></a>
<a id="secao-5"></a>

## Limitando $\| AB\|$

Podemos limitar $\| AB\|$ como fazemos com normas de vetores.

**Teorema**

Dadas $A \in {\mathbb{C}}^{l \times m}$,$B \in {\mathbb{C}}^{m \times n}$ e $x \in {\mathbb{C}}^{n}$, então a norma induzida de $AB$ deve satisfazer:

$\| AB\|_{l \rightarrow n} \leq \| A\|_{l \rightarrow m}\| B\|_{m \rightarrow n}$

**Demonstração**

$\| ABx\|_{l} \leq \| A\|_{l \rightarrow m}\| Bx\|_{m} \leq \| A\|_{l \rightarrow m}\| B\|_{m \rightarrow n}\| x\|_{n}$

<a id="generalizacao-das-normas-de-matrizes"></a>
<a id="secao-6"></a>

## Generalização das normas de matrizes

Vimos que uma norma segue 3 propriedades, definimos uma norma geral de matriz da mesma forma!!

**Definição**

Dadas as matrizes $A$ e $B$, uma norma $\| \cdot \|:{\mathbb{C}}^{m \times n} \rightarrow {\mathbb{R}}^{+}$ é uma função que segue estas 3 propriedades:

1.  $\| A\| \geq 0$, e $\| A\| = 0 \Leftrightarrow A = 0$

2.  $\| A + A\| \leq \| A\| + \| B\|$

3.  $\|\alpha A\| = \vert \alpha\|\vert A\|$

A mais importante é a **Norma de Frobenius**, definida como:

**Definição**

Dada uma matriz $A \in {\mathbb{C}}^{m \times n}$, sua **Norma de Frobenius** é definida como:

$\| A\|_{F} = \left( \sum_{i = 1}^{m}\sum_{j = 1}^{n}\vert a_{ij}\vert ^{2} \right)^{\frac{1}{2}}$ = $\sqrt{tr\left( A^{\ast}A \right)}$ = $\sqrt{tr\left( AA^{\ast} \right)}$

**Teorema**

$\| AB\|_{F} \leq \| A\|_{F}\| B\|_{F}$

**Demonstração**

$\| AB\|_{F} = \left( \sum_{i = 1}^{m}\sum_{j = 1}^{n}\vert c_{ij}\vert ^{2} \right)^{\frac{1}{2}} \leq \left( \sum_{i = 1}^{m}\sum_{j = 1}^{n}\left( \| a_{i}\|_{2}\| b_{j}\|_{2} \right)^{2} \right)^{\frac{1}{2}} = \left( \sum_{i = 1}^{m}\| a_{i}\|_{2}^{2}\sum_{j = 1}^{n}\| b_{j}\|_{2}^{2} \right)^{\frac{1}{2}} = \| A\|_{F}\| B\|_{F}$

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Próximo: [SVD](../svd/index.md)
