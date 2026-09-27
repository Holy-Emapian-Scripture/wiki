---
layout: "default"
title: "Método do Subgradiente"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A2.md"
trilha: "../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 6
---

[Otimização para Ciência de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-6"></a>

# Método do Subgradiente

------------------------------------------------------------------------

Até agora vimos um método que usa o Gradiente da função, logo, para que ele funcione, estamos assumindo que a função é diferenciável em todos os pontos, porém em aplicações reais muitas funções não são diferenciáveis em todos os pontos. Então faz sentido utilizar esse método? Claro que não, porém, podemos utilizar uma versão muito parecida!

**Definição: Subgradiente**

Seja uma função $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ e dado $x \in {\mathbb{R}}^{n}$, um vetor $g_{x} \in {\mathbb{R}}^{n}$ é chamado de **subgradiente** de $f$ em $x$ quando $$f(y) \geq f(x) + (y - x)^{T}g_{x}\text{\quad\quad}\forall y \in {\mathbb{R}}^{n}$$

**Definição: Subdiferencial**

O conjunto de todos os subgradientes de $f$ em $x$ é chamado de **subdiferencial** de $f$ em $x$ (Denotado por $\partial f(x)$) $$\partial f(x) ≔ \left\{ g_{x} \in {\mathbb{R}}^{n}:f(y) \geq f(x) + (y - x)^{T}g_{x}\ \forall y \in {\mathbb{R}}^{n} \right\}$$

O que seria um subgradiente **intuitivamente** então? Note que, se eu definir $y = x^{\ast}$ (Sendo o ponto mínimo), vamos obter o seguinte: $$f\left( x^{\ast} \right) \geq f(x) + g^{T}\left( x^{\ast} - x \right)$$ sabendo que $f\left( x^{\ast} \right) \leq f(x)$, temos que: $$f(x) \geq f(x) + g^{T}\left( x^{\ast} - x \right) \Leftrightarrow 0 \geq g^{T}\left( x^{\ast} - x \right) \Leftrightarrow 0 \leq g^{T}\left( x - x^{\ast} \right)$$

Ou seja, o subgradiente faz um ângulo **maior que $90º$** com o vetor que aponta de $x$ para $x^{\ast}$. O que isso quer dizer? Que os subgradientes são direções que, se seguirmos na **direção oposta**, nós **não** estamos indo eu uma direção em que nós temos **certeza** que ela sobe

Nem sempre existirão subgradientes, porém, quando falamos das **funções convexas**, mesmo elas não sendo **diferenciáveis**, elas possuem um subgradiente. Logo, um subgradiente é uma direção que, se eu vou na direção contrária a ela, eu tenho **certeza** que minha função não está aumentando

<a id="gradient-existence-convex"></a>

**Teorema**

Seja $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$, então vale que: $$f\text{ é convexa } \Leftrightarrow \partial f(x) \neq \varnothing\ \forall x$$

Vale ressaltar que funções subdiferenciáveis podem não ser suaves. E por que isso é importante? Acontece que antes, no método do gradiente e na direções de descida, utilizamos o fato das funções serem suaves para provar a convergência do método, porém, aqui estamos trabalhando com funções que não necessariamente são diferenciáveis, logo, intuitivamente, elas podem ter vários picos, ou paradas bruscas, etc.

<a id="subgradient-descent"></a>

1.  **func** SubgradientMethod($f$) {

    1.  $x^{(1)} \in {\mathbb{R}}^{n}$

    2.  $\left\{ \alpha^{(t)} \right\} \subset (0,\infty)$

    3.  **for** $t \in \lbrack T\rbrack$ **do** {

        1.  Compute um subgradiente $g^{(t)}$ de $f$ em $x^{(t)}$

        2.  $x^{(t + 1)} = x^{(t)} - \alpha^{(t)}g^{(t)}$

    4.  }

    5.  **return** $x^{(T)} ≔ \sum_{t = 1}^{T}\frac{\alpha^{(t)}}{\sum_{l = 1}^{T}\alpha^{(l)}}x^{(t)}$

2.  }

*Figura 4. Método do Subgradiente*

Esse algoritmo parece até que “ingênuo”, tipo, nada garante que o subgradiente vai fazer com que a função desça né?? Vamos mostrar que na verdade esse método converge sim! Porém, vamos assumir algumas coisas também. Para esse caso, vamos assumir que a função é $M$-Lipschitz ([\[m-lipschitz\]](../metodo-do-gradiente/caso-global/index.md#m-lipschitz))

Usando o que foi mostrado na introdução ([\[linear-approximation\]](../introducao/index.md#linear-approximation)), podemos mostrar o seguinte teorema:

**Teorema: Aproximação Linear de funções $M$-Lipschitz**

Seja $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ uma função convexa, então $f$ é $M$-Lipschitz contínua se, e somente se, $\forall x,y \in {\mathbb{R}}^{n}$ e todo subgradiente $g_{x} \in {\mathbb{R}}^{n}$ de $f$ em $x$: $$\vert f(y) - f(x) + g_{x}^{T}(y - x)\vert  \leq M\| y - x\|_{2}^{2}$$

E no que isso me é útil? Só parece um bando de complicação esquisita. Na verdade, o que será útil na demonstração é uma **consequência** desse teorema

**Corolário**

Seja $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ uma função convexa, então $f$ é $M$-Lipschitz se, e somente se, $\forall x \in {\mathbb{R}}^{n}$ e todo subgradiente $g_{x}$ de $f$ em $x$, vale que $\| g_{x}\|_{2} \leq M$

Vamos então mostrar a convergência do algoritmo. Um ponto interessante a se dizer é que, como você **talvez** possa ter pensado, nem sempre um subgradiente vai ser uma direção de **descida**. O que isso quer dizer? Isso quer dizer que, não necessariamente, a cada iteração, $f\left( x^{(t + 1)} \right) \leq f\left( x^{(t)} \right)$, porém, ele decresce o valor sobre a **média de todas iterações**.

**Teorema: Convergência do Subgradiente**

Suponha que $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ é $M$-Lipschitz contínua e convexa. Então: $$f\left( {\overline{x}}^{(T)} \right) - f^{\ast} \leq \frac{1}{T}\sum_{t = 1}^{T}\left( f\left( x^{(t)} \right) - f^{\ast} \right) \leq \frac{\| x^{(1)} - x^{\ast}\|_{2}^{2} + M^{2}\sum_{t = 1}^{T}\left( \alpha^{(t)} \right)^{2}}{\sum_{t = 1}^{T}\alpha^{(t)}}$$ em particular, para qualquer $\beta > 0$, consideramos: $$\alpha^{(t)} = \frac{\beta}{\sqrt{T}}\text{\quad\quad}t \in \lbrack T\rbrack$$

**Demonstração**

Primeiramente, temos que: $$\begin{aligned} \| x^{(t + 1)} - x^{\ast}\|_{2}^{2} & = \| x^{(t)} - x^{\ast} - \alpha^{(t)}g^{(t)}\|_{2}^{2} \\ & \leq \| x^{(t)} - x^{\ast}\|_{2}^{2} + 2\alpha^{(t)}\left( x - x^{\ast} \right)^{T}g^{(t)} + \left( \alpha^{(t)} \right)^{2}\| g^{(t)}\|_{2}^{2} \end{aligned}$$ e pela definição de subgradiente ($f$, por ser convexa, é garantida de ter subgradientes pelo [\[gradient-existence-convex\]](#gradient-existence-convex)), temos que: $$\left( x^{\ast} - x^{(t)} \right)^{T}g^{(t)} \leq f\left( x^{\ast} \right) - f\left( x^{(t)} \right)$$ A partir disso, também podemos escrever: $$\| x^{(t + 1)} - x^{\ast}\|_{2}^{2} \leq \| x^{(t)} - x^{\ast}\|_{2}^{2} - \alpha^{(t)}\left( f\left( x^{(t)} \right) - f^{\ast} \right) + \left( M\alpha^{(t)} \right)^{2}$$

Agora nós vamos fazer novamente a soma por recursão: $$\begin{aligned} \sum_{t = 1}^{T}\alpha^{(t)}\left( f\left( x^{(t)} \right) - f^{\ast} \right) & \leq \sum_{t = 1}^{T}\left( \| x^{(t)} - x^{\ast}\|_{2}^{2} - \| x^{(t + 1)} - x^{\ast}\|_{2}^{2} \right) + M^{2}\sum_{t = 1}^{T}\left( \alpha^{(t)} \right)^{2} \\ & \leq \| x^{(1)} - x^{\ast}\|_{2}^{2} + M^{2}\sum_{t = 1}^{T}\left( \alpha^{(t)} \right)^{2} \end{aligned}$$

Dividindo por $\sum_{t = 1}^{T}\alpha^{(t)}$ e, usando a desigualdade de Jensen $$f\left( {\overline{x}}^{(T)} \right) - f^{\ast} \leq \frac{1}{T}\sum_{t = 1}^{T}\left( f\left( x^{(t)} \right) - f^{\ast} \right) \leq \frac{\| x^{(1)} - x^{\ast}\|_{2}^{2} + M^{2}\sum_{t = 1}^{T}\left( \alpha^{(t)} \right)^{2}}{\sum_{t = 1}^{T}\alpha^{(t)}}$$ Ou seja, a média das iterações converge para próximo de $x^{\ast}$

Nós assumimos que $\alpha^{(t)}$ está em um conjunto de passos, e não que é um único passo, mas e se assumirmos que é um único, qual seria o melhor passo? Tomando $\alpha^{(t)} = \alpha$: $$f\left( {\overline{x}}^{(T)} \right) - f^{\ast} \leq \frac{\| x^{(1)} - x^{\ast}\|_{2}^{2}}{T\alpha} + M^{2}\alpha$$

perceba também que: $$\min\limits_{\alpha > 0}\left\{ \frac{\| x^{(1)} - x^{\ast}\|_{2}^{2}}{T\alpha} + M^{2}\alpha \right\} = \frac{M\| x^{(1)} - x^{\ast}\|_{2}}{\sqrt{T}}$$

logo, temos que: $$\alpha^{(t)} = \frac{\| x^{(1)} - x^{\ast}\|_{2}}{M\sqrt{T}}$$

então teremos a taxa de convergência: $$f\left( {\overline{x}}^{(T)} \right) - f^{\ast} \leq \frac{2M\| x^{(1)} - x^{\ast}\|_{2}}{\sqrt{T}}$$

Porém, na maioria esmagadora das vezes, não sabemos $M$ e $\| x^{(1)} - x^{\ast}\|$, então utilizamos o passo sequencial já definido anteriormente.

Como vimos antes, também conseguimos uma fórmula recursiva para o método do subgradiente, assim como para o do gradiente $$x^{(t + 1)} = \text{ argmin}_{x \in {\mathbb{R}}^{n}}\left\{ f\left( x^{(t)} \right) + < x - x^{(t)},g^{(t)} > + 1/\left( 2\alpha^{(t)} \right) \cdot \| x - x^{(t)}\|_{2}^{2} \right\}$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md#apresentacao-original)

- Anterior: [Método do Gradiente](../metodo-do-gradiente/index.md)
- Próximo: [Gradiente Projetado](../gradiente-projetado/index.md)
