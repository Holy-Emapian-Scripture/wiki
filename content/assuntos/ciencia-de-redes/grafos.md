---
layout: "default"
title: "Grafos"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A1.md"
trilha: "../../../trilhas/ciencia-de-redes/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 1
---

[Ciência de Redes](index.md)

<!-- wiki:original:inicio -->
<a id="secao-1"></a>

# Grafos

------------------------------------------------------------------------

De antemão valhe ressaltar que essa matéria, por mais que seja chamada de **Ciência de Redes**, o termo **rede** se refere a um grafo, não ao tipo específico de grafo que se é visto em **Fluxo em Redes** quando estudamos matemática discreta. Então que já fique esclarecido de antemão que, ao citarmos redes, estamos nos referindo a um grafo no geral, desde que o contrário seja explicitado

Essa sessão será apenas algumas definições que não foram passadas no curso de Matemática Discreta, então conceitos que forem citados sobre grafos e não houver definição nesse resumo, a mesma estará no recap de Matemática Discreta. Aqui segue algumas notações sobre grafos para que não fique confuso:

- $G(V,E) ≔$ Grafo com conjunto de vértices $V$ e de arestas $E$ (edges)

- $N(v) ≔$ Vizinhança do vértice $v$ (Neighbourhood)

- $\delta(v) ≔$ Grau do vértice $v$

- $K_{n} ≔$ Grafo completo com $n$ vértices

- $K_{m,n} ≔$ Grafo completo bipartido com $m$ vértices no primeiro conjunto e $n$ vértices no segundo

- $Χ(G) ≔$ Número cromático de $G$

- $Χ'(G) ≔$ Número cromático por arestas de $G$

**Definição: Grau Médio**

Dado um grafo não-dirigido $G(V,E)$, o grau médio de $G$ é: $$\delta_{\text{med }}(G) ≔ \frac{1}{\vert V\vert }\sum_{v_{i} \in V}\delta(v_{i})$$ Se G é dirigido, podemos definir os graus médios de entrada e saída $$\delta_{\text{med}}^{\text{in }}(G) ≔ \frac{1}{\vert V\vert }\sum_{v_{i} \in V}\delta^{\text{in }}\left( v_{i} \right)\ \ \ \text{ Entrada }$$ $$\delta_{\text{med}}^{\text{out }}(G) ≔ \frac{1}{\vert V\vert }\sum_{v_{i} \in V}\delta^{\text{out }}\left( v_{i} \right)\ \ \ \text{ Saída }$$

**Definição: Distribuição do Grau**

A distribuição do grau de um Grafo $G(V,E)$ é a distribuição da variável aleatória $X$, sendo $X$ o grau do vértice que eu escolho ao acaso

**Para os teoremas a seguir e daqui em diante, consideremos a matriz de incidência de forma que $A_{ij} = 1$ se a aresta $j$ se conecta no vértice $i$ e, 0 do contrário (-1 se $G$ for dirigido).**

**Teorema**

Dado um grafo $G(V,E)$ e sua matriz de incidência $A$, temos que: $$\text{ nº de ciclos } = \vert E\vert  - \text{ posto}(A)$$

**Demonstração**

$$
\begin{array}{r} \text{ posto(A) } + \dim(N(A)) = \vert E\vert  \\ \Leftrightarrow \vert E\vert  - \text{ posto(A) } = \dim(N(A)) \end{array}
$$

Porém, a dimensão do núcleo de $A$ é a quantidade de ciclos no grafo, então eu tenho que:

$$
\text{ nº de ciclos } = \vert E\vert  - \text{ posto}(A)
$$

**Definição: [Coeficiente de Clustering](redes-aleatorias.md#secao-12)**

Dado um grafo $G(V,E)$, o coeficiente de clustering de um nó $v \in V$ é: $$C(v) ≔ \frac{2E_{v}}{\delta(v)\left( \delta(v) - 1 \right)}$$ onde $E_{v}$ é a quantidade de arestas que ligam os **vizinhos** de $v$ entre si

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Conteúdos relacionados

- [Grafos — Projeto e Análise de Algoritmos](../projeto-e-analise-de-algoritmos/grafos-a2.md)
- [Grafos — Projeto e Análise de Algoritmos](../projeto-e-analise-de-algoritmos/grafos.md)

## Percurso de estudo

[Trilha: A1](../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Próximo: [Medidas de Centralidade](medidas-de-centralidade.md)
