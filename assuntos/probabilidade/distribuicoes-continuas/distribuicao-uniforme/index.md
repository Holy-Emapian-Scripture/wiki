---
layout: "default"
title: "Distribuição Uniforme — Distribuições Contínuas"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 8
---

[Probabilidade](../../index.md) · [Distribuições Contínuas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao_dist_uniforme"></a>

# Distribuição Uniforme

Uma v.a contínua $X$ tem distribuição uniforme no intervalo $\lbrack a,b\rbrack$ se sua PDF for da forma:

$$f_{X}(\varphi) = \begin{cases} 0\text{, }\text{ se }\varphi < a \\ \frac{1}{b - a}\text{, }\text{ se }a \leq \varphi \leq b \end{cases}$$

Desta forma sua CDF é:

$$F_{X}(\varphi) = \begin{cases} 0\text{, }\text{ se }\varphi < a \\ \frac{\varphi - a}{b - a}\text{, }\text{ se }a \leq \varphi \leq b \\ 1\text{, }\text{ se }\varphi > b \end{cases}$$

O seguinte teorema é extremamente importante:

**Teorema**

(Universalidade da Uniforme)  
Se $X$ é uma v.a contínua com PDF $f_{X}$ e CDF $F_{X}$, então $Y = F_{X}(X)$ é uma uniforme em $\lbrack 0,1\rbrack$, ou seja: $Y \sim U\lbrack 0,1\rbrack$

<a id="teorema_universalidade_uniforme"></a>

**Demonstração**

$$F_{Y}(y) = P(Y \leq y) = P\left( F_{X}(X) \leq y \right) = P\left( X \leq F_{X}^{- 1}(y) \right) = F_{X}\left( F_{X}^{- 1}(y) \right) = y$$

Logo $Y$ é uma uniforme em $\lbrack 0,1\rbrack$.

<a id="secao-9"></a>

## Esperança

Com $X \sim U\lbrack a,b\rbrack$, temos

$$E(X) = \int_{- \infty}^{\infty}\varphi f_{X}(\varphi)d\varphi = \int_{a}^{b}\varphi\left( \frac{1}{b - a} \right)d\varphi = \frac{a + b}{2}$$

<a id="secao-10"></a>

## Variância

Com $X \sim U\lbrack a,b\rbrack$, temos:

$$\begin{array}{r} E\left( X^{2} \right) = \int_{- \infty}^{\infty}\varphi^{2}f_{X}(\varphi)d\varphi = \int_{a}^{b}\varphi^{2}\left( \frac{1}{b - a} \right)d\varphi = \left( \frac{1}{b - a} \right)\int_{a}^{b}\varphi^{2}d\varphi \\ = \left( \frac{1}{b - a} \right)\left\lbrack \frac{\varphi^{3}}{3} \right\rbrack_{a}^{b} = \left( \frac{1}{b - a} \right)\left\lbrack \frac{b^{3} - a^{3}}{3} \right\rbrack = \frac{b^{2} + ab + a^{2}}{3} \end{array}$$ <a id="esperanca_uniforme"></a>

E a variância fica:

$$V(X) = E\left( X^{2} \right) - {E(X)}^{2} = \frac{b^{2} + ab + a^{2}}{3} - \left( \frac{a + b}{2} \right)^{2} = \frac{(b - a)^{2}}{12}$$ <a id="variancia_uniforme"></a>

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [Distribuições Contínuas](../index.md)
- Próximo: [Distribuição Exponencial](../distribuicao-exponencial/index.md)
