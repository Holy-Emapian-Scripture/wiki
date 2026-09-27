---
layout: "default"
title: "Otimização com restrições lineares"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 12
---

[Otimização para Ciência de Dados](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-17"></a>

# Otimização com restrições lineares


<a id="condicoes-kkt"></a>
<a id="secao-18"></a>

## Condições KKT

<a id="kkt-linear-conditions"></a>

**Teorema: Condições KKT para restrições lineares: condições necessárias de otimalidade**

Considere o problema de minimização [\[optimization-with-linear-conditions\]](../index.md#optimization-with-linear-conditions) onde $f$ é uma função continuamente diferenciável em ${\mathbb{R}}^{n}$, $\left\{ a_{i} \right\}_{i = 1}^{m} \subset {\mathbb{R}}$ e $\left\{ b_{i} \right\}_{i = 1}^{m} \subset R$. Então, **se** $x^{\ast}$ é um ponto de **mínimo local** do problema, $\exists\lambda_{1},...,\lambda_{m} \geq 0$ tais que $$\begin{array}{r} \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}a_{i} = 0, \\ \lambda_{i}\left( a_{i}^{T}x^{\ast} - b_{i} \right) = 0,\text{\quad\quad}i = 1,\ldots,m \\ a_{i}^{T}x^{\ast} - b_{i} \leq 0,\text{\quad\quad}i = 1,\ldots,m \end{array}$$

Como esse teorema necessita de vários outros resultados, não vou escrever a sua demonstração aqui. Se estiver curioso para saber a demonstração, confira o apêndice das anotações do Phillip

<a id="condicoes-kkt-problema-convexo"></a>
<a id="secao-19"></a>

## Condições KKT: Problema convexo

<a id="kkt-convex-conditions"></a>

**Teorema: Condições KKT para restrições lineares: condições necessárias de otimalidade com função convexa**

Considere o problema de minimização $$\begin{array}{r} \min\limits_{x}f(x) \\ \text{sujeito à }a_{i}^{T}x \leq b_{i},i = 1,\ldots,m \end{array}$$ onde $f$ é uma função continuamente diferenciável **convexa** em ${\mathbb{R}}^{n}$ $\left\{ a_{i} \right\}_{i = 1}^{m} \subset {\mathbb{R}} \land \left\{ b_{i} \right\}_{i = 1}^{m} \subset R$. Então, se $x^{\ast}$ é um ponto de mínimo local do problema $\Leftrightarrow \exists\lambda_{1},...,\lambda_{m} \geq 0$ tais que $$\begin{array}{r} \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}a_{i} = 0, \\ \lambda_{i}\left( a_{i}^{T}x^{\ast} - b_{i} \right) = 0,\text{\quad\quad}i = 1,\ldots,m \\ a_{i}^{T}x^{\ast} - b_{i} \leq 0,\text{\quad\quad}i = 1,\ldots,m \end{array}$$

**Demonstração**

$( \Longrightarrow )$ Segue do [\[kkt-linear-conditions\]](../condicoes-kkt/index.md#kkt-linear-conditions)

$( \Longleftarrow )$ Definamos a função: $$h(x) ≔ f(x) + \sum_{i = 1}^{m}\lambda_{i}\left( a_{i}^{T}x - b_{i} \right)$$ Temos que: $$\nabla h\left( x^{\ast} \right) = \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}a_{i}$$ Como $h$ é convexa (Soma de funções convexas), segue que $x^{\ast}$ é ponto mínimo de $h$ em ${\mathbb{R}}^{n}$. Em particular, dado qualquer $x \in {\mathbb{R}}^{n}$ tal que: $$a_{i}^{T}x \leq b_{i},\ i = 1,\ldots,m$$ Tem-se que: $$\begin{array}{r} f\left( x^{\ast} \right) = f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}\left( a_{i}^{T}x - b_{i} \right) \\ \leq f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}\left( a_{i}^{T}x - b_{i} \right) \\ \leq f(x) \end{array}$$ Na primeira equação utilizamos a segunda condição e na segunda desigualdade usamos o fato que $\lambda_{i} \geq 0$. Concluímos então que $x^{\ast}$ é solução do sistema

<a id="condicoes-kkt-com-restricoes-lineares-de-igualdade"></a>
<a id="secao-20"></a>

## Condições KKT com restrições lineares de igualdade

Show! Vimos as restrições afins de **desigualdade**, porém, em alguns casos, é possível que tenhamos restrições de igualdade: $$\begin{array}{r} \min\limits_{x}f(x) \\ x\text{ sujeito a restrições do tipo}: \\ a_{i}^{T}x \leq b_{i},\ i = 1,\ldots,m \\ c_{j}^{T}x = d_{j},\ j = 1,\ldots,p \end{array}$$<a id="optimization-with-linear-equality-conditions"></a>

onde $f$ é continuamente diferenciável em ${\mathbb{R}}^{n},\ \left\{ a_{i} \right\}_{i = 1}^{m} \subset {\mathbb{R}}^{n},\left\{ b_{i} \right\}_{i = 1}^{m} \subset {\mathbb{R}},\left\{ c_{j} \right\}_{j = 1}^{p} \subset {\mathbb{R}}^{n}$

Esse caso é o que costumamos aprender em cálculo dois como o **método de Lagrange**, porém vamos ver que esse método é **bem** mais geral do que viamos antes. Do problema que estabelecemos antes, segue um teorema bem parecido com [\[kkt-linear-conditions\]](../condicoes-kkt/index.md#kkt-linear-conditions)

**Teorema**

Considere o problema [\[optimization-with-linear-equality-conditions\]](#optimization-with-linear-equality-conditions), onde $f$ é continuamente diferenciável em ${\mathbb{R}}^{n},\ \left\{ a_{i} \right\}_{i = 1}^{m} \subset {\mathbb{R}}^{n},\left\{ b_{i} \right\}_{i = 1}^{m} \subset {\mathbb{R}},\left\{ c_{j} \right\}_{j = 1}^{p} \subset {\mathbb{R}}^{n}$. Então:

a\) Se $x^{\ast}$ é um ponto de mínimo local do problema, então existem $\lambda_{1},\ldots,\lambda_{m} \geq 0$ e $\mu_{1},\ldots,\mu_{p} \in {\mathbb{R}}$ tais que $$\begin{array}{r} \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}a_{i} + \sum_{j = 1}^{p}\mu_{j}c_{j} = 0 \\ \lambda_{i}\left( a_{i}^{T}x^{\ast} - b_{i} \right) = 0,\ i = 1,\ldots,m \\ a_{i}^{T}x^{\ast} - b_{i} \leq 0,\ i = 1,\ldots,m \\ \mu_{j}\left( c_{j}^{T}x^{\ast} - d_{j} \right) = 0,\ j = 1,\ldots,p \end{array}$$<a id="kkt-with-linear-equalities-conditions"></a>

b\) Suponha adicionalmente que $f$ é convexa, então $x^{\ast}$ é um mínimo global do problema $\Leftrightarrow$ existem $\lambda_{1},\ldots,\lambda_{m} \geq 0$ e $\mu_{1},\ldots,\mu_{p} \in {\mathbb{R}}$ tais que as condições [\[kkt-with-linear-equalities-conditions\]](#kkt-with-linear-equalities-conditions) ainda valem

**Demonstração**

Primeiro demonstraremos o (a). Demonstrar essa parte é equivalente a resolver o problema: $$\begin{array}{r} \min\limits_{x}f(x) \\ x\text{ sujeito a restrições do tipo }a_{i}^{T}x \leq b_{i},\ i = 1,\ldots,m \\ \ c_{j}^{T}x \leq d_{j} \land - c_{j}^{T}x \leq - d_{j},\ j = 1,\ldots,p \end{array}$$ onde $f$ é continuamente diferenciável em ${\mathbb{R}}^{n},\ \left\{ a_{i} \right\}_{i = 1}^{m} \subset {\mathbb{R}}^{n},\left\{ b_{i} \right\}_{i = 1}^{m} \subset {\mathbb{R}},\left\{ c_{j} \right\}_{j = 1}^{p} \subset {\mathbb{R}}^{n}$

Sendo $x^{\ast}$ uma solução do problema descrito anteriormente, pelo [\[kkt-linear-conditions\]](../condicoes-kkt/index.md#kkt-linear-conditions), temos: $$\begin{array}{r} \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}a_{i} + \sum_{j = 1}^{p}\mu_{j}^{+}c_{j} - \sum_{j = 1}^{p}\mu_{j}^{-}c_{j} = 0 \\ \lambda_{i}\left( a_{i}^{T}x^{\ast} - b_{i} \right) = 0 \\ \mu_{j}^{+}\left( c_{j}^{T}x^{\ast} - d_{j} \right) = 0 \\ \mu_{j}^{-}\left( - c_{j}^{T}x^{\ast} + d_{j} \right) = 0 \end{array}$$<a id="kkt-equality-gradient-equivalent"></a>

Como $x^{\ast}$ é viável, então as segundas e terceiras condições mencionadas na reformulação anterior são satisfeitas. Definindo então $\mu_{j} = \mu_{j}^{+} - \mu_{j}^{-}$, então temos que $$\sum_{j = 1}^{p}\mu_{j}^{+}c_{j} - \sum_{j = 1}^{p}\mu_{j}^{-}c_{j} = \sum_{j = 1}^{p}\mu_{j}c_{j}$$. Então segue que as condições estabelecidas originalmente no teorema são satisfeitas

Para a demonstração de (b), Suponha que $x^{\ast}$ viável e existem $\lambda_{1},\ldots,\lambda_{m} \geq 0$ e $\mu_{1},\ldots,\mu_{p} \in {\mathbb{R}}$ tais que as condições do teorema sejam satisfeitas. Defina $$\mu_{j}^{+} ≔ \left( \mu_{j} \right)_{+} = \max\left\{ \mu_{j},0 \right\},\text{\quad\quad}\mu_{j}^{-} ≔ \left( \mu_{j} \right)_{-} = \max\left\{ - \mu_{j},0 \right\}$$ Como $\mu_{j} = \mu_{j}^{+} - \mu_{j}^{-}$ e $c_{j}^{T}x^{\ast} - d_{j} = 0$ para $j \in \lbrack p\rbrack$, segue em particular que [\[kkt-equality-gradient-equivalent\]](#kkt-equality-gradient-equivalent) é satisfeito. Sendo $f$ convexa, segue do [\[kkt-convex-conditions\]](../condicoes-kkt-problema-convexo/index.md#kkt-convex-conditions) que $x^{\ast}$ é solução do problema reformulado e, em particular, do problema original do teorema

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Otimização Convexa](../otimizacao-convexa/index.md)
- Próximo: [Otimização com restrições genéricas](../otimizacao-com-restricoes-genericas/index.md)
