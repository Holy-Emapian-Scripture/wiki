---
layout: "default"
title: "Função objetivo — Introdução às GANs"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 62
---

[Aprendizado Profundo](../../../index.md) · [Generative Adversarial Networks (GANs)](../../index.md) · [Introdução às GANs](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-70"></a>

# Função objetivo

Seja $\omega$ e $\varphi$ o conjunto de parâmetros da rede geradora e discriminadora respectivamente, a função objetivo da GAN é dada por um jogo de soma zero (minmax game) que escrevemos da seguinte forma $$\min\limits_{\omega}\max\limits_{\varphi}\left\lbrack {\mathbb{E}}_{x \sim p_{\text{data}}}\left\lbrack \log D_{\varphi}(x) \right\rbrack + {\mathbb{E}}_{z \sim p_{\text{synthetic}}}\left\lbrack \log(1 - D_{\varphi}\left( G_{\omega}(z) \right)) \right\rbrack \right\rbrack$$

onde $D_{\varphi}$ é a função de decisão do discriminador e $G_{\omega}$ é a função de geração do gerador. Essa função é basicamente uma **entropia cruzada** entre a classificação do discriminador sobre os dados reais e a sua classificação sobre os dados **gerados pelo gerador**, com a diferença que na entropia cruzada clássica, o sinal negativo é aplicado pra que a otimização vire uma **minimzação** (por isso que na fórmula do GAN a equação está **maximizando** o discriminador e **minimizando** o gerador). Por consequência, nós minimizamos com relação ao gerador para que ele consiga **atrapalhar** a percepção do discriminador.

Na prática computacional, as esperanças são aproximadas pelas médias amostrais dentro de cada mini batch.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Two-player Game](../two-player-game/index.md)
- Próximo: [Dinâmica de Treinamento e Ajuste do Gradiente](../dinamica-de-treinamento-e-ajuste-do-gradiente/index.md)
