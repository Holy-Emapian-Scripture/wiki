---
layout: "default"
title: "Caminho mais barato em grafos — Menor caminho em Grafos"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A2.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 17
---

[Projeto e Análise de Algoritmos](../index.md) · [Menor caminho em Grafos](index.md)

<!-- wiki:original:inicio -->

<a id="secao-27"></a>

# Caminho mais barato em grafos


<a id="djikstra"></a>
<a id="secao-28"></a>

## Djikstra

Esse famoso algoritmo, que provavelmente você, caro leitor, já viu em MD, é capaz de encontrar caminhos mais baratos em um grafo $G = (V,E)$ que possua arestas com custos positivos.

A solução consiste em crescer uma árvore radicada a partir do vértice inicial $v_{0}$ até que ela seja uma árvore geradora do subgrafo induzido a partir de $v_{0}$.

Antes de explicar melhor, a **franja** de uma árvore radicada $T$ com raiz em $v_{0}$ é o conjunto das arestas $\left( v_{i},v_{j} \right)$ que possuem $v_{i}$ em $T$ e $v_{j}$ fora de $T$. A franja pode ser vista como o grau de saída do conjunto de vértices de $T$.

![Exemplo de franja. Os vértices $(1,2,3)$ já estão árvore radicada, e a franja é o conjuntos de arestas pontilhadas de peso $(2,4,1)$.](../assets/djikstra-1.png)

*Figura 38. Exemplo de franja. Os vértices $(1,2,3)$ já estão árvore radicada, e a franja é o conjuntos de arestas pontilhadas de peso $(2,4,1)$.*

Depois de entender esse conceito, essa é a ideia geral para o Djikstra:

1.  **insira** $v_{0}$ **em** $T$

2.  **defina** $d\left\lbrack v_{0} \right\rbrack = 0$

3.  **enquanto a franja não estiver vazia:**

    1.  **escolha $v_{k}$ de menor distância**

    2.  **aplique a operação de relaxamento em todas as arestas de $v_{k}$ da franja**

    3.  **insira $v_{k}$ em $T$**

Veja a implementação em C++:

``` cpp
void cptDijkstraSlow(vertex v0, vertex *parent, int *distance) {
  std::vector<bool> checked(m_numVertices);
  for (vertex v = 0; v < m_numVertices; v++) {
      parent[v] = -1;
      distance[v] = INT_MAX;
      checked[v] = false;
  }
  parent[v0] = v0;
  distance[v0] = 0;

  while (true) {
      int minDistance = INT_MAX;
      vertex v1 = -1;
      for (vertex i = 0; i < m_numVertices; i++) {
          if (!checked[i] && distance[i] < minDistance) {
              minDistance = distance[i];
              v1 = i;
          }
      }
      if (minDistance == INT_MAX || v1 == -1) break;
      checked[v1] = true;
      EdgeNode *edge = m_edges[v1];
      while (edge) {
          vertex v2 = edge->otherVertex();
          if (!checked[v2]) {
              int cost = edge->cost();
              if (distance[v1] != INT_MAX && distance[v1] + cost < distance[v2]) {
                  parent[v2] = v1;
                  distance[v2] = distance[v1] + cost;
              }
          }
          edge = edge->next();
      }
  }
}
```

O algoritmo inicializa os vetores do começo `parent`, `distance` e `checked`, e declara as informações iniciais de $v_{0}$. Depois, inicializa um while onde, a cada iteração declara a maior distância como um inteiro máximo, e, após isso, o vértice escolhido de $- 1$(pois não escolhemos ainda). Nosso objetivo no for de baixo é escolher, dentre os que tem distância definida e ainda não foram checados (ou seja, a franja), quem tem a menor distância. Após selecionar esse vértice e verificarmos a condição de parada(se a menor distância não mudou, então não temos mais vértices para checar), marcamos ele como checado e fazemos a análise para cada vizinho.

Para cada vizinho, chamamos de $v_{2}$ o vizinho a ser analisado. Se ele não tiver sido checado, pegamos o seu custo e se a distância do $v_{1} +$ custo da aresta for menor, então atualizamos a distância e o pai de $v_{2}$, e passamos para o próximo vértice. (a outra verificação desse if é pra evitar overflow).

**Implementação em Python**

Aqui, consideramos que a [lista de adjacências](../grafos.md#secao-12) é da forma:

``` py
[
[(vértice, custo), (vértice, custo)], #arestas do vértice 0
[(vértice, custo), (vértice, custo)], #arestas do vértice 1
]
```

Isso é apenas a transformação do código para Python, usando essa estrutura mais simples, que fica dessa forma:

``` py
def cpt_djikstra_slow(v0, list_adj):
    num_vertices = len(list_adj)
    checked = [0] * num_vertices
    parent = [-1] * num_vertices
    distance = [float('inf')] * num_vertices
    parent[v0] = v0
    distance[v0] = 0

    while True:
        mindistance = float('inf')
        v1 = -1
        for i in range(num_vertices):
            if checked[i] == False and distance[i] < mindistance:
                mindistance = distance[i]
                v1 = i
        if mindistance == float('inf') or v1 == -1:
            break
        checked[v1] = True
        for vizinho, custo in list_adj[v1]:
            if checked[vizinho] == False:
                if distance[v1] != float('inf') and distance[v1] + custo < distance[vizinho]:
                    parent[vizinho] = v1
                    distance[vizinho] = distance[v1] + custo

    return parent,  distance
```

Esse código é bem parecido com os que já vimos, ele faz várias declarações de variáveis $O(V)$, e o while True roda no máximo $V$ vezes, já que depende de um for que roda também $V$ vezes (pois a verificação em algum intervalo $\lbrack 0,\vert V⟧$ é interrompida, porque cai no caso de condição de parada). Esse for só faz verificações constantes, e por isso é $O(V)$. continuando, temos um if e outro for que passa por $g_{s}\left( v_{k} \right)$ arestas, que ao final somam $E$. Portanto, dentro do while temos $O\left( V\left( V + g_{s}\left( v_{k} \right) \right) \right) = O\left( V^{2} + E \right)$, já que $\sum_{i = 1}^{\vert V\vert }g_{s}\left( v_{i} \right) = \vert E\vert$.

Existe uma característica importante nesse algoritmo: a cada iteração onde verificamos o elemento da franja a ser escolhido (passando por mais elementos que o necessário para escolher o menor, pois passamos por todos), uma iteração qualquer é sempre semelhante à iteração anterior. Com essa informação, como podemos melhorar o desempenho do algoritmo?

<a id="djikstra-rapido"></a>
<a id="secao-29"></a>

## Djikstra “Rápido”

**Ideia**: manter os vértices da franja em uma fila de prioridades, implementada como um heap mínimo e que contém todos os vértices que ainda não foram verificados.

![Exemplo do estado do algoritmo após processar o vértice 1. A imagem à esquerda mostra o heap nessa iteração.](../assets/djikstra-4.png)

*Figura 39. Exemplo do estado do algoritmo após processar o vértice 1. A imagem à esquerda mostra o heap nessa iteração.*

Esse é o código em C++:

``` cpp
void cptDijkstraFast(vertex v0, vertex * parent, int * distance) {
    bool checked[m_numVertices];
    Heap heap; // Create the heap
    for (vertex v=0; v < m_numVertices; v++) {
        parent[v] = -1;
        distance[v] = INT_MAX;
        checked[v] = false;
    }
    parent[v0] = v0;
    distance[v0] = 0;

    heap.insert_or_update(distance[v0], v0);
    while (!heap.empty()) {
        vertex v1 = heap.top().second; // Min vertex
        heap.pop(); // Remove from heap
        if (distance[v1] == INT_MAX) { break; }
        EdgeNode * edge = m_edges[v1];
        while (edge) {
            vertex v2 = edge->otherVertex();
            if (!checked[v2]) {
                int cost = edge->cost();
                if (distance[v1] + cost < distance[v2]) {
                    parent[v2] = v1;
                    distance[v2] = distance[v1] + cost;
                    heap.insert_or_update(distance[v2], v2);
                }
            }
            edge = edge->next();
        }
        checked[v1] = true;
    }
}
```

Sabendo que o heap ordena pelo menor valor e no caso de adicionarmos (distância, vértice) ele ordena pelo primeiro elemento, o código atualiza o heap inicial com $v_{0}$, e, enquanto o heap não estiver vazio, chamamos de $v_{2}$ o próximo vizinho e, se ele não tiver sido visitado, acessa seu custo e verifica se pode relaxar a aresta. Se puder, adiciona também ao heap. Por fim, marca como checado.

**Implementação em Python**

``` py
import heapq

def cpt_dijkstra_fast(v0, list_adj):
    num_vertices = len(list_adj)
    checked = [False] * num_vertices
    parent = [-1] * num_vertices
    distance = [float('inf')] * num_vertices
    parent[v0] = v0
    distance[v0] = 0
    heap = []
    heapq.heappush(heap, (0, v0))

    while heap:
        dist_v1, v1 = heapq.heappop(heap)
        if dist_v1 > distance[v1]:
            continue
        if distance[v1] == float('inf'):
            break
        for v2, cost in list_adj[v1]:
            if not checked[v2]:
                if distance[v1] + cost < distance[v2]:
                    parent[v2] = v1
                    distance[v2] = distance[v1] + cost
                    heapq.heappush(heap, (distance[v2], v2))
        checked[v1] = True
    return parent, distance
```

A explicação é análoga. Para analisar a complexidade, note que o heappop é feito dentro do while que acontece para cada vértice(pois o while heap roda no máximo $V$ vezes), e que o heappush acontece dentro do for das arestas (que já discutirmos ter complexidade $E$). Portanto, é fácil ver que a complexidade é $O\left( \log(V)(V + E) \right)$. Note:

- Se todos os vértices forem acessíveis a partir de $v_{0}$, temos $O\left( E\log(V) \right)$ (pois isso significa que o grafo é conexo e, sabemos que $E \geq V - 1$, e, por isso, $E$ domina).

- Se o grafo for esparso (onde $E \approx V$), a complexidade será $O\left( V\log(V) \right)$.

- Se o grafo for denso (onde $E \approx V^{2}$), temos que a complexidade é $O\left( V^{2}\log(V) \right)$.Ou seja, apresenta um desempenho inferior à abordagem anterior, que mantém $O\left( V^{2} \right)$ fixo independentemente da densidade das arestas.

<a id="secao-30"></a>

## eventualmente adicionar corretude

Por fim, como seria a implementação de um algoritmo que funcionasse em grafos com ciclos negativos?

<a id="bellman-ford"></a>
<a id="secao-31"></a>

## Bellman-Ford

Esse algoritmo é capaz de encontrar caminhos mais baratos em um grafo $G = (V,E)$ mesmo que as arestas possuam custos positivos e negativos. Ele retorna falso se detectar um ciclo negativo.

O algoritmo consiste em relaxar as arestas do grafo sistematicamente,reduzindo progressivamente uma estimativa $d\lbrack v\rbrack$ para cada vértice $v \in V$ do grafo, até alcançar a menor distância.

Essa é a ideia geral:

1.  **insira** $v_{0}$ **em** $T$

2.  **defina** $d\left\lbrack v_{0} \right\rbrack = 0$

3.  **execute V - 1 vezes:**

    1.  **para cada arsta $\left( v_{i},v_{j} \right)$:**

        1.  **aplique o relaxamento**

4.  **execute o relaxamento sobre todas as arestas**

    1.  **se alguma distância $d\left\lbrack v_{k} \right\rbrack$ for reduzida, ciclo negativo**

O algoritmo executa as primeiras $V - 1$ iterações construindo caminhos com 1 aresta, 2 arestas, até $V - 1$ arestas, pois sabemos que um caminho simples pode ter no máximo $V - 1$ arestas. Antes de implementarmos o algoritmo, vejamos como ele ocorreria para o grafo de exemplo.

![Exemplo do estado do algoritmo Bellman-Ford](../assets/bellman-ford-1.png)

*Figura 40. Exemplo do estado do algoritmo Bellman-Ford*

Note que temos 6 iterações, 5 dos $V - 1$ vértices e o último é a verificação do ciclo negativo. Vamos analisar de perto da primeira iteração: Indo em ordem e sendo o vértice $0$ como raiz, temos a distância para ele é $0$. Vendo seus filhos, ele adiciona que a distância para o vértice $2$ é $7$, e para o $3$ $9$, então temos o vetor de distâncias como $\lbrack 0,7,9, - , - , - \rbrack$.

Na próxima iteração, temos vamos analisar o vértice $2$. Como ele tem uma distância, significa que podemos chegar nele dos vértices que já descobrimos, então podemos realizar a análise. Ele coloca distância $9$ no vértice $4$, e distância $11$ no vértice $5$. Temos então $\lbrack 0,7,9,9,11, - \rbrack$.

Com $i = 2$, estamos no vértice $3$ e atualizamos a distância para o $5$, ficando com $\lbrack 0,7,9,9,10, - \rbrack$.

No vértice $4$ não conseguimos mudar o valor de nada, já que só mudaríamos no 5, que já é um valor menor.

No vértice $5$, conseguimos mudar o valor do vértice $2$ e ao vértice $6$, e somando $- 6$ ao custo do $5$ (para o $2$) e $2$ ao custo do $5$(para o $6$), chegamos em $\lbrack 0,4,9,9,10,12\rbrack$.

Como o último vértice não tem nenhuma aresta de saída, a primeira iteração se encerra como $\lbrack 0,4,9,9,10,12\rbrack$.

Vamos ver como programar esse algoritmo:

``` cpp
bool cptBellmanFord(vertex v0, vertex * parent, int * distance) {
    for (int v=0; v < m_numVertices; v++) {
        parent[v] = -1;
        distance[v] = INT_MAX;
    }
    parent[v0] = v0;
    distance[v0] = 0;
    for (int i=1; i <= m_numVertices - 1; i++) {
        for (int v1 = 0; v1 < m_numVertices; v1++) {
            EdgeNode * edge = m_edges[v1];
            while (edge) {
                vertex v2 = edge->otherVertex();
                int cost = edge->cost();
                if (distance[v1] + cost < distance[v2]) {
                    parent[v2] = v1;
                    distance[v2] = distance[v1] + cost;
                }
                edge = edge->next();
            }
        }
    }
    for (int v1=0; v1 < m_numVertices; v1++) {
        EdgeNode * edge = m_edges[v1];
        while (edge) {
            vertex v2 = edge->otherVertex();
            int cost = edge->cost();
            if (distance[v1] + cost < distance[v2]) {
                return false;
            }
            edge = edge->next();
        }
    }
    return true;
}
```

A explicação já foi explicada, o algoritmo apenas passa por todas as arestas do grafo (pois o for de dentro passa por todos os vértices acessando todas as arestas) $V - 1$, ou seja, temos uma complexidade fácil de $O(VE)$.

**Implementação em Python**

``` py
def bellman_ford(v0, list_adj):
    num_vertices = len(list_adj)
    parent = [-1] * num_vertices
    distance = [float('inf')] * num_vertices
    parent[v0] = v0
    distance[v0] = 0
    for i in range(num_vertices - 1):
        for j in range(num_vertices):
            for vizinho, custo in list_adj[j]:
                if distance[j] + custo < distance[vizinho]:
                    parent[vizinho] = j
                    distance[vizinho] = distance[j] + custo

    for j in range(num_vertices):
        for vizinho, custo in list_adj[j]:
            if distance[j] + custo < distance[vizinho]:
                return False

    return parent, distance
```

Show! Mas, como achar a árvore mais barata que gera o grafo??

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/projeto-e-analise-de-algoritmos/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/projeto-e-analise-de-algoritmos/a2.md#apresentacao-original)

- Anterior: [Caminho mais curto em grafos não-dirigidos/ciclo](caminho-mais-curto-em-grafos-nao-dirigidos-ciclo.md)
- Próximo: [Árvore Geradora Minima](../arvore-geradora-minima.md)
