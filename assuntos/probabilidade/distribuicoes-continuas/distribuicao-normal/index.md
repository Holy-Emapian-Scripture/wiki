---
layout: "default"
title: "Distribuição Normal — Distribuições Contínuas"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 11
---

[Probabilidade](../../index.md) · [Distribuições Contínuas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao_dist_normal"></a>

# Distribuição Normal

$X$ v.a contínua tem distribuição normal com média $\mu$ e variância $\sigma^{2}$ se sua PDF é dada por:

$$f_{X}(\varphi) = \frac{1}{\sigma\sqrt{2\pi}}e^{- \frac{(\varphi - \mu)^{2}}{2\sigma^{2}}}$$

Note que $f(\mu + a) = f(\mu - a)$, então a PDF é simétrica em torno de $\mu$ (a média).

A PROPOSIÇÃO ABAIXO É MUITO IMPORTANTE PARA RESOLVER PROBLEMS COM A NORMAL:

**Proposição**

Se $X \sim N\left( \mu,\sigma^{2} \right)$, então $Z = \frac{X - \mu}{\sigma} \sim N(0,1)$

<a id="proposicao_magia_normal"></a>

**Demonstração**

Pela [\[propriedade_derivada_inversa\]](../../variaveis-aleatorias-continuas/propriedades-da-cdf-e-pdf/index.md#propriedade_derivada_inversa), temos:

$$\begin{array}{r} f_{Z}(z) = \frac{f_{X}(\varphi)}{h'(\varphi)} \\ h'(\varphi) = \frac{1}{\sigma} \\ \varphi = h^{- 1}(z) = \mu + \sigma z \end{array}$$

Então:

$$\begin{array}{r} f_{Z}(z) = \left( \frac{1}{\sigma\sqrt{2\pi}} \right)\frac{e^{- \frac{(\mu + \sigma z - \mu)^{2}}{2\sigma^{2}}}}{\frac{1}{\sigma}} \\ = \frac{1}{\sqrt{2\pi}}e^{- \frac{z^{2}}{2}} \end{array}$$

Logo $Z \sim N(0,1)$.

A [\[proposicao_magia_normal\]](#proposicao_magia_normal) é muito útil para resolver problemas com uma tabela de valores da FDA de $N(0,1)$.

<a id="secao-21"></a>

## Esperança

Com $X \sim N\left( \mu,\sigma^{2} \right)$, temos:

$$E(X) = \int_{- \infty}^{\infty}\varphi f_{X}(\varphi)d\varphi = \int_{- \infty}^{\infty}\varphi\left( \frac{1}{\sigma\sqrt{2\pi}} \right)e^{- \frac{(\varphi - \mu)^{2}}{2\sigma^{2}}}d\varphi = \mu$$

<a id="secao-22"></a>

## Variância

Com $X \sim N\left( \mu,\sigma^{2} \right)$, temos: $$E\left( X^{2} \right) = \int_{- \infty}^{\infty}\varphi^{2}f_{X}(\varphi)d\varphi = \int_{- \infty}^{\infty}\varphi^{2}\left( \frac{1}{\sigma\sqrt{2\pi}} \right)e^{- \frac{(\varphi - \mu)^{2}}{2\sigma^{2}}}d\varphi = \mu^{2} + \sigma^{2}$$

Logo a variância fica:

$$V(X) = E\left( X^{2} \right) - {E(X)}^{2} = \mu^{2} + \sigma^{2} - \mu^{2} = \sigma^{2}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [Distribuição Gamma](../distribuicao-gamma/index.md)
- Próximo: [Taxa de Falhas](../taxa-de-falhas/index.md)
