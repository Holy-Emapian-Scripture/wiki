---
layout: "default"
title: "Arquitetura — Simple RNN (Vanilla RNN)"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 45
---

[Aprendizado Profundo](../../../index.md) · [Recurrent Neural Networks (RNNs)](../../index.md) · [Simple RNN (Vanilla RNN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-53"></a>

# Arquitetura

Podemos estruturar uma arquitetura visual fixa para cada um dos passos temporais que a rede recorrente faz

![Arquitetura de uma RNN](../../../assets/A1/rnn-architecture.png)

*Figura 41. Arquitetura de uma RNN*

Podemos utilizar uma fórmula **recursiva** para representar a RNN, onde o estado oculto $h_{t}$ é atualizado a cada passo temporal com base no estado oculto anterior $h_{t - 1}$ e na entrada atual $x_{t}$. $$\underset{\text{ Estado Oculto}}{\underbrace{h_{t}}} = f_{\theta}\left( \underset{\text{ Estado Anterior}}{\underbrace{h_{t - 1}}},\underset{\text{ Entrada Atual}}{\underbrace{x_{t}}} \right)$$

e vale ressaltar que o **mesmo conjunto de parâmetros $\theta$** é utilizado em **todos os passos temporais**, diferente de uma rede neural padrão onde **cada camada possui um conjunto de parâmetros diferente**. Isso permite que a RNN generalize melhor para sequências de diferentes comprimentos e capture padrões temporais de forma mais eficiente.

Tomemos a simples RNN $h_{t} = \tanh(W_{hh}h_{t - 1} + W_{xh}x_{t})$ e vamos ver como a recursividade se comporta com $T = 3$ $$\begin{aligned} h_{3} & = \tanh(W_{hh}h_{2} + W_{xh}x_{3}) \\ h_{3} & = \tanh(W_{hh}\left( \tanh(W_{hh}h_{1} + W_{xh}x_{2}) \right) + W_{xh}x_{2}) \\ h_{3} & = \tanh(W_{hh}\left( \tanh(W_{hh}\left( \tanh(W_{hh}h_{0} + W_{xh}x_{1}) \right) + W_{xh}x_{2}) \right) + W_{xh}x_{3}) \end{aligned}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Simple RNN (Vanilla RNN)](../index.md)
- Próximo: [RNN Unroling](../rnn-unroling/index.md)
