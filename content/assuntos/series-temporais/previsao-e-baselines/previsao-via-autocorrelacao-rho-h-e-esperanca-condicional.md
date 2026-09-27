---
layout: "default"
title: "Previsão via Autocorrelação $\\rho(h)$ e Esperança Condicional — Previsão e Baselines"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 27
---

[Séries Temporais](../index.md) · [Previsão e Baselines](index.md)

<!-- wiki:original:inicio -->
<a id="secao-32"></a>

# Previsão via Autocorrelação $\rho(h)$ e Esperança Condicional

**Definição**

Seja $\left\{ Y_{t} \right\}$ um processo estocástico **gaussiano** e **fracamente estacionário**, com média constante ${\mathbb{E}}\left\lbrack Y_{t} \right\rbrack = \mu$, variância ${\mathbb{V}}\left\lbrack Y_{t} \right\rbrack = \gamma_{Y}(0) = \sigma^{2}$ e função de autocorrelação $\rho_{Y}(h) = \gamma_{Y}(h)/\sigma^{2}$. O vetor formado pela observação presente $Y_{n}$ e pela observação futura $Y_{n + h}$ segue uma [distribuição normal](../../probabilidade/distribuicoes-continuas.md#secao_dist_normal) bivariada $$\begin{pmatrix} Y_{n} \\ Y_{n + h} \end{pmatrix} \sim \mathcal{N}(\begin{pmatrix} \mu \\ \mu \end{pmatrix},\begin{pmatrix} \sigma^{2} & \rho_{Y}(h)\sigma^{2} \\ \rho_{Y}(h)\sigma^{2} & \sigma^{2} \end{pmatrix})$$

**Teorema: Condicional Gaussiana**

Sob a hipótesse de gaussianidade no processo $\left\{ Y_{t} \right\}$, a distribuição condicional de $Y_{n + h}$ dado $Y_{n} = y_{n}$ é dada por $$Y_{n + h}~\vert ~Y_{n} = y_{n} \sim \mathcal{N}(\mu + \rho_{Y}(h)\left( y_{n} - \mu \right),\sigma^{2}\left( 1 - \rho_{Y}(h)^{2} \right))$$

**Demonstração**

Defina a variável transformada $Z = \left( Y_{n + h} - \mu \right) - \beta\left( Y_{n} - \mu \right)$ onde $\beta$ é uma constante real **a ser determinada** para que $Z$ e $Y_{n}$ sejam **não-correlacionadas**. Pela definição de covariância, temos que $$\begin{aligned} \text{ Cov}\left( Z,Y_{n} \right) & = \text{ Cov}\left( \left( Y_{n + h} - \mu \right) - \beta\left( Y_{n} - \mu \right),Y_{n} \right) \\ & = \text{ Cov}\left( Y_{n + h},Y_{n} \right) - \beta{\mathbb{V}}\left\lbrack Y_{n} \right\rbrack \\ & = \gamma_{Y}(h) - \beta\sigma^{2} \end{aligned}$$

para anular a covariância, escolhemos $\beta = \frac{\gamma_{Y}(h)}{\sigma^{2}} = \rho_{Y}(h)$, assim: $$Z = \left( Y_{n + h} - \mu \right) - \rho_{Y}(h)\left( Y_{n} - \mu \right)$$

como $\left( Z,Y_{n} \right)$ é um vetor normal, temos que o fato de $\text{Cov}\left( Z,Y_{n} \right) = 0$ implica que $Z$ e $Y_{n}$ são independentes. Utilizando desse fato, sabemos que $$\begin{aligned} {\mathbb{E}}\left\lbrack Z~\vert ~Y_{n} \right\rbrack = {\mathbb{E}}\lbrack Z\rbrack & = 0 \\ {\mathbb{E}}\left\lbrack Y_{n + h} - \mu - \rho_{Y}(h)\left( Y_{n} - \mu \right)~\vert ~Y_{n} \right\rbrack & = 0 \\ {\mathbb{E}}\left\lbrack Y_{n + h}~\vert ~Y_{n} \right\rbrack - \mu - \rho_{Y}(h)\left( Y_{n} - \mu \right) & = 0 \\ {\mathbb{E}}\left\lbrack Y_{n + h}~\vert ~Y_{n} \right\rbrack & = \mu + \rho_{Y}(h)\left( Y_{n} - \mu \right) \end{aligned}$$

Já para a variância condional, temos que $$\begin{aligned} {\mathbb{V}}\left\lbrack Y_{n + h}~\vert ~Y_{n} \right\rbrack & = {\mathbb{V}}\left\lbrack Z + \rho_{Y}(h)\left( Y_{n} - \mu \right)~\vert ~Y_{n} \right\rbrack \end{aligned}$$ como é DADO $Y_{n}$, o termo $\rho_{Y}(h)\left( Y_{n} - \mu \right)$ é uma constante, logo $$\begin{aligned} {\mathbb{V}}\left\lbrack Y_{n + h}~\vert ~Y_{n} \right\rbrack & = {\mathbb{V}}\left\lbrack Z~\vert ~Y_{n} \right\rbrack = {\mathbb{V}}\lbrack Z\rbrack \\ & = {\mathbb{V}}\left\lbrack Y_{n + h} - \mu - \rho_{Y}(h)\left( Y_{n} - \mu \right) \right\rbrack \\ & = {\mathbb{V}}\left\lbrack Y_{n + h} \right\rbrack + \rho_{Y}(h)^{2}{\mathbb{V}}\left\lbrack Y_{n} \right\rbrack - 2\rho_{Y}(h)\text{ Cov}\left( Y_{n + h},Y_{n} \right) \\ & = \sigma^{2} + \rho_{Y}(h)^{2}\sigma^{2} - 2\rho_{Y}(h)\gamma_{Y}(h) \\ & = \sigma^{2} + \rho_{Y}(h)^{2}\sigma^{2} - 2\rho_{Y}(h)^{2}\sigma^{2} \\ & = \sigma^{2}\left( 1 - \rho_{Y}(h)^{2} \right) \end{aligned}$$

Dado esse contexto, podemos agora mostrar que para **qualquer preditor $g\left( Y_{n} \right)$**, **o preditor que minimiza o erro quadrático médio** é a **média condicional ${\mathbb{E}}\left\lbrack Y_{n + h}~\vert ~Y_{n} \right\rbrack$**.

**Teorema: Preditor que minimiza o MSE**

Para qualquer preditor $g\left( Y_{n} \right)$ baseado na observação $Y_{n}$, o preditor que minimiza o erro quadrático médio (${\mathbb{E}}\left\lbrack \left( Y_{n + h} - g\left( Y_{n} \right) \right)^{2} \right\rbrack$) é dado por $$g\left( Y_{n} \right) = {\mathbb{E}}\left\lbrack Y_{n + h}~\vert ~Y_{n} \right\rbrack$$

**Demonstração**

Definindo o erro quadrático médio como $f$, temos: $$\begin{aligned} f\left( y_{n} \right) & = {\mathbb{E}}\left\lbrack \left( Y_{n + h} - g\left( Y_{n} \right) \right)^{2}\vert Y_{n} = y_{n} \right\rbrack \end{aligned}$$

expandindo o termo quadrático, derivando e igualando a $0$, vamos ter que $$g\left( Y_{n} \right) = {\mathbb{E}}\left\lbrack Y_{n + h}~\vert ~Y_{n} = y_{n} \right\rbrack$$

Sob a hipótese de gaussianidade, o preditor linear possui forma fechada de: $${\mathbb{E}}\left\lbrack Y_{n + h}~\vert ~Y_{n} \right\rbrack = \mu + \rho_{Y}(h)\left( Y_{n} - \mu \right)$$ no entanto, sem essa premissa, o preditor linear pode não possuir forma fechada, mas ainda assim é o preditor que minimiza o erro quadrático médio. E como podemos perceber, a função $\rho_{Y}(h)$ determina diretamente a qualidade e o formato da predição

- $\rho_{Y}(h) \rightarrow 0$: A previsão tende a $\mu$ e o erro quadrático médio tende a $\sigma^{2}$, ou seja, a informação presente $Y_{n}$ não traz informação útil sobre o futuro $Y_{n + h}$. O melhor preditor reduz-se à média incondicional e a incerteza atinge a variância total da série

- $\rho_{Y}(h) \rightarrow 1$: A previsão tende a $Y_{n}$ e o erro quadrático médio tende a $0$, ou seja, a informação presente $Y_{n}$ praticamente carrega toda a informação sobre o futuro $Y_{n + h}$. O melhor preditor aproxima-se do valor atual e a incerteza diminui significativamente

Mas como eu comentei antes, esse é o melhor preditor **sobre gaussianiedade**, mas não necessariamente o melhor preditor **sobre a série temporal**. No entanto, é possível chegar que, definindo um preditor genérico $l\left( Y_{n} \right) = \alpha Y_{n} + \beta$, o melhor $l$ é exatamente o preditor linear que obtivemos na prova anterior

**Teorema: Preditor Linear que minimiza o MSE**

Para qualquer preditor linear $l\left( Y_{n} \right) = \alpha Y_{n} + \beta$ baseado na observação $Y_{n}$, o preditor que minimiza o erro quadrático médio (${\mathbb{E}}\left\lbrack \left( Y_{n + h} - l\left( Y_{n} \right) \right)^{2} \right\rbrack$) é dado por $$l\left( Y_{n} \right) = \mu + \rho_{Y}(h)\left( Y_{n} - \mu \right)$$ e apresenta um erro quadrático médio de $\sigma^{2}\left( 1 - \rho_{Y}(h)^{2} \right)$

**Demonstração**

Queremos determinar os escalares $\alpha$ e $\beta$ que minimizam o erro quadrático médio $$f(\alpha,\beta) = {\mathbb{E}}\left\lbrack \left( Y_{n + h} - \left( \alpha Y_{n} + \beta \right) \right)^{2} \right\rbrack$$ expandindo o termo quadrático (e lembrando que ${\mathbb{E}}\left\lbrack Y_{n} \right\rbrack = {\mathbb{E}}\left\lbrack Y_{n + h} \right\rbrack = \mu$), temos que $$f(\alpha,\beta) = {\mathbb{E}}\left\lbrack Y_{n + h}^{2} \right\rbrack - 2\alpha{\mathbb{E}}\left\lbrack Y_{n}Y_{n + h} \right\rbrack - 2\beta\mu + \alpha^{2}{\mathbb{E}}\left\lbrack Y_{n}^{2} \right\rbrack + 2\alpha\beta\mu + \beta^{2}$$ e derivando com relação à $\alpha$ $$\frac{\partial f}{\partial\alpha} = - 2{\mathbb{E}}\left\lbrack Y_{n}Y_{n + h} \right\rbrack + 2\alpha{\mathbb{E}}\left\lbrack Y_{n}^{2} \right\rbrack + 2\beta\mu = 0$$ igualando a $0$ e isolando $\alpha$, temos que $$\alpha = \frac{{\mathbb{E}}\left\lbrack Y_{n}Y_{n + h} \right\rbrack - \beta\mu}{\mathbb{E}}\left\lbrack Y_{n}^{2} \right\rbrack$$ agora derivando com relação à $\beta$ $$\frac{\partial f}{\partial\beta} = - 2\mu + 2\alpha\mu + 2\beta = 0$$ igualando a $0$ e isolando $\beta$, temos que $$\beta = \mu(1 - \alpha)$$ substituindo $\beta$ na equação de $\alpha$, temos que $$\begin{array}{r} \alpha = \frac{{\mathbb{E}}\left\lbrack Y_{n}Y_{n + h} \right\rbrack - \mu^{2}(1 - \alpha)}{\mathbb{E}}\left\lbrack Y_{n}^{2} \right\rbrack \\ \alpha{\mathbb{E}}\left\lbrack Y_{n}^{2} \right\rbrack = {\mathbb{E}}\left\lbrack Y_{n}Y_{n + h} \right\rbrack - \mu^{2} + \alpha\mu^{2} \\ \alpha\left( {\mathbb{E}}\left\lbrack Y_{n}^{2} \right\rbrack - \mu^{2} \right) = {\mathbb{E}}\left\lbrack Y_{n}Y_{n + h} \right\rbrack - \mu^{2} \\ \alpha{\mathbb{V}}\left\lbrack Y_{n} \right\rbrack = \text{ Cov}\left( Y_{n},Y_{n + h} \right) \\ \alpha = \rho_{Y}(h) \end{array}$$

Voltando na equação de $\beta$, temos que $$\beta = \mu(1 - \alpha) = \mu(1 - \rho_{Y}(h))$$

agora substituindo na equação do preditor linear, temos que $$\begin{aligned} l\left( Y_{n} \right) & = \alpha Y_{n} + \beta \\ & = \rho_{Y}(h)Y_{n} + \mu(1 - \rho_{Y}(h)) \\ & = \mu + \rho_{Y}(h)\left( Y_{n} - \mu \right) \end{aligned}$$

Substituindo isso tudo que encontramos na fórmula do erro quadrático médio, vamos acabar chegando que $$f(\alpha,\beta) = \sigma^{2}\left( 1 - \rho_{Y}(h)^{2} \right)$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Previsão e Baselines](index.md)
- Próximo: [Métodos simples de previsão (baseline)](metodos-simples-de-previsao-baseline.md)
