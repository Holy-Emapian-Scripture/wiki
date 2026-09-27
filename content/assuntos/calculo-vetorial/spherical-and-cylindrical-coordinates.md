---
layout: "default"
title: "Spherical and Cylindrical coordinates"
tipo: "conteudo"
disciplina: "Cálculo Vetorial"
origem: "3 semestre/Cálculo Vetorial/Recaps/A1_recap.md"
trilha: "../../../trilhas/calculo-vetorial/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 1
---

[Cálculo Vetorial](index.md)

<!-- wiki:original:inicio -->

<a id="secao-1"></a>

# Spherical and Cylindrical coordinates


<a id="cylindrical-coordinates"></a>
<a id="secao-2"></a>

## Cylindrical coordinates

The transformation from the ordinary space ${\mathbb{R}}^{3}$ to $C\left( {\mathbb{R}}^{3} \right)$ is nearly analogous to polar coordinates in ${\mathbb{R}}^{2}$ described below:

$$T(x,y,z) = \left( r\cos\theta,r\sin\theta,z \right)$$, and if we were integrating some function $f:{\mathbb{R}}^{3} \rightarrow {\mathbb{R}}$ under the region $A \subset {\mathbb{R}}^{3}$ in the space $(x,y,z)$, the equivalent integral in the new system $C\left( {\mathbb{R}}^{3} \right)$ is:

$$
\iiint_{C(A)}f\left( r\cos\theta,r\sin\theta,z \right)rdzdrd\theta
$$

<a id="spherical-coordinates"></a>
<a id="secao-3"></a>

## Spherical coordinates

From the reasoning used in cylindrical coordinates, we have:

$$
\iiint_{A}f(x,y,z)dxdydz = \iiint_{S(A)}f\left( \rho\sin\varphi\cos\theta,\rho\sin\varphi\sin\theta,\rho\cos\theta \right)\rho^{2}\sin\varphi d\rho d\theta d\varphi
$$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../trilhas/calculo-vetorial/a1.md) · [Apresentação e contexto da fonte](../../trilhas/calculo-vetorial/a1.md#apresentacao-original)

- Próximo: [Jacobian Determinant For Multiple Integrals](jacobian-determinant-for-multiple-integrals.md)
