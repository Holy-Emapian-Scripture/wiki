---
layout: "default"
title: "Treinamento e Problemas de Gradiente na RNN — Recurrent Neural Networks (RNNs)"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 48
---

[Aprendizado Profundo](../../index.md) · [Recurrent Neural Networks (RNNs)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-56"></a>

# Treinamento e Problemas de Gradiente na RNN

Como comentamos, os mesmos parâmetros $\theta$ são utilizados em **todas as camadas** da rede neural, por conta disso, não podemos usar o **backpropagation** tradicional, e sim o **backpropagation through time (BPTT)**, que é uma extensão do algoritmo de retropropagação para redes recorrentes.

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Backpropagation Through Time (BPTT)](backpropagation-through-time-bptt/index.md)
2. [A matemática dos gradientes explosivos ou desvanecentes](a-matematica-dos-gradientes-explosivos-ou-desvanecentes/index.md)
3. [Métodos de mitigação](metodos-de-mitigacao/index.md)

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Tipos de mapeamento sequencial](../simple-rnn-vanilla-rnn/tipos-de-mapeamento-sequencial/index.md)
- Próximo: [Backpropagation Through Time (BPTT)](backpropagation-through-time-bptt/index.md)
