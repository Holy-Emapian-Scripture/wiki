---
layout: "default"
title: "Mass Center and Centroid — Physics"
tipo: "conteudo"
disciplina: "Cálculo Vetorial"
origem: "3 semestre/Cálculo Vetorial/Recaps/A1_recap.md"
trilha: "../../../../trilhas/calculo-vetorial/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 6
---

[Cálculo Vetorial](../../index.md) · [Physics](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-6"></a>

# Mass Center and Centroid

Given a plane region $S^{2} \subset {\mathbb{R}}^{2}$, its **centroid** is the point $\left( x_{c},y_{c} \right)$, where:

$$\begin{array}{r} x_{c} = \frac{1}{\text{area}(S)}\iint_{S}xdxdy \\ y_{c} = \frac{1}{\text{area}(S)}\iint_{S}ydxdy \end{array}$$

If the region/body/whatever has **constant** density $\mu(x,y),\forall x,y \in {\mathbb{R}}$, then its centroid is the same as the mass center, which is the point $\left( \hat{x_{c}},\hat{y_{c}} \right)$ where:

$$\begin{array}{r} \hat{x_{c}} = \frac{\iint_{S}\mu(x,y)xdxdy}{\iint_{S}\mu(x,y)dxdy} \\ \hat{y_{c}} = \frac{\iint_{S}\mu(x,y)ydxdy}{\iint_{S}\mu(x,y)dxdy} \end{array}$$

Notice that the **mass** of $S$ is given by:

$$\iint_{S}\mu(x,y)dxdy$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/calculo-vetorial/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/calculo-vetorial/a1.md#apresentacao-original)

- Anterior: [Physics](../index.md)
- Próximo: [Moment of Inertia](../moment-of-inertia/index.md)
