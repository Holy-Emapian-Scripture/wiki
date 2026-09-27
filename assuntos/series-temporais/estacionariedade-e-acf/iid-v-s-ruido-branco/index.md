---
layout: "default"
title: "IID v.s Ruído Branco — Estacionariedade e ACF"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 24
---

[Séries Temporais](../../index.md) · [Estacionariedade e ACF](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-29"></a>

# IID v.s Ruído Branco

A distinção entre um processo **I.I.D.** (independente e identicamente distribuído) e um **Ruído Branco** (White Noise - WN) baseia-se na intensidade da independência estocástica exigida entre os instantes de tempo

**Definição: Ruído IID**

$\left\{ Y_{t} \right\} \sim \text{ I.I.D}\left( 0,\sigma^{2} \right)$ com $\sigma^{2} < \infty$ se $$\begin{aligned} {\mathbb{E}}\left\lbrack Y_{t} \right\rbrack & = 0 \\ \gamma_{Y}(h) & = \begin{cases} \sigma^{2}\text{\quad\quad}h = 0 \\ 0\text{\quad\quad}h \neq 0 \end{cases} \end{aligned}$$

Exige independência estocástica completa entre todas as variáveis aleatórias $Y_{t}$ e $Y_{s}$ ($t \neq s$). Não há qualquer dependência (linear ou não-linear) ou variação nas distribuições marginais

**Definição: Ruído Branco**

$\left\{ Y_{t} \right\} \sim \text{ WN}\left( 0,\sigma^{2} \right)$ com $\sigma^{2} < \infty$ se $$\begin{aligned} {\mathbb{E}}\left\lbrack Y_{t} \right\rbrack & = 0 \\ \gamma_{Y}(h) & = \begin{cases} \sigma^{2}\text{\quad\quad}h = 0 \\ 0\text{\quad\quad}h \neq 0 \end{cases} \end{aligned}$$

Exige apenas ausência de correlação linear ($\text{Cov}\left( Y_{t + h},Y_{t} \right) = 0$ para $h \neq 0$) e estacionariedade de 2ª ordem

**Teorema: Relação entre IID e White Noise**

$$\text{ I.I.D }\left( 0,\sigma^{2} \right) \Rightarrow \text{ WN}\left( 0,\sigma^{2} \right)$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [ACF e ACVF](../acf-e-acvf/index.md)
- Próximo: [Estimação Amostral](../estimacao-amostral/index.md)
