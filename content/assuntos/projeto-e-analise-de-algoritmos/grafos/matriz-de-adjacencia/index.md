---
layout: "default"
title: "Matriz de adjacência — Grafos"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 6
---

[Projeto e Análise de Algoritmos](../../index.md) · [Grafos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-9"></a>

# Matriz de adjacência

**Implemente uma classe para representar um grafo utilizando matriz de adjacência.**

<a id="secao-10"></a>

## C++

Em breve

<a id="secao-11"></a>

## Python

Nada de difícil entendimento aqui, portanto não precisa ser explicado. É apenas a implementação em Python do código dado nos slides de PAA do mesmo exercício em C++.

``` py
class GraphMatrix:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0 for _ in range(num_vertices)] for i in range(num_vertices)]

    def has_edge(self, v1, v2):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            return self.matrix[v1][v2]
        return False

    def add_edge(self, v1, v2):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            self.matrix[v1][v2] = 1
            self.matrix[v2][v1] = 1
        else:
            print("Erro")

    def remove_edge(self, v1, v2):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            self.matrix[v1][v2] = 0
            self.matrix[v2][v1] = 0
        else:
            print("Erro")

    def print(self):
        for v1 in range(self.num_vertices):
            list_adj = []
            for v2 in range(self.num_vertices):
                if self.has_edge(v1, v2):
                    list_adj.append(f"({v1},{v2})")
            print(list_adj)

    def print_matrix(self):
        for v1 in range(self.num_vertices):
            row = []
            for v2 in range(self.num_vertices):
                row.append(self.matrix[v1][v2])
            print(row)
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios de slides](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Grafos](../index.md)
- Próximo: [Lista de adjacências](../lista-de-adjacencias/index.md)
