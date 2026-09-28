---
layout: "default"
title: "Variáveis Aleatórias Contínuas"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 1
---

[Probabilidade](index.md)

<!-- wiki:original:inicio -->

<a id="secao-1"></a>

# Variáveis Aleatórias Contínuas


<a id="definicoes"></a>
<a id="secao-2"></a>

## Definições

Definimos aqui o necessário sobre variáveis aleatórias contínuas para a compreensão dos conteúdos do teste:

<a id="definiticao_variavel_aleatoria_continua"></a>

**Definição**

(V.A Contínua)  
Uma v.a $X:\Omega \rightarrow {\mathbb{R}}$ é dita contínua se e somente se sua CDF $F_{X}$ for derivável

<a id="definicao_CDF"></a>

**Definição**

(Função de Distribuição - CDF)  
A função de distribuição de uma v.a contínua $X$ é dada por: $$F_{X}(\varphi) = P(X \leq \varphi)$$

**Definição**

(Função de Densidade - PDF)  
Calculamos a densidade de probabilidade calculando a probabilidade de $X$ estar num intervalo, e dividimos pelo tamanho do intervalo:

$$
\frac{P\left( X \in I = \lbrack\psi,\psi + \varepsilon\rbrack \right)}{\left\| I \right\| = \varepsilon} = \frac{P(\psi \leq X \leq \psi + \varepsilon)}{\varepsilon} = \frac{F_{X}(\psi + \varepsilon) - F_{X}(\psi)}{\varepsilon}
$$

Tomando o limite quando $\varepsilon \rightarrow 0$, obtemos a *função de densidade de probabilidade* PDF no ponto $\psi$:

$$
\lim\limits_{\varepsilon \rightarrow 0}\frac{F_{X}(\psi + \varepsilon) - F_{X}(\psi)}{\varepsilon} = F'_{X}(\psi) = f_{X}(\psi)
$$

É importante notar que a PDF não é uma probabilidade, mas sim uma densidade de probabilidade. Veja:

$$
P(X \in I) = P(a \leq X \leq b) = F_{X}(b) - F_{X}(a)
$$

Usamos a PDF e o teorema fundamental do cálculo para calcular a probabilidade de $X$ estar em um intervalo $I = \lbrack a,b\rbrack$:

$$
P(X \in I) = F_{X}(b) - F_{X}(a) = \int_{a}^{b}f_{X}(\varphi)d\varphi
$$

Logo a **a integral definida** da PDF é de fato uma probabilidade.

<a id="definicao_PDF"></a>

<a id="secao_propriedades_CDF_PDF"></a>

## Propriedades da CDF e PDF

Dada uma v.a contínua $X$ com PDF $f_{X}$ e CDF $F_{X}$, é intuitivo que com $\varphi \rightarrow \infty$, $P(X \leq \varphi) = F_{X}(\varphi) \rightarrow 1$, e analogamente com $\varphi \rightarrow - \infty$, $P(X \leq \varphi) = F_{X}(\varphi) \rightarrow 0$. Então enunciamos as seguintes propriedades:

**Propriedade**

$$
\begin{array}{r} \lim\limits_{\varphi \rightarrow \infty}F_{X}(\varphi) = 1 \\ \lim\limits_{\varphi \rightarrow - \infty}F_{X}(\varphi) = 0 \end{array}
$$

Logo, $F_{X}(\varphi)$ é uma função crescente, e $F_{X}(\varphi) \in \lbrack 0,1\rbrack$.

<a id="propriedade_cdf_crescente"></a>

**Propriedade**

$$
\begin{array}{r} F_{X}(\varphi) = \int_{- \infty}^{\varphi}f_{X}(\psi)d\psi \\ \int_{- \infty}^{\infty}f_{X}(\psi)d\psi = 1 \end{array}
$$

<a id="propriedade_pdf_integra_1"></a>

**Propriedade**

Seja $X$ uma v.a contínua com PDF $f_{X}$ e CDF $F_{X}$, tome $h:{\mathbb{R}} \rightarrow {\mathbb{R}}$ crescente e $Y = g(X)$ com PDF e CDF $f_{Y},F_{Y}$, respectivamente. Então:

$$
f_{Y}(y) = \frac{f_{X}(\varphi)}{h'(\varphi)}
$$

Com $\varphi = h^{- 1}(y)$

Caso $h$ seja decrescente:

$$
f_{Y}(y) = - \frac{f_{X}(\varphi)}{h'(\varphi)}
$$

Caso seja injetiva (pode ser crescente e decrescente em lugares diferentes):

$$
f_{Y}(y) = \frac{f_{X}(\varphi)}{\left\vert  {h'(\varphi)} \right\vert }
$$

Caso seja uma função fudida quem nem injetiva é, mas pelo menos derivável, defina $\forall y \in \text{ Im}(h)$:

$$
I_{y} = \left\{ x \in {\mathbb{R}}~\vert ~h(x) = y \right\}
$$

Contendo um número finito de elementos $x_{1}(y),\ldots,x_{k(y)}(y)$. Então a densidade de $Y$ é dada por:

$$
f_{Y}(y) = \sum_{i = 1}^{k(y)}\frac{f_{X}\left( x_{i}(y) \right)}{\left\vert  {h'\left( x_{i}(y) \right)} \right\vert }
$$

<a id="propriedade_derivada_inversa"></a>

<a id="secao_lotus"></a>

## LOTUS (Law of The Unconscious Statistician)

Se $X$ é uma v.a contínua com PDF $f_{X}(\varphi)$ e $g:{\mathbb{R}} \rightarrow {\mathbb{R}}$ é contínua, então a esperança de $Y = g(X)$ é dada por:

$$
E\left( g(X) \right) = \int_{- \infty}^{\infty}g(\varphi)f_{X}(\varphi)d\varphi
$$

<a id="variancia-e-esperanca"></a>
<a id="secao-5"></a>

## Variância e Esperança

<a id="definicao_esperanca"></a>

**Definição**

(Esperança)  
Dada uma v.a contínua $X$ com PDF $f_{X}(\varphi)$, a esperança de $X$ é dada por:

$$
E(X) = \int_{- \infty}^{\infty}\varphi f_{X}(\varphi)d\varphi
$$

**Definição**

(Variância, Desvio-Padrão)  
A variância de uma v.a contínua $X$ com PDF $f_{X}(\varphi)$ e esperança $\mu = E(X)$ é dada por:

$$
V(X) = E\lbrack(X - {E(X)}^{2}\rbrack = \int_{- \infty}^{\infty}\lbrack\varphi - \mu\rbrack^{2}f_{X}(\varphi)d\varphi
$$

O desvio padrão é:

$$
\sigma(X) = \sqrt{V(X)}
$$

<a id="definicao_variancia_desviopadrao"></a>

<a id="propriedades-da-esperanca-e-variancia"></a>
<a id="secao_propriedades_esperanca_variancia"></a>

## Propriedades da Esperança e Variância

Dadas v.a’s contínuas $X,Y$ com PDF $f_{X}(\varphi),f_{Y}(\varphi)$ e $a,b \in {\mathbb{R}}$, temos:

<a id="propriedade_esperanca_variancia"></a>

**Propriedade**

$$
\begin{array}{r} E(aX + b) = aE(X) + b \\ E(X + Y) = E(X) + E(Y) \\ V(aX + b) = a^{2}V(X) \end{array}
$$

E caso $X,Y$ sejam independentes:

$$
\begin{array}{r} E(XY) = E(X)E(Y) \\ V(X + Y) = V(X) + V(Y) \end{array}
$$

**Propriedade**

Podemos calcular a variância de $X$ usando a esperança:

$$
V(X) = E\left( X^{2} \right) - {E(X)}^{2}
$$

<a id="propriedade_varianca_via_esperanca"></a>

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../trilhas/probabilidade/a2.md#apresentacao-original)

- Próximo: [Distribuições Contínuas](distribuicoes-continuas.md)
