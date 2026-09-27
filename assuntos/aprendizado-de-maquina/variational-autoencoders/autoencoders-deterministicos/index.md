---
layout: "default"
title: "Autoencoders Determinísticos — Variational Autoencoders"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 18
---

[Aprendizado de Máquina](../../index.md) · [Variational Autoencoders](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-18"></a>

# Autoencoders Determinísticos

Esses autoencoders são versões clássicas e mais simples. Eles consistem em uma rede neural que aprende a mapear entradas para saídas, passando por uma camada intermediária de menor dimensão. O objetivo é minimizar a diferença entre a entrada e a saída reconstruída, geralmente utilizando funções de perda como o erro quadrático médio (MSE).

<a id="secao-19"></a>

## Autoencoders Profundos

A principal ideia desse autoencoder é uma rede neural que recebe como input um vetor $x \in {\mathbb{R}}^{D}$, passa ele por diversas camadas ocultas de menor dimensão e tenta, a partir de um novo vetor $z \in {\mathbb{R}}^{M}$ ($M < D$) reconstruir o vetor original $x$. A função de perca utilizada nesses autoencoders é dada por: $$E(w) = \frac{1}{2}\sum_{n = 1}^{N}\| x_{n} - y\left( x_{n},w \right)\|^{2}$$ onde $y\left( x_{n},w \right)$ é a saída da rede neural com pesos $w$ para a entrada $x_{n}$. A função de perda é minimizada utilizando o algoritmo de retropropagação (backpropagation) e métodos de otimização como o gradiente descendente.

<a id="deep-autoencoder"></a>

![Arquitetura de um autoencoder profundo. A entrada $x$ é comprimida em uma representação latente $z$ e, em seguida, reconstruída como $y(x,w)$.](../../assets/deep-autoencoder.png)

*Figura 5. Arquitetura de um autoencoder profundo. A entrada $x$ é comprimida em uma representação latente $z$ e, em seguida, reconstruída como $y(x,w)$.*

Como podemos ver na [\[deep-autoencoder\]](#deep-autoencoder), a arquitetura do autoencoder profundo pode ser interpretada como dois mapeamentos distintos $F_{1}$ e $F_{2}$, onde $F_{1}$ é o encoder que mapeia a entrada $x$ para a representação latente $z$, e $F_{2}$ é o decoder que mapeia a representação latente $z$ de volta para a reconstrução da entrada original $y(x,w)$. A função de perda é então minimizada ajustando os pesos da rede neural para melhorar a qualidade da reconstrução.

<a id="secao-20"></a>

## Autoencoders Esparsos

Uma forma tradicional de limitar a capacidade de um autoencoder consiste em utilizar uma representação latente de dimensão menor que a dimensão dos dados de entrada. Entretanto, essa não é a única maneira de impor uma representação compacta. Nos **autoencoders esparsos**, em vez de restringir o número de neurônios da camada latente, utiliza-se uma regularização que incentiva apenas uma pequena fração desses neurônios a permanecer ativa para cada exemplo.

A ideia é permitir que a camada latente possua muitas unidades, mas forçar a maioria delas a assumir valores nulos ou próximos de zero. Dessa forma, cada amostra é representada por apenas alguns neurônios ativos, produzindo uma representação de baixa dimensionalidade efetiva.

Uma forma simples de obter esse comportamento é adicionar uma penalização $L_{1}$ sobre as ativações da camada latente. A função de custo passa a ser dada por

$$E(w) = \widetilde{E}(w) + \lambda\sum_{m = 1}^{M}\left\vert  z_{m} \right\vert ,$$

onde $\widetilde{E}(w)$ representa o erro de reconstrução, $z_{m}$ corresponde à ativação do neurônio latente $m$, e $\lambda$ controla a intensidade da regularização.

Como a norma $L_{1}$ favorece soluções esparsas, o treinamento passa a buscar simultaneamente uma boa reconstrução dos dados e uma representação latente na qual poucos neurônios estejam ativos. Em consequência, o modelo é capaz de aprender características relevantes dos dados mesmo quando a camada latente possui um número elevado de unidades.

<a id="secao-21"></a>

## Denoising Autoencoders

Vimos que para o autoencoder aprender representações úteis, é necessário impor restrições à sua capacidade de reconstrução. Uma abordagem alternativa é treinar o autoencoder para reconstruir a entrada original a partir de uma versão corrompida dela. Essa técnica é conhecida como **denoising autoencoder**. Assim, intuitivamente, eu forço o meu autoencoder a aprender representações robustas dos dados, que capturam as características essenciais e ignoram o ruído. $$E(w) = \frac{1}{2}\sum_{n = 1}^{N}\| x_{n} - y\left( {\widetilde{x}}_{n},w \right)\|^{2}$$

Um método de impor ruído nas entradas é selecionar uma fração $\tau \in (0,1)$ das amostras e colocar parte de suas entradas como $0$. Por exemplo, se $\tau = 0.2$, então 20% das entradas de cada amostra selecionada serão corrompidas, ou seja, substituídas por zero. Outro método é adicionar ruído gaussiano às entradas, ou seja, para cada entrada $x_{n}$, adicionamos um ruído $\varepsilon$ proveniente de uma distribuição normal com média zero e desvio padrão $\sigma$, resultando em uma entrada corrompida ${\widetilde{x}}_{n} = x_{n} + \varepsilon$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Introdução](../introducao/index.md)
- Próximo: [Autoencoders Variacionais](../autoencoders-variacionais/index.md)
