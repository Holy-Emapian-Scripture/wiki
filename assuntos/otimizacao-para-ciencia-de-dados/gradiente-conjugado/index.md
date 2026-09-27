---
layout: "default"
title: "Gradiente Conjugado"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A2.md"
trilha: "../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 10
---

[Otimização para Ciência de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-10"></a>

# Gradiente Conjugado

------------------------------------------------------------------------

Esse método é muito útil pois **garante a convergência globalmente em uma quantidade limitada de passos**. Porém, ele só pode ser aplicado no seguintes problemas: $$\min\limits_{x \in {\mathbb{R}}^{n}}c + b^{T}x + x^{T}Ax$$

Porém, antes de aplicarmos esse método, temos que fazer uma definição:

**Definição: Direção conjugada**

Dizemos que os vetores $\left\{ d_{1},\ldots,d_{n} \right\} \subseteq {\mathbb{R}}^{n}$ são direções conjugadas de $A$ se: $$d_{i}^{T}\left( Ad_{j} \right) = 0\text{\quad\quad}\forall i,j = 1,\ldots,n$$

Então vamos tentar, ingenuamente, aplicar o método: $$x^{(t + 1)} = x^{(t)} - \alpha d^{(t)}$$ de forma que $d_{t}$ é uma direção conjugada de $A$. Que tal tentarmos encontrar o melhor passo $\alpha$? Então temos que resolver: $$\begin{aligned} & \min\limits_{\alpha \in {\mathbb{R}}}f\left( x^{(t)} - \alpha d^{(t)} \right) \\ = & \min\limits_{\alpha \in {\mathbb{R}}}\left\{ c + b^{T}\left( x^{(t)} - \alpha d^{(t)} \right) + \left( x^{(t)} - \alpha d^{(t)} \right)^{T}A\left( x^{(t)} - \alpha d^{(t)} \right) \right\} \end{aligned}$$

Resolvendo esse problema, obtemos: $$\alpha^{(t)} = - \frac{\nabla f\left( x^{(t)} \right)d^{(t)}}{< d^{(t)},Ad^{(t)} >}$$

Também podemos mostrar que, tomando esse passo, o algoritmo irá convergir **exatamente** para o mínimo em apenas $n$ iterações

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md#apresentacao-original)

- Anterior: [Método de Newton](../metodo-de-newton/index.md)
- Próximo: [Dualidade](../dualidade/index.md)
