---
layout: "default"
title: "Poisson — Discrete Distributions"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1_recap.md"
trilha: "../../../../trilhas/probabilidade/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 11
---

[Probabilidade](../../index.md) · [Discrete Distributions](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-19"></a>

# Poisson 

<a id="secao-20"></a>

## Story

The Poisson distribution is often used in situations where we are counting the number of successes in a particular region or interval of time, and there are a large number of trials, each with a small probability of success. For example, the following random variables could follow a distribution that is approximately Poisson.

- The number of emails you receive in an hour, There are a lot of people who could potentially email you in that hour, but it is unlikely that any specifc person will actually email you in that hour.

- The number of chips in a chocolate chip cookie. Imagine subdividing the cookie into small cubes; the probability of getting a chocolate chip in a single cube is small, but the number of cubes is large.

- The number of earthquakes in a year in some region of the world. At any given time and location, the probability of an earthquake is small, but there are a large number of possible times and locations for earthquakes to occur over the course of the year.

Now we move to:

<a id="secao-21"></a>

## PMF, Expected Value and Variance

IF $X:\Omega \rightarrow {\mathbb{R}}$ is $X \sim \text{Pois}(\lambda)$ with parameter $\lambda$, then the following hold:

$$\begin{array}{r} P(X = k) = \frac{e^{- \lambda}\lambda^{k}}{k!} \\ E(X) = \sum_{\varphi \in {\mathbb{R}}}\varphi P(X = \varphi) = \sum_{\varphi \in {\mathbb{R}}}\varphi\frac{e^{- \lambda}\lambda^{\varphi}}{\varphi!} \\ = e^{- \lambda}\sum_{\varphi \in {\mathbb{R}}}\frac{\varphi\lambda^{\varphi}}{\varphi!} = \lambda e^{- \lambda}\sum_{\varphi \in {\mathbb{R}}}\frac{\lambda^{\varphi - 1}}{(\varphi - 1)!} = \lambda e^{- \lambda}e^{\lambda} = \lambda. \\ V(X) = E\left( X^{2} \right) - \left\lbrack E(X) \right\rbrack^{2} = \lambda(1 + \lambda) - \lambda^{2} = \lambda. \end{array}$$

The conclusion $E\left( X^{2} \right) = \lambda(1 + \lambda)$ is not trivial, but it is true.

We now proceed to continuous random variables,

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Hypergeometric](../hypergeometric/index.md)
- Próximo: [Continuous Random variables](../../continuous-random-variables/index.md)
