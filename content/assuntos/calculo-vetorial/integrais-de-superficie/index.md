---
layout: "default"
title: "Integrais de Superfície"
tipo: "conteudo"
disciplina: "Cálculo Vetorial"
origem: "3 semestre/Cálculo Vetorial/Recaps/A2_recap.md"
trilha: "../../../trilhas/calculo-vetorial/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 3
---

[Cálculo Vetorial](../index.md)

<!-- wiki:original:inicio -->

<a id="section_integral_superficie"></a>

# Integrais de Superfície


<a id="integrais-de-superficie-escalares"></a>
<a id="section_integral_superficie_escalar"></a>

## Integrais de Superfície Escalares

Lembrando que uma *superfície* é uma função:

$$
\varphi:D \subset {\mathbb{R}}^{2} \rightarrow {\mathbb{R}}^{3}
$$

Onde $D$ é fechado e limitado.

Se $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ é função escalar e $S$ uma superfície, a integral de $f$ sobre $S$ é:

$$
\iint_{S}fdS = \iint_{D}f\left( \varphi(u,v) \right) \cdot \left\| {\varphi_{u} \times \varphi_{v}} \right\| dudv
$$

<a id="integrais-de-superficie-vetoriais"></a>
<a id="section_integral_superficie_vetorial"></a>

## Integrais de Superfície Vetoriais

Se for $F:{\mathbb{R}}^{\rightarrow}{\mathbb{R}}^{n}$ um campo vetorial, o **fluxo** de $F$ sobre a superfície $S$ é:

$$
\iint_{S}FdS = \iint_{S}F \cdot \hat{n}dS = \iint_{D}F\left( \varphi(u,v) \right) \cdot \left( \varphi_{u} \times \varphi_{v} \right)dudv
$$

O vetor $\hat{n}$ é o vetor unitário normal à superfície $S$. Note que $\iint_{S}F \cdot \hat{n}dS$ é uma integral escalar.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/calculo-vetorial/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/calculo-vetorial/a2.md#apresentacao-original)

- Anterior: [Revisão da A1](../revisao-da-a1/index.md)
- Próximo: [Operadores Diferenciais](../operadores-diferenciais/index.md)
