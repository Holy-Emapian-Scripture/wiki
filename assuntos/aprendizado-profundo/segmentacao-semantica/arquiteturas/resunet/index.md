---
layout: "default"
title: "ResUNet — Arquiteturas"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 13
---

[Aprendizado Profundo](../../../index.md) · [Segmentação Semântica](../../index.md) · [Arquiteturas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-19"></a>

# ResUNet

Na ResUNet, a arquitetura é uma combinação da U-Net com blocos residuais, permitindo que a rede aprenda a diferença entre as features de downsampling e upsampling, melhorando ainda mais a segmentação.

![Arquitetura da ResUNet](../../../assets/A1/resunet-architecture.png)

*Figura 19. Arquitetura da ResUNet*

![(a) Bloco padrão da UNet. (b) Bloco residual da ResUNet](../../../assets/A1/resunet.png)

*Figura 20. (a) Bloco padrão da UNet. (b) Bloco residual da ResUNet*

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [U-Net](../u-net/index.md)
- Próximo: [DeepLab V1 & V2](../deeplab-v1-v2/index.md)
