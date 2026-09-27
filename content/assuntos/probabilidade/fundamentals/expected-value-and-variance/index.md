---
layout: "default"
title: "Expected Value and Variance — Fundamentals"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1_recap.md"
trilha: "../../../../trilhas/probabilidade/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 4
---

[Probabilidade](../../index.md) · [Fundamentals](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Expected Value and Variance

The expected value of a discrete random variable can be seen as a weighted sum of all possible values of $X$:

$$E(X) ≔ \sum_{\varphi \in {\mathbb{R}}}\varphi P(X = \varphi)$$

The most useful fact about indicator random variables is that the expected value of a i.r.v is the **probability** of the event at stake:

$$E\left( I_{A} \right) = P(A).$$

This is **very** useful to determine hard to calculate probabilities.

Functions of real variables are useful as well and derive a famous result, known as the **Law of the Unconscious Statistician (LOTUS)**:

Let $X,Y:\Omega \rightarrow {\mathbb{R}}$ be random variables and $Y = f(X),f:{\mathbb{R}} \rightarrow {\mathbb{R}}$, then:

$$E(Y) = \sum_{\varphi \in {\mathbb{R}}}f(\varphi)P(X = \varphi)$$

The Expected Value is a linear function and has the following properties:

$$\begin{array}{r} E(aX + b) = aE(X) + b \\ E(X + Y) = E(X) + E(Y) \end{array}$$ and if $X$ and $Y$ are independent,

$$E(XY) = E(X)E(Y).$$

A good method to quantify the behaviour of a r.v is using its **standard deviation**:

$$\text{SD}(X) = E\left( \vert X - E(X)\vert  \right)$$ and the **variance** and **mean deviation**:

$$\begin{array}{r} V(X) = E\left( \left\lbrack X - E(X) \right\rbrack^{2} \right) \\ \sigma(X) = \sqrt{V(X)}. \end{array}$$

The variance of a r.v has some properties too:

$$\begin{array}{r} V(aX + b) = a^{2}V(X) \\ \sigma(aX + b) = \vert a\vert \sigma(X) \\ \text{SD}(aX + b) = \vert a\vert \text{SD}(X) \end{array}$$ and if $X$ and $Y$ are independent:

$$V(X + Y) = V(X) + V(Y)$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Discrete Random Variables, Indicator Random Variables](../discrete-random-variables-indicator-random-variables/index.md)
- Próximo: [Covariance, Correlation](../covariance-correlation/index.md)
