---
layout: "default"
title: "Busca em Grafos"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 9
---

[Projeto e Análise de Algoritmos](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-18"></a>

# Busca em Grafos


<a id="verificacao-de-caminho-e-caminho-simples"></a>
<a id="secao-19"></a>

## Verificação de caminho e caminho simples

**Dado um grafo $G = (V,E)$ e um caminho $P$ composto por uma sequência de vértices, verifique se $P$ é um caminho de $G$, e se o caminho é simples.**

<a id="secao-20"></a>

### Matriz de adjacência

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

### Lista de adjacência

Basta passar a lista e a cada $v_{i}$ e $v_{i + 1}$ verificar se existe o vértice na lista de arestas de $v_{i}$

``` py
def is_path_list(list, path):
    for order in range(len(path) - 1):
        if path[order + 1] not in list[path[order]]:
            return False
    return True
```

<a id="verificacao-de-numeracao-topologica"></a>
<a id="secao-22"></a>

## Verificação de númeração topológica

**Crie um algoritmo que verifica se a numeração dos vértices de um grafo $G = (V,E)$ é topológica.**

<a id="secao-23"></a>

### Matriz de adjacência

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

### Lista de adjacência

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

<a id="verificacao-de-ordenacao-topologica-e-determinacao"></a>
<a id="secao-25"></a>

## Verificação de ordenação topológica (e determinação)

**Crie um algoritmo para determinar se um grafo possui ordenação topológica e determiná-la.**

<a id="secao-26"></a>

### Versão Slow (lista de adjacência)

Nessa versão, usamos a lista de ordem, counter e o número de vértices novamente. Então enquanto não preenchermos a lista de ordem corretamente (ou seja, `counter < V`), tentamos achar algum vértice com característica que nos ajudará a identificar a topologia do grafo, ou seja, se o grau de entrada do vértice é 0 (indício de fonte) e o vértice ainda não foi colocado na ordem.

Se nessa procura não acharmos esse vértice, então não temos essa ordenação topológica, e retornamos False. Se isso não ocorreu, então significa que o for parou exatamente no índice do vértice que satisfaz essas condições. Portanto marcamos ele na lista de ordem. Incrementamos o counter, e, por fim, decrementamos dos graus de saída dos vértices ligados ao vértice de fonte selecionado $i$, simulando a remoção do vértice.

``` py
def in_degree(list_adj):
    V = len(list_adj)
    in_d = [0] * V
    for v1 in list_adj:
        for v2 in v1:
            in_d[v2] += 1
    return in_d 

def has_topologic_order(list_adj):
    num_vertices = len(list_adj)
    order = [-1] * num_vertices
    counter = 0
    in_degre = in_degree(list_adj)
    while counter < num_vertices:
        i = 0
        while i < num_vertices:
            if in_degre[i] == 0  and order[i] == -1:
                break
            i += 1
        if i >= num_vertices:
            return False
        order [i] = counter
        counter += 1
        for v in list_adj[i]:
            in_degre[v] -= 1
    return True
```

A complexidade do `in_degree()` tem complexidade $O(V + E)$, já que passa em cada vértice pelas suas arestas que estão ligadas a ela.

Isso tem complexidade de bastante. Como melhorar isso?

<a id="secao-27"></a>

### Versão rápida (lista de adjacência)

Nessa nova ideia, usamos uma fila. Chamamos a função de contagem de graus de entrada, e declaramos a queue. Adicionamos todas as fontes iniciais na queue, e criamos o counter e a lista da ordem topológica.

Enquanto a queue não estiver vazia, guardamos o primeiro elemento da fila e o retiramos. Para cada vértice ligado na fonte, decrementamos sua saída, e se ela for zero, é uma nova fonte que adicionamos na queue.

``` py
from collections import deque       #uma fila com ponteiro de entrada e saída

def has_topologic_order(list_adj):
    num_vertices = len(list_adj)
    in_degre = in_degree(list_adj)
    queue = deque()
    for i in range(num_vertices):
        if in_degre[i] == 0:
            queue.append(i)
    topological_order = []
    counter = 0

    while queue:
        u = queue.popleft() 
        topological_order.append(u)
        counter += 1
        for v in list_adj[u]:
            in_degre[v] -= 1
            if in_degre[v] == 0:
                queue.append(v)

    if counter == num_vertices:
        return topological_order  
    else:
        return None
```

`in_degree()` é $O(V + E)$, o primeiro for é $O(V)$, e o while passa ou deveria passar, se existir a ordem topológica, em todos os vértices, e dentro dele ainda passamos por todos as suas ligações, trazendo $O(V + E)$, ou seja, $O(V + E) + O(V + E) + O(V) = O(V + E)$.

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: Exercícios de slides](../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Grafos](../grafos/index.md)
- Próximo: [Menor caminho em grafos](../menor-caminho-em-grafos/index.md)
