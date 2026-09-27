---
layout: "default"
title: "Otimização com restrições genéricas"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 16
---

[Otimização para Ciência de Dados](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-21"></a>

# Otimização com restrições genéricas


<a id="lagrangeano"></a>
<a id="secao-22"></a>

## Lagrangeano

O lagrangeando é uma função que será de grande importância, ela pode parecer meio confusa (Pois ela é), mas, a partir de agora, ela será nossa definição de “Derivar e igualar a $0$”. Como assim? Sempre que queríamos minimizar/maximizar uma função, derivávamos e igualávamos a $0$, só que vimos que, com restrições, isso não funciona mais, porém, essa função ainda se aplica (Com algumas ressalvas) no lagrangeano (Como veremos)

<a id="lagrange-function"></a>

**Definição: Lagrangeano**

O **Lagrangeano** associado à função $f$ é a função $L:{\mathbb{R}}^{n} \times {\mathbb{R}}^{m} \times {\mathbb{R}}^{p} \rightarrow {\mathbb{R}}$ tal que: $$L(x,\lambda,\mu) = f(x) + \lambda^{T}g(x) + \mu^{T}h(x)$$ Onde: $$\lambda = \begin{pmatrix} \lambda_{1} \\ \vdots \\ \lambda_{m} \end{pmatrix},\ \mu = \begin{pmatrix} \mu_{1} \\ \vdots \\ \mu_{p} \end{pmatrix},\ g(x) = \begin{pmatrix} g_{1}(x) \\ \vdots \\ g_{m}(x) \end{pmatrix},\ h(x) = \begin{pmatrix} h_{1}(x) \\ \vdots \\ h_{p}(x) \end{pmatrix}$$

**Teorema: Gradiente Lagrangeano**

Dado o Lagrangeano de uma função $f$, temos que o gradiente do lagrangeano **somente em relação a $x$** se da por: $$\nabla_{x}L(x,\lambda,\mu) = \nabla f(x) + \sum_{i = 1}^{m}\lambda_{i}\nabla g_{i}(x) + \sum_{j = 1}^{p}\mu_{j}\nabla h_{j}(x)$$

<a id="as-generalizacoes-do-kkt"></a>
<a id="secao-23"></a>

## As generalizações do KKT

Agora queremos generalizar totalmente o KKT, então vamos aos poucos. Lembre que, até que falemos o contrário, estamos considerando o problema [\[optimization-with-generic-restrictions\]](../index.md#optimization-with-generic-restrictions)

Antes de entrarmos diretamente no teorema KKT generalizado, vamos agora fazer uma definição que tem uma razão matemática, mas acaba por nos ajudar em alguns casos. Essa definição evita condições redundantes no nosso problema, ja que elas podem acabar nos atrapalhando. Faremos um exemplo para mostrar essa ajuda

<a id="licq"></a>

**Definição: Condições de qualificação de independência linear**

Sejam $g_{1},\ldots,g_{m}:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ e $h_{1},\ldots,h_{p}:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ continuamente diferenciáveis e $x^{\ast} \in {\mathbb{R}}^{n}$, defina: $$I\left( x^{\ast} \right) ≔ \left\{ i \in \lbrack m\rbrack:g_{i}\left( x^{\ast} \right) = 0 \right\}$$ Dizemos que LICQ (Linear Independent Condition Qualification) é satisfeita em $x^{\ast}$ para as funções $g_{1},\ldots,g_{m}$ e $h_{1},\ldots,h_{p}$ se $$\left\{ \nabla g_{i}\left( x^{\ast} \right):i \in I\left( x^{\ast} \right) \right\} \cup \left\{ \nabla h_{j}\left( x^{\ast} \right):j \in \lbrack p\rbrack \right\}\text{ é linearmente independente }$$

Definição feita, vamos enunciar o novo teorema KKT

<a id="generic-kkt"></a>

**Teorema: KKT**

Se $x^{\ast}$ é um ponto de mínimo local de $f(x)$ no problema [\[optimization-with-generic-restrictions\]](../index.md#optimization-with-generic-restrictions) e a [\[licq\]](#licq) é satisfeita em $x^{\ast}$, isso implica que: $$\begin{array}{r} \exists\lambda_{1},\ldots,\lambda_{m} \geq 0,\ \exists\mu_{1},\ldots,\mu_{p} \in {\mathbb{R}} \\ \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}\nabla g_{i}\left( x^{\ast} \right) + \sum_{j = 1}^{p}\mu_{j}\nabla h_{j}\left( x^{\ast} \right) = 0 \\ \lambda_{i}g_{i}\left( x^{\ast} \right) = 0\text{\quad\quad}i \in \lbrack m\rbrack \\ g_{i}\left( x^{\ast} \right) \leq 0\text{\quad\quad}i \in \lbrack m\rbrack \\ h_{j}\left( x^{\ast} \right) = 0\text{\quad\quad}j \in \lbrack p\rbrack \end{array}$$

**Exemplo: Utilidade da LICQ**

aaaaaaaaaaa preencher aqui aaaaaaaaaaaaa

Agora que vimos esses teoremas e condições, vamos fazer uma definição para facilitar em algumas terminologias:

**Definição: Ponto KKT**

Considere o problema [\[optimization-with-generic-restrictions\]](../index.md#optimization-with-generic-restrictions), onde $f$, $g_{1}$, …, $g_{m}$, $h_{1}$, …, $h_{p}$ são continuamente diferenciáveis no ${\mathbb{R}}^{n}$. Um ponto $x^{\ast}$ viável, ou seja, que satisfaz as condições do cojunto viável, é chamado de **ponto KKT** quando $\exists\lambda_{1},\ldots,\lambda_{m} \geq 0$ e $\exists\mu_{1},\ldots,\mu_{p} \in {\mathbb{R}}$ tais que: $$\begin{aligned} \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}\nabla g_{i}\left( x^{\ast} \right) + \sum_{j = 1}^{p}\mu_{j}\nabla h_{j}\left( x^{\ast} \right) & = 0 \\ \lambda_{i}g_{i\left( x^{\ast} \right)} & = 0\text{\quad\quad}i \in \lbrack m\rbrack \end{aligned}$$

Isso facilita um pouco a terminologia pois podemos resumir o [\[generic-kkt\]](#generic-kkt) em dizer que um ponto de LICQ não pode ser um ponto de mínimo se ele não for KKT

<a id="caso-convexo"></a>
<a id="secao-24"></a>

## Caso Convexo

Claro, não poderíamos de falar do caso convexo aqui, sempre tem algo de especial nele, vamos então enunciar novamente o nosso problema mudando ele um pouco $$\begin{array}{r} \min\limits_{x}f(x) \\ g_{i}(x) \leq 0,\ \forall i = 1,\ldots,m \\ h_{j}(x) = 0,\ \forall j = 1,\ldots,p \\ \text{onde }f,\ g_{i}\text{  e  }h_{j}\text{ são convexas }\forall i\text{  e  }\forall j \end{array}$$<a id="optimization-with-generic-convex-restrictions"></a>

Vale ressaltar também que $h_{j}$ são **afins**

**Teorema: KKT Convexo**

Se $x^{\ast}$ é um ponto de mínimo local de $f$ dado o problema [\[optimization-with-generic-convex-restrictions\]](#optimization-with-generic-convex-restrictions) e a [\[licq\]](../as-generalizacoes-do-kkt/index.md#licq) é satisfeita em $x^{\ast}$, então $x^{\ast}$ é uma solução do problema se, e somente se: $$\begin{array}{r} \exists\lambda_{1},\ldots,\lambda_{m} \geq 0,\ \exists\mu_{1},\ldots,\mu_{p} \in {\mathbb{R}} \\ \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}\nabla g_{i}\left( x^{\ast} \right) + \sum_{j = 1}^{p}\mu_{j}\nabla h_{j}\left( x^{\ast} \right) = 0 \\ \lambda_{i}g_{i}\left( x^{\ast} \right) = 0\text{\quad\quad}i \in \lbrack m\rbrack \\ g_{i}\left( x^{\ast} \right) \leq 0\text{\quad\quad}i \in \lbrack m\rbrack \\ h_{j}\left( x^{\ast} \right) = 0\text{\quad\quad}j \in \lbrack p\rbrack \end{array}$$

Show! Inclusive, por conta que o nosso problema é convexo, podemos trocar a necessidade do LICQ ([\[licq\]](../as-generalizacoes-do-kkt/index.md#licq)) por uma condição um pouco mais fácil

<a id="slater-condition"></a>

**Definição: Condição de Slater**

Dizemos que a condição de Slater é satisfeita para as funções $g_{1},\ldots,g_{m}$ (convexas) se $$\exists\hat{x} \in {\mathbb{R}}^{n}\ /\ g_{i}\left( \hat{x} \right) < 0,\ \forall i \in \lbrack m\rbrack$$

Ou seja, essa condição é satisfeita quando $x^{\ast}$ é um ponto viável (Dentro do conjunto viável). Agora podemos refazer o teorema utilizando dessa condição

<a id="kkt-and-slater"></a>

**Teorema: KKT e Slater**

Se $x^{\ast}$ é mínimo local de $f(x)$ (Nas restrições $g_{i}(x) \leq 0$ e $h_{j}(x) = 0$ sendo funções continuamente diferenciáveis e convexas) e $x^{\ast}$ satisfaz [\[slater-condition\]](#slater-condition), então $x^{\ast}$ é ponto KKT (A volta não vale)

Porém, como falei anteriormente, não faz sentido falarmos de funções convexas de igualdade ($h_{j}(x) = 0$) que **não são afins**, isso nos permite reescrever o problema de uma forma interessante: $$\begin{array}{r} \min\limits_{x}f(x) \\ g_{i}(x) \leq 0\text{\quad\quad}i \in \lbrack m\rbrack \\ h_{j}(x) = 0\text{\quad\quad}j \in \lbrack p\rbrack \\ s_{k}(x) = 0\text{\quad\quad}k \in \lbrack q\rbrack \\ \text{Onde }f,\ g_{i}\text{ são convexas e }h_{j},\ s_{k}\text{ são afins } \end{array}$$<a id="optimization-with-linear-and-generic-conditions"></a>

Então podemos adaptar a condição de slater:

**Teorema: Condição de Slater**

Dizemos que a condição de Slater é satisfeita para as funções $g_{1},\ldots,g_{m}$ (convexas) e $h_{1},\ldots,h_{p}$ e $s_{1},\ldots,s_{q}$ (afins) quando: $$\begin{array}{r} \exists\hat{x} \in {\mathbb{R}}^{n}\text{ tal que } \\ g_{i}\left( \hat{x} \right) < 0,\ \forall i \in \lbrack m\rbrack \\ h_{j}\left( \hat{x} \right) \leq 0,\ \forall j \in \lbrack p\rbrack \\ s_{k}\left( \hat{x} \right) = 0,\ \forall k \in \lbrack q\rbrack \end{array}$$

De forma que o [\[kkt-and-slater\]](#kkt-and-slater) continua valendo. Vimos 3 tipos de condições diferentes! Que tal a gente refazer o nosso teorema de uma forma geral?

**Teorema: Final KKT**

Dado o problema [\[optimization-with-generic-restrictions\]](../index.md#optimization-with-generic-restrictions), e seja $x^{\ast} \in C$ (Conjunto viável), temos 3 caracterizações:

1.  As restrições em $x^{\ast}$ são LICQ

2.  Problema convexo [\[optimization-with-generic-convex-restrictions\]](#optimization-with-generic-convex-restrictions) + Condição de slater ([\[slater-condition\]](#slater-condition))

Se $x^{\ast}$ ou o problema satisfaz qualquer uma dessas condições, então eu posso dividir meu problema em algumas condições:

- (Necessidade com qualificação de restrições)

  - Se $x^{\ast}$ é um mínimo local e as restrições ativas em $x^{\ast}$ satisfazem LICQ $\Rightarrow$ $x^{\ast}$ é um ponto KKT

- (Convexidade $+$ Slater)

  - $x^{\ast}$ é KKT (Ser mínimo $\Rightarrow$ KKT)

  - Reciprocamente, se $x^{\ast}$ é viável e é KKT, então $x^{\ast}$ é ótimo global

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Otimização com restrições lineares](../otimizacao-com-restricoes-lineares/index.md)
- Próximo: [Algoritmos de Otimização](../algoritmos-de-otimizacao/index.md)
