---
layout: "default"
title: "Regularização Lasso e Ridge — Modelagem Clássica aplicada ao Tempo"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 7
---

[Séries Temporais](../index.md) · [Modelagem Clássica aplicada ao Tempo](index.md)

<!-- wiki:original:inicio -->

<a id="secao-11"></a>

# Regularização Lasso e Ridge


<a id="lasso-least-absolute-shrinkage-and-selection-operator"></a>
<a id="secao-12"></a>

## Lasso (Least Absolute Shrinkage and Selection Operator)

Em vez de minimizarmos simplesmente o erro quadrático, adicionamos um peso nos valores absolutos dos coeficientes, de forma que se eles crescem muito em módulo, a nossa função de perca não diminui como esperado $$\sum_{t = 1}^{T}\left( y_{t} - {\hat{y}}_{t} \right)^{2} + \lambda\sum_{i = 1}^{P}\vert \beta_{i}\vert$$ essa abordagem tente a zerar alguns coeficientes, indicando quais coeficientes realmente influenciam ou não

<a id="ridge-regression"></a>
<a id="secao-13"></a>

## Ridge Regression

Em vez dos valores absolutos, usamos a soma dos quadrados $$\sum_{t = 1}^{T}\left( y_{t} - {\hat{y}}_{t} \right)^{2} + \lambda\sum_{i = 1}^{P}\beta_{i}^{2}$$ essa abordagem não costuma zerar os coeficientes, mas os puxa para muito próximo de $0$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Balanço Viés-Variância](balanco-vies-variancia.md)
- Próximo: [Generalized Additive Models (GAM)](generalized-additive-models-gam.md)
