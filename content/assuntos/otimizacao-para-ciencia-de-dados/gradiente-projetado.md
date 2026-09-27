---
layout: "default"
title: "Gradiente Projetado"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A2.md"
trilha: "../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 7
---

[Otimização para Ciência de Dados](index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# Gradiente Projetado

------------------------------------------------------------------------

Certo, perceba que, até o momento, nós utilizamos algoritmos aplicados apenas em funções em TODO o plano ${\mathbb{R}}^{n}$, mas e se, como em muitos casos, temos um conjunto limitado? Agora vamos considerar o seguinte problema de otimização $$\min\limits_{x \in C}f(x)$$ para funções $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ e o conjunto viável $C \subset {\mathbb{R}}^{n}$ **convexo** e vamos assumir também que $f$ tem gradientes ou pelo menos subgradientes em qualquer ponto. A gente viu a forma recursiva nos problemas anteriores, que tal a gente tentar aplicar aqui? Só que em vez de fazer no ${\mathbb{R}}^{n}$, nós fazemos em $C$? $$x^{(t + 1)} = \text{ argmin}_{x \in C}\left\{ f\left( x^{(t)} \right) + < x - x^{(t)},g^{(t)} > + \frac{1}{2\alpha^{(t)}}\| x - x^{(t)}\|_{2}^{2} \right\}$$

Podemos mostrar que essa fórmula é equivalente a $$x^{(t + 1)} = \text{ argmin}_{x \in C}\| x - \left( x^{(t)} - \alpha^{(t)}g^{(t)} \right)\|_{2}^{2}$$

Só que perceba que isso é equivalente a **projetar ortogonalmente** $x^{(t)} - \alpha^{(t)}g^{(t)}$ em $C$, então concluímos que: $$x^{(t + 1)} = \Pi_{x \in C}\left\lbrack x^{(t)} - \alpha^{(t)}g^{(t)} \right\rbrack$$

de forma que $\Pi$ é o projetor ortogonal a $C$. Então temos o seguinte algoritmo:

<a id="projected-gradient"></a>

1.  **func** SubgradientMethod($f$) {

    1.  $x^{(1)} \in {\mathbb{R}}^{n}$

    2.  $\left\{ \alpha^{(t)} \right\} \subset (0,\infty)$

    3.  **for** $t \in \lbrack T\rbrack$ **do** {

        1.  Compute um subgradiente $g^{(t)}$ de $f$ em $x^{(t)}$

        2.  $z^{(t + 1)} = x^{(t)} - \alpha^{(t)}g^{(t)}$

        3.  $x^{(t + 1)} = \Pi_{x \in C}\left\lbrack z^{(t + 1)} \right\rbrack$

    4.  }

    5.  **return** $x^{(T)} ≔ \frac{\sum_{t = 1}^{T}\alpha^{(t)}x^{(t)}}{\sum_{l = 1}^{T}\alpha^{(l)}}$

2.  }

*Figura 5. Método do Subgradiente Projetado*

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../trilhas/otimizacao-para-ciencia-de-dados/a2.md) · [Apresentação e contexto da fonte](../../trilhas/otimizacao-para-ciencia-de-dados/a2.md#apresentacao-original)

- Anterior: [Método do Subgradiente](metodo-do-subgradiente.md)
- Próximo: [Gradiente Proximal](gradiente-proximal.md)
