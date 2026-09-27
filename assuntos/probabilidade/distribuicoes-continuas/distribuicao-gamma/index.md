---
layout: "default"
title: "Distribuição Gamma — Distribuições Contínuas"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 10
---

[Probabilidade](../../index.md) · [Distribuições Contínuas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao_dist_gamma"></a>

# Distribuição Gamma

<a id="secao-16"></a>

## A função Gamma

A função $\Gamma$ é definida como:

$$\Gamma(\varphi) = \int_{0}^{\infty}t^{\varphi - 1}e^{- t}dt$$

As propriedades abaixo serão muito úteis:

**Propriedade**

$$n \in {\mathbb{N}} \Rightarrow \Gamma(n) = (n - 1)!$$

<a id="propriedade_natural_funcao_gamma"></a>

**Propriedade**

$$\Gamma(\varphi + 1) = \varphi\Gamma(\varphi),\forall\varphi > 0.$$

<a id="propriedade_funcao_gamma_phimaisum"></a>

Alguns valores úteis de $\Gamma$ são:

$$\begin{array}{r} \Gamma(\frac{1}{2}) = \sqrt{\pi} \\ \Gamma(\frac{3}{2}) = \left( \frac{1}{2} \right)\sqrt{\pi} \\ \Gamma(\frac{5}{2}) = \frac{3}{4}\sqrt{\pi} \\ \Gamma(\frac{7}{2}) = \frac{15}{8}\sqrt{\pi} \\ \Gamma(1) = 1 \\ \Gamma(2) = 1 \\ \Gamma(3) = 2 \\ \Gamma(4) = 6 \\ \Gamma(5) = 24 \\ \vdots \end{array}$$

<a id="secao-17"></a>

## A distribuição Gamma

Uma variável aleatória $X$ tem distribuição gamma com parâmetros $\alpha,\lambda > 0$ se sua PDF é dada por:

$$f_{X}(\varphi) = \begin{cases} 0\text{, }\text{ se }\varphi < 0 \\ \frac{\lambda^{\alpha}}{\Gamma(\alpha)}\varphi^{\alpha - 1}e^{- \lambda\varphi}\text{, }\text{ se }\varphi \geq 0 \end{cases}$$

<a id="secao-18"></a>

### Esperança

A esperança de $Z \sim \Gamma(\alpha,\lambda)$ é:

$$E(Z) = \int_{- \infty}^{\infty}\varphi f_{Z}(\varphi)d\varphi = \int_{0}^{\infty}\varphi\frac{\lambda^{\alpha}}{\Gamma(\alpha)}\varphi^{\alpha - 1}e^{- \lambda\varphi}d\varphi = \frac{1}{\Gamma(\alpha)}\int_{0}^{\infty}(\lambda\varphi)^{\alpha}e^{- \lambda\varphi}d\varphi$$

Fazendo $x = \lambda\varphi$, temos:

$$E(Z) = \frac{1}{\Gamma(\alpha)}\int_{0}^{\infty}x^{\alpha}e^{- x}\frac{dx}{\lambda} = \frac{1}{\lambda\Gamma(\alpha)}\Gamma(\alpha + 1) = \frac{\alpha}{\lambda}$$

<a id="secao-19"></a>

### Variância

Dada $Z \sim \Gamma(\alpha,\lambda)$:

$$\begin{array}{r} E\left( Z^{2} \right) = \frac{1}{\lambda\Gamma(\alpha)}\int_{0}^{\infty}(\lambda x)^{\alpha + 1}e^{- \lambda x}dx = \left( \frac{1}{\lambda^{2}}\Gamma(\alpha) \right)\int_{0}^{\infty}x^{\alpha + 1}e^{- x}dx \\ = \left( \frac{1}{\lambda}\Gamma(\alpha) \right)\Gamma(\alpha + 2) = \frac{\alpha(\alpha + 1)}{\lambda^{2}} \end{array}$$

E a variância fica:

$$V(Z) = E\left( Z^{2} \right) - {E(Z)}^{2} = \frac{\alpha(\alpha + 1)}{\lambda^{2}} - \left( \frac{\alpha}{\lambda} \right)^{2} = \frac{\alpha}{\lambda^{2}}$$

Isso também pode ser útil:

**Proposição**

Se $X \sim \Gamma(\alpha,\lambda)$ e $Z = \lambda X$, então $Z \sim \Gamma(\alpha,1)$

**Demonstração**

Pela [\[propriedade_derivada_inversa\]](../../variaveis-aleatorias-continuas/propriedades-da-cdf-e-pdf/index.md#propriedade_derivada_inversa), temos:

$$\begin{array}{r} f_{Z}(z) = \frac{f_{X}(\varphi)}{h'(\varphi)} \\ h'(\varphi) = \lambda \\ \varphi = h^{- 1}(z) = \frac{z}{\lambda} \end{array}$$

Então:

$$f_{Z}(z) = \frac{\frac{\lambda^{\alpha}}{\Gamma(\alpha)}\left( \frac{z}{\lambda} \right)^{\alpha - 1}e^{- \lambda\left( \frac{z}{\lambda} \right)}}{\lambda} = \left( \frac{1}{\Gamma(\alpha)} \right)z^{\alpha - 1}e^{- z}$$

Assim $Z \sim \Gamma(\alpha,1)$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [Distribuição Exponencial](../distribuicao-exponencial/index.md)
- Próximo: [Distribuição Normal](../distribuicao-normal/index.md)
