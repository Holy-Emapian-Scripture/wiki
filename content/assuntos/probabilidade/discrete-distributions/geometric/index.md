---
layout: "default"
title: "Geometric — Discrete Distributions"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1_recap.md"
trilha: "../../../../trilhas/probabilidade/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 9
---

[Probabilidade](../../index.md) · [Discrete Distributions](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-13"></a>

# Geometric

<a id="secao-14"></a>

## Story

Still on the Bernoulli universe, suppose we perform a bernoulli trial with parameter $p$ (probability of sucess), and let $X$ be the quantity of experiments performed until the first sucess (inclusive), then we say that $X:\Omega \rightarrow {\mathbb{R}}$ has a **geometric** distribution with parameter $p$.

<a id="secao-15"></a>

## PMF, CDF, Expected value and Variance

The PMF and CDF of $X \sim \text{Geom}(p)$ are: $$\begin{array}{r} P(X = k) = \text{Geom}(p) = p(1 - p)^{k - 1} \\ P(X \leq k) = 1 - P(X > k) = 1 - (1 - p)^{k}. \end{array}$$

Its Expected Value and Variance:

$$\begin{array}{r} E(X) = \sum_{\varphi \in {\mathbb{R}}}\varphi P(X = \varphi) = \sum_{\varphi \in {\mathbb{R}}}\varphi p(1 - p)^{\varphi - 1} = \frac{1}{p} \\ V(X) = E\left( X^{2} \right) - \left\lbrack E(X) \right\rbrack^{2} = \frac{1 - p}{p^{2}} \end{array}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Binomial](../binomial/index.md)
- Próximo: [Hypergeometric](../hypergeometric/index.md)
