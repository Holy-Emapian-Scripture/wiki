---
title: "Esperança"
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
ordem_na_trilha: 5
nav_exclude: true
render_with_liquid: false
---

[Probabilidade](index.md)

<!-- wiki:original:inicio -->
<a id="secao-39"></a>

# Esperança

Esse capítulo terá bastante conceitos importantes, no entanto, também existirão muitos teoremas e demonstrações, principalmente de **propriedades** dos conceitos. Se você preferir, pode pular as demonstrações e ir direto para os conceitos, mas se possível, tente se aprofundar nas demonstrações posteriormente, pois elas vão te ajudar a entender melhor os conceitos.

<a id="secao-40"></a>

## O Valor Médio

Em problemas cotidianos, muitas vezes gostamos de fazer a pergunta *“Quanto eu ganho em média?”*, *“Quanto eu perco em média?”*, *“Quantos pontos eu consigo em média?”*, … A esperança matemática é justamente a resposta para essa pergunta, ela nos dá o valor médio esperado de uma variável aleatória, que intuitivamente seria o valor que, se eu fosse chutar que cairía, seria o valor que eu chutaria. Por exemplo, se eu tenho uma contagem de caras e coroas em $n$ jogadas, eu com certeza chutaria que cairiam $n/2$ caras e $n/2$ coroas, afinal, a moeda é honesta.

**Definição: Esperança de uma Variável Aleatória Discreta**

A esperança de uma variável aleatória discreta $X$ é definida por

$$
{\mathbb{E}}\lbrack X\rbrack = \sum_{x}x \cdot {\mathbb{P}}(X = x)
$$

A esperança existe desde que a soma esteja bem definida (existem casos que ela pode divergir e não existe um valor de esperança).

<a id="secao-41"></a>

## Law of the Unconscious Statistician

Esse teorema é nomeado de forma a tirar sarro de estatísticos. Acontece que, se você tem uma variável aleatória $X$ e uma função $g$, ao fazer $g(X)$, você pode pensar de forma inocente, que

$$
{\mathbb{E}}\left\lbrack g(X) \right\rbrack = \sum_{x}g(x) \cdot {\mathbb{P}}(X = x)
$$

 mas isso na verdade está **corretíssimo**, acontece que a demonstração desse teorema é mais complexa, mas o seu resultado intuitivo está **correto**

<a id="lotus"></a>

**Teorema: Law of the Unconscious Statistician (LOTUS)**

Sejam $X$ uma variável aleatória discreta e $g$ uma função, então

$$
{\mathbb{E}}\left\lbrack g(X) \right\rbrack = \sum_{x}g(x) \cdot {\mathbb{P}}(X = x)
$$

**Demonstração**

Pensando numa demonstração **não rigorosa**, mas intuitiva, podemos pensar que, para encontrar a probabilidade de um $z = g(x)$ ocorrer, precisamos encontrar todos os valores de $x$ que vão gerar aquele $z$. O somatório faz isso em cima dos locais corretos e soma $zp(z)$

$$
\begin{aligned} {\mathbb{E}}\lbrack Z\rbrack & = \sum_{z}z{\mathbb{P}}(Z = z) = \sum_{z}z\left( \sum_{g(x) = z}{\mathbb{P}}(X = x) \right) \\ & = \sum_{z}\sum_{g(x) = z}z{\mathbb{P}}(X = x) \\ & = \sum_{z}\sum_{g(x) = z}g(x){\mathbb{P}}(X = x) \\ & = \sum_{x}g(x){\mathbb{P}}(X = x) \end{aligned}
$$

**Corolário: Linearidade da Esperança**

A esperança é linear, ou seja, para quaisquer constantes $a$ e $b$ e variáveis aleatórias $X$ e $Y$, temos

$$
{\mathbb{E}}\lbrack aX + bY\rbrack = a{\mathbb{E}}\lbrack X\rbrack + b{\mathbb{E}}\lbrack Y\rbrack
$$

**Demonstração**

$$
\begin{array}{r} {\mathbb{E}}\lbrack aX + bY\rbrack = \sum_{x,y}(ax + by) \cdot {\mathbb{P}}(X = x,Y = y) \\ = \sum_{x,y}ax \cdot {\mathbb{P}}(X = x,Y = y) + \sum_{x,y}by \cdot {\mathbb{P}}(X = x,Y = y) \\ = a\sum_{x}x\sum_{y} \cdot {\mathbb{P}}(X = x,Y = y) + b\sum_{y}y\sum_{x} \cdot {\mathbb{P}}(X = x,Y = y) \end{array}
$$

Pela lei da probabilidade total, temos que

$$
\begin{array}{r} \sum_{y}{\mathbb{P}}(X = x,Y = y) = {\mathbb{P}}(X = x) \\ \sum_{x}{\mathbb{P}}(X = x,Y = y) = {\mathbb{P}}(Y = y) \end{array}
$$

Logo:

$$
\begin{aligned} {\mathbb{E}}\lbrack aX + bY\rbrack & = a\sum_{x}x \cdot {\mathbb{P}}(X = x) + b\sum_{y}y \cdot {\mathbb{P}}(Y = y) \\ & = a{\mathbb{E}}\lbrack X\rbrack + b{\mathbb{E}}\lbrack Y\rbrack \end{aligned}
$$

<a id="lotus-two-variables"></a>

**Teorema: LOTUS com duas variáveis**

Sejam $X$ e $Y$ variáveis aleatórias discretas e $g$ uma função, então

$$
{\mathbb{E}}\left\lbrack g(X,Y) \right\rbrack = \sum_{x,y}g(x,y) \cdot {\mathbb{P}}(X = x,Y = y)
$$

**Demonstração**

Fazendo uma demonstração não rigorosa, mas intuitiva, podemos pensar que, para encontrar a probabilidade de um $z = g(x,y)$ ocorrer, precisamos encontrar todos os valores de $x$ e $y$ que vão gerar aquele $z$. O somatório faz isso em cima dos locais corretos e soma $zp(z)$

$$
\begin{aligned} {\mathbb{E}}\lbrack Z\rbrack & = \sum_{z}z{\mathbb{P}}(Z = z) = \sum_{z}z\left( \sum_{g(x,y) = z}{\mathbb{P}}(X = x,Y = y) \right) \\ & = \sum_{z}\sum_{g(x,y) = z}z{\mathbb{P}}(X = x,Y = y) \\ & = \sum_{z}\sum_{g(x,y) = z}g(x,y){\mathbb{P}}(X = x,Y = y) \\ & = \sum_{x,y}g(x,y){\mathbb{P}}(X = x,Y = y) \end{aligned}
$$

<a id="secao-42"></a>

## Esperança e Independência

A esperança também pode ser afetada pela independência de variáveis aleatórias.

**Teorema: Esperança de Variáveis Aleatórias Independentes**

Sejam $X$ e $Y$ variáveis aleatórias discretas independentes, então

$$
{\mathbb{E}}\lbrack XY\rbrack = {\mathbb{E}}\lbrack X\rbrack \cdot {\mathbb{E}}\lbrack Y\rbrack
$$

 a volta não vale

**Demonstração**

Pela definição de independência, temos que

$$
{\mathbb{P}}(X = x,Y = y) = {\mathbb{P}}(X = x) \cdot {\mathbb{P}}(Y = y)
$$

 então

$$
\begin{aligned} {\mathbb{E}}\lbrack XY\rbrack & = \sum_{x,y}xy \cdot {\mathbb{P}}(X = x,Y = y) \\ & = \sum_{x,y}xy \cdot {\mathbb{P}}(X = x) \cdot {\mathbb{P}}(Y = y) \\ & = \sum_{x}x \cdot {\mathbb{P}}(X = x)\sum_{y}y \cdot {\mathbb{P}}(Y = y) \\ & = {\mathbb{E}}\lbrack X\rbrack \cdot {\mathbb{E}}\lbrack Y\rbrack \end{aligned}
$$

Um contra exemplo para o caso contrário são as variáveis $X$ e $Y$ tais que

$$
{\mathbb{P}}(X = 1,Y = 1) = \frac{1}{2}\quad{\mathbb{P}}(X = - 1,Y = - 1) = \frac{1}{2}
$$

 aqui conseguimos ver que

$$
{\mathbb{E}}\lbrack X\rbrack = {\mathbb{E}}\lbrack Y\rbrack = 0
$$

 no entanto

$$
{\mathbb{E}}\lbrack XY\rbrack = 1
$$

 pois $X \cdot Y$ é sempre $1$

Acontece que, se duas variáveis são independentes, ao fazer $XY$, os valores de $X$ não influenciam nos valores de $Y$, logo, todos os valores de $XY$ são *“igualmente”* prováveis, não no sentido que cada um tem $1/\left( \vert S\vert  \right)$ de probabilidade, mas num sentido que, se eu pegar um valor de $X$ e um valor de $Y$, a probabilidade de que eles se encontrem é a mesma, e isso é justamente o que a definição de independência nos diz. Já se eles não forem independentes, como o valor de $X$ incluencia no de $Y$, pode acontecer de existirem valores de $XY$ mais prováveis de aparecer do que outros.

**Exemplo: Caso de Independência**

Suponha que eu jogo dois dados justos, e defino as variáveis aleatórias

$$
X = \ valor\ do\ dado\ 1\ \quad Y = \ valor\ do\ dado\ 2
$$

 Então, $X$ e $Y$ são independentes, e temos que

$$
{\mathbb{E}}\lbrack X\rbrack = {\mathbb{E}}\lbrack Y\rbrack = 3.5
$$

 então

$$
{\mathbb{E}}\lbrack XY\rbrack = {\mathbb{E}}\lbrack X\rbrack \cdot {\mathbb{E}}\lbrack Y\rbrack = 3.5 \cdot 3.5 = 12.25
$$

**Exemplo: Caso de Dependência**

Suponha que eu jogo **um** dado justo, e defino as variáveis aleatórias

$$
X = \text{ valor do dado }\quad Y = \text{ valor do dado }
$$

 aqui é **dependência total**, então

$$
X = Y
$$

 logo, se eu fizesse

$$
XY
$$

 saber o valor de $X$ **automaticamente me da o valor de $Y$**, então

$$
{\mathbb{E}}\lbrack X\rbrack{\mathbb{E}}\lbrack Y\rbrack \neq {\mathbb{E}}\lbrack XY\rbrack
$$

<a id="secao-43"></a>

## Monotonicidade da Esperança

A esperança também é uma função **monótona**, ou seja, se uma variável aleatória é maior que outra, a esperança dela também será maior.

**Teorema: Monotonicidade da Esperança**

Sejam $X$ e $Y$ variáveis aleatórias discretas, se $X \geq Y$, então

$$
{\mathbb{E}}\lbrack X\rbrack \geq {\mathbb{E}}\lbrack Y\rbrack
$$

**Demonstração**

Como $X \geq Y$, temos que $X - Y \geq 0$, então

$$
{\mathbb{E}}\lbrack X - Y\rbrack \geq 0 \Leftrightarrow {\mathbb{E}}\lbrack X\rbrack - {\mathbb{E}}\lbrack Y\rbrack \geq 0 \Leftrightarrow {\mathbb{E}}\lbrack X\rbrack \geq {\mathbb{E}}\lbrack Y\rbrack
$$

<a id="secao-44"></a>

## Função de Sobrevivência

Conseguimos expressar a esperança em termos da função de sobrevivência ([função de sobrevivência](variaveis-aleatorias-discretas.md#survival-function-discrete-random-variable)).

<a id="mean-survival-function"></a>

**Teorema: Esperança em termos da Função de Sobrevivência**

Sejam $X$ uma variável aleatória discreta não negativa, então

$$
{\mathbb{E}}\lbrack X\rbrack = \sum_{x = 0}^{\infty}G_{X}(x)
$$

**Demonstração**

Seja $I_{j}$ a variável aleatória definida como:

$$
I_{j} = \begin{cases} 1\quad X \geq j \\ 0\quad X < j \end{cases}
$$

 conseguimos decompor a variável aleatória $X$ como

$$
X = \sum_{j = 1}^{\infty}I_{j}
$$

 por exemplo, se $X = 3$, então $I_{1} = I_{2} = I_{3} = 1$ e $I_{j} = 0$ para $j > 3$. Então a esperança de $X$ será

$$
{\mathbb{E}}\lbrack X\rbrack = {\mathbb{E}}\left\lbrack \sum_{j = 1}^{\infty}I_{j} \right\rbrack = \sum_{j = 1}^{\infty}{\mathbb{E}}\left\lbrack I_{j} \right\rbrack
$$

 Agora só precisamos mostrar que ${\mathbb{E}}\left\lbrack I_{j} \right\rbrack = {\mathbb{P}}(X \geq j)$. Pela definição de $I_{j}$, sua esperança será

$$
{\mathbb{E}}\left\lbrack I_{j} \right\rbrack = 1 \cdot {\mathbb{P}}(I_{j} = 1) + 0 \cdot {\mathbb{P}}(I_{j} = 0) = {\mathbb{P}}(I_{j} = 1) = {\mathbb{P}}(X \geq j)
$$

 logo

$$
{\mathbb{E}}\lbrack X\rbrack = \sum_{j = 1}^{\infty}{\mathbb{P}}(X \geq j) = \sum_{x = 0}^{\infty}G_{X}(x)
$$
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Variáveis Aleatórias Discretas](variaveis-aleatorias-discretas.md)

- Próximo: [Medidas de Dispersão](medidas-de-dispersao.md)
