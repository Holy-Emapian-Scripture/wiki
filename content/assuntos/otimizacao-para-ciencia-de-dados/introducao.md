---
layout: "default"
title: "Introdução"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A2.md"
trilha: "../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 1
---

[Otimização para Ciência de Dados](index.md)

<!-- wiki:original:inicio -->
<a id="secao-1"></a>

# Introdução

------------------------------------------------------------------------

Antes de iniciarmos com o conteúdo de verdade, vou relembrar alguns conceitos importantes da A1 que vão ajudar a entender os métodos presentes nesse PDF.

<a id="first-order-approximation"></a>

**Teorema: Aproximação de Primeira Ordem**

Quando $f$ é continuamente diferenciável, em uma vizinhança de um ponto $x$ podemos mostrar que: $$\forall d \in {\mathbb{R}}^{n}\text{ com }\| d\| = 1\text{\quad\quad}\ \frac{df}{dd} = \nabla{f(x)}^{T}d$$ e, além disso, temos: $$\forall y \in {\mathbb{R}}^{n}\text{ na vizinhança }\text{\quad\quad}f(y) = f(x) + \nabla{f(x)}^{T}(y - x) + o\left( \| y - x\| \right)$$ Onde $o:{\mathbb{R}}_{+} \rightarrow {\mathbb{R}}$ satisfaz $\lim\limits_{t \rightarrow 0^{+}}\frac{o(t)}{t} = 0$

<a id="linear-approximation"></a>

**Teorema: Aproximação Linear**

Seja $f:U \rightarrow {\mathbb{R}}$ uma função duas vezes continuamente diferenciável e $U \subseteq {\mathbb{R}}^{n}$, e seja $x \in U$ e $r > 0$ tais que $B(x,r) \subset U$ então: $$\begin{array}{r} \forall y \in B(x,r)\ \exists\xi \in \lbrack x,y\rbrack\text{ tal que } \\ f(y) = f(x) + \nabla{f(x)}^{T}(y - x) + \frac{1}{2}(y - x)^{T}\nabla^{2}f(\xi)(y - x) \end{array}$$

<a id="second-order-approximation"></a>

**Teorema: Aproximação de Segunda Ordem**

Seja $f:U \rightarrow {\mathbb{R}}$ uma função duas vezes continuamente diferenciável e $U \subseteq {\mathbb{R}}^{n}$, e seja $x \in U$ e $r > 0$ tais que $B(x,r) \subset U$ então: $$\begin{array}{r} \forall y \in B(x,r)\text{ vale } \\ f(y) = f(x) + \nabla{f(x)}^{T}(y - x) + \frac{1}{2}(y - x)^{T}\nabla^{2}f(x)(y - x) + o\left( \| y - x\|^{2} \right) \end{array}$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../trilhas/otimizacao-para-ciencia-de-dados/a2.md) · [Apresentação e contexto da fonte](../../trilhas/otimizacao-para-ciencia-de-dados/a2.md#apresentacao-original)

- Próximo: [Método do Gradiente](metodo-do-gradiente.md)
