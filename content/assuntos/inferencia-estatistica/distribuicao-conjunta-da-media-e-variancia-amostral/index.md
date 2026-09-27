---
layout: "default"
title: "Distribuição Conjunta da Média e Variância Amostral"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 4
---

[Inferência Estatística](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-4"></a>

# Distribuição Conjunta da Média e Variância Amostral


<a id="independencia-da-media-e-variancia-amostrais"></a>
<a id="secao-5"></a>

## Independência da Média e Variância Amostrais

<a id="normals-orthogonal-transformation"></a>

**Teorema**

Suponha que as variáveis $X_{1},\ldots,X_{n}$ são iid, onde $X_{j} \sim N(0,1)$. Seja $Q$ uma matriz ortogonal $n \times n$ e $\underline{Y} = Q\underline{X}$ onde $\underline{X} = \left( X_{1},\ldots,X_{n} \right)^{T}$, então $Y_{j} \sim N(0,1)$ e $Y_{1},\ldots,Y_{n}$ são iid, além de que $\sum X_{i}^{2} = \sum Y_{i}^{2}$

**Demonstração**

A distribuição conjunta de $X_{1},\ldots,X_{n}$ é dada por: $$f_{X}\left( \underline{x} \right) = \frac{1}{(2\pi)^{\frac{n}{2}}}\exp\left\{ - \frac{1}{2}\sum_{i = 1}^{n}x_{i}^{2} \right\}$$ Sabemos que, se $Z = h(Y)$ com $h$ monótona, então $$f_{Z}(z) = \frac{f_{Y}(y)}{\vert h'(y)\vert }$$ Se considerarmos $h(x) = Qx$, então $\underline{Y} = h\left( \underline{X} \right)$, logo: $$f_{Y}(y) = \frac{f_{X}\left( Q^{T}y \right)}{\vert \det(Q)\vert }$$ Porém, $\det(Q) = 1$ pois $Q$ é ortogonal. Além disso, sabemos que $\| x\|^{2} = \| Qx\|^{2}$, então: $$f_{Y}(y) = \frac{1}{(2\pi)^{\frac{n}{2}}}\exp\left\{ - \frac{1}{2}\sum_{i = 1}^{n}y_{i}^{2} \right\}$$ Logo, chegamos que $Y_{j} \sim N(0,1)$ e são iid

Agora vamos demonstrar um dos teoremas mais surpreendentes da estatística

<a id="sample-mean-and-sample-variance-independence"></a>

**Teorema: Independência da Média e Variância Amostral**

Sejam $X_{1},\ldots,X_{n} \sim N\left( \mu,\sigma^{2} \right)$ e dados os estimadores: $$\hat{\mu} = \frac{1}{n}\sum_{i = 1}^{n}X_{i}\text{\quad\quad}\hat{\sigma^{2}} = \frac{1}{n}\sum_{i = 1}^{n}\left( X_{i} - \hat{\mu} \right)^{2}$$ As variáveis aleatórias $\hat{\mu}$ e $\hat{\sigma^{2}}$ são **INDEPENDENTES** entre si. Junto desse teorema, também mostraremos que: $$\frac{1}{\sigma^{2}}\sum_{i = 1}^{n}\left( X_{i} - \hat{\mu} \right)^{2} \sim Χ_{n - 1}^{2}$$

**Demonstração**

Primeiro vamos provar considerando que $\mu = 0$ e $\sigma^{2} = 1$, de forma que utilizaremos esse resultado para generalizar posteriormente.

Vamos primeiro definir $u = \begin{pmatrix} \frac{1}{\sqrt{n}} & \ldots & \frac{1}{\sqrt{n}} \end{pmatrix}^{T}$, então construímos uma matriz $Q$ utilizando Gram-Schmidt de forma que $u$ seja a primeira linha dessa matriz. Então definimos: $$\begin{pmatrix} Y_{1} \\ \vdots \\ Y_{n} \end{pmatrix} = Q\begin{pmatrix} X_{1} \\ \vdots \\ X_{n} \end{pmatrix}$$ Vimos pelo [\[normals-orthogonal-transformation\]](#normals-orthogonal-transformation) que $Y_{j}$ são iid e são normais padrão também. Guarde essa informação! Não é difícil ver que: $$Y_{1} = \frac{1}{\sqrt{n}}\sum_{i = 1}^{n}X_{i} = \hat{\mu}\sqrt{n}$$ Como $\sum_{i = 1}^{n}X_{i}^{2} = \sum_{i = 1}^{n}Y_{i}^{2}$, então: $$\sum_{i = 2}^{n}Y_{i}^{2} = \sum_{i = 1}^{n}Y_{i}^{2} - Y_{1}^{2} = \sum_{i = 1}^{n}X_{i}^{2} - n\left( \hat{\mu} \right)^{2} = \sum_{i = 1}^{n}\left( X_{i} - \hat{\mu} \right)^{2}$$ Ou seja, $\hat{\mu}$ e $\hat{\sigma^{2}}$ são independentes! Dado esse resultado, consideremos agora média e variância não-padrões. Então vamos definir: $$Z_{i} = \frac{X_{i} - \mu}{\sigma}$$ Então $Z_{1},\ldots,Z_{n}$ são iid. Sabemos que ${\overline{Z}}_{n}$ e $\sum(Z_{i} - {\overline{Z}}_{n})$ são independentes. Perceba também que, como $\sum(Z_{i} - {\overline{Z}}_{n})$ = $\sum_{i = 2}^{n}Y_{i}$, então $\sum(Z_{i} - {\overline{Z}}_{n}) \sim Χ_{n - 1}^{2}$. Porém, sabemos também que ${\overline{X}}_{n} \sim N\left( \mu,\frac{\sigma^{2}}{n} \right)$, então $$\begin{array}{r} {\overline{Z}}_{n} = \frac{{\overline{X}}_{n} - \mu}{\sigma} \\ \Rightarrow \sum\left( Z_{i} - {\overline{Z}}_{n} \right)^{2} = \frac{1}{\sigma^{2}}\sum\left( X_{i} - {\overline{X}}_{n} \right)^{2} \end{array}$$ Logo, ${\overline{X}}_{n}$ e $\frac{1}{n}\sum\left( X_{i} - {\overline{X}}_{n} \right)^{2}$ são independentes e $\frac{1}{\sigma^{2}}\sum\left( X_{i} - {\overline{X}}_{n} \right)^{2} \sim Χ_{n - 1}^{2}$

Esse resultado é interessante pois, em certas ocasiões, podemos querer saber a seguinte probabilidade: $${\mathbb{P}}(\vert \hat{\mu} - \mu\vert  \leq \frac{1}{5}\sigma,\vert \hat{\sigma} - \sigma\vert  \leq \frac{1}{5}\sigma) \geq \frac{1}{2}$$ Já que ela indica uma probabilidade de proximidade entre meus estimadores e meus parâmetros. Porém, pelo [\[sample-mean-and-sample-variance-independence\]](#sample-mean-and-sample-variance-independence), podemos separar essa probabilidade em: $$\underset{p_{1}}{\underbracket{{\mathbb{P}}(\vert \hat{\mu} - \mu\vert  \leq \frac{1}{5}\sigma)}}\ \underset{p_{2}}{\underbracket{{\mathbb{P}}(\vert \hat{\sigma} - \sigma\vert  \leq \frac{1}{5}\sigma)}} \geq \frac{1}{2}$$ e isso simplifica bastante nossas contas! Vamos definir $U \sim N(0,1)$, então podemos reescrever as probabilidades como: $$p_{1} = {\mathbb{P}}(\frac{\sqrt{n}}{\sigma}\vert \hat{\mu} - \mu\vert  < \frac{1}{5}\sqrt{n}) = {\mathbb{P}}(\vert U\vert  < \frac{1}{5}\sqrt{n})$$

definindo $V = \frac{n}{\sigma^{2}}\hat{\sigma^{2}}$, sabemos que $V \sim Χ_{n - 1}^{2}$, então $$\begin{aligned} p_{2} & = {\mathbb{P}}( - \frac{1}{5}\sigma \leq \hat{\sigma} - \sigma \leq \frac{1}{5}\sigma) = {\mathbb{P}}(\frac{4}{5}\sigma \leq \hat{\sigma} \leq \frac{6}{5}\sigma) \\ & = {\mathbb{P}}\left( \frac{16}{25}\sigma^{2} \leq {\hat{\sigma}}^{2} \leq \frac{36}{25}\sigma^{2} \right) = {\mathbb{P}}(\frac{16}{25}n \leq V \leq \frac{36}{25}n) \end{aligned}$$

e como $V \sim Χ_{n - 1}^{2}$, basta consultar uma tabela ou um software para descobrir esses quantis

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Propriedades](../distribuicao-chi-quadrado/index.md#propriedades)
- Próximo: [Distribuições $t$](../distribuicoes-t/index.md)
