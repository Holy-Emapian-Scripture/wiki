---
layout: "default"
title: "Marginais — Análise Bayesiana de Amostras Normais"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 14
---

[Inferência Estatística](../../index.md) · [Análise Bayesiana de Amostras Normais](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-14"></a>

# Marginais

Nós encontramos as distribuições de $\mu,\tau$, $\mu\vert \tau$ e $\tau$, porém, qual seria a marginal de $\mu$?

**Teorema: Marginal de $\mu$**

Suponha que $\mu,\tau \sim \text{ NormalGamma}\left( \mu_{0},\lambda_{0},\alpha_{0},\beta_{0} \right)$, então: $$\left( \frac{\lambda_{0}\alpha_{0}}{\beta_{0}} \right)^{\frac{1}{2}}\left( \mu - \mu_{0} \right) \sim t_{2\alpha_{0}}$$

**Demonstração**

$\mu\vert \tau \sim N\left( \mu_{0},\lambda_{0}\tau \right)$, então temos que: $${\mathbb{V}}\left\lbrack \mu\vert \tau \right\rbrack = \frac{1}{\lambda_{0}\tau} \Rightarrow \left( \mu - \mu_{0} \right) \cdot \left( \lambda_{0}\tau \right)^{\frac{1}{2}} \sim N(0,1)$$ Então seja $p(\tau)$ a marginal de $\tau$ e $p\left( \mu\vert \tau \right)$ a pdf condicional de $\mu$ em $\tau$ $$p(z,\tau) = \underset{\Phi(z) \rightarrow \text{ pdf da }N(0,1)}{\underbrace{\left( \lambda_{0}\tau \right)^{- \frac{1}{2}} \cdot p\left( \mu = \left( \lambda_{0}\tau \right)^{- \frac{1}{2}}z + \mu_{0}~\vert ~\tau \right)}}p(\tau)$$ Como eu consigo exprimir $p(z,\tau)$ como a multiplicação de suas marginais, isso significa que $z$ e $\tau$ são **independentes**. Definimos então $Y = 2\beta_{0}\tau \Rightarrow Y \sim \Gamma(\alpha_{0},\frac{1}{2}) \sim Χ_{2\alpha_{0}}^{2}$. Ou seja, vamos ter que: $$U = \frac{Z}{\left( \frac{Y}{2\alpha_{0}} \right)^{\frac{1}{2}}} \sim t_{2\alpha_{0}} = \frac{\left( \lambda_{0}\tau \right)^{\frac{1}{2}}\left( \mu - \mu_{0} \right)}{\left( \frac{2\beta_{0}\tau}{2\alpha_{0}} \right)^{\frac{1}{2}}} = \left( \frac{\lambda_{0}\alpha_{0}}{\beta_{0}} \right)^{\frac{1}{2}}\left( \mu - \mu_{0} \right)$$

Por conta disso, obtemos o seguinte

**Corolário: Propriedades da Marginal de $\mu$**

Se $\alpha_{0} > \frac{1}{2} \Rightarrow {\mathbb{E}}\lbrack\mu\rbrack = \mu_{0}$. Se $\alpha_{0} > 1 \Rightarrow {\mathbb{V}}\lbrack\mu\rbrack = \frac{\beta_{0}}{\lambda_{0}\left( \alpha_{0} - 1 \right)}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Família de Conjugados](../familia-de-conjugados/index.md)
- Próximo: [Distribuições Impróprias](../distribuicoes-improprias/index.md)
