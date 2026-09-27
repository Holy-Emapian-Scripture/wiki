---
layout: "default"
title: "Fatoração QR"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 20
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-20"></a>

# Fatoração QR


<a id="a-ideia-da-fatoracao-reduzida"></a>
<a id="secao-21"></a>

## A ideia da fatoração reduzida

Seja $\left\{ a_{j} \right\}$ as colunas de $A \in {\mathbb{C}}^{m \times n},\ m \geq n$. Em algumas aplicações, estamos interessados nos espaços das colunas de $A$, ou seja, os espaços sequenciais gerados pelas colunas de $A$:

span$\left\{ a_{1} \right\} \subseteq$ span$\left\{ a_{1},a_{2} \right\} \subseteq$ span$\left\{ a_{1},a_{2},a_{3} \right\} \subseteq \ldots$

Por enquanto, assumiremos que $A$ tem posto completo $n$. Primeiro, queremos obter um conjunto de vetores ortonormais com a seguinte propriedade:

span$\left\{ a_{1},\ldots,a_{j} \right\} =$ span$\left\{ q_{1},\ldots,q_{j} \right\}$ com $j = 1,\ldots,n$

Bem, acho que uma boa ideia para fazer isso é usar vetores tais que possamos expressar $a_{j}$ como uma combinação linear de $\left\{ q_{1},\ldots,q_{j} \right\}$. Isso significa: $$a_{1} = r_{11}q_{1}$$ $$a_{2} = r_{12}q_{1} + r_{22}q_{2}$$ $$\vdots$$ $$a_{n} = r_{1n}q_{1} + r_{2n}q_{2} + \ldots + r_{nn}q_{n}$$

Podemos expressar essas equações como um produto matricial!

$$
\begin{pmatrix} \vert  & \vert  & & \vert  \\ a_{1} & a_{2} & \ldots & a_{n} \\ \vert  & \vert  & & \vert \end{pmatrix} = \begin{pmatrix} \vert  & \vert  & & \vert  \\ q_{1} & q_{2} & \ldots & q_{n} \\ \vert  & \vert  & & \vert \end{pmatrix}\begin{pmatrix} r_{11} & r_{12} & \ldots & r_{1n} \\ & r_{22} & & \vdots \\ & & \ddots & \vdots \\ & & & r_{nn} \end{pmatrix}
$$

Então temos $A = \widehat{Q}\widehat{R}$, onde $Q \in {\mathbb{C}}^{m \times n}$ e $R \in {\mathbb{C}}^{n \times n}$

<a id="existencia-e-unicidade"></a>
<a id="secao-24"></a>

## Existência e unicidade

**Teorema**

Toda $A \in {\mathbb{C}}^{m \times n},\ (m \geq n)$ tem uma fatoração QR completa, portanto também uma fatoração QR reduzida

**Demonstração**

Se rank$(A) = n$, podemos construir a fatoração reduzida usando Gram-Schmidt como fizemos antes. O único problema aqui é se, em algum momento, $v_{j} = a_{j} - \sum_{k = 1}^{j - 1}q_{k}q_{k}^{\ast}a_{j} = 0$ e, portanto, não pode ser normalizado. Se isso acontecer, significa que $A$ não tem posto completo, o que significa que posso escolher qualquer vetor ortogonal que quiser para continuar o processo.

**Teorema**

Cada $A \in {\mathbb{C}}^{m \times n}\ (m \geq n)$ de posto completo tem uma fatoração QR reduzida única $A = \widehat{Q}\widehat{R}$ com $r_{jj} > 0$

**Demonstração**

Sabemos que, se $A$ é de posto completo $\Rightarrow r_{jj} \neq 0$ e, portanto, em cada passo sucessivo $j$, as fórmulas mostradas anteriormente determinam $r_{ij}$ e $q_{j}$ completamente, o único problema é o sinal de $r_{jj}$, uma vez que dizemos $r_{jj} > 0$, esse problema é resolvido

------------------------------------------------------------------------

<a id="fatoracao-qr-completa"></a>
<a id="secao-22"></a>

## Fatoração QR completa

Vai um pouco além. Sabemos que $\left\{ q_{1},\ldots,q_{n} \right\}$ é um conjunto de vetores ortonormais de ${\mathbb{C}}^{m}$, isso significa que temos mais $m - n$ vetores ortonormais aos que tínhamos antes, então podemos criar uma base para ${\mathbb{C}}^{m}$, adicionando esses vetores como colunas de $\widehat{Q}$, temos uma matriz ortogonal $Q$. Mas o que fazemos para $A$ permanecer a mesma? Podemos simplesmente adicionar linhas de 0 abaixo de $\widehat{R}$, criando $R \in {\mathbb{C}}^{m \times n}\ (m \geq n)$, obtendo

$$
A = QR
$$

<a id="ortonormalizacao-de-gram-schmidt"></a>
<a id="secao-23"></a>

## Ortonormalização de Gram-Schmidt

Nossa… a assustadora… Vamos com muita calma. Vimos anteriormente uma maneira de calcular todos os $q_{j}$, vamos relembrar: $$a_{1} = r_{11}q_{1}$$ $$a_{2} = r_{12}q_{1} + r_{22}q_{2}$$ $$\vdots$$ $$a_{n} = r_{1n}q_{1} + r_{2n}q_{2} + \ldots + r_{nn}q_{n}$$ Bem, isso sugere um algoritmo para calcular o próximo $q_{j}$, vamos pensar, temos todos os $a_{j}$, e cada $q_{j}$ precisa dos vetores $\left\{ q_{1},\ldots,q_{j - 1} \right\}$. Bem, podemos ter alguma liberdade aqui! Vamos ver o que acontece quando tentamos calcular $q_{j}$: $$a_{j} = r_{1j}q_{1} + \ldots + r_{jj}q_{j}$$ Vamos isolar $q_{j}$: $$q_{j} = \frac{a_{j} - r_{1j}q_{1} - r_{2j}q_{2} - \ldots - r_{2(j - 1)}q_{j - 1}}{r_{jj}}$$ Bem, isso sugere que $r_{jj}$ é a norma do vetor $a_{j} - \sum_{k = 1}^{j - 1}r_{ij}q_{i}$, mas o que é $r_{ij}$? Lembra da decomposição em fatores ortogonais? Sim, aquela, $v = r + \sum_{i = 1}^{n}q_{i}q_{i}^{\ast}v$. Se trocarmos $v$ por $a_{j}$, temos quase a mesma coisa que definimos anteriormente! $$a_{j} - \sum_{k = 1}^{j - 1}r_{ij}q_{i},\ v - \sum_{i = 1}^{k}q_{i}q_{i}^{\ast}v$$ E você lembra que $r$ é ortogonal a span$\left\{ q_{1},\ldots,q_{k} \right\}$? Isso é exatamente o que $q_{j}$ é! Tudo isso que acabei de dizer sugere que posso definir $r_{ij}$ como $q_{i}^{\ast}a_{j}\ (i \neq j)$. E nosso algoritmo está pronto! Vamos recapitular tudo aqui:

$$
q_{1} = \frac{a_{1}}{\| a_{1}\|_{2}}
$$

$$
q_{2} = \frac{a_{2} - q_{1}q_{1}^{\ast}a_{2}}{\| a_{2} - q_{1}q_{1}^{\ast}a_{2}\|_{2}}
$$

$$
q_{3} = \frac{a_{3} - q_{1}q_{1}^{\ast}a_{3} - q_{2}q_{2}^{\ast}a_{3}}{\| a_{3} - q_{1}q_{1}^{\ast}a_{3} - q_{2}q_{2}^{\ast}a_{3}\|_{2}}
$$

$$
\vdots
$$

$$
q_{n} = \frac{a_{n} - \sum_{i = 1}^{n - 1}q_{i}q_{i}^{\ast}a_{n}}{\| a_{n} - \sum_{i = 1}^{n - 1}q_{i}q_{i}^{\ast}a_{n}\|_{2}}
$$

Escrevendo na forma de um algoritmo:

1.  **para** $j = 1$ **até** $n$

    1.  $v_{j} = a_{j}$

    2.  **para** $i = 1$ **até** $j - 1$

        1.  $r_{ij} = q_{i}^{\ast}a_{j}$

        2.  $v_{j} = v_{j} - r_{ij}q_{i}$

    3.  $r_{jj} = \| v_{j}\|_{2}$

    4.  $q_{j} = \frac{v_{j}}{r_{jj}}$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Projeção em base arbitrária](../projetores/index.md#projecao-em-base-arbitraria)
- Próximo: [Existência e unicidade](#existencia-e-unicidade)
