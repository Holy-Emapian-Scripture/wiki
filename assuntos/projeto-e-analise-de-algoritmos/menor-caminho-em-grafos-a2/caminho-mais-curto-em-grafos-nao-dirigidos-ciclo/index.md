---
layout: "default"
title: "Caminho mais curto em grafos não-dirigidos/ciclo — Menor caminho em Grafos"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A2.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 16
---

[Projeto e Análise de Algoritmos](../../index.md) · [Menor caminho em Grafos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-26"></a>

# Caminho mais curto em grafos não-dirigidos/ciclo

A comparação $d\left\lbrack v_{i} \right\rbrack + 1 \leq d\left\lbrack v_{j} \right\rbrack$ e a eventual atualização no vetor de distância é conhecida como **operação de relaxamento.** Uma aresta está **relaxada** se $d\left\lbrack v_{j} \right\rbrack - d\left\lbrack v_{i} \right\rbrack \leq 1$ e **tensa** se $d\left\lbrack v_{j} \right\rbrack - d\left\lbrack v_{i} \right\rbrack > 1$.

**Exemplo**

estou no vértice $v_{i}$, e quero ir para o meu vizinho $v_{j}$, sabendo que $d\lbrack v\rbrack$ é a distância mínima conhecida até agora da origem até aquele vértice. Se $d\left\lbrack v_{j} \right\rbrack - d\left\lbrack v_{i} \right\rbrack \leq 1$ (considerando que os pesos são inteiros e unitários), significa que a aresta $\left( e_{i},e_{j} \right)$, mesmo com peso 1, não conseguiria fazer com que o valor de $d\left\lbrack v_{j} \right\rbrack$ mude, pois ele já é o menor possível, e então essa aresta é relaxada. Pelo contrário, se $d\left\lbrack v_{j} \right\rbrack - d\left\lbrack v_{i} \right\rbrack > 1$, significa que se o peso da aresta entre os dois vértices é 1, então $d\left\lbrack v_{j} \right\rbrack$ consegue ser atualizado, por isso é uma aresta tensa.

Chamamos de potencial relaxado uma numeração para os vértices que torne todas as aresta do grafo relaxadas. O vetor de distâncias resultante do algoritmo anterior é um potencial relaxado.

Voltando ao problema inicial: desejamos encontrar o caminho mais curto entre dois vértices em qualquer grafo. Como produzir uma solução para grafos não-dirigidos e/ou que possuem ciclos?

Podemos adaptar o algoritmo de busca em largura (BFS) de forma que a numeração dos vértices represente a distância para a raiz.

**Ideia geral:** modificar o ciclo do BFS para remover o vértice $v_{i}$ da fila, visitar seus vértices adjacentes e:

- se $d\left\lbrack v_{j} \right\rbrack$ não estiver definida:

  - $d\left\lbrack v_{j} \right\rbrack = d\left\lbrack v_{i} \right\rbrack + 1$

  - $\text{parent}\left\lbrack v_{j} \right\rbrack = v_{i}$

  - inserir $v_{j}$ na fila

Note que o valor $d\lbrack v\rbrack$ é alterado somente uma vez.

**Nota:** a implementação disso está nos Exercises

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/projeto-e-analise-de-algoritmos/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/a2.md#apresentacao-original)

- Anterior: [Caminho mais curto em um DAG](../caminho-mais-curto-em-um-dag/index.md)
- Próximo: [Caminho mais barato em grafos](../caminho-mais-barato-em-grafos/index.md)
