---
layout: "default"
title: "Métodos simples de previsão (baseline) — Previsão e Baselines"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 28
---

[Séries Temporais](../../index.md) · [Previsão e Baselines](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-33"></a>

# Métodos simples de previsão (baseline)


<a id="metodo-da-media"></a>
<a id="secao-34"></a>

## Método da média

![Ilustração do método da média](../../assets/A1/mean.png)

*Figura 9. Ilustração do método da média*

Prevemos todas as observações futuras pela média aritmética histórica da amostra: $${\hat{Y}}_{T + h\vert T} = {\overline{Y}}_{T} = \frac{1}{T}\sum_{t = 1}^{T}Y_{t}\text{\quad\quad}\forall h \geq 1$$

o método da média assume que o processo é **fracamente estacionário**, sem tendência e sem sazonalidade $$Y_{t} = \mu + \varepsilon_{t},\text{\quad\quad}\varepsilon_{t} \sim \text{ WN}\left( 0,\sigma^{2} \right)$$

Corresponde ao caso em que a autocorrelação $\rho(h) \approx 0$ para todo $h \geq 1$ (série sem memória linear)

Conseguimos notar também que esse estimador é **não-viesado** e **consistente**, ou seja, a previsão converge para o valor real da série temporal à medida que o tamanho da amostra aumenta (pois a média amostral converge para a média populacional).

**Teorema: Variância do Erro de Previsão**

$${\mathbb{V}}\left\lbrack \varepsilon_{T + h} \right\rbrack = \sigma^{2}\left( 1 + \frac{1}{T} \right)\text{\quad\quad}\forall h \geq 1$$ Ou seja, a precisão converge para a variância do ruído branco à medida que o tamanho da amostra aumenta ($T \rightarrow \infty$)

**Demonstração**

$$\begin{aligned} {\mathbb{V}}\left\lbrack Y_{T + h} - {\overline{Y}}_{T} \right\rbrack & = {\mathbb{V}}\left\lbrack \varepsilon_{T + h} \right\rbrack \\ & = {\mathbb{V}}\left\lbrack Y_{T + h} \right\rbrack + {\mathbb{V}}\left\lbrack {\overline{Y}}_{T} \right\rbrack - 2\text{ Cov}\left( Y_{T + h},{\overline{Y}}_{T} \right) \\ & = \sigma^{2} + \frac{\sigma^{2}}{T} \\ & = \sigma^{2}\left( 1 + \frac{1}{T} \right) \end{aligned}$$ Aqui a covariância entre $Y_{T + h}$ e ${\overline{Y}}_{T}$ é nula, pois o ruído branco não possui memória linear, logo não há correlação entre o valor futuro e a média amostral (além de que o valor futuro está fora dos valores utilizados para a estimação da média amostral, pois $h \geq 1$)

<a id="metodo-do-desvio-drift"></a>
<a id="secao-37"></a>

## Método do desvio (drift)

![Ilustração do método do desvio](../../assets/A1/drift.png)

*Figura 12. Ilustração do método do desvio*

Extrapola uma tendência linear permitindo que a previsão mude ao longo do tempo a uma taxa constante $C$ $${\hat{Y}}_{T + h\vert T} = Y_{T} + hC\text{\quad\quad}\forall h \geq 1$$

onde a taxa de variação (inclinação do desvio) é estimada pela variação média por período entre a primeira e a última observação da amostra $$C = \frac{Y_{T} - Y_{1}}{T - 1}$$

na intuição geométrica, estamos traçando uma linha reta entre o primeiro e o último ponto da série temporal, e projetando essa linha para frente. Esse método assume um modelo de **Passeio Aleatório com Drift (Tendência)**: $$Y_{t} = C + Y_{t - 1} + \varepsilon_{t},\text{\quad\quad}\varepsilon_{t} \sim \text{ WN}\left( 0,\sigma^{2} \right)$$

<a id="metodo-ingenuo-passeio-aleatorio-sem-tendencia"></a>
<a id="secao-35"></a>

## Método ingênuo (Passeio aleatório sem tendência)

![Ilustração do método ingênuo](../../assets/A1/naive.png)

*Figura 10. Ilustração do método ingênuo*

A previsão para qualquer horizonte futuro é o **último valor observado** da série $${\hat{Y}}_{T + h\vert T} = Y_{T}\text{\quad\quad}\forall h \geq 1$$

ele assume que o processo segue um **Passeio Aleatório** puro (não-estacionário na variância) $$Y_{t} = Y_{t - 1} + \varepsilon_{t},\text{\quad\quad}\varepsilon_{t} \sim \text{ IID}\left( 0,\sigma^{2} \right)$$

É o caso limite em que a autocorrelação de curto prazo é extremamente alta ($\rho(h) \approx 1$ para $h$ pequeno). O estado atual $Y_{T}$ é a melhor estimativa para a posição futura

O erro de previsão acaba por ser a soma dos ruídos futuros acumulados $$Y_{T + h} - {\hat{Y}}_{T + h\vert T} = Y_{T + h} - Y_{T} = \varepsilon_{T + 1} + \ldots + \varepsilon_{T + h}$$

É fácil ver que o estimador é não-viezado (basta tirar a esperança do erro de previsão). E podemos mostrar que a variância da previsão aumenta linearmente com o horizonte de previsão, pois a variância do erro de previsão é a soma das variâncias dos ruídos futuros

**Teorema: Variância do Erro de Previsão**

$${\mathbb{V}}\left\lbrack Y_{T + h} - {\hat{Y}}_{T + h\vert T} \right\rbrack = h\sigma^{2}\text{\quad\quad}\forall h \geq 1$$ Ou seja, a precisão da previsão diminui linearmente com o horizonte de previsão, pois a variância do erro de previsão aumenta linearmente com o horizonte de previsão

**Demonstração**

$$
\begin{aligned} {\mathbb{V}}\left\lbrack Y_{T + h} - {\hat{Y}}_{T + h\vert T} \right\rbrack & = {\mathbb{V}}\left\lbrack \varepsilon_{T + 1} + \ldots + \varepsilon_{T + h} \right\rbrack \\ & = {\mathbb{V}}\left\lbrack \varepsilon_{T + 1} \right\rbrack + \ldots + {\mathbb{V}}\left\lbrack \varepsilon_{T + h} \right\rbrack \\ & = h\sigma^{2} \end{aligned}
$$

<a id="metodo-ingenuo-sazonal"></a>
<a id="secao-36"></a>

## Método ingênuo sazonal

![Ilustração do método ingênuo sazonal](../../assets/A1/seasonal_naive.png)

*Figura 11. Ilustração do método ingênuo sazonal*

Para séries com sazonalidade de período $m$ (ex: $m = 12$ para dados mensais, $m = 4$ para dados trimestrais), a previsão copia o valor observado na mesma fase do ciclo sazonal anterior $${\hat{Y}}_{T + h\vert T} = Y_{T + h - m(K + 1)}\text{\quad\quad}\forall h \geq 1\text{\quad\quad}K = \left\lfloor \frac{h - 1}{m} \right\rfloor$$

Esse método assume um modelo de **Passeio Aleatório Sazonal** sem tendência: $$Y_{t} = Y_{t - m} + \varepsilon_{t},\text{\quad\quad}\varepsilon_{t} \sim \text{ IID}\left( 0,\sigma^{2} \right)$$

Já aqui, conseguimos mostrar que a incerteza cresce não com $h$, mas a **cada ciclo sazonal completo** $${\mathbb{V}}\left\lbrack \varepsilon_{T + h} \right\rbrack = (K + 1)\sigma^{2}$$

**Teorema: Variância do Erro de Previsão**

$${\mathbb{V}}\left\lbrack Y_{T + h} - {\hat{Y}}_{T + h\vert T} \right\rbrack = (K + 1)\sigma^{2}\text{\quad\quad}\forall h \geq 1\text{\quad\quad}K = \left\lfloor \frac{h - 1}{m} \right\rfloor$$ Ou seja, a precisão da previsão diminui a cada ciclo sazonal completo, pois a variância do erro de previsão aumenta a cada ciclo sazonal completo

**Demonstração**

$$
\begin{aligned} {\mathbb{V}}\left\lbrack Y_{T + h} - {\hat{Y}}_{T + h\vert T} \right\rbrack & = {\mathbb{V}}\left\lbrack \varepsilon_{T + h - m(K + 1)} + \ldots + \varepsilon_{T + h} \right\rbrack \\ & = {\mathbb{V}}\left\lbrack \varepsilon_{T + h - m(K + 1)} \right\rbrack + \ldots + {\mathbb{V}}\left\lbrack \varepsilon_{T + h} \right\rbrack \\ & = (K + 1)\sigma^{2} \end{aligned}
$$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Previsão via Autocorrelação $\rho(h)$ e Esperança Condicional](../previsao-via-autocorrelacao-rho-h-e-esperanca-condicional/index.md)
- Próximo: [Método do desvio (drift)](#metodo-do-desvio-drift)
