---
layout: "default"
title: "Fundamentals"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1_recap.md"
trilha: "../../../trilhas/probabilidade/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 1
---

[Probabilidade](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-1"></a>

# Fundamentals


<a id="bayes-theorem-and-lotp"></a>
<a id="secao-2"></a>

## Baye’s Theorem and LOTP

Baye’s theorem states that $\forall A,B \subset \Omega$:

$$
P\left( A\vert B \right) = \frac{P\left( B\vert A \right)P(A)}{P(B)}
$$

This follows directly from the **Law of Total Probability(LOTP)**:

$$
P(A) = \sum_{i = 1}^{n}P\left( A\vert B_{i} \right)P\left( B_{i} \right) = \sum_{i = 1}^{n}P\left( A \cap B_{i} \right).
$$

Given $B_{i}$ a partition of $\Omega$.

Notice that the function $P_{C}:\Omega \rightarrow \lbrack 0,1\rbrack$, $P_{C}(A) = P\left( A\vert C \right)$, given $C \subset \Omega$ is also a probability in the same space $E$, so both Baye’s theorem and LOTP assume conditional versions written in terms of $P_{C}$.

<a id="covariance-correlation"></a>
<a id="secao-5"></a>

## Covariance, Correlation

We will go straight to the definition:

The **Covariance** of $X,Y:\Omega \rightarrow {\mathbb{R}}$ is:

$$
\text{Cov}(X,Y) = E\left( \left\lbrack X - E(X)\left( Y - E(Y) \right) \right\rbrack \right)
$$

This is the same as $\text{Cov}(X) = E(XY) - E(X)E(Y)$, so the idea behind this concept is to measure how both random variables change, when analyzed together. Notice that $\text{Cov}(X,Y) = 0$ if $X$ and $Y$ are independent, this is intuitive

Another useful concept is the **correlation coefficient:**

$$\rho(X,Y) = \frac{\text{Cov}(X,Y)}{\sigma(X)\sigma(Y)}$$ You can verify that $\rho(aX,bY) = \rho(X,Y),\forall a,b \in {\mathbb{R}}$, so the units used to measure $X,Y$ are irrelevant to their correlation coefficient.

<a id="discrete-random-variables-indicator-random-variables"></a>
<a id="secao-3"></a>

## Discrete Random Variables, Indicator Random Variables

A **Discrete Random Variable** is a function $X:\Omega \rightarrow {\mathbb{R}}$, with $\text{Im}(X)$ a countable set. A good example is the amount of heads in 4 tosses of a fair coin:

$$
\begin{array}{r} X(HHHH) = 4 \\ X(HTHH) = 3 \\ \ldots \end{array}
$$

The values $X$ for which a random variable assumes positive values have a special name: the **support of X**

$$
\text{supp}(X) ≔ \left\{ \varphi \in {\mathbb{R}}~\vert ~P(X = \varphi) > 0 \right\}
$$

Random variables are very useful in probability, and there is a category of them so useful and ubiquituous that it has its own name:

An **Indicator Random Variable** of $A \subset \Omega$ is $I_{A}:\Omega \rightarrow {\mathbb{R}}$ defined below:

$$
I_{A} = \begin{cases} 1\text{ if A occurs} \\ 0\text{ otherwise,} \end{cases}
$$

This will be of particular use after we define Expected Values:

<a id="expected-value-and-variance"></a>
<a id="secao-4"></a>

## Expected Value and Variance

The expected value of a discrete random variable can be seen as a weighted sum of all possible values of $X$:

$$
E(X) ≔ \sum_{\varphi \in {\mathbb{R}}}\varphi P(X = \varphi)
$$

The most useful fact about indicator random variables is that the expected value of a i.r.v is the **probability** of the event at stake:

$$
E\left( I_{A} \right) = P(A).
$$

This is **very** useful to determine hard to calculate probabilities.

Functions of real variables are useful as well and derive a famous result, known as the **Law of the Unconscious Statistician (LOTUS)**:

Let $X,Y:\Omega \rightarrow {\mathbb{R}}$ be random variables and $Y = f(X),f:{\mathbb{R}} \rightarrow {\mathbb{R}}$, then:

$$
E(Y) = \sum_{\varphi \in {\mathbb{R}}}f(\varphi)P(X = \varphi)
$$

The Expected Value is a linear function and has the following properties:

$$\begin{array}{r} E(aX + b) = aE(X) + b \\ E(X + Y) = E(X) + E(Y) \end{array}$$ and if $X$ and $Y$ are independent,

$$
E(XY) = E(X)E(Y).
$$

A good method to quantify the behaviour of a r.v is using its **standard deviation**:

$$\text{SD}(X) = E\left( \vert X - E(X)\vert  \right)$$ and the **variance** and **mean deviation**:

$$
\begin{array}{r} V(X) = E\left( \left\lbrack X - E(X) \right\rbrack^{2} \right) \\ \sigma(X) = \sqrt{V(X)}. \end{array}
$$

The variance of a r.v has some properties too:

$$\begin{array}{r} V(aX + b) = a^{2}V(X) \\ \sigma(aX + b) = \vert a\vert \sigma(X) \\ \text{SD}(aX + b) = \vert a\vert \text{SD}(X) \end{array}$$ and if $X$ and $Y$ are independent:

$$
V(X + Y) = V(X) + V(Y)
$$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/probabilidade/a1.md#apresentacao-original)

- Próximo: [Covariance, Correlation](#covariance-correlation)
