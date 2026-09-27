---
layout: "default"
title: "Verificação de caminho e caminho simples — Busca em Grafos"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 10
---

[Projeto e Análise de Algoritmos](../../index.md) · [Busca em Grafos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-19"></a>

# Verificação de caminho e caminho simples

**Dado um grafo $G = (V,E)$ e um caminho $P$ composto por uma sequência de vértices, verifique se $P$ é um caminho de $G$, e se o caminho é simples.**

<a id="secao-20"></a>

## Matriz de adjacência

Basta passar a matriz e a cada $v_{i}$ e $v_{i + 1}$ verificar se é $1$ na matriz. Eu decidi verificar se é um caminho simples em uma função separada, mas o leitor pode fazer junto se quiser. (a função serve tanto para lista quanto para matriz, por isso não irei repeti-la). É só olhar o tamanho da lista de caminhos se for igual quanto a transformamos em conjunto.

``` py
def is_path_matrix(matrix, path):
    for order in range(len(path) - 1):
        if matrix[path[order]][path[order + 1]] != 1:
            return False
    return True

def is_simple_path(path):
    if len(set(path)) != len(path):
        return False
    return True
```

<a id="secao-21"></a>

## Lista de adjacência

Basta passar a lista e a cada $v_{i}$ e $v_{i + 1}$ verificar se existe o vértice na lista de arestas de $v_{i}$

``` py
def is_path_list(list, path):
    for order in range(len(path) - 1):
        if path[order + 1] not in list[path[order]]:
            return False
    return True
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios de slides](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Busca em Grafos](../index.md)
- Próximo: [Verificação de númeração topológica](../verificacao-de-numeracao-topologica/index.md)
