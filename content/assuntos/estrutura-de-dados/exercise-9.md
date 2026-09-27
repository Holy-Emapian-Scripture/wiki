---
layout: "default"
title: "Exercise 9"
tipo: "exercicio"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Exercices/lecture_10/exercises.md"
trilha: "../../../trilhas/estrutura-de-dados/exercicios-aula-10.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 6
---

[Estrutura de Dados](index.md)

<!-- wiki:original:inicio -->
<a id="secao-11"></a>

# Exercise 9

<a id="secao-12"></a>

## Solution

<a id="secao-13"></a>

### a)

$O(n)$:

``` cpp
int get_minimum_value_linear(int* stack_array, int current_stack_size) {
    if (current_stack_size == 0) return -1;
    int minimum_value = stack_array[0];
    for (int i = 1; i < current_stack_size; i++) {
        if (stack_array[i] < minimum_value) {
            minimum_value = stack_array[i];
        }
    }
    return minimum_value;
}
```

<a id="secao-14"></a>

### b)

$O(1)$:

``` cpp
struct StackWithMinimum {
    int* element_array;
    int current_size;
    int maximum_capacity;
    std::stack<int> minimum_tracking_stack;
};

void push_with_min_tracking(StackWithMinimum* stack, int value_to_push) {
    if (stack->current_size < stack->maximum_capacity) {
        stack->element_array[stack->current_size++] = value_to_push;
        if (stack->minimum_tracking_stack.empty() || value_to_push <= stack->minimum_tracking_stack.top()) {
            stack->minimum_tracking_stack.push(value_to_push);
        }
    }
}

int pop_with_min_tracking(StackWithMinimum* stack) {
    if (stack->current_size == 0) return -1;
    int popped_value = stack->element_array[--stack->current_size];
    if (!stack->minimum_tracking_stack.empty() && popped_value == stack->minimum_tracking_stack.top()) {
        stack->minimum_tracking_stack.pop();
    }
    return popped_value;
}

int get_minimum_value_constant_time(StackWithMinimum* stack) {
    return (!stack->minimum_tracking_stack.empty()) ? stack->minimum_tracking_stack.top() : -1;
}
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios — aula 10](../../trilhas/estrutura-de-dados/exercicios-aula-10.md) · [Apresentação e contexto da fonte](../../trilhas/estrutura-de-dados/exercicios-aula-10.md#apresentacao-original)

- Anterior: [Exercise 8](exercise-8.md)
- Próximo: [Exercise 10](exercise-10.md)
