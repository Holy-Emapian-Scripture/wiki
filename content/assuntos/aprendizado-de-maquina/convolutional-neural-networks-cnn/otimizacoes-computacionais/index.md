---
layout: "default"
title: "Otimizações Computacionais — Convolutional Neural Networks (CNN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 29
---

[Aprendizado de Máquina](../../index.md) · [Convolutional Neural Networks (CNN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-36"></a>

# Otimizações Computacionais

Fizemos algumas definições e teoremas sobre convolução, mas não falamos sobre como implementá-las de forma eficiente. A implementação direta das operações de convolução e pooling pode ser ineficiente, especialmente para imagens grandes e redes profundas. Para melhorar a eficiência computacional, podemos utilizar certas técnicas

<a id="secao-37"></a>

## im2col

Temos um problema, na convolução comum, temos: $$Y_{ij} = \sum_{m = 0}^{M - 1}\sum_{n = 0}^{N - 1}{\widetilde{X}}_{i \cdot S + m,j \cdot S + n}K_{mn} + b$$ essa operação já tem complexidade $O(MN)$, e isso é apenas para uma das entradas, tendo em mente que faremos isso para outras $H \times W$ entradas, a complexidade sobe para $O(HWMN)$, o que é computacionalmente caro. Entretanto, existe uma observação genial que podemos fazer aqui

Considere a imagem: $$X = \begin{pmatrix} x_{0,0} & x_{0,1} & x_{0,2} & x_{0,3} \\ x_{1,0} & x_{1,1} & x_{1,2} & x_{1,3} \\ x_{2,0} & x_{2,1} & x_{2,2} & x_{2,3} \\ x_{3,0} & x_{3,1} & x_{3,2} & x_{3,3} \end{pmatrix}$$ e um kernel $3 \times 3$. Em um stride padrão de $1$, as janelas visitadas são. Primeira: $$\begin{pmatrix} x_{0,0} & x_{0,1} & x_{0,2} \\ x_{1,0} & x_{1,1} & x_{1,2} \\ x_{2,0} & x_{2,1} & x_{2,2} \end{pmatrix}$$ Segunda: $$\begin{pmatrix} x_{0,1} & x_{0,2} & x_{0,3} \\ x_{1,1} & x_{1,2} & x_{1,3} \\ x_{2,1} & x_{2,2} & x_{2,3} \end{pmatrix}$$ e assim vai. A ideia é transformar cada uma dessas janelas em uma coluna de uma matriz. Primeira janela: $$\begin{pmatrix} x_{0,0} \\ x_{0,1} \\ x_{0,2} \\ x_{1,0} \\ x_{1,1} \\ x_{1,2} \\ x_{2,0} \\ x_{2,1} \\ x_{2,2} \end{pmatrix}$$ Segunda janela: $$\begin{pmatrix} x_{0,1} \\ x_{0,2} \\ x_{0,3} \\ x_{1,1} \\ x_{1,2} \\ x_{1,3} \\ x_{2,1} \\ x_{2,2} \\ x_{2,3} \end{pmatrix}$$ e assim vai. Então como resultado, vamos ter: $$X_{\text{col }} = \begin{pmatrix} x_{0,0} & x_{0,1} & \\ x_{0,1} & x_{0,2} & \\ x_{0,2} & x_{0,3} & \\ x_{1,0} & x_{1,1} & \\ x_{1,1} & x_{1,2} & \ldots \\ x_{1,2} & x_{1,3} & \\ x_{2,0} & x_{2,1} & \\ x_{2,1} & x_{2,2} & \\ x_{2,2} & x_{2,3} & \end{pmatrix}$$

e o resultado obtido da convolução será $Y_{\text{col}}$ e estará no mesmo estilo de $X_{\text{col}}$. Para isso, precisamos achatar o kernel, de forma que, se nosso kernel tem tamanho $3 \times 3$ $$K = \begin{pmatrix} k_{0,0} & k_{0,1} & k_{0,2} \\ k_{1,0} & k_{1,1} & k_{1,2} \\ k_{2,0} & k_{2,1} & k_{2,2} \end{pmatrix}$$

então $K_{\text{col}}$ será: $$K_{\text{col }} = \begin{pmatrix} k_{0,0} \\ k_{0,1} \\ k_{0,2} \\ k_{1,0} \\ k_{1,1} \\ k_{1,2} \\ k_{2,0} \\ k_{2,1} \\ k_{2,2} \end{pmatrix}$$

Logo, teremos que $$Y_{\text{col }} = K_{\text{col}}^{T}X_{\text{col }} + b$$

matematicamente, essa operação também não altera nada, pois no backward do filtro $$\nabla_{K}L = X_{\text{col }}\delta_{\text{col}}^{T}$$ e o backward do input $$\nabla_{X_{\text{col}}}L = K_{\text{col }}\delta_{\text{col }}$$

<a id="secao-38"></a>

## col2im

Essa operação é mais utilizada para, a partir do gradiente de $X_{\text{col}}$, obtermos o gradiente com respeito de $X$ de volta para continuar as operações do backpropagation

<a id="secao-39"></a>

## Aplicação como uma Multiplicação de Matrizes

Como vimos, a maior parte das operações de convolução podem ser representadas como multiplicações de matrizes, o que permite que possamos utilizar bibliotecas otimizadas para multiplicação de matrizes, como BLAS e cuBLAS, para acelerar o treinamento das CNNs. Além disso, podemos utilizar técnicas de paralelização e distribuição para treinar redes profundas em grandes conjuntos de dados.

Seja $X$ a imagem de entrada, podemos definir a saída da convolução como: $$Y = D_{S} \cdot K \cdot M \cdot D_{P} \cdot X$$ onde

- $D_{P}$ é o operador de padding

- $M$ é o operador de im2col

- $K$ é o operador de multiplicação do kernel

- $D_{S}$ é o operador de stride

Então o backward será simplesmente a operação: $$\nabla_{X}L = D_{P}^{\ast} \cdot M^{\ast} \cdot K^{\ast} \cdot D_{S}^{\ast} \cdot \delta$$

- Crop $P^{\ast}$

- col2im $M^{\ast}$

- Kernel invertido $K^{\ast}$

- Operador de expansão $D_{S}^{\ast}$ (O mesmo definido em [\[input-gradient-with-stride\]](../os-gradientes/index.md#input-gradient-with-stride))

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Os Gradientes](../os-gradientes/index.md)
- Próximo: [Pooling](../pooling/index.md)
