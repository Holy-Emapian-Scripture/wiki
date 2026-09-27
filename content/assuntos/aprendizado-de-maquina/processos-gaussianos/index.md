---
layout: "default"
title: "Processos Gaussianos"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 9
---

[Aprendizado de Máquina](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-9"></a>

# Processos Gaussianos


<a id="revisitando-a-priori-gaussiana"></a>
<a id="secao-10"></a>

## Revisitando a priori Gaussiana

Como discutimos anteriormente, prioris gaussianas são extremamente populares em modelos Bayesianos para regressão. Uma escolha comum, por exemplo, é colocar uma priori isotrópica $N(0,cI)$ sobre o vetor de pesos $\theta$. Nesse caso, a priori sobre $\theta$ também induz implicitamente uma priori sobre $f(X') = X'\theta$ para qualquer $X' \in {\mathbb{R}}^{N' \times (D + 1)}$ e $N' \in {\mathbb{N}}^{+}$. Mais especificamente, como $f(X')$ é uma transformação linear de variáveis Gaussianas, essa priori é Gaussiana com vetor de médias $\mu(X')$ e matriz de covariância $\Sigma(X',X')$ dados por: $$\begin{aligned} \mu(X') & = {\mathbb{E}}_{\theta}\lbrack X'\theta\rbrack = X'{\mathbb{E}}_{\theta}\lbrack\theta\rbrack = 0 \\ \Sigma(X',X') & = {\mathbb{E}}_{\theta}\left\lbrack (X'\theta - 0)(X'\theta - 0)^{T} \right\rbrack = cX'X'^{T} \end{aligned}$$

Com essas observações em mente, podemos abstrair $\theta$ totalmente do nosso processo de aprendizado usando a seguinte priori sobre os valores de $f$: $$f(X') \sim N\left( 0,\Sigma(X',X') \right)\ \forall X' \in {\mathbb{R}}^{N' \times (D + 1)},\ N' \in {\mathbb{N}}^{+}$$<a id="priori-gp"></a> que é uma instância específica de um processo estocástico conhecido como **processo Gaussiano** (Gaussian process, GP). De forma geral, $\left( f(x) \right)_{x \in \mathcal{X}}$ define um processo Gaussiano se qualquer vetor $\left\lbrack f\left( x_{1} \right),\ldots,f\left( x_{N} \right) \right\rbrack^{T}$ com $x_{1},\ldots,x_{N} \in \mathcal{X}$ segue uma distribuição normal multivariada.

**Definição: Processo Gaussiano**

Seja $\mathcal{X}$ um espaço de entradas. Dizemos que $\left( f(x) \right)_{x \in \mathcal{X}}$ é um processo Gaussiano se, para qualquer conjunto finito de pontos $x_{1},\ldots,x_{N} \in \mathcal{X}$, o vetor $\mathbf{f} = \left\lbrack f\left( x_{1} \right),\ldots,f\left( x_{N} \right) \right\rbrack^{T}$ segue uma distribuição normal multivariada.

É importante ressaltar que a matriz de covariância $\Sigma(X',X')$ é proporcional à matriz Gramiana $K$ (de produtos internos) dos vetores linha de $X'$, i.e., $K_{ij} = x'_{i} \cdot x'_{j}$, onde $x'_{i}$ e $x'_{j}$ denotam os vetores nas linhas $i$ e $j$ de $X'$, respectivamente. Além disso, incorporar uma função de expansão de base $\Phi$ no modelo da Equação [\[priori-gp\]](#priori-gp) apenas implica em redefinir as entradas de $K$ como $K_{ij} = k\left( x'_{i},x'_{j} \right) = \Phi(x'_{i}) \cdot \Phi(x'_{j})$. Em outras palavras, nosso GP sobre $f$ pode ser completamente caracterizado por uma função de produto interno generalizada $k$ — também conhecida como **função de kernel**. Por simplicidade notacional, denotaremos que $f$ segue uma priori de GP como $f \sim \text{ GP}(0,k)$. Nesse capítulo, assumiremos que a média de $f$ é zero a priori; no entanto, seria possível utilizar uma função de média arbitrária $\mu( \cdot )$ com poucas alterações nos nossos desenvolvimentos.

Do ponto de vista de interpretação, funções de kernel nos permitem diretamente expressar como regularidades no espaço de entrada devem ser refletidas no espaço de saída. Além disso, existem casos em que $\Phi$ é computacionalmente intratável, mas seu kernel correspondente tem forma simples. Por exemplo, o kernel exponencial quadrático (ou Gaussiano), dado por $k(x,x') = \exp\left\{ - \| x - x'\frac{\|_{2}^{2}}{2\gamma^{2}} \right\}$ é gerado a partir de uma expansão de base “infinita” — veja a Seção 4.2 do livro texto de [Rasmussen e Williams (2006)](https://gaussianprocess.org/gpml/chapters/RW.pdf) para mais detalhes.

<a id="secao-11"></a>

### Funções de kernel comuns

Na literatura de GPs, existe uma variedade de funções de kernel criadas para modelar fenômenos distintos. No entanto, alguns kernels são extremamente populares, como:

1.  **Exponencial quadrático** (ou Gaussiano):

$$k(x,x') = e^{- \| x - x'\frac{\|_{2}^{2}}{2\gamma^{2}}}$$ onde $\gamma^{2}$ é um hiperparâmetro que controla a suavidade da função de kernel;

2.  **Racional quadrático**:

$$k(x,x') = \sigma^{2}\left( 1 + \frac{\| x - x'\|_{2}^{2}}{2\alpha\gamma^{2}} \right)^{- \alpha}$$ que corresponde a uma soma ponderada de kernels exponenciais quadráticos com diferentes larguras de banda;

3.  **Periódico**:

$$k(x,x') = e^{- 2\gamma^{- 2}\sin^{2}\left( \pi\| x - x'\frac{\|_{2}}{p} \right)}$$ que tem natureza periódica, com período $p$.

<a id="secao-12"></a>

### Construindo funções de kernel

A família das funções de kernel é fechada por um número de operações. Isto é, é possível manipular um kernel $k$ de várias maneiras diferentes e ainda assim obter um kernel válido. Isso é extremamente útil em cenários em que precisamos, e.g., combinar propriedades de diferentes funções de kernel para refletir um fenômeno. Por exemplo, as seguintes operações resultam em kernels válidos:

1.  Multiplicação por constante $c > 0$: $k'(x,x') = ck(x,x')$;

2.  Produto: $k'(x,x') = k_{1}(x,x')k_{2}(x,x')$;

3.  Soma: $k'(x,x') = k_{1}(x,x') + k_{2}(x,x')$;

4.  Exponenciação: $k'(x,x') = e^{k_{1}(x,x')}$;

5.  Multiplicação por função escalar avaliada em $x$ e $x'$: $k'(x,x') = f(x)f(x')k(x,x')$.

<a id="gps-para-regressao"></a>
<a id="secao-13"></a>

## GPs para regressão

Em problemas de regressão, é comum que a variável de resposta $y_{n}$ para a entrada $x_{n}$ seja observada com algum ruído. Seguindo o capítulo de regressão linear, suponha que $y = g(x) = f(x) + \varepsilon$ com $\varepsilon \sim N\left( 0,\sigma^{2} \right)$. Note que isso é equivalente a dizer que $y\vert x \sim N\left( f(x),\sigma^{2} \right)$; portanto, podemos descrever um modelo qualquer de regressão com priori GP como: $$\begin{aligned} y\vert f,x & \sim N\left( f(x),\sigma^{2} \right) \\ f & \sim \text{ GP}(0,k) \end{aligned}$$<a id="modelo-gp-regressao"></a>

Como é de costume, estamos interessados em usar o modelo acima e o conjunto de treino $D = \left\{ \left( x_{n},y_{n} \right) \right\}_{n = 1}^{N}$ para fazer predições para, e.g., a variável de resposta $y^{\ast}$ relativa a um novo vetor de atributos $x^{\ast}$. Em outras palavras, queremos avaliar $p\left( y^{\ast}\vert x^{\ast},x_{1},y_{1},\ldots,x_{N},y_{N} \right)$. No entanto, existe um detalhe no modelo acima que facilitará nossa vida: a nossa combinação de priori e verossimilhança induz um processo Gaussiano sobre $g$. Mais especificamente, para qualquer $X' \in {\mathbb{R}}^{M \times D}$, $g(X')$ pode ser descrito como uma soma de duas variáveis aleatórias Gaussianas: $f(X')$ e um vetor $M$-dimensional $\varepsilon$ com distribuição $N\left( 0,\sigma^{2}I \right)$. Portanto, temos que $g(X') \sim N\left( 0,k(X',X') + \sigma^{2}I \right)$.

Tomando $X' = \begin{pmatrix} x_{1}^{T} \\ \vdots \\ x_{N}^{T} \\ \left( x^{\ast} \right)^{T} \end{pmatrix}$, segue que: $$\begin{pmatrix} y^{\ast} \\ y_{1} \\ \vdots \\ y_{N} \end{pmatrix} \sim N\left( \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix},\begin{pmatrix} k\left( x^{\ast},x^{\ast} \right) + \sigma^{2} & k\left( x^{\ast},x_{1} \right) & \ldots & k\left( x^{\ast},x_{N} \right) \\ k\left( x_{1},x^{\ast} \right) & k\left( x_{1},x_{1} \right) + \sigma^{2} & \ldots & k\left( x_{1},x_{N} \right) \\ \vdots & \vdots & \vdots & \vdots \\ k\left( x_{N},x^{\ast} \right) & k\left( x_{N},x_{1} \right) & \ldots & k\left( x_{N},x_{N} \right) + \sigma^{2} \end{pmatrix} \right)$$ onde o lado direito está implicitamente condicionado nas entradas $x_{1},\ldots,x_{N}$ e $x^{\ast}$. Portanto, podemos obter a distribuição $p\left( y^{\ast}\vert x^{\ast},x_{1},y_{1},\ldots,x_{N},y_{N} \right)$ simplesmente condicionando a Gaussiana acima nos valores observados $y_{1},\ldots,y_{N}$, i.e., $p\left( y^{\ast}\vert x^{\ast},x_{1},y_{1},\ldots,x_{N},y_{N} \right) = N\left( \mu^{\ast},S^{\ast} \right)$ com parâmetros $\mu^{\ast}$, $S^{\ast}$ dados por: $$\begin{aligned} \mu^{\ast} & = k\left( x^{\ast},X \right)\left( k(X,X) + \sigma^{2}I \right)^{- 1}y \\ S^{\ast} & = k\left( x^{\ast},x^{\ast} \right) + \sigma^{2} - k\left( x^{\ast},X \right)\left( k(X,X) + \sigma^{2}I \right)^{- 1}{k\left( x^{\ast},X \right)}^{T} \end{aligned}$$<a id="predicao-gp"></a> onde $X$ é a matriz com dados de treinamento e $y$ é o vetor de suas respectivas respostas.

**Interpretação de $\mu^{\ast}$**: Uma observação interessante é que $\mu^{\ast}$ é, essencialmente, uma combinação linear das respostas em $y$. Finalmente, vale ressaltar que $\sigma^{2}$ é comumente tratado como um hiperparâmetro, que podemos escolher com auxílio de um conjunto de validação.

<a id="secao-14"></a>

### Escolhendo os parâmetros do kernel

Já sabemos como construir um GP simples para regressão. No entanto, não discutimos como escolher os parâmetros da nossa função de kernel (e.g., a largura de banda $\gamma$ do kernel Gaussiano). Como fazer isso? Na literatura de GPs, a saída comum é maximizar a esperança da verossimilhança sob a nossa priori, i.e., $p\left( y_{1},\ldots,y_{N}~\vert ~x_{1},\ldots,x_{N} \right) = {\mathbb{E}}_{f \sim \text{ GP}(0,k)}\left\lbrack N\left( y~\vert ~f(X),\sigma^{2}I \right) \right\rbrack$. Mais concretamente, denotando de maneira genérica os parâmetros da função de kernel por $\omega$, os parâmetros ótimos podem ser calculados como: $$\begin{aligned} \hat{\omega} & = \text{ argmax}_{\omega \in \Omega}\log p\left( y_{1},\ldots,y_{N}~\vert ~x_{1},\ldots,x_{N} \right) \\ & = \text{ argmax}_{\omega \in \Omega}\log N\left( y~\vert ~0,k(X,X) + \sigma^{2}I \right) \\ & = \text{ argmax}_{\omega \in \Omega}\left\{ - \frac{1}{2}\log\det(k(X,X) + \sigma^{2}I) - \frac{1}{2}y^{T}\left( k(X,X) + \sigma^{2}I \right)^{- 1}y \right\} \end{aligned}$$<a id="evidencia-gp"></a>

O procedimento descrito acima é comumente conhecido como **type II maximum likelihood**, **maximização da verossimilhança marginal** e **maximização da evidência** (note que estamos maximizando o denominador da regra de Bayes). Vale ressaltar que, ao contrário de MLE para regressão linear e logística, o problema acima costuma não ser convexo em $\omega$. Por isso, é ideal conduzir otimização multi-start — e.g., rodando SGD usando diferentes pontos iniciais e escolhendo o melhor ótimo local obtido.

**Estimando $\sigma^{2}$**: Note também que o procedimento que descrevemos assume que o ruído observacional $\sigma^{2}$ é uma constante. Nesse caso, poderíamos estimar os parâmetros do kernel para cada valor de $\sigma^{2}$ usando o conjunto de treino e escolher o $\sigma^{2}$ que resulta na maior evidência. Outra opção é otimizar $\sigma^{2}$ juntamente com $\omega$, i.e.: $${\hat{\sigma}}^{2},\hat{\omega} = \text{ argmax}_{\omega \in \Omega,\sigma \in {\mathbb{R}}}\left\{ - \frac{1}{2}\log\det(k(X,X) + \sigma^{2}I) - \frac{1}{2}y^{T}\left( k(X,X) + \sigma^{2}I \right)^{- 1}y \right\}$$ No entanto, otimizar $\sigma^{2}$ e $\omega$ juntos pode tornar nosso processo de aprendizado instável. Para aliviar esse problema, a comunidade de GPs em ML costuma usar algumas heurísticas de inicialização. A heurística mais comum consiste em fixar (a priori) a razão $r^{2}$ entre a variância da verossimilhança e da priori. Assumindo que nosso kernel é da forma $k = c^{2}k'$, o primeiro passo é inicializar $c$ com a variância das saídas de treinamento $y_{1},\ldots,y_{N}$. Subsequentemente, inicializamos o ruído observacional $\sigma^{2}$ com $\frac{c^{2}}{r^{2}}$. Nesse contexto, repetimos o processo de otimização para diferentes valores de $r^{2}$ e escolhemos o resultado que leva ao melhor ótimo local.

<a id="gps-para-classificacao"></a>
<a id="secao-15"></a>

## GPs para classificação

Para classificações, vamos reformular como as saídas se comportam. Dessa vez, assumimos que $$y_{i}~\vert ~f_{i},x_{i} \sim \text{ Bernoulli}\left( \sigma(f_{i}\left( x_{i} \right)) \right)$$ para simplificar notação, vou definir $\sigma_{i} = \sigma(f_{i}\left( x_{i} \right))$. Nós vamos aproximar $p\left( y\vert f,X \right)$ usando a aproximação de Laplace ou métodos de amostragem e depois achar a preditiva posteriori $p\left( y^{\ast}\vert X,y,x^{\ast} \right)$. Primeiro vamos achar a forma da verossimilhança $$p\left( y_{n}\vert f_{n},x_{n} \right) = \sigma_{n}^{y_{n}}\left( 1 - \sigma_{n} \right)^{1 - y_{n}} \Rightarrow p\left( y\vert f,X \right) = \prod_{n = 1}^{N}\sigma_{n}^{y_{n}}\left( 1 - \sigma_{n} \right)^{1 - y_{n}}$$ agora, vamos escrever a posteriori de $f$ dado $X$ e $y$ usando Bayes: $$p\left( f\vert X,y \right) \propto p\left( y\vert f,X \right)p\left( f\vert X \right)$$ escrevendo em forma de $\log$ para facilitar as contas $$\begin{aligned} \ln p\left( f\vert X,y \right) & = \ln p\left( y\vert f,X \right) + \ln p\left( f\vert X \right) + C \\ & = \sum_{n = 1}^{N}\left\{ y_{n}\ln\sigma_{n} + \left( 1 - y_{n} \right)\ln\left( 1 - \sigma_{n} \right) \right\} - \frac{1}{2}{f(x)}^{T}K^{- 1}f(x) + C \end{aligned}$$

Agora podemos derivar para conseguir achar a moda $m$ $$\begin{array}{r} \frac{\partial}{\partial f_{n}}\ln p\left( f\vert X,y \right) = y_{n}\left( 1 - \sigma_{n} \right) - \left( 1 - y_{n} \right)\sigma_{n} - \left( K^{- 1}f(x) \right)_{n} = 0 \\ \Rightarrow \nabla\ln p\left( f\vert X,y \right) = y - \sigma(f(x)) - K^{- 1}f(x) = 0 \end{array}$$

essa equação não tem solução analítica, então utilizamos de métodos numéricos para achar a moda $m$ que satisfaz $$y - \sigma(m) - K^{- 1}m = 0$$

Agora, para continuar com a aproximação de Laplace, precisamos achar a matriz Hessiana da posteriori de $f$ dado $X$ e $y$. A matriz Hessiana é dada por $$H = \nabla^{2}\ln p\left( f\vert X,y \right) = - W - K^{- 1}$$ onde $W$ é uma matriz diagonal com entradas $W_{nn} = \sigma_{n}\left( 1 - \sigma_{n} \right)$. A aproximação de Laplace nos diz que a posteriori de $f$ dado $X$ e $y$ pode ser aproximada por uma Gaussiana centrada na moda $m$ com covariância $\Sigma = - H^{- 1} = \left( K^{- 1} + W \right)^{- 1}$. Sabendo que $p\left( f\vert X,y \right) \approx \mathcal{N}(m,\Sigma)$, temos que: $$p\left( y^{\ast}\vert X,y,x^{\ast} \right) = \int\underset{\mathcal{N}(f^{\ast}\left( x^{\ast} \right),\sigma^{2})}{\underbrace{p\left( y^{\ast}\vert f^{\ast} \right)}}\underset{\mathcal{N}(m',\Sigma')}{\underbrace{p\left( f^{\ast}\vert X,y,x^{\ast} \right)}}df^{\ast}$$ $m'$ e $\Sigma'$ representam as mesmas contas que fizemos antes, porém adicionando o ponto $x^{\ast}$ no conjunto de dados. A integral acima não tem solução analítica, então podemos utilizar métodos de amostragem para aproximar a integral.

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Diferenciação Automática](../diferenciacao-automatica/index.md)
- Próximo: [Graph Neural Networks](../graph-neural-networks/index.md)
