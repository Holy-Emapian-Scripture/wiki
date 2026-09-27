---
layout: "default"
title: "Binomial — Discrete Distributions"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1_recap.md"
trilha: "../../../../trilhas/probabilidade/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 8
---

[Probabilidade](../../index.md) · [Discrete Distributions](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-10"></a>

# Binomial

<a id="secao-11"></a>

## Story

A random variable $X:\Omega \rightarrow {\mathbb{R}}$ has a binomial distribution if we can see it as a **series** of independent Bernoulli trials of same parameter $p$, such as tossing multiple coins, trying a binary experiment multiple times, etc.

<a id="secao-12"></a>

## PMF, CDF, Expected Value and Variance

A random variable $X:\Omega \rightarrow {\mathbb{R}}$ is said to have the Binomial distribution if it can be decomposed as n independent and consecutive Bernouli Trials $X_{i} \sim \text{Bern}(p)$, das ist:

$$X = X_{1} + X_{2} + \ldots + X_{n}$$

So we can see that its PMF and PDF are:

$$\begin{array}{r} P(X = k) = p^{k}(1 - p)^{n - k}\binom{n}{k} \\ P(X \leq k) = \sum_{i = 1}^{k}P(X = k) \end{array}$$

The Expected value and Variance of $X$ are:

$$\begin{array}{r} E(X) = \sum_{\varphi \in {\mathbb{R}}}\varphi P(X = \varphi) = \sum_{\varphi \in {\mathbb{R}}}\varphi p^{\varphi}(1 - p)^{n - \varphi}\binom{n}{\varphi} = np \\ V(X) = E\left( X^{2} \right) - \left\lbrack E(X) \right\rbrack^{2} = \sum_{\varphi \in {\mathbb{R}}}\varphi^{2}P(X = \varphi) = \sum_{\varphi \in {\mathbb{R}}}\varphi^{2}p^{\varphi}(1 - p)^{n - \varphi}\binom{n}{\varphi} - (np)^{2} \\ = npq \end{array}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Bernoulli](../bernoulli/index.md)
- Próximo: [Geometric](../geometric/index.md)
