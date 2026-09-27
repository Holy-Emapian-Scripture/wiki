---
layout: "default"
title: "Vector Calculus"
tipo: "conteudo"
disciplina: "Cálculo Vetorial"
origem: "3 semestre/Cálculo Vetorial/Recaps/A1_recap.md"
trilha: "../../../trilhas/calculo-vetorial/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 8
---

[Cálculo Vetorial](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-8"></a>

# Vector Calculus


<a id="centroid-and-mass-center-of-a-curve"></a>
<a id="secao-11"></a>

## Centroid and Mass Center of a Curve

<a id="secao-12"></a>

### Mass Cernter

Given $\gamma \subset {\mathbb{R}}^{3}$ a curve, and let $f(x,y,z)$ be the mass density per unit of lenght of $\gamma$, we know that the $\gamma$‘s mass is given by:

$$
M = \int_{\gamma}f(x,y,z)ds.
$$

So the mass center of $\gamma$ is the point $c_{m} = \left( x_{c},y_{c},z_{c} \right)$ s.t:

$$
\begin{array}{r} x_{c} = \frac{\int_{\gamma}xf(x,y,z)ds}{M} \\ y_{c} = \frac{\int_{\gamma}yf(x,y,z)ds}{M} \\ z_{c} = \frac{\int_{\gamma}zf(x,y,z)ds}{M} \end{array}
$$

If $f$ is constant (homogeneous curve), then the mass center is the centroid as well

<a id="secao-13"></a>

### Centroid

Let $\gamma \subset {\mathbb{R}}^{3}$ be a smooth or piecewise smooth curve, parameterized by $\gamma(t):\lbrack a,b\rbrack \rightarrow {\mathbb{R}}^{3}$. If the curve is **homogeneous**, meaning the mass density per unit length is constant, then its **centroid** is the point $\left( x_{c},y_{c},z_{c} \right)$ given by:

$$
\begin{array}{r} x_{c} = \frac{1}{L}\int_{\gamma}xds \\ y_{c} = \frac{1}{L}\int_{\gamma}yds \\ z_{c} = \frac{1}{L}\int_{\gamma}zds \end{array}
$$

Where $L$ is the total arc length of the curve:

$$
L = \int_{\gamma}ds = \int_{a}^{b}\|\gamma'(t)\| dt
$$

<a id="conservative-vector-fields-and-angle-variation"></a>
<a id="secao-15"></a>

## Conservative Vector Fields and Angle Variation

<a id="secao-16"></a>

### Foreword

We have been trained in the mysterious and dark arts of newtonian and lagrangian mechanics by Master Paulo Verdasca Amorim himself, this is nothing to us.

<a id="secao-17"></a>

### Conservative Vector Fields

A field $F:\Omega \subset {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}$, $\Omega$ an open and connected set, is said to be conservative if $\exists U:\Omega \rightarrow {\mathbb{R}}$ s.t $F = \Delta U$, $U$ is called $F$‘s **potential**

**Theorem**: Let $F:\Omega \rightarrow {\mathbb{R}}^{n}$ be a vector field and $f:\Omega \rightarrow {\mathbb{R}}$ be its potential, i.e $F = \Delta f$. Let $A,B \in \Omega$ and $c:\lbrack a,b\rbrack \rightarrow {\mathbb{R}}^{n}$ be a $C^{1}$ by parts curve s.t c(a) = A and c(b) = B, then:

$$\int_{c}F = f(B) - f(A)$$ This looks like Calculus” Fundamental Theorem

<a id="secao-18"></a>

### Angle Variation

We conclude this section on line integrals with a counterexample: a vector field that satisfies $\partial\frac{F_{1}}{\partial}y = \partial\frac{F_{2}}{\partial}x$ but is not conservative.

Let $F(x,y) = \frac{1}{x^{2} + y^{2}}( - y,x)$, defined over ${\mathbb{R}}^{2} \smallsetminus 0$. Note that:

$$
\partial\frac{F_{1}}{\partial}y = \partial\frac{F_{2}}{\partial}x = \frac{y^{2} - x^{2}}{\left( x^{2} + y^{2} \right)^{2}}
$$

So the field meets the symmetry of mixed partials, but $F$ is still not conservative — the domain is not simply connected.

Take the closed curve $c:\lbrack 0,2\pi\rbrack \rightarrow {\mathbb{R}}^{2}$ given by:

$$
c(t) = \left( \cos t,\sin t \right)
$$

Then:

$$
\int_{c}F = \int_{0}^{\left\{ 2\pi \right\}}\left( - \sin t,\cos t \right) \cdot \left( - \sin t,\cos t \right)dt = \int_{0}^{\left\{ 2\pi \right\}}1dt = 2\pi \neq 0
$$

Since the line integral over a closed curve is nonzero, $F$ is not conservative.

<a id="curves"></a>
<a id="secao-9"></a>

## Curves

A Curve is a continuous function $\gamma:\lbrack a,b\rbrack \rightarrow {\mathbb{R}}^{n}$, it is of class $C^{1}$ if $\gamma'$ exists and is continuous in \[a,b\], if $\gamma(a) = \gamma(b)$, the curve is **closed**.

A curve is said to be $C^{1}$ *by parts* if there is a partition of $\lbrack a,b\rbrack$ in a finite number of subintervals such that the curve is $C^{1}$ in each of tese subintervals.

<a id="scalar-line-integrals"></a>
<a id="secao-10"></a>

## Scalar Line Integrals

Given $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ a function and $\gamma:\lbrack a,b\rbrack \rightarrow {\mathbb{R}}^{n}$ a $C^{1}$ class curve in ${\mathbb{R}}^{n}$, the **scalar line integral** of f along $\gamma$ is:

$$
\int_{\gamma}fds = \int_{a}^{b}f\left( \gamma(t) \right)\|\gamma'(y)\| dt
$$

If $\gamma$ is $C^{1}$ *by parts*, we integrate on the $C^{1}$ partition-subintervals and sum each odf the smaller integrals.

<a id="vectorial-line-integrals"></a>
<a id="secao-14"></a>

## Vectorial Line Integrals

Consider now $F:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}$, usually called a *vector field*, and a class $C^{1}$ curve $\gamma:\lbrack a,b\rbrack \rightarrow {\mathbb{R}}^{n}$ in this field.

The integral of F *along* $\gamma$ is:

$$
\int_{\gamma}F = \int_{a}^{b}F\left( \gamma(t) \right)\gamma'(t)dt
$$

This line integral is linear: $\int_{\gamma}(aF + bG) = a\int_{\gamma}F + b\int_{\gamma}G$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/calculo-vetorial/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/calculo-vetorial/a1.md#apresentacao-original)

- Anterior: [Moment of Inertia](../physics/index.md#moment-of-inertia)
- Próximo: [Conservative Vector Fields and Angle Variation](#conservative-vector-fields-and-angle-variation)
