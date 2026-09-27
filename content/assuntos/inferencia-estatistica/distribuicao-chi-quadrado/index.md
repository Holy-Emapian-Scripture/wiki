---
layout: "default"
title: "Distribuição Chi-Quadrado"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 2
---

[Inferência Estatística](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-2"></a>

# Distribuição Chi-Quadrado


<a id="propriedades"></a>
<a id="secao-3"></a>

## Propriedades

**Teorema**

Se $X \sim Χ_{m}^{2}$ então: $${\mathbb{E}}\lbrack X\rbrack = m\text{\quad\quad}{\mathbb{V}}\lbrack X\rbrack = 2m$$

**Demonstração**

A esperança de uma Gamma$(\alpha,\beta)$ é $\frac{\alpha}{\beta}$, logo: $${\mathbb{E}}\lbrack X\rbrack = \frac{\frac{m}{2}}{\frac{1}{2}} = m$$ E a variância é $\frac{\alpha}{\beta^{2}}$, logo: $${\mathbb{V}}\lbrack X\rbrack = \frac{\frac{m}{2}}{\frac{1}{4}} = 2m$$

**Teorema**

A função geradora de momentos de uma $Χ_{m}^{2}$ é dada por $$\psi(t) = \left( \frac{1}{1 - 2t} \right)^{m/2}\text{\quad\quad}\left( t < \frac{1}{2} \right)$$

<a id="sum-of-independent-chi-squares"></a>

**Teorema**

Se $X_{1},\ldots,X_{k}$ são iid e $X_{i} \sim {Χ_{m}^{2}}_{i}$, então $Y = \sum_{j = 1}^{k}X_{j} \sim Χ_{\sum_{j = 1}^{k}m_{j}}^{2}$

**Demonstração**

Sabemos que, dado a FGM de $X$ ($\psi_{X}$) e de $Y$ ($\psi_{Y}$) onde $X$ e $Y$ são iid, então a FGM de $X + Y$ é $\psi_{X}\psi_{Y}$. Sabendo disso, calculamos a FGM de $X_{1} + \ldots + X_{k}$: $$\begin{aligned} \psi_{Y}(t) & = \prod_{j = 1}^{k}\left( \frac{1}{1 - 2t} \right)^{m_{j}/2}\text{\quad\quad}\left( t < \frac{1}{2} \right) \\ & = \left( \frac{1}{1 - 2t} \right)^{\frac{1}{2}\sum_{j = 1}^{k}m_{j}}\text{\quad\quad}\left( t < \frac{1}{2} \right) \end{aligned}$$

**Teorema**

Se $X \sim N(0,1)$, então $Y = X^{2} \sim Χ_{1}^{2}$

**Demonstração**

Sabemos que se $X$ tem pdf $f_{X}(x)$ e $Z = h(X)$, então a pdf de $Z$ é $$f_{Z}(z) = \frac{f_{X}(x)}{\vert h'(x)\vert }$$ Então, considerando $h(x) = x^{2}$ e $f_{X}(x) = \frac{1}{\sqrt{2\pi}}e^{- \frac{x^{2}}{2}}$, temos que $$f_{Z}(z) = \frac{\frac{1}{\sqrt{2\pi}}e^{- \frac{x^{2}}{2}}}{2x} = \frac{1}{2\sqrt{\pi z}}e^{- \frac{1}{2}z}$$ Perceba que isso é a densidade de uma $Χ_{1}^{2}$, veja: $$\frac{\left( \frac{1}{2} \right)^{\frac{1}{2}}}{\Gamma(\frac{1}{2})}z^{\frac{1}{2} - 1}e^{- \frac{1}{2}z} = \frac{\frac{1}{\sqrt{2}}}{\sqrt{\pi}}\frac{1}{\sqrt{z}}e^{- \frac{1}{2}z} = \frac{1}{\sqrt{2\pi z}}e^{- \frac{1}{2}z}$$ Logo, $Z \sim Χ_{1}^{2}$. A função $f_{Z}(z)$ possui um termo $\frac{1}{2}$ pois preciamos lembrar que a normal vai de $\lbrack - \infty,\infty\rbrack$, então para que $h(x)$ seja monótona, precisamos restringir em $\lbrack - \infty,0\rbrack$ e $\lbrack 0,\infty\rbrack$ então obtemos duas funções que integram $\frac{1}{2}$ em cada intervalo, logo o resultado integra $1$

**Corolário**

Se $X_{1},\ldots,X_{n} \sim N(0,1)$, então: $$X_{1}^{2} + \ldots + X_{n}^{2} \sim Χ_{m}^{2}$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Distribuição Amostral de Estimadores](../distribuicao-amostral-de-estimadores/index.md)
- Próximo: [Distribuição Conjunta da Média e Variância Amostral](../distribuicao-conjunta-da-media-e-variancia-amostral/index.md)
