---
layout: "default"
title: "A necessidade de Patches (Tiles) — Pontos Práticos"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 25
---

[Aprendizado Profundo](../../../index.md) · [Segmentação Semântica](../../index.md) · [Pontos Práticos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-31"></a>

# A necessidade de Patches (Tiles)

Em aplicações reais, as imagens originais frequentemente possuem resoluções massivas (ex: $(4000 \times 4000$) pixels ou mais). Tentar passar uma imagem desse tamanho inteira por uma rede neural de uma só vez estoura o limite de memória VRAM da GPU.

Por isso, na prática, a imagem é fatiada em blocos menores (**patches** ou **tiles**) para serem processados individualmente durante o treinamento e a inferência, montando-se um **mosaico** com os resultados finais de cada bloco.

![Exemplo de fatiamento de uma imagem em blocos menores](../../../assets/A1/patches.png)

*Figura 26. Exemplo de fatiamento de uma imagem em blocos menores*

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Pontos Práticos](../index.md)
- Próximo: [O Problema do Contexto nas Bordas (Border Context Loss)](../o-problema-do-contexto-nas-bordas-border-context-loss/index.md)
