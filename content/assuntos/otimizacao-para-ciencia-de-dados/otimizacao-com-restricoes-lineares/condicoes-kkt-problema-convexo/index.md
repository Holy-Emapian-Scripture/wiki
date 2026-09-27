---
layout: "default"
title: "Condições KKT: Problema convexo — Otimização com restrições lineares"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 14
---

[Otimização para Ciência de Dados](../../index.md) · [Otimização com restrições lineares](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-19"></a>

# Condições KKT: Problema convexo

<a id="kkt-convex-conditions"></a>

**Teorema: Condições KKT para restrições lineares: condições necessárias de otimalidade com função convexa**

Considere o problema de minimização $$\begin{array}{r} \min\limits_{x}f(x) \\ \text{sujeito à }a_{i}^{T}x \leq b_{i},i = 1,\ldots,m \end{array}$$ onde $f$ é uma função continuamente diferenciável **convexa** em ${\mathbb{R}}^{n}$ $\left\{ a_{i} \right\}_{i = 1}^{m} \subset {\mathbb{R}} \land \left\{ b_{i} \right\}_{i = 1}^{m} \subset R$. Então, se $x^{\ast}$ é um ponto de mínimo local do problema $\Leftrightarrow \exists\lambda_{1},...,\lambda_{m} \geq 0$ tais que $$\begin{array}{r} \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}a_{i} = 0, \\ \lambda_{i}\left( a_{i}^{T}x^{\ast} - b_{i} \right) = 0,\text{\quad\quad}i = 1,\ldots,m \\ a_{i}^{T}x^{\ast} - b_{i} \leq 0,\text{\quad\quad}i = 1,\ldots,m \end{array}$$

**Demonstração**

$( \Longrightarrow )$ Segue do [\[kkt-linear-conditions\]](../condicoes-kkt/index.md#kkt-linear-conditions)

$( \Longleftarrow )$ Definamos a função: $$h(x) ≔ f(x) + \sum_{i = 1}^{m}\lambda_{i}\left( a_{i}^{T}x - b_{i} \right)$$ Temos que: $$\nabla h\left( x^{\ast} \right) = \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}a_{i}$$ Como $h$ é convexa (Soma de funções convexas), segue que $x^{\ast}$ é ponto mínimo de $h$ em ${\mathbb{R}}^{n}$. Em particular, dado qualquer $x \in {\mathbb{R}}^{n}$ tal que: $$a_{i}^{T}x \leq b_{i},\ i = 1,\ldots,m$$ Tem-se que: $$\begin{array}{r} f\left( x^{\ast} \right) = f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}\left( a_{i}^{T}x - b_{i} \right) \\ \leq f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}\left( a_{i}^{T}x - b_{i} \right) \\ \leq f(x) \end{array}$$ Na primeira equação utilizamos a segunda condição e na segunda desigualdade usamos o fato que $\lambda_{i} \geq 0$. Concluímos então que $x^{\ast}$ é solução do sistema

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Condições KKT](../condicoes-kkt/index.md)
- Próximo: [Condições KKT com restrições lineares de igualdade](../condicoes-kkt-com-restricoes-lineares-de-igualdade/index.md)
