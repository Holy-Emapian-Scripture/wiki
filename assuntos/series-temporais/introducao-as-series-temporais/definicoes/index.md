---
layout: "default"
title: "Definições — Introdução às Séries Temporais"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 2
---

[Séries Temporais](../../index.md) · [Introdução às Séries Temporais](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-2"></a>

# Definições

**Definição: Série Temporal de Tempo Discreto**

Conjunto de observações $y_{t}$ registradas em intervalos de tempo específico $t$ medidas de forma **discreta**. $$\left\{ y_{t} \right\}\vert _{t = 1}^{T}$$

**Exemplo**

A temperatura de uma região registrada **diariamente**

**Definição: Modelo de Séries Temporais**

Um modelo de séries temporais para $\left\{ y_{t} \right\}$ é a **especificação da distribuição conjunta** de uma **sequência de variáveis aleatórias** $\left\{ Y_{t} \right\}$ das quais $\left\{ y_{t} \right\}$ é esperada ser uma realização $${\mathbb{P}}(X_{1} \leq x_{1},\ldots,X_{n} \leq x_{n}), - \infty < x_{1},\ldots,x_{n} < \infty,n = 1,2,\ldots$$

Modelar essa distribuição é muito complexo, pois temos acesso apenas à uma realização da série temporal $\left\{ Y_{t} \right\}$. Para contornar essa limitação, focamos nos momentos de **primeira** e **segunda** ordem $${\mathbb{E}}\left\lbrack Y_{t} \right\rbrack\text{ e }{\mathbb{E}}\left\lbrack Y_{t}Y_{t + h} \right\rbrack$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Introdução às Séries Temporais](../index.md)
- Próximo: [Por que modelar séries temporais é importante?](../por-que-modelar-series-temporais-e-importante/index.md)
