---
layout: "default"
title: "Physics"
tipo: "conteudo"
disciplina: "Cálculo Vetorial"
origem: "3 semestre/Cálculo Vetorial/Recaps/A1_recap.md"
trilha: "../../../trilhas/calculo-vetorial/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 5
---

[Cálculo Vetorial](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-5"></a>

# Physics


<a id="mass-center-and-centroid"></a>
<a id="secao-6"></a>

## Mass Center and Centroid

Given a plane region $S^{2} \subset {\mathbb{R}}^{2}$, its **centroid** is the point $\left( x_{c},y_{c} \right)$, where:

$$
\begin{array}{r} x_{c} = \frac{1}{\text{area}(S)}\iint_{S}xdxdy \\ y_{c} = \frac{1}{\text{area}(S)}\iint_{S}ydxdy \end{array}
$$

If the region/body/whatever has **constant** density $\mu(x,y),\forall x,y \in {\mathbb{R}}$, then its centroid is the same as the mass center, which is the point $\left( \hat{x_{c}},\hat{y_{c}} \right)$ where:

$$
\begin{array}{r} \hat{x_{c}} = \frac{\iint_{S}\mu(x,y)xdxdy}{\iint_{S}\mu(x,y)dxdy} \\ \hat{y_{c}} = \frac{\iint_{S}\mu(x,y)ydxdy}{\iint_{S}\mu(x,y)dxdy} \end{array}
$$

Notice that the **mass** of $S$ is given by:

$$
\iint_{S}\mu(x,y)dxdy
$$

<a id="moment-of-inertia"></a>
<a id="secao-7"></a>

## Moment of Inertia

Let $X \subset {\mathbb{R}}^{3}$ be a body, rotating over a given axis, let $\mu(x)$ be the mass density in $x,\forall x \in X$, if $r(X)$ is the distance to axis it is rotating over, and $v(x)$ is the speed, $\forall x \in X$, then $\vert v(x)\vert  = \omega r(x)$, where $\omega$ is the angular speed

It follows that the **kinetic energy** of the body is $\frac{mv^{2}}{2}$:

$$
\frac{1}{2} \cdot \int_{X}\mu(x)\vert v(x)\vert ^{2}dX = \frac{1}{2}\omega^{2} \cdot \int_{X}\mu(x){r(x)}^{2}dX
$$

We define now the **Moment of Inertia** as:

$$
I = \int_{X}\mu(x){r(x)}^{2}dX.
$$

$L = \omega I$ is called the **angular momentum**, it is conserved if there are no external rotational forces.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/calculo-vetorial/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/calculo-vetorial/a1.md#apresentacao-original)

- Anterior: [Jacobian Determinant For Multiple Integrals](../jacobian-determinant-for-multiple-integrals/index.md)
- Próximo: [Vector Calculus](../vector-calculus/index.md)
