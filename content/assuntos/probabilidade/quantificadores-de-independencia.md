---
title: "Quantificadores de Independência"
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
ordem_na_trilha: 7
nav_exclude: true
render_with_liquid: false
---

[Probabilidade](index.md)

<!-- wiki:original:inicio -->
<a id="secao-49"></a>

# Quantificadores de Independência

<a id="secao-50"></a>

## Quantificadores de Independência

A independência de variáveis aleatórias é um conceito muito importante, mas como podemos quantificar o quão independentes duas variáveis aleatórias são? Dizer se elas são independentes com uma tabelinha de probabilidades bonitinha é muito fácil, mas e se não temos essa informação? E se nossas probabilidades são **estimadas**? E se temos uma quantidade enorme de variáveis aleatórias e queremos saber quais são independentes entre si?

**Definição: Covariância**

A covariância de duas variáveis aleatórias discretas $X$ e $Y$ é definida por

$$
\text{ Cov}(X,Y) = {\mathbb{E}}\left\lbrack \left( X - {\mathbb{E}}\lbrack X\rbrack \right)\left( Y - {\mathbb{E}}\lbrack Y\rbrack \right) \right\rbrack
$$

Como essa medida indica independência? Sabemos que $X - {\mathbb{E}}\lbrack X\rbrack$ é a distância dos valores de $X$ até sua média. Quando isso é maior ou igual a $0$, então a maioria dos valores está acima da média. Quando multiplicamos isso por $Y - {\mathbb{E}}\lbrack Y\rbrack$, se o valor for positivo e grande, é um indicativo que, conforme $X$ está acima da média, $Y$ **também está** acima da média. Se o valor for negativo e grande, é um indicativo que, conforme $X$ está acima da média, $Y$ **está abaixo** da média. Se o valor for próximo de $0$, então não há uma relação clara entre as duas variáveis aleatórias. Mas vale ressaltar que a covariância mede a independência **linear** de variáveis. O fato de ela ser $0$ **não significa** que as variáveis são $100\%$ independentes. Antes de mostrar isso, vamos mostrar uma forma mais prática de calcular a covariância.

<a id="covariance-equals-expectation-of-product-minus-product-of-expectations"></a>

**Teorema: Covariância em função de Esperanças**

$$
\text{ Cov}(X,Y) = {\mathbb{E}}\lbrack XY\rbrack - {\mathbb{E}}\lbrack X\rbrack \cdot {\mathbb{E}}\lbrack Y\rbrack
$$

**Demonstração**

$$
\begin{aligned} \text{ Cov}(X,Y) & = {\mathbb{E}}\left\lbrack \left( X - {\mathbb{E}}\lbrack X\rbrack \right)\left( Y - {\mathbb{E}}\lbrack Y\rbrack \right) \right\rbrack \\ & = {\mathbb{E}}\left\lbrack XY - X{\mathbb{E}}\lbrack Y\rbrack - Y{\mathbb{E}}\lbrack X\rbrack + {\mathbb{E}}\lbrack X\rbrack{\mathbb{E}}\lbrack Y\rbrack \right\rbrack \\ & = {\mathbb{E}}\lbrack XY\rbrack - {\mathbb{E}}\lbrack X\rbrack{\mathbb{E}}\lbrack Y\rbrack - {\mathbb{E}}\lbrack Y\rbrack{\mathbb{E}}\lbrack X\rbrack + {\mathbb{E}}\lbrack X\rbrack{\mathbb{E}}\lbrack Y\rbrack \\ & = {\mathbb{E}}\lbrack XY\rbrack - {\mathbb{E}}\lbrack X\rbrack \cdot {\mathbb{E}}\lbrack Y\rbrack \end{aligned}
$$

Agora sim podemos mostrar que correlação $0$ **não implica independência**, mas o contrário vale.

**Teorema**

$$
X\text{ e }Y\text{ são independentes } \Rightarrow \text{ Cov}(X,Y) = 0
$$

 a volta não vale

**Demonstração**

Pelo [teorema da expressão da covariância](#covariance-equals-expectation-of-product-minus-product-of-expectations), temos que

$$
\text{ Cov}(X,Y) = {\mathbb{E}}\lbrack XY\rbrack - {\mathbb{E}}\lbrack X\rbrack \cdot {\mathbb{E}}\lbrack Y\rbrack
$$

 como sabemos que $X$ e $Y$ são independentes, então ${\mathbb{E}}\lbrack XY\rbrack = {\mathbb{E}}\lbrack X\rbrack \cdot {\mathbb{E}}\lbrack Y\rbrack$, e portanto:

$$
\text{ Cov}(X,Y) = {\mathbb{E}}\lbrack X\rbrack \cdot {\mathbb{E}}\lbrack Y\rbrack - {\mathbb{E}}\lbrack X\rbrack \cdot {\mathbb{E}}\lbrack Y\rbrack = 0
$$

.

Agora se analisarmos a volta, vamos supor que $X = \left\{ 1,0, - 1 \right\}$ e $Y = X^{2}$ de forma que ${\mathbb{P}}(X = i) = \frac{1}{3}$ para $i = 1,0, - 1$. Conseguimos ver que ${\mathbb{E}}\lbrack X\rbrack = 0$ e ${\mathbb{E}}\lbrack XY\rbrack = {\mathbb{E}}\left\lbrack X^{3} \right\rbrack = 0$, logo, temos que

$$
\text{ Cov}(X,Y) = {\mathbb{E}}\lbrack XY\rbrack - {\mathbb{E}}\lbrack X\rbrack \cdot {\mathbb{E}}\lbrack Y\rbrack = 0 - 0 \cdot {\mathbb{E}}\lbrack Y\rbrack = 0
$$

 No entanto, vamos checar a condição de independência:

$$
\begin{array}{r} {\mathbb{P}}(X = 0,Y = 0) = {\mathbb{P}}(X = 0) = \frac{1}{3} \\ {\mathbb{P}}(X = 0) \cdot {\mathbb{P}}(Y = 0) = \frac{1}{3} \cdot \frac{1}{3} = \frac{1}{9} \end{array}
$$

 logo, $X$ e $Y$ **não são independentes**

<a id="secao-51"></a>

## O Problema de Escala da Covariância

A covariância é muito útil, mas ela tem um problema, a **escala**. Vamos ver isso na prática com alguns exemplos

**Exemplo**

Sejam $X$ a altura de uma população e $Y$ o peso dessa população. Se $X$ é medido em *m* e $Y$ em *kg*, poderíamos obter uma covariância de

$$
\text{ Cov}(X,Y) = 0.7\text{ m } \cdot \text{ kg }
$$

 No entanto, se mudarmos a unidade de medida de $X$ para *cm* e $Y$ para *g*, teríamos

$$
\text{ Cov}(100 \cdot X,1000 \cdot Y) = 100 \cdot 1000\text{ Cov}(X,Y) = 70000\text{ cm } \cdot \text{ g }
$$

 Essas covariâncias representam a **mesma relação**, mas os números são completamente diferentes. Enquanto o primeiro aparenta ser uma correlação baixa, o segundo aparenta ser uma correlação altíssima.

Para resolver esses problemas de escala e dificuldade de interpretabilidade, nós utilizamos uma outra medida, a **correlação**.

**Definição: Correlação**

A correlação de duas variáveis aleatórias discretas $X$ e $Y$ é definida por

$$
\rho(X,Y) = \frac{\text{Cov}(X,Y)}{\sigma\lbrack X\rbrack \cdot \sigma\lbrack Y\rbrack}
$$

A principal vantagem da correlação é que ela é **adimensional**, ou seja, ela não depende da unidade de medida das variáveis aleatórias. Além de se situar no intervalo $\lbrack - 1,1\rbrack$.

<a id="secao-52"></a>

## Aprofundamento: Covariância como Produto Interno

Esse tópico é um aprofundamento e preparação para futuras demonstrações dentro desse capítulo, se necessário, pode pular esse tópico na primeira leitura. Antes de provarmos algumas das propriedades da correlação (juntamente com a covariância), vamos definir ambas com um pouco de **álgebra linear**. Vamos definir a covariância como um **produto interno**.

<a id="covariance-as-inner-product"></a>

**Teorema: Covariância como Produto Interno**

Sejam $X$ e $Y$ variáveis aleatórias discretas, então a covariância entre $X$ e $Y$ pode ser interpretada como o produto interno entre dois vetores.

**Demonstração**

Sejam $X = \left\{ x_{i} \right\}\vert _{i = 1}^{m}$ e $Y = \left\{ y_{i} \right\}\vert _{i = 1}^{n}$, defina a matriz de probabilidade:

$$
\begin{pmatrix} p_{11} & p_{12} & \ldots & p_{1n} \\ p_{21} & p_{22} & \ldots & p_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ p_{m1} & p_{m2} & \ldots & p_{mn} \end{pmatrix}
$$

 de forma que ${\mathbb{P}}(X = x_{i},Y = y_{j}) = p_{ij}$. Defina também os vetores

$$
\begin{aligned} v_{X} & = \begin{pmatrix} x_{1} & x_{1} & \ldots & x_{1} & x_{2} & x_{2} & \ldots & x_{2} & \ldots & x_{m} & x_{m} & \ldots & x_{m} \end{pmatrix}^{T} \\ v_{Y} & = \begin{pmatrix} y_{1} & y_{2} & \ldots & y_{n} & y_{1} & y_{2} & \ldots & y_{n} & \ldots & y_{1} & y_{2} & \ldots & y_{n} \end{pmatrix}^{T} \end{aligned}
$$

 e os vetores **resíduos**

$$
\begin{aligned} r_{X} & = v_{X} - {\mathbb{E}}\lbrack X\rbrack \cdot \mathbb{1} \\ r_{Y} & = v_{Y} - {\mathbb{E}}\lbrack Y\rbrack \cdot \mathbb{1} \end{aligned}
$$

 onde $\mathbb{1}$ é o vetor coluna de números $1$ do tamanho do vetor $v_{X}$ e $v_{Y}$. Vamo definir $\omega(x,y)$ como o seguinte produto interno:

$$
\omega(x,y) = \sum_{i,j}x_{i}y_{j}p_{ij}
$$

 segue a demonstração que essa função é um produto interno: Para ela ser um produto interno, é necessário satisfazer:

$$
\begin{array}{r} \omega(x,y) = \omega(y,x) \\ \omega(\alpha x + \beta y,z) = \alpha\omega(x,z) + \beta\omega(y,z) \\ \omega(x,x) \geq 0\quad\omega(x,x) = 0 \Leftrightarrow x = 0 \end{array}
$$

 Para a primeira condição:

$$
\sum_{i,j}x_{i}y_{j}p_{ij} = \sum_{j,i}y_{j}x_{i}p_{ji}
$$

 Para a segunda condição:

$$
\begin{aligned} \omega(\alpha x + \beta y,z) & = \sum_{i,j}\left( \alpha x_{i} + \beta y_{i} \right)z_{j}p_{ij} \\ & = \sum_{i,j}\alpha x_{i}z_{j}p_{ij} + \sum_{i,j}\beta y_{i}z_{j}p_{ij} \\ & = \alpha\sum_{i,j}x_{i}z_{j}p_{ij} + \beta\sum_{i,j}y_{i}z_{j}p_{ij} \\ & = \alpha\omega(x,z) + \beta\omega(y,z) \end{aligned}
$$

 Para a terceira condição: Perceba que $\omega(x,y) = {\mathbb{E}}\lbrack XY\rbrack$, logo, $\omega(x,x) = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack \geq 0$ e é igual a $0$ se, e somente se, $X = 0$.

Mostrado que essa função é um produto interno, podemos ver que a covariância é justamente o produto interno entre os vetores de resíduos:

$$
\begin{aligned} \omega(r_{X},r_{Y}) & = \sum_{i,j}\left( x_{i} - {\mathbb{E}}\lbrack X\rbrack \right)\left( y_{j} - {\mathbb{E}}\lbrack Y\rbrack \right)p_{ij} \\ & = {\mathbb{E}}\left\lbrack \left( X - {\mathbb{E}}\lbrack X\rbrack \right)\left( Y - {\mathbb{E}}\lbrack Y\rbrack \right) \right\rbrack \\ & = \text{ Cov}(X,Y) \end{aligned}
$$

<a id="secao-53"></a>

## Propriedades

Agora que sabemos que a covariância é um produto interno, podemos utilizar essa relação para demonstrar outras propriedades da covariância. Nem todas as propriedades aqui enunciadas utilizam dessa definição, mas já preparamos o terreno para não dividir em vários tópicos de propriedade.

**Teorema**

$$
\begin{array}{r} \text{ Cov}(X,Y) = \text{ Cov}(Y,X) \\ \text{Cov}(X,X) = {\mathbb{V}}\lbrack X\rbrack \\ \text{Cov}(\alpha X + \beta Y,Z) = \alpha\text{ Cov}(X,Z) + \beta\text{ Cov}(Y,Z) \end{array}
$$

**Demonstração**

Segue da definição de produto interno

**Teorema**

$$
{-} 1 \leq \rho(X,Y) \leq 1
$$

**Demonstração**

Utilizando os vetores resíduos que definimos na demonstração do [teorema da covariância como produto interno](#covariance-as-inner-product), temos que

$$
\cos\theta = \frac{\omega(r_{X},r_{Y})}{\| r_{X}\|\| r_{Y}\|} = \frac{\text{ Cov}(X,Y)}{\sigma\lbrack X\rbrack \cdot \sigma\lbrack Y\rbrack} = \rho(X,Y)
$$

<a id="variance-of-generic-variables"></a>

**Teorema**

$$
{\mathbb{V}}(X + Y) = {\mathbb{V}}\lbrack X\rbrack + {\mathbb{V}}\lbrack Y\rbrack + 2\text{ Cov}(X,Y)
$$

**Demonstração**

$$
\begin{aligned} {\mathbb{V}}\lbrack X + Y\rbrack & = {\mathbb{E}}\left\lbrack (X + Y)^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X + Y\rbrack \right)^{2} \\ & = {\mathbb{E}}\left\lbrack X^{2} + 2XY + Y^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2} - 2{\mathbb{E}}\lbrack X\rbrack{\mathbb{E}}\lbrack Y\rbrack - \left( {\mathbb{E}}\lbrack Y\rbrack \right)^{2} \\ & = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack + 2{\mathbb{E}}\lbrack XY\rbrack + {\mathbb{E}}\left\lbrack Y^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2} - 2{\mathbb{E}}\lbrack X\rbrack{\mathbb{E}}\lbrack Y\rbrack - \left( {\mathbb{E}}\lbrack Y\rbrack \right)^{2} \\ & = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2} + {\mathbb{E}}\left\lbrack Y^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack Y\rbrack \right)^{2} + 2\left( {\mathbb{E}}\lbrack XY\rbrack - {\mathbb{E}}\lbrack X\rbrack \cdot {\mathbb{E}}\lbrack Y\rbrack \right) \\ & = {\mathbb{V}}\lbrack X\rbrack + {\mathbb{V}}\lbrack Y\rbrack + 2\text{ Cov}(X,Y) \end{aligned}
$$

**Teorema**

$$
\text{ Cov}(aX + b,Y) = a\text{ Cov}(X,Y)
$$

**Demonstração**

$$
\begin{aligned} \text{ Cov}(aX + b,Y) & = {\mathbb{E}}\left\lbrack \left( aX + b - {\mathbb{E}}\lbrack aX + b\rbrack \right)\left( Y - {\mathbb{E}}\lbrack Y\rbrack \right) \right\rbrack \\ & = {\mathbb{E}}\left\lbrack \left( aX + b - \left( a{\mathbb{E}}\lbrack X\rbrack + b \right) \right)\left( Y - {\mathbb{E}}\lbrack Y\rbrack \right) \right\rbrack \\ & = {\mathbb{E}}\left\lbrack \left( aX - a{\mathbb{E}}\lbrack X\rbrack \right)\left( Y - {\mathbb{E}}\lbrack Y\rbrack \right) \right\rbrack \\ & = a{\mathbb{E}}\left\lbrack \left( X - {\mathbb{E}}\lbrack X\rbrack \right)\left( Y - {\mathbb{E}}\lbrack Y\rbrack \right) \right\rbrack \\ & = a\text{ Cov}(X,Y) \end{aligned}
$$

**Teorema**

$$
\rho(aX + b,Y) = \begin{cases} \rho(X,Y)\quad a > 0 \\ - \rho(X,Y)\quad a < 0 \end{cases}
$$

**Demonstração**

$$
\begin{aligned} \rho(aX + b,Y) & = \frac{\text{ Cov}(aX + b,Y)}{\sigma\lbrack aX + b\rbrack \cdot \sigma\lbrack Y\rbrack} \\ & = \frac{a\text{ Cov}(X,Y)}{\vert a\vert \sigma\lbrack X\rbrack \cdot \sigma\lbrack Y\rbrack} \end{aligned}
$$

 e temos que

$$
\frac{a}{\vert a\vert } = \text{ sign}(a)
$$
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Medidas de Dispersão](medidas-de-dispersao.md)

- Próximo: [Distribuições de Variáveis Aleatórias Discretas](distribuicoes-de-variaveis-aleatorias-discretas.md)
