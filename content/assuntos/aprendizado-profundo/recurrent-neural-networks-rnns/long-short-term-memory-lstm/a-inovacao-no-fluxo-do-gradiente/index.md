---
layout: "default"
title: "A inovação no Fluxo do Gradiente — Long-short Term Memory (LSTM)"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 54
---

[Aprendizado Profundo](../../../index.md) · [Recurrent Neural Networks (RNNs)](../../index.md) · [Long-short Term Memory (LSTM)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-62"></a>

# A inovação no Fluxo do Gradiente

A grande inovação matemática da LSTM que resolve o problema do Gradiente Desaparecido (Vanishing Gradient) está na forma como o erro retropropaga pelo Cell State ($c_{t}$)

Na Simple RNN, a derivada do estado em relação ao estado anterior exigia a multiplicação matricial pela transposta dos pesos $$\frac{\partial h_{t}}{\partial h_{t - 1}} \propto W_{hh}^{T}$$

Ao retropropagar por $T - k$ passos, acumulava-se a multiplicação de matrizes $\left( W_{hh}^{T} \right)^{T - k}$, fazendo o gradiente desaparecer quando o maior valor singular era menor que $1$

Na LSTM, a atualização do estado celular é aditiva: $c_{t} = f_{t} \odot c_{t - 1} + i_{t} \odot {\widetilde{c}}_{t}$. Ao calcular a derivada parcial do estado celular atual $c_{t}$ diretamente em relação ao estado celular anterior $c_{t - 1}$ $$\frac{\partial c_{t}}{\partial c_{t - 1}} = f_{t}$$

Ao retropropagar o erro ao longo de uma sequência de $T$ até um instante distante $k$ exclusivamente pela linha do Cell State, o gradiente resultante é dado por $$\frac{\partial c_{T}}{\partial c_{k}} = \prod_{j = k + 1}^{T}f_{j}$$

Sem Multiplicação Matricial Sucessiva: A retropropagação de $c_{t - 1}$ para $c_{t}$ envolve apenas multiplicação elemento a elemento pelo vetor do forget gate $f_{t}$, eliminando a multiplicação matricial por $W^{T}$. Como cada passo temporal possui um vetor $f_{j}$ diferente (calculado dinamicamente com base em $h_{j - 1}$ e $x_{j}$), a rede pode aprender a definir $f_{j} \approx 1.0$ para manter memórias importantes intactas. Desta forma, a informação e o gradiente conseguem fluir sem desaparecer ao longo da “esteira” do Cell State por centenas de passos temporais.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Long-short Term Memory (LSTM)](../index.md)
- Próximo: [Gated Recurrent Unit (GRU)](../../gated-recurrent-unit-gru/index.md)
