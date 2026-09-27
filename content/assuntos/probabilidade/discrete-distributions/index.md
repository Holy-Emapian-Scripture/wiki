---
layout: "default"
title: "Discrete Distributions"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1_recap.md"
trilha: "../../../trilhas/probabilidade/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 6
---

[Probabilidade](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-6"></a>

# Discrete Distributions


<a id="bernoulli"></a>
<a id="secao-7"></a>

## Bernoulli

<a id="secao-8"></a>

### Story

A random variable $X:\Omega \rightarrow {\mathbb{R}}$ has a **Bernoulli** distribution if we can think about it as an event with two and only two possible outcomes: succes or failure. Ex: Tossing a coin, throwing a 2-sided dice (a fucking coin).

<a id="secao-9"></a>

### PMF, CDF, Expected Value and Variance

A random variable $X:\Omega \rightarrow {\mathbb{R}}$ is said to have a Bernoulli distribution if $\text{supp}(X) ≔ \left\{ v_{1},v_{2} \right\},v_{i} \in {\mathbb{R}}$ and X’s PMF is:

$$
\begin{array}{r} P\left( X = \varphi_{1} \right) = p \\ P\left( X = \varphi_{2} \right) = 1 - p \end{array}
$$

We write $X \sim \text{Bern}(p)$ with parameter $p$ and say that X describes a Bernoulli Trial, a random experiment with 2 possible outcomes: success or failure.

The Expected value and Variance of X are:

$$\begin{array}{r} E(X) = \sum_{\varphi \in {\mathbb{R}}}\varphi P(X = \varphi) = v_{1}p + v_{2}(1 - p) \\ V(X) = E\left( X^{2} \right) - \left\lbrack E(X) \right\rbrack^{2} = \sum_{\varphi \in {\mathbb{R}}}\varphi^{2}P(X = \varphi) - \left\lbrack v_{1}p + v_{2}(1 - p) \right\rbrack^{2} \\ = v_{1}^{2}p + v_{2}^{2}(1 - p) - \left\lbrack v_{1}p + v_{2}(1 - p) \right\rbrack^{2.} \end{array}$$ **P.S**: In the very common situation where $\text{supp}(X) = \left\{ 1,0 \right\}$, we have $E(X) = p$ and $V(X)$ = np.

<a id="binomial"></a>
<a id="secao-10"></a>

## Binomial

<a id="secao-11"></a>

### Story

A random variable $X:\Omega \rightarrow {\mathbb{R}}$ has a binomial distribution if we can see it as a **series** of independent Bernoulli trials of same parameter $p$, such as tossing multiple coins, trying a binary experiment multiple times, etc.

<a id="secao-12"></a>

### PMF, CDF, Expected Value and Variance

A random variable $X:\Omega \rightarrow {\mathbb{R}}$ is said to have the Binomial distribution if it can be decomposed as n independent and consecutive Bernouli Trials $X_{i} \sim \text{Bern}(p)$, das ist:

$$
X = X_{1} + X_{2} + \ldots + X_{n}
$$

So we can see that its PMF and PDF are:

$$
\begin{array}{r} P(X = k) = p^{k}(1 - p)^{n - k}\binom{n}{k} \\ P(X \leq k) = \sum_{i = 1}^{k}P(X = k) \end{array}
$$

The Expected value and Variance of $X$ are:

$$
\begin{array}{r} E(X) = \sum_{\varphi \in {\mathbb{R}}}\varphi P(X = \varphi) = \sum_{\varphi \in {\mathbb{R}}}\varphi p^{\varphi}(1 - p)^{n - \varphi}\binom{n}{\varphi} = np \\ V(X) = E\left( X^{2} \right) - \left\lbrack E(X) \right\rbrack^{2} = \sum_{\varphi \in {\mathbb{R}}}\varphi^{2}P(X = \varphi) = \sum_{\varphi \in {\mathbb{R}}}\varphi^{2}p^{\varphi}(1 - p)^{n - \varphi}\binom{n}{\varphi} - (np)^{2} \\ = npq \end{array}
$$

<a id="geometric"></a>
<a id="secao-13"></a>

## Geometric

<a id="secao-14"></a>

### Story

Still on the Bernoulli universe, suppose we perform a bernoulli trial with parameter $p$ (probability of sucess), and let $X$ be the quantity of experiments performed until the first sucess (inclusive), then we say that $X:\Omega \rightarrow {\mathbb{R}}$ has a **geometric** distribution with parameter $p$.

<a id="secao-15"></a>

### PMF, CDF, Expected value and Variance

The PMF and CDF of $X \sim \text{Geom}(p)$ are: $$\begin{array}{r} P(X = k) = \text{Geom}(p) = p(1 - p)^{k - 1} \\ P(X \leq k) = 1 - P(X > k) = 1 - (1 - p)^{k}. \end{array}$$

Its Expected Value and Variance:

$$
\begin{array}{r} E(X) = \sum_{\varphi \in {\mathbb{R}}}\varphi P(X = \varphi) = \sum_{\varphi \in {\mathbb{R}}}\varphi p(1 - p)^{\varphi - 1} = \frac{1}{p} \\ V(X) = E\left( X^{2} \right) - \left\lbrack E(X) \right\rbrack^{2} = \frac{1 - p}{p^{2}} \end{array}
$$

<a id="hypergeometric"></a>
<a id="secao-16"></a>

## Hypergeometric

<a id="secao-17"></a>

### Story

If we have an urn filled with $w$ white and $b$ black balls, then drawing n balls out of the urn with replacement yields a $\text{Bin}(n,\frac{w}{w + b})$ distribution for the number of white balls obtained in $n$ trials, because the draws are independent Bernoulli trials, each with probability $\frac{w}{w + b}$ of success. If we instead sample without replacement, then the number of white balls follows a **Hypergeometric** distribution. A good example is written below:

**(Communists capture-recapture)**. A forest has $N$ communists. Today, $m$ of the communists are captured, tagged, and released into the wild. At a later date, $n$ communists are recaptured at random. Assume that the recaptured communists are equally likely to be any set of $n$ of the communists, e.g., a communist that has been captured does not learn how to avoid being captured again (how surprising).

By the story of the Hypergeometric, the number of tagged communists in the recaptured sample has the $\text{Hypergeom}(m,N - m,n)$ distribution. The $m$ tagged communists in this story correspond to the white balls and the $N - m$ untagged communists correspond to the black balls. Instead of sampling $n$ balls from the urn, we recapture $n$ communists from the forest.

<a id="secao-18"></a>

### PMF, Expected value and Variance

$X:\Omega \rightarrow {\mathbb{R}}$, $X \sim \text{Hypergeom}(w,b,n)$ has the following:

$$
\begin{array}{r} P(X = k) = \frac{\binom{w}{k}\binom{b}{n - k}}{\binom{w + b}{n}} \\ E(X) = np \\ V(X) = npq \end{array}
$$

<a id="poisson"></a>
<a id="secao-19"></a>

## Poisson 

<a id="secao-20"></a>

### Story

The Poisson distribution is often used in situations where we are counting the number of successes in a particular region or interval of time, and there are a large number of trials, each with a small probability of success. For example, the following random variables could follow a distribution that is approximately Poisson.

- The number of emails you receive in an hour, There are a lot of people who could potentially email you in that hour, but it is unlikely that any specifc person will actually email you in that hour.

- The number of chips in a chocolate chip cookie. Imagine subdividing the cookie into small cubes; the probability of getting a chocolate chip in a single cube is small, but the number of cubes is large.

- The number of earthquakes in a year in some region of the world. At any given time and location, the probability of an earthquake is small, but there are a large number of possible times and locations for earthquakes to occur over the course of the year.

Now we move to:

<a id="secao-21"></a>

### PMF, Expected Value and Variance

IF $X:\Omega \rightarrow {\mathbb{R}}$ is $X \sim \text{Pois}(\lambda)$ with parameter $\lambda$, then the following hold:

$$
\begin{array}{r} P(X = k) = \frac{e^{- \lambda}\lambda^{k}}{k!} \\ E(X) = \sum_{\varphi \in {\mathbb{R}}}\varphi P(X = \varphi) = \sum_{\varphi \in {\mathbb{R}}}\varphi\frac{e^{- \lambda}\lambda^{\varphi}}{\varphi!} \\ = e^{- \lambda}\sum_{\varphi \in {\mathbb{R}}}\frac{\varphi\lambda^{\varphi}}{\varphi!} = \lambda e^{- \lambda}\sum_{\varphi \in {\mathbb{R}}}\frac{\lambda^{\varphi - 1}}{(\varphi - 1)!} = \lambda e^{- \lambda}e^{\lambda} = \lambda. \\ V(X) = E\left( X^{2} \right) - \left\lbrack E(X) \right\rbrack^{2} = \lambda(1 + \lambda) - \lambda^{2} = \lambda. \end{array}
$$

The conclusion $E\left( X^{2} \right) = \lambda(1 + \lambda)$ is not trivial, but it is true.

We now proceed to continuous random variables,

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Fundamentals](../fundamentals/index.md)
- Próximo: [Continuous Random variables](../continuous-random-variables/index.md)
