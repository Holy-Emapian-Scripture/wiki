---
layout: "default"
title: "Variáveis Aleatórias Contínuas Bidimensionais"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 13
---

[Probabilidade](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-24"></a>

# Variáveis Aleatórias Contínuas Bidimensionais


<a id="covariancia-e-correlacao"></a>
<a id="secao_covariancia_correlacao"></a>

## Covariância e Correlação

A Covariância e correlação são **análogas** ao caso discreto:

**Definição**

(Covariância)  
A covariância de $X$ e $Y$ é dada por:

$$
\text{ Cov}(X,Y) = E(XY) - E(X)E(Y)
$$

<a id="definicao_covariancia"></a>

**Definição**

(Correlação)  
A correlação de $X$ e $Y$ é dada por:

$$
\rho(X,Y) = \frac{\text{ Cov}(X,Y)}{\sigma(X)\sigma(Y)}
$$

<a id="definicao_correlacao"></a>

<a id="distribuicoes-marginais-e-condicionais"></a>
<a id="secao_distr_marginais_condicionais"></a>

## Distribuições Marginais e Condicionais

Lembrando o caso discreto, dadas $X,Y$ v.a’s discretas com densidade conjunta $p(x,y) = P(X = x \cap Y = y)$, temos os conceitos e covariância e correlação:

$$
\begin{array}{r} \text{ Cov}(X,Y) = E(XY) - E(X)E(Y) \\ \rho(X,Y) = \frac{\text{ Cov}(X,Y)}{\sigma(X)\sigma(Y)} \end{array}
$$

Também temos as distribuições marginais e condicionais (Pelo teorema de Bayes e a Lei da Probabilidade Total):

$$
\begin{array}{r} p_{X}(x) = P(X = x) = \sum_{y}p(x,y) \\ p_{Y}(y) = P(Y = y) = \sum_{x}p(x,y) \\ p_{X\vert Y}\left( x\vert y \right) = P\left( X = x~\vert ~Y = y \right) = \frac{p(x,y)}{p_{Y}(y)} \end{array}
$$

Com $f(x,y)$ sendo uma densidade conjunta, a diferença agora é a transição de $\sum \rightarrow \int$:

**Definição**

(Distribuição Marginal)  
A distribuição marginal de $X$ é dada por:

$$
f_{X}(x) = \int_{- \infty}^{\infty}f(x,y)dy
$$

<a id="definicao_distr_marginal"></a>

**Definição**

(Distribuição Condicional)  
A distribuição condicional de $X$ dado $Y$ é dada por:

$$
f_{X\vert Y}\left( x\vert y \right) = \frac{f(x,y)}{f_{Y}(y)}
$$

<a id="definicao_distr_condicional"></a>

<a id="esperanca-condicional"></a>
<a id="secao-30"></a>

## Esperança Condicional

Isso é bem útil:

**Definição**

A esperança condicional de $X$ na certeza de $Y = y$ é:

$$
E\left( X~\vert ~Y = y \right) = \int_{- \infty}^{\infty}xf_{X\vert Y}\left( x\vert y \right)dx
$$

(As vezes denotado por $E\left\lbrack X\vert y \right\rbrack$).

Os teoremas da gênesis também são úteis:

**Teorema**

(Lei de Adão)  
$\forall$ v.a’s $X,Y$ temos:

$$
E\left( E\left( X\vert Y \right) \right) = E(X)
$$

**Demonstração**

Trivial

**Teorema**

(Lei de Eva)  
$\forall$ v.a’s $X,Y$, temos:

$$
V(Y) = E\left( V\left( Y\vert X \right) \right) + V\left( E\left( Y\vert X \right) \right)
$$

**Demonstração**

Trivial

<a id="funcao-de-densidade-conjunta"></a>
<a id="secao_fdc"></a>

## Função de Densidade Conjunta

**Definição**

(Função de Densidade Conjunta)  
Uma função de densidade conjunta $f(x,y)$ das variáveis $X$ e $Y$ é uma função com a seguinte propriedade:

$$
P\left( (X,Y) \in R \right) = \iint_{R}f(x,y)dA
$$

Onde $R \subset {\mathbb{R}}^{2}$. Por conseguinte, $f$ deve satisfazer:

$$
\begin{array}{r} f(x,y) \geq 0,\forall(x,y) \in {\mathbb{R}}^{2} \\ \int_{- \infty}^{\infty}\int_{- \infty}^{\infty}f(x,y)dxdy = 1 \end{array}
$$

<a id="definicao_conjunta"></a>

<a id="secao-26"></a>

### Esperança, Variância e Desvio-Padrão

**Definição**

(Esperança)  
Dadas $X,Y$ com densidade conjunta $f(x,y)$, a esperança de $X$ é:

$$
E(X) = \iint_{{\mathbb{R}}^{2}}xf(x,y)dA
$$

<a id="definicao_esperanca_conjunta"></a>

**Definição**

(Variância, Desvio-Padrão)  
A variância de $X$ é análoga ao caso anterior:

$$
V(X) = E\left( X^{2} \right) - {E(X)}^{2}
$$

O desvio padrão é:

$$
\sigma(X) = \sqrt{V(X)}
$$

<a id="definicao_variancia_desviopadrao_conjunta"></a>

<a id="secao-27"></a>

### LOTUS 2

Dadas $X,Y$ com densidade conjunta $f(x,y)$, o valor esperado de uma função qualquer $g(X,Y)$ é:

$$E\left( g(X,Y) \right) = \iint_{{\mathbb{R}}^{2}}g(x,y)f(x,y)dA$$ <a id="lotus2"></a>

Quando a densidade conjunta é constante em $S \subset {\mathbb{R}}^{2}$ e $0$ fora de $S$, dizemos que $f(x,y)$ é uma função de densidade uniforme em $S$:

$$
f(x,y) = \begin{cases} 0\text{, }\text{ se }(x,y) \notin S \\ \frac{1}{\text{Área}(S)}\text{, }\text{ se }(x,y) \in S \end{cases}
$$

<a id="independencia"></a>
<a id="secao-31"></a>

## Independência

As v.a’s contínuas $X$ e $Y$ são ditas **independentes** se e somente se a densidade conjunta $f(x,y)$ for o produto das marginais:

$$
f(x,y) = f_{X}(x)f_{Y}(y)
$$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [Taxa de Falhas](../distribuicoes-continuas/index.md#taxa-de-falhas)
- Próximo: [Distribuições Marginais e Condicionais](#distribuicoes-marginais-e-condicionais)
