---
layout: "default"
title: "Árvore Geradora Minima"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A2.md"
trilha: "../../../trilhas/projeto-e-analise-de-algoritmos/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 21
---

[Projeto e Análise de Algoritmos](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-32"></a>

# Árvore Geradora Minima


<a id="arvore-geradora-minima"></a>
<a id="secao-33"></a>

## Árvore Geradora Mínima

Uma árvore geradora de um grafo $G = (V,E)$ é um subgrafo $T$ que não possua ciclos e que contenha todos os vértices de $G$. Se um grafo $G$ possui uma árvore geradora, então ele é conexo (claro, uma árvore é conexa) e possui sempre $V - 1$ arestas. Considere abaixo grafos conexos e não-dirigidos.

Um **corte** é um conjunto de arestas que conecta duas partes de um grafo.Dado um conjunto $A$ de vértices, as arestas que possuem uma ponta em $A$ e a outra ponta no complemento de $Ã$ representam um corte.

![Exemplo de corte em grafo](../assets/minimal-tree-1.png)

*Figura 41. Exemplo de corte em grafo*

Dada uma árvore geradora, temos duas operações básicas:

- A adição de uma aresta em uma árvore geradora cria um ciclo.

- A remoção de uma aresta em uma árvore geradora cria um corte.

Dada uma árvore geradora $T$ e um grafo $G = (V,E)$, a propriedade dos ciclos consiste em :

- Se $e_{i} \notin T$, o grafo $T + e_{i}$ possui um único ciclo $C$.

- Se $e_{j} \in C$, o grafo $T + e_{i} - e_{j}$ é uma árvore geradora.

Claro que, se existir um $e_{k} \in T$, $T - e_{k}$ produz uma florest com duas componentes conexas em $G$.

Dada as mesmas coisas, a propriedade dos cortes consiste em:

- Dado $e_{i} \in T$ e $e_{j} \in \text{ corte}\left( T - e_{i} \right)$.

- $T - e_{i} + e_{j}$ é uma árvore geradora.

![Exemplo da propriedade dos cortes: Se retirarmos a aresta $(2,5)$, o corte que conectaria as duas árvores geradoras seria qualquer aresta $\left\lbrack (3,5),(3,6),(4,5),(4,6) \right\rbrack$.](../assets/minimal-tree-2.png)

*Figura 42. Exemplo da propriedade dos cortes: Se retirarmos a aresta $(2,5)$, o corte que conectaria as duas árvores geradoras seria qualquer aresta $\left\lbrack (3,5),(3,6),(4,5),(4,6) \right\rbrack$.*

Se $G = (V,E)$ for um grafo não-dirigido com custos nas arestas (com valores positivos e negativos), sabemos que o custo de um subgrafo $H$ de $G$ é calculado pelo somatório de custos das arestas em $H$. Com isso, podemos definir que uma **Árvore Geradora Mínima** (Mininum Spamming Tree - MST) de um grafo $G$ é qualquer árvore geradora cujo custo seja mínimo.

**Problema:** dado $G = (V,E)$ não-dirigido com custos nas arestas encontre uma árvore geradora mínima.

<a id="algoritmo-de-prim"></a>
<a id="secao-34"></a>

## Algoritmo de Prim

Esse algoritmo é capaz de encontrar a MST de um grafo $G = (V,E)$.

<a id="secao-35"></a>

### Prim Slow

Dada uma árvore $T$ de $G$, considere a franja de $T$ como o corte cuja margem é composta pelos vértices em $T$. Ideia geral do algoritmo:

1.  **Escolha a raiz de $T$**

2.  **Enquanto a franja não estiver vazia:**

    1.  **Escolha a aresta de menor custo**

    2.  **Insira a aresta e o vértice em $T$**

Vamos ver sua implementação:

![Exemplo da franja para $T = \left\{ 1,2,4 \right\}$, com as arestas em verde sendo a franja.](../assets/minimal-tree-3.png)

*Figura 43. Exemplo da franja para $T = \left\{ 1,2,4 \right\}$, com as arestas em verde sendo a franja.*

``` cpp
void mstPrimSlow(vertex * parent) {
    for (vertex v=0; v < m_numVertices; v++) { parent[v] = -1; }
    parent[0] = 0;
    while (true) {
        int min = INT_MAX;
        vertex treeV, newV = -1;
        for (vertex v1=0; v1 < m_numVertices; v1++) {
            if (parent[v1] == -1) { continue; }
            EdgeNode * edge = m_edges[v1];
            while (edge) {
                vertex v2 = edge->otherVertex();
                int cost = edge->cost();
                if (parent[v2] == -1 && cost < min) {
                    min = cost;
                    treeV = v1;
                    newV = v2;
                }
                edge = edge->next();
            }
        }
        if (min == INT_MAX) { break; }
        parent[newV] = treeV;
    }
}
```

O código preenche o vetor de `parent` e abrimos um while true que só para de funcionar quando o `min` não mudou durante toda uma interação. Iniciamos o min, e as variáveis `treeV`, que é o vértice pertencente a $T$, e `newV`, que é o vértice a ser avaliado.

Então, percorremos todos os vértices que já estão na árvore (chamamos de $v_{1}$ e fazemos a verificação vendo se eles já foram incluidos no vetor `parent`), e para cada aresta de `newV` (que chamamos de $v_{2}$), verificamos o custo de adicionar a árvore. Se for menor do que o mínimo, marcamos o respectivo pai e filho, e depois do for acabar, adicionamos essa aresta no vetor de `parent`.

**Implementação em Python**

``` py
def mst_prim_slow(v0, list_adj):
    num_vertices = len(list_adj)
    parent = [-1] * num_vertices
    parent[v0] = v0
    while True:
        min = float('inf')
        treeV, newV = -1, -1
        for i in range(num_vertices):
            if parent[i] == -1:
                continue
            for vizinho, custo in list_adj[i]:
                if parent[vizinho] == -1 and custo < min:
                    min = custo
                    treeV = i
                    newV = vizinho
        if min == float('inf'):
            break
        parent[newV] = treeV

    return parent
```

A ideia é a mesma, claro. Olhando para complexidade, a cada iteração, adicionamos um novo vértice à árvore. No pior caso, onde todos os vértices tem pai, o for passa por todas as arestas para adicionar um único vértice novo, e como rodamos até $V$ vezes, o algoritmo é $O(V + E)$.

A **corretude** do algoritmo pode ser avaliada através do critério de minimalidade baseado em cortes. Uma árvore geradora $T$ é uma MST se e somente se cada aresta $e_{k} \in T$ apresentar o menor custo no corte fundamental de $e_{k}$ relativo à $T$.

Uma coisa que podemos observar no algoritmo é que essa versão calcula a franja a cada iteração, em vez de modificar gradualmente à medida que a árvore é construída. Como melhoramos isso?

<a id="secao-36"></a>

### Prim Fast

Uma estratégia consiste em manter uma estrutura de dados com o custo de cada vértice que pode ser adicionado a $T$. Considere como **fronteira** todos os vértices que podem ser acessados à partir da franja e não pertencem a $T$. A nova ideia é:

1.  **Escolha a raiz de $T$**

2.  **Enquanto a franja não estiver vazia:**

    1.  **Procure $v_{k}$ na fronteira com o menor custo**

    2.  **Insira $V_{k}$ em $T$**

    3.  **Atualize a fronteira adicionando os acessíveis de $v_{k}$**

``` cpp
void mstPrimFastV1(vertex * parent) {
    bool inTree[m_numVertices];
    int vertexCost[m_numVertices];
    for (vertex v = 0; v < m_numVertices; v++) {
        parent[v] = -1;
        inTree[v] = false;
        vertexCost[v] = INT_MAX;
    }
    parent[0] = 0;
    inTree[0] = true;
    EdgeNode * edge = m_edges[0];
    while (edge) {
        vertex v2 = edge->otherVertex();
        parent[v2] = 0;
        vertexCost[v2] = edge->cost();
        edge = edge->next();
    }
    while (true) {
        int minCost = INT_MAX;
        vertex v1 = -1;
        for (vertex v = 0; v < m_numVertices; v++) {
            if (!inTree[v] && vertexCost[v] < minCost) {
                minCost = vertexCost[v];
                v1 = v;
            }
        }
        if (minCost == INT_MAX) {
            break;
        }
        inTree[v1] = true;
        edge = m_edges[v1];
        while (edge) {
            vertex v2 = edge->otherVertex();
            int cost = edge->cost();
            if (!inTree[v2] && cost < vertexCost[v2]) {
                vertexCost[v2] = cost;
                parent[v2] = v1;
            }
            edge = edge->next();
        }
    }
}
```

No código, usaremos três listas, e declaramos e preenchemos elas inicialmente. Após declararmos para o vértice inicial $0$ em `parent[0] = 0` e `inTree[0] = 1`, fazemos um while especificamente para as arestas do vértice inicial para preencher o array `vertexCost` com os respectivos pesos de cada vizinho.

Iniciamos um while para fazer a verificação de cada vértice, e iniciamos `minCost` e `v1`. Para cada vértice, verificamos se ele não está na árvore e se o custo desse vértice é menor que o mínimo. Se for, atualizamos o custo e o vértice. Verificamos a condição de parada e marcamos `v1` como true na árvore, pois é o menor que achamos.

Passamos no outro while por cada aresta do vértice selecionado para atualizar os custos dos seus vizinhos (`v2`). Verificamos se esse vizinho ainda não está incluído na árvore e se o peso da aresta atual é menor do que o custo que já tínhamos registrado para ele em `vertexCost`. Se for menor, atualizamos o `vertexCost[v2]` com esse novo peso (pois achamos uma conexão mais barata) e definimos o `parent[v2]` como sendo o `v1` (isso é a atualização da franja). Ao fim, temos o menor custo possível para cada vértice em `VertexCost` e a árvore mínima pelo `parent`.

**Implementação em Python**

``` py
def mst_prim_fastv1(list_adj):
    num_vertices = len(list_adj)
    parent = [-1] * num_vertices
    intree = [False] * num_vertices
    vertexcost = [float('inf')] * num_vertices
    parent[0] = 0
    intree[0] = True
    for vizinho, custo in list_adj[0]:
        parent[vizinho] = 0
        vertexcost[vizinho] = custo

    while True:
        mincost = float('inf')
        v1 = -1
        for v in range(num_vertices):
            if not intree[v] and vertexcost[v] < mincost:
                mincost = vertexcost[v]
                v1 = v
        if mincost == float('inf'):
            break
        intree[v1] = True
        for v2,custo in list_adj[v1]:
             if not intree[v2] and custo < vertexcost[v2]:
                vertexcost[v2] = custo
                parent[v2] = v1

    return parent
```

É análoga a ideia em C++. Analisando a complexidade, vemos que a cada iteração do while de fora, passamos por todos os vértices, e a cada aresta desse vértice. Como queremos passar por todos os vértices, sabemos que temos que fazer isso $V$ vezes. Isso intuitivamente dá, então, $O\left( V^{2} + E \right)$. Como $E < V^{2}$(ou $E \propto V^{2}$), isso é simplesmente $O\left( V^{2} \right)$. Será que tem como ficar ainda melhor?

<a id="secao-37"></a>

### Prim Fast V2

E se mantessemos os vértices da fronteira em ordem crescente de custo? Dessa forma, não seria necessário procurar o vértice que apresenta o menor custo à cada iteração (basta usar o famoso heap mínimo).

``` cpp
void mstPrimFastV2(vertex * parent) {
    bool inTree[m_numVertices];
    int vertexCost[m_numVertices];
    for (vertex v = 0; v < m_numVertices; v++) {
        parent[v] = -1;
        inTree[v] = false;
        vertexCost[v] = INT_MAX;
    }
    parent[0] = 0;
    inTree[0] = true;
    EdgeNode * edge = m_edges[0];
    while (edge) {
        vertex v2 = edge->otherVertex();
        parent[v2] = 0;
        vertexCost[v2] = edge->cost();
        edge = edge->next();
    }
    Heap heap;
    for (vertex v = 1; v < m_numVertices; v++) { 
        heap.insert_or_update(vertexCost[v], v); 
    }
    while (!heap.empty()) {
        vertex v1 = heap.top().second; 
        heap.pop(); 
        if (vertexCost[v1] == INT_MAX) {
            break;
        }
        inTree[v1] = true;
        edge = m_edges[v1];
        while (edge) {
            vertex v2 = edge->otherVertex();
            int cost = edge->cost();
            if (!inTree[v2] && cost < vertexCost[v2]) {
                vertexCost[v2] = cost;
                parent[v2] = v1;
                heap.insert_or_update(vertexCost[v2], v2);
            }
            edge = edge->next();
        }
    }
}
```

A implementação é muito parecida, e o que muda é que, antes de fazer o while principal, iniciamos o heap, e preenchemos com os custos iniciais de cada vértice (incluindo os que já atualizamos que vem da raiz). Ainda, no while principal, pegamos o topo diretamente do heap e depois retiramos ele ($\log(V)$), e, na hora de atualizarmos a franja, também inserimos no heap.

``` py
import heapq

def mst_prim_fastv2(v0, list_adj):
    num_vertices = len(list_adj)
    parent = [-1] * num_vertices
    intree = [False] * num_vertices
    vertexcost = [float('inf')] * num_vertices
    parent[v0] = v0
    intree[v0] = True
    for vizinho, custo in list_adj[v0]:
        parent[vizinho] = v0
        vertexcost[vizinho] = custo
    heap = []
    for v in range(num_vertices):
        if v != v0:
            heapq.heappush(heap, (vertexcost[v], v))

    while heap:
        custo_v1, v1 = heapq.heappop(heap)
        if intree[v1] or custo_v1 > vertexcost[v1]:
            continue
        if custo_v1 == float('inf'):
            break
        intree[v1] = True
        for v2, custo in list_adj[v1]:
            if not intree[v2] and custo < vertexcost[v2]:
                vertexcost[v2] = custo
                parent[v2] = v1
                heapq.heappush(heap, (vertexcost[v2], v2))

    return parent
```

Para a complexidade, muito parecido com o djikstra, o que vemos aqui é que temos um heap pop quando passamos por todos os vértices e temos um heap push quando temos que adicionar(ao passarmos pelas arestas). Ou seja, juntando com a explicação de complexidades anteriores, isso dá simplesmente $O\left( (V + E)\log(V) \right)$.

<a id="algoritmo-de-kruskal"></a>
<a id="secao-38"></a>

## Algoritmo de Kruskal

A estratégia desse algoritmo consiste em crescer uma floresta $F = (V',E')$ até que ela se torne uma árvore geradora $F = (V,E')$, diferente de crescer arbitrariamente como o Prim.

<a id="secao-39"></a>

### Kruskal Slow

Uma aresta $e_{k}$ é externa a floresta $F$ se $e_{k} \notin F$ e o grafo $F + e_{k}$ é uma floresta. Ideia geral do algoritmo:

1.  **Inicialize a floresta com todos os vértices e nenhuma aresta**

2.  **Escolha a aresta $e_{k} = \left( v_{i},v_{j} \right)$ de $G$ que possua o menor custo**

3.  **Insira $e_{k}$ em $F$.**

Vamos ver como seria a implementação disso:

``` cpp
void mstKruskalSlow(Edge * edges) {
    vertex group[m_numVertices];
    for (vertex v=0; v < m_numVertices; v++) { group[v] = v; }
    int k = 0;
    while (true) {
        int minCost = INT_MAX;
        vertex minV1, minV2 = -1;
        for (vertex v1=0; v1 < m_numVertices; v1++) {
            EdgeNode * edge = m_edges[v1];
            while (edge) {
                vertex v2 = edge->otherVertex();
                int cost = edge->cost();
                if (v1 < v2 && group[v1] != group[v2] && cost < minCost) {
                    minCost = cost;
                    minV1 = v1;
                    minV2 = v2;
                }
                edge = edge->next();
            }
        }
        if (minCost == INT_MAX) return;
        edges[k++] = Edge(minV1, minV2, minCost);
        vertex leaderV1 = group[minV1];
        vertex leaderV2 = group[minV2];
        for (vertex v=0; v < m_numVertices; v++) {
            if (group[v] == leaderV2) {
                group[v] = leaderV1;
            }
        }
    }
}
```

No algoritmo, recebemos uma lista vazia denominada `edges`, onde iremos colocar as arestas da forma `(vértice1, vértice2, custo)`. Criamos um vetor para entendermos de que parte da floresta cada vértice pertence, o `group`. E o `k` vai servir como contador de arestas. Após preenchermos cada vértice a cada grupo próprio, iniciamos o while com o `mincost` e o `minV1` e `minV2`, pra marcar a aresta.

Então, para cada vértice eu pego suas arestas, e faço 3 verificações para atualizar parâmetros:

- `v1 < v2` - Para evitar duplicatas em caso de grafo não dirigido, por exemplo a aresta $(0,1)$ é a mesma que $(1,0)$.

- `group[v2] != group[v1]` - as arestas devem ser de grupos diferentes, caso contrário certamente já pegamos a menor para a árvore.

- e o custo tem que ser menor que o último.

Se passou nessas verificações, então ele deve ser atualizado, e atualizamos a aresta de menor custo, em `minV1` e `minV2`. Após a verificação de contorno e a declaração de da aresta no edges. Por fim, salvamos os líderes de cada grupo e atualizamos o grupo de um dos grupos.

Que ideia do caramba!

**Implementação em Python**

``` py
def mst_kruskal_slow(list_adj):
    num_vertices = len(list_adj)
    group = [v for v in range(num_vertices)]
    edges = []
    while True:
        mincost = float('inf')
        minv1, minv2 = -1, -1
        for v in range(num_vertices):
            for vizinho, custo in list_adj[v]:
                if v < vizinho and group[v] != group[vizinho] and custo < mincost:
                    mincost = custo
                    minv1 = v
                    minv2 = vizinho

        if mincost == float('inf'):
            break
        edges.append((minv1, minv2, mincost))
        leader1 = group[minv1]
        leader2 = group[minv2]
        for v in range(num_vertices):
            if group[v] == leader2:
                group[v] = leader1

    return edges
```

A explicação é análoga à anterior, e, olhando para a complexidade, o while True passa em cada vértice $V$ vezes, e os dois primeiros fors passam por todas as arestas (a cada iteração!). Por fim, o for final percorre todos os vértices novamente, trazendo uma complexidade de $O\left( V(V + E) \right)$.

A corretude do algoritmo pode ser avaliada através do critério de minimalidade baseado em ciclos. Uma árvore geradora $T$ é uma MST de $G$ se e somente se cada aresta $e_{k} \notin T$ apresentar o maior custo no ciclo fundamental de $e_{k}$ relativo à $T$ (não entendi, e espero que vocês acreditem).

Essa versão é um pouco lenta pois:

- A cada iteração todas as arestas são verificadas em busca da com menor custo.

- A cada iteração todos os vértices são verificados para avaliar se é necessário atualizar seu grupo.

Como melhorar isso?

<a id="secao-40"></a>

### Kruskal Fast

Podemos ordenar as arestas por seu custo e utilizar uma estrutura de dados mais eficiente para fazer a busca e união dos vértices.

Na estrutura **union-find**, todo elemento é associado à um conjunto:

- `group[v] = v`, se for o líder do grupo;

- `group[v] = v'`, se não for o líder.

Essa representação força uma estrutura de árvore entre os elementos de mesmo conjunto (também armazenamos o tamanho).

Seguindo essa abordagem podemos comparar se dois elementos pertencem ao mesmo grupo verificando se o líder de cada grupo é o mesmo.

![Exemplo bobo do tal do union-find.](../assets/kruskal-1.png)

*Figura 44. Exemplo bobo do tal do union-find.*

Como precisamos chegar na raiz, isso consome até $O\left( \log(n) \right)$ no pior caso. A união de grupos passa a ser realizada definindo como pai do menor conjunto o pai do maior conjunto.

Voltando ao Kruskal, podemos otimizá-lo usando o que acabamos de aprender. Veja a ideia:

1.  **Inicialize a floresta com todos os vértices e sem nenhuma aresta**

2.  **Crie a lista de arestas ordenando-a pelo custo**

3.  **Para cada aresta $e_{k} = \left( v_{i},v_{j} \right)$**

    1.  **Obtenha os líderes dos vértices**

    2.  **Se forem diferentes, una-os**

    3.  **insira $e_{k}$ em $F$**

    4.  **Pare ao encontrar $V - 1$ arestas**

``` cpp
void mstKruskalFast(Edge * mstEdges) {
    vector<Edge> edges(m_numEdges);
    int currentEdge = 0;
    for (vertex v1=0; v1 < m_numVertices; v1++) {
        EdgeNode * edge = m_edges[v1];
        while (edge) {
            vertex v2 = edge->otherVertex();
            if (v1 < v2) {
                edges[currentEdge++] = Edge(v1, v2, edge->cost());
            }
            edge = edge->next();
        }
    }
    sort(edges.begin(), edges.end(), compareEdges);
    UnionFind uf(m_numVertices);
    currentEdge = 0;
    for (int e=0; currentEdge < m_numVertices - 1; e++) {
        Edge & edge = edges[e];
        vertex leaderV1 = uf.findE(edge.v1());
        vertex leaderV2 = uf.findE(edge.v2());
        if (leaderV1 != leaderV2) {
            uf.unionE(leaderV1, leaderV2);
            mstEdges[currentEdge++] = edge;
        }
    }
}
```

Após montar a estrutura edges bonitinha e ordenada pelo custo, fazemos literalmente o que foi dito no pseudocódigo - passamos por cada vértice, identificamos os líderes e, se os líderes forem diferentes, adicionamos na lista de retorno a aresta escolhida.

Não vou implementar isso em Python por falta de tempo

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/projeto-e-analise-de-algoritmos/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/projeto-e-analise-de-algoritmos/a2.md#apresentacao-original)

- Anterior: [Menor caminho em Grafos](../menor-caminho-em-grafos-a2/index.md)
