---
layout: "default"
title: "Menor caminho em grafos"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 13
---

[Projeto e Análise de Algoritmos](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-28"></a>

# Menor caminho em grafos


<a id="caminho-mais-curto-em-um-dag"></a>
<a id="secao-29"></a>

## Caminho mais curto em um DAG

**Dado um grafo $G = (V,E)$, como criar um algoritmo capaz de gerar a SPT de um DAG iniciando na sua única fonte?**

Lembre-se: nesse código, estamos considerando uma ordenação topológica já pré-determinada, por isso nosso for é simples e não precisamos olhar vértices novamente.

``` py
def dag_spt(list_adj):
    inf = len(list_adj)
    distance = [inf] * inf
    parent = [-1] * inf
    distance[0] = 0
    parent[0] = 0

    for i in range(inf):
        for vizinho in list_adj[i]:
            if distance[i] + 1 < distance[vizinho]:
                distance[vizinho] = distance[i] + 1
                parent[vizinho] = i

    return distance, parent
```

O código cria um vetor de distâncias e um vetor de pais de cada vértice, e preenche o inicial, considerando ordenação topológica. Graças a característica da ordenação topológica existente, o for que fazemos passa por cada vértice da lista, e depois por cada vizinho, verificando se suas arestas estão relaxadas ou não (considerando o peso de cada aresta sempre 1), se ela tiver tensa, então atualizamos com a distância do vetor pai $+ 1$.

Criamos dois vetores $O(V)$, e o for de fora passa por todos os vértices ($O(V)$) e o for de dentro passa por todos os vértices (no total, não a cada iteração), trazendo $O(E)$ ao final dos dois fors. Portanto, a complexidade é $\Theta(V + E)$.

<a id="caminho-mais-curto-em-grafo-nao-dirigido-com-ciclos"></a>
<a id="secao-30"></a>

## Caminho mais curto em grafo não-dirigido/com ciclos

**Dado um grafo $G = (V,E)$, implemente a adaptação do algoritmo BFS para encontrar o caminho mais curto entre um vértice e todos os acessíveis por ele.**

A diferença agora é que não fazemos o for na ordem dos vértices, ou seja, na ordem topológica, e agora, partimos de um $v_{0}$, e usamos um deque para administrar a ordem com que colocamos na fila, para fazermos uma busca em profundidade.

``` py
from collections import deque

def spt(v0, list_adj):
    inf = len(list_adj)
    distance = [inf] * inf
    parent = [-1] * inf
    distance[v0] = 0
    parent[v0] = 0

    fila = deque()
    fila.append(v0)
    while fila:
        v1 = fila.popleft()
        for vizinho in list_adj[v1]:
            if distance[vizinho] == inf:
                distance[vizinho] = distance[v1] + 1
                parent[vizinho] = v1
                fila.append(vizinho)

    return distance, parent
```

Agora, o nosso if também verifica apenas se a distância não foi alterada, trazendo assim apenas uma alteração por valor `distance[v]`. Ainda, como estamos fazendo uma verificação por nível, fica claro que a distância é sempre a do pai $+ 1$, e que agora também funciona em ciclos, já que ele só processa o vizinho se nunca tiver visto ele antes.

A complexidade é a mesma, já que o deque é $O(1)$ para tirar à esquerda e para appendar. É a mesma complexidade $O(V + E)$, pelos mesmos motivos.

Podemos avaliar a corretude desse algoritmo através das suas invariantes: primeiro, toda aresta $\left( v_{i},v_{j} \right)$ de $T$ (a árvore definida por parent) está relaxada com relação à distance; segundo, para cada aresta $\left( v_{i},v_{j} \right)$, se $v_{i}$ está em $T$ e $v_{j}$ está fora de $T$, então $v_{i}$ está na fila. Ao término da execução, a fila está vazia e, a partir da invariante (2), conclui-se que toda aresta com $v_{i}$ em $T$ também possui $v_{j}$ em $T$. O vetor distance é um potencial relaxado, portanto, $T$ é uma SPT e distance fornece o comprimento do caminho entre a raiz e os demais vértices acessíveis a partir dela.

<a id="djikstra-fast"></a>
<a id="secao-31"></a>

## Djikstra fast

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: Exercícios de slides](../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Busca em Grafos](../busca-em-grafos/index.md)
