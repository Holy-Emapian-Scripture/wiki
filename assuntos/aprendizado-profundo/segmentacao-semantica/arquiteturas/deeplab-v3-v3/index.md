---
layout: "default"
title: "Deeplab V3 & V3+ — Arquiteturas"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 17
---

[Aprendizado Profundo](../../../index.md) · [Segmentação Semântica](../../index.md) · [Arquiteturas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-23"></a>

# Deeplab V3 & V3+

A DeepLabV3 foi teve algumas melhorias implementadas. O primeiro ponto foi a remoção do pós-processamento com CRF, que foi substituído por um **upsampling** simples, dessa forma a própria rede consegue aprender a mapear corretamente a segmentação. O segundo ponto foi a implementação do ASPP, que já havíamos comentado anteriormente. E o terceiro ponto foi a implementação, em paralelo com o ASPP, de um **image pooling** para pegar contexto global da rede

![Arquitetura da DeepLabV3](../../../assets/A1/deeplabv3.png)

*Figura 24. Arquitetura da DeepLabV3*

O **DeepLabv3+** foi projetado para resolver uma limitação fundamental do DeepLabv3: embora o DeepLabv3 capturasse um contexto multi-escala excelente através do ASPP, ele perdia detalhes finos e precisão nas bordas dos objetos devido à redução de resolução espacial (**striding** e **pooling**) no backbone. Para corrigir isso, o DeepLabv3+ combina o melhor de duas abordagens: a extração de contexto do **Spatial Pyramid Pooling (ASPP)** com a capacidade de recuperação de bordas da estrutura **Encoder-Decoder**.

![Arquitetura da DeepLabV3+](../../../assets/A1/deeplabv3plus.png)

*Figura 25. Arquitetura da DeepLabV3+*

Em vez do upsampling bilinear direto que o V3 fazia, o V3+ agora tem um módulo decoder dedicado, onde ele faz upsampling das características e vai utilizando das features do encoder para refinar a segmentação, especialmente nas bordas dos objetos. Isso permite que o modelo mantenha a precisão espacial enquanto ainda aproveita o contexto global capturado pelo ASPP.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [PSPNet](../pspnet/index.md)
- Próximo: [Percas](../../percas/index.md)
