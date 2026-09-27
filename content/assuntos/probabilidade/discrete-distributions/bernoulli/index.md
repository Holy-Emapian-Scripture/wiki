---
layout: "default"
title: "Bernoulli — Discrete Distributions"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1_recap.md"
trilha: "../../../../trilhas/probabilidade/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 7
---

[Probabilidade](../../index.md) · [Discrete Distributions](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# Bernoulli

<a id="secao-8"></a>

## Story

A random variable $X:\Omega \rightarrow {\mathbb{R}}$ has a **Bernoulli** distribution if we can think about it as an event with two and only two possible outcomes: succes or failure. Ex: Tossing a coin, throwing a 2-sided dice (a fucking coin).

<a id="secao-9"></a>

## PMF, CDF, Expected Value and Variance

A random variable $X:\Omega \rightarrow {\mathbb{R}}$ is said to have a Bernoulli distribution if $\text{supp}(X) ≔ \left\{ v_{1},v_{2} \right\},v_{i} \in {\mathbb{R}}$ and X’s PMF is:

$$\begin{array}{r} P\left( X = \varphi_{1} \right) = p \\ P\left( X = \varphi_{2} \right) = 1 - p \end{array}$$

We write $X \sim \text{Bern}(p)$ with parameter $p$ and say that X describes a Bernoulli Trial, a random experiment with 2 possible outcomes: success or failure.

The Expected value and Variance of X are:

$$\begin{array}{r} E(X) = \sum_{\varphi \in {\mathbb{R}}}\varphi P(X = \varphi) = v_{1}p + v_{2}(1 - p) \\ V(X) = E\left( X^{2} \right) - \left\lbrack E(X) \right\rbrack^{2} = \sum_{\varphi \in {\mathbb{R}}}\varphi^{2}P(X = \varphi) - \left\lbrack v_{1}p + v_{2}(1 - p) \right\rbrack^{2} \\ = v_{1}^{2}p + v_{2}^{2}(1 - p) - \left\lbrack v_{1}p + v_{2}(1 - p) \right\rbrack^{2.} \end{array}$$ **P.S**: In the very common situation where $\text{supp}(X) = \left\{ 1,0 \right\}$, we have $E(X) = p$ and $V(X)$ = np.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Discrete Distributions](../index.md)
- Próximo: [Binomial](../binomial/index.md)
