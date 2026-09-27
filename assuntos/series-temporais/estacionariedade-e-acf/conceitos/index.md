---
layout: "default"
title: "Conceitos — Estacionariedade e ACF"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 22
---

[Séries Temporais](../../index.md) · [Estacionariedade e ACF](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-27"></a>

# Conceitos

**Definição: Função Média**

Seja $\left\{ Y_{t} \right\}$ uma série temporal onde ${\mathbb{E}}\left\lbrack Y_{t}^{2} \right\rbrack < \infty$, então a média em cada instante, denotada como $$\mu_{Y}(t) = {\mathbb{E}}\left\lbrack Y_{t} \right\rbrack$$

É a tendência central do processo ao longo de $t$. Em geral pode depender do tempo: nada obriga ${\mathbb{E}}\left\lbrack Y_{i} \right\rbrack = {\mathbb{E}}\left\lbrack Y_{j} \right\rbrack$ para $i \neq j$

Nos quatro exemplos que comentamos, temos que ${\mathbb{E}}\left\lbrack \varepsilon_{t} \right\rbrack = 0$, então temos que:

- **Ruído Branco**: $\mu_{Y}(t) = 0$

- **Tendência Linear**: $\mu_{Y}(t) = \beta_{0} + \beta_{1}t$

- **AR**: $\mu_{Y}(t) = \varphi \cdot \mu_{Y}(t - 1)$

- **Passeio Aleatório**: $\mu_{Y}(t) = \mu_{Y}(t - 1)$, se considerarmos $Y_{0} = 0$, então $\mu_{Y}(t) = 0$, perceba que se mantém constante, isso mostra que uma realização não altera a **média**, mas sim a **covariância** do processo, que cresce com o tempo

**Definição: Covariância**

Dados dois instantes $r,s$, definimos a covariância entre $Y_{r}$ e $Y_{s}$ como $$\gamma_{Y}(r,s) = {\mathbb{E}}\left\lbrack \left( Y_{r} - \mu_{Y}(r) \right)\left( Y_{s} - \mu_{Y}(s) \right) \right\rbrack$$

Para vermos como a correlação nos exemplos vistos se comportam, tenha em mente que ${\mathbb{V}}\left\lbrack \varepsilon_{t} \right\rbrack = \sigma^{2}$ e $\gamma_{\varepsilon}(r,s) = 0$ para $r \neq s$

- **Ruído Branco**: $\gamma_{Y}(r,s) = 0$ para $r \neq s$, ou seja, não existe correlação entre os valores da série temporal e $\gamma_{Y}(r,s) = \sigma^{2}$ se $r = s$, ou seja, a variância é constante ao longo do tempo

- **Tendência Linear**: $$\begin{aligned} \gamma_{Y(r,s)} & = \text{ Cov}\left( Y_{r},Y_{s} \right) \\ & = \text{ Cov}\left( \beta_{0} + \beta_{1}r + \varepsilon_{r},\beta_{0} + \beta_{1}s + \varepsilon_{s} \right) \\ & = \text{ Cov}\left( \varepsilon_{r},\varepsilon_{s} \right) \\ & = \begin{cases} \sigma^{2}\text{\quad\quad}r = s \\ 0\text{\quad\quad}r \neq s. \end{cases} \end{aligned}$$

- **AR**: Dado que $Y_{t} = \varphi Y_{t - 1} + \varepsilon_{t}$, então temos: $${\mathbb{V}}\left\lbrack Y_{t} \right\rbrack = {\mathbb{V}}\left\lbrack \varphi Y_{t - 1} + \varepsilon_{t} \right\rbrack = \varphi^{2}{\mathbb{V}}\left\lbrack Y_{t - 1} \right\rbrack + \sigma^{2}$$ e se assumirmos que $Y_{t} = Y_{t - 1}$: $${\mathbb{V}}\left\lbrack Y_{t} \right\rbrack = \varphi^{2}{\mathbb{V}}\left\lbrack Y_{t} \right\rbrack + \sigma^{2} \Rightarrow {\mathbb{V}}\left\lbrack Y_{t} \right\rbrack = \frac{\sigma^{2}}{1 - \varphi^{2}}$$

- **Passeio Aleatório**: Assumindo o caso onde $Y_{t} = \varepsilon_{1} + \varepsilon_{2} + \ldots + \varepsilon_{t}$, temos que: $${\mathbb{V}}\left\lbrack Y_{t} \right\rbrack = {\mathbb{V}}\left\lbrack \varepsilon_{1} + \varepsilon_{2} + \ldots + \varepsilon_{t} \right\rbrack = t\sigma^{2}$$ Ou seja, a variância do passeio aleatório cresce linearmente com o tempo. Além disso, a covariância entre dois instantes $r$ e $s$ é dada por $$\gamma_{Y}(r,s) = {\mathbb{E}}\left\lbrack Y_{r}Y_{s} \right\rbrack = {\mathbb{E}}\left\lbrack \left( \varepsilon_{1} + \ldots + \varepsilon_{r} \right)\left( \varepsilon_{1} + \ldots + \varepsilon_{s} \right) \right\rbrack = \min(r,s)\sigma^{2}$$

**Definição: Estacionariedade Fraca**

Dizemos que uma série temporal $\left\{ Y_{t} \right\}$ é **estacionária fraca** se:

- Média $\mu_{Y}(t)$ é constante no tempo

- Covariância $\gamma_{Y}(r,s)$ depende apenas da diferença $\vert r - s\vert$ e não dos instantes absolutos $r$ e $s$

Como vemos pelos exemplos, as únicas séries que são estacionárias fracas são o **ruído branco** e o **AR**. A tendência linear e o passeio aleatório não são estacionários fracos, pois a média e a covariância dependem do tempo

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Exemplos de Série](../exemplos-de-serie/index.md)
- Próximo: [ACF e ACVF](../acf-e-acvf/index.md)
