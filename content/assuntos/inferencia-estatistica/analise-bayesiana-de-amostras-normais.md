---
layout: "default"
title: "Análise Bayesiana de Amostras Normais"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 12
---

[Inferência Estatística](index.md)

<!-- wiki:original:inicio -->

<a id="secao-12"></a>

# Análise Bayesiana de Amostras Normais


<a id="familia-de-conjugados"></a>
<a id="secao-13"></a>

## Família de Conjugados

**Teorema: Família de Conjugados**

Suponha que $X_{1},\ldots,X_{n}\vert \mu,\tau \sim N(\mu,\tau)$ e temos que $\mu\vert \tau \sim N\left( \mu_{0},\lambda_{0}\tau_{0} \right)$ e $\tau \sim \Gamma(\alpha_{0},\beta_{0})$, então a posteriori de $\mu$ e $\tau$ \[$p\left( \mu,\tau\vert \underline{x} \right)$\] é: $$\begin{array}{r} \mu,\tau\vert \underline{x} \sim N\left( \mu_{1},\lambda_{1}\tau \right) \\ \mu_{1} = \frac{\lambda_{0}\mu_{0} + n{\overline{x}}_{n}}{\lambda_{0} + n}\text{\quad\quad}\lambda_{1} = \lambda_{0} + n \end{array}$$ $$\begin{array}{r} \tau \sim \Gamma(\alpha_{1},\beta_{1}) \\ \alpha_{1} = \alpha_{0} + \frac{n}{2}\text{\quad\quad}\beta_{1} = \beta_{0} + \frac{1}{2}s_{n}^{2} + \frac{n\lambda_{0}\left( {\overline{x}}_{n} - \mu_{0} \right)^{2}}{2\left( \lambda_{0} + n \right)} \end{array}$$

Essa família de conjugados é chamada de NormalGamma com parâmetros $\alpha_{0}$, $\beta_{0}$, $\mu_{0}$ e $\lambda_{0}$, de forma que a posteriori de $\mu,\tau$ é a NormalGamma com parâmetros $\alpha_{1}$, $\beta_{1}$, $\mu_{1}$ e $\lambda_{1}$. Vale lembrar também que: $$p(\mu,\tau) \propto p\left( \mu\vert \tau \right)p(\tau)$$

Outro ponto é que $\mu$ e $\tau$ **não** são independentes, e mesmo que a gente escolha eles de forma que eles sejam independentes a priori, mesmo após uma única observação, eles já viram dependentes

<a id="secao-14"></a>

## Marginais

Nós encontramos as distribuições de $\mu,\tau$, $\mu\vert \tau$ e $\tau$, porém, qual seria a marginal de $\mu$?

**Teorema: Marginal de $\mu$**

Suponha que $\mu,\tau \sim \text{ NormalGamma}\left( \mu_{0},\lambda_{0},\alpha_{0},\beta_{0} \right)$, então: $$\left( \frac{\lambda_{0}\alpha_{0}}{\beta_{0}} \right)^{\frac{1}{2}}\left( \mu - \mu_{0} \right) \sim t_{2\alpha_{0}}$$

**Demonstração**

$\mu\vert \tau \sim N\left( \mu_{0},\lambda_{0}\tau \right)$, então temos que: $${\mathbb{V}}\left\lbrack \mu\vert \tau \right\rbrack = \frac{1}{\lambda_{0}\tau} \Rightarrow \left( \mu - \mu_{0} \right) \cdot \left( \lambda_{0}\tau \right)^{\frac{1}{2}} \sim N(0,1)$$ Então seja $p(\tau)$ a marginal de $\tau$ e $p\left( \mu\vert \tau \right)$ a pdf condicional de $\mu$ em $\tau$ $$p(z,\tau) = \underset{\Phi(z) \rightarrow \text{ pdf da }N(0,1)}{\underbrace{\left( \lambda_{0}\tau \right)^{- \frac{1}{2}} \cdot p\left( \mu = \left( \lambda_{0}\tau \right)^{- \frac{1}{2}}z + \mu_{0}~\vert ~\tau \right)}}p(\tau)$$ Como eu consigo exprimir $p(z,\tau)$ como a multiplicação de suas marginais, isso significa que $z$ e $\tau$ são **independentes**. Definimos então $Y = 2\beta_{0}\tau \Rightarrow Y \sim \Gamma(\alpha_{0},\frac{1}{2}) \sim Χ_{2\alpha_{0}}^{2}$. Ou seja, vamos ter que: $$U = \frac{Z}{\left( \frac{Y}{2\alpha_{0}} \right)^{\frac{1}{2}}} \sim t_{2\alpha_{0}} = \frac{\left( \lambda_{0}\tau \right)^{\frac{1}{2}}\left( \mu - \mu_{0} \right)}{\left( \frac{2\beta_{0}\tau}{2\alpha_{0}} \right)^{\frac{1}{2}}} = \left( \frac{\lambda_{0}\alpha_{0}}{\beta_{0}} \right)^{\frac{1}{2}}\left( \mu - \mu_{0} \right)$$

Por conta disso, obtemos o seguinte

**Corolário: Propriedades da Marginal de $\mu$**

Se $\alpha_{0} > \frac{1}{2} \Rightarrow {\mathbb{E}}\lbrack\mu\rbrack = \mu_{0}$. Se $\alpha_{0} > 1 \Rightarrow {\mathbb{V}}\lbrack\mu\rbrack = \frac{\beta_{0}}{\lambda_{0}\left( \alpha_{0} - 1 \right)}$

<a id="distribuicoes-improprias"></a>
<a id="secao-15"></a>

## Distribuições Impróprias

Utilizamos esses parâmetros mais por conveniência do que por qualquer outro motivo (Como uma convicção). Para a posteriori, utilizamos os seguintes hiperparâmetros: $$\alpha_{0} = - \frac{1}{2}\text{\quad\quad}\beta_{0} = 0\text{\quad\quad}\mu_{0} = 0\text{\quad\quad}\lambda_{0} = 0$$ assim, obtemos as seguintes pdf’s **a priori**: $$p(\mu) = 1\text{\quad\quad}p(\tau) = \frac{1}{2}\tau^{- 1}\text{\quad\quad}p(\mu,\tau) = \frac{1}{\tau}$$ Dessa forma, a posteriori fica: $$p(\mu,\tau) \propto \left\{ \tau^{\frac{1}{2}}\exp\left\lbrack \frac{- (n\pi)}{2}\left( \mu - {\overline{x}}_{n} \right)^{2} \right\rbrack \right\}\tau^{\frac{n - 1}{2} - 1}\exp\left\lbrack - \tau\frac{s_{n}^{2}}{2} \right\rbrack$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Intervalos de Confiança](intervalos-de-confianca.md)
- Próximo: [Estimadores não-viezados](estimadores-nao-viezados.md)
