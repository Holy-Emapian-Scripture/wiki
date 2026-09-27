---
layout: "default"
title: "Modelo linear padrão — Modelagem Clássica aplicada ao Tempo"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 5
---

[Séries Temporais](../../index.md) · [Modelagem Clássica aplicada ao Tempo](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-9"></a>

# Modelo linear padrão

É o modelo mais simples que podemos utilizar para modelar a dependência entre uma variável dependente $y_{t}$ e variáveis explicativas $x_{it}$ ao longo do tempo. Já vimos esse modelo $n$ vezes nos semestres passados, então vou reescrever apenas os passos mais importantes $$y_{t} = \beta_{0} + \sum_{i = 1}^{P}\beta_{i}x_{it} + \varepsilon_{t}\text{\quad\quad}\varepsilon_{t} \sim N\left( 0,\sigma^{2} \right)$$ ou, em forma matricial $$y = X\beta + \varepsilon\text{\quad\quad}\varepsilon \sim N\left( 0,\sigma^{2}I \right) \Rightarrow y \sim N\left( X\beta,\sigma^{2}I \right)$$ onde $y \in {\mathbb{R}}^{T}$ é o vetor das observações da variável dependente, $X \in {\mathbb{R}}^{T \times P}$ é a matriz de observações das variáveis explicativas, $\beta \in {\mathbb{R}}^{P}$ é o vetor de pesos atribuindo a importância de cada parâmetro para explicar $y$ e $\varepsilon \in {\mathbb{R}}^{T}$ é um ruído gaussiano. Com essa estrutura, podemos obter o estimador de máxima verossimilhança de $\beta$ $$\hat{\beta} = \left( X^{T}X \right)^{- 1}X^{T}y$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Modelagem Clássica aplicada ao Tempo](../index.md)
- Próximo: [Balanço Viés-Variância](../balanco-vies-variancia/index.md)
