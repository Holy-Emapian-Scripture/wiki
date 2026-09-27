---
layout: "default"
title: "Graph Convolutional Network (GCN) — Graph Neural Networks"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 18
---

[Aprendizado de Máquina](../../index.md) · [Graph Neural Networks](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-21"></a>

# Graph Convolutional Network (GCN)

Popularizou as GNNs por sua simplicidade. É um modelo baseado em message-passing, onde a função de agregação é uma média ponderada dos vizinhos de um nó e a função de atualização é uma rede neural simples. A GCN é definida como: $$\begin{array}{rlr} m_{v}^{(t)} & = \sum_{u \in \mathcal{N}(v)}\frac{h_{u}^{(t - 1)}}{\sqrt{{\overline{d}}_{u}{\overline{d}}_{v}}}\text{\quad\quad} & \forall v \in V \\ h_{v}^{(t)} & = \sigma(\left( \frac{1}{{\overline{d}}_{v}}h_{v}^{(t - 1)} + m_{v}^{(t)} \right)\Theta_{t})\text{\quad\quad} & \forall v \in V \end{array}$$

onde $\Theta_{t}$ é uma matriz de pesos aprendida durante o treinamento e ${\overline{d}}_{v}$ é o grau do nó $v$ com self-loops. A função de ativação $\sigma$ é geralmente uma função não-linear como ReLU ou sigmoid. Podemos reescrever a GCN de forma matricial como: $$H^{(t)} = \sigma(D^{- \frac{1}{2}}AD^{- \frac{1}{2}}H^{(t - 1)}\Theta_{t})$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Passagem de Mensagem](../passagem-de-mensagem/index.md)
- Próximo: [Convolutional Neural Networks (CNN)](../../convolutional-neural-networks-cnn/index.md)
