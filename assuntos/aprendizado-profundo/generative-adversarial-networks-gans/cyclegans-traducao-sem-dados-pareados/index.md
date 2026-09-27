---
layout: "default"
title: "CycleGANs (Tradução sem dados pareados) — Generative Adversarial Networks (GANs)"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 69
---

[Aprendizado Profundo](../../index.md) · [Generative Adversarial Networks (GANs)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-79"></a>

# CycleGANs (Tradução sem dados pareados)

Agora o objetivo é traduzir imagens de um domínio para outro sem a necessidade de dados pareados, ou seja, se eu recebo uma imagem de, por exemplo, um cavalo, eu quero que a rede substitua ele por uma zebra, mantendo posição, aparência, iluminação etc. No entanto, nós **não temos** acesso à imagens pareadas, como uma foto idêntica com cavalos e zebras na mesma pose, etc. Então como fazer a GAN aprender?

É aí que entram as CyclGANs([Zhu et al. 2018](../../referencias/index.md#ref-cyclegans)) para aprender essa dependência e mapeamento sem utilização de pares

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Estrutura de pareamento duplo](estrutura-de-pareamento-duplo/index.md)
2. [Função objetivo completa](funcao-objetivo-completa/index.md)
3. [Arquitetura de CycleGANs](arquitetura-de-cyclegans/index.md)

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Aplicações das cGANs](../gans-condicionais-cgans/aplicacoes-das-cgans/index.md)
- Próximo: [Estrutura de pareamento duplo](estrutura-de-pareamento-duplo/index.md)
