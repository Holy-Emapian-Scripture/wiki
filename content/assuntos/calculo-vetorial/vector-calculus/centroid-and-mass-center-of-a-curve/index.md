---
layout: "default"
title: "Centroid and Mass Center of a Curve — Vector Calculus"
tipo: "conteudo"
disciplina: "Cálculo Vetorial"
origem: "3 semestre/Cálculo Vetorial/Recaps/A1_recap.md"
trilha: "../../../../trilhas/calculo-vetorial/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 11
---

[Cálculo Vetorial](../../index.md) · [Vector Calculus](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-11"></a>

# Centroid and Mass Center of a Curve

<a id="secao-12"></a>

## Mass Cernter

Given $\gamma \subset {\mathbb{R}}^{3}$ a curve, and let $f(x,y,z)$ be the mass density per unit of lenght of $\gamma$, we know that the $\gamma$‘s mass is given by:

$$M = \int_{\gamma}f(x,y,z)ds.$$

So the mass center of $\gamma$ is the point $c_{m} = \left( x_{c},y_{c},z_{c} \right)$ s.t:

$$\begin{array}{r} x_{c} = \frac{\int_{\gamma}xf(x,y,z)ds}{M} \\ y_{c} = \frac{\int_{\gamma}yf(x,y,z)ds}{M} \\ z_{c} = \frac{\int_{\gamma}zf(x,y,z)ds}{M} \end{array}$$

If $f$ is constant (homogeneous curve), then the mass center is the centroid as well

<a id="secao-13"></a>

## Centroid

Let $\gamma \subset {\mathbb{R}}^{3}$ be a smooth or piecewise smooth curve, parameterized by $\gamma(t):\lbrack a,b\rbrack \rightarrow {\mathbb{R}}^{3}$. If the curve is **homogeneous**, meaning the mass density per unit length is constant, then its **centroid** is the point $\left( x_{c},y_{c},z_{c} \right)$ given by:

$$\begin{array}{r} x_{c} = \frac{1}{L}\int_{\gamma}xds \\ y_{c} = \frac{1}{L}\int_{\gamma}yds \\ z_{c} = \frac{1}{L}\int_{\gamma}zds \end{array}$$

Where $L$ is the total arc length of the curve:

$$L = \int_{\gamma}ds = \int_{a}^{b}\|\gamma'(t)\| dt$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/calculo-vetorial/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/calculo-vetorial/a1.md#apresentacao-original)

- Anterior: [Scalar Line Integrals](../scalar-line-integrals/index.md)
- Próximo: [Vectorial Line Integrals](../vectorial-line-integrals/index.md)
