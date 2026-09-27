---
layout: "default"
title: "Jacobian Determinant For Multiple Integrals"
tipo: "conteudo"
disciplina: "Cálculo Vetorial"
origem: "3 semestre/Cálculo Vetorial/Recaps/A1_recap.md"
trilha: "../../../trilhas/calculo-vetorial/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 4
---

[Cálculo Vetorial](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Jacobian Determinant For Multiple Integrals

More general change of variables require some technicalities:

If $T:{\mathbb{R}}^{3} \rightarrow {\mathbb{R}}^{3}$ is a bijective function that morphes a region in the space $xyz$ into the space $uvw$ throught the equations that follow:

$$
\begin{array}{r} x = g(u,v,w) \\ y = h(u,,w) \\ z = k(u,v,w) \end{array}
$$

Then the **jacobian determinant of T** is:

$$
\frac{\partial(x,y,z)}{\partial(u,v,w)} = \det\begin{pmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\ \frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w} \end{pmatrix}
$$

And the equivalent integral onto the new system is:

$$
\iiint_{A}f(x,y,z)dxdydz = \iiint_{T(A)}f\left( x(u,v,w),y(u,v,w),z(u,v,w) \right)\vert \frac{\partial(x,y,z)}{\partial(u,v,w)}\vert dudvdw
$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../trilhas/calculo-vetorial/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/calculo-vetorial/a1.md#apresentacao-original)

- Anterior: [Spherical and Cylindrical coordinates](../spherical-and-cylindrical-coordinates/index.md)
- Próximo: [Physics](../physics/index.md)
