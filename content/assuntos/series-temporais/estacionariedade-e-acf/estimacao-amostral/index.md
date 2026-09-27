---
layout: "default"
title: "Estimação Amostral — Estacionariedade e ACF"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 25
---

[Séries Temporais](../../index.md) · [Estacionariedade e ACF](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-30"></a>

# Estimação Amostral

No dia a dia, não conseguimos dizer com precisão os parâmetros de uma série temporal, como a média e a covariância. Para contornar essa limitação, utilizamos estimadores amostrais, que são funções das observações da série temporal que nos permitem inferir sobre os parâmetros populacionais

**Definição: Estimador de média amostral de processo estocástico fracamente estacionário**

Dada uma realização $\left\{ y_{1},y_{2},\ldots,y_{T} \right\}$ de um processo estocástico fracamente estacionário $\{ Y_{t}\}$ com média populacional ${\mathbb{E}}\left\lbrack Y_{t} \right\rbrack = \mu$ e função de autocovariância $\gamma(h) = \text{ Cov}\left( Y_{t},Y_{t + h} \right)$, o estimador da média amostral é definido por $${\overline{Y}}_{t} = \frac{1}{T}\sum_{t = 1}^{T}Y_{t}$$

**Teorema: Não-viesamento e Variância da Média Amostral**

Se $\left\{ Y_{t} \right\}$ for um processo fracamente estacionário com ${\mathbb{E}}\left\lbrack Y_{t} \right\rbrack = \mu$ e autocovariância $\gamma(h)$ então

- ${\overline{Y}}_{t}$ é um estimador não-viezado de $\mu$

- A variância de ${\overline{Y}}_{t}$ é dada por $${\mathbb{V}}\left\lbrack {\overline{Y}}_{t} \right\rbrack = \frac{1}{T}\sum_{h = - (T - 1)}^{T - 1}\left( 1 - \frac{\vert h\vert }{T} \right)\gamma(h)$$

**Demonstração**

**Parte do não-viesamento**: Aplicamos a esperança no estimador $${\mathbb{E}}\left\lbrack {\overline{Y}}_{t} \right\rbrack = {\mathbb{E}}\left\lbrack \frac{1}{T}\sum_{t = 1}^{T}Y_{t} \right\rbrack = \frac{1}{T}\sum_{t = 1}^{T}{\mathbb{E}}\left\lbrack Y_{t} \right\rbrack = \frac{1}{T}\sum_{t = 1}^{T}\mu = \mu$$

**Parte da variância**: Pela definição da variância da soma de variáveis aleatórias, temos $${\mathbb{V}}\left\lbrack {\overline{Y}}_{t} \right\rbrack = {\mathbb{V}}\left\lbrack \frac{1}{T}\sum_{t = 1}^{T}Y_{t} \right\rbrack = \frac{1}{T^{2}}{\mathbb{V}}\left\lbrack \sum_{t = 1}^{T}Y_{t} \right\rbrack = \frac{1}{T^{2}}\sum_{r = 1}^{T}\sum_{s = 1}^{T}\text{ Cov}\left( Y_{r},Y_{s} \right)$$ como o processo é fracamente estacionário, podemos reescrever a covariância como uma função do lag $h = \vert r - s\vert$, assim $${\mathbb{V}}\left\lbrack {\overline{Y}}_{t} \right\rbrack = \frac{1}{T^{2}}\sum_{r = 1}^{T}\sum_{s = 1}^{T}\gamma(\vert r - s\vert )$$

se agruparmos os pares $(r,s)$ cuja a diferença $r - s$ seja igual a um determinado lag $h$ ($\left\{ - (T - 1),\ldots,T - 1 \right\}$), nota-se que existem exatamente $T - \vert h\vert$ pares com aquele lag $h$. Logo, podemos reescrever a soma como $${\mathbb{V}}\left\lbrack {\overline{Y}}_{t} \right\rbrack = \frac{1}{T^{2}}\sum_{h = - (T - 1)}^{T - 1}\left( T - \vert h\vert  \right)\gamma(h) = \frac{1}{T}\sum_{h = - (T - 1)}^{T - 1}\left( 1 - \frac{\vert h\vert }{T} \right)\gamma(h)$$

**Definição: Autocovariância Amostral**

A autocovariância amostral usual para um lag $h \geq 0$ é definida com o divisor $T$ $$\hat{\gamma}(h) = \frac{1}{T}\sum_{t = 1}^{T - h}\left( Y_{t} - {\overline{Y}}_{t} \right)\left( Y_{t + h} - {\overline{Y}}_{t} \right)\text{\quad\quad}0 \leq h < T$$

**Teorema: Propriedades do estimador de Autocovariância Amostral**

1.  O estimador de autocovariância amostral é viesado em amostra finita, mas é **assintoticamente não-viesado** (isto é, $\lim\limits_{T \rightarrow \infty}{\mathbb{E}}\left\lbrack \hat{\gamma}(h) \right\rbrack = \gamma(h)$)

2.  O uso do divisor $T$ em vez de $T - h$ garante que a matriz de autocovariância amostral seja **semi-definida positiva**, o que é importante para a consistência de estimadores de modelos de séries temporais e minimiza o MSE para lags elevados

**Demonstração**

Para simplificar a demonstração sem perder generalidade, considere inicialmente o estimador simplificado com $\mu$ conhecido $$\widetilde{\gamma}(h) = \frac{1}{T}\sum_{t = 1}^{T - h}\left( Y_{t} - \mu \right)\left( Y_{t + h} - \mu \right)$$ tomando a esperança desse estimador $$\begin{aligned} {\mathbb{E}}\left\lbrack \widetilde{\gamma}(h) \right\rbrack & = \frac{1}{T}\sum_{t = 1}^{T - h}{\mathbb{E}}\left\lbrack \left( Y_{t} - \mu \right)\left( Y_{t + h} - \mu \right) \right\rbrack \\ & = \frac{1}{T}\sum_{t = 1}^{T - h}\gamma(h) \\ & = \frac{T - h}{T}\gamma(h) \end{aligned}$$ logo $${\mathbb{E}}\left\lbrack \widetilde{\gamma}(h) \right\rbrack - \gamma(h) = - \frac{h}{T}\gamma(h)$$

Quando substituímos $\mu$ por ${\overline{Y}}_{t}$, o estimador se torna viesado, mas a diferença entre os dois estimadores é de ordem $O\left( \frac{1}{T} \right)$, logo, o estimador com média amostral também é assintoticamente não-viesado $$\lim\limits_{T \rightarrow \infty}{\mathbb{E}}\left\lbrack \hat{\gamma}(h) \right\rbrack = \lim\limits_{T \rightarrow \infty}\left( 1 - \frac{h}{T} \right)\gamma(h) = \gamma(h)$$

Com relação à matriz semi-definida positiva, considere o vetor de observações centradas $Y = \left( Y_{1} - {\overline{Y}}_{T},\ldots,Y_{T} - {\overline{Y}}_{T} \right)^{T}$. A matriz de autocovariância amostral de ordem $k \times k$ definida como $${\hat{\Gamma}}_{k} = \left\lbrack \hat{\gamma}(i - j) \right\rbrack_{i,j = 1}^{k}$$ pode ser escrita da seguinte forma matricial $${\hat{\Gamma}}_{k} = \frac{1}{T}X^{T}X$$ onde $X_{rj} = Y_{r - j + 1} - {\overline{Y}}_{T}$ para $r \in \left\{ 1,\ldots,T + k - 1 \right\}$ e $j \in \left\{ 1,\ldots,k \right\}$. Para qualquer vetor não-nulo $a = \left( a_{1},\ldots,a_{k} \right)^{T} \in {\mathbb{R}}^{k}$: $$a^{T}{\hat{\Gamma}}_{k}a = a^{T}\left( \frac{1}{T}X^{T}X \right)a = \frac{1}{T}(Xa)^{T}(Xa) = \frac{1}{T}\| Xa\| \geq 0$$ Se dividíssemos por $T - h$ em vez de $T$, esse cancelamento matricial exato falharia, podendo gerar matrizes de autocovariância amostrais não-definidas positivas (com variâncias teóricas negativas para combinações lineares da série) e maior variabilidade estatística em $h$ elevad

**Definição: Autocorrelação Amostral**

A autocorrelação amostral é a razão normalizada $$\hat{\rho}(h) = \frac{\hat{\gamma}(h)}{\hat{\gamma}(0)}$$

<a id="acf-amostral-dist"></a>

**Teorema: Distribuição Limite sob Hipótese IID - Bartlett**

Se $\left\{ Y_{t} \right\} \sim \text{ IID}\left( 0,\sigma^{2} \right)$ com ${\mathbb{E}}\left\lbrack Y_{t}^{4} \right\rbrack < \infty$, então para qualquer $h > 0$ fixo, quando $T \rightarrow \infty$: $$\sqrt{T}{\hat{\rho}}_{h}\overset{d}{\rightarrow}\mathcal{N}(0,1)$$ e isso implica que ${\hat{\rho}}_{h} \approx \mathcal{N}(0,\frac{1}{T})$ para $T$ grande

**Demonstração**

Sob a hipótese de ruído IID, temos que $\mu = 0$, $\gamma(0) = \sigma^{2}$ e $\gamma(k) = 0\ \forall k \neq 0$.

**Passo 1 - Comportamento do Numerador**: Considere o estimador $\widetilde{\gamma}(h) = \frac{1}{T}\sum_{t = 1}^{T - h}Y_{t}Y_{t + h}$. Defina a sequência de variáveis $W_{t} = Y_{t}Y_{t + h}$. Como $\left\{ Y_{t} \right\}$ é IID, de média $0$

1.  ${\mathbb{E}}\left\lbrack W_{t} \right\rbrack = {\mathbb{E}}\left\lbrack Y_{t}Y_{t + h} \right\rbrack = {\mathbb{E}}\left\lbrack Y_{t} \right\rbrack{\mathbb{E}}\left\lbrack Y_{t + h} \right\rbrack = 0$

2.  Para $t \neq s$, as variáveis $W_{t}$ e $W_{s}$ são não-correlacionadas (Formam uma sequência de diferenças de martingale)

3.  ${\mathbb{V}}\left\lbrack W_{t} \right\rbrack = {\mathbb{E}}\left\lbrack W_{t}^{2} \right\rbrack = {\mathbb{E}}\left\lbrack Y_{t}^{2}Y_{t + h}^{2} \right\rbrack = {\mathbb{E}}\left\lbrack Y_{t}^{2} \right\rbrack{\mathbb{E}}\left\lbrack Y_{t + h}^{2} \right\rbrack = \sigma^{4}$

Pelo Teorema Central do Limite, para Sequências de Diferenças de Martingale, temos que $$\sqrt{T}\widetilde{\gamma}(h) = \frac{1}{\sqrt{T}}\sum_{t = 1}^{T - h}W_{t}\overset{d}{\rightarrow}\mathcal{N}(0,\sigma^{4})$$

**Passo 2 - Comportamento do Denominador**: O denominador $\hat{\gamma}(0)$, pela lei forte dos grandes números: $$\hat{\gamma}(0) = \frac{1}{T}\sum_{t = 1}^{T}\left( Y_{t} - {\overline{Y}}_{T} \right)^{2}\overset{p}{\rightarrow}{\mathbb{V}}\left\lbrack Y_{t} \right\rbrack = \sigma^{2}$$

**Passo 3 - Aplicação do Teorema de Slutsky**: A autocorrelação pode escrita como $$\sqrt{T}\hat{\rho}(h) = \sqrt{T}\frac{\widetilde{\gamma}(h)}{\hat{\gamma}(0)}$$

Como a substituição de ${\overline{Y}}_{T}$ por $\mu = 0$ introduz apenas termos de ordem $o_{p}(1)$ (que somem assintoticamente), aplicamos o Teorema de Slutsky combinando a convergência em distribuição do numerador com a convergência em probabilidade do denominador: $$\sqrt{T}\hat{\rho}(h) = \frac{\sqrt{T}\hat{\gamma}(h)}{\hat{\gamma}(0)}\overset{d}{\rightarrow}\frac{\mathcal{N}(0,\sigma^{4})}{\sigma^{2}} = \mathcal{N}\left( 0,\frac{\sigma^{4}}{\left( \sigma^{2} \right)^{2}} \right) = \mathcal{N}(0,1)$$

**Corolário: Construção formal do intervalo de confiança da ACF**

Do [\[acf-amostral-dist\]](#acf-amostral-dist), decorre que quando temos um ruído IID e amostras grandes, podemos construir um intervalo de confiança para a autocorrelação amostral. Para um nível de confiança $1 - \alpha$: $$\begin{array}{r} {\mathbb{P}}( - z_{1 - \alpha/2} \leq \sqrt{T}\hat{\rho}(h) \leq z_{1 - \alpha/2}) \approx 1 - \alpha \\ {\mathbb{P}}( - \frac{z_{1 - \alpha/2}}{\sqrt{T}} \leq \hat{\rho}(h) \leq \frac{z_{1 - \alpha/2}}{\sqrt{T}}) \approx 1 - \alpha \end{array}$$

Com esse corolário, podemos interpretar o seguinte: Em um teste de nível de significância $\alpha = 0.05$ (confiança $95\%$), usamos o quantil $z_{0.975} \approx 1.96$, logo o intervalo de confiança é dado por $$\left\lbrack - \frac{1.96}{\sqrt{T}},\frac{1.96}{\sqrt{T}} \right\rbrack$$

se o valor amostral $\hat{\rho}(h)$ ultrapassar um desses limites, então rejeita-se a hipótese nula $H_{0}$ da **ausência de autocorrelação** no lag $h$, ou seja, existe evidência de que a série temporal possui memória linear. Caso contrário, não rejeitamos a hipótese nula, indicando que não há evidência suficiente para afirmar que existe autocorrelação nesse lag

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [IID v.s Ruído Branco](../iid-v-s-ruido-branco/index.md)
- Próximo: [Previsão e Baselines](../../previsao-e-baselines/index.md)
