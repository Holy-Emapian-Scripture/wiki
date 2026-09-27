---
layout: "default"
title: "Cross Entropy Loss — Percas"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 19
---

[Aprendizado Profundo](../../../index.md) · [Segmentação Semântica](../../index.md) · [Percas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-25"></a>

# Cross Entropy Loss

A primeira que vamos ver é a mais padrão para problemas de classificação, a **cross entropy loss**. Ela é definida como $$\text{ CE } = - \frac{1}{N}\sum_{i = 1}^{N}\log(p_{i})$$

se o modelo prevê alta probabilidade para a classe correta do pixel, o $\log(p_{i})$ será próximo de $0$, e a loss será pequena. Se o modelo prevê baixa probabilidade para a classe correta do pixel, o $\log(p_{i})$ será negativo e a loss será grande. O objetivo do treinamento é minimizar essa loss, ajustando os pesos da rede para que ela preveja corretamente as classes dos pixels.

No entanto, essa loss carrega um problema. Quando existe um desbalanceamento de classes dentro do meu dataset, pode acontecer de a rede aprender a prever apenas a classe majoritária, ignorando as classes minoritárias.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Percas](../index.md)
- Próximo: [Balanced Cross Entropy Loss](../balanced-cross-entropy-loss/index.md)
