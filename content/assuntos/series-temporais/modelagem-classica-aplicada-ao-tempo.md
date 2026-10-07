---
layout: "default"
title: "Modelagem Clássica aplicada ao Tempo"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/Recaps/A1.typ"
trilha: "../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 4
---

[Séries Temporais](index.md)

<!-- wiki:original:inicio -->
<a id="secao-8"></a>

# Modelagem Clássica aplicada ao Tempo

------------------------------------------------------------------------

<a id="secao-9"></a>

## Modelo linear padrão

É o modelo mais simples que podemos utilizar para modelar a dependência entre uma variável dependente $y_{t}$ e variáveis explicativas $x_{it}$ ao longo do tempo. Sua base é a [regressão linear](../aprendizado-de-maquina/regressao-linear.md). Já vimos esse modelo $n$ vezes nos semestres passados, então vou reescrever apenas os passos mais importantes

$$
y_{t} = \beta_{0} + \sum_{i = 1}^{P}\beta_{i}x_{it} + \varepsilon_{t}\text{\quad\quad}\varepsilon_{t} \sim N\left( 0,\sigma^{2} \right)
$$

ou, em forma matricial

$$
y = X\beta + \varepsilon\text{\quad\quad}\varepsilon \sim N\left( 0,\sigma^{2}I \right) \Rightarrow y \sim N\left( X\beta,\sigma^{2}I \right)
$$

onde $y \in {\mathbb{R}}^{T}$ é o vetor das observações da variável dependente, $X \in {\mathbb{R}}^{T \times P}$ é a matriz de observações das variáveis explicativas, $\beta \in {\mathbb{R}}^{P}$ é o vetor de pesos atribuindo a importância de cada parâmetro para explicar $y$ e $\varepsilon \in {\mathbb{R}}^{T}$ é um ruído gaussiano. Com essa estrutura, podemos obter o estimador de [máxima verossimilhança](../inferencia-estatistica/estatistica-frequentista.md#secao-14) de $\beta$

$$
\hat{\beta} = \left( X^{T}X \right)^{- 1}X^{T}y
$$

<a id="secao-10"></a>

## Balanço Viés-Variância

Vale relembrar que dentro do ramo da estatística (inclusive das séries temporais), sempre existirá o balanço **viés e variância**. O erro mais comum de se minimizar em contextos estatísticos é o erro quadrático médio

$$
{\mathbb{E}}\left\lbrack \left( y_{t} - {\hat{y}}_{t} \right)^{2} \right\rbrack = {\text{ Bias}\left( {\hat{y}}_{t} \right)}^{2} + {\mathbb{V}}\left\lbrack {\hat{y}}_{t} \right\rbrack^{2} + \sigma^{2}
$$

Obter modelos mais precisos na previsão de $y_{t}$ (com menos viés) acaba resultando em modelos com variação alta (mudanças pequenas nos dados podem impactar muito os resultado) e vice-versa

<a id="secao-11"></a>

## Regularização Lasso e Ridge

<a id="secao-12"></a>

### Lasso (Least Absolute Shrinkage and Selection Operator)

Em vez de minimizarmos simplesmente o erro quadrático, adicionamos um peso nos valores absolutos dos coeficientes, de forma que se eles crescem muito em módulo, a nossa função de perca não diminui como esperado

$$
\sum_{t = 1}^{T}\left( y_{t} - {\hat{y}}_{t} \right)^{2} + \lambda\sum_{i = 1}^{P}\vert \beta_{i}\vert
$$

Essa abordagem tente a zerar alguns coeficientes, indicando quais coeficientes realmente influenciam ou não
<a id="secao-13"></a>

### Ridge Regression

Em vez dos valores absolutos, usamos a soma dos quadrados

$$
\sum_{t = 1}^{T}\left( y_{t} - {\hat{y}}_{t} \right)^{2} + \lambda\sum_{i = 1}^{P}\beta_{i}^{2}
$$

Essa abordagem não costuma zerar os coeficientes, mas os puxa para muito próximo de $0$

<a id="secao-14"></a>

## Generalized Additive Models (GAM)

Extensão dos modelos lineares, permitindo que cada variável possua uma função não-linear associada com ela. A estrutura do GAM é dada por

$$
y_{t} = f_{1}\left( x_{1t} \right) + \ldots + f_{p}\left( x_{pt} \right) + \varepsilon_{t}
$$

Aqui, $f_{j}( \cdot )$ são funções não-lineares suaves que modelam a relação entre $y_{t}$ e $x_{jt}$. O exemplo mais conhecido de GAM são os modelos polinomiais

<a id="secao-15"></a>

## Deep Learning (DL)

Em deep learning, expressamos a relação entre $y_{t}$ e suas covariáveis através de uma função complexa $f$

$$
y_{t} = f\left( x_{1t},\ldots,x_{pt} \right) + \varepsilon_{t}
$$

onde $f$ é uma função altamente flexível modelada por uma rede neural, capaz de capturar padrões complexos e não-lineares dos dados
<a id="secao-16"></a>

### Janelas, Batches e Seta do Tempo

As [redes neurais](../aprendizado-de-maquina/redes-neurais.md), durante seu treinamento, assumem uma hipótese que muitas vezes esquecemos, mas que são MUITO importantes no nosso contexto: os dados **podem ser trocados**, eu posso embaralhar minhas amostras **sem perca de informação**.

No entanto, o conceito de séries temporais não permite essa premissa, o que podemos fazer para mitigar isso? É aí que entram as **janelas**, onde empacotamos o passado e a dependência temporal entre elas. Por exemplo, imagine que temos a seguinte sequência:

$$
\left\{ 10,12,9,14,11,13,8,15... \right\}
$$

Para podermos alimentar essas informações em uma rede neural, vamos criar uma janela de tamanho $3$ e gerar nossos conjuntos de dados e alvo

$$
\begin{array}{r} \ Janela\ 1\  \rightarrow \left\{ 10,12,9 \right\} \rightarrow 14 \\ Janela\ 2\  \rightarrow \left\{ 11,13,8 \right\} \rightarrow 15 \end{array}
$$

perceba que eu sempre pego um conjunto de $3$ valores e digo que o valor resultante (alvo) deve ser o seguinte e assim por diante. Dessa forma, a ordem **entre janelas** passa a ser irrelevante pois a informação de passado e como ele influencia na resposta está incorporada na própria janela. No entanto, vale ressaltar que a ordem **dentro da janela** é **sagrada** e **nunca deve ser alterada**, do contrário a informação temporal entre amostras **se perde**

Como nem tudo são flores, existem alguns pontos de atenção que devemos tomar cuidado. O primeiro é quando formos separar nossos dados nos conjuntos de **treino** e **teste**. Não podemos, ao realizar a divisão, criar janelas com dados em conjuntos diferentes. Por exemplo, se temos a seguinte série, e fazemos a seguinte separação:

$$
\left\{ \underset{\text{ TREINO}}{\underbrace{10,\ 12,\ 9,\ 14,\ 11}},\underset{\text{ TESTE}}{\underbrace{13,\ 8,\ 15}}\ldots \right\}
$$

em hipótese alguma podemos, dentro das nossas janelas de treino, ter uma janela tipo $\left\{ 14,11,13 \right\}$, pois estariamos misturando pontos de treino e teste, de forma que nosso modelo estaria vendo o futuro fora do controlado

Além disso, devemos tomar cuidado com **janelas sobrepostas**. Como falei antes, criamos as janelas para que elas possam ser independentes, no entanto, é possível criar janelas que não são independentes (ainda podemos embaralhar elas como artimanha computacional). Por exemplo, dado a série:

$$
\left\{ 10,12,9,14,11,13,8,15,\ldots \right\}
$$

as janelas $\left\{ 10,12,9 \right\}$ e $\left\{ 12,9,14 \right\}$ se sobrepõem, de tal forma que elas NÃO são independentes pois contém a mesma parcela do passado e como ela influencia nos valores internos. O ponto é que, para um SGD, você **pode** embaralhar essas janelas, mas isso não lhe permite tratá-las como **independentes**

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Introdução às Séries Temporais](introducao-as-series-temporais.md)
- Próximo: [Diagnóstico Visual](diagnostico-visual.md)
