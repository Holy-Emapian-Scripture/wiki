---
layout: "default"
title: "Grafos"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 5
---

[Projeto e Análise de Algoritmos](index.md)

<!-- wiki:original:inicio -->

<a id="secao-8"></a>

# Grafos


<a id="matriz-de-adjacencia"></a>
<a id="secao-9"></a>

## Matriz de adjacência

**Implemente uma classe para representar um grafo utilizando matriz de adjacência.**

<a id="secao-10"></a>

### C++

Em breve

<a id="secao-11"></a>

### Python

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

<a id="lista-de-adjacencias"></a>
<a id="secao-12"></a>

## Lista de adjacências

**Implemente uma classe para representar um grafo utilizando lista de adjacências.**

<a id="secao-13"></a>

### C++

Em breve

<a id="secao-14"></a>

### Python

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

<a id="verificacao-de-subgrafo"></a>
<a id="secao-15"></a>

## Verificação de subgrafo

**Dados dois grafos $G = (V,E)$ e $H = (V',E')$ com $V = V'$, crie um algoritmo que verifica se $H$ é subgrafo de $G$.**

Nesse problema, $V = V'$, então é possível usarmos matriz de adjacência tranquilamente (lista de adjacência também). Sabendo disso, vamos fazer para os dois casos:

<a id="secao-16"></a>

### Matriz de adjacência

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

### Lista de adjacência

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


## Conteúdos relacionados

- [Grafos — Ciência de Redes](../ciencia-de-redes/grafos.md)


## Percurso de estudo

[Trilha: Exercícios de slides](../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Técnicas de Projeto](tecnicas-de-projeto.md)
- Próximo: [Busca em Grafos](busca-em-grafos.md)
