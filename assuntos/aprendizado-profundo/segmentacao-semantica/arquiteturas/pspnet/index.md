---
layout: "default"
title: "PSPNet — Arquiteturas"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 16
---

[Aprendizado Profundo](../../../index.md) · [Segmentação Semântica](../../index.md) · [Arquiteturas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-22"></a>

# PSPNet

A PSPNet é uma arquitetura de rede neural convolucional projetada para segmentação semântica, que utiliza **pyramid pooling** para capturar informações de diferentes escalas da imagem. Ela também utiliza **atrous convolution** para aumentar o campo receptivo da rede sem aumentar o número de parâmetros.

Primeiro a imagem passa por um processamento em uma CNN, essa rede diminui a imagem original para $1/8$ do seu tamanho original e entra no bloco PSP **único**. Assim como no ASPP a imagem passa por múltiplas convoluções paralelas, no bloco PSP, a imagem passa por múltiplos **average pooling** com diferentes tamanhos de agrupamento:

- **Nível Red ($1 \times 1$)**: Realiza um Global Average Pooling sobre toda a extensão espacial. Gera um único vetor por canal que representa o contexto macro/global da cena inteira

- **Nível Orange ($2 \times 2$)**: Divide o mapa em 4 quadrantes (grade $2 \times 2$) e extrai a média de cada região (contexto regional amplo)

- **Nível Blue ($3 \times 3$)**: Divide o mapa em 9 sub-regiões (grade $3 \times 3$) para capturar um contexto regional médio

- **Nível Green ($6 \times 6$)**: Divide o mapa em 36 sub-regiões (grade $6 \times 6$) para capturar detalhes locais e regionais finos

![Arquitetura da PSPNet](../../../assets/A1/pspnet.png)

*Figura 23. Arquitetura da PSPNet*

então através do upsample, cada mapa de pooling é redimensionado para o tamanho original do feature map, e todos os mapas são concatenados, permitindo que a rede utilize informações de diferentes escalas para melhorar a segmentação.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [PARSENet](../parsenet/index.md)
- Próximo: [Deeplab V3 & V3+](../deeplab-v3-v3/index.md)
