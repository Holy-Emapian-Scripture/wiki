---
layout: "default"
title: "Condições KKT — Otimização com restrições lineares"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 13
---

[Otimização para Ciência de Dados](../../index.md) · [Otimização com restrições lineares](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-18"></a>

# Condições KKT

<a id="kkt-linear-conditions"></a>

**Teorema: Condições KKT para restrições lineares: condições necessárias de otimalidade**

Considere o problema de minimização [\[optimization-with-linear-conditions\]](../index.md#optimization-with-linear-conditions) onde $f$ é uma função continuamente diferenciável em ${\mathbb{R}}^{n}$, $\left\{ a_{i} \right\}_{i = 1}^{m} \subset {\mathbb{R}}$ e $\left\{ b_{i} \right\}_{i = 1}^{m} \subset R$. Então, **se** $x^{\ast}$ é um ponto de **mínimo local** do problema, $\exists\lambda_{1},...,\lambda_{m} \geq 0$ tais que $$\begin{array}{r} \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}a_{i} = 0, \\ \lambda_{i}\left( a_{i}^{T}x^{\ast} - b_{i} \right) = 0,\text{\quad\quad}i = 1,\ldots,m \\ a_{i}^{T}x^{\ast} - b_{i} \leq 0,\text{\quad\quad}i = 1,\ldots,m \end{array}$$

Como esse teorema necessita de vários outros resultados, não vou escrever a sua demonstração aqui. Se estiver curioso para saber a demonstração, confira o apêndice das anotações do Phillip

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Otimização com restrições lineares](../index.md)
- Próximo: [Condições KKT: Problema convexo](../condicoes-kkt-problema-convexo/index.md)
