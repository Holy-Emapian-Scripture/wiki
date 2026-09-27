---
layout: "default"
title: "Distribuições Marginais e Condicionais — Variáveis Aleatórias Contínuas Bidimensionais"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 15
---

[Probabilidade](../../index.md) · [Variáveis Aleatórias Contínuas Bidimensionais](../index.md)

<!-- wiki:original:inicio -->
<a id="secao_distr_marginais_condicionais"></a>

# Distribuições Marginais e Condicionais

Lembrando o caso discreto, dadas $X,Y$ v.a’s discretas com densidade conjunta $p(x,y) = P(X = x \cap Y = y)$, temos os conceitos e covariância e correlação:

$$\begin{array}{r} \text{ Cov}(X,Y) = E(XY) - E(X)E(Y) \\ \rho(X,Y) = \frac{\text{ Cov}(X,Y)}{\sigma(X)\sigma(Y)} \end{array}$$

Também temos as distribuições marginais e condicionais (Pelo teorema de Bayes e a Lei da Probabilidade Total):

$$\begin{array}{r} p_{X}(x) = P(X = x) = \sum_{y}p(x,y) \\ p_{Y}(y) = P(Y = y) = \sum_{x}p(x,y) \\ p_{X\vert Y}\left( x\vert y \right) = P\left( X = x~\vert ~Y = y \right) = \frac{p(x,y)}{p_{Y}(y)} \end{array}$$

Com $f(x,y)$ sendo uma densidade conjunta, a diferença agora é a transição de $\sum \rightarrow \int$:

**Definição**

(Distribuição Marginal)  
A distribuição marginal de $X$ é dada por:

$$f_{X}(x) = \int_{- \infty}^{\infty}f(x,y)dy$$

<a id="definicao_distr_marginal"></a>

**Definição**

(Distribuição Condicional)  
A distribuição condicional de $X$ dado $Y$ é dada por:

$$f_{X\vert Y}\left( x\vert y \right) = \frac{f(x,y)}{f_{Y}(y)}$$

<a id="definicao_distr_condicional"></a>

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [Função de Densidade Conjunta](../funcao-de-densidade-conjunta/index.md)
- Próximo: [Covariância e Correlação](../covariancia-e-correlacao/index.md)
