---
layout: "default"
title: "A matemática dos gradientes explosivos ou desvanecentes — Treinamento e Problemas de Gradiente na RNN"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 50
---

[Aprendizado Profundo](../../../index.md) · [Recurrent Neural Networks (RNNs)](../../index.md) · [Treinamento e Problemas de Gradiente na RNN](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-58"></a>

# A matemática dos gradientes explosivos ou desvanecentes

No entanto, essa estrutura pode gerar um grande problema quando a diferença $t - k$ é muito grande. Tomando como base a equação base da RNN $h_{t} = \tanh(W_{hh}h_{t - 1} + W_{xh}x_{t})$, podemos calcular a derivada do estado oculto $h_{j}$ em relação ao estado oculto anterior $h_{j - 1}$ $$\frac{\partial h_{j}}{\partial h_{j - 1}} = \text{ diag}\left( 1 - \tanh^{2}( \cdot ) \right)W_{hh}^{T}$$

então a propagação do gradiente de $h_{0}$ até $h_{t}$ envolve a multiplicação repetida de $t - k$ termos $W_{hh}^{T}$ e da derivada de $\tanh$

Podemos chegar nesse mesmo resultado de uma forma mais matemática fazendo uma análise por SVD. Considere a decomposição SVD da matriz de transição $W_{hh} = U\Sigma V^{T}$ e seja a parcial derivada do estado oculto $h_{j}$ em relação ao estado oculto anterior $h_{j - 1}$ escrita como $$\frac{\partial h_{j}}{\partial h_{j - 1}} = D_{j}W_{hh}^{T}$$

então sabemos que a derivada de $h_{t}$ com relação a um estado oculto anterior $h_{k}$ é dada por $$\frac{\partial h_{t}}{\partial h_{k}} = \prod_{j = k + 1}^{t}D_{j}W_{hh}^{T}$$

vamos então medir a norma $L_{2}$ desse gradiente para entender como ele se comporta $$\left. \frac{\|\left( \partial h_{t} \right)}{\partial h_{k}} \right\|_{2} = \left\| \prod_{j = k + 1}^{t}D_{j}W_{hh}^{T} \right\|_{2}$$

Pela propriedade submultiplicativa das normas matriciais $\| AB\|_{2} \leq \| A\|_{2}\| B\|_{2}$, temos que: $$\left. \frac{\|\left( \partial h_{t} \right)}{\partial h_{k}} \right\|_{2} \leq \prod_{j = k + 1}^{t}\| D_{j}\|_{2}\| W_{hh}^{T}\|_{2}$$

No entanto, temos que $\| D_{j}\|_{2} = \sigma_{\text{max }}\left( D_{j} \right) = \max\limits_{i}\vert 1 - \tanh^{2}\left( z_{ji} \right)\vert  \leq 1$ e $\| W_{hh}^{T}\|_{2} = \sigma_{\text{max }}\left( W_{hh}^{T} \right)$, então $$\begin{aligned} & \left. \frac{\|\left( \partial h_{t} \right)}{\partial h_{k}} \right\|_{2} \leq \prod_{j = k + 1}^{t}1 \cdot \sigma_{\text{max }}\left( W_{hh}^{T} \right) \\ \Rightarrow & \left. \frac{\|\left( \partial h_{t} \right)}{\partial h_{k}} \right\|_{2} \leq \left( \sigma_{\text{max }}\left( W_{hh}^{T} \right) \right)^{t - k} \end{aligned}$$

A conclusão que temos dessa análise é que, se o maior valor singular é menor que 1, então o gradiente vai decair exponencialmente com o aumento da diferença $t - k$, levando ao problema de **vanishing gradient**. Por outro lado, se o maior valor singular é maior que 1, então o gradiente vai crescer exponencialmente com o aumento da diferença $t - k$, levando ao problema de **exploding gradient**.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Backpropagation Through Time (BPTT)](../backpropagation-through-time-bptt/index.md)
- Próximo: [Métodos de mitigação](../metodos-de-mitigacao/index.md)
