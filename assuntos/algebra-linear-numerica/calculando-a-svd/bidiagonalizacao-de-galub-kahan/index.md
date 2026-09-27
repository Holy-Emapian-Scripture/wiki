---
layout: "default"
title: "Bidiagonalização de Galub-Kahan — Calculando a SVD"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 64
---

[Álgebra Linear Numérica](../../index.md) · [Calculando a SVD](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-64"></a>

# Bidiagonalização de Galub-Kahan

A ideia é aplicar matrizes unitárias distintas na esquerda de $A$ e na sua direita, e advinha que tipo de matrizes usamo? Exatamente: **Refletores de Householder**. A ideia é aplicar refletores a esquerda de $A$ para colocar zeros abaixo da diagonal principal e a direita para aplicar zeros após a diagonal superior de $A$:

![Bidiagonalização de Galub-Kahan exemplificada](../../assets/galub-kahan-diagonalization.png)

*Figura 21. Bidiagonalização de Galub-Kahan exemplificada*

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Divisão em duas fases](../divisao-em-duas-fases/index.md)
- Próximo: [Métodos de Bidiagonalização mais eficientes](../metodos-de-bidiagonalizacao-mais-eficientes/index.md)
