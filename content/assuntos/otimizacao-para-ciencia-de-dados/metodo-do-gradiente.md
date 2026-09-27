---
layout: "default"
title: "Método do Gradiente"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A2.md"
trilha: "../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 2
---

[Otimização para Ciência de Dados](index.md)

<!-- wiki:original:inicio -->

<a id="secao-2"></a>

# Método do Gradiente


<a id="caso-global"></a>
<a id="secao-3"></a>

## Caso Global

É o método de otimização mais clássico que existe! Vamos supor que queremos resolver o problema: $$\min\limits_{x \in {\mathbb{R}}^{n}}f(x)$$

Lembra do que vimos em cálculo? Que $\nabla f(x)$ é o vetor que aponta pra direção em que $f(x)$ aumenta? Então que tal a gente seguir na direção contrária a $f(x)$? Isso faz bastante sentido, e funciona! Mas deve ter um motivo mais matemático por trás, não é? Vamos primeiro mostrar o algoritmo:

<a id="gradient-descent"></a>

1.  **func** GradientDescent($f$) {

    1.  $x^{(0)} \in {\mathbb{R}}^{n}$

    2.  $\alpha > 0$

    3.  **for** $t \in \lbrack T\rbrack$ **do** {

        1.  $x^{(t + 1)} = x^{(t)} - \alpha\nabla f\left( x^{(t)} \right)$

    4.  }

    5.  **return** $x^{(T)}$

2.  }

*Figura 1. Gradient Descent*

Antes de entender um motivo mais matemático por trás do algoritmo, vamos ver algumas definições

<a id="m-lipschitz"></a>

**Definição: Funções $M$-Lipschitz**

Dizemos que uma função $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{m}$ é $M$-Lipschitz quando: $$\| f(x) - f(y)\| \leq M\| x - y\|\text{\quad\quad}\forall x,y \in {\mathbb{R}}^{n}$$

<a id="l-suave"></a>

**Definição: Função $L$-Suave**

Uma função $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ é $L$-suave quando seu gradiente é $L$-Lipschitz: $$\|\nabla f(x) - \nabla f(y)\| \leq L\| x - y\|\text{\quad\quad}\forall x,y \in {\mathbb{R}}^{n}$$

Essa definição de suavidade tem uma interpretação, imagine que, se eu estou na posição $x$ e vou pra posição $y$, a variação que eu vou ter na função, dentro dessa passada, não ultrapassa o quanto eu andei vezes uma constante $L$. Então funções muito onduladas, e com ondulações

![Função bem desregular, mas suave, $f(x) = \sin(10x) + \cos(10y)$](assets/func-nao-suave.png)

*Figura 2. Função bem desregular, mas suave, $f(x) = \sin(10x) + \cos(10y)$*

**Teorema: Aproximação linear de funções suaves**

Seja $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ uma função diferenciável. Então $f$ é $L$-suave se, e somente se, $\forall x,y \in {\mathbb{R}}^{n}$: $$\vert f(y) - f(x) - \nabla{f(x)}^{T}(y - x)\vert  \leq \frac{L}{2}\| y - x\|_{2}^{2}$$

Usando esse teorema, a gente pode escrever isso: $$\begin{aligned} f\left( x^{(t + 1)} \right) & \leq f\left( x^{(t)} \right) + \nabla{f\left( x^{(t)} \right)}^{T}\left( x^{(t + 1)} - x^{(t)} \right) + \frac{L}{2}\| x^{(t + 1)} - x^{(t)}\|^{2} \\ & \leq f\left( x^{(t)} \right) - \alpha\|\nabla f\left( x^{(t)} \right)\|^{2} + \frac{\alpha^{2}L}{2}\|\nabla f\left( x^{(t)} \right)\|^{2} \\ & \leq f\left( x^{(t)} \right) - \alpha\left( 1 - \frac{\alpha L}{2} \right)\|\nabla f\left( x^{(t)} \right)\|^{2} \end{aligned}$$<a id="iterated-aproximation"></a>

E isso vale quando $\alpha \in \left( 0,\frac{2}{L} \right)$, ou seja, se o ponto atual $x^{(t)}$ **NÃO É ESTACIONÁRIO**, o valor da função no próximo ponto será **menor** que o valor do ponto atual menos o tamanho do gradiente ao quadrado vezes um termo de regulação. Parece complicado, mas o que isso quer dizer? Eu vou usar esse fato para mostrar que, independente do ponto que eu iniciar o método do gradiente, eu **sempre vou encontrar um ponto mínimo local utilizando o método do gradiente**

<a id="gradient-descent-convergence"></a>

**Teorema: Convergência do Gradient Descent**

Suponha que $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ é $L$-suave. Tome qualquer passo: $$\alpha = \frac{\beta}{L}$$ para algum $\beta \in (0,2)$. Então: $$\min\limits_{t \in \lbrack T\rbrack}\|\nabla f\left( x^{(t)} \right)\|_{2}^{2} \leq \frac{1}{T}\sum_{t = 1}^{T}\|\nabla f\left( x^{(t)} \right)\|_{2}^{2} \leq \left( \frac{2/\beta}{2 - \beta} \right)\frac{L\left( f\left( x^{(1)} \right) - f^{\ast} \right)}{T}$$

**Demonstração**

Sabemos que, dado $n$ pontos $x_{i}$, a média $\frac{1}{n}\sum_{i = 1}^{n}x_{i} \in \left\lbrack \min(x_{i}),\max(x_{i}) \right\rbrack$, então a desigualdade inicial já está provada. Vamos provar a segunda. Usando a equação [\[iterated-aproximation\]](#iterated-aproximation), temos que: $$\alpha\left( 1 - \frac{\alpha L}{2} \right)\|\nabla f\left( x^{(t)} \right)\|^{2} \leq f\left( x^{(t)} \right) - f\left( x^{(t + 1)} \right)$$ isso para todo $t \in \lbrack T\rbrack$, então vamos somar todos os termos para obter: $$\begin{aligned} \alpha\left( 1 - \frac{\alpha L}{2} \right)\sum_{t = 1}^{T}\|\nabla f\left( x^{(t)} \right)\|_{2}^{2} & \leq \sum_{t = 1}^{T}\left( f\left( x^{(t)} \right) - f\left( x^{(t + 1)} \right) \right) \\ & \leq f\left( x^{(1)} \right) - f\left( x^{(T + 1)} \right) \\ & = f\left( x^{(1)} \right) - f^{\ast} + f^{\ast} + f\left( x^{(T + 1)} \right) \\ & \leq f\left( x^{(1)} \right) - f^{\ast} \end{aligned}$$ A primeria desigualdade eu fiz uma soma telescópica, depois eu somei $0$ ($f^{\ast} - f^{\ast}$) e, como $f^{\ast}$ é o valor mínimo da função, com certeza subtrair a parte que eu somei $f^{\ast}$ vai dar um valor maior, então eu obtenho o resultado do enunciado do teorema dividindo tudo por $\alpha(1\frac{- (\alpha L)}{2})T$

Por que esse teorema mostra que, independentemente do lugar, o algoritmo converge para um ponto estacionário? Ele ta me dizendo isso daqui: $$\min\limits_{t \in \lbrack T\rbrack}\|\nabla f\left( x^{(t)} \right)\|_{2}^{2} = O\left( \frac{1}{T} \right)$$ Ou seja, o mínimo **converge para $0$** conforme $T \rightarrow \infty$ **independentemente do ponto inicial $x^{(0)}$**

Só que se pararmos para pensar, se $\nabla f(x)$ é uma direção de subida, então $- \nabla f(x)$ é de descida, mas será que é a melhor? Será que **precisa** ser a melhor para o método funcionar? Se eu escolher **uma direção de descida arbitrária** ele funciona? Mas antes disso, vamos entender o que é uma direção de descida

**Definição: Direção de Descida**

Dizemos que $d \in {\mathbb{R}}^{n}$ é uma direção de descida para a funçaõ $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ no ponto $x \in {\mathbb{R}}^{n}$ quando: $$d^{T}\nabla f(x) < 0$$

então podemos considerar um novo algoritmo

<a id="gradient-descent-2"></a>

1.  **func** GradientDescentWithArbitraryDescentDirection($f$) {

    1.  $x^{(0)} \in {\mathbb{R}}^{n}$

    2.  $\alpha > 0$

    3.  **for** $t \in \lbrack T\rbrack$ **do** {

        1.  Encontrar **uma** direção de descida $d^{(t)}$

        2.  $x^{(t + 1)} = x^{(t)} + \alpha d^{(t)}$

    4.  }

    5.  **return** $x^{(T)}$

2.  }

*Figura 3. Gradient Descent com Direção de Descida Arbitrária*

Podemos provar, analogamente ao [\[gradient-descent-convergence\]](#gradient-descent-convergence), que o algoritmo converge para um ponto estacionário

<a id="caso-convexo"></a>
<a id="secao-4"></a>

## Caso Convexo

Antes, não assumimos nada além da suavidade da função, agora vamos mostrar que, assumindo que $f$ é convexa, o algoritmo converge para uma solução global. Primeiro, nós sabemos que: $$\begin{aligned} x^{(t + 1)} & = x^{(t)} - \alpha\nabla f\left( x^{(t)} \right) \\ \Leftrightarrow x^{(t + 1)} - x^{\ast} & = x^{(t)} - x^{\ast} - \alpha\nabla f\left( x^{(t)} \right) \\ \Leftrightarrow \| x^{(t + 1)} - x^{\ast}\|_{2}^{2} & = \| x^{(t)} - x^{\ast} - \alpha\nabla f\left( x^{(t)} \right)\|_{2}^{2} \end{aligned}$$

Pelas propriedades da [convexidade](otimizacao-convexa.md#secao-10): $$\left( x^{\ast} - x^{(t)} \right)^{T}\nabla f\left( x^{(t)} \right) \leq f\left( x^{\ast} \right) - f\left( x^{(t)} \right)$$

e pelo que vimos na equação [\[iterated-aproximation\]](#iterated-aproximation), se $\alpha \in \left( 0,\frac{2}{L} \right)$, podemos chegar que: $$\| x^{(t + 1)} - x^{\ast}\|_{2}^{2} \leq \| x^{(t)} - x^{\ast}\|_{2}^{2} - \alpha\left( 2 - \frac{1}{1\frac{- (\alpha L)}{2}} \right)\left( f\left( x^{(t)} \right) - f^{\ast} \right)$$

ou seja, a distância do próximo iterado pro ponto ótimo é menor a distância atual, menos um termo proporcional a distância dos resultados de $x^{(t)}$ e do ponto ótimo. Vamos usar isso para provar a convergência global do resultado

**Teorema: Convergência Convexa do Método do Gradiente**

Suponha que $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ é $L$-suave e convexa e tome qualquer passo $$\alpha = \frac{\beta}{L}$$ para algum $\beta \in (0,1)$, então: $$f\left( x^{(T)} \right) - f^{\ast} \leq \frac{1}{T}\sum_{t = 1}^{T}\left( f\left( x^{t} \right) - f^{\ast} \right) \leq \frac{\beta^{- 1} - \frac{1}{2}}{1 - \beta}\frac{L\| x^{(1)} - x^{\ast}\|_{2}^{2}}{T}$$

**Demonstração**

Somando-se em $tin\lbrack T\rbrack$ a [recorrência](../projeto-e-analise-de-algoritmos/recorrencia.md): $$\alpha(2 - \frac{1}{1 - \alpha\frac{L}{2}}\left( f\left( x^{t} \right) - f^{\ast} \right) \leq \| x^{(t)} - x^{\ast}\|_{2}^{2} - \| x^{(t + 1)} - x^{\ast}\|_{2}^{2}$$

obtemos novamente uma soma telescópica: $$\begin{aligned} \alpha\left( \frac{1 - \alpha L}{1 - \alpha\frac{L}{2}} \right)\sum_{t = 1}^{T}\left( f\left( x^{(t)} \right) - f^{\ast} \right) & \leq \sum_{t = 1}^{T}\left( \| x^{(t)} - x^{\ast}\|_{2}^{2} - \| x^{(t + 1)} - x^{\ast}\|_{2}^{2} \right) \\ & \leq \| x^{(1)} - x^{\ast}\|_{2}^{2} - \| x^{(T + 1)} - x^{\ast}\|_{2}^{2} \\ & \leq \| x^{1} - x^{\ast}\|_{2}^{2.} \end{aligned}$$

Dividindo-se por $\alpha\left( \frac{1 - \alpha L}{1 - \alpha\frac{L}{2}} \right)T$, e lembrando que, pelo , a sequência $\left\{ f\left( x^{(t)} \right) \right\}$ é decrescente: $$f\left( x^{(T)} \right) - f^{\ast} \leq \frac{1}{T}\sum_{\left\{ t = 1 \right\}}^{T}\left( f\left( x^{(t)} \right) - f^{\ast} \right) \leq \frac{\alpha^{- 1}\left( 1 - \alpha\frac{L}{2} \right)}{T}\| x^{1} - x^{\ast}\|_{2}^{2.}$$

<a id="interpretacao-via-regularizacao"></a>
<a id="secao-5"></a>

## Interpretação via regularização

Outra formas que podemos ver e interpretar o algoritmo do gradiente é resolver a seguinte fórmula: $$x^{(t + 1)} = \text{ argmin}_{x \in {\mathbb{R}}^{n}}\left( \underset{\text{ Aproximação Linear }}{\underbrace{f\left( x^{(t)} \right) + \left( x - x^{(t)} \right)^{T}\nabla f\left( x^{(t)} \right)}} + \underset{\text{ Regularização Proximal }}{\underbrace{\frac{1}{2\alpha^{(t)}}\| x - x^{(t)}\|_{2}^{2}}} \right)$$

Ou seja, eu vou pegar qual que é o valor que minimiza a aproximação linear regularizada por um termo quadrático

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Conteúdos relacionados

- [Método Gradiente — Otimização para Ciência de Dados](algoritmos-de-otimizacao.md#metodo-gradiente)


## Percurso de estudo

[Trilha: A2](../../trilhas/otimizacao-para-ciencia-de-dados/a2.md) · [Apresentação e contexto da fonte](../../trilhas/otimizacao-para-ciencia-de-dados/a2.md#apresentacao-original)

- Anterior: [Introdução](introducao.md)
- Próximo: [Método do Subgradiente](metodo-do-subgradiente.md)
