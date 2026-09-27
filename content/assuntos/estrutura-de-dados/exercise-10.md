---
layout: "default"
title: "Exercise 10"
tipo: "exercicio"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Exercices/lecture_10/exercises.md"
trilha: "../../../trilhas/estrutura-de-dados/exercicios-aula-10.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 7
---

[Estrutura de Dados](index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Exercise 10

<a id="secao-16"></a>

## Solution

<a id="secao-17"></a>

### a)

$O(n)$:

``` cpp
int get_minimum_value_in_queue_linear(std::queue<int> input_queue) {
    if (input_queue.empty()) return -1;
    int minimum_value = input_queue.front();
    while (!input_queue.empty()) {
        if (input_queue.front() < minimum_value) {
            minimum_value = input_queue.front();
        }
        input_queue.pop();
    }
    return minimum_value;
}
```

<a id="secao-18"></a>

### b)

Optimized if $n \in \lbrack 1,10\rbrack$:

``` cpp
int get_minimum_value_with_fixed_range(std::queue<int> input_queue) {
    int frequency_counter[11] = {0}; 
    while (!input_queue.empty()) {
        int current_value = input_queue.front();
        input_queue.pop();
        frequency_counter[current_value]++;
    }

    for (int value = 1; value <= 10; value++) {
        if (frequency_counter[value] > 0) {
            return value;
        }
    }
    return -1;
}
```
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios — aula 10](../../trilhas/estrutura-de-dados/exercicios-aula-10.md) · [Apresentação e contexto da fonte](../../trilhas/estrutura-de-dados/exercicios-aula-10.md#apresentacao-original)

- Anterior: [Exercise 9](exercise-9.md)
