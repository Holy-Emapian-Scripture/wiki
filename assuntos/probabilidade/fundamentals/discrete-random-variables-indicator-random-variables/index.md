---
layout: "default"
title: "Discrete Random Variables, Indicator Random Variables — Fundamentals"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1_recap.md"
trilha: "../../../../trilhas/probabilidade/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 3
---

[Probabilidade](../../index.md) · [Fundamentals](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-3"></a>

# Discrete Random Variables, Indicator Random Variables

A **Discrete Random Variable** is a function $X:\Omega \rightarrow {\mathbb{R}}$, with $\text{Im}(X)$ a countable set. A good example is the amount of heads in 4 tosses of a fair coin:

$$\begin{array}{r} X(HHHH) = 4 \\ X(HTHH) = 3 \\ \ldots \end{array}$$

The values $X$ for which a random variable assumes positive values have a special name: the **support of X**

$$\text{supp}(X) ≔ \left\{ \varphi \in {\mathbb{R}}~\vert ~P(X = \varphi) > 0 \right\}$$

Random variables are very useful in probability, and there is a category of them so useful and ubiquituous that it has its own name:

An **Indicator Random Variable** of $A \subset \Omega$ is $I_{A}:\Omega \rightarrow {\mathbb{R}}$ defined below:

$$I_{A} = \begin{cases} 1\text{ if A occurs} \\ 0\text{ otherwise,} \end{cases}$$

This will be of particular use after we define Expected Values:

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Baye’s Theorem and LOTP](../bayes-theorem-and-lotp/index.md)
- Próximo: [Expected Value and Variance](../expected-value-and-variance/index.md)
