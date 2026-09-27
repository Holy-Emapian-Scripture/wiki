---
layout: "default"
title: "Os Gradientes — Convolutional Neural Networks (CNN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 28
---

[Aprendizado de Máquina](../../index.md) · [Convolutional Neural Networks (CNN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-33"></a>

# Os Gradientes

Não basta mostrar arquiteturas e métodos usados em CNN se não sabemos como treiná-las. Para isso, precisamos entender como calcular os gradientes das operações de convolução e pooling. O cálculo dos gradientes é feito através do algoritmo de backpropagation (também muito utilizado o automatic differentiation).

<a id="secao-34"></a>

## Convolução sem Padding e Stride

Vamos primeiro olhar a derivação dos gradientes no caso mais fácil, que é com uma imagem com escalas de cinza, onde toda a imagem é representada por uma única matriz 2D.

**Definição: Convolução/Correlação Cruzada 2D sem padding e stride**

Seja a imagem $X \in {\mathbb{R}}^{H \times W}$ e o filtro $K \in {\mathbb{R}}^{M \times N}$, definimos a saída da camada convolucional, sem padding e sem stride como: $$(X \ast K)_{ij} = Y_{ij} = \sum_{m = 0}^{M - 1}\sum_{n = 0}^{N - 1}X_{i + m,j + n}K_{mn} + b$$ para $$0 \leq i \leq H - M\text{\quad\quad}0 \leq j \leq W - N$$

considere que estamos trabalhando com o gradiente em cima de uma função de perca $L$, por exemplo, se estamos usando a CNN para fazer a classificação de imagens, podemos usar a função de perca **cross-entropy**. Defina também: $$\delta_{ij} = \frac{\partial L}{\partial Y_{ij}}$$

**Teorema: Gradiente da Convolução Discreta 2D sem padding e stride**

O gradiente da perca em relação ao coeficiente $K_{mn}$ é dado por: $$\frac{\partial L}{\partial K_{mn}} = \sum_{i = 0}^{H - M}\sum_{j = 0}^{W - N}\delta_{ij}X_{i + m,j + n}$$ para $$0 \leq m \leq M - 1\text{\quad\quad}0 \leq n \leq N - 1$$ ou, equivalentemente, podemos escrever de forma matricial como: $$\nabla_{K}L = X \ast \delta$$ onde $\delta \in {\mathbb{R}}^{H - M + 1 \times W - N + 1}$ e $$\delta = \begin{pmatrix} - & \delta_{0,0} & - & \delta_{0,1} & - & \ldots & - & \delta_{0,W - N} & - \\ & \vdots & \\ - & \delta_{H - M,0} & - & \delta_{H - M,1} & - & \ldots & - & \delta_{H - M,W - N} & - \end{pmatrix}$$

**Demonstração**

Pela regra da cadeia, temos que $$\frac{\partial L}{\partial K_{mn}} = \sum_{i,j}\frac{\partial L}{\partial Y_{ij}}\frac{\partial Y_{ij}}{\partial K_{mn}}$$ e, por definição $$Y_{ij} = \sum_{u,v}X_{i + u,j + v}K_{uv} + b$$ logo: $$\frac{\partial Y_{ij}}{\partial K_{mn}} = X_{i + m,j + n}$$ substituindo na equação anterior, temos que $$\frac{\partial L}{\partial K_{mn}} = \sum_{i,j}\delta_{ij}X_{i + m,j + n}$$

**Teorema: Gradiente do Bias**

Temos que: $$\frac{\partial L}{\partial b} = \sum_{ij}\delta_{ij}$$

**Demonstração**

Novamente, pela regra da cadeia, temos que $$\frac{\partial L}{\partial b} = \sum_{i,j}\frac{\partial L}{\partial Y_{ij}}\frac{\partial Y_{ij}}{\partial b}$$ e como vimos anteriormente, pela definição, temos que $$\frac{\partial Y_{ij}}{\partial b} = 1$$ substituindo na equação anterior, temos que $$\frac{\partial L}{\partial b} = \sum_{i,j}\delta_{ij}$$

**Teorema: Gradiente da Imagem**

O gradiente da perca em relação à imagem $X$ é dado por: $$\frac{\partial L}{\partial X_{ij}} = \sum_{m = 0}^{M - 1}\sum_{n = 0}^{N - 1}\delta_{i - m,j - n}K_{mn}$$ para $$0 \leq i \leq H - 1\text{\quad\quad}0 \leq j \leq W - 1$$ ou, equivalentemente, podemos escrever de forma matricial como: $$\nabla_{X}L = \delta \ast K^{\text{flip }}$$ onde $\delta \in {\mathbb{R}}^{H - M + 1 \times W - N + 1}$ e $K^{\text{flip}}$ é a imagem da kernel $K$ rotacionada por 180 graus, ou seja: $$K_{mn}^{\text{flip}} = K_{M - 1 - m,N - 1 - n}$$

**Demonstração**

Vamos fixar uma coordenada $(a,b)$ e calcular o gradiente da perca em relação à imagem $X$ nessa coordenada. Pela regra da cadeia, temos que: $$\frac{\partial L}{\partial X_{ab}} = \sum_{i,j}\frac{\partial L}{\partial Y_{ij}}\frac{\partial Y_{ij}}{\partial X_{ab}}$$ como vimos anteriormente, pela definição, temos que $$Y_{ij} = \sum_{u,v}X_{i + u,j + v}K_{uv} + \text{ bias }$$ temos então que $$\frac{\partial Y_{ij}}{\partial X_{ab}} = K_{a - i,b - j}$$ sempre que os índices estão no suporte do kernel. Logo, $$\frac{\partial L}{\partial X_{ab}} = \sum_{i,j}\delta_{ij}K_{a - i,b - j}$$ e por que essa expressão equivale a $K^{\text{flip}}$? Pois, se definirmos $K_{ij}^{\text{flip}} = K_{M - 1 - i,N - 1 - j}$, então podemos reescrever a expressão acima como: $$\frac{\partial L}{\partial X_{ab}} = \sum_{i,j}\delta_{a - i,b - j}K_{ij}^{\text{flip}}$$

<a id="secao-35"></a>

## Convolução com Padding e Stride

**Definição: Padding**

Padding pode ser definido como uma função $T:{\mathbb{R}}^{H \times W} \rightarrow {\mathbb{R}}^{H + 2P \times W + 2P}$, onde $P$ é o tamanho do padding que adicona $P$ linhas e $P$ colunas de zeros ao redor da imagem original

**Teorema: Padding é Linear**

Seja $X,Y \in {\mathbb{R}}^{H \times W}$ e $T(X) \in {\mathbb{R}}^{H + 2P \times W + 2P}$ o padding de $X$, então temos que: $$T(\alpha X + \beta Y) = \alpha T(X) + \beta T(Y)$$

**Demonstração**

Primeiro, vamos mostrar que $T$ é linear em vetores, e então, mostrar que a operação também é linear em matrizes. Seja $x \in {\mathbb{R}}^{m}$ e $\hat{x} = T(x) \in {\mathbb{R}}^{m + 2P}$ o padding de $x$, temos que a operação faz: $$\begin{pmatrix} x_{1} \\ x_{2} \\ \vdots \\ x_{m} \end{pmatrix} \mapsto \begin{pmatrix} 0 \\ \vdots \\ 0 \\ x_{1} \\ \vdots \\ x_{m} \\ 0 \\ \vdots \\ 0 \end{pmatrix}$$ No entando, perceba que, se definirmos a matriz: $$M = \begin{pmatrix} \mathbf{0} \\ I \\ \mathbf{0} \end{pmatrix} \in {\mathbb{R}}^{(m + 2P) \times m}$$ onde $\mathbf{O} \in {\mathbb{R}}^{P \times m}$ e a identidade $I \in {\mathbb{R}}^{m \times m}$, então podemos definir: $$\hat{x} = T(x) = Mx$$ então podemos definir o padding de matrizes como: $$T(X) = \begin{pmatrix} & \vert  & & \vert  & \\ \mathbf{0} & T\left( x_{1} \right) & \ldots & T\left( x_{W} \right) & \mathbf{0} \\ & \vert  & & \vert \end{pmatrix}$$ esses novos $0$ são bloco de matrizes de zeros de tamanho $H \times P$. Logo, temos que: $$T(X) = \begin{pmatrix} \mathbf{0} & M & \mathbf{0} \end{pmatrix}X$$ onde $M$ é matriz $(m + 2P) \times m$ que vimos e $\mathbf{0}$ é uma matriz de zeros de tamanho $H \times P$. Logo, temos no final uma matriz de tamanho $(H + 2P) \times (W + 2P)$ e, como $T$ é uma multiplicação de matrizes, temos que $T$ é linear.

**Definição: Stride**

Seja $S \in {\mathbb{N}}$ o stride. Definimos o operador de stride

$$D_{S}:{\mathbb{R}}^{H \times W} \rightarrow {\mathbb{R}}^{H' \times W'}$$

onde

$$H' = \left\lfloor \frac{H - 1}{S} \right\rfloor + 1$$

e

$$W' = \left\lfloor \frac{W - 1}{S} \right\rfloor + 1$$

tal que

$$\left( D_{S}(X) \right)_{i,j} = X_{iS,jS}.$$

Em outras palavras, o operador mantém apenas as entradas espaçadas de $S$ posições.

**Teorema: Stride é Linear**

Seja

$$D_{S}:{\mathbb{R}}^{H \times W} \rightarrow {\mathbb{R}}^{H' \times W'}$$

o operador de stride de tamanho $S$.

Então

$$D_{S}(\alpha X + \beta Y) = \alpha D_{S}(X) + \beta D_{S}(Y)$$

para quaisquer

$$X,Y \in {\mathbb{R}}^{H \times W}$$

e

$$\alpha,\beta \in {\mathbb{R}}.$$

**Demonstração**

Primeiro consideremos o caso vetorial.

Seja

$$x = \left( x_{0},x_{1},\ldots,x_{n - 1} \right)^{T} \in {\mathbb{R}}^{n}.$$

O operador de stride mantém apenas as coordenadas

$$0,S,2S,\ldots$$

Assim,

$$D_{S}(x) = \left( x_{0},x_{S},x_{2S},\ldots \right)^{T}.$$

Definamos a matriz

$$M_{S} = \begin{pmatrix} 1 & 0 & 0 & 0 & \ldots \\ 0 & \ldots & 1 & 0 & \ldots \\ \ldots & \ldots & \ldots & \ldots & \ldots \end{pmatrix}$$

cujas linhas possuem exatamente um elemento igual a $1$ nas posições

$$0,S,2S,\ldots$$

e zero nas demais.

Então

$$D_{S}(x) = M_{S}x.$$

Logo,

$$D_{S}(\alpha x + \beta y) = M_{S}(\alpha x + \beta y)$$

$$= \alpha M_{S}x + \beta M_{S}y$$

$$= \alpha D_{S}(x) + \beta D_{S}(y).$$

Portanto $D_{S}$ é linear em vetores.

**Definição: Convolução/Correlação Cruzada 2D com padding e stride**

Seja $X \in {\mathbb{R}}^{H \times W}$, $K \in {\mathbb{R}}^{M \times N}$, $P$ o padding, $S$ o stride e $\widetilde{X} = T(X)$ a imagem com padding, então a saída da camada convolucional é dada por: $$Y_{ij} = \sum_{m = 0}^{M - 1}\sum_{n = 0}^{N - 1}{\widetilde{X}}_{i \cdot S + m,j \cdot S + n}K_{mn} + b$$

**Teorema: Gradiente da Convolução Discreta 2D com padding e stride**

O gradiente da perca em relação ao coeficiente $K_{mn}$ é dado por: $$\frac{\partial L}{\partial K_{mn}} = \sum_{i = 0}^{H - M}\sum_{j = 0}^{W - N}\delta_{ij}{\widetilde{X}}_{i \cdot S + m,j \cdot S + n}$$ para $$0 \leq m \leq M - 1\text{\quad\quad}0 \leq n \leq N - 1$$ ou, equivalentemente, podemos escrever de forma matricial como: $$\nabla_{K}L = \widetilde{X} \ast \delta$$ onde $\ast$ denota a convolução cruzada com stride $S$

**Demonstração**

Pela regra da cadeia, temos que $$\frac{\partial L}{\partial K_{mn}} = \sum_{i,j}\frac{\partial L}{\partial Y_{ij}}\frac{\partial Y_{ij}}{\partial K_{mn}}$$ e, por definição $$Y_{ij} = \sum_{u,v}{\widetilde{X}}_{i \cdot S + u,j \cdot S + v}K_{uv} + b$$ logo: $$\frac{\partial Y_{ij}}{\partial K_{mn}} = {\widetilde{X}}_{i \cdot S + m,j \cdot S + n}$$ substituindo na equação anterior, temos que $$\frac{\partial L}{\partial K_{mn}} = \sum_{i,j}\delta_{ij}{\widetilde{X}}_{i \cdot S + m,j \cdot S + n}$$

<a id="input-gradient-with-stride"></a>

**Teorema: Gradiente da Entrada com Stripe**

Defina o operador de expansão $$U_{S}(\delta):{\mathbb{R}}^{H \times W} \rightarrow {\mathbb{R}}^{(H - 1) \cdot (S - 1) + 1 \times (W - 1) \cdot (S - 1) + 1}$$ obtido inserindo $S - 1$ linhas e colunas de zeros entre cada linha e coluna de $\delta$. Então, o gradiente da perca em relação à imagem $X$ é dado por: $$\nabla_{\widetilde{X}}L = U_{S}(\delta) \ast K^{\text{flip }}$$

**Exemplo**

Suponha $S = 2$ e $$\delta = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$ então $$U_{2}(\delta) = \begin{pmatrix} a & 0 & b \\ 0 & 0 & 0 \\ c & 0 & d \end{pmatrix}$$ logo $$\nabla_{\widetilde{X}}L = U_{2}(\delta) \ast K^{\text{flip }}$$

A intuição é que, quando o stride é 2, a convolução só visita $$(0,0),(0,2),(2,0),(2,2)$$ As posições intermediárias nunca participam do forward. Por isso surgem os zeros na expansão, pois essas posições intermediárias não contribuem para o gradiente da entrada.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Arquiteturas](../arquiteturas/index.md)
- Próximo: [Otimizações Computacionais](../otimizacoes-computacionais/index.md)
