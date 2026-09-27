---
layout: "default"
title: "Verificação de númeração topológica — Busca em Grafos"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 11
---

[Projeto e Análise de Algoritmos](../../index.md) · [Busca em Grafos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-22"></a>

# Verificação de númeração topológica

**Crie um algoritmo que verifica se a numeração dos vértices de um grafo $G = (V,E)$ é topológica.**

<a id="secao-23"></a>

## Matriz de adjacência

Trivialmente, basta verificar se cada $i \geq j$(evitando laços). Como a matriz não é simétrica, não podemos ignorar metade da matriz.

``` py
def is_topological_matrix(matrix):
    num_vertices = len(matrix)
    for i in range (num_vertices):
        for j in range (num_vertices):
            if matrix[i][j] == 1 and i >= j:
                return False
    return True
```

<a id="secao-24"></a>

## Lista de adjacência

Análogo, só que para lista :D

``` py
def is_topological_list(list):
    num_vertices = len(list)
    for i in range (num_vertices):
        for j in range(len(list[i])):
            if i >= list[i][j]:
                return False
    return True
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios de slides](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Verificação de caminho e caminho simples](../verificacao-de-caminho-e-caminho-simples/index.md)
- Próximo: [Verificação de ordenação topológica (e determinação)](../verificacao-de-ordenacao-topologica-e-determinacao/index.md)
