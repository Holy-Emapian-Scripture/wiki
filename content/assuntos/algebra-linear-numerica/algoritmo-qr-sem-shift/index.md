---
layout: "default"
title: "Algoritmo QR sem Shift"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 43
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-43"></a>

# Algoritmo QR sem Shift


<a id="convergencia-do-algoritmo-qr"></a>
<a id="secao-48"></a>

## Convergência do algoritmo QR

Show, agora a gente pode entender melhor como que esse algoritmo acha os autovalores e autovetores. A parte dos autovetores a gente consegue visualizara pela equação [\[unshifted-qr-eigenvectors-estimative\]](../iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md#unshifted-qr-eigenvectors-estimative), e pelo [\[unshifted-qr-and-sumultanious-iteration-equivalence\]](../iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md#unshifted-qr-and-sumultanious-iteration-equivalence), já que, se o método de iteração simultânea converge para autovetores e tanto ele quanto o algoritmo QR geram as mesmas matrizes, obviamente ambos vão ter as matrizes $Q$ convergindo para a matriz de colunas sendo os autovetores. Como $Q$ converge pra matriz de autovetores, por consequência, se eu faço $Q^{T}AQ$, isso vai convergir pra matriz com os autovalores de $A$ na diagonal (Diagonalização)

**Teorema**

Deixe que o [\[unshifted-qr-algorithm\]](../iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md#unshifted-qr-algorithm) seja aplicado em uma matriz real simétrica $A$ que os autovalores satisfazem $\vert \lambda_{1}\vert  > \vert \lambda_{2}\vert  > \ldots > \vert \lambda_{m}\vert$ e que a matriz de autovetores correspondente $Q$ não tem blocos singulares (Todos os blocos da matriz formam matrizes inversíveis). Então, conforme $k \rightarrow \infty$, $A^{(k)}$ converge linearmente com constante $\max\limits_{j\left( \vert \lambda_{j + 1}\vert /\vert \lambda_{j}\vert  \right)}$ para a matriz com os autovalores na diagonal e $Q^{(k)}$ converge na mesma velocidade para $Q$

------------------------------------------------------------------------

<a id="iteracao-simultanea"></a>
<a id="secao-46"></a>

## Iteração Simultânea

Conforme $k \rightarrow \infty$, os vetores $v_{j}^{(k)}$ vão convergindo para múltiplos do autovetor dominante (Associado ao autovalor). Quando eu digo múltiplos, eu quero dizer muito próximos. Por mais que o span deles converja para algo útil, eles em si formam uma base muito mal condicionada.

Vamos fazer uma alteração então, vamos construir uma sequência de matrizes $Z^{(k)}$ tal que $C\left( Z^{(k)} \right) = C\left( V^{(k)} \right)$

<a id="simultanious-iteration"></a>

1.  **function** SimultaniousAlgorithm($A \in {\mathbb{C}}^{m \times m}$) {

    1.  Escolha ${\hat{Q}}^{(0)} \in {\mathbb{R}}^{m \times n}$ com colunas ortonormais

    2.  **for** $k = 1,2,3,\ldots$

        1.  $Z = A{\hat{Q}}^{(k - 1)}$

        2.  ${\hat{Q}}^{(k)},{\hat{R}}^{(k)} = \text{ qr}(Z)$ \# Fatoração Reduzida

2.  }

*Figura 15. Iteração Simultânea*

Assim é mais tranquilo de ver que $C\left( Z^{(k)} \right) = C\left( {\hat{Q}}^{(k)} \right) = C\left( A^{k}{\hat{Q}}^{(0)} \right)$. Matematicamente falando, esse novo método converge igual o método anterior (Sob as mesmas circunstâncias)

**Teorema**

O [\[simultanious-iteration\]](#simultanious-iteration) gera as mesmas matrizes ${\hat{Q}}^{(k)}$ que os passos de iteração [\[simultanious-iterations-step-1\]](../iteracoes-simultaneas-nao-normalizadas/index.md#simultanious-iterations-step-1) ~ [\[simultanious-iterations-step-2\]](../iteracoes-simultaneas-nao-normalizadas/index.md#simultanious-iterations-step-2) considerados no [\[simultanious-iteration-convergence\]](../iteracoes-simultaneas-nao-normalizadas/index.md#simultanious-iteration-convergence) e sob as mesmas condições \[simultanious-iterations-assumption-1\] e \[simultanious-iterations-assumption-2\]

<a id="iteracao-simultanea-leftrightarrow-algoritmo-qr"></a>
<a id="secao-47"></a>

## Iteração Simultânea $\Leftrightarrow$ Algoritmo QR

Beleza, agora a gente pode tentar entender o algoritmo QR (Não é um algoritmo pra calcular a fatoração QR, mas usa ela para calcular os autovalores e autovetores de A). A gente vai aplicar a iteração simultânea na identidade, assim, a gente até remove os acentos de ${\hat{Q}}^{(k)}$ e ${\hat{R}}^{(k)}$. A gente vai fazer umas substituições que eu vou explicar direitinho depois.

Primeiro de tudos, temos um algoritmo de iteração simultânea com uma leve adaptação, mostraremos que ele e o algoritmo qr são equivalentes

<a id="modified-simultanious-iteration"></a>

1.  **function** ModifiedSimultaniousAlgorithm($A \in {\mathbb{C}}^{m \times m}$) {

    1.  ${\underline{Q}}^{(0)} = I$

    2.  **for** $k = 1,2,3,\ldots$

        1.  $Z = A{\underline{Q}}^{(k - 1)}$

        2.  ${\underline{Q}}^{(k)},R^{(k)} = \text{ qr}(Z)$

        3.  $A^{(k)} = \left( {\underline{Q}}^{(k)} \right)^{T}A{\underline{Q}}^{(k)}$

        4.  ${\underline{R}}^{(k)} = R^{(k)}R^{(k - 1)}\ldots R^{(1)}$

2.  }

*Figura 16. Iteração Simultânea Modificada*

Aqui, a gente colocou ${\underline{Q}}^{(k)}$ com esse traço em baixo só pra diferenciar o $Q$ do algoritmo de iteração simultânea e do algoritmo QR

<a id="unshifted-qr-algorithm"></a>

1.  **function** UnshiftedQRAlgorithm($A \in {\mathbb{C}}^{m \times m}$) {

    1.  $A^{(0)} = A$

    2.  **for** $k = 1,2,3,\ldots$

        1.  $Q^{(k)},R^{(k)} = \text{ qr}\left( A^{(k - 1)} \right)$

        2.  $A^{(k)} = R^{(k)}Q^{(k)}$

        3.  ${\underline{Q}}^{(k)} = Q^{(1)}Q^{(2)}\ldots Q^{(k)}$

        4.  ${\underline{R}}^{(k)} = R^{(k)}R^{(k - 1)}\ldots R^{(1)}$

2.  }

*Figura 17. Algoritmo QR sem Shift*

Agora podemos visualizar a convergência de ambos os algoritmos.

<a id="unshifted-qr-and-sumultanious-iteration-equivalence"></a>

**Teorema**

O [\[modified-simultanious-iteration\]](#modified-simultanious-iteration) e [\[unshifted-qr-algorithm\]](#unshifted-qr-algorithm) geram a mesma sequência de matrizes ${\underline{Q}}^{(k)}$, ${\underline{R}}^{(k)}$ e $A^{(k)}$, de tal forma que: $$A^{k} = {\underline{Q}}^{(k)}{\underline{R}}^{(k)}$$<a id="unshifted-qr-eigenvectors-estimative"></a> junto da projeção $$A^{(k)} = \left( {\underline{Q}}^{(k)} \right)^{T}A{\underline{Q}}^{(k)}$$<a id="unshifted-qr-eigenvalues-estimative"></a>

**Demonstração**

Vamos fazer indução em $k$

- Caso base ($k = 1$): Trivial, já que $A^{(0)} = {\underline{Q}}^{(0)} = {\underline{R}}^{(0)} = I$ e $A^{(0)} = A$

- Passo indutivo ($k > 1$): A parte de que $A^{(k)} = \left( {\underline{Q}}^{(k)} \right)^{T}A{\underline{Q}}^{(k)}$ por definição de $A^{k}$ ([\[modified-simultanious-iteration\]](#modified-simultanious-iteration)). Então só precisamos conferir que $A^{k} = {\underline{Q}}^{(k)}{\underline{R}}^{(k)}$, e fazemos isso, primeiro, considerando o algoritmo de iteração simultânea (Assumindo que isso é válido para $A^{k - 1}$): $$A^{k} = A{\underline{Q}}^{(k - 1)}{\underline{R}}^{(k - 1)} = {\underline{Q}}^{(k)}R^{(k)}{\underline{R}}^{(k - 1)} = {\underline{Q}}^{(k)}{\underline{R}}^{(k)}$$ Agora, faremos o mesmo assumindo o algoritmo QR $$A^{k} = A{\underline{Q}}^{(k - 1)}{\underline{R}}^{(k - 1)} = {\underline{Q}}^{(k - 1)}A^{(k - 1)}{\underline{R}}^{(k - 1)} = {\underline{Q}}^{(k)}{\underline{R}}^{(k)}$$ Então verificamos que $$A^{(k)} = \left( Q^{(k)} \right)^{T}A^{(k - 1)}Q^{(k)} = \left( {\underline{Q}}^{(k)} \right)^{T}A{\underline{Q}}^{(k)}$$

<a id="iteracoes-simultaneas-nao-normalizadas"></a>
<a id="secao-45"></a>

## Iterações Simultâneas Não-normalizadas

A gente vai tentar relacionar (Eu vou tentar traduzir o que o livro fala né) o [\[iteration-qr\]](../o-algoritmo-qr/index.md#iteration-qr) com um algoritmo chamado **iterações simultâneas** que tem um comportamento mais simples de visualizar (De acordo com o livro, pq tudo pra ele é fácil né)

A ideia do algoritmo é aplicar o [\[power-iteration\]](../../quociente-de-rayleigh-e-iteracao-inversa/iteracao-por-potencias/index.md#power-iteration) (Iteração por Potências) para vários vetores simultaneamente. Vamo supor que a gente tem $n$ vetores LI iniciais $v_{1}^{(0)},\ldots,v_{n}^{(0)}$. Se a gente aplica $A^{k}v_{1}^{(0)}$, conforme $k \rightarrow \infty$, isso converge para o autovetor correspondente ao autovalor de maior valor absoluto (Com algumas condições adequadas), meio que parece plausível que $\text{span}\left\{ A^{k}v_{1}^{(0)},A^{k}v_{2}^{(0)},\ldots,A^{k}v_{n}^{(0)} \right\}$ converge para $\text{span}\left\{ q_{1},\ldots,q_{n} \right\}$ que é o espaço formado pelos autovetores associados aos $n$ (Novamente com condições adequadas). Ué, mas quando eu aplico o método a um único vetor ele não converge pro maior? Como que aplicar a vários muda isso? Vou primeiro definir uma estrutura importante no algoritmo e depois faço uma explicação mais simplificada e uma analogia pra entender isso melhor

Na notação matricial, fazemos: $$V^{(0)} = \begin{pmatrix} & \vert  & & \vert  & \\ v_{1}^{(0)} & \vert  & \ldots & \vert  & v_{n}^{(0)} \\ & \vert  & & \vert  & \end{pmatrix}$$<a id="simultanious-iterations-step-1"></a>

E definimos $$V^{(k)} = A^{k}V^{(0)} = \begin{pmatrix} & \vert  & & \vert  & \\ v_{1}^{(k)} & \vert  & \ldots & \vert  & v_{n}^{(k)} \\ & \vert  & & \vert  & \end{pmatrix}$$

Vamos tentar entender a pergunta que fiz antes. Quando a gente aplica o algoritmo a um único vetor, ele vai se alinhando ao vetor dominante, porém, se a gente faz o mesmo com vários vetores **ao mesmo tempo**,ou seja, eu aplico na matriz, não faz muito sentido isso ocorrer. Pensa que se isso acontecesse, eu ia ter como resultado uma matriz que todas as colunas fossem iguais (Meio esquisito isso). O que acontece é que o espaço das colunas de $V^{(0)}$ vai “girando” e se alinhando ao espaço que falei dos autovetores de $A$

Imagine 3 agulhas em 3 direções diferentes (De forma que as agulhas representem vetores LI, e to falando apenas 3 pra representar ${\mathbb{R}}^{3}$, mas se aplica pra outros espaços). Aplicar o método de potência em um único vetor é como se aplicássemos um campo magnético que direciona todas as agulhas pra direção norte (Que seria a direção do autovetor associado ao maior autovalor). Aplicar na matriz $V^{(0)}$ seria aplicar um campo magnético complexo, em que cada vetor $v_{j}^{(0)}$ fica virado pra direção que ele “sente mais”

Beleza, vamos continuar então. A gente ta interessado em $C\left( V^{(k)} \right)$. Que tal a gente pegar uma boa base desse espaço? Uma boa ideia é a fatoração QR dessa matriz né? Já que as colunas de $Q$ são uma base ortonormal de $C\left( V^{(k)} \right)$ $${\hat{Q}}^{(k)}{\hat{R}}^{(k)} = V^{(k)}$$<a id="simultanious-iterations-step-2"></a>

Aqui estamos vendo a fatoração reduzida, logo, ${\hat{Q}}^{(k)}$ é $m \times n$ e ${\hat{R}}^{(k)}$ é $n \times n$. Bem, se as colunas de ${\hat{Q}}^{(k)}$ vão formando uma base do span dos autovetores que eu comentei antes, então faz sentido elas irem convergindo para os próprios autovetores de $A$ ($\pm q_{1},\ldots, \pm q_{n}$). A gente pode argumentar melhor sobre isso fazendo uma expansão das colunas de $V^{(0)}$ e $V^{(k)}$ como combinação linear dos autovetores de $A$ que nem a gente fez em uma lecture anterior $$\begin{array}{r} v_{j}^{(0)} = a_{1j}q_{1} + \ldots + a_{mj}q_{m} \\ v_{j}^{(k)} = \lambda_{1}^{k}a_{1j}q_{1} + \ldots + \lambda_{m}^{k}a_{mj}q_{m} \end{array}$$<a id="v_j-decomposition"></a> Mas não precisamos entrer em detalhes mais aprofundados. Assim como na lecture anterior, resultados vão convergir quando satisfazemos duas condições.

1.  A primeira é que, ao calcularmos $n$ autovalores, todos tenham valor absoluto distintos $$\vert \lambda_{1}\vert  > \vert \lambda_{2}\vert  > \ldots > \vert \lambda_{n}\vert  > \vert \lambda_{n + 1}\vert  \geq \vert \lambda_{n + 2}\vert  \geq \ldots \geq \vert \lambda_{m}\vert$$<a id="simultanious-iterations-assumption-1"></a>

2.  A segunda condição é que os valores $a_{ij}$ na decomposição dos $v_{j}^{(i)}$ que comentei antes sejam, de certa forma, não-singulares. O que isso quer dizer? Significa que eu preciso formar uma boa mistura dos meus autovetores originais. Tipo, se eu formar $v_{j}^{(i)}$ ortogonal a algum autovetor, ele não vai ser muito bem aproximado pelo meu algoritmo. Vou formarlizar essa condição um pouco. Vamos definir $\hat{Q}$ como a matriz $m \times n$ que as colunas são os autovetores $q_{1},\ldots,q_{n}$ de $A$. Então podemos formalizar isso escrevendo: $$\text{ Todas as submatrizes consequentes de }{\hat{Q}}^{T}V^{(0)}\text{ são inversíveis }$$<a id="simultanious-iterations-assumption-2"></a> Eu posso definir como essa multiplicação pois eu vou ter que o elemento $ij$ dessa matriz vai ser $q_{i}^{T}v_{j}^{(0)}$, que ao olharmos para a Equação [\[v_j-decomposition\]](#v_j-decomposition), é igual a $a_{ij}$

<a id="simultanious-iteration-convergence"></a>

**Teorema**

Suponha que a iteração [\[simultanious-iterations-step-1\]](#simultanious-iterations-step-1) e [\[simultanious-iterations-step-2\]](#simultanious-iterations-step-2) é realizada e as condições \[simultanious-iterations-assumption-1\] e \[simultanious-iterations-assumption-2\] são satisfeitas. Conforme $k \rightarrow \infty$, as colunas da matriz $Q^{(k)}$ vão convergindo linearmente para os autovetores de $A$: $$\| q_{j}^{(k)} - \pm q_{j}\| = O\left( C^{k} \right)$$ para cada $j$ com $1 \leq j \leq n$ e $C < 1$ é a constante $\max\limits_{1 \leq k \leq n}\left( \vert \lambda_{k + 1}\vert /\vert \lambda_{k}\vert  \right)$

**Demonstração**

Vamos transformar $\hat{Q} \in {\mathbb{R}}^{m \times n}$ em $Q \in {\mathbb{R}}^{m \times m}$, de forma que $Q$ tenha como colunas todos os autovetores de $A$. Definimos também $\Lambda$ como a matriz de autovalores de $A$ de tal forma que $A = Q\Lambda Q^{T}$. Defina também $\hat{\Lambda}$ como sendo o bloco $n \times n$ de $\Lambda$ com os autovalores associados a matriz $\hat{Q}$. $$V^{(k)} = A^{k}V^{(0)} = Q\Lambda^{k}Q^{T}V^{(0)} = \hat{Q}\Lambda^{k}{\hat{Q}}^{T}V^{(0)} + O\left( \vert \lambda_{k + 1}\vert  \right)$$ Se a condição \[simultanious-iterations-assumption-2\] for satisfeita, podemos fazer uma manipulação simples $$V^{(k)} = \left( \hat{Q}\Lambda^{k} + O\left( \vert \lambda_{k + 1}\vert  \right)\left( {\hat{Q}}^{T}V^{(0)} \right)^{- 1} \right){\hat{Q}}^{T}V^{(0)}$$ Como ${\hat{Q}}^{T}V^{(0)}$ é inversível, $C\left( V^{(k)} \right) = C\left( \hat{Q}\Lambda^{k} + O\left( \vert \lambda_{k + 1}\vert  \right)\left( {\hat{Q}}^{T}V^{(0)} \right)^{- 1} \right)$. Ou seja, a gente consegue perceber que o espaço vai convergindo para o span dos autovetores de $A$. A gente pode até tentar quantificar a convergência, mas não tem necessidade

<a id="o-algoritmo-qr"></a>
<a id="secao-44"></a>

## O Algoritmo QR

A versão mais simplificada parece coisa de doido.

<a id="iteration-qr"></a>

1.  **function** QRIteration($A \in {\mathbb{C}}^{m \times m}$) {

    1.  $A^{(0)} = A$

    2.  **for** $k = 1,2,3,\ldots$

        1.  $Q^{(k)},R^{(k)} = \text{ qr}\left( A^{(k - 1)} \right)$

        2.  $A^{(k)} = R^{(k)}Q^{(k)}$

2.  }

*Figura 13. Algoritmo QR*

É um algoritmo estupidamente simples, mas sobre certas circunstâncias, esse algoritmo converge para a forma de Schur de uma matriz (Triangular superior se for arbitrária e diagonal se for simétrica). Por questão de simplicidade, vamos continuar assumindo que $A$ é simétrica

Pra que a redução a forma diagonal seja útil pra achar autovalor, a gente precisa que transformações similares estejam envolvidas. “Oxe, daonde?”. Quando a gente faz $A^{(k)} = R^{(k)}Q^{(k)}$, a gente pode substituir $R^{(k)}$ por $\left( Q^{(k)} \right)^{T}A^{(k - 1)}$, ou seja: $A^{(k)} = \left( Q^{(k)} \right)^{T}A^{(k - 1)}Q^{(k)}$ (Mesmo que $M^{- 1}AM$). O [\[iteration-qr\]](#iteration-qr) converge cubicamente assim como o do [\[rayleigh-quotient-iteration\]](../../quociente-de-rayleigh-e-iteracao-inversa/iteracao-do-quociente-de-rayleigh/index.md#rayleigh-quotient-iteration), porém, para o algoritmo ser prático, precisamos introduzir **shifts**. Introdução de **shifts** é 1 de 3 modificações que fazemos nesse algoritmo para que ele fique prático.

1.  Antes de iniciar a iteração, $A$ é reduzida a forma tridiagonal

2.  Em vez de $A^{(k)}$, usamos uma matriz trocada $A^{(k)} - \mu^{(k)}I$ que é fatorada a cada iteração e $\mu^{(k)}$ é uma estimativa de autovalor

3.  Quando possível (Especialmente quando um autovalor é encontrado) nós quebramos $A^{(k)}$ em submatrizes

<a id="shifted-qr-with-well-known-shifts"></a>

1.  **function** ShiftedQR($A \in {\mathbb{C}}^{m \times m}$) {

    1.  $\left( Q^{(0)} \right)^{T}A^{(0)}Q^{(0)} = A$

    2.  **for** $k = 1,2,3,\ldots$

        1.  Escolha um shift $\mu^{(k)}$

        2.  $Q^{(k)},R^{(k)} = \text{ qr}\left( A^{(k - 1)} - \mu^{(k)}I \right)$

        3.  $A^{(k)} = R^{(k)}Q^{(k)} + \mu^{(k)}I$

        4.  **Se** qualquer elemento $A_{j,j + 1}^{(k)}$ fora da diagonal é suficientemente próximo de 0

            1.  $A_{j,j + 1} = A_{j + 1,j} = 0$ para obter

            2.  $\begin{pmatrix} A_{1} & 0 \\ 0 & A_{2} \end{pmatrix} = A^{(k)}$

            3.  e agora aplicamos o algoritmo em $A_{1}$ e $A_{2}$

2.  }

*Figura 14. Algoritmo QR com **shifts***

Esse é um algoritmo muito usado desde 1960. Mas perceba que precisamos ter uma noção prévia de quanto vale os autovalores da matriz, pois necessitamos ter aproximações particularmente boas de $\mu^{(k)}$ para que o algoritmo tenha uma boa convergência.Porém, nos anos 1990 um competidor surgiu (Vai ser discutido na lecture 30 e a gente detalha o algoritmo com shifts na próxima lecture).

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Iteração do Quociente de Rayleigh](../quociente-de-rayleigh-e-iteracao-inversa/index.md#iteracao-do-quociente-de-rayleigh)
- Próximo: [Iterações Simultâneas Não-normalizadas](#iteracoes-simultaneas-nao-normalizadas)
