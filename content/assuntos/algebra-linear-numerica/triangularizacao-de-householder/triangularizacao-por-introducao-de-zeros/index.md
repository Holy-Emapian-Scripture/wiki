---
layout: "default"
title: "Triangularização por Introdução de Zeros — Triangularização de Householder"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 29
---

[Álgebra Linear Numérica](../../index.md) · [Triangularização de Householder](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-29"></a>

# Triangularização por Introdução de Zeros

No coração do algoritmo de Householder, temos a ideia de aplicar uma matriz ortogonal que introduz zeros abaixo da diagonal principal! Assim (neste exemplo, $x$ significa uma entrada não nula, **$x$** significa uma entrada que mudou desde a última aplicação ortogonal e nada significa 0)

$$\begin{pmatrix} x & x & x \\ x & x & x \\ x & x & x \\ x & x & x \\ x & x & x \end{pmatrix}_{A} \rightarrow Q_{1}A \rightarrow \begin{pmatrix} \mathbf{x} & \mathbf{x} & \mathbf{x} \\ & \mathbf{x} & \mathbf{x} \\ & \mathbf{x} & \mathbf{x} \\ & \mathbf{x} & \mathbf{x} \\ & \mathbf{x} & \mathbf{x} \end{pmatrix}_{Q_{1}A} \rightarrow Q_{2}Q_{1}A \rightarrow \begin{pmatrix} x & x & x \\ & \mathbf{x} & \mathbf{x} \\ & & \mathbf{x} \\ & & \mathbf{x} \\ & & \mathbf{x} \end{pmatrix}_{Q_{2}Q_{1}A} \rightarrow Q_{3}Q_{2}Q_{1}A \rightarrow \begin{pmatrix} x & x & x \\ & x & x \\ & & \mathbf{x} \\ & & \\ & & \end{pmatrix}_{Q_{3}Q_{2}Q_{1}A}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Triangularização de Householder](../index.md)
- Próximo: [Refletores de Householder](../refletores-de-householder/index.md)
