---
layout: "default"
title: "Ridge Regression — Regularização Lasso e Ridge"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 9
---

[Séries Temporais](../../../index.md) · [Modelagem Clássica aplicada ao Tempo](../../index.md) · [Regularização Lasso e Ridge](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-13"></a>

# Ridge Regression

Em vez dos valores absolutos, usamos a soma dos quadrados $$\sum_{t = 1}^{T}\left( y_{t} - {\hat{y}}_{t} \right)^{2} + \lambda\sum_{i = 1}^{P}\beta_{i}^{2}$$ essa abordagem não costuma zerar os coeficientes, mas os puxa para muito próximo de $0$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Lasso (Least Absolute Shrinkage and Selection Operator)](../lasso-least-absolute-shrinkage-and-selection-operator/index.md)
- Próximo: [Generalized Additive Models (GAM)](../../generalized-additive-models-gam/index.md)
