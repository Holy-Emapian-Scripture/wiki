---
layout: "default"
title: "Continuous Random variables"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1_recap.md"
trilha: "../../../trilhas/probabilidade/a1-anterior.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 12
---

[Probabilidade](index.md)

<!-- wiki:original:inicio -->

<a id="secao-22"></a>

# Continuous Random variables


<a id="secao-23"></a>

## Fundamentals

A random variable $X:\Omega \rightarrow {\mathbb{R}}$ is said to be **continuous** if $\Omega$ is uncountable,

This is equivalent to the possible outcomes to the random experiment performed being infinite, such as choosing a **real** number in (0,1).

A continious random variable has some interesting properties, such as the PMF being constant = 0,

To see why this is true, let $X$ be a c.r.v. We know by the naive definition of probability that $P(X = k)$ is “the occurences of k in the support of X divided by the size of the sample space”. But $\vert \Omega\vert  \notin {\mathbb{R}}$! ($= \infty$), therefore $P(X = k) = 0,\forall k \in {\mathbb{R}}$!

We now proceed with new concepts and a definition:

<a id="secao-24"></a>

### Definition

A random variable $X:\Omega \rightarrow {\mathbb{R}}$ is said to be **continuous** if its CDF is differentiable.

<a id="secao-25"></a>

### PDF, CDF of a c.r.v

Let $X:\Omega \rightarrow {\mathbb{R}}$ be a c.r.v with a differentiable $F:{\mathbb{R}} \rightarrow \lbrack 0,1\rbrack$ CDF, analyzing $P(X = k)$ is a waste of time, instead we use the **PDF - Probability Density Function**: The density $f:{\mathbb{R}} \rightarrow {\mathbb{R}}$ in $a$ is, for $\varepsilon \in {\mathbb{R}}^{+}$:

$$
f(a) = \lim\limits_{\varepsilon \rightarrow 0}\frac{P(a \leq X \leq a + \varepsilon)}{\varepsilon} = \lim\limits_{\varepsilon \rightarrow 0}\frac{P(X \leq a + \varepsilon) - P(X \leq a)}{\varepsilon} = F'(a)
$$

This is rather useful because it yields an impressive result from calculus” fundamental theorem:

$$
P(a \leq X \leq b) = F(b) - F(a) = \int_{a}^{b}f(x)dx
$$

Now calculating probabilities continously has been reduced to integrating a ${\mathbb{R}} \rightarrow {\mathbb{R}}$ function, which is not so hard.

<a id="secao-26"></a>

### Cauchy distribution

A c.r.v $X:\Omega \rightarrow {\mathbb{R}}$ has the **Cauchy Distribution** if its PDF has the form:

$$
f(x) = \frac{c}{1 + x^{2}},c \in {\mathbb{R}}
$$

<a id="secao-27"></a>

### Functions of Continuous Random variables

Given $X:\Omega \rightarrow {\mathbb{R}}$ a c.r.v $f(x)\text{ and }F(X)$ its PDF and CDF, in that order, finding the PDF and CDF of $Y:\Omega \rightarrow {\mathbb{R}},Y = h(X),h:{\mathbb{R}} \rightarrow {\mathbb{R}}$ is not so hard.

See that $Y \leq y \Leftrightarrow h(X) \leq y$, and the right part can be solved for $X \in I$, for some interval $I \subset {\mathbb{R}}$, so Y’s CMF is:

$$
G(Y) = P(Y \leq y) = P(X \in I)
$$

With $G$ in hands, it is easy to calculate $g(y) = G'(y)$.

**Example:**

Let $X:\Omega \rightarrow {\mathbb{R}}$ have a uniform distribution in $\lbrack 0,1\rbrack$ ($F(X) = x,\forall x \in \lbrack 0,1\rbrack$), calculate the PMF and CMF of $Y = \sqrt{X}$.

Solution:

We know that for $y \in (0,1)$, $Y \leq y \Leftrightarrow \sqrt{X} \leq y \Leftrightarrow X < y^{2}$, and since $P(X \leq x) = x$;

$$
\begin{array}{r} G(y) = P(Y \leq y) = P\left( X \leq y^{2} \right) = y^{2},\text{ and} \\ g(y) = G'(y) = 2y\text{ is the PDF}, \end{array}
$$

Now we can move to the Expected Value and Variance of a c.r.v.

<a id="secao-28"></a>

### Expected value and variance of a c.r.V

As in the discrete case we had $\mu = E(X) = \sum_{\varphi = - \infty}^{\infty}\varphi P(X = \varphi)$, in the continous case, the $\sum$ becomes and $\int$, and we use the fact that $P(X = k) \sim f(k)$, so:

$$\mu = E(X) = \int_{- \infty}^{\infty}\varphi f(\varphi)d\varphi.$$ Everything you know about $E(X)$ for a discrete r.v $X$ is valid for the discrete case, just switch the $\sum$ for $\int$.

For the variance, we had $V(X) = E\left( \left\lbrack X - \mu^{2} \right\rbrack \right)$ in the discrete case, and the continuous case is:

$$
V(X) = E\left( \lbrack X - \mu\rbrack^{2} \right) = \int_{- \infty}^{\infty}(\varphi - \mu)^{2}f(\varphi)d\varphi.
$$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../trilhas/probabilidade/a1-anterior.md) · [Apresentação e contexto da fonte](../../trilhas/probabilidade/a1-anterior.md#apresentacao-original)

- Anterior: [Poisson](discrete-distributions.md#poisson)
