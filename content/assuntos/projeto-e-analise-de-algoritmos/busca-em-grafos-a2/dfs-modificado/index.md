---
layout: "default"
title: "DFS modificado — Busca em Grafos"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A2.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 11
---

[Projeto e Análise de Algoritmos](../../index.md) · [Busca em Grafos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-21"></a>

# DFS modificado

Dado que o grau de entrada de cada vértice é no máximo $1$, podemos representar a floresta DFS como um vetor de pais (parents). Portanto, o algoritmo pode ser modificado para gerar a árvore DFS da seguinte forma:

Esse código assume a existência de tipos como ‘vertex’, ‘EdgeNode” e variáveis de membro como ‘m_numVertices” e ‘m_edges’, que seriam parte de uma classe de Grafo.

Esse código é bem parecido com o DFS anterior, a menos da marcação para ``parents``.

``` cpp
void dfs(int * preOrder, int * parents) {
    int counter = 0;
    for (vertex v=0; v < m_numVertices; v++) {
        preOrder[v] = -1;
        parents[v] = -1;
    }

    for (vertex v=0; v < m_numVertices; v++) {
        if (preOrder[v] == -1) {
            parents[v] = v; 
            dfsRecursive(v, preOrder, counter, parents, 0);
        }
    }
}


void dfsRecursive(vertex v1, int * preOrder, int & counter, int * parents, int level=0) {
    preOrder[v1] = counter++;
    EdgeNode * edge = m_edges[v1];
    while (edge) {
        vertex v2 = edge->otherVertex();
        if (preOrder[v2] == -1) {
            parents[v2] = v1; // Set parent first
            dfsRecursive(v2, preOrder, counter, parents, level + 1);
        }
        edge = edge->next();
    }
}
```

Focando na função ``dfs_parents``, e, usando lista de adjacência, criamos a lista de ordem e de pais, e o ``counter``(para marcação de pré-ordem) como $0$. Para cada item da ordem do vértice, se a pré-ordem for $- 1$, ou seja, se não tivermos descoberto o vértice ainda (procurando vértices de partida), então ele é marcado como item de partida (se referenciando ``parents\[i\] = i``). Após isso para cada vértice de partida, iniciamos a marcação.

No ``dfs_recursive_parents``, incrementamos o ``counter`` a cada uso da função (para atualizar o ``preorder``), e a cada filho da lista de adjacências, marca o vértice atual como pai (apenas se esse filho não tiver sido visitado, ignorando filhos já visitados por “outros pais”).

``` py
def dfs_recursive_parents(v_atual, preorder, parents, counter, adj_list):
    preorder[v_atual] = counter
    counter += 1
    for v_vizinho in adj_list[v_atual]:
        if preorder[v_vizinho] == -1:
            parents[v_vizinho] = v_atual  
            counter = dfs_recursive_parents(v_vizinho, preorder, parents, counter, adj_list)

    return counter

def dfs_parents(adj_list):
  num_vertices = len(adj_list)
  preorder = [-1] * num_vertices
  parents = [-1] * num_vertices
  counter = 0

  for v in range(num_vertices):
      if preorder[v] == -1:
          parents[v] = v   
          counter = dfs_recursive_parents(v, preorder,parents, counter, adj_list)
  return preorder, parents
```

Como isso funcionaria no exemplo que já vimos até agora?

![Exemplo do algoritmo ``dfs_parents`` para o grafo de exemplo.](../../assets/graph-search-example6.png)

*Figura 30. Exemplo do algoritmo ``dfs_parents`` para o grafo de exemplo.*

um vértice é **exaurido** (essa definição não é minha e não está nos slides do Thiago) no momento em que a busca já explorou todos os caminhos possíveis que saem daquele vértice.

Uma outra informação que podemos gerar a partir da execução de um DFS é a ordem em que os vértices são exauridos (essa sequência é conhecida como pós-ordem).

O algoritmo de DFS pode ser modificado de forma que registre o momento em que o algoritmo termina a avaliação do vértice, da seguinte forma:

``` cpp
void dfs(int * preOrder, int * postOrder,
         int * parents) {
    int preCounter = 0;
    int postCounter = 0;
    for (vertex v=0; v < m_numVertices; v++) {
        preOrder[v] = -1;
        parents[v] = -1;
        postOrder[v] = -1;
    }

    for (vertex v=0; v < m_numVertices; v++) {
        if (preOrder[v] == -1) {
            parents[v] = v;
            dfsRecursive(
                v, preOrder, preCounter,
                postOrder, postCounter, parents);
        }
    }
}

void dfsRecursive(vertex v1, int * preOrder, int & preCounter, int * postOrder,
                  int & postCounter, int * parents) {
    preOrder[v1] = preCounter++;
    EdgeNode * edge = m_edges[v1];
    while (edge) {
        vertex v2 = edge->otherVertex();
        if (preOrder[v2] == -1) {
            parents[v2] = v1;
            dfsRecursive(v2, preOrder, preCounter,
                         postOrder, postCounter, parents);
        }
        edge = edge->next();
    }
    postOrder[v1] = postCounter++;
}
```

Note que ele é o mesmo algoritmo que o do DFS modificado, a menos de uma declaração da lista de pós-ordem e preenchimento no fim do while, após exaurir o vértice. Note que

``` py
def dfs_recursive_full(v_atual, preorder, postorder, parents, pre_counter, post_counter, adj_list):
    preorder[v_atual] = pre_counter
    pre_counter += 1
    for v_vizinho in adj_list[v_atual]:
        if preorder[v_vizinho] == -1:
            parents[v_vizinho] = v_atual
            pre_counter, post_counter = dfs_recursive_full(v_vizinho, preorder, postorder, parents, pre_counter, post_counter, adj_list)
    postorder[v_atual] = post_counter
    post_counter += 1
    return pre_counter, post_counter

def dfs_full(adj_list):
    num_vertices = len(adj_list)
    preorder = [-1] * num_vertices
    postorder = [-1] * num_vertices
    parents = [-1] * num_vertices
    pre_counter = 0
    post_counter = 0
    for v in range(num_vertices):
        if preorder[v] == -1:
            parents[v] = v  
            pre_counter, post_counter = dfs_recursive_full(v, preorder, postorder, parents, pre_counter, post_counter, adj_list)
return preorder, postorder, parents
```

Focando na pós-ordem, como seria a execução desse algoritmo nos grafos que vimos até agora?

![Exemplo do algoritmo ``dfs_parents_full`` para o grafo de exemplo.](../../assets/graph-search-example7.png)

*Figura 31. Exemplo do algoritmo ``dfs_parents_full`` para o grafo de exemplo.*

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/projeto-e-analise-de-algoritmos/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/a2.md#apresentacao-original)

- Anterior: [Grafo topológico](../grafo-topologico/index.md)
- Próximo: [Propriedades úteis advindas do DFS](../propriedades-uteis-advindas-do-dfs/index.md)
