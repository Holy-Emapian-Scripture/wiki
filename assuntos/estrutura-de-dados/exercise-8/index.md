---
layout: "default"
title: "Exercise 8"
tipo: "exercicio"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Exercices/lecture_10/exercises.md"
trilha: "../../../trilhas/estrutura-de-dados/exercicios-aula-10.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 5
---

[Estrutura de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-9"></a>

# Exercise 8

<a id="secao-10"></a>

## Solution

``` cpp
void enqueue_value_into_queue(int value_to_enqueue) {
    input_stack_for_enqueue_operations.push(value_to_enqueue); // O(1)
}

void transfer_elements_from_input_to_output_stack() {
    while (!input_stack_for_enqueue_operations.empty()) {
        int top_value_from_input_stack = input_stack_for_enqueue_operations.top();
        input_stack_for_enqueue_operations.pop();
        output_stack_for_dequeue_operations.push(top_value_from_input_stack);
    }
}

int dequeue_value_from_queue() {
    if (output_stack_for_dequeue_operations.empty()) {
        transfer_elements_from_input_to_output_stack();
    }

    if (output_stack_for_dequeue_operations.empty()) {
        return -1; // Queue is empty
    }

    int value_to_return = output_stack_for_dequeue_operations.top();
    output_stack_for_dequeue_operations.pop();
    return value_to_return;
}
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios — aula 10](../../../trilhas/estrutura-de-dados/exercicios-aula-10.md) · [Apresentação e contexto da fonte](../../../trilhas/estrutura-de-dados/exercicios-aula-10.md#apresentacao-original)

- Anterior: [Exercise 7](../exercise-7/index.md)
- Próximo: [Exercise 9](../exercise-9/index.md)
