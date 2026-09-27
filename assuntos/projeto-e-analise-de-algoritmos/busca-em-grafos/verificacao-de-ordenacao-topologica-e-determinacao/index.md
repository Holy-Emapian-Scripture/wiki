---
layout: "default"
title: "Verificação de ordenação topológica (e determinação) — Busca em Grafos"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 12
---

[Projeto e Análise de Algoritmos](../../index.md) · [Busca em Grafos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-25"></a>

# Verificação de ordenação topológica (e determinação)

**Crie um algoritmo para determinar se um grafo possui ordenação topológica e determiná-la.**

<a id="secao-26"></a>

## Versão Slow (lista de adjacência)

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

## Versão rápida (lista de adjacência)

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

[Trilha: Exercícios de slides](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Verificação de númeração topológica](../verificacao-de-numeracao-topologica/index.md)
- Próximo: [Menor caminho em grafos](../../menor-caminho-em-grafos/index.md)
