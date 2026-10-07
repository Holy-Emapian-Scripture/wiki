---
title: "Medidas de Dispersão"
tags:
  - probabilidade
  - a1
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1.typ"
trilha: "../../trilhas/probabilidade/a1.md"
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 6
nav_exclude: true
render_with_liquid: false
---

[Probabilidade](index.md)

<!-- wiki:original:inicio -->
<a id="secao-45"></a>

# Medidas de Dispersão

<a id="secao-46"></a>

## Introdução

Essas medidas nos ajudam a entender o **quanto** os valores da variável aleatória estão espalhados em torno da média. Se a esperança nos dá o valor que esperamos que a variável aleatória assuma, as medidas de dispersão nos dizem o quão *“bem comportadas”* essas variáveis são, elas se concentram perto da média? Ou elas se espalham em vários lugares? Para uma visualização visual do que essas medidas representam, acesse esse vídeo: [PREENCHER — link pendente na origem]

**Definição: Desvio Médio**

O desvio médio de uma variável aleatória discreta $X$ é definido por

$$
\text{ DM}\lbrack X\rbrack = {\mathbb{E}}\left\lbrack \vert X - {\mathbb{E}}\lbrack X\rbrack\vert  \right\rbrack
$$

**Definição: Variância**

A variância de uma variável aleatória discreta $X$ é definida por

$$
{\mathbb{V}}\lbrack X\rbrack = {\mathbb{E}}\left\lbrack \left( X - {\mathbb{E}}\lbrack X\rbrack \right)^{2} \right\rbrack
$$

**Definição: Desvio Padrão**

O desvio padrão de uma variável aleatória discreta $X$ é definido por

$$
\sigma\lbrack X\rbrack = \sqrt{{\mathbb{V}}\lbrack X\rbrack}
$$

<a id="secao-47"></a>

## Propriedades

A variância e o desvio padrão são as medidas de dispersão mais utilizadas. Vamos enunciar e demonstrar algumas propriedades dessas medidas de dispersão.

**Teorema**

$$
{\mathbb{V}}\lbrack aX + b\rbrack = a^{2}{\mathbb{V}}\lbrack X\rbrack
$$

**Demonstração**

$$
\begin{aligned} {\mathbb{V}}\lbrack aX + b\rbrack & = {\mathbb{E}}\left\lbrack \left( aX + b - {\mathbb{E}}\lbrack aX + b\rbrack \right)^{2} \right\rbrack \\ & = {\mathbb{E}}\left\lbrack \left( aX + b - \left( a{\mathbb{E}}\lbrack X\rbrack + b \right) \right)^{2} \right\rbrack \\ & = {\mathbb{E}}\left\lbrack \left( aX - a{\mathbb{E}}\lbrack X\rbrack \right)^{2} \right\rbrack \\ & = {\mathbb{E}}\left\lbrack a^{2}\left( X - {\mathbb{E}}\lbrack X\rbrack \right)^{2} \right\rbrack \\ & = a^{2}{\mathbb{E}}\left\lbrack \left( X - {\mathbb{E}}\lbrack X\rbrack \right)^{2} \right\rbrack \\ & = a^{2}{\mathbb{V}}\lbrack X\rbrack \end{aligned}
$$

**Teorema**

$$
\sigma\lbrack aX + b\rbrack = \vert a\vert \sigma\lbrack X\rbrack
$$

**Demonstração**

Pela propriedade anterior, temos que

$$
\sigma\lbrack aX + b\rbrack = \sqrt{{\mathbb{V}}\lbrack aX + b\rbrack} = \sqrt{a^{2}{\mathbb{V}}\lbrack X\rbrack} = \vert a\vert \sqrt{{\mathbb{V}}\lbrack X\rbrack} = \vert a\vert \sigma\lbrack X\rbrack
$$

**Teorema**

$$
\text{ DM}\lbrack aX + b\rbrack = \vert a\vert \text{ DM}\lbrack X\rbrack
$$

**Demonstração**

Pela definição de desvio médio, temos que

$$
\begin{aligned} \text{ DM}\lbrack aX + b\rbrack & = {\mathbb{E}}\left\lbrack \vert aX + b - {\mathbb{E}}\lbrack aX + b\rbrack\vert  \right\rbrack \\ & = {\mathbb{E}}\left\lbrack \vert aX + b - \left( a{\mathbb{E}}\lbrack X\rbrack + b \right)\vert  \right\rbrack \\ & = {\mathbb{E}}\left\lbrack \vert aX - a{\mathbb{E}}\lbrack X\rbrack\vert  \right\rbrack \\ & = {\mathbb{E}}\left\lbrack \vert a\vert \vert X - {\mathbb{E}}\lbrack X\rbrack\vert  \right\rbrack \\ & = \vert a\vert {\mathbb{E}}\left\lbrack \vert X - {\mathbb{E}}\lbrack X\rbrack\vert  \right\rbrack \\ & = \vert a\vert \text{ DM}\lbrack X\rbrack \end{aligned}
$$

Intuitivamente, quando nós adicionamos uma constante $b$ em uma variável, a média vai se descolar esse exato mesmo valor, no entanto, como todos os pontos vão se mover exatamente $b$ unidades, a dispersão vai se manter a mesma. No entanto, se multiplicarmos a variável por uma constante $a$, os erros que já existiam vão se ampliar em $a$ vezes, então a dispersão vai se multiplicar por $a$ também.

**Teorema: Variância em função de Esperanças**

$$
{\mathbb{V}}\lbrack X\rbrack = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2}
$$

**Demonstração**

$$
\begin{aligned} {\mathbb{V}}\lbrack X\rbrack & = {\mathbb{E}}\left\lbrack \left( X - {\mathbb{E}}\lbrack X\rbrack \right)^{2} \right\rbrack \\ & = {\mathbb{E}}\left\lbrack X^{2} - 2X{\mathbb{E}}\lbrack X\rbrack + \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2} \right\rbrack \\ & = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack - 2{\mathbb{E}}\lbrack X\rbrack{\mathbb{E}}\lbrack X\rbrack + \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2} \\ & = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2} \end{aligned}
$$

Existe também a variância da soma de variáveis aleatórias! No entanto, vale ressaltar que o teorema abaixo é um **caso específico** do [teorema da variância da soma de variáveis aleatórias](quantificadores-de-independencia.md#variance-of-generic-variables)

**Teorema**

Se $X$ e $Y$ são variáveis aleatórias independentes, então

$$
{\mathbb{V}}\lbrack X + Y\rbrack = {\mathbb{V}}\lbrack X\rbrack + {\mathbb{V}}\lbrack Y\rbrack
$$

**Demonstração**

$$
\begin{aligned} {\mathbb{V}}\lbrack X + Y\rbrack & = {\mathbb{E}}\left\lbrack (X + Y)^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X + Y\rbrack \right)^{2} \\ & = {\mathbb{E}}\left\lbrack X^{2} + 2XY + Y^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack + {\mathbb{E}}\lbrack Y\rbrack \right)^{2} \\ & = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack + 2{\mathbb{E}}\lbrack XY\rbrack + {\mathbb{E}}\left\lbrack Y^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2} - 2{\mathbb{E}}\lbrack X\rbrack{\mathbb{E}}\lbrack Y\rbrack - \left( {\mathbb{E}}\lbrack Y\rbrack \right)^{2} \\ & = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack + 2{\mathbb{E}}\lbrack X\rbrack{\mathbb{E}}\lbrack Y\rbrack + {\mathbb{E}}\left\lbrack Y^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2} - 2{\mathbb{E}}\lbrack X\rbrack{\mathbb{E}}\lbrack Y\rbrack - \left( {\mathbb{E}}\lbrack Y\rbrack \right)^{2} \\ & = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2} + {\mathbb{E}}\left\lbrack Y^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack Y\rbrack \right)^{2} \\ & = {\mathbb{V}}\lbrack X\rbrack + {\mathbb{V}}\lbrack Y\rbrack \end{aligned}
$$

<a id="secao-48"></a>

## Desigualdade de Chebyshev

Essa desigualdade nos dá uma generalização da probabilidade estar distante de sua média. Vamos ver o teorema e sua demonstração, depois nós elaboramos mais

**Teorema: Desigualdade de Chebyshev**

Sejam $X$ uma variável aleatória discreta com média ${\mathbb{E}}\lbrack X\rbrack = \mu$ e desvio padrão $\sigma = \sigma\lbrack X\rbrack$. Denote $P = \left\{ x \in {\mathbb{R}}~\vert ~\vert x - \mu\vert  < k\sigma \right\}$, ou seja, $P$ é o intervalo aberto $(x - k\sigma,x + k\sigma)$. Então, para qualquer $k > 0$, temos que

$$
{\mathbb{P}}(X \notin P) \leq \frac{1}{k^{2}} \equiv {\mathbb{P}}(\vert X - \mu\vert  \geq k\sigma) \leq \frac{1}{k^{2}}
$$

**Demonstração**

$$
\begin{aligned} {\mathbb{V}}\lbrack X\rbrack & = {\mathbb{E}}\left\lbrack (X - \mu)^{2} \right\rbrack \\ & = \sum_{x}(x - \mu)^{2} \cdot {\mathbb{P}}(X = x) \\ & = \sum_{x \in P}(x - \mu)^{2} \cdot {\mathbb{P}}(X = x) + \sum_{x \notin P}(x - \mu)^{2} \cdot {\mathbb{P}}(X = x) \end{aligned}
$$

 por conta da definição dos $x$ no intervalo $P$, temos que, para valores de $x$ que **não estão** no intervalo:

$$
\vert x - \mu\vert  \geq k\sigma\begin{array}{r} \\ (x - \mu) \end{array}^{2} \geq k^{2}\sigma^{2}
$$

logo, como a primeira parte da soma é maior que $0$, podemos fazer:

$$
\begin{aligned} {\mathbb{V}}\lbrack X\rbrack & \geq \sum_{x \notin P}\sigma^{2}k^{2} \cdot {\mathbb{P}}(X = x) \\ \sigma^{2} & \geq \sigma^{2}k^{2}\sum_{x \notin P}{\mathbb{P}}(X = x) \\ 1 & \geq k^{2}{\mathbb{P}}(X \notin P) \\ \frac{1}{k^{2}} & \geq {\mathbb{P}}(X \notin P) \end{aligned}
$$

Como interpretamos esse teorema então?

- Existe no máximo $\frac{1}{4}$ de chance de uma variável aleatória estar a mais de $2$ desvios padrões da média

- Existe no máximo $\frac{1}{9}$ de chance de uma variável aleatória estar a mais de $3$ desvios padrões da média

- Existe no máximo $\frac{1}{16}$ de chance de uma variável aleatória estar a mais de $4$ desvios padrões da média

E assim em diante para um $k$ qualquer. Ou seja, ele atribui uma probabilidade máxima de o quão bem comportada a variável aleatória é, ou seja, o quão concentrada ela está em torno da média. Quanto maior o $k$, mais difícil é que os valores da variável aleatória estejam distantes. Isso também mostra uma quantificação de **valores extremos**. Por exemplo, é **muito improvável** que, ao jogar uma moeda honesta $100$ vezes, eu consiga $90$ caras. A desigualdade de chebyshev nos dá justamente uma formalização da intuição de que, quanto mais distante da média, mais improvável é que o evento ocorra.
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Esperança](esperanca.md)

- Próximo: [Quantificadores de Independência](quantificadores-de-independencia.md)
