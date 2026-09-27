---
layout: "default"
title: "Algoritmos de Otimização"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 20
---

[Otimização para Ciência de Dados](index.md)

<!-- wiki:original:inicio -->

<a id="secao-25"></a>

# Algoritmos de Otimização


<a id="metodo-gradiente"></a>
<a id="secao-26"></a>

## Método Gradiente

Vamos definir o algoritmo do gradiente

1.  $x_{1}$ inicial

2.  **for** $t = 1,\ldots,n$ **do**:

    1.  $x_{t + 1} = x_{t} - \alpha_{t}\nabla f\left( x_{t} \right)$

Onde $\alpha_{t} > 0$ é o “passo” ou learning rate. Vamos agora fazer algumas definições para mostrar o porquê do método do gradiente funcionar

**Definição: Suavidade**

Dizemos que $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ é uma função $L$-suave se $\exists L > 0$ tal que: $$\forall x,y,\ \|\nabla f(x) - \nabla f(y)\| \leq L\| x - y\|$$ Ou, equivalentemente $$\|\nabla f(x) - \nabla f(y)\| \leq O\left( \| x - y\| \right)$$

**Definição: Direção de Descida**

Dizemos que $d \in {\mathbb{R}}^{n}$ é de “descida” a partir de um ponto $x \in {\mathbb{R}}^{n}$ se: $$\left( \nabla f(x) \right)^{T}d < 0$$

**Teorema: Suavidade**

$\forall x,y \in {\mathbb{R}}^{n}$ vale que: $$f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}\text{ é L-suave } \Leftrightarrow f(y) \leq f(x) + \nabla{f(x)}^{T}(y - x) + \frac{L}{2}\| y - x\|^{2}$$

Se $d$ é a direção de descida em $x$, então $$x^{+} ≔ x + \alpha d$$

tem que, por suavidade de f: $$\begin{aligned} f\left( x^{+} \right) - f(x) & \leq \nabla{f(x)}^{T}\left( x^{+} - x \right) + \frac{L}{2}\| x^{+} - x\|^{2} \\ & = \alpha\nabla{f(x)}^{T}d + \frac{L\alpha^{2}}{2}\| d\|^{2} \\ & = \alpha\left( \nabla{f(x)}^{T}d + \frac{L\alpha}{2}\| d\|^{2} \right) < 0 \end{aligned}$$

E temos que $$\begin{array}{r} \lim\limits_{\alpha \rightarrow 0^{+}}\left( \nabla{f(x)}^{T}d + \frac{L\alpha}{2}\| d\|^{2} \right) = \nabla{f(x)}^{T}d < 0 \\ \Rightarrow \exists\hat{\alpha} > 0\text{ tal que }\nabla{f(x)}^{T}d + \frac{L\hat{\alpha}}{2}\| d\|^{2} < 0 \end{array}$$

**Teorema**

$\forall t \in {\mathbb{N}}$ e supondo que $0 < \alpha_{t} \leq \frac{2}{L}$, então (Considerando que a direção de descida é $- \nabla f(x)$: $$\alpha_{t}\left( 1 - \frac{L\alpha_{t}}{2} \right)\|\nabla f\left( x_{t} \right)\|^{2} \leq f\left( x_{t} \right) - f\left( x_{t + 1} \right)$$

**Demonstração**

$f$ é suave: $$\begin{aligned} f\left( x_{t + 1} \right) & \leq f\left( x_{t} \right) + \nabla{f\left( x_{t} \right)}^{T}\left( x_{t + 1} - x_{t} \right) + \frac{L}{2}\| x_{t + 1} - x_{t}\|^{2} \\ & = f\left( x_{t} \right) - \alpha_{t}\| f\left( x_{t} \right)\|^{2} + \frac{L\alpha_{t}^{2}}{2}\|\nabla f\left( x_{t} \right)\|^{2} \end{aligned}$$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Caso Convexo](otimizacao-com-restricoes-genericas.md#caso-convexo)
