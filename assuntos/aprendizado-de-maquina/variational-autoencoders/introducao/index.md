---
layout: "default"
title: "Introdução — Variational Autoencoders"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 17
---

[Aprendizado de Máquina](../../index.md) · [Variational Autoencoders](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-17"></a>

# Introdução

Autoencoders são modelos de aprendizado não supervisionado projetados para aprender representações compactas dos dados. Seu objetivo é comprimir uma entrada em uma representação de menor dimensão e, em seguida, reconstruir a entrada original a partir dessa representação.

A arquitetura de um autoencoder é composta por duas partes principais:

- **Encoder:** transforma a entrada original em uma representação latente, também chamada de **código** ou **embedding**.

- **Decoder:** utiliza essa representação latente para reconstruir uma aproximação da entrada original.

De forma simplificada, dado um dado de entrada (x), o encoder produz uma representação (z),

$$z = f(x),$$

e o decoder gera uma reconstrução ($\hat{x}$),

$$\hat{x} = g(z).$$

Durante o treinamento, os parâmetros do modelo são ajustados para minimizar a diferença entre (x) e ($\hat{x}$), fazendo com que a representação latente retenha as características mais relevantes dos dados.

Ao aprender a reconstruir as entradas a partir de uma representação comprimida, os autoencoders podem descobrir estruturas e padrões presentes nos dados, sendo amplamente utilizados para redução de dimensionalidade, compressão, remoção de ruído, detecção de anomalias e aprendizado de representações.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Variational Autoencoders](../index.md)
- Próximo: [Autoencoders Determinísticos](../autoencoders-deterministicos/index.md)
