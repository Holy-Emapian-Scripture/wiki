---
layout: "default"
title: "Propriedades da CDF e PDF — Variáveis Aleatórias Contínuas"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 3
---

[Probabilidade](../../index.md) · [Variáveis Aleatórias Contínuas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao_propriedades_CDF_PDF"></a>

# Propriedades da CDF e PDF

Dada uma v.a contínua $X$ com PDF $f_{X}$ e CDF $F_{X}$, é intuitivo que com $\varphi \rightarrow \infty$, $P(X \leq \varphi) = F_{X}(\varphi) \rightarrow 1$, e analogamente com $\varphi \rightarrow - \infty$, $P(X \leq \varphi) = F_{X}(\varphi) \rightarrow 0$. Então enunciamos as seguintes propriedades:

**Propriedade**

$$\begin{array}{r} \lim\limits_{\varphi \rightarrow \infty}F_{X}(\varphi) = 1 \\ \lim\limits_{\varphi \rightarrow - \infty}F_{X}(\varphi) = 0 \end{array}$$

Logo, $F_{X}(\varphi)$ é uma função crescente, e $F_{X}(\varphi) \in \lbrack 0,1\rbrack$.

<a id="propriedade_cdf_crescente"></a>

**Propriedade**

$$\begin{array}{r} F_{X}(\varphi) = \int_{- \infty}^{\varphi}f_{X}(\psi)d\psi \\ \int_{- \infty}^{\infty}f_{X}(\psi)d\psi = 1 \end{array}$$

<a id="propriedade_pdf_integra_1"></a>

**Propriedade**

Seja $X$ uma v.a contínua com PDF $f_{X}$ e CDF $F_{X}$, tome $h:{\mathbb{R}} \rightarrow {\mathbb{R}}$ crescente e $Y = g(X)$ com PDF e CDF $f_{Y},F_{Y}$, respectivamente. Então:

$$f_{Y}(y) = \frac{f_{X}(\varphi)}{h'(\varphi)}$$

Com $\varphi = h^{- 1}(y)$

Caso $h$ seja decrescente:

$$f_{Y}(y) = - \frac{f_{X}(\varphi)}{h'(\varphi)}$$

Caso seja injetiva (pode ser crescente e decrescente em lugares diferentes):

$$f_{Y}(y) = \frac{f_{X}(\varphi)}{\left\vert  {h'(\varphi)} \right\vert }$$

Caso seja uma função fudida quem nem injetiva é, mas pelo menos derivável, defina $\forall y \in \text{ Im}(h)$:

$$I_{y} = \left\{ x \in {\mathbb{R}}~\vert ~h(x) = y \right\}$$

Contendo um número finito de elementos $x_{1}(y),\ldots,x_{k(y)}(y)$. Então a densidade de $Y$ é dada por:

$$f_{Y}(y) = \sum_{i = 1}^{k(y)}\frac{f_{X}\left( x_{i}(y) \right)}{\left\vert  {h'\left( x_{i}(y) \right)} \right\vert }$$

<a id="propriedade_derivada_inversa"></a>

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [Definições](../definicoes/index.md)
- Próximo: [LOTUS (Law of The Unconscious Statistician)](../lotus-law-of-the-unconscious-statistician/index.md)
