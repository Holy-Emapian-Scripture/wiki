---
layout: "default"
title: "Lagrangeano — Otimização com restrições genéricas"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 17
---

[Otimização para Ciência de Dados](../../index.md) · [Otimização com restrições genéricas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-22"></a>

# Lagrangeano

O lagrangeando é uma função que será de grande importância, ela pode parecer meio confusa (Pois ela é), mas, a partir de agora, ela será nossa definição de “Derivar e igualar a $0$”. Como assim? Sempre que queríamos minimizar/maximizar uma função, derivávamos e igualávamos a $0$, só que vimos que, com restrições, isso não funciona mais, porém, essa função ainda se aplica (Com algumas ressalvas) no lagrangeano (Como veremos)

<a id="lagrange-function"></a>

**Definição: Lagrangeano**

O **Lagrangeano** associado à função $f$ é a função $L:{\mathbb{R}}^{n} \times {\mathbb{R}}^{m} \times {\mathbb{R}}^{p} \rightarrow {\mathbb{R}}$ tal que: $$L(x,\lambda,\mu) = f(x) + \lambda^{T}g(x) + \mu^{T}h(x)$$ Onde: $$\lambda = \begin{pmatrix} \lambda_{1} \\ \vdots \\ \lambda_{m} \end{pmatrix},\ \mu = \begin{pmatrix} \mu_{1} \\ \vdots \\ \mu_{p} \end{pmatrix},\ g(x) = \begin{pmatrix} g_{1}(x) \\ \vdots \\ g_{m}(x) \end{pmatrix},\ h(x) = \begin{pmatrix} h_{1}(x) \\ \vdots \\ h_{p}(x) \end{pmatrix}$$

**Teorema: Gradiente Lagrangeano**

Dado o Lagrangeano de uma função $f$, temos que o gradiente do lagrangeano **somente em relação a $x$** se da por: $$\nabla_{x}L(x,\lambda,\mu) = \nabla f(x) + \sum_{i = 1}^{m}\lambda_{i}\nabla g_{i}(x) + \sum_{j = 1}^{p}\mu_{j}\nabla h_{j}(x)$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Otimização com restrições genéricas](../index.md)
- Próximo: [As generalizações do KKT](../as-generalizacoes-do-kkt/index.md)
