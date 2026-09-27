---
layout: "default"
title: "Conservative Vector Fields and Angle Variation — Vector Calculus"
tipo: "conteudo"
disciplina: "Cálculo Vetorial"
origem: "3 semestre/Cálculo Vetorial/Recaps/A1_recap.md"
trilha: "../../../../trilhas/calculo-vetorial/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 13
---

[Cálculo Vetorial](../../index.md) · [Vector Calculus](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Conservative Vector Fields and Angle Variation

<a id="secao-16"></a>

## Foreword

We have been trained in the mysterious and dark arts of newtonian and lagrangian mechanics by Master Paulo Verdasca Amorim himself, this is nothing to us.

<a id="secao-17"></a>

## Conservative Vector Fields

A field $F:\Omega \subset {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}$, $\Omega$ an open and connected set, is said to be conservative if $\exists U:\Omega \rightarrow {\mathbb{R}}$ s.t $F = \Delta U$, $U$ is called $F$‘s **potential**

**Theorem**: Let $F:\Omega \rightarrow {\mathbb{R}}^{n}$ be a vector field and $f:\Omega \rightarrow {\mathbb{R}}$ be its potential, i.e $F = \Delta f$. Let $A,B \in \Omega$ and $c:\lbrack a,b\rbrack \rightarrow {\mathbb{R}}^{n}$ be a $C^{1}$ by parts curve s.t c(a) = A and c(b) = B, then:

$$\int_{c}F = f(B) - f(A)$$ This looks like Calculus” Fundamental Theorem

<a id="secao-18"></a>

## Angle Variation

We conclude this section on line integrals with a counterexample: a vector field that satisfies $\partial\frac{F_{1}}{\partial}y = \partial\frac{F_{2}}{\partial}x$ but is not conservative.

Let $F(x,y) = \frac{1}{x^{2} + y^{2}}( - y,x)$, defined over ${\mathbb{R}}^{2} \smallsetminus 0$. Note that:

$$\partial\frac{F_{1}}{\partial}y = \partial\frac{F_{2}}{\partial}x = \frac{y^{2} - x^{2}}{\left( x^{2} + y^{2} \right)^{2}}$$

So the field meets the symmetry of mixed partials, but $F$ is still not conservative — the domain is not simply connected.

Take the closed curve $c:\lbrack 0,2\pi\rbrack \rightarrow {\mathbb{R}}^{2}$ given by:

$$c(t) = \left( \cos t,\sin t \right)$$

Then:

$$\int_{c}F = \int_{0}^{\left\{ 2\pi \right\}}\left( - \sin t,\cos t \right) \cdot \left( - \sin t,\cos t \right)dt = \int_{0}^{\left\{ 2\pi \right\}}1dt = 2\pi \neq 0$$

Since the line integral over a closed curve is nonzero, $F$ is not conservative.
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/calculo-vetorial/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/calculo-vetorial/a1.md#apresentacao-original)

- Anterior: [Vectorial Line Integrals](../vectorial-line-integrals/index.md)
