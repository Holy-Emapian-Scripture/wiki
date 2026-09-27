---
layout: "default"
title: "Definições e Revisões de Cálculo — Otimização Irrestrita"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 3
---

[Otimização para Ciência de Dados](../../index.md) · [Otimização Irrestrita](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-3"></a>

# Definições e Revisões de Cálculo

Nesse capítulo, vamos rever alguns conceitos de cálculo e introduzir a otimização irrestrita, onde queremos trabalhar em uma função $f$ sem nenhuma restrição

**Definição: Ponto de Mínimo**

Seja $f:C \subseteq {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$

- $x^{\ast} \in C$ é um **ponto de mínimo global** de $f$ em $C \Leftrightarrow$ $$\forall x \in C,\text{       }f\left( x^{\ast} \right) \leq f(x)$$

- $x^{\ast} \in C$ é um **ponto de mínimo global estrito** de $f$ em $C \Leftrightarrow$ $$\forall x \in C,\text{       }f\left( x^{\ast} \right) < f(x)$$

- $x^{\ast} \in C$ é um **ponto de mínimo local** de $f$ em $C \Leftrightarrow$ $$\exists r > 0 \land \forall x \in C \cap B\left( x^{\ast},r \right),\text{       }f\left( x^{\ast} \right) \leq f(x)$$

- $x^{\ast} \in C$ é um **ponto de mínimo local estrito** de $f$ em $C \Leftrightarrow$ $$\exists r > 0 \land \forall x \in C \cap B\left( x^{\ast},r \right)\backslash\left\{ x^{\ast} \right\},\text{       }f\left( x^{\ast} \right) < f(x)$$

**Definição: Bola**

Uma bola $B \subset {\mathbb{R}}^{n}$ de raio $r > 0 \in {\mathbb{R}}$ e centro $p \in {\mathbb{R}}^{n}$ é o conjunto: $$B(p,r) = \left\{ x \in {\mathbb{R}}/\| x - p\| \leq r \right\}$$

Ou seja, qual é a diferença dos dois? Pontos de mínimo globais são menores que todo e qualquer outro ponto no domínio $C$ da função, enquanto os pontos locais são os menores em uma determinada vizinhança, a partir do ponto de mínimo local em questão, qualquer direção que eu tomar eu vou começar a subir o valor de $f$, mesmo que existam pontos em outros locais do domínio que sejam menores que o ponto de mínimo local que eu estava analisando

Agora vamos lembrar algumas coisas que vimos em cálculo (Alguns teoremas que são apenas revisão não serão demonstrados)

**Definição: Derivada direcional**

Dada $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ e $d \neq 0 \in {\mathbb{R}}^{n}$ e $\| d\| = 1$. Se $$\exists\lim\limits_{t \rightarrow 0^{+}}\frac{f(x + td) - f(x)}{t}$$ Isso é chamado de derivada direcional de $f$ na direção $d$ ($\frac{df}{dd}$)

**Definição: Gradiente**

Dada $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ e $\exists\frac{\partial f}{\partial x_{i}}$, $i = 1,\ldots,n$, o vetor gradiente de $f$ é definido como: $$\nabla f(x) = \begin{pmatrix} \frac{\partial f}{\partial x_{1}} \\ \frac{\partial f}{\partial x_{2}} \\ \vdots \\ \frac{\partial f}{\partial x_{n}} \end{pmatrix}$$

**Definição: Continuamente Diferenciável**

Uma função $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ é continuamente diferenciável se: $$\forall x \in {\mathbb{R}}^{n},\ \exists\frac{\partial f}{\partial x_{i}}(x)$$ e $\frac{\partial f}{\partial x_{i}}$ são contínuas $\forall i$

**Teorema: Aproximação de Primeira Ordem**

Quando $f$ é continuamente diferenciável, em uma vizinhança de um ponto $x$ podemos mostrar que: $$\forall d \in {\mathbb{R}}^{n}\text{ com }\| d\| = 1\text{\quad\quad}\ \frac{df}{dd} = \nabla{f(x)}^{T}d$$ e, além disso, temos: $$\forall y \in {\mathbb{R}}^{n}\text{ na vizinhança }\text{\quad\quad}f(y) = f(x) + \nabla{f(x)}^{T}(y - x) + o\left( \| y - x\| \right)$$ Onde $o:{\mathbb{R}}_{+} \rightarrow {\mathbb{R}}$ satisfaz $\lim\limits_{t \rightarrow 0^{+}}\frac{o(t)}{t} = 0$

Apenas para relembrar, esse teorema está nos dando uma forma de aproximar uma função:

![Função $f(x,y) = \frac{x + y}{x^{2} + y^{2} + 1/5}$](../../assets/function-example-1.png)

*Figura 1. Função $f(x,y) = \frac{x + y}{x^{2} + y^{2} + 1/5}$*

Perceba que, próximo do ponto, a distância entre os pontos da curva e os do plano não são tão grandes, por isso que definimos a aproximação linear como mostrado anteriormente

**Definição: Funções duas vezes continuamente diferenciáveis**

Podemos também expressar uma definição similar para uma função $f:C \rightarrow R$<!-- Expressão matemática vazia no original. --> definida num conjunto $C \subset {\mathbb{R}}^{n}$. Dizemos que $f:C \rightarrow R$<!-- Expressão matemática vazia no original. --> é duas continuamente diferenciável em $C$ se existe $U \supset C$ conjunto aberto tal que existem todas derivadas parciais de primeira e segunda ordem em todo ponto $x \in U$ e, além disso, as funções $\frac{\partial^{2}f}{\partial x_{i}\partial x_{j}}:U \rightarrow {\mathbb{R}}$ são contínuas

**Definição: Matriz Hessiana**

Seja $f:U \rightarrow {\mathbb{R}}$ com $U \subset {\mathbb{R}}$ e duas vezes continuamente diferenciável, a matriz hessiana de $f$ no ponto $x \in U$ é definida como: $$\nabla^{2}f(x) ≔ \begin{pmatrix} \frac{\partial^{2}f}{\partial x_{1}^{2}} & \frac{\partial^{2}f}{\partial x_{1}\partial x_{2}} & \ldots & \frac{\partial^{2}f}{\partial x_{1}\partial x_{n}} \\ \frac{\partial^{2}f}{\partial x_{2}\partial x_{1}} & \frac{\partial^{2}f}{\partial x_{2}^{2}} & \ddots & \vdots \\ \vdots \\ \frac{\partial^{2}f}{\partial x_{n}\partial x_{1}} & \frac{\partial^{2}f}{\partial x_{n}\partial x_{2}} & \ldots & \frac{\partial^{2}f}{\partial x_{n}^{2}} \end{pmatrix}$$

Perceba que $\nabla^{2}f(x)$ é simétrica

<a id="linear-approximation"></a>

**Teorema: Aproximação Linear**

Seja $f:U \rightarrow {\mathbb{R}}$ uma função duas vezes continuamente diferenciável e $U \subseteq {\mathbb{R}}^{n}$, e seja $x \in U$ e $r > 0$ tais que $B(x,r) \subset U$ então: $$\begin{array}{r} \forall y \in B(x,r)\ \exists\xi \in \lbrack x,y\rbrack\text{ tal que } \\ f(y) = f(x) + \nabla{f(x)}^{T}(y - x) + \frac{1}{2}(y - x)^{T}\nabla^{2}f(\xi)(y - x) \end{array}$$

<a id="second-order-approximation"></a>

**Teorema: Aproximação de Segunda Ordem**

Seja $f:U \rightarrow {\mathbb{R}}$ uma função duas vezes continuamente diferenciável e $U \subseteq {\mathbb{R}}^{n}$, e seja $x \in U$ e $r > 0$ tais que $B(x,r) \subset U$ então: $$\begin{array}{r} \forall y \in B(x,r)\text{ vale } \\ f(y) = f(x) + \nabla{f(x)}^{T}(y - x) + \frac{1}{2}(y - x)^{T}\nabla^{2}f(x)(y - x) + o\left( \| y - x\|^{2} \right) \end{array}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Introdução](../introducao/index.md)
- Próximo: [Soluções Locais: Condições de primeira ordem](../solucoes-locais-condicoes-de-primeira-ordem/index.md)
