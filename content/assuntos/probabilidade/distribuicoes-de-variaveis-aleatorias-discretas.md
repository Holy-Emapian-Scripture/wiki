---
title: "Distribuições de Variáveis Aleatórias Discretas"
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
ordem_na_trilha: 8
nav_exclude: true
render_with_liquid: false
---

[Probabilidade](index.md)

<!-- wiki:original:inicio -->
<a id="secao-54"></a>

# Distribuições de Variáveis Aleatórias Discretas

<a id="secao-55"></a>

## O que é uma distribuição?

Até o momento, o curso apresentou problemas que requerem um certo pensamento crítico e racicínio lógico. As distribuições vem para nos dar uma forma de **automatizar** o raciocínio que fizemos até agora. Elas são funções matemáticas que descrevem o comportamento de variáveis aleatórias, ou seja, elas nos dão a probabilidade de cada valor que a variável aleatória pode assumir.

<a id="secao-56"></a>

## Bernoulli

Começamos com a distribuição mais simples, a **bernoulli**. Sempre que você encontrar situações que a variável assume apenas dois valores possíveis (*sim* e *não*, *cara* e *coroa*, *sucesso* e *fracasso*), você pode modelar isso com uma distribuição de bernoulli. A distribuição de bernoulli é a base para muitas outras distribuições, como a binomial, a geométrica, a hipergeométrica, entre outras.

**Definição: Distribuição de Bernoulli**

Uma variável aleatória discreta $X$ segue uma distribuição de bernoulli com parâmetro $p \in \lbrack 0,1\rbrack$ quando sua função de massa de probabilidade é dada por

$$
p_{X}(x) = \begin{cases} p\quad x = 1 \\ 1 - p\quad x = 0 \\ 0\quad\text{ otherwise } \end{cases}
$$

Denotamos como

$$
X \sim \text{ Bernoulli}(p)
$$

Essa distribuição é muito útil para modelar eventos que podem ter apenas dois resultados, como cara ou coroa, sucesso ou fracasso, sim ou não, etc. Ela parece até bem bobinha, mas ela é a base para muitas outras distribuições que veremos mais a frente. Essa distribuição é a que se aplica justamente no caso de uma moeda honesta, onde $p = \frac{1}{2}$, basta montarmos a variável aleatória como $1$ se for cara e $0$ se for coroa.

<a id="mean-and-variance-of-bernoulli"></a>

**Teorema**

Se $X \sim \text{ Bernoulli}(p)$, então

$$
\begin{array}{r} {\mathbb{E}}\lbrack X\rbrack = p \\ {\mathbb{V}}\lbrack X\rbrack = p(1 - p) \end{array}
$$

**Demonstração**

$$
\begin{aligned} {\mathbb{E}}\lbrack X\rbrack & = 1 \cdot p + 0 \cdot (1 - p) = p \\ {\mathbb{V}}\lbrack X\rbrack & = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2} = p - p^{2} = p(1 - p) \end{aligned}
$$

<a id="secao-57"></a>

## Binomial

A partir de agora, vamos definir cada distribiução a partir de uma **história**, dessa forma, não ficamos limitados apenas à função de massa daquela distribuição, mas ao que essa distribuição significa. Sempre que um problema indicar que ele quer contar **de quantas formas** um evento pode ocorrer, ou **quantas vezes** um evento ocorre, provavelmente ele está pedindo para modelar o problema com uma distribuição binomial.

**Definição: Distribuição Binomial**

Suponha que $n$ tentativas de Bernoulli independentes sejam realizadas, cada uma com a mesma probabilidade $p$ de sucesso. Seja $X$ o **número de sucessos** nessas $n$ jogadas, a distribuição de $X$ é chamada de *“binomial”* com parâmetros $n$ e $p$. Ela é denotada por

$$
X \sim \text{ Bin}(n,p)
$$

**Teorema: PMF da Binomial**

Se $X \sim \text{ Bin}(n,p)$, então a função de massa de probabilidade de $X$ é dada por

$$
{\mathbb{P}}(X = k) = \begin{pmatrix} n \\ k \end{pmatrix}p^{k}(1 - p)^{n - k}
$$

 para $k = 0,1,2,\ldots,n$.

**Demonstração**

Imagine que temos as letras *“S”* e *“F”* representando sucesso e fracasso, respectivamente. Para achar a pmf da binomial, dado sua história, podemos imaginar que temos $n$ espaços para formar uma sequência de *“S”* e *“F”* e queremos saber de quantas formas diferentes podemos fazer isso. Vamos supor que ocorreram $k$ sucessos, então temos que escolher $k$ espaços para colocar *“S”* e os outros $n - k$ espaços serão preenchidos com *“F”*. Ou seja, aplicando o principio multiplicativo, a probabilidade seria

$$
p^{k}(1 - p)^{n - k}
$$

 no entanto, existem $\begin{pmatrix} n \\ k \end{pmatrix}$ formas diferentes de escolher os $k$ espaços para colocar *“S”*. Logo, a probabilidade total será

$$
{\mathbb{P}}(X = k) = \begin{pmatrix} n \\ k \end{pmatrix}p^{k}(1 - p)^{n - k}
$$

**Teorema: Simetria da Binomial**

Se $X \sim \text{ Bin}(n,p)$ e $q = 1 - p$, então

$$
n - X \sim \text{ Bin}(n,q)
$$

**Demonstração**

Dada a história da distribuição, se $X$ é a quantidade de sucessos entre $n$ tentativas, então $n - X$ é a quantidade de fracassos entre $n$ tentativas. Como a probabilidade de fracasso é $q = 1 - p$, então definindo $Y = n - X$, temos que:

$$
\begin{array}{r} {\mathbb{P}}(Y = k) = {\mathbb{P}}(n - X = k) = {\mathbb{P}}(X = n - k) \\ = \begin{pmatrix} n \\ n - k \end{pmatrix}p^{n - k}(1 - p)^{k} = \begin{pmatrix} n \\ k \end{pmatrix}q^{k}(1 - q)^{n - k} \end{array}
$$

**Teorema**

Se $X \sim \text{ Bin}(n,p)$, então

$$
\begin{array}{r} {\mathbb{E}}\lbrack X\rbrack = np \\ {\mathbb{V}}\lbrack X\rbrack = np(1 - p) \end{array}
$$

**Demonstração**

Vou demonstrar a esperança de duas formas. A primeira é a mais algébrica. Expresse a esperança de $X$ como a definição:

$$
{\mathbb{E}}\lbrack X\rbrack = \sum_{k = 0}^{n}k\begin{pmatrix} n \\ k \end{pmatrix}p^{k}(1 - p)^{n - k}
$$

 pelo [teorema da escolha do líder](combinatoria.md#choice-of-leader), podemos reescrever o somatório como

$$
{\mathbb{E}}\lbrack X\rbrack = \sum_{k = 1}^{n}n\begin{pmatrix} n - 1 \\ k - 1 \end{pmatrix}p^{k}(1 - p)^{n - k}
$$

 se tormarmos $j = k - 1$, também podemos reescrever o somatório como

$$
\begin{aligned} {\mathbb{E}}\lbrack X\rbrack & = n\sum_{j = 0}^{n - 1}\begin{pmatrix} n - 1 \\ j \end{pmatrix}p^{j + 1}(1 - p)^{n - 1 - j} \\ & = np\sum_{j = 0}^{n - 1}\begin{pmatrix} n - 1 \\ j \end{pmatrix}p^{j}(1 - p)^{n - 1 - j} \end{aligned}
$$

 perceba que o somatório ao lado é a soma de todas as probabilidades de uma distribuição binomial com parâmetros $n - 1$ e $p$, logo, o somatório é igual a $1$. Portanto, temos que

$$
{\mathbb{E}}\lbrack X\rbrack = np
$$

 A forma mais intuitiva é utilizando a história da distribuição. Lembra que falamos que ela é a **realização de múltiplas bernoullis independentes**? Como a Bernoulli pode ser expressa como $0$ para fracasso e $1$ para sucesso, podemos expressar a variável aleatória $X$ como a soma de $n$ variáveis aleatórias independentes de Bernoulli, ou seja,

$$
X = {\mathbb{I}}_{1} + {\mathbb{I}}_{2} + \ldots + {\mathbb{I}}_{n}
$$

 onde ${\mathbb{I}}_{j} \sim \text{ Bernoulli}(p)$. Assim, a soma dessas variáveis será exatamente a quantidade de sucessos. Aplicando a linearidade da esperança, temos que

$$
{\mathbb{E}}\lbrack X\rbrack = {\mathbb{E}}\left\lbrack {\mathbb{I}}_{1} + {\mathbb{I}}_{2} + \ldots + {\mathbb{I}}_{n} \right\rbrack = {\mathbb{E}}\left\lbrack {\mathbb{I}}_{1} \right\rbrack + {\mathbb{E}}\left\lbrack {\mathbb{I}}_{2} \right\rbrack + \ldots + {\mathbb{E}}\left\lbrack {\mathbb{I}}_{n} \right\rbrack = p + p + \ldots + p = np
$$

Para a variância, podemos utilizar a mesma ideia. Como as variáveis aleatórias de Bernoulli são independentes, temos que

$$
\begin{aligned} {\mathbb{V}}\lbrack X\rbrack & = {\mathbb{V}}\left\lbrack {\mathbb{I}}_{1} + {\mathbb{I}}_{2} + \ldots + {\mathbb{I}}_{n} \right\rbrack \\ & = {\mathbb{V}}\left\lbrack {\mathbb{I}}_{1} \right\rbrack + {\mathbb{V}}\left\lbrack {\mathbb{I}}_{2} \right\rbrack + \ldots + {\mathbb{V}}\left\lbrack {\mathbb{I}}_{n} \right\rbrack \\ & = p(1 - p) + p(1 - p) + \ldots + p(1 - p) \\ & = np(1 - p) \end{aligned}
$$

<a id="secao-58"></a>

## Hípergeométrica

Essa é uma das mais confusas, pois sua história é bem longa, mas vamos simplificar ao máximo. Quando você conseguir associar um problema com retirar elementos de **dois grupos diferentes** (sem reposição), então você está diante de uma distribuição hípergeométrica.

**Definição: Distribuição Hípergeométrica**

Suponha que tenhamos **uma urna** com $w$ **bolas brancas** e $b$ **bolas pretas**. Se tirarmos $n$ bolas da urna *com reposição*, isso nos dá uma distribuição binomial para o número de bolas brancas que tiramos. No entanto, se tirarmos $n$ bolas da urna **sem reposição**, e $X$ for a quantidade de bolas brancas retiradas, então ela segue uma distribuição hípergeométrica, denotada como

$$
X \sim \text{ HGeo}(w,b,n)
$$

**Teorema: PMF da Hípergeométrica**

Se $X \sim \text{ HGeo}(w,b,n)$, então a função de massa de probabilidade de $X$ é dada por

$$
{\mathbb{P}}(X = k) = \frac{\begin{pmatrix} w \\ k \end{pmatrix}\begin{pmatrix} b \\ n - k \end{pmatrix}}{\begin{pmatrix} w + b \\ n \end{pmatrix}}
$$

 para $k = \max(0,n - b),\ldots,\min(n,w)$.

**Demonstração**

Temos no total, $w + b$ bolas, e vamos retirar $n$ no total, então nosso espaço amostral é o total de combinação que podemos fazer com $n$ bolas dentre $w + b$, ou seja, $\begin{pmatrix} w + b \\ n \end{pmatrix}$. Agora, para que tenhamos exatamente $k$ bolas brancas, precisamos escolher $k$ bolas dentre as $w$ brancas e $n - k$ bolas dentre as $b$ pretas. Pelo principio multiplicativo, temos que o número de combinações possíveis é $\begin{pmatrix} w \\ k \end{pmatrix} \cdot \begin{pmatrix} b \\ n - k \end{pmatrix}$.

**Teorema: Simetria da Hípergeométrica**

As distribuições

$$
\begin{array}{r} X \sim \text{ HGeo}(w,b,n) \\ Y \sim \text{ HGeo}(n,w + b - n,w) \end{array}
$$

 são idênticas

**Demonstração**

Pela história da distribuição, $X$ é a quantidade de bolas brancas retiradas dentre $n$ bolas retiradas de uma urna com $w$ bolas brancas e $b$ bolas pretas. Se nós criarmos um conjunto de etiquetas, e colocarmos nas bolas, de forma que, se a bola **possui** uma etiqueta, então nós tiramos ela quando estávamos amostrando as bolas, então sabemos que de todas as $w + b$ bolas, $n$ tem a etiqueta e $w + b - n$ **não tem**. Com isso em mente, podemos afirmar que $Y$ representa a quantidade de formas possíveis de escolher $w$ e que essas $w$ bolas **tem a etiqueta**, ou seja, são as bolas que foram retiradas. Logo, a quantidade de bolas brancas retiradas é a mesma que a quantidade de bolas com etiqueta dentre as $w$ bolas brancas. Portanto, as distribuições são idênticas.

**Teorema**

Se $X \sim \text{ HGeo}(w,b,n)$, então

$$
\begin{array}{r} {\mathbb{E}}\lbrack X\rbrack = n\frac{w}{w + b} \\ {\mathbb{V}}\lbrack X\rbrack = n\frac{w}{w + b}\frac{b}{b + w}\frac{w + b - n}{w + b - 1} \end{array}
$$

**Demonstração**

Vamos numerar as bolas brancas de $1$ até $w$, e definir

$$
{\mathbb{I}}_{j} = \begin{cases} 1\quad\text{ bola branca }j\text{ foi retirada} \\ 0\quad\text{ bola branca }j\text{ não foi retirada } \end{cases}
$$

 definindo essa variável indicadora, podemos expressar a variável aleatória $X$ como

$$
X = {\mathbb{I}}_{1} + {\mathbb{I}}_{2} + \ldots + {\mathbb{I}}_{w}
$$

 vale ressaltar que $X$ **não é binomial**, pois as variáveis aleatórias ${\mathbb{I}}_{j}$ **não são independentes**. No entanto, podemos utilizar a linearidade da esperança para calcular a esperança de $X$:

$$
{\mathbb{E}}\lbrack X\rbrack = {\mathbb{E}}\left\lbrack \sum_{j = 1}^{w}{\mathbb{I}}_{j} \right\rbrack = \sum_{j = 1}^{w}{\mathbb{E}}\left\lbrack {\mathbb{I}}_{j} \right\rbrack = \sum_{j = 1}^{w}{\mathbb{P}}(I_{j} = 1)
$$

 como cada bola tem a mesma probabilidade de ser retirada, temos que

$$
{\mathbb{P}}(I_{j} = 1) = \frac{n}{w + b}
$$

 logo

$$
{\mathbb{E}}\lbrack X\rbrack = n\frac{w}{w + b}
$$

Para a variância, aplicamos ela em $X$, mas como ${\mathbb{I}}_{j}$ não são independentes, precisamos aplicar a correção com covariância conforme enunciado no [teorema da variância da soma de variáveis aleatórias](quantificadores-de-independencia.md#variance-of-generic-variables):

$$
\begin{aligned} {\mathbb{V}}\lbrack X\rbrack & = {\mathbb{V}}\left\lbrack \sum_{j = 1}^{w}{\mathbb{I}}_{j} \right\rbrack \\ & = \sum_{j = 1}^{w}{\mathbb{V}}\left\lbrack {\mathbb{I}}_{j} \right\rbrack + 2\sum_{i < j}\text{ Cov}\left( {\mathbb{I}}_{i},{\mathbb{I}}_{j} \right) \end{aligned}
$$

 como ${\mathbb{I}}_{j}$ é bernoulli, pelo [teorema da esperança e variância da Bernoulli](#mean-and-variance-of-bernoulli), temos que

$$
{\mathbb{V}}\left\lbrack {\mathbb{I}}_{j} \right\rbrack = \frac{n}{w + b}\left( 1 - \frac{n}{w + b} \right)
$$

 já para a covariância entre duas variáveis aleatórias ${\mathbb{I}}_{i}$ e ${\mathbb{I}}_{j}$, temos que

$$
\text{ Cov}\left( {\mathbb{I}}_{i},{\mathbb{I}}_{j} \right) = {\mathbb{E}}\left\lbrack {\mathbb{I}}_{i}{\mathbb{I}}_{j} \right\rbrack - {\mathbb{P}}({\mathbb{I}}_{i} = 1) \cdot {\mathbb{P}}({\mathbb{I}}_{j} = 1)
$$

 pela definição de ${\mathbb{I}}_{i}$ e ${\mathbb{I}}_{j}$, ${\mathbb{E}}\left\lbrack {\mathbb{I}}_{i}{\mathbb{I}}_{j} \right\rbrack = 1$ apenas quando ambos são $1$, logo

$$
{\mathbb{E}}\left\lbrack {\mathbb{I}}_{i}{\mathbb{I}}_{j} \right\rbrack = {\mathbb{P}}({\mathbb{I}}_{i} = 1,{\mathbb{I}}_{j} = 1)
$$

 Para que ambas as bolas apareçam na mesma amostragem, precisamos escolher $n - 2$ bolas dentre as $w + b - 2$ restantes, logo

$$
{\mathbb{P}}({\mathbb{I}}_{i} = 1,{\mathbb{I}}_{j} = 1) = \frac{\begin{pmatrix} w + b - 2 \\ n - 2 \end{pmatrix}}{\begin{pmatrix} w + b \\ n \end{pmatrix}} = \frac{n(n - 1)}{(w + b)(w + b - 1)}
$$

 logo

$$
\text{ Cov}\left( {\mathbb{I}}_{i},{\mathbb{I}}_{j} \right) = \frac{n(n - 1)}{(w + b)(w + b - 1)} - \frac{n^{2}}{(w + b)^{2}} = - \frac{n(w + b - n)}{(w + b)^{2}(w + b - 1)}
$$

 voltando para a variância de $X$, o termo abaixo

$$
\begin{aligned} 2 \cdot \sum_{i < j}\text{ Cov}\left( {\mathbb{I}}_{i},{\mathbb{I}}_{j} \right) & = 2\begin{pmatrix} w \\ 2 \end{pmatrix}\left( - \frac{n(w + b - n)}{(w + b)^{2}(w + b - 1)} \right) \\ & = - w(w - 1)n\frac{w + b - n}{(w + b)^{2}(w + b - 1)} \end{aligned}
$$

 somando tudo

$$
\begin{aligned} {\mathbb{V}}\lbrack X\rbrack & = n\frac{w}{w + b}\left( 1 - \frac{n}{w + b} \right) - w(w - 1)n\frac{w + b - n}{(w + b)^{2}(w + b - 1)} \\ & = n\frac{w}{w + b} - n^{2}\frac{w}{(w + b)^{2}} - w(w - 1)n\frac{w + b - n}{(w + b)^{2}(w + b - 1)} \\ & = \frac{wn(w + b - n)}{(w + b)^{2}}\left( 1 - \frac{w - 1}{w + b - 1} \right) \\ & = \frac{wn(w + b - n)}{(w + b)^{2}}\frac{b}{w + b - 1} \end{aligned}
$$

 reorganizando

$$
{\mathbb{V}}\lbrack X\rbrack = n\frac{w}{w + b}\frac{b}{b + w}\frac{w + b - n}{w + b - 1}
$$

<a id="secao-59"></a>

## Geométrica

Sempre que o seu problema puder ser associado com uma quantidade de tentativas até que um evento ocorra, você pode modelar o problema com uma distribuição geométrica. Ela é muito útil para modelar problemas de confiabilidade, como a quantidade de tentativas até que um equipamento falhe, ou a quantidade de tentativas até que um paciente se recupere.

**Definição: Distribuição Geométrica**

Suponha que tenhamos uma sequência de tentativas de Bernoulli independentes, cada uma com a mesma probabilidade $p$ de sucesso. Seja $X$ o número de tentativas **até o primeiro sucesso** (inclusivo, ou seja, a tentativa do sucesso em si entra na contagem), a distribuição de $X$ é chamada de *“geométrica”* com parâmetro $p$. Ela é denotada por

$$
X \sim \text{ Geom}(p)
$$

**Teorema: PMF da Geométrica**

Se $X \sim \text{ Geom}(p)$, então a função de massa de probabilidade de $X$ é dada por

$$
{\mathbb{P}}(X = k) = (1 - p)^{k - 1}p
$$

 para $k = 1,2,3,\ldots$.

**Demonstração**

Cada jogada que realizarmos terá a probabilidade $1 - p$ de falhar, logo, se queremos que o número de jogadas seja $k$, precisamos que as primeiras $k - 1$ jogadas falhem e a última jogada seja um sucesso. Pela regra do produto, temos que a probabilidade de isso acontecer é

$$
(1 - p)^{k - 1}p
$$

**Teorema**

Se $X \sim \text{ Geom}(p)$, então temos que

$$
\begin{array}{r} {\mathbb{E}}\lbrack X\rbrack = \frac{1}{p} \\ {\mathbb{V}}\lbrack X\rbrack = \frac{1 - p}{p^{2}} \end{array}
$$

**Demonstração**

Lembra que, pelo [teorema da esperança pela função de sobrevivência](esperanca.md#mean-survival-function), podemos escrever a esperança de $X$ como

$$
{\mathbb{E}}\lbrack X\rbrack = \sum_{k = 0}^{\infty}G_{X}(x)
$$

 onde $x$ é a função de sobrevivência de $X$. Para a distribuição geométrica, como ${\mathbb{P}}(X = k) = (1 - p)^{k - 1}p$, temos que, para que $X > k$, precisamos que as primeiras $k$ tentativas falhem, logo, a função de sobrevivência é

$$
G_{X}(k) = (1 - p)^{k}
$$

 escrevemos então

$$
{\mathbb{E}}\lbrack X\rbrack = \sum_{k = 0}^{\infty}(1 - p)^{k} = \frac{1}{p}
$$

 pois sabemos que

$$
\sum_{k = 0}^{\infty}x^{k} = \frac{1}{1 - x}
$$

 para $\vert x\vert  < 1$.

Para achar a variância, vamos utilizar a mesma ideia. Para tal, vamos utilizar da seguinte igualdade:

$$
n^{2} = \sum_{k = 0}^{n}(2k - 1)
$$

 Assim, podemos escrever $X^{2}$ como

$$
X^{2} = \sum_{k = 0}^{X}(2k - 1)
$$

 porém, para ficar com soma infinita, vamos inserir uma variável indicadora ${\mathbb{I}}(X \geq k)$ que é $1$ se $X \geq k$ e $0$ caso contrário. Assim, podemos escrever

$$
X^{2} = \sum_{k = 0}^{\infty}(2k - 1){\mathbb{I}}(X \geq k)
$$

 então tirando a esperança

$$
{\mathbb{E}}\left\lbrack X^{2} \right\rbrack = \sum_{k = 0}^{\infty}(2k - 1){\mathbb{P}}(X \geq k) = \sum_{k = 0}^{\infty}(2k - 1)(1 - p)^{k}
$$

 podemos separar a soma em duas partes

$$
{\mathbb{E}}\left\lbrack X^{2} \right\rbrack = 2 \cdot \sum_{k = 0}^{\infty}k(1 - p)^{k - 1} - \sum_{k = 0}^{\infty}(1 - p)^{k - 1}
$$

 a segunda sabemos para onde converge, a primeira nem tanto. No entanto, como enunciado antes, sabemos que

$$
\sum_{k = 0}^{\infty}x^{k} = \frac{1}{1 - x}
$$

 vamos tirar a derivada em ambos os lados

$$
\sum_{k = 0}^{\infty}kx^{k - 1} = \frac{1}{(1 - x)^{2}}
$$

 logo, sabemos que

$$
{\mathbb{E}}\left\lbrack X^{2} \right\rbrack = \frac{2}{\left( 1 - (1 - p) \right)^{2}} - \frac{1}{1 - (1 - p)} = \frac{2}{p^{2}} - \frac{1}{p} = \frac{2 - p}{p^{2}}
$$

 voltando para a fórmula da variância

$$
{\mathbb{V}}\lbrack X\rbrack = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2} = \frac{2 - p}{p^{2}} - \frac{1}{p^{2}} = \frac{1 - p}{p^{2}}
$$

<a id="secao-60"></a>

## Binomial Negativa

Muito parecida com a geométrica, no entanto, é quando o problema pode ser modelado como a quantidade de tentativas até que múltiplos eventos ocorram. Por exemplo, a quantidade de tentativas até que um paciente se recupere **duas vezes**, ou a quantidade de tentativas até que um equipamento falhe **três vezes**.

**Definição: Distribuição Binomial Negativa**

Suponha um experimento onde eu vou realizar tentativas de Bernoulli independentes até obter $r$ **sucessos** e cada tentativa tem a mesma probabilidade $p$ de sucesso. Seja $X$ a quantidade de tentativas necessárias para obter $r$ sucessos (onde o último sucesso entra na contagem), dizemos que $X$ tem distribuição **binomial negativa** com parâmetros $r$ e $p$, denotada por

$$
X \sim \text{ NegBin}(r,p)
$$

**Teorema: PMF da Binomial Negativa**

Se $X \sim \text{ NegBin}(r,p)$, então a função de massa de probabilidade de $X$ é dada por

$$
{\mathbb{P}}(X = k) = \begin{pmatrix} k - 1 \\ r - 1 \end{pmatrix}p^{r}(1 - p)^{k - r}
$$

 para $k = r,r + 1,r + 2,\ldots$.

**Demonstração**

Seja $Y$ o número de sucesso nas primeiras $k - 1$ tentativas e $Z$ o número de sucessos que ocorreram na $k$-ésima tentativa ($Z \in \left\{ 0,1 \right\}$). O $r$-ésimo sucesso acontece no $k$-ésimo lançamento se, e somente se, $Y = r - 1$ e $Z = 1$, isto é

$$
X = k \Leftrightarrow Y = r - 1,Z = 1
$$

 Como $Y$ e $Z$ são independentes, temos que

$$
{\mathbb{P}}(X = k) = {\mathbb{P}}(Y = r - 1,Z = 1) = {\mathbb{P}}(Y = r - 1) \cdot {\mathbb{P}}(Z = 1)
$$

 como $Y$ é binomial com parâmetros $k - 1$ e $p$ e $Z$ é bernoulli com parâmetro $p$, temos que

$$
{\mathbb{P}}(X = k) = \begin{pmatrix} k - 1 \\ r - 1 \end{pmatrix}p^{r - 1}(1 - p)^{(k - 1) - (r - 1)} \cdot p = \begin{pmatrix} k - 1 \\ r - 1 \end{pmatrix}p^{r}(1 - p)^{k - r}
$$

**Teorema**

Se $X \sim \text{ NegBin}(r,p)$, então temos que

$$
\begin{array}{r} {\mathbb{E}}\lbrack X\rbrack = \frac{r}{p} \\ {\mathbb{V}}\lbrack X\rbrack = r\frac{1 - p}{p^{2}} \end{array}
$$

**Demonstração**

Assim como a binomial, podemos subdividir essa variável aleatória em $r$ variáveis com outra distribuição. Se eu estou procurando $r$ sucessos, eu posso dividir como a quantidade de jogadas até o primeiro, depois até o segundo etc. E isso é exatamente a distribuição geométrica. Ou seja, podemos expressar $X$ como

$$
X = Y_{1} + Y_{2} + \ldots + Y_{r}
$$

 com $Y_{j} \sim \text{ Geom}(p)$

Dessa forma, aplicando a linearidade da esperança, temos que

$$
{\mathbb{E}}\lbrack X\rbrack = {\mathbb{E}}\left\lbrack \sum_{j = 1}^{r}Y_{j} \right\rbrack = \sum_{j = 1}^{r}{\mathbb{E}}\left\lbrack Y_{j} \right\rbrack = \sum_{j = 1}^{r}\frac{1}{p} = \frac{r}{p}
$$

 aplicando a mesma coisa com a variância

$$
{\mathbb{V}}\lbrack X\rbrack = {\mathbb{V}}\left\lbrack \sum_{j = 1}^{r}Y_{j} \right\rbrack = \sum_{j = 1}^{r}{\mathbb{V}}\left\lbrack Y_{j} \right\rbrack = \sum_{j = 1}^{r}\frac{1 - p}{p^{2}} = r\frac{1 - p}{p^{2}}
$$

<a id="secao-61"></a>

## Poison

Essa é um pouco mais complexa. A poisson representa a quantidade de vezes que um evento ocorre em um intervalo de tempo fixo, mas sabendo quantas vezes ele ocorre em média. Por exemplo, fixando uma janela de $6$ segundos, sabemos que em uma avenida passam em média $10$ carros, mas não sabemos quantos carros vão passar em cada janela de $6$ segundos, podem ser $10$, $100$ num dia de pico, ou até mais se acontecer algo inesperado, então não há limite para a quantidade real de contagem. Outro exemplo é, dentro de um intervalo fixo, quantas gotas de chuva vão cair em um lago? É literalmente impossível você **limitar** a quantidade de gotas, então a distribuição de poisson é perfeita para modelar esse tipo de problema.

**Definição: Distribuição de Poisson**

Seja $\lambda$ a **média** da quantidade de eventos que ocorrem em um intervalo de tempo fixo e $X$ é a variável aleatória que representa quantas vezes o evento ocorreu nesse mesmo intervalo de tempo, então dizemos que $X$ segue uma distribuição de Poisson com parâmetro $\lambda$, denotada por

$$
X \sim \text{ Poisson}(\lambda)
$$

**Teorema: PMF da Poisson**

Se $X \sim \text{ Poisson}(\lambda)$, então a função de massa de probabilidade de $X$ é dada por

$$
{\mathbb{P}}(X = k) = \frac{\lambda^{k}e^{- \lambda}}{k!}
$$

 para $k = 0,1,2,\ldots$.

**Demonstração**

Estamos avaliando a ocorrência de um evento dentro de um intervalo de tempo fixo. Isso significa que eu posso realizar esse evento uma quantidade $n$ de vezes, no entanto, como o intervalo de tempo não é finito, podemos assumir que $n$ pode ser extendido ao infinito (pois eu não consigo afirmar quantas tentativas podem acontecer dentro do intervalo de tempo. Uma milisegundo? Uma hora? Uma semana? $1000$ por milisegundo?). Então nós vamos pegar a distribuição binomial e vamos estender ela ao infinito. Sabemos que

$$
\begin{aligned} {\mathbb{P}}(X = x) & = \frac{n!}{(n - x)!x!}\left( p^{x} \right)(1 - p)^{n - x} \\ & = \frac{n!}{(n - x)!x!} \cdot p^{x} \cdot \frac{n^{x}}{n^{x}}\left( 1\frac{- (np)}{n} \right)^{n - x} \\ & = \frac{(np)^{x}}{x!} \cdot \frac{n!}{(n - x)!n^{x}}\left( 1\frac{- (np)}{n} \right)^{n}\left( 1\frac{- (np)}{n} \right)^{- x} \end{aligned}
$$

 tendendo $n$ ao infinito, temos que

$$
\begin{aligned} \lim\limits_{n \rightarrow \infty}{\mathbb{P}}(X = x) & = \lim\limits_{n \rightarrow \infty}\frac{(np)^{x}}{x!} \cdot \underset{\text{ I}}{\underbrace{\frac{n!}{(n - x)!n^{x}}}}\underset{\text{ II}}{\underbrace{\left( 1\frac{- (np)}{n} \right)^{n}}}\underset{\text{ III}}{\underbrace{\left( 1\frac{- (np)}{n} \right)^{- x}}} \end{aligned}
$$

 pelo teorema da multiplicação de limites, podemos separar o limite em três partes. Vamos analisar cada uma separadamente.

**I**:

$$
\begin{aligned} \lim\limits_{n \rightarrow \infty}\frac{n!}{(n - x)!n^{x}} & = \lim\limits_{n \rightarrow \infty}\frac{n(n - 1)(n - 2)\ldots(n - x + 1)}{n^{x}} \\ & = \lim\limits_{n \rightarrow \infty}\left( 1 - \frac{1}{n} \right)\left( 1 - \frac{2}{n} \right)\ldots\left( 1 - \frac{x - 1}{n} \right) \\ & = 1 \end{aligned}
$$

**II**:

$$
\lim\limits_{n \rightarrow \infty}\left( 1\frac{- (np)}{n} \right)^{n}
$$

 queremos fixar ${\mathbb{E}}\lbrack X\rbrack = np = \lambda$ como fixo

$$
\lim\limits_{n \rightarrow \infty}\left( 1\frac{- (np)}{n} \right)^{n} = \lim\limits_{n \rightarrow \infty}\left( 1 - \frac{\lambda}{n} \right)^{n} = e^{- \lambda}
$$

**III**:

$$
\lim\limits_{n \rightarrow \infty}\left( 1\frac{- (np)}{n} \right)^{- x} = \lim\limits_{n \rightarrow \infty}\left( 1 - \frac{\lambda}{n} \right)^{- x} = 1
$$

logo, voltando para a fórmula original, temos que

$$
\lim\limits_{n \rightarrow \infty}{\mathbb{P}}(X = x) = \lambda^{x}\frac{e^{- \lambda}}{x!}
$$

**Teorema**

Se $X \sim \text{ Poisson}(\lambda)$, então temos que

$$
\begin{array}{r} {\mathbb{E}}\lbrack X\rbrack = \lambda \\ {\mathbb{V}}\lbrack X\rbrack = \lambda \end{array}
$$

**Demonstração**

$$
\begin{aligned} {\mathbb{E}}\lbrack X\rbrack & = \sum_{k = 0}^{\infty}ke^{- \lambda}\frac{\lambda^{k}}{k!} \\ & = e^{- \lambda}\sum_{k = 0}^{\infty}\frac{\lambda^{k}}{(k - 1)!} \end{aligned}
$$

 sabemos pela definição de $e^{x}$ que

$$
e^{x} = \sum_{k = 0}^{\infty}\frac{x^{k}}{k!}
$$

 e tirando a derivada, que

$$
e^{x} = \sum_{k = 0}^{\infty}k\frac{x^{k - 1}}{k!}
$$

 note que ao multiplicarmos por $\lambda$, temos

$$
\lambda e^{\lambda} = \sum_{k = 0}^{\infty}k\frac{\lambda^{k}}{k!}
$$

 logo

$$
{\mathbb{E}}\lbrack X\rbrack = e^{- \lambda}\lambda e^{\lambda} = \lambda
$$

Já para a variância, podemos utilizar o mesmo truque

$$
{\mathbb{V}}\lbrack X\rbrack = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2}
$$

 analisando ${\mathbb{E}}\left\lbrack X^{2} \right\rbrack$

$$
\begin{aligned} {\mathbb{E}}\left\lbrack X^{2} \right\rbrack & = \sum_{k = 0}^{\infty}k^{2}e^{- \lambda}\frac{\lambda^{k}}{k!} \end{aligned}
$$

 vimos a derivada da função $e^{x}$ e podemos tirar a segunda derivada, que é

$$
e^{x} = \sum_{k = 0}^{\infty}k(k - 1)\frac{x^{k - 2}}{k!}
$$

 ou seja, temos que

$$
\lambda^{2}e^{\lambda} = \sum_{k = 0}^{\infty}k(k - 1)\frac{\lambda^{k}}{k!}
$$

 logo

$$
{\mathbb{E}}\left\lbrack X^{2} \right\rbrack = e^{- \lambda}\left( \lambda^{2}e^{\lambda} + \lambda e^{\lambda} \right) = \lambda^{2} + \lambda
$$

 então

$$
{\mathbb{V}}\lbrack X\rbrack = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack - \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2} = \lambda^{2} + \lambda - \lambda^{2} = \lambda
$$
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Quantificadores de Independência](quantificadores-de-independencia.md)
