---
layout: "default"
title: "GPs para regressão — Processos Gaussianos"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 11
---

[Aprendizado de Máquina](../../index.md) · [Processos Gaussianos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-13"></a>

# GPs para regressão

Em problemas de regressão, é comum que a variável de resposta $y_{n}$ para a entrada $x_{n}$ seja observada com algum ruído. Seguindo o capítulo de regressão linear, suponha que $y = g(x) = f(x) + \varepsilon$ com $\varepsilon \sim N\left( 0,\sigma^{2} \right)$. Note que isso é equivalente a dizer que $y\vert x \sim N\left( f(x),\sigma^{2} \right)$; portanto, podemos descrever um modelo qualquer de regressão com priori GP como: $$\begin{aligned} y\vert f,x & \sim N\left( f(x),\sigma^{2} \right) \\ f & \sim \text{ GP}(0,k) \end{aligned}$$<a id="modelo-gp-regressao"></a>

Como é de costume, estamos interessados em usar o modelo acima e o conjunto de treino $D = \left\{ \left( x_{n},y_{n} \right) \right\}_{n = 1}^{N}$ para fazer predições para, e.g., a variável de resposta $y^{\ast}$ relativa a um novo vetor de atributos $x^{\ast}$. Em outras palavras, queremos avaliar $p\left( y^{\ast}\vert x^{\ast},x_{1},y_{1},\ldots,x_{N},y_{N} \right)$. No entanto, existe um detalhe no modelo acima que facilitará nossa vida: a nossa combinação de priori e verossimilhança induz um processo Gaussiano sobre $g$. Mais especificamente, para qualquer $X' \in {\mathbb{R}}^{M \times D}$, $g(X')$ pode ser descrito como uma soma de duas variáveis aleatórias Gaussianas: $f(X')$ e um vetor $M$-dimensional $\varepsilon$ com distribuição $N\left( 0,\sigma^{2}I \right)$. Portanto, temos que $g(X') \sim N\left( 0,k(X',X') + \sigma^{2}I \right)$.

Tomando $X' = \begin{pmatrix} x_{1}^{T} \\ \vdots \\ x_{N}^{T} \\ \left( x^{\ast} \right)^{T} \end{pmatrix}$, segue que: $$\begin{pmatrix} y^{\ast} \\ y_{1} \\ \vdots \\ y_{N} \end{pmatrix} \sim N\left( \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix},\begin{pmatrix} k\left( x^{\ast},x^{\ast} \right) + \sigma^{2} & k\left( x^{\ast},x_{1} \right) & \ldots & k\left( x^{\ast},x_{N} \right) \\ k\left( x_{1},x^{\ast} \right) & k\left( x_{1},x_{1} \right) + \sigma^{2} & \ldots & k\left( x_{1},x_{N} \right) \\ \vdots & \vdots & \vdots & \vdots \\ k\left( x_{N},x^{\ast} \right) & k\left( x_{N},x_{1} \right) & \ldots & k\left( x_{N},x_{N} \right) + \sigma^{2} \end{pmatrix} \right)$$ onde o lado direito está implicitamente condicionado nas entradas $x_{1},\ldots,x_{N}$ e $x^{\ast}$. Portanto, podemos obter a distribuição $p\left( y^{\ast}\vert x^{\ast},x_{1},y_{1},\ldots,x_{N},y_{N} \right)$ simplesmente condicionando a Gaussiana acima nos valores observados $y_{1},\ldots,y_{N}$, i.e., $p\left( y^{\ast}\vert x^{\ast},x_{1},y_{1},\ldots,x_{N},y_{N} \right) = N\left( \mu^{\ast},S^{\ast} \right)$ com parâmetros $\mu^{\ast}$, $S^{\ast}$ dados por: $$\begin{aligned} \mu^{\ast} & = k\left( x^{\ast},X \right)\left( k(X,X) + \sigma^{2}I \right)^{- 1}y \\ S^{\ast} & = k\left( x^{\ast},x^{\ast} \right) + \sigma^{2} - k\left( x^{\ast},X \right)\left( k(X,X) + \sigma^{2}I \right)^{- 1}{k\left( x^{\ast},X \right)}^{T} \end{aligned}$$<a id="predicao-gp"></a> onde $X$ é a matriz com dados de treinamento e $y$ é o vetor de suas respectivas respostas.

**Interpretação de $\mu^{\ast}$**: Uma observação interessante é que $\mu^{\ast}$ é, essencialmente, uma combinação linear das respostas em $y$. Finalmente, vale ressaltar que $\sigma^{2}$ é comumente tratado como um hiperparâmetro, que podemos escolher com auxílio de um conjunto de validação.

<a id="secao-14"></a>

## Escolhendo os parâmetros do kernel

Já sabemos como construir um GP simples para regressão. No entanto, não discutimos como escolher os parâmetros da nossa função de kernel (e.g., a largura de banda $\gamma$ do kernel Gaussiano). Como fazer isso? Na literatura de GPs, a saída comum é maximizar a esperança da verossimilhança sob a nossa priori, i.e., $p\left( y_{1},\ldots,y_{N}~\vert ~x_{1},\ldots,x_{N} \right) = {\mathbb{E}}_{f \sim \text{ GP}(0,k)}\left\lbrack N\left( y~\vert ~f(X),\sigma^{2}I \right) \right\rbrack$. Mais concretamente, denotando de maneira genérica os parâmetros da função de kernel por $\omega$, os parâmetros ótimos podem ser calculados como: $$\begin{aligned} \hat{\omega} & = \text{ argmax}_{\omega \in \Omega}\log p\left( y_{1},\ldots,y_{N}~\vert ~x_{1},\ldots,x_{N} \right) \\ & = \text{ argmax}_{\omega \in \Omega}\log N\left( y~\vert ~0,k(X,X) + \sigma^{2}I \right) \\ & = \text{ argmax}_{\omega \in \Omega}\left\{ - \frac{1}{2}\log\det(k(X,X) + \sigma^{2}I) - \frac{1}{2}y^{T}\left( k(X,X) + \sigma^{2}I \right)^{- 1}y \right\} \end{aligned}$$<a id="evidencia-gp"></a>

O procedimento descrito acima é comumente conhecido como **type II maximum likelihood**, **maximização da verossimilhança marginal** e **maximização da evidência** (note que estamos maximizando o denominador da regra de Bayes). Vale ressaltar que, ao contrário de MLE para regressão linear e logística, o problema acima costuma não ser convexo em $\omega$. Por isso, é ideal conduzir otimização multi-start — e.g., rodando SGD usando diferentes pontos iniciais e escolhendo o melhor ótimo local obtido.

**Estimando $\sigma^{2}$**: Note também que o procedimento que descrevemos assume que o ruído observacional $\sigma^{2}$ é uma constante. Nesse caso, poderíamos estimar os parâmetros do kernel para cada valor de $\sigma^{2}$ usando o conjunto de treino e escolher o $\sigma^{2}$ que resulta na maior evidência. Outra opção é otimizar $\sigma^{2}$ juntamente com $\omega$, i.e.: $${\hat{\sigma}}^{2},\hat{\omega} = \text{ argmax}_{\omega \in \Omega,\sigma \in {\mathbb{R}}}\left\{ - \frac{1}{2}\log\det(k(X,X) + \sigma^{2}I) - \frac{1}{2}y^{T}\left( k(X,X) + \sigma^{2}I \right)^{- 1}y \right\}$$ No entanto, otimizar $\sigma^{2}$ e $\omega$ juntos pode tornar nosso processo de aprendizado instável. Para aliviar esse problema, a comunidade de GPs em ML costuma usar algumas heurísticas de inicialização. A heurística mais comum consiste em fixar (a priori) a razão $r^{2}$ entre a variância da verossimilhança e da priori. Assumindo que nosso kernel é da forma $k = c^{2}k'$, o primeiro passo é inicializar $c$ com a variância das saídas de treinamento $y_{1},\ldots,y_{N}$. Subsequentemente, inicializamos o ruído observacional $\sigma^{2}$ com $\frac{c^{2}}{r^{2}}$. Nesse contexto, repetimos o processo de otimização para diferentes valores de $r^{2}$ e escolhemos o resultado que leva ao melhor ótimo local.

  

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Revisitando a priori Gaussiana](../revisitando-a-priori-gaussiana/index.md)
- Próximo: [GPs para classificação](../gps-para-classificacao/index.md)
