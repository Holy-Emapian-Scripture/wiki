---
layout: "default"
title: "Método dos Vizinhos mais próximos (k-NN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 1
---

[Aprendizado de Máquina](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-1"></a>

# Método dos Vizinhos mais próximos (k-NN)


<a id="classificacao"></a>
<a id="secao-3"></a>

## Classificação

Seja $\mathcal{D} ≔ \left\{ \left( x_{1},y_{1} \right),\ldots,\left( x_{N},y_{N} \right) \right\} \subset \mathcal{X} \times \mathcal{Y}$ o conjunto de treinamento e $d:\mathcal{D} \times \mathcal{D} \rightarrow {\mathbb{R}}^{+} \cup \left\{ 0 \right\}$ uma função de **distância**. Vamos supor que queremos classificar um vetor $x \in \mathcal{X}$ arbitrário.

O método k-NN classifica o vetor $x$ atribuindo a ele a classe mais comum entre os rótulos dos pontos em $\mathcal{V}_{k}(x)$, ou seja: $$h(x) ≔ \text{ argmax}_{\left\{ y \in \mathcal{Y} \right\}}\sum_{\left\{ \left( x_{i},y_{i} \right) \in \mathcal{V}_{k}(x) \right\}}{\mathbb{I}}_{\left\{ y_{i} = y \right\}}$$ (De forma simplificada, o rótulo mais comum dentro do conjunto de vizinhos é o rótulo atribuído ao ponto $x$)

![Exemplo de classificação usando o método k-NN. O ponto $x$ é o ponto a ser classificado, os pontos azuis e vermelhos são os pontos do conjunto de treinamento, e as linhas tracejadas indicam as fronteiras de decisão do modelo. Aqui, se $k = 5$, ele vai classificar como **Classe 1** (vermelho)](../assets/knn-classification.png)

*Figura 1. Exemplo de classificação usando o método k-NN. O ponto $x$ é o ponto a ser classificado, os pontos azuis e vermelhos são os pontos do conjunto de treinamento, e as linhas tracejadas indicam as fronteiras de decisão do modelo. Aqui, se $k = 5$, ele vai classificar como **Classe 1** (vermelho)*

<a id="introducao-intuitiva"></a>
<a id="secao-2"></a>

## Introdução Intuitiva

O método dos vizinhos mais próximos (k-NN) é um algoritmo de aprendizado de máquina simples e eficaz usado para classificação e regressão. Ele funciona com base na ideia de que objetos semelhantes estão próximos uns dos outros no espaço de características. Para classificar um novo ponto, o k-NN identifica os k pontos mais próximos no conjunto de treinamento e atribui a classe mais comum entre esses vizinhos ao novo ponto.

O valor de k é um hiperparâmetro que pode ser ajustado para melhorar o desempenho do modelo. O k-NN é fácil de entender e implementar, mas pode ser computacionalmente caro para grandes conjuntos de dados, pois requer o cálculo das distâncias entre o novo ponto e todos os pontos do conjunto de treinamento.

Um das hipóteses fundamentais em ML é que existe algum nível de suavidade no mapeamento entre o espaço de entrada $\mathcal{X}$ e o de saída $\mathcal{Y}$. Em outras palavras, se dois elementos $x,x' \in \mathcal{X}$ são semelhantes, então eles devem ter saídas $y,y' \in \mathcal{Y}$ similares. O método dos k vizinhos mais próximos (k nearest neighbors, k-NN), proposto por Cover e Hart (1967), aplica diretamente esse conceito.

Nesse capítulo, vamos estudar como k-NN pode ser usados para problemas de classificação e regressão. Discutiremos o impacto do k e também da escolha de distância (ou métrica) para o espaço $\mathcal{X}$, que é primordial para a aplicação do método. Finalmente, estudaremos o comportamento do método k-NN quando a dimensionalidade do espaço $\mathcal{X}$ é alta

<a id="maldicao-da-dimensionalidade"></a>
<a id="secao-9"></a>

## Maldição da Dimensionalidade

A expressão maldição da dimensionalidade foi introduzida por Bellman (1957) e é comumente usada para descrever problemas causados pelo aumento exponencial do volume associado em função da dimensionalidade em espaços euclidianos. No caso do k-NN, esse aumento implica na esparsidade dos exemplos de treino, fazendo com que os k-vizinhos que procuramos estejam muito distantes.

Para ilustrar tal efeito, suponha que a distribuição ${\mathbb{P}}_{x}$ sobre os vetores de entrada $x_{1},\ldots,x_{N}$ seja uniforme sobre uma hiperbola $D$-dimensional $S_{D}$ centrada na origem e com raio unitário (Ou seja, todo ponto dentro dessa bola é uniformemente provável de ser escolhida para ser um vetor de entrada). Suponha também que queremos classificar o vetor de origem $z = (0,\ldots,0)^{T}$. Defina $r$ como o raio da hiperbola $S'_{D} \subseteq S_{D}$ que **contém os k vizinhos mais próximos de $z$**. Em esperança, o quão grande devemos esperar que $r$ seja? Antes, é intuitivo notar que ${\mathbb{P}}\left( x_{i} \in S'_{D} \right)$ é a razão dos volumes de $S'_{D}$ e $S_{D}$, ou seja: $${\mathbb{P}}\left( x_{i} \in S'_{D} \right) = {\mathbb{E}}_{x_{i} \sim {\mathbb{P}}_{x}}\left\lbrack {\mathbb{I}}_{x_{i} \in S'_{D}} \right\rbrack = \frac{\pi^{\frac{D}{2}}r^{D}}{\pi^{\frac{D}{2}}1^{D}} = r^{D}$$ Segue então que o número esperado de amostra, dentre as $N$ que possuímos, dentro de $S'_{D}$ é: $$\sum_{i = 1}^{N}{\mathbb{P}}\left( x_{i} \in S'_{D} \right) = Nr^{D}$$ Então, para que tenhamos, em esperança, $k$ vizinhos dentro de $S'_{D}$, devemos escolher $r$ tal que $r = \left( \frac{k}{N} \right)^{\frac{1}{D}}$, e a medida que $D$ cresce, temos: $$\lim\limits_{D \rightarrow \infty}r = \lim\limits_{D \rightarrow \infty}\left( \frac{k}{N} \right)^{\frac{1}{D}} = 1$$ Ou seja, quanto maior é a dimensão, maior é o raio de $S'_{D}$, o que mostra que a propriedade de “vizinhos próximos tem propriedades parecidas” é quebrada em altas dimensões, o que é um grande problema para o método k-NN.

<a id="secao-10"></a>

### Manifolds de baixa dimensão.

Na prática, não é incomum ver k-NN sendo utilizado em espaços de alta dimensão, como de imagens, e atingindo boas taxas de acurácia. Uma explicação para esse fenômeno é que os dados não estão uniformemente distribuídos e, na verdade, residem em um subespaço de baixa dimensão. Por exemplo, suponha que $\mathcal{X} \subset {\mathbb{R}}^{256 \times 256 \times 3}$ é o espaço de imagens de tamanho $256 \times 256$ com três canais de cores — red, green, and blue (RGB) — que contém um gato. Nós esperamos que ${\mathbb{P}}_{x}$ aloque massa zero para fotos de paisagens, obras de arte, etc

------------------------------------------------------------------------

<a id="qual-distancia-escolher"></a>
<a id="secao-5"></a>

## Qual distância escolher?

Até então, descrevemos o k-NN sem especificar exatamente o formato da função de distância $d$. No entanto, a escolha de uma distância apropriada pode ser crítica para o sucesso do método. Por exemplo, se os dados de entrada estão dispostos na superfície do globo terrestre, gostariamos de usar uma distância que considere a curvatura da terra (e.g., a distância esférica).

No entanto, raramente temos esse tipo de conhecimento sobre $\mathcal{X}$ e as escolhas mais comuns para $d$ incluem casos particulares da distância de Minkowski: $$d_{p}(x,z) = \| x - z\|_{p} = \left( \sum_{i = 1}^{D}\vert x_{i} - z_{i}\vert ^{p} \right)^{\frac{1}{p}}$$

que para valores de $p = 1$ chama-se distância quarteirão ou Manhattan; $p = 2$ resulta na distância euclidiana; e $p \rightarrow \infty$ retorna o máximo da diferença entre as componentes dos vetores. A notação $\| \cdot \|_{p}$ é também chamada de norma $L^{p}$ de um vetor.

Uma possível deficiência de normas $L^{p}$ é que elas não incorporam nenhuma informação sobre a distribuição ${\mathbb{P}}_{x}:\mathcal{X} \rightarrow {\mathbb{R}}^{+} \cup \left\{ 0 \right\}$ (Que é a distribuição que os vetores $x$ foram extraídos) — além do fato do suporte ser subconjunto dos reais. Por exemplo, se uma componente $x_{i}$ tiver escala muito maior às demais $x_{j \neq i}$, ela pode dominar o cálculo da distância, ofuscando diferenças nas demais componentes $x_{j \neq i}$. Além disso, $L^{p}$ são agnósticas a correlações entre componentes de $x \sim {\mathbb{P}}_{x}$ (Quando falamos em relação, dizemos da relação entre os componentes de um $x$. Por exemplo, digamos que $x_{i} = \left( x_{1i},x_{2i},\ldots,x_{Di} \right)$ então a feature $2$ e $3$ são altura e peso respectivamente, sabemos que quando altura cresce, peso tende a crescer, mas a distância de Minkowski não captura essa relação). Uma alternativa para cobrir esses problema é utilizar a distância de Mahalanobis: $$d_{M}(x,z) = \sqrt{(x - z)^{T}\Sigma^{- 1}(x - z)}$$ em que $\Sigma$ é a matriz de covariância dos dados de treinamento. Uma escolha típica para $\Sigma$ é a matriz de covariância amostral, não viezada: $$\Sigma = \frac{1}{N - 1}\sum_{i = 1}^{N}\left( x_{i} - \overset{-}{x} \right)\left( x_{i} - \overset{-}{x} \right)^{T}$$ onde $\overset{-}{x} ≔ \frac{1}{N}\sum_{i = 1}^{N}x_{i}$ é o vetor de médias amostrais. Observe que quando $\Sigma$ é igual à matriz identidade, temos a distância euclidiana. Mas, afinal, qual distância utilizar? De modo geral, a menos que tenhamos profundo conhecimento sobre a geometria de $\mathcal{X}$ , é impossível dar uma resposta direta. O melhor que podemos fazer é testar opções diferentes.

<a id="secao-6"></a>

### Normalização para média zero e variância um

Subtrair a média $\overset{-}{x} ≔ \frac{1}{N}\sum_{i = 1}^{N}x_{i}$ de cada vetor $x_{1},\ldots,x_{N}$ e, subsequentemente, multiplicá-los pela inversa da matriz diagonal $C$ com entradas: $$C_{jj} = \sqrt{\frac{1}{N - 1}\sum_{i = 1}^{N}\left( x_{ij} - {\overset{-}{x}}_{j} \right)^{2}}$$ é um procedimento comum em ML, sendo geralmente chamado de normalização ou padronização (standardization). Aplicar k-NN com $d(x,z) = \| x - z\|_{2}$ em dados transformados dessa maneira equivale a aplicar k-NN nos dados originais usando a distância de Mahalanobis com $\Sigma^{- 1} = C^{- 2}$

<a id="secao-7"></a>

### Similaridade Cosseno

As distâncias estudadas até aqui são consideradas medidas de dissimilaridade (Qualidade ou estado do que é diferente, desigual ou heterogêneo) entre vetores. De modo análogo, podemos definir a vizinhança de um ponto em termos de medidas de similaridade. Uma importante medida de similaridade entre dois vetores quaisquer $x$ e $z$ é dada pelo coseno do ângulo $\gamma$ entre eles: $$\cos(\gamma) = \frac{x^{T}z}{\| x\|_{2}\| z\|_{2}}$$ A similaridade coseno é particularmente útil quando estamos interessados na orientação, e não na magnitude, dos vetores. Ela tem sido bastante utilizada em aplicações que envolvem dados textuais (Manning & Schütze, 1999). Note também que $\cos(\gamma)$ pode ser escrito como uma função do tipo $k(x,z) = {\Phi(x)}^{T}\Phi(z)$, i.e., como uma generalização do produto interno entre $x$ e $z$. Medidas de similaridade que podem ser descritas dessa forma são chamadas funções de kernel.

<a id="secao-8"></a>

### Aprendendo Métricas

Além de usar distâncias clássicas, como as $L^{p}$ e a de Mahalanobis, é possível aprender métrica (ou pseudo-métrica) de distância de modo supervisionado, com base na taxa de classificacão. Existe uma área de pesquisa em ML conhecida como aprendizado de métrica (metric learning) que se dedica a essa finalidade. Nesse nicho, um dos métodos mais comuns é o chamado large margin nearest neighbor [(Weinberger et al., 2006)](https://jmlr.csail.mit.edu/papers/volume10/weinberger09a/weinberger09a.pdf).

<a id="regressao"></a>
<a id="secao-4"></a>

## Regressão

O k-NN pode também ser empregado em problemas de regressão. Para isso, precisamos de uma forma de combinar as saídas em $\mathcal{V}_{k( \cdot )}$. Uma das estratégias mais comuns consiste em computar a média ponderada pelo inverso da distância: $$h(x) ≔ \frac{1}{Z}\sum_{(x',y') \in \mathcal{V}_{k}(x)}y\frac{'}{d(x,x')}\text{\quad\quad}Z ≔ \sum_{(x',y') \in \mathcal{V}_{k}(x)}\frac{1}{d(x,x')}$$

permitindo que pontos mais próximos a $x$ exerçam maior influência no cômputo da predição $h(x)$. Ideia semelhante pode também ser aplicada a classificação.

Observe que o algoritmo k-NN não necessita de treinamento, ou equivalentemente, o treinamento consiste em simplesmente armazenar o conjunto de dados $\mathcal{D}$. Por conta disso, k-NN é dito ser uma abordagem de lazy learning (Atkeson et al., 1997)

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Próximo: [Qual distância escolher?](#qual-distancia-escolher)
