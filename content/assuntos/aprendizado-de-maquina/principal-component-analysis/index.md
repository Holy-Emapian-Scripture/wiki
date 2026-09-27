---
layout: "default"
title: "Principal Component Analysis"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 4
---

[Aprendizado de Máquina](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-4"></a>

# Principal Component Analysis


<a id="definicoes"></a>
<a id="secao-6"></a>

## Definições

O PCA pode ser interpretado como duas definições distintas que dão origem ao mesmo resultado

- Projeção ortogonal dos dados em um espaço de menor dimensão (Subespaço Principal) de forma que a variância dos dados seja maximizada

- Projeção Linear que minimiza o custo médio de projeção

Antes de entrarmos em detalhes sobre essas definições, vamos colocar algumas definições úteis que, nós já sabemos, mas refrescar a nossa memória nunca é demais

**Definição: Projetar sobre um subespaço**

Dado um ponto $x \in {\mathbb{R}}^{D}$, sua projeção ortogonal no subespaço é o ponto $\hat{x}$ nesse subespaço mais próximo de $x$. Como consequência, temos que $$\left( x - \hat{x} \right)^{T}u = 0$$ onde é um vetor qualquer no subespaço

**Teorema: Projeção ortogonal**

Seja $X$ uma matriz ${\mathbb{R}} \times {\mathbb{R}}$, a projeção do vetor $y$ no espaço coluna de $X$ é dada por: $$\hat{y} = {X\left( X^{T}X \right)}^{- 1}X^{T}y$$ se $X$ é ortogonal, então $$\hat{y} = XX^{T}y$$

<a id="base-coefficients"></a>

**Teorema: Coeficientes de Base**

Seja $\left\{ q_{1},\ldots,q_{D} \right\}$ uma base ortogonal do ${\mathbb{R}}^{D}$ e $x \in {\mathbb{R}}^{D}$ tal que $$x = \sum_{i = 1}^{D}\alpha_{i}q_{i}$$ então temos que $$Qx = \begin{pmatrix} \alpha_{1} & \ldots & \alpha_{D} \end{pmatrix}^{T}$$ onde $Q$ é a matriz cujas colunas são os vetores da base.

<a id="introducao"></a>
<a id="secao-5"></a>

## Introdução

Nós que trabalhamos com análise de dados, muitas vezes nos deparamos com datasets assustadores, com muitas dimensões, o que acaba dificultando nossa capacidade de fazer análises e visualizações. Visando solucionar esse nosso problema, é que o PCA entra em cena. Ele é um método de redução de dimensionalidade que busca encontrar uma representação mais compacta dos dados, preservando ao máximo a variância dos dados originais. O PCA é amplamente utilizado em diversas áreas, como reconhecimento de padrões, compressão de imagens e análise exploratória de dados.

<a id="maxima-variancia"></a>
<a id="secao-7"></a>

## Máxima Variância

Seja $X \in {\mathbb{R}}^{N \times D}$ onde $x_{i}^{T}$ é a $i$-ésima linha de $X$, queremos projetar $X$ em um subespaço ${\mathbb{R}}^{M}$ com $M < D$ enquanto maximizamos a variância dos dados projetados.

Supondo que $M = 1$, pegamos $u_{1} \in {\mathbb{R}}^{D}$ tal que $u_{1}^{T}u_{1} = 1$ então pegamos quanto de $u_{1}$ compõe o vetor $x_{i}$ com $u_{1}^{T}x_{i}$ ([\[base-coefficients\]](../definicoes/index.md#base-coefficients)). Vamos definir a média dos dados projetados como $$u_{1}^{T}\overline{x} = \frac{1}{N}\sum_{i = 1}^{N}u_{1}^{T}x_{i}$$

e também definimos a variância deles como $$u_{1}^{T}Su_{1} = \frac{1}{N}\sum_{i = 1}^{N}\left( u_{1}^{T}x_{i} - u_{1}^{T}\overline{x} \right)^{2}$$

e $$S = \frac{1}{N}\sum_{n = 1}^{N}\left( x_{n} - \overline{x} \right)\left( x_{n} - \overline{x} \right)^{T}$$

Agora, queremos maximizar $u_{1}^{T}Su_{1}$ com respeito a $u_{1}$ com a restrição de $u_{1}^{T}u_{1} = 1$. Antes de fazermos isso mesmo, a lógica desse processo é que queremos entender qual a direção do espaço que mais contribui com a variância dos dados, ou seja, qual a direção que mais “espalha” os dados. Para isso, vamos utilizar o método de multiplicadores de Lagrange para maximizar $u_{1}^{T}Su_{1}$ com a restrição de $u_{1}^{T}u_{1} = 1$. Definimos a função lagrangiana como: $$\mathcal{L}(u_{1},\lambda) = u_{1}^{T}Su_{1} - \lambda\left( u_{1}^{T}u_{1} - 1 \right)$$

Realizando as contas necessárias, chegamos que $$Su_{1} = \lambda u_{1}$$

Ou seja, a direção que mais contribui com a variância dos dados é o autovetor de $S$ correspondente ao maior autovalor. Esse autovetor é chamado de *primeira componente principal*. Sabendo disso, podemos utilizar de **indução forte** para mostrar que a segunda componente principal é o autovetor de $S$ correspondente ao segundo maior autovalor, e assim por diante. Dessa forma, as $M$ primeiras componentes principais são os $M$ autovetores de $S$ correspondentes aos $M$ maiores autovalores.

<a id="minimzando-o-erro-de-projecao"></a>
<a id="secao-8"></a>

## Minimzando o Erro de Projeção

Pegamos um set $\left\{ u_{1},u_{2},\ldots,u_{D} \right\}$ de vetores otornomais em ${\mathbb{R}}^{D}$. Pelo [\[base-coefficients\]](../definicoes/index.md#base-coefficients), sabemos que $$x_{n} = \sum_{i = 1}^{D}\left( x_{n}^{T}u_{i} \right)u_{i}$$

Porém, queremos aproximar $x_{n}$ usando um conjunto de só $M < D$ variáveis. Escrevemos então: $${\hat{x}}_{n} = \sum_{i = 1}^{M}\underset{\text{ Depende de }x_{n}}{\underbrace{z_{ni}}}u_{i} + \sum_{i = M + 1}^{D}\underset{\text{ Constante em }x_{n}}{\underbrace{b_{i}}}u_{i}$$

E queremos então minimizar $$J = \frac{1}{N}\sum_{n = 1}^{N}\| x_{n} - {\hat{x}}_{n}\|^{2}$$

Derivando essa função de custo com relação a $z_{ni}$ e $b_{i}$ e igualando a zero e usando das condições de ortogonalidade, chegamos que $$z_{ni} = x_{n}^{T}u_{i}$$ $$b_{i} = {\overline{x}}^{T}u_{i}$$

substituindo, obtemos então: $$x_{n} - {\hat{x}}_{n} = \sum_{i = M + 1}^{D}\left\{ \left( x_{n}^{T} - {\overline{x}}^{T} \right)u_{i} \right\} u_{i}$$

com isso, conseguimos achar uma fórmula para $J$ $$J = \frac{1}{N}\sum_{n = 1}^{N}\sum_{i = M + 1}^{D}\left\{ \left( x_{n}^{T} - {\overline{x}}^{T} \right)u_{i} \right\}^{2} = \sum_{i = M + 1}^{D}u_{i}^{T}Su_{i}$$

Agora, só nos falta otimizar $J$ com relação à $u_{i}$ e aplicar a otimização com as condições de ortogonalidade. Vamos primeiro considerar o caso $M = 1$, temos que a função de lagrange é dada por $$\mathcal{L}(u_{1},\lambda) = \sum_{i = 2}^{D}u_{i}^{T}Su_{i} - \sum_{i = 2}^{D}\lambda_{i}\left( u_{i}^{T}u_{i} - 1 \right)$$

derivando essa função e aplicando as regras de otimização restrita, chegamos que $$Su_{i} = \lambda_{i}u_{i}$$

Novamente, chegamos na conclusão de que os autovetores de $S$ são as direções que minimizam o erro de projeção. E, novamente, podemos utilizar de indução forte para mostrar que os autovetores correspondentes aos maiores autovalores são as direções que minimizam o erro de projeção.

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Conteúdos relacionados

- [SVD — Álgebra Linear Numérica](../../algebra-linear-numerica/estabilidade-de-algoritmos-de-minimos-quadrados/index.md#svd)
- [SVD — Álgebra Linear Numérica](../../algebra-linear-numerica/svd/index.md)


## Percurso de estudo

[Trilha: A3](../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [O Algoritmo](../k-means/index.md#o-algoritmo)
- Próximo: [Gaussian and Bernoulli Mixture Models](../gaussian-and-bernoulli-mixture-models/index.md)
