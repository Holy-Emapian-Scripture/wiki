---
layout: "default"
title: "Two-player Game — Introdução às GANs"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 61
---

[Aprendizado Profundo](../../../index.md) · [Generative Adversarial Networks (GANs)](../../index.md) · [Introdução às GANs](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-69"></a>

# Two-player Game

A primeira rede, chamada de **gerador** (Generator), é responsável por gerar novas amostras a partir de uma distribuição simples, enquanto a segunda rede, chamada de **discriminador** (Discriminator), é responsável por distinguir entre amostras reais e amostras geradas pelo gerador.

![Arquitetura de uma GAN](../../../assets/A1/gan-architecture.png)

*Figura 55. Arquitetura de uma GAN*

O objetivo do gerador é gerar imagens cada vez melhores, de forma que ele consiga **enganar** o discriminador, enquanto o objetivo do discriminador é se tornar cada vez melhor em distinguir entre imagens reais e imagens geradas. Esse processo de competição leva a um aprimoramento contínuo de ambas as redes, resultando em um gerador capaz de produzir amostras altamente realistas. Mas vale ressaltar que o objetivo principal é a melhora da rede **geradora**, mas nós aprimoramos a discriminadora também com a intenção de que ela se torne mais forte e assim force a geradora a melhorar ainda mais.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Introdução às GANs](../index.md)
- Próximo: [Função objetivo](../funcao-objetivo/index.md)
