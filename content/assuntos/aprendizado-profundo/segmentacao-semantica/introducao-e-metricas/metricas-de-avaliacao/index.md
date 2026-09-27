---
layout: "default"
title: "Métricas de Avaliação — Introdução e Métricas"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 3
---

[Aprendizado Profundo](../../../index.md) · [Segmentação Semântica](../../index.md) · [Introdução e Métricas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-3"></a>

# Métricas de Avaliação

Podemos utilizar algumas métricas para avaliar a performance de um modelo de segmentação semântica. As métricas mais comuns incluem:

<a id="iou"></a>

**Definição: Intersection over Union (IoU)**

$$\text{ IoU } = \frac{\text{ TP }}{\text{TP } + \text{ FP } + \text{ FN}}$$

<a id="precision"></a>

**Definição: Precision**

$$\text{ Precision } = \frac{\text{ TP }}{\text{TP } + \text{ FP}}$$

<a id="avg-precision"></a>

**Definição: Average Precision**

Dado que na minha imagem eu tenho mapeado $K$ classes, a métrica de Average Precision (AP) é definida como a média das precisões de cada classe: $$\text{ AP } = \left( \frac{1}{K} \right) \ast \sum_{k = 1}^{K}\text{ Precision}_{k}$$

<!-- wiki:original:fim -->

## Conteúdos relacionados

- [Métricas de Avaliação — Séries Temporais](../../../../series-temporais/metricas-de-avaliacao/index.md)

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Introdução e Métricas](../index.md)
- Próximo: [Evolução das Abordagens](../evolucao-das-abordagens/index.md)
