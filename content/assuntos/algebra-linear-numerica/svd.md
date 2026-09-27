---
layout: "default"
title: "SVD"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 7
---

[Álgebra Linear Numérica](index.md)

<!-- wiki:original:inicio -->

<a id="secao-7"></a>

# SVD


<a id="forma-reduzida"></a>
<a id="secao-8"></a>

## Forma reduzida

Podemos reescrever esta equação como um produto matricial!

$AV = \widehat{U}\widehat{\Sigma}$

Onde

$V = \begin{pmatrix} \vert  & & \vert  \\ v_{1} & \ldots & v_{n} \\ \vert  & & ~\vert ~ \end{pmatrix},\Sigma = \begin{pmatrix} \sigma_{1} & & & \\ & \sigma_{2} & & \\ & & \ddots & \\ & & & \sigma_{n} \end{pmatrix},U = \begin{pmatrix} \vert  & & \vert  \\ u_{1} & \ldots & u_{n} \\ \vert  & & ~\vert ~ \end{pmatrix}$

Isso é conhecido como a fatoração SVD **reduzida**. Podemos ver que $V$ é uma matriz ortogonal quadrada (para $Av_{j}$ ser uma multiplicação válida, $v_{j} \in {\mathbb{C}}^{n}$), então podemos reescrever $A$ como:

$A = \widehat{U}\widehat{\Sigma}V^{\ast}$

<a id="svd-completa"></a>
<a id="secao-9"></a>

## SVD completa

Ok, se $v_{j} \in {\mathbb{C}}^{n}$ e $Av_{j} = \sigma_{j}u_{j}$, então $u_{j} \in {\mathbb{C}}^{m}$! Isso significa que, além dos vetores $u$ que adicionamos em $\widehat{U}$, temos mais $m - n$ vetores ortonormais para as colunas de $\widehat{U}$, ao encontrar esses vetores, podemos construir outra matriz $U$ cujas colunas são uma base ortonormal de ${\mathbb{C}}^{m}$, o que significa que a nova matriz $U$ é ortogonal!

$V = \begin{pmatrix} \vert  & & \vert  \\ v_{1} & \ldots & v_{n} \\ \vert  & & ~\vert ~ \end{pmatrix},U = \begin{pmatrix} \vert  & & \vert  \\ u_{1} & \ldots & u_{m} \\ \vert  & & ~\vert ~ \end{pmatrix}$

Legal! Mas e a matriz $\widehat{\Sigma}$? Como ela muda? Bem, queremos manter $V$ e $U$ como queríamos, certo? Bem, o que fizemos foi adicionar colunas a $\widehat{U}$, então, na multiplicação, só precisamos que essas colunas desapareçam, como fazemos isso? Multiplicando por 0! Então, antes, $\widehat{\Sigma}$ era uma matriz quadrada com os valores singulares na diagonal, especificamente, $n$ valores singulares. Se adicionamos $m - n$ vetores em $U$, podemos adicionar $m - n$ zeros em $\widehat{\Sigma}$, então nossa nova multiplicação matricial é

$A = U\Sigma V^{\ast}$

$\begin{pmatrix} \vert  & & \vert  \\ a_{1} & \ldots & a_{n} \\ \vert  & & ~\vert ~ \end{pmatrix} = \begin{pmatrix} \vert  & & \vert  \\ u_{1} & \ldots & u_{m} \\ \vert  & & ~\vert ~ \end{pmatrix}\begin{pmatrix} \sigma_{1} & & \\ & \ddots & \\ & & \sigma_{n} \\ - & 0 & - \\ & \vdots & \end{pmatrix}\begin{pmatrix} - v_{1} - \\ \ldots \\ - v_{n} - \end{pmatrix}$

<a id="definicao-formal"></a>
<a id="secao-10"></a>

## Definição formal

**Definição**

Dada $A \in {\mathbb{C}}^{m \times n}$ com $m \geq n$, a Decomposição por Valores Singulares de $A$ é:

$A = U\Sigma V^{\ast}$

onde $U \in {\mathbb{C}}^{m \times m}$ é unitária, $V \in {\mathbb{C}}^{n \times n}$ é unitária e $\Sigma \in {\mathbb{C}}^{m \times n}$ é diagonal. Para **conveniência**, denotamos:

$\sigma_{1} \geq \sigma_{2} \geq \sigma_{3} \geq \ldots \geq \sigma_{n}$

Onde $\sigma_{j}$ é a j-ésima entrada de $\Sigma$

Ok, vimos um método intuitivo para ver que toda matriz tem essa decomposição, mas como provamos isso matematicamente?

**Teorema**

Toda matriz $A \in {\mathbb{C}}^{m \times n}$ tem uma decomposição S.V.D

**Demonstração**

Seja $\left\{ v_{j} \right\}$ uma base ortonormal de ${\mathbb{C}}^{n}$, $\left\{ u_{j} \right\}$ uma base ortonormal de ${\mathbb{C}}^{m}$, $Av_{j} = \sigma_{j}u_{j}$, $U_{1}$ e $V_{1}$ matrizes unitárias de colunas $\left\{ u_{j} \right\}$ e $\left\{ v_{j} \right\}$ respectivamente e que, para toda matriz com menos de $m$ linhas e $n$ colunas, a fatoração é válida:

$A = U_{1}SV_{1}^{\ast} \Leftrightarrow U_{1}^{\ast}AV_{1} = S$

Então temos $S = \begin{pmatrix} \sigma_{1} & w^{\ast} \\ 0 & B \end{pmatrix}$ onde $\sigma_{1}$ é $1 \times 1$, $w^{\ast}$ é $1 \times (n - 1)$ e $B$ é $(m - 1) \times (n - 1)$. Beleza, mas o que é $w$? Bem, podemos chegar nesse resultado fazendo algumas manipulações com $\|\begin{pmatrix} \sigma_{1} & w^{\ast} \\ 0 & B \end{pmatrix}\begin{pmatrix} \sigma_{1} \\ w \end{pmatrix}\|_{2}$:

$\|\begin{pmatrix} \sigma_{1} & w^{\ast} \\ 0 & B \end{pmatrix}\begin{pmatrix} \sigma_{1} \\ w \end{pmatrix}\|_{2}^{2} \geq \sigma_{1}^{2} + w^{\ast}w$

O quê? Por que isso é válido? Porque:

$\| Mx\|_{2} \leq \| M\|_{2}\| x\|_{2} \Rightarrow \| M\|_{2} \geq \frac{\| Mx\|_{2}}{\| x\|_{2}}$

Se definirmos $x = \begin{pmatrix} \sigma_{1} \\ w \end{pmatrix}$ e $M = S$, então temos:

$Mx = \begin{pmatrix} \sigma_{1}^{2} + \| w\|^{2} \\ Bw \end{pmatrix} \Rightarrow \| M\|_{2} \geq \frac{\vert \sigma_{1}^{2} + \| w\|^{2}\vert ^{2} + \| Bw\|^{2}}{\sigma_{1}^{2} + \| w\|^{2}}$

Mas observe que o numerador é sempre maior que o denominador, então isso significa

$\frac{\vert \sigma_{1}^{2} + \| w\|^{2}\vert ^{2} + \| Bw\|^{2}}{\sigma_{1}^{2} + \| w\|^{2}} \geq \sigma_{1}^{2} + \| w\|^{2} = \left( \sigma_{1}^{2} + w^{\ast}w \right)^{\frac{1}{2}}\|\begin{pmatrix} \sigma_{1} \\ w \end{pmatrix}\|$

Agora podemos voltar para ver o que é $w$! Bem, agora é fácil! Sabemos que $\| S\|_{2} = \| U_{1}^{\ast}AV_{1}\|_{2} = \| A\|_{2} = \sigma_{1}$ porque $U_{1}$ e $V_{1}$ são ortogonais. Isso significa $\| S\|_{2} \geq \left( \sigma_{1}^{2} + \| w\|^{2} \right)^{\frac{1}{2}} \Rightarrow \sigma_{1} \geq \left( \sigma_{1}^{2} + \| w\|^{2} \right)^{\frac{1}{2}} \Leftrightarrow \sigma_{1}^{2} \geq \sigma_{1}^{2} + \| w\|^{2} \Rightarrow w = 0$.

Pela hipótese indutiva descrita no início da prova, sabemos que $B = U_{2}\Sigma_{2}V_{2}^{\ast}$, então podemos facilmente escrever $A$ como

$A = U_{1}\begin{pmatrix} 1 & 0 \\ 0 & U_{2} \end{pmatrix}\begin{pmatrix} \sigma_{1} & 0 \\ 0 & \Sigma_{2} \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & V_{2}^{\ast} \end{pmatrix}^{\ast}V_{1}^{\ast}$

Isso é uma S.V.D de $A$, usando o caso base de $m = 1$ e $n = 1$, terminamos a prova da existência

<a id="mudanca-de-base"></a>
<a id="secao-11"></a>

## Mudança de base

Dado $b \in {\mathbb{C}}^{m}$, $x \in {\mathbb{C}}^{n}$ e $A \in {\mathbb{C}}^{m \times n},A = U\Sigma V^{\ast}$ podemos obter as coordenadas de $b$ na base das colunas de $U$ e $x$ nas colunas de $V$. Só para lembrar:

**Definição**

Dado $w \in V$ onde $V$ é um Espaço Vetorial, $\exists!x_{1},\ldots,x_{n} \in {\mathbb{C}}$ tal que $w = v_{1}x_{1} + \ldots + v_{n}x_{n}$ onde $\left\{ v_{j} \right\}$ é uma base de $V$. O vetor $\begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix}$, também denotado como $\lbrack w\rbrack_{v}$, é o **vetor de coordenadas** de $w$ na base $v$

Voltando, podemos expressar $\lbrack b\rbrack_{u} = U^{\ast}b$ e $\lbrack x\rbrack_{v} = V^{\ast}x$, mas por quê?

**Teorema**

Dada uma base ortonormal $\left\{ v_{k} \right\}$ de $V$ e $w \in V$, então

$\left( \lbrack w\rbrack_{v} \right)_{j} = v_{j}^{\ast}w$

**Demonstração**

$w = \alpha_{1}v_{1} + \ldots + \alpha_{n}v_{n}$

$v_{j}^{\ast}w = \alpha_{1}v_{j}^{\ast}v_{1} + \ldots + \alpha_{n}v_{j}^{\ast}v_{n}$

Sabendo que $\left\{ v_{j} \right\}$ é uma base ortonormal, o produto $\alpha_{i}v_{j}^{\ast}v_{i}$ é igual a 0 se $j \neq i$ e igual a $\alpha_{i}$ se $j = i$, ou seja:

$v_{j}^{\ast}w = \alpha_{j}$

Ok, agora que lembramos todas essas propriedades, podemos expressar a relação $b = Ax$ em termos de $\lbrack b\rbrack_{u}$ e $\lbrack x\rbrack_{v}$, vamos ver:

$b = Ax \Leftrightarrow U^{\ast}b = U^{\ast}Ax = U^{\ast}U\Sigma V^{\ast}x \Leftrightarrow U^{\ast}b = \Sigma V^{\ast}x$

$\Leftrightarrow \lbrack b\rbrack_{u} = \Sigma\lbrack x\rbrack_{v}$

Então podemos reduzir $A$ à matriz $\Sigma$ e $b$ e $x$ às suas coordenadas nas bases $u$ e $v$

<a id="s-v-d-vs-decomposicao-por-autovalores"></a>
<a id="secao-12"></a>

## S.V.D vs Decomposição por Autovalores

Podemos fazer algo semelhante com a decomposição por autovalores. Dada $A \in {\mathbb{C}}^{m \times m}$ com autovetores linearmente independentes, ou seja, podemos expressar $A = S\Lambda S^{- 1}$ com as colunas de $S$ sendo os autovetores de $A$ e $\Lambda$ sendo uma matriz diagonal com os autovalores de $A$ como entradas.

Definindo $b,x \in {\mathbb{C}}^{m}$ satisfazendo $b = Ax$, podemos escrever:

$\lbrack b\rbrack_{s^{- 1}} = S^{- 1}b$ e $\lbrack x\rbrack_{s^{- 1}} = S^{- 1}x$

Onde estou denotando $s^{- 1}$ como a base expressa pelas colunas de $S^{- 1}$, então a nova expressão expandida é:

$b = Ax \Leftrightarrow S^{- 1}b = S^{- 1}Ax = S^{- 1}S\Lambda S^{- 1}x \Leftrightarrow S^{- 1}b = \Lambda S^{- 1}x$

$\lbrack b\rbrack_{s^{- 1}} = \Lambda\lbrack x\rbrack_{s^{- 1}}$

<a id="propriedades-de-matrizes-com-svd"></a>
<a id="secao-13"></a>

## Propriedades de matrizes com SVD

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


## Conteúdos relacionados

- [Principal Component Analysis — Aprendizado de Máquina](../aprendizado-de-maquina/principal-component-analysis.md)


## Percurso de estudo

[Trilha: A1](../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Normas](normas.md)
- Próximo: [Projetores](projetores.md)
