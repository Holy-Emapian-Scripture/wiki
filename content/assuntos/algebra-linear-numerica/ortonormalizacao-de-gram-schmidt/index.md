---
layout: "default"
title: "Ortonormalização de Gram-Schmidt"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 25
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-25"></a>

# Ortonormalização de Gram-Schmidt


<a id="algoritmo-de-gram-schmidt-modificado"></a>
<a id="secao-26"></a>

## Algoritmo de Gram-Schmidt Modificado

Usando as definições anteriores, vamos reescrever o Algoritmo de Gram-Schmidt.

Para cada valor de $j$, o algoritmo de Gram-Schmidt original calcula uma única projeção ortogonal de posto $m - (j - 1)$. Estou apenas traduzindo para a linguagem usando projetores, ele faz isso: $$v_{j} = P_{j}a_{j} = \left( I - {\widehat{Q}}_{j - 1}{\widehat{Q}}_{j - 1}^{\ast} \right)a_{j}$$ Se você voltar ao que eu disse antes, obterá a fórmula original, estou apenas trocando aquele monte de somas e vetores por um produto matricial. O algoritmo original faz esse cálculo usando um único projetor, mas o que veremos faz isso por uma sequência de $j - 1$ projetores de posto $m - 1$. Pela definição de $P_{j}$, podemos afirmar que:

**Teorema**

$$
P_{j} = P_{\perp q_{j - 1}}\ldots P_{\perp q_{2}}P_{\perp q_{1}}
$$

**Demonstração**

Lembre-se que $P_{\perp q_{k}} = I - q_{k}q_{k}^{\ast}$, e o que isso faz? Ele projeta um vetor $v$ no subespaço ortogonal a $\left\{ q_{1},\ldots,q_{k - 1} \right\}$, ou seja, removendo os componentes $\left\{ q_{1},\ldots,q_{k - 1} \right\}$ de $v$. O projetor $P_{j}$ faz exatamente a mesma coisa, certo? Então, você pode pensar que, se eu projeto no complemento de $q_{1}$, depois no complemento de $q_{2}$ e assim por diante, no $j$-ésimo passo, terei um vetor que é ortogonal aos anteriores, o que significa que removo todos os componentes anteriores, deixando o vetor projetado como uma combinação linear de $\left\{ q_{k},\ldots \right\}$

Ok! Se definirmos $P_{1} = I$, podemos reescrever $v_{j} = P_{j}a_{j}$ como:

$$
v_{j} = P_{\perp q_{j - 1}}\ldots P_{\perp q_{2}}P_{\perp q_{1}}a_{j}
$$

O novo algoritmo modificado é baseado nesta nova equação. Podemos obter o mesmo resultado declarado na versão anterior do algoritmo como:

$$
v_{j}^{(1)} = a_{j}
$$

$$
v_{j}^{(2)} = P_{\perp q_{1}}v_{j}^{(1)}
$$

$$
v_{j}^{(3)} = P_{\perp q_{2}}v_{j}^{(2)}
$$

$$
v_{j} = v_{j}^{(j)} = P_{\perp q_{j - 1}}v_{j}^{(j - 1)}
$$

Podemos reescrevê-lo na forma de pseudocódigo:

1.  **para** $i = 1$ **até** $n$

    1.  $v_{i} = a_{i}$

2.  **para** $i = 1$ **até** $n$

    1.  $r_{ii} = \| v_{i}\|$

    2.  $q_{i} = \frac{v_{i}}{r_{ii}}$

    3.  **para** $j = i + 1$ **até** $n$

        1.  $r_{ij} = q_{i}^{\ast}v_{j}$

        2.  $v_{j} = v_{j} - r_{ij}q_{i}$

<a id="gram-schmidt-como-ortonormalizacao-triangular"></a>
<a id="secao-27"></a>

## Gram-Schmidt como Ortonormalização Triangular

Podemos interpretar cada passo do algoritmo de Gram-Schmidt como uma multiplicação à direita por uma matriz triangular superior quadrada. Espere, o quê? Por quê? Pegue a matriz $R$: $$\begin{pmatrix} r_{11} & r_{12} & \ldots & r_{1n} \\ & r_{22} & & \vdots \\ & & \ddots & \vdots \\ & & & r_{nn} \end{pmatrix}$$

Você pode separá-la como: $$\begin{pmatrix} r_{11} & r_{12} & \ldots & r_{1n} \\ & 1 & & \vdots \\ & & \ddots & \vdots \\ & & & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 & \ldots & 0 \\ & r_{22} & & \vdots \\ & & \ddots & \vdots \\ & & & 1 \end{pmatrix}\ldots$$

Então, podemos ver facilmente que, para a $j$-ésima matriz, a inversa dela é:

$$
\begin{pmatrix} \ddots & \\ & 1 \\ & & r_{jj} & r_{j(j + 1)} & \ldots \\ & & & \ddots \end{pmatrix}^{- 1} = \begin{pmatrix} \ddots & \\ & 1 \\ & & \frac{1}{r_{jj}} & - \frac{r_{j(j + 1)}}{r_{jj}} & \ldots \\ & & & \ddots \end{pmatrix}
$$

Isso significa que podemos entender o algoritmo de Gram-Schmidt como uma ortonormalização por matrizes triangulares

$$
AR_{1}R_{2.}..R_{n} = \widehat{Q}
$$

$$
R_{1}R_{2.}..R_{n} = R^{- 1}
$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Existência e unicidade](../fatoracao-qr/index.md#existencia-e-unicidade)
- Próximo: [Triangularização de Householder](../triangularizacao-de-householder/index.md)
