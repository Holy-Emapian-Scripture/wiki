---
layout: "default"
title: "Imagens como dados — Convolutional Neural Networks (CNN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 21
---

[Aprendizado de Máquina](../../index.md) · [Convolutional Neural Networks (CNN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-24"></a>

# Imagens como dados

Podemos interpretar imagens como dados estruturados em uma grade bidimensional, onde cada pixel representa uma unidade de informação. Cada pixel possui valores que representam a intensidade da cor em diferentes canais (como vermelho, verde e azul para imagens RGB). Essa estrutura de grade permite que as CNNs explorem a relação espacial entre os pixels, capturando padrões locais e hierárquicos. $$I \in {\mathbb{R}}^{H \times W \times C}$$ onde $H$, $W$ e $C$ representam a altura, largura e número de canais da imagem, respectivamente. No caso, se a imagem é colorida, $C = 3$ e se ela é preto e branco, $C = 1$ (O que podemos entender como uma matriz com dimensões $H \times W$)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Introdução](../introducao/index.md)
- Próximo: [Filtros](../filtros/index.md)
