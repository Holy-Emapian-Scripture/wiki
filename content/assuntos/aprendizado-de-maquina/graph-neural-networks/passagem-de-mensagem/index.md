---
layout: "default"
title: "Passagem de Mensagem — Graph Neural Networks"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 17
---

[Aprendizado de Máquina](../../index.md) · [Graph Neural Networks](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-20"></a>

# Passagem de Mensagem

As redes em grafo funcionam de forma que as informações de cada nó são passadas para seus vizinhos, que por sua vez passam as informações para seus vizinhos, e assim por diante. Esse processo é chamado de **passagem de mensagem** (message passing). A passagem de mensagem é um processo iterativo que ocorre em $T$ rodadas, onde $T$ é um hiperparâmetro do modelo. Em cada rodada $t$, cada nó $v$ recebe mensagens de seus vizinhos $\mathcal{N}(v)$ e atualiza seu estado com base nessas mensagens. Podemos dividir o processo aplicado à cada nó como: $$\begin{array}{rlr} m_{v}^{(t)} & = \text{ AGGREGATE}^{(t)}\left( \left\{ h_{u}^{(t - 1)},\forall u \in \mathcal{N}(v) \right\} \right)\text{\quad\quad} & \forall v \in V \\ h_{v}^{(t)} & = \text{ UPDATE}^{(t)}\left( h_{v}^{(t - 1)},m_{v}^{(t)} \right)\text{\quad\quad} & \forall v \in V \end{array}$$ de forma que $h_{v}^{(0)} = x_{v}$

As funções $\text{AGGREGATE}$ e $\text{UPDATE}$ são funções que variam dependendo da implementação, de forma que diferentes implementações de GNNs podem ser obtidas. A função $\text{AGGREGATE}$ é responsável por agregar as informações dos vizinhos de um nó, enquanto a função $\text{UPDATE}$ é responsável por atualizar o estado do nó com base nas informações agregadas. A escolha dessas funções é crucial para o desempenho da GNN e pode ser feita de várias maneiras, incluindo somas, médias, máximos ou redes neurais.

Podemos reformular de forma mais compacta a passagem de mensagem definindo: $$\begin{array}{r} H^{(t)} = \begin{pmatrix} - & h_{1}^{(t)} & - \\ & \vdots & \\ - & h_{\vert V\vert }^{(t)} & - \end{pmatrix} \\ M^{(t)} = \begin{pmatrix} - & m_{1}^{(t)} & - \\ & \vdots & \\ - & m_{\vert V\vert }^{(t)} & - \end{pmatrix} \end{array}$$ então reescrevemos os passos anteriores como $$\begin{array}{r} M^{(t)} = \text{ AGGREGATE}^{(t)}\left( A,H^{(t - 1)} \right) \\ H^{(t)} = \text{ UPDATE}^{(t)}\left( H^{(t - 1)},M^{(t)} \right) \end{array}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Usos de GNNs](../usos-de-gnns/index.md)
- Próximo: [Graph Convolutional Network (GCN)](../graph-convolutional-network-gcn/index.md)
