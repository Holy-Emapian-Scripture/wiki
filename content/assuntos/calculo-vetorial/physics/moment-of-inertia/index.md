---
layout: "default"
title: "Moment of Inertia — Physics"
tipo: "conteudo"
disciplina: "Cálculo Vetorial"
origem: "3 semestre/Cálculo Vetorial/Recaps/A1_recap.md"
trilha: "../../../../trilhas/calculo-vetorial/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 7
---

[Cálculo Vetorial](../../index.md) · [Physics](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# Moment of Inertia

Let $X \subset {\mathbb{R}}^{3}$ be a body, rotating over a given axis, let $\mu(x)$ be the mass density in $x,\forall x \in X$, if $r(X)$ is the distance to axis it is rotating over, and $v(x)$ is the speed, $\forall x \in X$, then $\vert v(x)\vert  = \omega r(x)$, where $\omega$ is the angular speed

It follows that the **kinetic energy** of the body is $\frac{mv^{2}}{2}$:

$$\frac{1}{2} \cdot \int_{X}\mu(x)\vert v(x)\vert ^{2}dX = \frac{1}{2}\omega^{2} \cdot \int_{X}\mu(x){r(x)}^{2}dX$$

We define now the **Moment of Inertia** as:

$$I = \int_{X}\mu(x){r(x)}^{2}dX.$$

$L = \omega I$ is called the **angular momentum**, it is conserved if there are no external rotational forces.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/calculo-vetorial/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/calculo-vetorial/a1.md#apresentacao-original)

- Anterior: [Mass Center and Centroid](../mass-center-and-centroid/index.md)
- Próximo: [Vector Calculus](../../vector-calculus/index.md)
