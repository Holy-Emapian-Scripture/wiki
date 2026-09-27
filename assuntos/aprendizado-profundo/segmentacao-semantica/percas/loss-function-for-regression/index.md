---
layout: "default"
title: "Loss Function for Regression — Percas"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 23
---

[Aprendizado Profundo](../../../index.md) · [Segmentação Semântica](../../index.md) · [Percas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-29"></a>

# Loss Function for Regression

A saída por pixel pode não necessariamente ser um label de classe, mas um valor numérico. Por exemplo, se a rede estiver tentando estimar a profundidade aplicada àquela foto, então utilizamos as losses $L_{1}$ e $L_{2}$ $$\begin{aligned} L_{1} & = \frac{1}{N}\sum_{i = 1}^{N}\vert y_{i} - t_{i}\vert  \\ L_{2} & = \frac{1}{N}\sum_{i = 1}^{N}\left( y_{i} - t_{i} \right)^{2} \end{aligned}$$

onde $y_{i}$ é o valor predito pelo modelo e $t_{i}$ é o valor verdadeiro.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Balanced Focal Loss](../balanced-focal-loss/index.md)
- Próximo: [Pontos Práticos](../../pontos-praticos/index.md)
