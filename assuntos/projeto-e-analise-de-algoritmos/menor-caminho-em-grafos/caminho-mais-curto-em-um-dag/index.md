---
layout: "default"
title: "Caminho mais curto em um DAG — Menor caminho em grafos"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 14
---

[Projeto e Análise de Algoritmos](../../index.md) · [Menor caminho em grafos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-29"></a>

# Caminho mais curto em um DAG

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

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios de slides](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Menor caminho em grafos](../index.md)
- Próximo: [Caminho mais curto em grafo não-dirigido/com ciclos](../caminho-mais-curto-em-grafo-nao-dirigido-com-ciclos/index.md)
