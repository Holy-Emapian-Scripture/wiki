---
layout: "default"
title: "Valores Ajustados V.S Previsões — Previsão e Baselines"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 33
---

[Séries Temporais](../index.md) · [Previsão e Baselines](index.md)

<!-- wiki:original:inicio -->
<a id="secao-38"></a>

# Valores Ajustados V.S Previsões

É importante notar que os métodos de previsão que vimos até agora são **modelos de previsão**, e não **modelos de ajuste**. Ou seja, eles não são modelos que descrevem a série temporal, mas sim modelos que descrevem como prever o futuro da série temporal.

Para um modelo de séries temporais ajustado sobre um conjunto de dados históricos $\mathcal{F}_{T} = \left\{ Y_{1},\ldots,Y_{T} \right\}$ temos as seguintes definições

**Definição: Valores ajustados**

O valor ajustado ${\hat{Y}}_{t\vert t - 1}$ é a estimativa **dentro da amostra** de um passo à frente ($h = 1$) para instantes passados $t = 2,3,\ldots,T$. Representa o valor que o modelo teria previsto para o instante $t$ conhecendo as observações anteriores $Y_{1},Y_{2},\ldots,Y_{t - 1}$ e com parâmetros globais **já calibrados na amostra completa**

**Definição: Previsão (Forecast)**

A previsão ${\hat{Y}}_{T + h\vert T}$ são as projeções **fora da amostra** de $h$ passos à frente ($h \geq 1$) para instantes futuros $t = T + 1,T + 2,\ldots$. Utilizam estritamente a informação disponível até o instante de corte $T$, sem qualquer acesso visual ou numérico às realizações reais de $Y_{T + h}$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Método do desvio (drift)](metodos-simples-de-previsao-baseline.md#metodo-do-desvio-drift)
- Próximo: [Diagnóstico de Resíduos](../diagnostico-de-residuos.md)
