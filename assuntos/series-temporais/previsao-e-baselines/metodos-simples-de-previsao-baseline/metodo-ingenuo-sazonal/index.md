---
layout: "default"
title: "Método ingênuo sazonal — Métodos simples de previsão (baseline)"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 31
---

[Séries Temporais](../../../index.md) · [Previsão e Baselines](../../index.md) · [Métodos simples de previsão (baseline)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-36"></a>

# Método ingênuo sazonal

![Ilustração do método ingênuo sazonal](../../../assets/A1/seasonal_naive.png)

*Figura 11. Ilustração do método ingênuo sazonal*

Para séries com sazonalidade de período $m$ (ex: $m = 12$ para dados mensais, $m = 4$ para dados trimestrais), a previsão copia o valor observado na mesma fase do ciclo sazonal anterior $${\hat{Y}}_{T + h\vert T} = Y_{T + h - m(K + 1)}\text{\quad\quad}\forall h \geq 1\text{\quad\quad}K = \left\lfloor \frac{h - 1}{m} \right\rfloor$$

Esse método assume um modelo de **Passeio Aleatório Sazonal** sem tendência: $$Y_{t} = Y_{t - m} + \varepsilon_{t},\text{\quad\quad}\varepsilon_{t} \sim \text{ IID}\left( 0,\sigma^{2} \right)$$

Já aqui, conseguimos mostrar que a incerteza cresce não com $h$, mas a **cada ciclo sazonal completo** $${\mathbb{V}}\left\lbrack \varepsilon_{T + h} \right\rbrack = (K + 1)\sigma^{2}$$

**Teorema: Variância do Erro de Previsão**

$${\mathbb{V}}\left\lbrack Y_{T + h} - {\hat{Y}}_{T + h\vert T} \right\rbrack = (K + 1)\sigma^{2}\text{\quad\quad}\forall h \geq 1\text{\quad\quad}K = \left\lfloor \frac{h - 1}{m} \right\rfloor$$ Ou seja, a precisão da previsão diminui a cada ciclo sazonal completo, pois a variância do erro de previsão aumenta a cada ciclo sazonal completo

**Demonstração**

$$\begin{aligned} {\mathbb{V}}\left\lbrack Y_{T + h} - {\hat{Y}}_{T + h\vert T} \right\rbrack & = {\mathbb{V}}\left\lbrack \varepsilon_{T + h - m(K + 1)} + \ldots + \varepsilon_{T + h} \right\rbrack \\ & = {\mathbb{V}}\left\lbrack \varepsilon_{T + h - m(K + 1)} \right\rbrack + \ldots + {\mathbb{V}}\left\lbrack \varepsilon_{T + h} \right\rbrack \\ & = (K + 1)\sigma^{2} \end{aligned}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Método ingênuo (Passeio aleatório sem tendência)](../metodo-ingenuo-passeio-aleatorio-sem-tendencia/index.md)
- Próximo: [Método do desvio (drift)](../metodo-do-desvio-drift/index.md)
