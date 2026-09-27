---
layout: "default"
title: "Lasso (Least Absolute Shrinkage and Selection Operator) — Regularização Lasso e Ridge"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 8
---

[Séries Temporais](../../../index.md) · [Modelagem Clássica aplicada ao Tempo](../../index.md) · [Regularização Lasso e Ridge](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-12"></a>

# Lasso (Least Absolute Shrinkage and Selection Operator)

Em vez de minimizarmos simplesmente o erro quadrático, adicionamos um peso nos valores absolutos dos coeficientes, de forma que se eles crescem muito em módulo, a nossa função de perca não diminui como esperado $$\sum_{t = 1}^{T}\left( y_{t} - {\hat{y}}_{t} \right)^{2} + \lambda\sum_{i = 1}^{P}\vert \beta_{i}\vert$$ essa abordagem tente a zerar alguns coeficientes, indicando quais coeficientes realmente influenciam ou não

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Regularização Lasso e Ridge](../index.md)
- Próximo: [Ridge Regression](../ridge-regression/index.md)
