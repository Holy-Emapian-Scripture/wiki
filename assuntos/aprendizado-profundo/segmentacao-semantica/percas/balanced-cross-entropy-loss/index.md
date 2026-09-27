---
layout: "default"
title: "Balanced Cross Entropy Loss — Percas"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 20
---

[Aprendizado Profundo](../../../index.md) · [Segmentação Semântica](../../index.md) · [Percas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-26"></a>

# Balanced Cross Entropy Loss

Para resolver o problema citado, podemos utilizar a **balanced cross entropy loss**, que atribui pesos diferentes para cada classe, penalizando mais os erros nas classes minoritárias. $$\text{ BCE } = - \frac{1}{N}\sum_{i = 1}^{N}\omega_{t_{i}}\log(p_{i})$$

o peso $\omega_{t_{i}}$ é pré-calculado de forma inversamente proporcional à frequência da classe $t_{i}$ no dataset, de forma que classes minoritárias tenham pesos maiores e classes majoritárias tenham pesos menores. Isso força a rede a prestar mais atenção às classes minoritárias durante o treinamento. Podemos ter uma formulação binária também $$\text{ BCE } = - \frac{1}{N}\left( \sum_{i \in \text{ positivos}}\omega_{\text{pos }}\log(p_{i}) + \sum_{i \in \text{ negativos}}\omega_{\text{neg }}\log(p_{i}) \right)$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Cross Entropy Loss](../cross-entropy-loss/index.md)
- Próximo: [Focal Loss](../focal-loss/index.md)
