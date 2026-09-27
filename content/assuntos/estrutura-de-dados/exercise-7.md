---
layout: "default"
title: "Exercise 7"
tipo: "exercicio"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Exercices/lecture_10/exercises.md"
trilha: "../../../trilhas/estrutura-de-dados/exercicios-aula-10.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 4
---

[Estrutura de Dados](index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# Exercise 7

<a id="secao-8"></a>

## Solution

``` cpp
struct DequeWithFixedArray {
    int* deque_array;
    int front_index;
    int rear_index;
    int current_size;
    int array_capacity;

    DequeWithFixedArray(int maximum_capacity) {
        array_capacity = maximum_capacity;
        deque_array = new int[array_capacity];
        front_index = 0;
        rear_index = 0;
        current_size = 0;
    }

    void insert_at_front(int value_to_insert) {
        if (current_size == array_capacity) return;
        front_index = (front_index - 1 + array_capacity) % array_capacity;
        deque_array[front_index] = value_to_insert;
        current_size++;
    }

    void insert_at_rear(int value_to_insert) {
        if (current_size == array_capacity) return;
        deque_array[rear_index] = value_to_insert;
        rear_index = (rear_index + 1) % array_capacity;
        current_size++;
    }

    void remove_from_front() {
        if (current_size == 0) return;
        front_index = (front_index + 1) % array_capacity;
        current_size--;
    }

    void remove_from_rear() {
        if (current_size == 0) return;
        rear_index = (rear_index - 1 + array_capacity) % array_capacity;
        current_size--;
    }
};
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios — aula 10](../../trilhas/estrutura-de-dados/exercicios-aula-10.md) · [Apresentação e contexto da fonte](../../trilhas/estrutura-de-dados/exercicios-aula-10.md#apresentacao-original)

- Anterior: [Exercise 6](exercise-6.md)
- Próximo: [Exercise 8](exercise-8.md)
