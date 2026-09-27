---
layout: "default"
title: "Esperança Condicional — Variáveis Aleatórias Contínuas Bidimensionais"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 17
---

[Probabilidade](../../index.md) · [Variáveis Aleatórias Contínuas Bidimensionais](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-30"></a>

# Esperança Condicional

Isso é bem útil:

**Definição**

A esperança condicional de $X$ na certeza de $Y = y$ é:

$$E\left( X~\vert ~Y = y \right) = \int_{- \infty}^{\infty}xf_{X\vert Y}\left( x\vert y \right)dx$$

(As vezes denotado por $E\left\lbrack X\vert y \right\rbrack$).

Os teoremas da gênesis também são úteis:

**Teorema**

(Lei de Adão)  
$\forall$ v.a’s $X,Y$ temos:

$$E\left( E\left( X\vert Y \right) \right) = E(X)$$

**Demonstração**

Trivial

**Teorema**

(Lei de Eva)  
$\forall$ v.a’s $X,Y$, temos:

$$V(Y) = E\left( V\left( Y\vert X \right) \right) + V\left( E\left( Y\vert X \right) \right)$$

**Demonstração**

Trivial

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [Covariância e Correlação](../covariancia-e-correlacao/index.md)
- Próximo: [Independência](../independencia/index.md)
