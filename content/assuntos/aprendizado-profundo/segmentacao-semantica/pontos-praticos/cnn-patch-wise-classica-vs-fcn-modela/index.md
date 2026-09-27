---
layout: "default"
title: "CNN Patch-wise Clássica vs. FCN Modela — Pontos Práticos"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 27
---

[Aprendizado Profundo](../../../index.md) · [Segmentação Semântica](../../index.md) · [Pontos Práticos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-33"></a>

# CNN Patch-wise Clássica vs. FCN Modela

- **CNN Clássica Por Patch (Sliding Window)**: Classificava isoladamente o pixel central de um **patch** deslocado. Isso gerava alta redundância de cálculos e resultava em um efeito de **suavização excessiva nas bordas dos objetos (*oversmoothing*)**.

- **FCN Moderna**: Classifica todos os pixels do **patch** simultaneamente em uma única passada (**dense prediction**), aprendendo estruturas e geometrias específicas diretamente contidas dentro de cada bloco.

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [O Problema do Contexto nas Bordas (Border Context Loss)](../o-problema-do-contexto-nas-bordas-border-context-loss/index.md)
- Próximo: [Object Detection](../../../object-detection/index.md)
