---
layout: "default"
title: "Lista de adjacências — Grafos"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 7
---

[Projeto e Análise de Algoritmos](../../index.md) · [Grafos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-12"></a>

# Lista de adjacências

**Implemente uma classe para representar um grafo utilizando lista de adjacências.**

<a id="secao-13"></a>

## C++

Em breve

<a id="secao-14"></a>

## Python

Considerando que os vértices são sempre sequências de inteiros de $0$ a $n - 1$, podemos fazer apenas uma lista de listas em vez de usar ponteiros em Python. Caso não fosse, poderíamos usar uma hashtable de listas, ou algo semelhante.

``` py
class GraphAdjList:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.listadj = [[] for _ in range(num_vertices)]

    def has_edge(self, v1, v2):
        for i in range(len(self.listadj[v1])):
            if v2 in self.listadj[v1]:
                return True
        return False

    def add_edge(self, v1, v2):
        self.listadj[v1].append(v2)
        self.listadj[v2].append(v1)

    def remove_edge(self, v1, v2):
        self.listadj[v1].remove(v2)
        self.listadj[v2].remove(v1)

    def print_listadj(self):
        for vertex in range(self.num_vertices):
            print(f'{vertex}: {self.listadj[vertex]}')

    def print_matrix(self):
        matrix = [[0 for _ in range(self.num_vertices)] for i in range(self.num_vertices)]
        for vertex in range(self.num_vertices):
            for edge in self.listadj[vertex]:
                matrix[vertex][edge] = 1
            print(matrix[vertex])
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios de slides](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Matriz de adjacência](../matriz-de-adjacencia/index.md)
- Próximo: [Verificação de subgrafo](../verificacao-de-subgrafo/index.md)
