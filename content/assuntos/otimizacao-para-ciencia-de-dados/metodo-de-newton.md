---
layout: "default"
title: "Método de Newton"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A2.md"
trilha: "../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 9
---

[Otimização para Ciência de Dados](index.md)

<!-- wiki:original:inicio -->
<a id="secao-9"></a>

# Método de Newton

------------------------------------------------------------------------

Até agora, vimos métodos que utilizam de aproximações de primeira ordem das funções, porém, e se tentarmos utilizar mais informações além dessas? E se a função que estamos trabalhando for diferenciável duas vezes? Será que não poderiamos usar sua **Hessiana** para auxiliar? Lembra no primeiro resumo que falamos, inutitivamente, como a Hessiana carrega informações sobre para quais lados a função cresce e decresce? Poderíamos tentar utilizar essas informações! Vamos tentar aplicar uma fórmula recursiva igual fizemos no último? $$x^{(t + 1)} = \text{ argmin}_{x \in {\mathbb{R}}^{n}}\left\{ f\left( x^{(t)} \right) + \left( x - x^{(t)} \right)^{T}\nabla f\left( x^{(t)} \right) + \frac{1}{2}\left( x - x^{(t)} \right)^{T}\nabla^{2}f\left( x^{(t)} \right)\left( x - x^{(t)} \right) \right\}$$

onde aqui utilizamos a [aproximação de segunda ordem](introducao.md#second-order-approximation). Aqui, estamos assumindo algumas coisas:

- $\nabla^{2}f(x) \succ 0\ \forall x$

- $\nabla^{2}f(x)$ é $L$-Lipschitz, ou seja: $\|\nabla^{2}f(x) - \nabla^{2}f(y)\| < L\| x - y\|\ \forall x,y$

Como resultado dessa operação, obtemos: $$x^{(t + 1)} = x^{(t)} - \alpha^{(t)}\left( \nabla^{2}f\left( x^{(t)} \right) \right)^{- 1}\nabla f\left( x^{(t)} \right)$$

Assim, temos:

<a id="newton-method"></a>

1.  **func** NewtonMethod($f$) {

    1.  $x^{\left\{ (1) \right\}} \in {\mathbb{R}}^{n}$

    2.  $\alpha^{(t)} \in {\mathbb{R}}$

    3.  **for** $t \in \lbrack T\rbrack$ **do** {

        1.  $x^{(t + 1)} = x^{(t)} - \alpha^{(t)}\left( \nabla^{2}f\left( x^{(t)} \right) \right)^{- 1}\nabla f\left( x^{(t)} \right)$

    4.  }

    5.  **return** $x^{(T)}$

2.  }

*Figura 7. Método de Newton*

Por conta da “adição” de informações ao método convencional, esse método costuma convergir **MUITO** mais rápido que os já vistos anteriormente. Porém, ele não tem uma garantia **global** de convergência. Como assim? Os métodos anteriores, independente de qual fosse o ponto inicial $x^{(0)}$, convergiam para uma solução local, porém, dependendo do ponto que iniciarmos o método de newton, ele pode **divergir**.

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../trilhas/otimizacao-para-ciencia-de-dados/a2.md) · [Apresentação e contexto da fonte](../../trilhas/otimizacao-para-ciencia-de-dados/a2.md#apresentacao-original)

- Anterior: [Gradiente Proximal](gradiente-proximal.md)
- Próximo: [Gradiente Conjugado](gradiente-conjugado.md)
