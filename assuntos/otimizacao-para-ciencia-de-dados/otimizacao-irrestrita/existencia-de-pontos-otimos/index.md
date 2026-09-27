---
layout: "default"
title: "Existência de pontos ótimos — Otimização Irrestrita"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 6
---

[Otimização para Ciência de Dados](../../index.md) · [Otimização Irrestrita](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-6"></a>

# Existência de pontos ótimos

Até agora estávamos assumindo que pontos ótimos existiam, mas e se eles não existem?

**Definição: Conjunto fechado**

Um conjunto $C$ é fechado se seu complementar $C^{c}$ é aberto

**Definição: Conjunto limitado**

Um conjunto $C$ é limitado se $\exists r > 0$ tal que $C \subset B(0,r)$

**Definição: Conjunto compacto**

Um conjunto $C$ é compacto se é fechado e limitado

**Teorema: Weierstrass**

Seja $C \subset {\mathbb{R}}^{n}$ um conjunto compacto e $f:C \rightarrow {\mathbb{R}}$, então $f$ possui um ponto de mínimo global e de máximo global em $C$

Quando o conjunto não é compacto, o teorema de Weierstrass não garante a existência, então podemos usar essa outra definição:

**Definição: Coercividade**

Seja $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$. A função é dita coerciva se: $$\lim\limits_{\| x\| \rightarrow \infty}f(x) = \infty$$

Ou seja, todo e qualquer vetor que eu pegar e aumentar seu tamanho, a função aumenta junto, formando o que parece uma grande bacia, onde você coloca água e ela nunca vaza

![Exemplo de função coerciva $f(x,y) = 0.1x^{2} + 0.1y^{2}$](../../assets/coercive-function.png.png)

*Figura 5. Exemplo de função coerciva $f(x,y) = 0.1x^{2} + 0.1y^{2}$*

**Teorema: Existência de soluções: Coercividade**

Seja $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ uma função contínua e coerciva e $C \subset {\mathbb{R}}^{n}$ um conjunto fechado não-vazio. Então f tem um mínimo global em C

**Demonstração**

Seja $x_{0} \in C$ um ponto arbitrário. Como f é coerciva, segue que existe $M > 0$ tal que $$f(x) > f\left( x_{0} \right)\text{ para todo }x\text{ tal que }\| x\| > M$$ Temos que $x^{\ast}$ é um ponto de mínimo global de $f$ sobre $C$. Portanto $f\left( x^{\ast} \right) \geq f\left( x_{0} \right)$. Segue da afirmação em diplay que o conjunto de mínimos globais de $f$ sobre $C$ é exatamente o conjunto de mínimos globais de $f$ sobre $C \cap B(0,M)$. O conjunto $C \cap B(0,M)$ é fechado e limitado, portanto compacto. Segue do Teorema de Weierstrass que $f$ possui ponto de mínimo global sobre $C \cap B(0,M)$, e portanto, sobre $C$ também

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Soluções Locais: Condições de segunda ordem](../solucoes-locais-condicoes-de-segunda-ordem/index.md)
- Próximo: [Condições para soluções globais](../condicoes-para-solucoes-globais/index.md)
