---
layout: "default"
title: "Redes de Dois Estágios e Segmentação de Instâncias: Mask R-CNN — Object Detection"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 38
---

[Aprendizado Profundo](../../index.md) · [Object Detection](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-46"></a>

# Redes de Dois Estágios e Segmentação de Instâncias: Mask R-CNN

As redes Mask R-CNN são uma extensão das redes Faster R-CNN, projetadas para realizar não apenas a detecção de objetos, mas também a segmentação de instâncias. A Mask R-CNN adiciona um ramo adicional à arquitetura Faster R-CNN para prever máscaras binárias para cada objeto detectado, permitindo que a rede identifique não apenas a localização e a classe do objeto, mas também sua forma precisa.

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Geração de propostas com a RPN (Region Proposal Network)](geracao-de-propostas-com-a-rpn-region-proposal-network/index.md)
2. [Alinhamento de Características com RoIAlign](alinhamento-de-caracteristicas-com-roialign/index.md)
3. [Predições em Paralelo (R-CNN + FCN)](predicoes-em-paralelo-r-cnn-fcn/index.md)

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Loss Function](../redes-de-estagio-unico-single-shot-a-familia-yolo/loss-function/index.md)
- Próximo: [Geração de propostas com a RPN (Region Proposal Network)](geracao-de-propostas-com-a-rpn-region-proposal-network/index.md)
