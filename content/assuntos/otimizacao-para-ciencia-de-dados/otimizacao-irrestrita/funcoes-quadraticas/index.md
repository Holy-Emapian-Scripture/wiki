---
layout: "default"
title: "Funções quadráticas — Otimização Irrestrita"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 8
---

[Otimização para Ciência de Dados](../../index.md) · [Otimização Irrestrita](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-8"></a>

# Funções quadráticas

Um conjunto interessante de funções com algumas propriedades convenientes são as funções quadráticas

<a id="quadratic-function"></a>

**Definição: Função quadrática**

Uma função é quadrática quando $\exists A \in {\mathbb{R}}^{n \times n}\text{ simétrica},b \in {\mathbb{R}}^{n},c \in {\mathbb{R}}$ tal que a função $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ pode ser expressa como: $$f(x) = x^{T}Ax + 2b^{T}x + c$$

**Teorema: Derivadas de uma quadrática**

Seja $f$ uma função quadrática como na [\[quadratic-function\]](#quadratic-function), temos que: $$\begin{array}{r} \nabla f(x) = 2(Ax + b) \\ \nabla^{2}f(x) = 2A \end{array}$$

**Demonstração**

Sabemos que $f(x) = x^{T}Ax + 2b^{T}x + c$. Vamos definir que $x_{i}$ é a $i$-ésima entrada de $x$. Vamos primeiro calcular uma derivada parcial genérica de $f$. Como a derivada é uma operação linear, eu vou ver cada componente separadamente. $$x^{T}Ax = \begin{pmatrix} x_{1} & \ldots & x_{n} \end{pmatrix}\begin{pmatrix} a_{11} & \ldots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{n1} & \ldots & a_{nn} \end{pmatrix}\begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix} = \begin{pmatrix} x_{1} & \ldots & x_{n} \end{pmatrix}\begin{pmatrix} \sum_{k = 1}^{n}a_{1k}x_{k} \\ \vdots \\ \sum_{k = 1}^{n}a_{nk}x_{k} \end{pmatrix}$$

Para facilitar nossa vida, vamos definir $$\alpha_{j} = \sum_{k = 1}^{n}a_{jk}x_{k}$$. Então: $$f(x) = \alpha_{1}x_{1} + \ldots + \alpha_{n}x_{n} + 2\left( b_{1}x_{1} + \ldots + b_{n}x_{n} \right) + c$$ Agora podemos tirar a derivada de $f(x)$ em $x_{j}$, mas antes, perceba que: $$\frac{\partial\alpha_{i}}{\partial x_{j}} = a_{ij}$$ Agora sim: $$\frac{\partial f}{\partial x_{j}} = x_{1}\frac{\partial\alpha_{1}}{\partial x_{j}} + \ldots + \frac{\partial}{\partial x_{j}}\left( \alpha_{j}x_{j} \right) + \ldots + x_{n}\frac{\partial\alpha_{n}}{\partial x_{j}} + 2b_{j}\frac{\begin{array}{r} \\ (\partial f) \end{array}}{\partial x_{j}} = x_{1}a_{1j} + \ldots + \frac{\partial\alpha_{j}}{\partial x_{j}}x_{j} + \alpha_{j} + \ldots + x_{n}a_{nj} + 2b_{j}\frac{\begin{array}{r} \\ (\partial f) \end{array}}{\partial x_{j}} = \sum_{k = 1}^{n}a_{jk}x_{k} + \sum_{k = 1}^{n}a_{kj}x_{k} + 2b_{j}$$

Como $A$ é simétrica, podemos reescrever isso como: $$\frac{\partial f}{\partial x_{j}} = 2\left( \sum_{k = 1}^{n}a_{kj}x_{k} + b_{j} \right)$$

Ou seja, o gradiente da função é: $$\nabla f(x) = 2(Ax + b)$$

E para a hessiana é bem mais fácil, dado o item anterior, basta que tiremos a derivada novamente para $x_{i}$: $$\frac{\partial^{2}f}{\partial x_{j}\partial x_{i}} = 2a_{ij}$$ Ou seja: $$\nabla^{2}f(x) = 2A$$

**Teorema: Pontos estacionários e ótimos de função quadrática**

Seja uma função $f$ definida na [\[quadratic-function\]](#quadratic-function), então:

1.  $x$ é ponto estacionário $\Leftrightarrow Ax = - b$.

2.  Suponha que $A \succeq 0$. Então $x$ é ponto de mínimo global $\Leftrightarrow Ax = - b$.

3.  Suponha que $A \succ 0$. Então $x = - A^{- 1}b$ é ponto de mínimo global estrito.

**Demonstração**

1.  Segue imediatamente da fórmula do gradiente.

2.  Suponha que $A \succeq 0$. Da f́ormula da Hessiana, segue que $\nabla^{2}f(x) \succeq 0\ \forall x \in {\mathbb{R}}^{n}$. O resultado segue então do [\[sufficient-condition-global-minimum\]](../condicoes-para-solucoes-globais/index.md#sufficient-condition-global-minimum) e item 1.

3.  Suponha que $A \succ 0$. Então $x = - A^{- 1}b$ é a única solução de $Ax = - b$. Segue do item (ii) que $x = - A^{- 1}b$ é o único ponto de mínimo global de $f$ e, portanto, mínimo global estrito.

**Teorema: Coercividade de funções quadráticas**

Seja função $f$ definida como na [\[quadratic-function\]](#quadratic-function). Então $f$ é coerciva $\Leftrightarrow A \succ 0$.

**Demonstração**

Precisamos do seguinte lema: Seja $A \in {\mathbb{R}}^{n \times n}$ simétrica, então $\forall x \neq 0 \in {\mathbb{R}}^{n \times n}$ $$\lambda_{\text{min }}(A) \leq \frac{x^{T}Ax}{\| x\|^{2}} \leq \lambda_{\text{max }}(A)$$ (Pode-se demonstrar pelo teorema espectral)

Agora podemos começar a prova:

$( \Longleftarrow )$ Suponha que $A \succ 0$. Denote $\alpha ≔ \lambda_{\text{min }}(A)$. Pelo lema àcima e Cauchy-Schwarz, segue que, para todo $x \in {\mathbb{R}}^{n}$, $$f(x) = x^{T}Ax + 2b^{T}x + c \geq \alpha\| x\|^{2} - 2\| b\|\| x\| + c$$ Segue que $f(x) \rightarrow \infty$ quando $\| x\| \rightarrow \infty$; isto é, $f$ é coerciva.

$( \Longrightarrow )$ Suponha que $f$ é coerciva. Suponha que $A$ tenha auto-valores negativos. Portanto, existem $v \neq 0$ e $\lambda < 0$ tais que $Av = \lambda v$. Portanto, para todo $\alpha \in {\mathbb{R}}$, $$f(\alpha v) = \lambda\| v\|^{2}\alpha^{2} + 2\left( b^{T}v \right)\alpha + c \rightarrow \infty\text{ quando }\alpha \rightarrow \infty$$

Isto contradiz a hipótese de coercividade. Portanto, A possui todos auto-valores não-negativos. Provaremos agora que $0$ não é auto-valor de $A$, provando que $A \succ 0$. Assuma que exista $v\not{} = 0$ tal que $Av = 0$. Então, para todo $\alpha \in {\mathbb{R}}$, $$f(\alpha v) = 2\left( b^{T}v \right)\alpha + c.$$ Temos que: $$f(\alpha v) \rightarrow \begin{cases} c\text{ quando }\alpha \rightarrow \infty\text{ se }b^{T}v = 0 \\ - \infty\text{ quando }\alpha \rightarrow - \infty\text{ se }b^{T}v > 0 \\ \infty\text{ quando }\alpha \rightarrow \infty\text{ se }b^{T}v < 0 \end{cases}$$ Em qualquer caso a coerção é violada, portanto, $0$ não pode ser autovalor de $A$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Condições para soluções globais](../condicoes-para-solucoes-globais/index.md)
- Próximo: [Otimização Convexa](../../otimizacao-convexa/index.md)
