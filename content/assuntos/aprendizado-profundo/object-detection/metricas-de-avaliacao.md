---
layout: "default"
title: "Métricas de Avaliação — Object Detection"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 30
---

[Aprendizado Profundo](../index.md) · [Object Detection](index.md)

<!-- wiki:original:inicio -->
<a id="secao-36"></a>

# Métricas de Avaliação

Podemos utilizar métricas já vistas como [\[iou\]](../segmentacao-semantica/introducao-e-metricas.md#iou), [\[precision\]](../segmentacao-semantica/introducao-e-metricas.md#precision) e [\[avg-precision\]](../segmentacao-semantica/introducao-e-metricas.md#avg-precision), porém podemos também utilizar métricas como **Recall**

<a id="recall"></a>

**Definição: Recall**

$$
\text{ Recall } = \frac{\text{ TP }}{\text{TP } + \text{ FN}}
$$

A maioria das competições utiliza a **mean Average Precision (mAP)** como métrica principal, que é a média das precisões de cada classe, considerando diferentes limiares de confiança para as detecções. O mAP é derivado de valores *precision v.s recall*, fazendo uma variação do limiar de confiança para cada classe. O **limiar de confiança** é a probabilidade de que uma **caixa de âncora** contenha um objeto. Dado a [\[avg-precision\]](../segmentacao-semantica/introducao-e-metricas.md#avg-precision) de Average Precision, podemos definir melhor o mAP

**Definição: mAP**

Dado que na minha imagem eu tenho mapeado $K$ classes, a métrica de mean Average Precision (mAP) é definida como a média das precisões de cada classe: $$\text{ mAP } = \frac{1}{K}\sum_{k = 1}^{K}\text{ AP}_{k}$$

<!-- wiki:original:fim -->

## Conteúdos relacionados

- [Métricas de Avaliação — Séries Temporais](../../series-temporais/metricas-de-avaliacao.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Introdução](introducao.md)
- Próximo: [Redes de Estágio Único (Single-Shot): A Família YOLO](redes-de-estagio-unico-single-shot-a-familia-yolo.md)
