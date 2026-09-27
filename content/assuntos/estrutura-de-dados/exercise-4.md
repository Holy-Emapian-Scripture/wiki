---
layout: "default"
title: "Exercise 4"
tipo: "exercicio"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Exercices/lecture_10/exercises.md"
trilha: "../../../trilhas/estrutura-de-dados/exercicios-aula-10.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 1
---

[Estrutura de Dados](index.md)

<!-- wiki:original:inicio -->
<a id="secao-1"></a>

# Exercise 4

<a id="secao-2"></a>

## Solution

``` cpp
#include <queue>
#include <stack>

std::queue<char> reverse_queue_using_stack(std::queue<char> input_queue) {
    std::stack<char> temporary_stack;

    while (!input_queue.empty()) {
        char current_element = input_queue.front();
        input_queue.pop();
        temporary_stack.push(current_element);
    }

    std::queue<char> reversed_queue;
    while (!temporary_stack.empty()) {
        char top_element = temporary_stack.top();
        temporary_stack.pop();
        reversed_queue.push(top_element);
    }

    return reversed_queue;
}
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios — aula 10](../../trilhas/estrutura-de-dados/exercicios-aula-10.md) · [Apresentação e contexto da fonte](../../trilhas/estrutura-de-dados/exercicios-aula-10.md#apresentacao-original)

- Próximo: [Exercise 5](exercise-5.md)
