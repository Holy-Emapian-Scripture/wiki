---
layout: "default"
title: "Exercise 6"
tipo: "exercicio"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Exercices/lecture_10/exercises.md"
trilha: "../../../trilhas/estrutura-de-dados/exercicios-aula-10.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 3
---

[Estrutura de Dados](index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Exercise 6

<a id="secao-6"></a>

## Solution

``` cpp
int circular_sequential_search(int* circular_list, int list_length, int target_value, int start_index) {
    for (int offset = 0; offset < list_length; offset++) {
        int current_index = (start_index + offset) % list_length;
        if (circular_list[current_index] == target_value) {
            return current_index;
        }
    }
    return -1;
}
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios — aula 10](../../trilhas/estrutura-de-dados/exercicios-aula-10.md) · [Apresentação e contexto da fonte](../../trilhas/estrutura-de-dados/exercicios-aula-10.md#apresentacao-original)

- Anterior: [Exercise 5](exercise-5.md)
- Próximo: [Exercise 7](exercise-7.md)
