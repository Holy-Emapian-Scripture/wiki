---
layout: "default"
title: "Verificação de subgrafo — Grafos"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 8
---

[Projeto e Análise de Algoritmos](../../index.md) · [Grafos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Verificação de subgrafo

**Dados dois grafos $G = (V,E)$ e $H = (V',E')$ com $V = V'$, crie um algoritmo que verifica se $H$ é subgrafo de $G$.**

Nesse problema, $V = V'$, então é possível usarmos matriz de adjacência tranquilamente (lista de adjacência também). Sabendo disso, vamos fazer para os dois casos:

<a id="secao-16"></a>

## Matriz de adjacência

Para a matriz, basta apenas passar por cada elemento das matrizes e verificarmos se, quando em $H$ é $1$, $G$ é $0$, pois isso significaria que existe alguma aresta fora do grafo original.

``` py
def is_subgraph_matrix(gmatrix, hmatrix):
    num_vertices = len(gmatrix)
    for row in range(num_vertices):
        for column in range(num_vertices):
            if hmatrix[row][column] == 1 and gmatrix[row][column] == 0:
                return False
    return True
```

<a id="secao-17"></a>

## Lista de adjacência

Para a lista, basta apenas passarmos por cada elemento de cada lista de vértice, e ver so vértice está na lista do grafo original.

``` py
def is_subgraph_list(glist,hlist):
    num_vertices = len(glist)
    for vi in range(num_vertices):
        for vj in hlist[vi]:
            if vj not in glist[vi]:
                return False
    return True
```

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios de slides](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Lista de adjacências](../lista-de-adjacencias/index.md)
- Próximo: [Busca em Grafos](../../busca-em-grafos/index.md)
