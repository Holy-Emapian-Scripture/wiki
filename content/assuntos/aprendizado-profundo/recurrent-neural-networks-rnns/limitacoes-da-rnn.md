---
layout: "default"
title: "Limitações da RNN — Recurrent Neural Networks (RNNs)"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 52
---

[Aprendizado Profundo](../index.md) · [Recurrent Neural Networks (RNNs)](index.md)

<!-- wiki:original:inicio -->
<a id="secao-60"></a>

# Limitações da RNN

Em RNN simples, ela consegue capturar contexto relevante de curto prazo, mas tem dificuldade em capturar dependências de longo prazo. Isso ocorre porque, à medida que a sequência se torna mais longa, o gradiente pode se tornar muito pequeno (vanishing gradient) ou muito grande (exploding gradient), dificultando o aprendizado de padrões de longo prazo. Por exemplo, na frace *“I grew up in france, \[…\] I speak fluent french”* as palavras *france* e *french* estão separadas por várias palavras, e a RNN simples pode ter dificuldade em capturar essa relação de longo prazo.

Não só isso, como a RNN também pode ter dificuldade, mesmo em dependências de curto prazo, de selecionar a informação que é de fato relevante para aquele contexto

![Exemplo de limitação da RNN simples](../assets/A1/rnn-limitation.png)

*Figura 49. Exemplo de limitação da RNN simples*

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Métodos de mitigação](treinamento-e-problemas-de-gradiente-na-rnn.md#metodos-de-mitigacao)
- Próximo: [Long-short Term Memory (LSTM)](long-short-term-memory-lstm.md)
