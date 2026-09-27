---
layout: "default"
title: "Introdução — Generative Adversarial Networks"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 21
---

[Aprendizado de Máquina](../../index.md) · [Generative Adversarial Networks](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-26"></a>

# Introdução

Esse capítulo trata de um método de aprendizado não supervisionado usado para treinar modelos **generativos**. Esses modelos são capazes de gerar novos exemplos que se assemelham aos dados de treinamento. A ideia central é simples. Queremos que as novas amostras geradas por nosso modelo generativo sejam tão boas que seja difícil afirmar qual é a amostra real e qual é a amostra gerada. Para isso, utilizamos uma abordagem de aprendizado adversarial, onde dois modelos competem entre si: um gerador e um discriminador.

Enquanto o modelo generativo cria imagens, o discriminador tenta distinguir entre imagens reais e imagens geradas. O objetivo do gerador é enganar o discriminador, enquanto o objetivo do discriminador é identificar corretamente as imagens reais e falsas. Esse processo de competição leva a uma melhoria contínua de ambos os modelos, resultando em um gerador capaz de produzir amostras realistas.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Generative Adversarial Networks](../index.md)
- Próximo: [Treinamento Adversarial](../treinamento-adversarial/index.md)
