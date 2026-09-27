---
layout: "default"
title: "Regressão Logística"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 11
---

[Aprendizado de Máquina](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-17"></a>

# Regressão Logística

------------------------------------------------------------------------

Uma das maneiras mais naturais de criar um modelo de regressão consiste em escolher um modelo observacional para a variável de resposta $y$ cujos parâmetros dependam diretamente do seu respectivo vetor de entradas $x$. Por exemplo, na capítulo anterior, vimos que minimizar o MSE é equivalente a admitir uma verossimilhança da forma $y\vert x \sim N\left( \theta^{T}x,\sigma^{2} \right)$, na qual o parâmetro de média é uma função linear de $x$. Note também que esse escolha implica que $y$ pode tomar valores arbitrários em $\mathbb{R}$, já que esse é o suporte da distribuição normal (i.e., região com densidade maior que zero).

Se $y$ é uma variável binária (0/1), a escolha mais comum é utilizar uma distribuição Bernoulli com parâmetro $r = g(x)$. Em outras palavras, falamos que $y$ assume valor 1 com probabilidade $r$ e $0$ com probabilidade $1 - r$. Adotando esse modelo observacional para $y\vert x$, resta-nos definir a função $g$ para completar nosso modelo de regressão. Para tal, iremos calcular uma função linear de $x$, como anteriormente, mas aplicaremos uma função que mapeie o valor resultante (comumente conhecido como logit) para $\lbrack 0,1\rbrack$, gerando valores válidos para a probabilidade $r$. Mais especificamente, usamos a função sigmoide $\sigma(t) = \left( 1 + e^{- t} \right)^{- 1}$ para definir a probabilidade de $y\vert x$ como $$p\left( y\vert x \right) = \text{ Bern}\left( y\vert \sigma(\theta^{T}x) \right) = {\sigma(\theta^{T}x)}^{y}\left( 1 - \sigma(\theta^{T}x) \right)^{1 - y}$$

**Propriedades da função sigmoide** $$\rightarrow t < t' \Rightarrow \sigma(t) < \sigma(t')$$ $$\lim\limits_{t \rightarrow \infty}\sigma(t) = 1\text{\quad\quad}\lim\limits_{t \rightarrow - \infty}\sigma(t) = 0$$ $$\sigma( - t) = 1 - \sigma(t)$$ $$\frac{d}{dt}\sigma(t) = \sigma(t)\left( 1 - \sigma(t) \right) = \sigma(t)\sigma( - t)$$ $$\sigma(t) = \frac{1}{2} + \frac{1}{2}\tanh(\frac{t}{2})$$ $$\int\sigma(t)dt = \log(\sigma( - t)) + C$$

Dado um conjunto de treinamento $D$ com $N$ exemplos de treinamento $\left( x_{n},y_{n} \right)$, podemos então definir a função de verossimilhança $\mathcal{L}$ como $$\mathcal{L}(\theta) = \prod_{i = 1}^{N}p\left( y_{i}\vert x_{i} \right) = \prod_{i = 1}^{N}{\sigma(\theta^{T}x_{i})}^{y_{i}}\left( 1 - \sigma(\theta^{T}x_{i}) \right)^{1 - y_{i}}$$ e agora podemos encontrar o estimador de máxima verossimilhança $\hat{\theta}$ para $\theta$: $$\begin{aligned} \hat{\theta} & = \text{ argmax}_{\theta \in {\mathbb{R}}^{D + 1}}\mathcal{L}(\theta) = \text{ argmin}_{\theta \in {\mathbb{R}}^{D + 1}} - \log\mathcal{L}(\theta) \\ & = \text{ argmin}_{\theta \in {\mathbb{R}}^{D + 1}} - \sum_{i = 1}^{N}\left\lbrack y_{i}\log\sigma(\theta^{T}x_{i}) + \left( 1 - y_{i} \right)\log\left( 1 - \sigma(\theta^{T}x_{i}) \right) \right\rbrack \\ & = \text{ argmin}_{\theta \in {\mathbb{R}}^{D + 1}} - \left\{ \underset{⏝}{\sum_{i = 1}^{N}}\log\sigma(\theta^{T}x_{i}) - \underset{⏝}{\sum_{i = 1}^{N}}\log\sigma( - \theta^{T}x_{i}) \right\} \end{aligned}$$

Similar ao MSE, que minimizamos no capítulo passado, a função objetivo $- \log(\mathcal{L})$ é uma convexa. No entanto, não possuímos uma solução analítica para $\hat{\theta}$ e, portanto, precisamos utilizar algum método de otimização númerica, como o SGD que já conhecemos. Para fins de implementação, podemos definir a variável $y'_{i} = 2y_{i} - 1$. Com isso, conseguimos escrever o gradiente $\nabla\theta\mathcal{l}_{i}(\theta)$ da log verossimilhança para o $i$-ésimo exemplo de treinamento $\mathcal{l}_{i}$ como: $$\begin{aligned} \nabla_{\theta}\mathcal{l}_{i}(\theta) & = \nabla_{\theta}\log\sigma(y'_{i}\theta^{T}x_{i}) \\ & = \frac{\partial\log\sigma(y'_{i}\theta^{T}x_{i})}{\partial\sigma(y'_{i}\theta^{T}x_{i})} \cdot \frac{\partial\sigma(y'_{i}\theta^{T}x_{i})}{\partial\left( y'_{i}\theta^{T}x_{i} \right)} \cdot \frac{\partial y'_{i}\theta^{T}x_{i}}{\partial\theta} \\ & = \sigma( - y'_{i}\theta^{T}x_{i})y'_{i}x_{i} \end{aligned}$$

Aplicando o algoritmo gradiente descendente à função custo da regressão logística, obtemos o seguinte algoritmo:

**Regressão Logística**

1.  $\theta_{0} \leftarrow 0$

2.  $y' \leftarrow 2y - \mathbf{1}$

3.  **for** $t = 0,1,2,\ldots$ **do**

    1.  $g \leftarrow \sum_{i = 1}^{N}\sigma( - y'_{i}\theta_{t}^{T}x_{i})y'_{i}x_{i}$

    2.  $\theta^{(t + 1)} \leftarrow \theta^{(t)} - \eta g$

    3.  Verifica condição de parada

4.  **end for**

5.  **return** $\theta$

*Figura 7. Regressão Logística*

**Interpretação geométrica**: Uma vez que obtivemos $\hat{\theta}$, podemos estimar a probabilide de uma nova amostra $x^{\ast}$ pertencer à classe 1 como $\sigma({\hat{\theta}}^{T}x^{\ast})$ e a de pertencer à classe 0 como $1 - \sigma({\hat{\theta}}^{T}x^{\ast})$. Com isso em mente, se precisamos prever a classe de $x^{\ast}$, é razoável escolher aquela que achamos mais provável. Lembre que $\sigma(0) = 0.5$. Portanto, o plano ${\hat{\theta}}^{T}x = 0$ caracteriza os pontos $x \in \mathcal{X}$ que cremos ter probabilidade idêntica de pertencer a ambas as classes. Isso implica que todos os vetores de entrada cujo ângulo $\gamma$ com o vetor normal $\hat{\theta}$ é menor que noventa graus são classificados como positivos (classe 1) — lembre que $\theta^{T}x = \|\hat{\theta}\|_{2}\| x\|_{2}\cos(\gamma)$. Os demais pontos são classificados como negativos (classe 0).

**Convexidade do problema de aprendizado**: Como a soma de funções convexas é também convexa, basta verificar que as $\mathcal{l}_{1},\ldots,\mathcal{l}_{N}$ são convexas para provarmos que $- \log\mathcal{L}$ também o é. Para esse fim, podemos usar o fato de que a função composta $h = g \circ f$ é convexa se $f$ é côncava e $g$ é convexa não-crescente. Note que $y'_{i}\theta^{T}x_{i}$ é tanto côncava como convexa, como é o caso de funções lineares. Em contrapartida, $- \log\sigma(t)$ é convexa não-crescente já que ela descresce com $t$ e sua derivada $- \sigma( - t)$ é estritamente crescente

**Entropia Cruzada Binária**: Na comunidade de ML, é comum se referir ao logaritmo negativo da verossimilhança Bernoulli como entropia cruzada binária (binary cross entropy, BCE). De forma geral, a entropia cruzada entre duas funções de massa/densidade $p$ e $q$ sobre a mesma variável aleatória $z$ e com suportes idênticos é definida como: $$H(p,q) ≔ - {\mathbb{E}}_{z \sim p}\log q(z)$$ e dá-se o nome BCE para o caso especial em que p e q são distribuições Bernoulli.

Em teoria da informação, é comum interpretar $\log\frac{1}{q(z)}$ como uma medida de surpresa, i.e., do quanto observar um valor específico $z$ contrasta com seu conhecimento prévio, representado por $q$. Nesse contexto, $H(p,q)$ é o valor dessa medida se os valores de $z$ são amostrados de $p$ (ao invés de q). Vale ressaltar que, para um $p$ fixo, $q = p$ minimiza $H(p,q)$. Nesse caso, a quantia $H(p) ≔ H(p,p)$ é chamada de entropia. Por sua vez, a entropia também pode ser vista como uma medida de concentração de $p$, atingindo seu valor máximo quando $p$ é uma distribuição uniforme.

Para concluir que a BCE generaliza $- \log\text{Ber}\left( y\vert r \right)$, basta definir $p(z) = \text{ Ber}\left( z\vert y \right)$ e tomar $q(z) = \text{ Ber}\left( z\vert r \right)$. Com essas escolhas, obtemos: $$\begin{aligned} H(p,q) & = - y\log q(1) - (1 - y)\log q(0) \\ & = - \left( y\log r + (1 - y)\log(1 - r) \right) \end{aligned}$$ o que implica que: $$e^{- H(p,q)} = r^{y}(1 - r)^{1 - y}(1 - y) = \text{ Ber}\left( y\vert r \right)$$

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Regressão Logística Bayesiana](regressao-logistica-bayesiana/index.md)
2. [Problemas multiclasse, classificador *softmax*](problemas-multiclasse-classificador-softmax/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Modelo com expansão de base](../regressao-linear/modelo-com-expansao-de-base/index.md)
- Próximo: [Regressão Logística Bayesiana](regressao-logistica-bayesiana/index.md)
