---
layout: "default"
title: "Família de Conjugados — Análise Bayesiana de Amostras Normais"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 13
---

[Inferência Estatística](../../index.md) · [Análise Bayesiana de Amostras Normais](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-13"></a>

# Família de Conjugados

**Teorema: Família de Conjugados**

Suponha que $X_{1},\ldots,X_{n}\vert \mu,\tau \sim N(\mu,\tau)$ e temos que $\mu\vert \tau \sim N\left( \mu_{0},\lambda_{0}\tau_{0} \right)$ e $\tau \sim \Gamma(\alpha_{0},\beta_{0})$, então a posteriori de $\mu$ e $\tau$ \[$p\left( \mu,\tau\vert \underline{x} \right)$\] é: $$\begin{array}{r} \mu,\tau\vert \underline{x} \sim N\left( \mu_{1},\lambda_{1}\tau \right) \\ \mu_{1} = \frac{\lambda_{0}\mu_{0} + n{\overline{x}}_{n}}{\lambda_{0} + n}\text{\quad\quad}\lambda_{1} = \lambda_{0} + n \end{array}$$ $$\begin{array}{r} \tau \sim \Gamma(\alpha_{1},\beta_{1}) \\ \alpha_{1} = \alpha_{0} + \frac{n}{2}\text{\quad\quad}\beta_{1} = \beta_{0} + \frac{1}{2}s_{n}^{2} + \frac{n\lambda_{0}\left( {\overline{x}}_{n} - \mu_{0} \right)^{2}}{2\left( \lambda_{0} + n \right)} \end{array}$$

Essa família de conjugados é chamada de NormalGamma com parâmetros $\alpha_{0}$, $\beta_{0}$, $\mu_{0}$ e $\lambda_{0}$, de forma que a posteriori de $\mu,\tau$ é a NormalGamma com parâmetros $\alpha_{1}$, $\beta_{1}$, $\mu_{1}$ e $\lambda_{1}$. Vale lembrar também que: $$p(\mu,\tau) \propto p\left( \mu\vert \tau \right)p(\tau)$$

Outro ponto é que $\mu$ e $\tau$ **não** são independentes, e mesmo que a gente escolha eles de forma que eles sejam independentes a priori, mesmo após uma única observação, eles já viram dependentes

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Análise Bayesiana de Amostras Normais](../index.md)
- Próximo: [Marginais](../marginais/index.md)
