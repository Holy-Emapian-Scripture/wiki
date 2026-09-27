---
layout: "default"
title: "Variational Autoencoders"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 16
---

[Aprendizado de Máquina](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-16"></a>

# Variational Autoencoders


<a id="autoencoders-deterministicos"></a>
<a id="secao-18"></a>

## Autoencoders Determinísticos

Esses autoencoders são versões clássicas e mais simples. Eles consistem em uma rede neural que aprende a mapear entradas para saídas, passando por uma camada intermediária de menor dimensão. O objetivo é minimizar a diferença entre a entrada e a saída reconstruída, geralmente utilizando funções de perda como o erro quadrático médio (MSE).

<a id="secao-19"></a>

### Autoencoders Profundos

A principal ideia desse autoencoder é uma rede neural que recebe como input um vetor $x \in {\mathbb{R}}^{D}$, passa ele por diversas camadas ocultas de menor dimensão e tenta, a partir de um novo vetor $z \in {\mathbb{R}}^{M}$ ($M < D$) reconstruir o vetor original $x$. A função de perca utilizada nesses autoencoders é dada por: $$E(w) = \frac{1}{2}\sum_{n = 1}^{N}\| x_{n} - y\left( x_{n},w \right)\|^{2}$$ onde $y\left( x_{n},w \right)$ é a saída da rede neural com pesos $w$ para a entrada $x_{n}$. A função de perda é minimizada utilizando o algoritmo de retropropagação (backpropagation) e métodos de otimização como o gradiente descendente.

<a id="deep-autoencoder"></a>

![Arquitetura de um autoencoder profundo. A entrada $x$ é comprimida em uma representação latente $z$ e, em seguida, reconstruída como $y(x,w)$.](../assets/deep-autoencoder.png)

*Figura 5. Arquitetura de um autoencoder profundo. A entrada $x$ é comprimida em uma representação latente $z$ e, em seguida, reconstruída como $y(x,w)$.*

Como podemos ver na [\[deep-autoencoder\]](#deep-autoencoder), a arquitetura do autoencoder profundo pode ser interpretada como dois mapeamentos distintos $F_{1}$ e $F_{2}$, onde $F_{1}$ é o encoder que mapeia a entrada $x$ para a representação latente $z$, e $F_{2}$ é o decoder que mapeia a representação latente $z$ de volta para a reconstrução da entrada original $y(x,w)$. A função de perda é então minimizada ajustando os pesos da rede neural para melhorar a qualidade da reconstrução.

<a id="secao-20"></a>

### Autoencoders Esparsos

Uma forma tradicional de limitar a capacidade de um autoencoder consiste em utilizar uma representação latente de dimensão menor que a dimensão dos dados de entrada. Entretanto, essa não é a única maneira de impor uma representação compacta. Nos **autoencoders esparsos**, em vez de restringir o número de neurônios da camada latente, utiliza-se uma regularização que incentiva apenas uma pequena fração desses neurônios a permanecer ativa para cada exemplo.

A ideia é permitir que a camada latente possua muitas unidades, mas forçar a maioria delas a assumir valores nulos ou próximos de zero. Dessa forma, cada amostra é representada por apenas alguns neurônios ativos, produzindo uma representação de baixa dimensionalidade efetiva.

Uma forma simples de obter esse comportamento é adicionar uma penalização $L_{1}$ sobre as ativações da camada latente. A função de custo passa a ser dada por

$$
E(w) = \widetilde{E}(w) + \lambda\sum_{m = 1}^{M}\left\vert  z_{m} \right\vert ,
$$

onde $\widetilde{E}(w)$ representa o erro de reconstrução, $z_{m}$ corresponde à ativação do neurônio latente $m$, e $\lambda$ controla a intensidade da regularização.

Como a norma $L_{1}$ favorece soluções esparsas, o treinamento passa a buscar simultaneamente uma boa reconstrução dos dados e uma representação latente na qual poucos neurônios estejam ativos. Em consequência, o modelo é capaz de aprender características relevantes dos dados mesmo quando a camada latente possui um número elevado de unidades.

<a id="secao-21"></a>

### Denoising Autoencoders

Vimos que para o autoencoder aprender representações úteis, é necessário impor restrições à sua capacidade de reconstrução. Uma abordagem alternativa é treinar o autoencoder para reconstruir a entrada original a partir de uma versão corrompida dela. Essa técnica é conhecida como **denoising autoencoder**. Assim, intuitivamente, eu forço o meu autoencoder a aprender representações robustas dos dados, que capturam as características essenciais e ignoram o ruído. $$E(w) = \frac{1}{2}\sum_{n = 1}^{N}\| x_{n} - y\left( {\widetilde{x}}_{n},w \right)\|^{2}$$

Um método de impor ruído nas entradas é selecionar uma fração $\tau \in (0,1)$ das amostras e colocar parte de suas entradas como $0$. Por exemplo, se $\tau = 0.2$, então 20% das entradas de cada amostra selecionada serão corrompidas, ou seja, substituídas por zero. Outro método é adicionar ruído gaussiano às entradas, ou seja, para cada entrada $x_{n}$, adicionamos um ruído $\varepsilon$ proveniente de uma distribuição normal com média zero e desvio padrão $\sigma$, resultando em uma entrada corrompida ${\widetilde{x}}_{n} = x_{n} + \varepsilon$.

<a id="autoencoders-variacionais"></a>
<a id="secao-22"></a>

## Autoencoders Variacionais

Agora chegamos na brincadeira de gente grande. Nós já vimos que, a função de verossimilhança de um modelo com variáveis latentes dada por: $$p\left( x\vert w \right) = \int p\left( x\vert z,w \right)p(z)dz$$ onde $p\left( x\vert z,w \right)$ é definida por uma rede neural profunda, é intratável pois a integral em $z$ não tem forma fechada. Os autoencoders variacionais (VAEs) resolvem esse problema utilizando uma aproximação variacional para a posteriori $p\left( z\vert x,w \right)$, que é definida por outra rede neural profunda. A ideia é otimizar os parâmetros do modelo para maximizar a verossimilhança dos dados, enquanto simultaneamente aproximamos a posteriori das variáveis latentes. Existem 3 conceitos-chave dentro dos VAEs:

1.  Utilizar o **ELBO** (Evidence Lower Bound) para aproximar a verossimilhança dos dados

2.  **Inferência Amortizada** onde um segundo modelo, a **rede encoder**, é usada para aproximar a distribuição posteriori das variáveis latentes no passo **E** em vez de calcular para cada ponto

3.  Fazer o treino da rede encoder tratável utilizando do **truque da reparametrização**

Considere um modelo generativo com distribuição $p\left( x\vert z,w \right)$ governado pela saída de uma rede $g(w,z)$ (Por exemplo, $g(w,z)$ retorna a média de uma distribuição gaussiana). Considere também $p(z) \sim N(0,I)$ sobre $z \in {\mathbb{R}}^{M}$

Lembrando do documento da A1, vimos que: $$\ln p\left( x\vert w \right) = \mathcal{L}(w) + \text{ KL}\left( q(z)\| p\left( z\vert x,w \right) \right)$$ onde $\mathcal{L}(w)$ é o ELBO e $q(z)$ é a distribuição aproximada das variáveis latentes e $\mathcal{L}(w)$ é dado por: $$\mathcal{L}(w) = \int q(z)\ln\frac{p\left( x\vert z,w \right)p(z)}{q(z)}dz$$ e $\text{KL}\left( p\| q \right)$ é definido como: $$\text{ KL}\left( p\| q \right) = \int p(z)\ln\frac{p(z)}{q(z)}dz$$

Pelo que tinhamos visto no primeiro documento, sabemos que $\ln p\left( x\vert w \right) \geq \mathcal{L}$ (Por isso o nome EVIDENCE **LOWER BOUND**). Mesmo que $\ln p\left( x\vert w \right)$ seja intratável, podemos aproximar ela utilizando de $\mathcal{L}$ aproximado por **monte carlo**.

Considere o conjunto de dados $x_{1},\ldots,x_{N}$. Temos então que $$\ln p\left( D\vert w \right) = \sum_{n = 1}^{N}\mathcal{L}_{n} + \sum_{n = 1}^{N}\text{ KL}\left( q_{n}\left( z_{n}\vert x_{n} \right)\| p\left( z_{n}\vert x_{n},w \right) \right)$$<a id="elbo-dataset-likelihood"></a>

onde $$\mathcal{L}_{n} = \int q_{n}\left( z_{n}\vert x_{n} \right)\ln\left\{ \frac{p\left( x_{n}\vert z_{n},w \right) \cdot p\left( z_{n} \right)}{q_{n}\left( z_{n}\vert x_{n} \right)} \right\} dz_{n}$$

Perceba que agora, cada $x_{n}$ tem sua variável latente, o que indica que cada variável $z_{n}$ tem sua distribuição $q_{n}\left( z_{n}\vert x_{n} \right)$. Como a equação [\[elbo-dataset-likelihood\]](#elbo-dataset-likelihood) é mantida independente da escolha de $q_{n}\left( z_{n}\vert x_{n} \right)$, podemos escolher $q_{n}\left( z_{n}\vert x_{n} \right)$ para cada ponto $x_{n}$ de forma à maximizar $\mathcal{L}_{n}$ ou, equivalentemente, minimizar $\text{KL}\left( q_{n}\left( z_{n}\vert x_{n} \right)\| p\left( z_{n}\vert x_{n},w \right) \right)$. EM GMMs, conseguimos achar $q_{n}\left( z_{n}\vert x_{n} \right)$ de forma exata ($q_{n}\left( z_{n}\vert x_{n} \right) = p\left( z_{n}\vert x_{n},w \right)$) $$p\left( z_{n}\vert x_{n},w \right) = \frac{p\left( x_{n}\vert z_{n},w \right)p\left( z_{n} \right)}{p\left( x_{n}\vert w \right)}$$

o numerador é trivial de calcular, mas o denominador é intratável. Então precisamos de um método diferente para aproximar $q_{n}\left( z_{n}\vert x_{n} \right)$.

<a id="secao-23"></a>

### Inferência Amortizada

Nessa abordagem, nós treinamos **uma única** rede neural para aproximar todas as posterioris $p\left( z_{n}\vert x_{n},w \right)$, chamada de **Encoder Network**. Essa abordagem se chama **inferência amortizada** que requer um encoder que gera uma única distribuição $q\left( z\vert x,\varphi \right)$ condicionada em $x$, onde $\varphi$ são os parâmetros da rede neural. Nessa abordagem, a função-objetivo (dada pelo ELBO) depende tanto de $\varphi$ quanto de $w$, assim ela faz a otimização conjunta dos parâmetros com abordagens baseadas em gradiente.

![Arquitetura de um autoencoder variacional](../assets/autoencoder.png)

*Figura 6. Arquitetura de um autoencoder variacional*

Um encoder variacional é então composto por duas redes, um **encoder** que mapeia do espaço dos dados para um espaço latente e um **decoder** que mapeia do espaço latente de volta para o espaço dos dados e ambas as redes são treinadas simultaneamente para maximizar o ELBO.

Certo, mas agora temos que decidir ao menos qual espaço latente nós gostariamos de mapear nossos dados pra termos uma base, correto? Sim! Uma escolha muito comum de se usar para o encoder é uma Gaussiana $N\left( \mu_{j},\sigma_{j}^{2}I \right)$ onde $\mu_{j}$ e $\sigma_{j}$ são outputs de uma rede neural $$q\left( z\vert x,\varphi \right) = \prod_{j = 1}^{M}N\left( z_{j}~\vert ~\mu_{j}(x,\varphi),\sigma_{j}^{2}(x,\varphi) \right)$$

<a id="secao-24"></a>

### Truque da Reparametrização

Infelizmente, temos que o lower bound ainda é intratável $$\mathcal{L}_{n}(w,\varphi) = \int q\left( z_{n}\vert x_{n},\varphi \right)\ln\left\{ \frac{p\left( x_{n}\vert z_{n},w \right)p\left( z_{n} \right)}{q\left( z_{n}\vert x_{n},\varphi \right)} \right\} dz_{n}$$ porque envolve integrar sobre as variáveis latentes $\left\{ z \right\}$ e ele depende de forma complexa dos parâmetros da rede neural. Porém, podemos decompor essa integral em duas partes: $$\mathcal{L}_{n}(w,\varphi) = {\mathbb{E}}_{z_{n} \sim q}\left\lbrack \ln p\left( x_{n}\vert z_{n},w \right) \right\rbrack - \text{ KL}\left( q\left( z_{n}\vert x_{n},\varphi \right)\| p\left( z_{n} \right) \right)$$<a id="elbo-decomposition"></a>

Se nós escolhemos $q\left( z_{n}\vert x_{n},\varphi \right)$ como uma Gaussiana, e $p\left( z_{n} \right)$ também, então a divergência KL entre elas tem uma forma fechada, que é dada por: $$\text{ KL}\left( q\left( z_{n}\vert x_{n},\varphi \right)\| p\left( z_{n} \right) \right) = \frac{1}{2}\sum_{j = 1}^{M}\left\{ 1 + \ln\sigma_{j}^{2}\left( x_{n},\varphi \right) - \sigma_{j}^{2}\left( x_{n},\varphi \right) - \mu_{j}^{2}\left( x_{n},\varphi \right) \right\}$$ Já com relação à primeira parte, podemos tentar aproximar ela utilizando **monte carlo** $${\mathbb{E}}_{z_{n} \sim q}\left\lbrack \ln p\left( x_{n}\vert z_{n},w \right) \right\rbrack = \int q\left( z_{n}\vert x_{n},\varphi \right)\ln p\left( x_{n}\vert z_{n},w \right)dz_{n} \approx \frac{1}{L}\sum_{l = 1}^{L}\ln p\left( x_{n}\vert z_{n}^{(l)},w \right)$$ onde $\left\{ z_{n}^{(l)} \right\}$ são amostras de $q\left( z_{n}\vert x_{n},\varphi \right)$. Toda essa equação [\[elbo-decomposition\]](#elbo-decomposition) é diferenciável com relação a $w$, no entanto, ela tem uma relação complexa em $\varphi$ para ser facilmente diferenciável.

![Esquema de como o erro se espalha no autoencoder. O fato de $z$ depender de $\varphi$ de forma complexa impede que o gradiente seja propagado através do processo de amostragem.](../assets/autoencoder-structure-without-reparametrization.png)

*Figura 7. Esquema de como o erro se espalha no autoencoder. O fato de $z$ depender de $\varphi$ de forma complexa impede que o gradiente seja propagado através do processo de amostragem.*

Para consertar isso, utilizamos do **truque da reparametrização**. Nessa abordagem, nós não vamos amostrar $z_{n}^{(l)}$ diretamente. Em vez disso, vamos amostrar $\varepsilon \sim N(0,1)$. Após amostrar $\varepsilon$, nós podemos reparametrizar $z_{n}^{(l)}$ como: $$z_{nj}^{(l)} = \mu(x_{n},\varphi) + \sigma(x_{n},\varphi) \cdot \varepsilon_{nj}^{(l)}$$ pois sabemos que $z_{n}^{(l)} \sim N\left( \mu(x_{n},\varphi),\sigma^{2}\left( x_{n},\varphi \right) \right)$. Dessa forma, a amostragem de $z_{n}^{(l)}$ é feita de forma diferenciável com relação a $\varphi$, permitindo que o gradiente seja propagado através do processo de amostragem. Dessa forma, a função de erro do autoencoder variacional, depois de todas nossas premissas, é dada por: $$\mathcal{L} = \sum_{n}\left\{ \frac{1}{2}\sum_{j = 1}^{M}\left\{ 1 + \ln\sigma_{nj}^{2} - \sigma_{nj}^{2} - \mu_{nj}^{2} \right\} + \frac{1}{L}\sum_{l = 1}^{L}\ln p\left( x_{n}\vert z_{n}^{(l)},w \right) \right\}$$ onde, para simplificar a notação, nós escrevemos $\mu_{nj} = \mu_{j}\left( x_{n},\varphi \right)$ e $\sigma_{nj} = \sigma_{j}\left( x_{n},\varphi \right)$ e $z_{n}^{(l)} = \mu(x_{n},\varphi) + \sigma(x_{n},\varphi) \cdot \varepsilon^{(l)}$.

![Esquema de como o erro se espalha no autoencoder após o truque da reparametrização. Como a amostragem não depende mais de $\varphi$, o gradiente pode ser propagado através do processo de amostragem.](../assets/autoencoder-structure-with-reparametrization.png)

*Figura 8. Esquema de como o erro se espalha no autoencoder após o truque da reparametrização. Como a amostragem não depende mais de $\varphi$, o gradiente pode ser propagado através do processo de amostragem.*

**Treinamento do VAE**

1.  **function** *train_VAE*($D$, $w$, $\varphi$) {

    1.  **for** $x_{n} \in D$ {

        1.  $\mathcal{L} \leftarrow 0$

        2.  **for** $j \in \left\{ 1,2,\ldots,M \right\}$ {

            1.  $\varepsilon_{nj} \sim N(0,1)$

            2.  $z_{nj} \leftarrow \mu_{nj} + \sigma_{nj} \cdot \varepsilon_{nj}$

            3.  $\mathcal{L} \leftarrow \mathcal{L} + \frac{1}{2}\left( 1 + \ln\sigma_{nj}^{2} - \sigma_{nj}^{2} - \mu_{nj}^{2} \right)$

        3.  }

        4.  $\mathcal{L} \leftarrow \mathcal{L} + \ln p\left( x_{n}\vert z_{n},w \right)$

        5.  $w \leftarrow w - \eta \ast \nabla_{w}\mathcal{L}$

        6.  $\varphi \leftarrow \varphi - \eta \ast \nabla_{\varphi}\mathcal{L}$

2.  }

------------------------------------------------------------------------

<a id="introducao"></a>
<a id="secao-17"></a>

## Introdução

Autoencoders são modelos de aprendizado não supervisionado projetados para aprender representações compactas dos dados. Seu objetivo é comprimir uma entrada em uma representação de menor dimensão e, em seguida, reconstruir a entrada original a partir dessa representação.

A arquitetura de um autoencoder é composta por duas partes principais:

- **Encoder:** transforma a entrada original em uma representação latente, também chamada de **código** ou **embedding**.

- **Decoder:** utiliza essa representação latente para reconstruir uma aproximação da entrada original.

De forma simplificada, dado um dado de entrada (x), o encoder produz uma representação (z),

$$
z = f(x),
$$

e o decoder gera uma reconstrução ($\hat{x}$),

$$
\hat{x} = g(z).
$$

Durante o treinamento, os parâmetros do modelo são ajustados para minimizar a diferença entre (x) e ($\hat{x}$), fazendo com que a representação latente retenha as características mais relevantes dos dados.

Ao aprender a reconstruir as entradas a partir de uma representação comprimida, os autoencoders podem descobrir estruturas e padrões presentes nos dados, sendo amplamente utilizados para redução de dimensionalidade, compressão, remoção de ruído, detecção de anomalias e aprendizado de representações.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A3](../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Singularidades e Identificabilidade](../gaussian-and-bernoulli-mixture-models/index.md#singularidades-e-identificabilidade)
- Próximo: [Autoencoders Determinísticos](#autoencoders-deterministicos)
