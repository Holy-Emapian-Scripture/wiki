---
layout: "default"
title: "Pontos Práticos — Segmentação Semântica"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 24
---

[Aprendizado Profundo](../index.md) · [Segmentação Semântica](index.md)

<!-- wiki:original:inicio -->

<a id="secao-30"></a>

# Pontos Práticos


<a id="secao-31"></a>

## A necessidade de Patches (Tiles)

Em aplicações reais, as imagens originais frequentemente possuem resoluções massivas (ex: $(4000 \times 4000$) pixels ou mais). Tentar passar uma imagem desse tamanho inteira por uma rede neural de uma só vez estoura o limite de memória VRAM da GPU.

Por isso, na prática, a imagem é fatiada em blocos menores (**patches** ou **tiles**) para serem processados individualmente durante o treinamento e a inferência, montando-se um **mosaico** com os resultados finais de cada bloco.

![Exemplo de fatiamento de uma imagem em blocos menores](../assets/A1/patches.png)

*Figura 26. Exemplo de fatiamento de uma imagem em blocos menores*

<a id="secao-32"></a>

## O Problema do Contexto nas Bordas (Border Context Loss)

Dividir a imagem em blocos cria um desafio geométrico nas extremidades de cada bloco:

- **Perda de Contexto Espacial**: Os pixels situados nas bordas de um **patch** perdem a vizinhança e o contexto espacial da região vizinha que ficou no **patch** ao lado.

- **Artefatos no Mosaico**: Ao colar os **patches** de volta para reconstruir a imagem final, essa falta de contexto nas margens gera artefatos de corte visíveis, descontinuidades e erros de classificação ao longo das linhas de junção dos blocos.

Para mitigar a perda de contexto nas bordas dos blocos, podemos destacar a estratégia de *mosaico com sobreposição (**Overlapping Patches**)*:

1.  **Sobreposição de Blocos**: Os **patches** são recortados com uma porcentagem de sobreposição em relação aos vizinhos, em vez de serem colados estritamente lado a lado.

2.  **Considerar Apenas a Região Central (*Inner Part*)**: Descarta-se a borda externa do **patch** (onde o contexto foi prejudicado) e utiliza-se apenas a previsão da região central válida.

3.  **Média das Predições (*Averaging Results*)**: Nas áreas onde os blocos se sobrepõem, calcula-se a média das probabilidades previstas por cada bloco para definir a classe final do pixel.

<a id="cnn-patch-wise-classica-vs-fcn-modela"></a>
<a id="secao-33"></a>

## CNN Patch-wise Clássica vs. FCN Modela

- **[CNN Clássica](../../aprendizado-de-maquina/convolutional-neural-networks-cnn.md) Por Patch (Sliding Window)**: Classificava isoladamente o pixel central de um **patch** deslocado. Isso gerava alta redundância de cálculos e resultava em um efeito de **suavização excessiva nas bordas dos objetos (*oversmoothing*)**.

- **FCN Moderna**: Classifica todos os pixels do **patch** simultaneamente em uma única passada (**dense prediction**), aprendendo estruturas e geometrias específicas diretamente contidas dentro de cada bloco.

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Percas](percas.md)
- Próximo: [Object Detection](../object-detection/index.md)
