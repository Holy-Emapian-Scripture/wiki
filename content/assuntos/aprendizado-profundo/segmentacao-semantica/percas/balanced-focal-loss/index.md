---
layout: "default"
title: "Balanced Focal Loss — Percas"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 22
---

[Aprendizado Profundo](../../../index.md) · [Segmentação Semântica](../../index.md) · [Percas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-28"></a>

# Balanced Focal Loss

Combina as duas soluções, ponderando cada pixel de acordo com sua classe e aplicando penalidade em pixels fáceis, de forma que a rede foque nos pixels mais difíceis e nas classes minoritárias. $$\text{ FL}_{\text{bal }} = - \frac{1}{N}\sum_{i = 1}^{N}\omega_{t_{i}}\left( 1 - p_{i} \right)^{\gamma}\log(p_{i})$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Focal Loss](../focal-loss/index.md)
- Próximo: [Loss Function for Regression](../loss-function-for-regression/index.md)
