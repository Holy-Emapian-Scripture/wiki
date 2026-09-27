---
layout: "default"
title: "Redes de Estágio Único (Single-Shot): A Família YOLO — Object Detection"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 31
---

[Aprendizado Profundo](../../index.md) · [Object Detection](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-37"></a>

# Redes de Estágio Único (Single-Shot): A Família YOLO

Baseada em redes neurais convolucionais que redefiniu o problema de detecção como uma única tarefa de regressão e classificação em uma só passada (**single-shot**).

Ao contrário das abordagens tradicionais baseadas em **sliding window** (janela deslizante), que executavam classificadores repetidamente sobre centenas de retalhos da imagem gerando um custo computacional altíssimo, o YOLO avalia a imagem inteira de uma só vez

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Fundamentos do YOLO](fundamentos-do-yolo/index.md)
2. [Parametrização do vetor de saída](parametrizacao-do-vetor-de-saida/index.md)
3. [Caixas de Ancoragem (Anchor Boxes)](caixas-de-ancoragem-anchor-boxes/index.md)
4. [Supressão Não-Máxima (Non-Maximum Suppression - NMS)](supressao-nao-maxima-non-maximum-suppression-nms/index.md)
5. [Evolução Arquitetural](evolucao-arquitetural/index.md)
6. [Loss Function](loss-function/index.md)

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Métricas de Avaliação](../metricas-de-avaliacao/index.md)
- Próximo: [Fundamentos do YOLO](fundamentos-do-yolo/index.md)
