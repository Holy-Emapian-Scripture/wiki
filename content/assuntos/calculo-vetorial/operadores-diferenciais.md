---
layout: "default"
title: "Operadores Diferenciais"
tipo: "conteudo"
disciplina: "Cálculo Vetorial"
origem: "3 semestre/Cálculo Vetorial/Recaps/A2_recap.md"
trilha: "../../../trilhas/calculo-vetorial/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 6
---

[Cálculo Vetorial](index.md)

<!-- wiki:original:inicio -->

<a id="section_operadores_diferenciais"></a>

# Operadores Diferenciais


<a id="gradiente"></a>
<a id="section_gradiente"></a>

## Gradiente

O gradiente $\nabla$ de $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ é:

$$\nabla f = \left( \frac{\partial f}{\partial x_{1}},\ldots,\frac{\partial f}{\partial x_{n}} \right)$$ <a id="equation_definition_gradiente"></a>

<a id="rotacional"></a>
<a id="section_rotacional"></a>

## Rotacional

Dada $F:{\mathbb{R}}^{3} \rightarrow {\mathbb{R}}^{3},F = \left( F_{1},F_{2},F_{3} \right)$ um campo vetorial, o rotacional de $F$ é:

$$
\begin{array}{r} {\text{rot}(F)} = \nabla \times F \\ = \left( \frac{\partial F_{3}}{\partial y} - \frac{\partial F_{2}}{\partial z},\frac{\partial F_{1}}{\partial z} - \frac{\partial F_{3}}{\partial x},\frac{\partial F_{2}}{\partial x} - \frac{\partial F_{1}}{\partial y} \right) \end{array}
$$

Se for $F:{\mathbb{R}}^{2} \rightarrow {\mathbb{R}}^{2},F = \left( F_{1},F_{2} \right)$, o rotacional fica:

$$
{\text{rot}(F)} = \frac{\partial F_{2}}{\partial x} - \frac{\partial F_{1}}{\partial y}
$$

<a id="laplaciano"></a>
<a id="section_laplaciano"></a>

## Laplaciano

Dada $f:{\mathbb{R}}^{\rightarrow}{\mathbb{R}}$, o laplaciano é:

$$\mathrm{\Delta}f = {\text{div}(\nabla f)} = \frac{\partial^{2}f}{\partial x_{1}^{2}} + \ldots + \frac{\partial^{2}f}{\partial x_{n}^{2}}$$ <a id="equation_definition_laplaciano"></a>

Se $\mathrm{\Delta}f = 0$, $f$ é dita *harmônica*.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/calculo-vetorial/a2.md) · [Apresentação e contexto da fonte](../../trilhas/calculo-vetorial/a2.md#apresentacao-original)

- Anterior: [Integrais de Superfície](integrais-de-superficie.md)
- Próximo: [Propriedades dos Operadores Diferenciais](propriedades-dos-operadores-diferenciais.md)
