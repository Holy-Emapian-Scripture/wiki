---
layout: "default"
title: "Qual distância escolher? — Método dos Vizinhos mais próximos (k-NN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 5
---

[Aprendizado de Máquina](../../index.md) · [Método dos Vizinhos mais próximos (k-NN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Qual distância escolher?

Até então, descrevemos o k-NN sem especificar exatamente o formato da função de distância $d$. No entanto, a escolha de uma distância apropriada pode ser crítica para o sucesso do método. Por exemplo, se os dados de entrada estão dispostos na superfície do globo terrestre, gostariamos de usar uma distância que considere a curvatura da terra (e.g., a distância esférica).

No entanto, raramente temos esse tipo de conhecimento sobre $\mathcal{X}$ e as escolhas mais comuns para $d$ incluem casos particulares da distância de Minkowski: $$d_{p}(x,z) = \| x - z\|_{p} = \left( \sum_{i = 1}^{D}\vert x_{i} - z_{i}\vert ^{p} \right)^{\frac{1}{p}}$$

que para valores de $p = 1$ chama-se distância quarteirão ou Manhattan; $p = 2$ resulta na distância euclidiana; e $p \rightarrow \infty$ retorna o máximo da diferença entre as componentes dos vetores. A notação $\| \cdot \|_{p}$ é também chamada de norma $L^{p}$ de um vetor.

Uma possível deficiência de normas $L^{p}$ é que elas não incorporam nenhuma informação sobre a distribuição ${\mathbb{P}}_{x}:\mathcal{X} \rightarrow {\mathbb{R}}^{+} \cup \left\{ 0 \right\}$ (Que é a distribuição que os vetores $x$ foram extraídos) — além do fato do suporte ser subconjunto dos reais. Por exemplo, se uma componente $x_{i}$ tiver escala muito maior às demais $x_{j \neq i}$, ela pode dominar o cálculo da distância, ofuscando diferenças nas demais componentes $x_{j \neq i}$. Além disso, $L^{p}$ são agnósticas a correlações entre componentes de $x \sim {\mathbb{P}}_{x}$ (Quando falamos em relação, dizemos da relação entre os componentes de um $x$. Por exemplo, digamos que $x_{i} = \left( x_{1i},x_{2i},\ldots,x_{Di} \right)$ então a feature $2$ e $3$ são altura e peso respectivamente, sabemos que quando altura cresce, peso tende a crescer, mas a distância de Minkowski não captura essa relação). Uma alternativa para cobrir esses problema é utilizar a distância de Mahalanobis: $$d_{M}(x,z) = \sqrt{(x - z)^{T}\Sigma^{- 1}(x - z)}$$ em que $\Sigma$ é a matriz de covariância dos dados de treinamento. Uma escolha típica para $\Sigma$ é a matriz de covariância amostral, não viezada: $$\Sigma = \frac{1}{N - 1}\sum_{i = 1}^{N}\left( x_{i} - \overset{-}{x} \right)\left( x_{i} - \overset{-}{x} \right)^{T}$$ onde $\overset{-}{x} ≔ \frac{1}{N}\sum_{i = 1}^{N}x_{i}$ é o vetor de médias amostrais. Observe que quando $\Sigma$ é igual à matriz identidade, temos a distância euclidiana. Mas, afinal, qual distância utilizar? De modo geral, a menos que tenhamos profundo conhecimento sobre a geometria de $\mathcal{X}$ , é impossível dar uma resposta direta. O melhor que podemos fazer é testar opções diferentes.

<a id="secao-6"></a>

## Normalização para média zero e variância um

Subtrair a média $\overset{-}{x} ≔ \frac{1}{N}\sum_{i = 1}^{N}x_{i}$ de cada vetor $x_{1},\ldots,x_{N}$ e, subsequentemente, multiplicá-los pela inversa da matriz diagonal $C$ com entradas: $$C_{jj} = \sqrt{\frac{1}{N - 1}\sum_{i = 1}^{N}\left( x_{ij} - {\overset{-}{x}}_{j} \right)^{2}}$$ é um procedimento comum em ML, sendo geralmente chamado de normalização ou padronização (standardization). Aplicar k-NN com $d(x,z) = \| x - z\|_{2}$ em dados transformados dessa maneira equivale a aplicar k-NN nos dados originais usando a distância de Mahalanobis com $\Sigma^{- 1} = C^{- 2}$

<a id="secao-7"></a>

## Similaridade Cosseno

As distâncias estudadas até aqui são consideradas medidas de dissimilaridade (Qualidade ou estado do que é diferente, desigual ou heterogêneo) entre vetores. De modo análogo, podemos definir a vizinhança de um ponto em termos de medidas de similaridade. Uma importante medida de similaridade entre dois vetores quaisquer $x$ e $z$ é dada pelo coseno do ângulo $\gamma$ entre eles: $$\cos(\gamma) = \frac{x^{T}z}{\| x\|_{2}\| z\|_{2}}$$ A similaridade coseno é particularmente útil quando estamos interessados na orientação, e não na magnitude, dos vetores. Ela tem sido bastante utilizada em aplicações que envolvem dados textuais (Manning & Schütze, 1999). Note também que $\cos(\gamma)$ pode ser escrito como uma função do tipo $k(x,z) = {\Phi(x)}^{T}\Phi(z)$, i.e., como uma generalização do produto interno entre $x$ e $z$. Medidas de similaridade que podem ser descritas dessa forma são chamadas funções de kernel.

<a id="secao-8"></a>

## Aprendendo Métricas

Além de usar distâncias clássicas, como as $L^{p}$ e a de Mahalanobis, é possível aprender métrica (ou pseudo-métrica) de distância de modo supervisionado, com base na taxa de classificacão. Existe uma área de pesquisa em ML conhecida como aprendizado de métrica (metric learning) que se dedica a essa finalidade. Nesse nicho, um dos métodos mais comuns é o chamado large margin nearest neighbor [(Weinberger et al., 2006)](https://jmlr.csail.mit.edu/papers/volume10/weinberger09a/weinberger09a.pdf).

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Regressão](../regressao/index.md)
- Próximo: [Maldição da Dimensionalidade](../maldicao-da-dimensionalidade/index.md)
