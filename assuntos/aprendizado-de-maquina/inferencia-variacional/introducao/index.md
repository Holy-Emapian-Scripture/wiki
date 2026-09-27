---
layout: "default"
title: "Introdução — Inferência Variacional"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 20
---

[Aprendizado de Máquina](../../index.md) · [Inferência Variacional](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-33"></a>

# Introdução

Na inferência variacional, nosso objetivo é aproximar uma distribuição $p$ através de outra distribuição $q$ que conseguimos manipular mais facilmente. Fazemos isso minimizando alguma medida de discrepância entre as duas distribuições, a forma mais comum de fazer isso é através da divergência de Kullback-Leibler, que é dada por: $$\text{ KL}\left( q\| p \right) = \int q(x)\ln\left\{ \frac{q(x)}{p(x)} \right\} dx = {\mathbb{E}}_{x \sim q}\left\lbrack \ln\left\{ \frac{q(x)}{p(x)} \right\} \right\rbrack$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Inferência Variacional](../index.md)
- Próximo: [Propriedades da divergência de Kullback-Leibler](../propriedades-da-divergencia-de-kullback-leibler/index.md)
