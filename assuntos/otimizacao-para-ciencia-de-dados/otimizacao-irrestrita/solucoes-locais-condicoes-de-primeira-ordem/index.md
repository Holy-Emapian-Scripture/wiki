---
layout: "default"
title: "Soluções Locais: Condições de primeira ordem — Otimização Irrestrita"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 4
---

[Otimização para Ciência de Dados](../../index.md) · [Otimização Irrestrita](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Soluções Locais: Condições de primeira ordem

Agora podemos começar a brincadeira. Quando falamos de condições de primeira ordem, estamos nos referindo a condições relacionadas a derivadas de primeiro grau, ou seja, funções que são continuamente diferenciáveis. Antes eu comentei que estávamos interessados em minimizar funções num conjunto $C$, porém, vamos primeiro ver sobre otimização **irrestrita**, ou seja, problemas do tipo: $$\min\limits_{x \in {\mathbb{R}}^{n}}f(x)$$

Lembram que o vetor gradiente indica a direção que minha função tá crescendo? Quando estamos procurando um mínimo local, faz sentido dizer que a função cresça pra todos os lados, correto? Então faz sentido dizer que isso vai me dar um vetor gradiente $0$ (Apenas uma intuição)

**Teorema: Condições de primeira ordem**

Seja $f:U \rightarrow {\mathbb{R}}$ uma função definida no conjunto aberto $U \subset {\mathbb{R}}^{n}$. Se $x^{\ast} \in U$ é um mínimo local de $f$ e todas as derivadas parciais de $f$ existem, então $$\nabla f\left( x^{\ast} \right) = 0$$

**Demonstração**

Seja $i \in \lbrack n\rbrack$ e defina a função $g(t) = f(x^{\ast} + te_{i}$. Temos que $g$ é diferenciável em $0$ e $$g'(0) = \frac{\partial f}{\partial x_{i}}\left( x^{\ast} \right)$$. Sendo $x^{\ast}$ um ponto ótimo local de $f$ , segue que $0$ é um ponto ótimo local de $g$; portanto $0 = g'(0) = \frac{\partial f}{\partial x_{i}}\left( x^{\ast} \right)$. O argumento vale para todo $i \in \lbrack n\rbrack$, implicando que $\nabla f\left( x^{\ast} \right) = 0$

Esse teorema não vale na volta, já que, como vimos antes em cálculo, pontos de máximo e de sela também possuem essa característica, isso nos leva a criar a definição:

**Definição: Ponto estacionário**

Seja $f:U \rightarrow {\mathbb{R}}$ uma função definida no conjunto aberto $U \subset {\mathbb{R}}^{n}$ e todas as derivadas parciais de $f$ existem, então chamamos $x^{\ast} \in U$ de ponto estacionário de $f$ em $U$ se $$\nabla f\left( x^{\ast} \right) = 0$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Definições e Revisões de Cálculo](../definicoes-e-revisoes-de-calculo/index.md)
- Próximo: [Soluções Locais: Condições de segunda ordem](../solucoes-locais-condicoes-de-segunda-ordem/index.md)
