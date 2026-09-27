---
layout: "default"
title: "Geração de propostas com a RPN (Region Proposal Network) — Redes de Dois Estágios e Segmentação de Instâncias: Mask R-CNN"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 39
---

[Aprendizado Profundo](../../../index.md) · [Object Detection](../../index.md) · [Redes de Dois Estágios e Segmentação de Instâncias: Mask R-CNN](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-47"></a>

# Geração de propostas com a RPN (Region Proposal Network)

Antes de mais nada, a **imagem é redimensionada** para caber na rede backbone. Essa rede backbone recebe a imagem e gera um **feature map** que representa as características da imagem. Esse **feature map** é então passado para a **Region Proposal Network (RPN)**, que é responsável por gerar propostas de regiões onde objetos podem estar localizados. A RPN utiliza um conjunto de $k$ **anchor boxes** de diferentes tamanhos e proporções para cobrir uma variedade de objetos possíveis na imagem.

A RPN fica responsável por aprender principalmente duas coisas: A probabilidade de a anchor box conter ou não um objeto e estimar o tamanho/formato da caixa delimitadora do objeto. Primeiro, uma convolução $3 \times 3$ com $512$ filtros é aplicada ao **feature map** da backbone, gerando um **feature map** intermediário.

Em seguida, duas convoluções $1 \times 1$ são aplicadas: uma para prever a probabilidade de cada **anchor box** conter um objeto (**objectness score**), contento um total de $36$ filtros e outra para prever os ajustes necessários para refinar as coordenadas da caixa delimitadora (**bounding box regression**) com $18$ filtros.

![Arquitetura da Mask R-CNN](../../../assets/A1/mask-rcnn-backbone.png)

*Figura 32. Arquitetura da Mask R-CNN*

Logo após isso, para escolher as melhores propostas de regiões, a RPN aplica a técnica de **Non-Maximum Suppression (NMS)** para eliminar propostas redundantes e manter apenas as mais promissoras. As propostas selecionadas são então passadas para a próxima etapa da Mask R-CNN, onde cada proposta é processada individualmente para prever a classe do objeto, refinar a caixa delimitadora e gerar a máscara binária correspondente.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Redes de Dois Estágios e Segmentação de Instâncias: Mask R-CNN](../index.md)
- Próximo: [Alinhamento de Características com RoIAlign](../alinhamento-de-caracteristicas-com-roialign/index.md)
