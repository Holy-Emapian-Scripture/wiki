---
layout: "default"
title: "Otimização com restrições lineares"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 12
---

[Otimização para Ciência de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-17"></a>

# Otimização com restrições lineares

------------------------------------------------------------------------

Aqui nós vamos introduzir um teorema muito importamte no ramo da otimização, o **teorema das condições KKT**. Esse teorema generaliza as condições **necessárias** para um problema de minimização **genérico**, porém, vamos começar por baixo, em vez de ja ir para o caso geral, vamos começar a passos pequenos

Primeiramente, queremos minimizar problemas do tipo: $$\begin{array}{r} \min\limits_{x}f(x) \\ x\text{ sujeito a restrições do tipo }a_{i}^{T}x \leq b_{i},\ i = 1,\ldots,m \end{array}$$<a id="optimization-with-linear-conditions"></a>

onde $f$ é continuamente diferenciável em ${\mathbb{R}}^{n},\ \left\{ a_{i} \right\}_{i = 1}^{m} \subset {\mathbb{R}}^{n},\left\{ b_{i} \right\}_{i = 1}^{m} \subset {\mathbb{R}}$. Ou seja, o conjunto viável $C$ é o poliédro: $$C = \cap_{i = 1}^{m}\left\{ x \in {\mathbb{R}}^{n}/a_{i}^{T}x \leq b_{i} \right\}$$

Há um exemplo nas anotaçẽos sobre convexidade do Phillip que mostram que $C$ é convexo.

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Condições KKT](condicoes-kkt/index.md)
2. [Condições KKT: Problema convexo](condicoes-kkt-problema-convexo/index.md)
3. [Condições KKT com restrições lineares de igualdade](condicoes-kkt-com-restricoes-lineares-de-igualdade/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Otimização sobre conjuntos convexos](../otimizacao-convexa/otimizacao-sobre-conjuntos-convexos/index.md)
- Próximo: [Condições KKT](condicoes-kkt/index.md)
