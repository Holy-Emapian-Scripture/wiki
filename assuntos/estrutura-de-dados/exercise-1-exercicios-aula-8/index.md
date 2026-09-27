---
layout: "default"
title: "Exercise 1"
tipo: "exercicio"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Exercices/lecture_8/exercises.md"
trilha: "../../../trilhas/estrutura-de-dados/exercicios-aula-8.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 1
---

[Estrutura de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-1"></a>

# Exercise 1

<a id="secao-2"></a>

## Solution

<a id="secao-3"></a>

### a)

It is clear that:

$$T_{1} \in O(n)$$

$$T_{2} \in O(n²)$$

Given the proper definition of the function class $O(g)$ (“Big O”) of a function $g:{\mathbb{N}} \rightarrow {\mathbb{R}}$ as follows;

$$O(g) ≔ \left\{ f:{\mathbb{N}} \rightarrow {\mathbb{R}}~\vert ~\exists c \in {\mathbb{R}},n_{0} \in {\mathbb{N}},f(n) \leq cg(n),\forall n > n_{0} \right\}$$

<a id="secao-4"></a>

### b)

We assume $n \neq 0$ , for obviously $T_{1}(0) = T_{2}(0)$, so $T_{2}$ is more efficient if:

$$T_{1}(n) > T_{2}(n) \Leftrightarrow 625n > n² \Leftrightarrow 625 > n$$

And the opposite is true for $625 < n$ , for $n = 625$ the algorithms perform equally.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios — aula 8](../../../trilhas/estrutura-de-dados/exercicios-aula-8.md) · [Apresentação e contexto da fonte](../../../trilhas/estrutura-de-dados/exercicios-aula-8.md#apresentacao-original)

- Próximo: [Exercise 2](../exercise-2-exercicios-aula-8/index.md)
