---
layout: "default"
title: "Hypergeometric — Discrete Distributions"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1_recap.md"
trilha: "../../../../trilhas/probabilidade/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 10
---

[Probabilidade](../../index.md) · [Discrete Distributions](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-16"></a>

# Hypergeometric

<a id="secao-17"></a>

## Story

If we have an urn filled with $w$ white and $b$ black balls, then drawing n balls out of the urn with replacement yields a $\text{Bin}(n,\frac{w}{w + b})$ distribution for the number of white balls obtained in $n$ trials, because the draws are independent Bernoulli trials, each with probability $\frac{w}{w + b}$ of success. If we instead sample without replacement, then the number of white balls follows a **Hypergeometric** distribution. A good example is written below:

**(Communists capture-recapture)**. A forest has $N$ communists. Today, $m$ of the communists are captured, tagged, and released into the wild. At a later date, $n$ communists are recaptured at random. Assume that the recaptured communists are equally likely to be any set of $n$ of the communists, e.g., a communist that has been captured does not learn how to avoid being captured again (how surprising).

By the story of the Hypergeometric, the number of tagged communists in the recaptured sample has the $\text{Hypergeom}(m,N - m,n)$ distribution. The $m$ tagged communists in this story correspond to the white balls and the $N - m$ untagged communists correspond to the black balls. Instead of sampling $n$ balls from the urn, we recapture $n$ communists from the forest.

<a id="secao-18"></a>

## PMF, Expected value and Variance

$X:\Omega \rightarrow {\mathbb{R}}$, $X \sim \text{Hypergeom}(w,b,n)$ has the following:

$$\begin{array}{r} P(X = k) = \frac{\binom{w}{k}\binom{b}{n - k}}{\binom{w + b}{n}} \\ E(X) = np \\ V(X) = npq \end{array}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Geometric](../geometric/index.md)
- Próximo: [Poisson](../poisson/index.md)
