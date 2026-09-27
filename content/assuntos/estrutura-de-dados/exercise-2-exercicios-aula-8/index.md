---
layout: "default"
title: "Exercise 2"
tipo: "exercicio"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Exercices/lecture_8/exercises.md"
trilha: "../../../trilhas/estrutura-de-dados/exercicios-aula-8.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 2
---

[Estrutura de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Exercise 2

<a id="secao-6"></a>

## Solution

Algorithms $T_{1},\ldots,T_{5},T_{7},\ldots,T_{9}$ are trivial. for $T_{6}$, if $n > 1$ then $T_{6} \in O\left( n\log ²(n) \right)$. For $T_{10}$, notice that:

$$
T(2) = 2T(1) + 2 \in O(1),
$$

$$
T(3) = 2T(2) + 2 = 2\left\lbrack 2T(1) + 2 \right\rbrack + 2
$$

$$
.
$$

$$
.
$$

$$
.
$$

$$
T(n) = 2^{n}\left\lbrack T(1) + 1 \right\rbrack + 2 \in O\left( 2^{n} \right).
$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios — aula 8](../../../trilhas/estrutura-de-dados/exercicios-aula-8.md) · [Apresentação e contexto da fonte](../../../trilhas/estrutura-de-dados/exercicios-aula-8.md#apresentacao-original)

- Anterior: [Exercise 1](../exercise-1-exercicios-aula-8/index.md)
- Próximo: [Exercise 3](../exercise-3-exercicios-aula-8/index.md)
