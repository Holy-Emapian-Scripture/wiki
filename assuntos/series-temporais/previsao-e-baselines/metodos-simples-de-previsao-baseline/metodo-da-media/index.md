---
layout: "default"
title: "Método da média — Métodos simples de previsão (baseline)"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 29
---

[Séries Temporais](../../../index.md) · [Previsão e Baselines](../../index.md) · [Métodos simples de previsão (baseline)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-34"></a>

# Método da média

![Ilustração do método da média](../../../assets/A1/mean.png)

*Figura 9. Ilustração do método da média*

Prevemos todas as observações futuras pela média aritmética histórica da amostra: $${\hat{Y}}_{T + h\vert T} = {\overline{Y}}_{T} = \frac{1}{T}\sum_{t = 1}^{T}Y_{t}\text{\quad\quad}\forall h \geq 1$$

o método da média assume que o processo é **fracamente estacionário**, sem tendência e sem sazonalidade $$Y_{t} = \mu + \varepsilon_{t},\text{\quad\quad}\varepsilon_{t} \sim \text{ WN}\left( 0,\sigma^{2} \right)$$

Corresponde ao caso em que a autocorrelação $\rho(h) \approx 0$ para todo $h \geq 1$ (série sem memória linear)

Conseguimos notar também que esse estimador é **não-viesado** e **consistente**, ou seja, a previsão converge para o valor real da série temporal à medida que o tamanho da amostra aumenta (pois a média amostral converge para a média populacional).

**Teorema: Variância do Erro de Previsão**

$${\mathbb{V}}\left\lbrack \varepsilon_{T + h} \right\rbrack = \sigma^{2}\left( 1 + \frac{1}{T} \right)\text{\quad\quad}\forall h \geq 1$$ Ou seja, a precisão converge para a variância do ruído branco à medida que o tamanho da amostra aumenta ($T \rightarrow \infty$)

**Demonstração**

$$\begin{aligned} {\mathbb{V}}\left\lbrack Y_{T + h} - {\overline{Y}}_{T} \right\rbrack & = {\mathbb{V}}\left\lbrack \varepsilon_{T + h} \right\rbrack \\ & = {\mathbb{V}}\left\lbrack Y_{T + h} \right\rbrack + {\mathbb{V}}\left\lbrack {\overline{Y}}_{T} \right\rbrack - 2\text{ Cov}\left( Y_{T + h},{\overline{Y}}_{T} \right) \\ & = \sigma^{2} + \frac{\sigma^{2}}{T} \\ & = \sigma^{2}\left( 1 + \frac{1}{T} \right) \end{aligned}$$ Aqui a covariância entre $Y_{T + h}$ e ${\overline{Y}}_{T}$ é nula, pois o ruído branco não possui memória linear, logo não há correlação entre o valor futuro e a média amostral (além de que o valor futuro está fora dos valores utilizados para a estimação da média amostral, pois $h \geq 1$)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Métodos simples de previsão (baseline)](../index.md)
- Próximo: [Método ingênuo (Passeio aleatório sem tendência)](../metodo-ingenuo-passeio-aleatorio-sem-tendencia/index.md)
