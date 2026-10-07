---
title: "Variáveis Aleatórias Discretas"
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
ordem_na_trilha: 4
nav_exclude: true
render_with_liquid: false
---

[Probabilidade](index.md)

<!-- wiki:original:inicio -->
<a id="secao-29"></a>

# Variáveis Aleatórias Discretas

<a id="secao-30"></a>

## Experimentos Aleatórios

Dentro de um experimento qualquer, estamos a todo momento medindo quantidades, como por exemplo, o número de vezes que um dado caiu em $6$, ou o número de vezes que uma moeda caiu em **cara**. Essas quantidades são chamadas de **variáveis aleatórias**.

**Definição: Variável Aleatória Discreta**

Uma variável aleatória discreta é uma função $X:S \rightarrow {\mathbb{R}}$ que associa a cada resultado do espaço amostral $S$ um número real $\mathbb{R}$ e tal que o conjunto de valores assumidos por $X$,

$$
\text{ Im}(X) = \left\{ X(s):s \in S \right\}
$$

 é **finito** ou **enumerável**.

**Exemplo**

Dado um experimento de jogar uma moeda honesta $3$ vezes, poderíamos ter as seguintes variáveis aleatórias discretas:

$$
\begin{array}{r} X = \text{ número de caras } \\ Y = \text{ número de transições de cara para coroa } \end{array}
$$

O nome de **aleatório** não vem do número em si, mas vem da **naturaza do experimento** conter aleatoriedade

<a id="secao-31"></a>

## Função de Massa

Precisamos definir uma forma de associar cada valor que a variável aleatória pode assumir com a probabilidade que aquele valor ocorra no meu experimento, é aí que entra a **função de massa**.

<a id="secao-32"></a>

### Probabilidade Marginal

É a função que descreve a probabilidade de cada valor que a variável aleatória discreta pode assumir. Por exemplo, se eu jogo uma moeda honesta $3$ vezes, a variável aleatória $X$ que mede o número de caras pode assumir os valores $0$, $1$, $2$ e $3$. A função de massa de probabilidade vai me dizer qual a probabilidade de cada um desses valores ocorrer.

**Definição: Função de Massa de Probabilidade (PMF)**

A função de massa de probabilidade (ou PMF) de uma variável aleatória discreta $X$ é uma função $p_{X}:{\mathbb{R}} \rightarrow \lbrack 0,1\rbrack$ definida por

$$
p_{X}(x) = {\mathbb{P}}(X = x)
$$

 para todo $x \in {\mathbb{R}}$. A função de massa de probabilidade satisfaz as seguintes propriedades:

1.  $p_{X}(x) \geq 0$ para todo $x \in {\mathbb{R}}$

2.  $\sum_{x \in \text{ Im}(X)}p_{X(x)} = 1$

Essa função também é chamada de **Probabilidade Marginal de $X$**.

<a id="secao-33"></a>

### Probabilidade Conjunta

Outra função de massa muito importante é a que descreve o comportamento de múltiplas variáveis aleatórias conjuntamente, associando como um conjunto de valores que as variáveis aleatórias podem assumir, e qual a probabilidade de cada conjunto ocorrer.

**Definição: Função de Massa Conjunta**

Sejam $X_{1},\ldots,X_{n}$ variáveis aleatórias discretas, a função de massa conjunta é uma função $p_{X_{1},\ldots,X_{n}}:{\mathbb{R}}^{n} \rightarrow \lbrack 0,1\rbrack$ definida por

$$
p_{X_{1},\ldots,X_{n}}\left( x_{1},\ldots,x_{n} \right) = {\mathbb{P}}(X_{1} = x_{1},\ldots,X_{n} = x_{n})
$$

**Definição: Função de Massa Condicional**

Sejam $X_{1},\ldots,X_{n}$ variáveis aleatórias discretas e $Y$ uma variável aleatória discreta, a função de massa condicional é uma função $p_{X_{1},\ldots,X_{n}\vert Y}:{\mathbb{R}}^{n} \rightarrow \lbrack 0,1\rbrack$ definida por

$$
p_{X_{1},\ldots,X_{n}\vert Y}\left( x_{1},\ldots,x_{n}\vert y \right) = {\mathbb{P}}(X_{1} = x_{1},\ldots,X_{n} = x_{n}\vert Y = y)
$$

Ela descreve a probabilidade de cada combinação de valores que as variáveis aleatórias podem assumir. Por exemplo, se eu jogo uma moeda honesta $3$ vezes e defino as variáveis

$$
X = \text{ número de caras }\quad Y = \text{ número de coroas }
$$

 e eu gostaria de saber ${\mathbb{P}}(X = 2,Y = 0)$. A função de massa me retornaria $0$, afinal, eu não posso ter $2$ caras e $0$ coroas ao mesmo tempo. Já se eu quisesse saber ${\mathbb{P}}(X = 2,Y = 1)$, a função de massa me retornaria $3/8$, afinal, existem $3$ maneiras de ter $2$ caras e $1$ coroa em $3$ jogadas, e o total de possibilidades é $8$.

<a id="secao-34"></a>

### Relação entre as funções de massa

Perceba que ao saber o valor de $Y$ no exemplo acima, isso me da algum tipo de informação sobre o valor de $X$! Na verdade, conseguimos obter múltiplas relações entre as funções de massa, como **independência** e **obter a marginal de $X$ a partir da conjunta**, vamos ver como isso funciona.

<a id="secao-35"></a>

#### Independência

No exemplo anterior, vimos que, se eu sei o valor de $X$, eu consigo informações sobre os possíveis valores de $Y$. Isso me é um indicativo que $X$ e $Y$ **não são independentes**. Será que a função de massa pode nos ajudar a descobrir se duas variáveis aleatórias são independentes? Na verdade sim! Lembra que definimos que dois eventos $A$ e $B$ são independentes quando ${\mathbb{P}}(A,B) = {\mathbb{P}}(A) \cdot {\mathbb{P}}(B)$? Na verdade, perceba que $X = x$ e $Y = y$ **também são eventos**, então podemos aplicar a definição de independência para variáveis aleatórias.

**Definição: Independência de Variáveis Aleatórias**

Duas variáveis aleatórias $X$ e $Y$ são independentes quando a função de massa conjunta for igual ao produto das funções de massa marginais:

$$
\begin{array}{r} p_{X,Y}(x,y) = p_{X}(x) \cdot p_{Y}(y) \\ {\mathbb{P}}(X = x,Y = y) = {\mathbb{P}}(X = x) \cdot {\mathbb{P}}(Y = y) \end{array}
$$

 para todos $x$ e $y$.

E assim como na parte de conjuntos, conseguimos extender isso para a formalização que o conhecimento de variáveis independentes não afeta a probabilidade entre elas

**Corolário: Independência por Condicionalidade**

$$
X\text{ e }Y\text{ são independentes } \Leftrightarrow {\mathbb{P}}(X = x\vert Y = y) = {\mathbb{P}}(X = x)
$$

**Exemplo**

Voltando no exemplo do dado com soma $6$, vamos separar o problema em dois eventos para aplicar a definição de independência. Seja $X$ o evento de que o primeiro valor seja $2$, e seja $Y$ o evento de que a soma dos valores seja $6$. Então, temos que

$$
{\mathbb{P}}(Y) = \frac{5}{36}\quad{\mathbb{P}}(X \cap Y) = \frac{1}{36}
$$

 então aplicando a definição:

$$
{\mathbb{P}}(X~\vert ~Y) = \frac{{\mathbb{P}}(X \cap Y)}{{\mathbb{P}}(Y)} = \frac{\frac{1}{36}}{\frac{5}{36}} = \frac{1}{5}
$$

 e como ${\mathbb{P}}(X) = \frac{1}{6}$, temos que

$$
{\mathbb{P}}(X~\vert ~Y) \neq {\mathbb{P}}(X)
$$

 logo, os eventos não são independentes.

<a id="secao-36"></a>

#### Marginalização

Lembra que o [teorema da lei da probabilidade total](probabilidade-condicional.md#law-of-total-probability) indica como obter a probabilidade de um evento $B$ em função de outros eventos disjuntos? Na verdade, conseguimos aplicar o mesmo raciocínio para variáveis aleatórias, e isso é chamado de **marginalização**. A marginalização nos permite obter a função de massa marginal de uma variável aleatória a partir da função de massa conjunta, para obter o [teorema da lei da probabilidade total](#lotp-for-discrete-random-variables), basta definir o evento $B$ como $X = x$ e os eventos $A_{j}$ como $Y = y_{j}$

<a id="lotp-for-discrete-random-variables"></a>

**Teorema: Lei da Probabilidade Total**

$$
\begin{aligned} {\mathbb{P}}(X = x) & = \sum_{y}{\mathbb{P}}(X = x\vert Y = y) \cdot {\mathbb{P}}(Y = y) \\ & = \sum_{y}{\mathbb{P}}(X = x,Y = y) \end{aligned}
$$

<a id="secao-37"></a>

## Transformações sobre as variáveis

Esse tema é bem profundo, mas agora no inicio, nós vamos ver algumas transformaçẽos básicas que podem ser aplicadas em variáveis aleatórias e **como** elas influenciam nas probabilidades dos eventos. Para os casos abaixo, considere $X$ e $Y$ variáveis aleatórias.

- $a \cdot X$ com $a \in {\mathbb{R}}$: Se a imagem de $X$ é $x_{1},\ldots,x_{n}$, então a imagem de $a \cdot X$ é $a \cdot x_{1},\ldots,a \cdot x_{n}$. A função de massa de probabilidade de $a \cdot X$ é dada por

$$
p_{a \cdot X}(a \cdot x) = p_{X}(x)
$$

 ou seja, as probabilidades não mudam, apenas os valores que a variável aleatória pode assumir.

- $X + b$ com $b \in {\mathbb{R}}$: Se a imagem de $X$ é $x_{1},\ldots,x_{n}$, então a imagem de $X + b$ é $x_{1} + b,\ldots,x_{n} + b$. A função de massa de probabilidade de $X + b$ é dada por

$$
p_{X + b}(x + b) = p_{X}(x)
$$

 ou seja, as probabilidades não mudam, apenas os valores que a variável aleatória pode assumir.

- $X + Y$: Se a imagem de $X$ é $x_{1},\ldots,x_{n}$ e a imagem de $Y$ é $y_{1},\ldots,y_{m}$, então a imagem de $X + Y$ é $x_{1} + y_{1},\ldots,x_{n} + y_{m}$. A função de massa de probabilidade de $X + Y$ pode ser calculada analíticamente, no entanto, não será o foco nesse momento. Como os problemas nessa etapa são simples, podemos calcular o novo espaço amostral de $X + Y$ manualmente e calcular as probabilidades com base nas probabilidades de $X$ e $Y$. Esse raciocínio se aplica a qualquer função $g(X,Y)$

<a id="secao-38"></a>

## Função Acumulada e de Sobrevivência

A função de distribuição acumulada (CDF) calcula a probabilidade do valor mostrado pela variável ser menor que um $x$.

<a id="cdf-discrete-random-variable"></a>

**Definição: Função de Distribuição Acumulada (CDF)**

A função de distribuição acumulada (CDF) de uma variável aleatória discreta $X$ é uma função $F_{X}:{\mathbb{R}} \rightarrow \lbrack 0,1\rbrack$ definida por

$$
F_{X}(x) = {\mathbb{P}}(X \leq x)
$$

 para todo $x \in {\mathbb{R}}$. A função de distribuição acumulada satisfaz as seguintes propriedades:

1.  $F_{X}(x)$ é não decrescente

2.  $\lim\limits_{x \rightarrow - \infty}F_{X}(x) = 0$

3.  $\lim\limits_{x \rightarrow \infty}F_{X}(x) = 1$

<a id="survival-function-discrete-random-variable"></a>

**Definição: Função de Sobrevivência**

A função de sobrevivência de uma variável aleatória discreta $X$ é uma função $G_{X}:{\mathbb{R}} \rightarrow \lbrack 0,1\rbrack$ definida por

$$
G_{X}(x) = {\mathbb{P}}(X > x)
$$

 para todo $x \in {\mathbb{R}}$. A função de sobrevivência satisfaz as seguintes propriedades:

1.  $G_{X}(x)$ é não crescente

2.  $\lim\limits_{x \rightarrow - \infty}G_{X}(x) = 1$

3.  $\lim\limits_{x \rightarrow \infty}G_{X}(x) = 0$

Essa função pode não parecer super útil no momento, mas ela é muito útil para calcular probabilidades de intervalos, por exemplo, se eu quero saber a probabilidade de $X$ estar entre $a$ e $b$!

**Teorema**

$$
{\mathbb{P}}(a < X \leq b) = F_{X}(b) - F_{X}(a)
$$

Ela também vai nos ajudar muito no futuro quando começarmos a falar sobre variáveis **contínuas**.
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Probabilidade Condicional](probabilidade-condicional.md)

- Próximo: [Esperança](esperanca.md)
