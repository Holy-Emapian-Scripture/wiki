---
layout: "default"
title: "Covariance, Correlation — Fundamentals"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1_recap.md"
trilha: "../../../../trilhas/probabilidade/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 5
---

[Probabilidade](../../index.md) · [Fundamentals](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Covariance, Correlation

We will go straight to the definition:

The **Covariance** of $X,Y:\Omega \rightarrow {\mathbb{R}}$ is:

$$\text{Cov}(X,Y) = E\left( \left\lbrack X - E(X)\left( Y - E(Y) \right) \right\rbrack \right)$$

This is the same as $\text{Cov}(X) = E(XY) - E(X)E(Y)$, so the idea behind this concept is to measure how both random variables change, when analyzed together. Notice that $\text{Cov}(X,Y) = 0$ if $X$ and $Y$ are independent, this is intuitive

Another useful concept is the **correlation coefficient:**

$$\rho(X,Y) = \frac{\text{Cov}(X,Y)}{\sigma(X)\sigma(Y)}$$ You can verify that $\rho(aX,bY) = \rho(X,Y),\forall a,b \in {\mathbb{R}}$, so the units used to measure $X,Y$ are irrelevant to their correlation coefficient.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Expected Value and Variance](../expected-value-and-variance/index.md)
- Próximo: [Discrete Distributions](../../discrete-distributions/index.md)
