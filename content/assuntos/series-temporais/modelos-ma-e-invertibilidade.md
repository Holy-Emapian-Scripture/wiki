---
layout: "default"
title: "Modelos MA e Invertibilidade"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/Recaps/A1.typ"
trilha: "../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 38
---

[Séries Temporais](index.md)

<!-- wiki:original:inicio -->
<a id="scripture-secao-68"></a>

<a id="secao-43"></a>
<a id="modelos-ma-e-invertibilidade"></a>

# Modelos MA e Invertibilidade

<a id="scripture-secao-69"></a>

## Modelo de Média Móvel ($\text{MA}$)

Ao contrário do $\text{AR}(p)$, que usa valores passados de $y$, o modelo $\text{MA}(q)$ escreve $y_{t}$ como uma combinação linear dos erros passados $\varepsilon_{t}$

**Definição: Média Móvel**

Ao modelarmos $y_{t} = \text{ MA}(q)$, dizemos que:

$$
y_{t} = C + \varepsilon_{t} + \theta_{1}\varepsilon_{t - 1} + \ldots + \theta_{q}\varepsilon_{t - q}\text{\quad\quad}\varepsilon_{t} \sim \text{ WN}\left( 0,\sigma^{2} \right)
$$

Assim como o $\text{AR}(p)$, o $\text{MA}(q)$ também pode ser representado em termos de polinômios característicos.

**Definição: Polinômio Característico do $\text{MA}(q)$**

Dado um processo $\text{MA}(q)$, o polinômio característico $\theta(z)$ é definido como

$$
\theta(z) = 1 + \theta_{1}z + \theta_{2}z^{2} + \ldots + \theta_{q}z^{q}
$$

Essa definição de polinômio característico é útil para reescrever o modelo em termos do operador de defasagem $B$:

$$
\begin{aligned} y_{t} & = C + \varepsilon_{t} + \theta_{1}\varepsilon_{t - 1} + \ldots + \theta_{q}\varepsilon_{t - q} \\ & = C + \varepsilon_{t} + \theta_{1}B\varepsilon_{t} + \theta_{2}B^{2}\varepsilon_{t} + \ldots + \theta_{q}B^{q}\varepsilon_{t} \\ & = C + \left( 1 + \theta_{1}B + \theta_{2}B^{2} + \ldots + \theta_{q}B^{q} \right)\varepsilon_{t} \\ & = C + \theta(B)\varepsilon_{t} \end{aligned}
$$

<a id="scripture-secao-70"></a>

## ACF do $\text{MA}(q)$

A propriedade fundamental desse modelo é que ele possui **memória finita**, onde após $q$ períodos, o erro $\varepsilon_{t}$ não exerce mais influência

**Teorema: Memória do $\text{MA}(q)$**

Seja $Y_{t}$ um processo de Média Móvel de ordem $q$, $\text{MA}(q)$, definido por:

$$
Y_{t} = C + \varepsilon_{t} + \theta_{1}\varepsilon_{t - 1} + \theta_{2}\varepsilon_{t - 2} + \ldots + \theta_{q}\varepsilon_{t - q},\text{\quad\quad}\varepsilon_{t} \sim \text{ WN}\left( 0,\sigma^{2} \right)
$$

 onde $\theta_{q} \neq 0$. A Função de Autocorrelação (ACF) teórica $\rho(h)$ apresenta um corte abrupto exatamente após o lag $q$:

$$
\rho(h) = \begin{cases} 1\text{\quad\quad} & h = 0 \\ \frac{\sum_{j = 0}^{q - \vert h\vert }\theta_{j}\theta_{j + \vert h\vert }}{\sum_{j = 0}^{q}\theta_{j}^{2}}\text{\quad\quad} & 1 \leq \vert h\vert  \leq q\text{ assumindo }\theta_{0} = 1 \\ 0\text{\quad\quad} & \vert h\vert  > q \end{cases}
$$

**Demonstração**

Sem perda de generalidade, assuma que a constante $C = 0$ (processo centrado na média). Escrevemos o somatório compacto do processo para o instante $t$ definindo $\theta_{0} = 1$:

$$
Y_{t} = \sum_{j = 0}^{q}\theta_{j}\varepsilon_{t - j}
$$

Por definição, a autocovariância no lag $h \geq 0$ é dada pela esperança do produto de duas observações separadas por $h$ passos no tempo:

$$
\gamma(h) = {\mathbb{E}}\left\lbrack Y_{t + h}Y_{t} \right\rbrack = {\mathbb{E}}\left\lbrack \left( \sum_{j = 0}^{q}\theta_{j}\varepsilon_{t + h - j} \right)\left( \sum_{k = 0}^{q}\theta_{k}\varepsilon_{t - k} \right) \right\rbrack
$$

 Pela linearidade da esperança, podemos expandir o produto das duas somas em uma soma dupla:

$$
\gamma(h) = \sum_{j = 0}^{q}\sum_{k = 0}^{q}\theta_{j}\theta_{k}{\mathbb{E}}\left\lbrack \varepsilon_{t + h - j}\varepsilon_{t - k} \right\rbrack
$$

Como os ruídos $\varepsilon_{t}$ formam um ruído branco não-correlacionado (${\mathbb{E}}\left\lbrack \varepsilon_{r}\varepsilon_{s} \right\rbrack = 0$ para $r \neq s$ e ${\mathbb{E}}\left\lbrack \varepsilon_{r}^{2} \right\rbrack = \sigma^{2}$), a esperança ${\mathbb{E}}\left\lbrack \varepsilon_{t + h - j}\varepsilon_{t - k} \right\rbrack$ é não-nula se e somente se os índices dos ruídos forem idênticos:

$$
t + h - j = t - k \Leftrightarrow k = j - h
$$

Então vamos reescrever a autocovariância como uma soma simples, percorrendo apenas os índices $(j,k)$ que satisfazem a condição $h = j - k$:

$$
\gamma(h) = \sum_{j = 0}^{q}\theta_{j}\sum_{k = 0}^{q}\theta_{k}{\mathbb{E}}\left\lbrack \varepsilon_{t + h - j}\varepsilon_{t - k} \right\rbrack = \sum_{j = 0}^{q}\theta_{j}\theta_{j - h}\sigma^{2}
$$

No entanto, para que $k = j - h$ seja um índice válido (i.e., $k \geq 0$), precisamos que $j \geq h$. Analisando o caso $h > q$, para qualquer lag $h > q$, observamos os limites do índice $j$:

1.  Por definição do processo, $j \leq q$

2.  Para que o choque seja o mesmo, exige-se $j \geq h$

Como $h > q$, a condição exigiria que $j \geq h > q$, o que contradiz $j \leq q$. Logo, o conjunto de índices válidos é **vazio** — ou seja, as duas janelas temporais de $Y_{t + h}$ e $Y_{t}$ não compartilham nenhum choque $\varepsilon$ em comum. Portanto, para todo $h > q$, $\gamma(h) = 0$, $\forall h > q$, logo $\rho(h) = 0\ \forall h > q$.

Agora desenvolvendo o caso $1 \leq h \leq q$, temos que a soma válida de índices $j$ é limitada por $h \leq j \leq q$, então podemos reescrever a autocovariância como:

$$
\gamma(h) = \sigma^{2}\sum_{j = h}^{q}\theta_{j}\theta_{j - h} = \sigma^{2}\sum_{j = 0}^{q - h}\theta_{j + h}\theta_{j}
$$

Dividindo isso por $\gamma(0)$, temos que

$$
\rho(h) = \frac{\gamma(h)}{\gamma(0)} = \frac{\sigma^{2}\sum_{j = 0}^{q - h}\theta_{j + h}\theta_{j}}{\sigma^{2}\sum_{j = 0}^{q}\theta_{j}^{2}} = \frac{\sum_{j = 0}^{q - h}\theta_{j + h}\theta_{j}}{\sum_{j = 0}^{q}\theta_{j}^{2}}
$$

e quando $\vert h\vert  = 0$, temos $\rho(0) = 1$, fechando assim todos os casos da ACF do $\text{MA}(q)$

<a id="scripture-secao-71"></a>

## Invertibilidade

**Definição: Invertibilidade do $\text{MA}(q)$**

Um processo $\text{MA}(q)$ dado por $y_{t} = C + \theta(B)\varepsilon_{t}$ é dito **invertível** se todas as raízes complexas $z_{j}$ do seu polinômio característico $\theta(z) = 0$ estão estritamente fora do círculo unitário no plano complexo:

$$
\vert z_{j}\vert  < 1\text{\quad\quad}\forall j \in \left\{ 1,\ldots,q \right\}
$$

<a id="scripture-secao-72"></a>

## $\text{MA}(1)$ como $\text{AR}(\infty)$

Conseguimos reescrever um processo $\text{MA}(1)$ como um processo $\text{AR}(\infty)$ de choques passados acumulados:

**Teorema**

Seja $y_{t}$ um processo $\text{MA}(1)$, ou seja, $y_{t} = C + \theta_{1}\varepsilon_{t - 1} + \varepsilon_{t}$ com $\vert \theta_{1}\vert  < 1$. Então, o processo pode ser reescrito como:

$$
\begin{array}{r} y_{t} = \sum_{j = 1}^{\infty}\varphi_{j}y_{t - j} + \varepsilon_{t} \\ \varphi_{j} = {- \left( - \theta_{1} \right)}^{j} \end{array}
$$

**Demonstração**

Temos que

$$
y_{t} = \left( 1 + \theta_{1}B \right)\varepsilon_{t}
$$

 pela hipótese de invertibilidade, sabemos que $\vert \theta_{1}\vert  < 1$, e para qualquer $x \in {\mathbb{C}}$ tal que $\vert x\vert  < 1$, a função $(1 - x)^{- 1}$ admite uma expansão geométrica (Série de Neumann) infinita convergente

$$
(1 + x)^{- 1} = \sum_{j = 0}^{\infty}( - x)^{j}
$$

então temos que

$$
\left( 1 + B\theta_{1} \right)^{- 1} = \sum_{j = 0}^{\infty}\left( - B\theta_{1} \right)^{j} = \sum_{j = 0}^{\infty}\left( - \theta_{1} \right)^{j}B^{j}
$$

multiplicando ambos os lados da equação $y_{t} = \left( 1 + \theta_{1}B \right)\varepsilon_{t}$ por $\left( 1 + B\theta_{1} \right)^{- 1}$:

$$
\begin{aligned} \varepsilon_{t} & = \left( 1 + B\theta_{1} \right)^{- 1}y_{t} \\ \varepsilon_{t} & = \sum_{j = 0}^{\infty}\left( - \theta_{1} \right)^{j}B^{j}y_{t} \\ & = \sum_{j = 0}^{\infty}\left( - \theta_{1} \right)^{j}y_{t - j} \\ & = y_{t} + \sum_{j = 1}^{\infty}\left( - \theta_{1} \right)^{j}y_{t - j} \\ y_{t} & = - \sum_{j = 1}^{\infty}\left( - \theta_{1} \right)^{j}y_{t - j} + \varepsilon_{t} \\ y_{t} & = \sum_{j = 1}^{\infty}\varphi_{j}y_{t - j} + \varepsilon_{t} \end{aligned}
$$

<a id="scripture-secao-73"></a>

## Não-Identificabilidade do $\text{MA}(1)$ não invertível

**Teorema**

Os modelos $\text{MA}(1)$ com parâmetro $\theta_{1} = \theta$ e com parâmetro $\theta_{1} = \frac{1}{\theta}$ geram exatamente a mesma Função de Autocorrelação (ACF).

**Demonstração**

Seja $\rho_{\theta}(1)$ a ACF no lag $1$ do modelo com parâmetro $\theta$:

$$
\rho_{\theta}(1) = \frac{\theta}{1 + \theta^{2}}
$$

 Substituindo $\theta$ por $\widetilde{\theta} = \frac{1}{\theta}$:

$$
\rho_{\widetilde{\theta}}(1) = \frac{\frac{1}{\theta}}{1 + \left( \frac{1}{\theta} \right)^{2}} = \frac{\frac{1}{\theta}}{\frac{\theta^{2} + 1}{\theta^{2}}} = \frac{1}{\theta} \cdot \frac{\theta^{2}}{\theta^{2} + 1} = \frac{\theta}{1 + \theta^{2}} = \rho_{\theta}(1)
$$

Mas por que isso seria um problema? A amostra de dados não consegue distinguir um $\text{MA}(1)$ com $\theta = 0.5$ de um com $\theta = 2$ pois ambos geram a mesma ACF. Se o modelo tivesse $\theta = 2$ (não-invertível), a recuperação do erro usaria pesos $( - 2)^{j}$ que explodem no passado remoto. Para garantir identificabilidade única e uma expansão $\text{AR}(\infty)$ estável, todos os algoritmos de estimação impõem estritamente a restrição de invertibilidade $\vert \theta\vert  < 1$

<a id="scripture-secao-74"></a>

## $\text{AR}(1)$ como $\text{MA}(\infty)$

Todo processo $\text{AR}(p)$ **estacionário** pode ser reescrito como um processo $\text{MA}(\infty)$ de choques passados acumulados:

**Teorema**

Se $\vert \varphi_{1}\vert  < 1$, o modelo $y_{t} = \varphi_{1}y_{t - 1} + \varepsilon_{t}$ admite a representação:

$$
y_{t} = \sum_{j = 0}^{\infty}\varphi_{1}^{j}\varepsilon_{t - j}
$$

**Demonstração**

Substituindo a equação de $y_{t - 1}$ recursivamente em $y_{t}$:

$$
y_{t} = \varphi_{1}\left( \varphi_{1}y_{t - 2} + \varepsilon_{t - 1} \right) + \varepsilon_{t} = \varepsilon_{t} + \varphi_{1}\varepsilon_{t - 1} + \varphi_{1}^{2}y_{t - 2}
$$

 Após $N$ substituições:

$$
y_{t} = \sum_{j = 0}^{N}\varphi_{1}^{j}\varepsilon_{t - j} + \varphi_{1}^{N + 1}y_{t - N - 1}
$$

 Tomando o limite $N \rightarrow \infty$, como $\vert \varphi_{1}\vert  < 1$, o termo de memória inicial $\varphi_{1}^{N + 1}y_{t - N - 1} \rightarrow 0$, resultando em $y_{t} = \sum_{j = 0}^{\infty}\varphi_{1}^{j}\varepsilon_{t - j}$
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Modelo AR e PACF](modelo-ar-e-pacf.md)

- Próximo: [Modelo ARIMA](modelo-arima.md)
