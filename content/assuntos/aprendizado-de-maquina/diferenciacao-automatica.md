---
layout: "default"
title: "Diferenciação Automática"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 4
---

[Aprendizado de Máquina](index.md)

<!-- wiki:original:inicio -->

<a id="secao-4"></a>

# Diferenciação Automática


<a id="introducao"></a>
<a id="secao-5"></a>

## Introdução

Aposto que, se você é alguém que, como eu, sempre teve interesse de ver esses algoritmos de machine learning e implementar eles do $0$, sentiu alguma dificuldade principalmente quando a sua implementação envolvia o cálculo de algum gradiente (principalmente algum gradiente difícil). Calcular o gradiente de uma função $g:{\mathbb{R}}^{D} \rightarrow {\mathbb{R}}$ com relação a $x \in {\mathbb{R}}^{D}$ é uma tarefa que pode ser extremamente trabalhosa, especialmente quando $g$ é uma função complexa, e justamente essa tarefa complexa é a base fundamental pra que nossas máquinas possam aprender.

Existem, essencialmente, $4$ formas de se calcular o gradiente de uma rede neural.

1.  Derivar as expressões analiticamente e implementá-las manualmente via software. Essa abordagem é extremamente trabalhosa, propensa a erros e não escalável para funções complexas. (Particularmente, exatamente o que eu sempre tentava fazer). Não só isso, mas as implementações dessas alternativas envolvem montar funções distintas para o forward pass e o backward pass, o que torna o processo ainda mais trabalhoso.

2.  Outro método é calcular o gradiente de forma aproximada: $$\frac{\partial f}{\partial x} \approx \frac{f(x + h) - f(x)}{h}\text{\quad\quad}h \approx 0$$ ele está bastante sujetio à erros numéricos, mas esse não é o principal problema, mas sim que ele escala muito mal com o tamanho da rede neural, mas ele é muito útil para verificar se a implementação do gradiente está correta (já que ele utiliza apenas o forward pass da rede neural).

3.  O terceiro método é o **symbolic differentiation**, que consiste em derivar a função simbolicamente e depois implementá-la. Essa abordagem é mais escalável do que a primeira, mas ainda assim pode ser trabalhosa e propensa a erros, especialmente para funções complexas. Por exemplo, considere uma função $f(x) = u(x) \cdot v(x)$, $$\frac{\partial f}{\partial x} = \frac{\partial u}{\partial x} \cdot v + u \cdot \frac{\partial v}{\partial x}$$ e se $u$ e $v$ forem funções complexas, a derivada de $f$ pode se tornar extremamente complicada. Além disso, o symbolic differentiation pode gerar expressões redundantes, o que pode levar a uma implementação ineficiente.

4.  O quarto e último método é o **automatic differentiation**, que é o método mais eficiente e escalável para calcular gradientes de funções complexas. Ele é baseado na regra da cadeia e na decomposição da função em operações elementares, permitindo calcular o gradiente de forma eficiente e precisa. Além disso, ele permite calcular o gradiente de funções complexas sem a necessidade de derivar manualmente as expressões analiticamente.

<a id="diferenciacao-automatica-forward-mode"></a>
<a id="secao-6"></a>

## Diferenciação Automática forward-mode

Considere a seguinte função: $$f\left( x_{1},x_{2} \right) = x_{1}x_{2} + e^{x_{1}x_{2}} - \sin(x_{2})$$<a id="funcao-exemplo-diferenciacao-automatica-forward"></a> quando implementado em código, podemos decompor a função em operações elementares que podem ser visualizadas em grafo

![Grafo de computação da função [\[funcao-exemplo-diferenciacao-automatica-forward\]](#funcao-exemplo-diferenciacao-automatica-forward)](../assets/automatic-diff-forward.png)

*Figura 1. Grafo de computação da função [\[funcao-exemplo-diferenciacao-automatica-forward\]](#funcao-exemplo-diferenciacao-automatica-forward)*

essas operações são chamadas de *evaluation trace* $$\begin{aligned} & v_{1} = x_{1} \\ & v_{2} = x_{2} \\ & v_{3} = x_{1}x_{2} \\ & v_{4} = \sin(x_{2}) \\ & v_{5} = e^{v_{3}} \\ & v_{6} = v_{3} - v_{4} \\ & v_{7} = v_{5} + v_{6} \end{aligned}$$

Agora suponha que precisamos calcular o gradiente $\frac{\partial f}{\partial x_{1}}$. Nós definimos a **variável tangente** como ${\dot{v}}_{i} = \frac{\partial v_{i}}{\partial x_{1}}$. Podemos calcular essa variável automaticamente com a regra da cadeia: $${\dot{v}}_{i} = \frac{\partial v_{i}}{\partial x_{1}} = \sum_{j \in \text{ pa}\left( v_{i} \right)}\frac{\partial v_{i}}{\partial v_{j}} \cdot \frac{\partial v_{j}}{\partial x_{1}} = \sum_{j \in \text{ pa}\left( v_{i} \right)}\frac{\partial v_{i}}{\partial v_{j}} \cdot {\dot{v}}_{j}$$ onde $\text{pa}\left( v_{i} \right)$ é o conjunto de pais de $v_{i}$ no grafo de computação. Por exemplo, para $v_{3} = x_{1}x_{2}$, temos que $\text{pa}\left( v_{3} \right) = \left\{ v_{1},v_{2} \right\}$. Resolvendo de acordo com a equação acima, obtemos os valores de ${\dot{v}}_{i}$ para cada $v_{i}$: $$\begin{aligned} {\dot{v}}_{1} & = 1 \\ {\dot{v}}_{2} & = 0 \\ {\dot{v}}_{3} & = v_{1}{\dot{v}}_{2} + v_{2}{\dot{v}}_{1} \\ {\dot{v}}_{4} & = \cos(v_{2}){\dot{v}}_{2} \\ {\dot{v}}_{5} & = e^{v_{3}}{\dot{v}}_{3} \\ {\dot{v}}_{6} & = {\dot{v}}_{3} - {\dot{v}}_{4} \\ {\dot{v}}_{7} & = {\dot{v}}_{5} + {\dot{v}}_{6} \end{aligned}$$

Podemos resumir a **diferenciação automática** para este exemplo da seguinte forma:

Primeiro, escrevemos um código para implementar a avaliação das **variáveis primais** (**primal variables**), dadas pelas equações (8.50) a (8.56). As equações associadas e o código correspondente para avaliar as **variáveis tangentes** (**tangent variables**), dadas pelas equações (8.58) a (8.64), são gerados automaticamente.

Para calcular a derivada ($\frac{\partial f}{\partial x_{1}}$), fornecemos valores específicos para ($x_{1}$) e ($x_{2}$), e então o código executa as equações primais e tangentes, avaliando numericamente, em sequência, os pares ($\left( v_{i},{\dot{v}}_{i} \right)$) até obtermos ($\left( {\dot{v}}_{5} \right)$), que é a derivada desejada.

Agora considere o cenário onde temos uma função vetorial, onde a segunda saída é dada por: $$f_{2}\left( x_{1},x_{2} \right) = \left( x_{1}x_{2} - \sin(x_{2}) \right)\exp(x_{1}x_{2})$$<a id="funcao-exemplo-diferenciacao-automatica-forward-multidimensional"></a>

![Grafo de computação da função [\[funcao-exemplo-diferenciacao-automatica-forward\]](#funcao-exemplo-diferenciacao-automatica-forward) e [\[funcao-exemplo-diferenciacao-automatica-forward-multidimensional\]](#funcao-exemplo-diferenciacao-automatica-forward-multidimensional)](../assets/automatic-diff-forward-multidimensional.png)

*Figura 2. Grafo de computação da função [\[funcao-exemplo-diferenciacao-automatica-forward\]](#funcao-exemplo-diferenciacao-automatica-forward) e [\[funcao-exemplo-diferenciacao-automatica-forward-multidimensional\]](#funcao-exemplo-diferenciacao-automatica-forward-multidimensional)*

Se quisermos calcular $\frac{\partial f_{2}}{\partial x_{1}}$, conseguimos fazer isso no mesmo forward pass do cálculo de $\frac{\partial f_{1}}{\partial x_{1}}$, apenas adicionando mais equações para as **variáveis primais** e **variáveis tangentes** correspondentes a $f_{2}$. No entanto, se quisermos calcular $\frac{\partial f_{1}}{\partial x_{2}}$, precisamos fazer um novo forward pass, pois a variável tangente ${\dot{v}}_{i}$ depende da variável de entrada que estamos diferenciando. Portanto, no geral, se temos uma função com $D$ inputs e $K$ outputs, então um único forward pass produz apenas uma coluna da matriz jacobiana $K \times D$ $$J = \begin{pmatrix} \frac{\partial f_{1}}{\partial x_{1}} & \ldots & \frac{\partial f_{1}}{\partial x_{D}} \\ \vdots & \vdots & \vdots \\ \frac{\partial f_{K}}{\partial x_{1}} & \ldots & \frac{\partial f_{K}}{\partial x_{D}} \end{pmatrix}$$

A diferenciação automática forward-mode é muito útil pricipalmente em casos onde temos muito mais outputs do que inputs ($K \gg D$). Entretanto, no contexto de machine learning, o mais comum é termos uma única função de erro $\mathcal{l}:{\mathbb{R}}^{D} \rightarrow {\mathbb{R}}$ que queremos minimizar com relação a milhões de parâmetros em cadeia dentro das redes neurais, então a implementação forward-mode fica ineficiente, para contornar isso, mudamos para outra abordagem

<a id="diferenciacao-automatica-reverse-mode"></a>
<a id="secao-7"></a>

## Diferenciação Automática reverse-mode

Podemos pensar nessa implementação como uma generalização do processo de backpropagation. No modo forward, nós alimentamos cada variável intermediária $v_{i}$ com varáveis adicionais, nesses casos chamadas de **variáveis adjuntas**, denotadas por ${\overset{-}{v}}_{i}$. Considere novamente uma função de apenas $1$ output na forma $f:{\mathbb{R}}^{D} \rightarrow {\mathbb{R}}$. A variável adjunta ${\overset{-}{v}}_{i}$ é definida como: $${\overset{-}{v}}_{i} = \frac{\partial f}{\partial v_{i}}$$

Podemos calcular esse valor automaticamente com a regra da cadeia: $${\overset{-}{v}}_{i} = \frac{\partial f}{\partial v_{i}} = \sum_{j \in \text{ ch}\left( v_{i} \right)}\frac{\partial f}{\partial v_{j}} \cdot \frac{\partial v_{j}}{\partial v_{i}} = \sum_{j \in \text{ ch}\left( v_{i} \right)}{\overset{-}{v}}_{j} \cdot \frac{\partial v_{j}}{\partial v_{i}}$$

onde $\text{ch}\left( v_{i} \right)$ representa o conjunto de variáveis que dependem de $v_{i}$ (filhos do nó $v_{i}$). Considerando novamente o exemplo da função [\[funcao-exemplo-diferenciacao-automatica-forward\]](../diferenciacao-automatica-forward-mode/index.md#funcao-exemplo-diferenciacao-automatica-forward), podemos calcular as variáveis adjuntas ${\overset{-}{v}}_{i}$ para cada $v_{i}$: $$\begin{aligned} {\overset{-}{v}}_{7} & = 1 \\ {\overset{-}{v}}_{6} & = {\overset{-}{v}}_{7} \\ {\overset{-}{v}}_{5} & = {\overset{-}{v}}_{7} \\ {\overset{-}{v}}_{4} & = - {\overset{-}{v}}_{6} \\ {\overset{-}{v}}_{3} & = {\overset{-}{v}}_{5}v_{5} + {\overset{-}{v}}_{6} \\ {\overset{-}{v}}_{2} & = {\overset{-}{v}}_{2}v_{1} + {\overset{-}{v}}_{4}\cos(v_{2}) \\ {\overset{-}{v}}_{1} & = {\overset{-}{v}}_{3}v_{2} \end{aligned}$$

Observe que essas equações começam na saída (output) e fluem para trás através do grafo até as entradas (inputs). Mesmo com múltiplas entradas, apenas um único backward pass é necessário para calcular as derivadas.

Para uma função de erro de rede neural, as derivadas de $E$ em relação aos pesos e vieses (biases) são obtidas como as variáveis adjuntas (adjoint variables) correspondentes. Entretanto, se tivermos mais de uma saída, será necessário executar um backward pass separado para cada variável de saída.

O reverse mode costuma exigir mais memória do que o forward mode, porque todas as variáveis primais intermediárias (intermediate primal variables) precisam ser armazenadas para que estejam disponíveis quando for necessário calcular as variáveis adjuntas durante a passagem para trás.

Em contraste, no forward mode, as variáveis primais e tangentes são calculadas conjuntamente durante o forward pass, de modo que as variáveis podem ser descartadas assim que forem utilizadas.

Por isso, em geral, o forward mode também é mais simples de implementar do que o reverse mode.

<a id="exemplo-em-codigo"></a>
<a id="secao-8"></a>

## Exemplo em código

``` python
class SinLayer:
  def forward(self, x):
    self.x = x
    return np.sin(x)

  def backward(self, dout):
    dx = dout * np.cos(self.x)
    return dx


class SquaredLayer:
  def forward(self, x):
    self.x = x
    return x ** 2

  def backward(self, dout):
    dx = dout * 2 * self.x
    return dx


class ModuleList:
  def __init__(self, layers = None):
    self.layers = layers or []

  def forward(self, x):
    for layer in self.layers:
      x = layer.forward(x)
    return x

  def backward(self, dout):
    for layer in reversed(self.layers):
      dout = layer.backward(dout)
    return dout

import numpy as np

class SinLayer:
    def forward(self, x):
        self.x = x
        return np.sin(x)

    def backward(self, dout):
        return dout * np.cos(self.x)


class SquaredLayer:
    def forward(self, x):
        self.x = x
        return x ** 2

    def backward(self, dout):
        return dout * 2 * self.x


class ModuleList:
    def __init__(self, layers=None):
        self.layers = layers or []

    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def backward(self, dout=1):
        for layer in reversed(self.layers):
            dout = layer.backward(dout)
        return dout


## Função f representando sin^2(x)
f = ModuleList([
    SinLayer(),
    SquaredLayer()
])

x = 2

y = f.forward(x)
dy = f.backward()

print(y)   # 0.8268218104...
print(dy)  # -0.7568024953...
```

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Problema de Aprendizagem](problema-de-aprendizagem.md)
- Próximo: [Processos Gaussianos](processos-gaussianos.md)
