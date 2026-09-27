---
layout: "default"
title: "Exercise 5"
tipo: "exercicio"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Exercices/lecture_10/exercises.md"
trilha: "../../../trilhas/estrutura-de-dados/exercicios-aula-10.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 2
---

[Estrutura de Dados](index.md)

<!-- wiki:original:inicio -->
<a id="secao-3"></a>

# Exercise 5

<a id="secao-4"></a>

## Solution

We can make 2 different queuess growing in opposite directions (they’ll colide at the middle, this may or may not be relevant to the problem):

``` cpp
struct TwoStacksInOneArray {
  int* shared_array;
  int array_capacity;
  int top_index_stack_1;
  int top_index_stack_2;

  TwoStacksInOneArray(int total_capacity) {
      array_capacity = total_capacity;
      shared_array = new int[array_capacity];
      top_index_stack_1 = -1;
      top_index_stack_2 = array_capacity;
  }

  void push_to_stack_1(int value_to_push) {
      if (top_index_stack_1 < top_index_stack_2 - 1) {
        shared_array[++top_index_stack_1] = value_to_push;
      }
  }

  void push_to_stack_2(int value_to_push) {
      if (top_index_stack_1 < top_index_stack_2 - 1) {
          shared_array[--top_index_stack_2] = value_to_push;
      }
  }

  int pop_from_stack_1() {
      return (top_index_stack_1 >= 0) ? shared_array[top_index_stack_1--] : -1;
  }

  int pop_from_stack_2() {
      return (top_index_stack_2 < array_capacity) ? shared_array[top_index_stack_2++] : -1;
  }
};
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios — aula 10](../../trilhas/estrutura-de-dados/exercicios-aula-10.md) · [Apresentação e contexto da fonte](../../trilhas/estrutura-de-dados/exercicios-aula-10.md#apresentacao-original)

- Anterior: [Exercise 4](exercise-4.md)
- Próximo: [Exercise 6](exercise-6.md)
