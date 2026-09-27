---
layout: "default"
title: "Desigualdades de Cauchy-Schwarz e Hölder — Normas"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 4
---

[Álgebra Linear Numérica](../../index.md) · [Normas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Desigualdades de Cauchy-Schwarz e Hölder

Quando usamos normas, geralmente é difícil calcular normas-p com valores altos de $p$, então as gerenciamos usando desigualdades! Uma desigualdade muito útil é a de Hölder:

**Definição: Desigualdade de Hölder**

Dados $1 \leq p,q \leq \infty$, e $\frac{1}{p} + \frac{1}{q} = 1$, então, para quaisquer vetores $x,y$:

$\vert x^{\ast}y\vert  \leq \| x\|_{p}\| y\|_{q}$

E a desigualdade de Cauchy-Schwarz é um caso especial onde $p = q = 2$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Normas de matrizes](../normas-de-matrizes/index.md)
- Próximo: [Limitando $\| AB\|$](../limitando-ab/index.md)
