---
layout: "default"
title: "Função de Densidade Conjunta — Variáveis Aleatórias Contínuas Bidimensionais"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 14
---

[Probabilidade](../../index.md) · [Variáveis Aleatórias Contínuas Bidimensionais](../index.md)

<!-- wiki:original:inicio -->
<a id="secao_fdc"></a>

# Função de Densidade Conjunta

**Definição**

(Função de Densidade Conjunta)  
Uma função de densidade conjunta $f(x,y)$ das variáveis $X$ e $Y$ é uma função com a seguinte propriedade:

$$P\left( (X,Y) \in R \right) = \iint_{R}f(x,y)dA$$

Onde $R \subset {\mathbb{R}}^{2}$. Por conseguinte, $f$ deve satisfazer:

$$\begin{array}{r} f(x,y) \geq 0,\forall(x,y) \in {\mathbb{R}}^{2} \\ \int_{- \infty}^{\infty}\int_{- \infty}^{\infty}f(x,y)dxdy = 1 \end{array}$$

<a id="definicao_conjunta"></a>

<a id="secao-26"></a>

## Esperança, Variância e Desvio-Padrão

**Definição**

(Esperança)  
Dadas $X,Y$ com densidade conjunta $f(x,y)$, a esperança de $X$ é:

$$E(X) = \iint_{{\mathbb{R}}^{2}}xf(x,y)dA$$

<a id="definicao_esperanca_conjunta"></a>

**Definição**

(Variância, Desvio-Padrão)  
A variância de $X$ é análoga ao caso anterior:

$$V(X) = E\left( X^{2} \right) - {E(X)}^{2}$$

O desvio padrão é:

$$\sigma(X) = \sqrt{V(X)}$$

<a id="definicao_variancia_desviopadrao_conjunta"></a>

<a id="secao-27"></a>

## LOTUS 2

Dadas $X,Y$ com densidade conjunta $f(x,y)$, o valor esperado de uma função qualquer $g(X,Y)$ é:

$$E\left( g(X,Y) \right) = \iint_{{\mathbb{R}}^{2}}g(x,y)f(x,y)dA$$ <a id="lotus2"></a>

Quando a densidade conjunta é constante em $S \subset {\mathbb{R}}^{2}$ e $0$ fora de $S$, dizemos que $f(x,y)$ é uma função de densidade uniforme em $S$:

$$f(x,y) = \begin{cases} 0\text{, }\text{ se }(x,y) \notin S \\ \frac{1}{\text{Área}(S)}\text{, }\text{ se }(x,y) \in S \end{cases}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [Variáveis Aleatórias Contínuas Bidimensionais](../index.md)
- Próximo: [Distribuições Marginais e Condicionais](../distribuicoes-marginais-e-condicionais/index.md)
