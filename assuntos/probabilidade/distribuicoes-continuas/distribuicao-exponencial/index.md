---
layout: "default"
title: "Distribuição Exponencial — Distribuições Contínuas"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 9
---

[Probabilidade](../../index.md) · [Distribuições Contínuas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao_dist_exponencial"></a>

# Distribuição Exponencial

Uma v.a contínua $X$ tem distribuição exponencial se sua PDF for da forma:

$$f_{X}(\varphi) = \begin{cases} 0\text{, }\text{ se }\varphi < 0 \\ \lambda e^{- \lambda\varphi}\text{, }\text{ se }\varphi \geq 0 \end{cases}$$

$\lambda > 0$ é o parâmetro da distribuição. A CDF é dada por:

$$F_{X}(\varphi) = \begin{cases} 0\text{, }\text{ se }\varphi < 0 \\ 1 - e^{- \lambda\varphi}\text{, }\text{ se }\varphi \geq 0 \end{cases}$$

![PDF e CDF Da Exponencial com $\lambda = 2$](../../assets/pdf_cdf_expo.png)

*Figura 1. PDF e CDF Da Exponencial com $\lambda = 2$*

Isto também é útil:

**Proposição**

Se $X \sim \text{Expo}(\lambda)$, $Y = aX$, então $Y \sim \text{Expo}(\frac{\lambda}{a})$

**Demonstração**

Pela [\[propriedade_derivada_inversa\]](../../variaveis-aleatorias-continuas/propriedades-da-cdf-e-pdf/index.md#propriedade_derivada_inversa), temos:

$$\begin{array}{r} f_{Y}(y) = \frac{f_{X}(\varphi)}{h'(\varphi)} \\ h'(\varphi) = a \\ \varphi = h^{- 1}(y) = \frac{y}{a} \end{array}$$

Então:

$$\begin{array}{r} f_{Y}(y) = \frac{\lambda e^{- \lambda\left( \frac{y}{a} \right)}}{a} = \left( \frac{\lambda}{a} \right)e^{- \lambda\left( \frac{y}{a} \right)} \\ F_{Y}(y) = 1 - e^{- \lambda\left( \frac{y}{a} \right)} \end{array}$$

O que conclui a prova.

<a id="proposicao_exponencial"></a>

**Corolário**

Se $X \sim \text{Expo}(\lambda)$, então $\lambda X \sim \text{Expo}(1)$

<a id="corolario_exponencial"></a>

<a id="secao-12"></a>

## Esperança

Com $X \sim \text{Expo}(\lambda)$

$$E(X) = \int_{- \infty}^{\infty}\varphi f_{X}(\varphi)d\varphi = \int_{0}^{\infty}\varphi\lambda e^{- \lambda\varphi}d\varphi = \frac{1}{\lambda}$$

<a id="secao-13"></a>

## Variância

Com $X \sim \text{Expo}(\lambda)$, temos:

$$E\left( X^{2} \right) = \int_{- \infty}^{\infty}\varphi^{2}f_{X}(\varphi)d\varphi = \int_{0}^{\infty}\varphi^{2}\lambda e^{- \lambda\varphi}d\varphi = \frac{2}{\lambda^{2}}$$ <a id="esperanca_exponencial"></a>

E a variância fica:

$$V(X) = E\left( X^{2} \right) - {E(X)}^{2} = \frac{2}{\lambda^{2}} - \left( \frac{1}{\lambda} \right)^{2} = \frac{1}{\lambda^{2}}$$ <a id="variancia_exponencial"></a>

<a id="secao-14"></a>

## Perda de Memória

Uma v.a $X$ tem a propriedade de **perda de memória** se: $$P\left( X > s + t~\vert ~X > s \right) = P(X > t)$$ Isto é, a probabilidade de $X$ ser maior que $s + t$, dado que já passou $s$, é a mesma que a probabilidade de $X$ ser maior que $t$.

**A distribuição exponencial é a única distribuição contínua que tem a propriedade de perda de memória.**

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [Distribuição Uniforme](../distribuicao-uniforme/index.md)
- Próximo: [Distribuição Gamma](../distribuicao-gamma/index.md)
