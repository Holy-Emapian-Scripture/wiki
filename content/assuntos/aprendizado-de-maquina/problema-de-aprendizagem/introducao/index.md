---
layout: "default"
title: "Introdução — Problema de Aprendizagem"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 2
---

[Aprendizado de Máquina](../../index.md) · [Problema de Aprendizagem](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-2"></a>

# Introdução

Em aprendizado supervisionado, o objetivo principal é criar uma aproximação $h:\mathcal{X} \rightarrow \mathcal{Y}$ para uma função $f:\mathcal{X} \rightarrow \mathcal{Y}$ a partir de amostras $D = \left\{ \left( x_{n},y_{n} \right) \right\}_{n = 1}^{N}$, onde cada exemplo de treinamento é uma amostra independente proveniente de ${\mathbb{P}}_{x,y}$ e $y_{n}$ é uma observação (possivelmente ruidosa) de $f\left( x_{n} \right)$. No caso de regressão, poderíamos usar vários métodos distintos para construir $h$. Alguns exemplos que já vimos são $k$-NN, regressão linear e redes neurais RBF. Além disso, podemos alterar drasticamente o comportamento desses modelos alterando hiper-parâmetros. Isso nos leva às duas perguntas estruturantes desse capítulo:

1.  Qual é a melhor classe de modelos (e.g., regressão linear, rede RBF) para cada problema?

2.  Como escolher escolher os melhores híper-parâmetros para cada classe de modelos?

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Problema de Aprendizagem](../index.md)
- Próximo: [Dilema viés-variância](../dilema-vies-variancia/index.md)
