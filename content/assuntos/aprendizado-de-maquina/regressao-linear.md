---
layout: "default"
title: "Regressão Linear"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 7
---

[Aprendizado de Máquina](index.md)

<!-- wiki:original:inicio -->

<a id="secao-11"></a>

# Regressão Linear


<a id="o-problema"></a>
<a id="secao-12"></a>

## O Problema

Suponha que você recebe um conjunto de dados $D$ com $N$ pares ordenados $\left( x_{n},y_{n} \right)$, no qual $x_{n} \in {\mathbb{R}}^{D}$ são as entradas (ou variáveis independentes), e $y_{n} \in {\mathbb{R}}$ são amostras de uma variável de saída (ou variável dependente). Suponha ainda que cada variável de saída pode ser descrita aproximadamente como uma combinação afim do seu respectivo vetor de entradas, isto é: $$y_{n} = \sum_{j = 1}^{D}\theta_{j}x_{nj} + \theta_{0} + \varepsilon_{n} = \theta^{T}x_{n} + \varepsilon_{n}$$ onde $\varepsilon_{n} \in {\mathbb{R}}$ é uma variável que reflete o grau de incerteza na observação de $y_{n}$

**Nota**: A partir daqui, insermos um $1$ no vetor $x$ para representar o *bias*, então vamos redefinir $x_{n} ≔ \left( 1,x_{n1},\ldots,x_{nD} \right)^{T}$ e $\theta ≔ \left( \theta_{0},\theta_{1},\ldots,\theta_{D} \right)^{T}$, de modo que a expressão acima possa ser escrita de forma mais compacta como $y_{n} = \theta^{T}x_{n} + \varepsilon_{n}$.

Uma das maneiras mais comuns de obter uma estimativa $\hat{\theta}$ para $\theta$ é obter o aquele que minimiza a média (ou a soma) dos erros quadráticos entre as predições ${\hat{y}}_{n} ≔ {\hat{\theta}}^{T}x_{n}$ e as saídas observadas $y_{n}$: $${\hat{\theta}}_{\text{LS }} ≔ \text{ argmin}_{\theta \in {\mathbb{R}}^{D + 1}}\left\{ \mathcal{l}(\theta) ≔ \frac{1}{N}\sum_{n = 1}^{N}\left( y_{n} - \theta^{T}x_{n} \right)^{2} \right\}$$ Esse método de otimização é chamado de **mínimos quadrados ordinários** Podemos escrever a função de custo $\mathcal{l}$ de forma matricial como: $$\begin{aligned} \mathcal{l}(\theta) & = \frac{1}{N}\| y - X\theta\|_{2}^{2} \\ & = \frac{1}{N}(y - X\theta)^{T}(y - X\theta) \\ & = \frac{1}{N}\left( y^{T}y - 2\theta^{T}X^{T}y + \theta^{T}X^{T}X\theta \right) \end{aligned}$$

Note que, quando $X^{T}X$ é positiva definida, a função de custo $\mathcal{l}$ é estritamente convexa, o que garante a existência de um único mínimo global. Podemos encontrar uma solução analítica para ${\hat{\theta}}_{\text{LS}}$ derivando $\mathcal{l}$ e igualando a zero: $$\begin{aligned} \nabla_{\theta}\mathcal{l}(\theta) & = \frac{1}{N}\left( - 2X^{T}y + 2X^{T}X\theta \right) = 0 \\ & \Rightarrow {\hat{\theta}}_{\text{LS }} = \left( X^{T}X \right)^{- 1}X^{T}y \end{aligned}$$<a id="hat-theta-ls"></a>

**E se $X^{T}X$ não for positiva definida?**: Considere o caso em que $N > D$. Para que a inversa exista, precisamos que todas as colunas de $X$, nossas variáveis preditoras, sejam linarmente independentes. Caso contrário, não podemos calcular a inversa na Equação [\[hat-theta-ls\]](#hat-theta-ls). No entanto, essas variáveis não agregam nenhuma informação ao nosso modelo de regressão, e podemos pré-processar os dados de maneira a remover atributos redundantes. Uma outra alternativa, é substituir a inversa de $X^{T}X$ pela inversa de $X^{T}X + \alpha I$, para algum pequeno escalar $\alpha$ positivo. É possível provar que $X^{T}X + \alpha I$ sempre possui inversa (verifique!)

**Casos $N = D$ e $N < D$**: No caso em que o número de dados é igual ao número atributos ($N = D$), existe uma solução ótima única, com $\mathcal{l} = 0$, se a matriz $X$ possuir inversa. Nesses casos, a função linear resultante, com ${\hat{\theta}}_{\text{LS }} = X^{- 1}y$, intersecta todos as observações $D$.

Quando $N < D$, no caso mais geral, o problema admite infinitas soluções com $\mathcal{l} = 0$. Quando as linhas de $X$ são linearmente independentes — $\text{posto}(X) = N$ — uma opção comum é achar a solução que possui a menor norma L2, dada por ${\hat{\theta}}_{\text{MN }} = X^{T}\left( XX^{T} \right)^{- 1}y$

**Em bancos de dados massivos**: Quando $N$ é um grande número, armazenar a matriz $X$ nas camadas de memória mais velozes de um computador se torna impraticável e, portanto, calcular ${\hat{\theta}}_{\text{LS}}$ usando a Equação [\[hat-theta-ls\]](#hat-theta-ls) não é computacionalmente viável. Nesse caso, podemos utilizar SGD para minimizar $\mathcal{l}$. Para tal, note que pode-se escrever $\mathcal{l}(\theta) = \sum\mathcal{l}_{n}(\theta)$, no qual definimos $\mathcal{l}_{n}(\theta) ≔ \frac{1}{N}\left( y_{n} - \theta^{T}x_{n} \right)^{2}$

**Exemplo: Regressão Linear Simples**

No ano 2020, o mundo foi tomado por uma pandemia do vírus Sars-Cov-2, causando milhões de infeções e centenas de milhares de mortos. No dia 29 de abril, a infeção ainda não havia atingido seu estado crítico no Ceará.

Neste exemplo, utilizamos um modelo linear para descrever o logaritmo do número de novas infeções diárias no Ceará como uma função do número de dias que se passaram desde a data na qual o primeiro caso de infecção foi reportado. Uma das utilidades de um modelo como esse é produzir estimativas para o número de novos infectados nos próximos dias, o que pode auxiliar epidemiologistas e gestores públicos em seus processos de tomada de decisão.

![](assets/regression-ceara.png)

Vale a pena ressaltar que em geral a dinâmica de contágios em uma epidemia possui um ponto de inflexão no qual número de novos casos começa a diminuir. Portanto, um modelo linear como esse não descreve todo o processo epidemiológico e seu uso deve ser validado por um especialista.

**Exemplo: Antiruido**

O método de mínimos quadrados pode ser utilizado para remoção de ruído (denoising). Suponha que você recebe um sinal digital ruidoso $s_{r}(t)$ em que $t$ denota um instante de tempo discreto e $t = 1,\ldots,T$. Estamos interessados em encontrar a versão não ruidosa $s(t)$ de $s_{r}(t)$.

Um sinal ruidoso $s_{r}(t)$ pode ser decrito como um sinal suave $s(t)$ adicionado de um ruído de alta frequência $r(t)$:

![](assets/ruido.png)

Queremos encontrar um sinal $s$ que seja:

- Similar ao sinal ruidoso

- Suave (a diferença entre os valores do sinal em instantes sucessivos seja pequena)

Com essas propriedades em mente, podemos propor uma função custo a se minimizar da forma: $$\min\limits_{s \in {\mathbb{R}}^{T}}\underset{\text{ similar ao sinal ruidoso}}{\underbrace{\| s - s_{r}\|^{2}}} + \underset{\text{ suavidade}}{\underbrace{\mu\sum_{t = 1}^{T - 1}\left( s(t + 1) - s(t) \right)^{2}}}$$ onde $s$ é a representação vetorial do sinal $s(t)$. O termo $\mu$ controla o peso que queremos dar a propriedade da suavidade. Essa função custo pode ser colocada na forma $\min\limits_{s}\| y - Xs\|^{2}$ escolhendo: $$X = \begin{pmatrix} I_{T \times T} \\ \sqrt{\mu}D_{T - 1 \times T} \end{pmatrix},D = \begin{pmatrix} - 1 & 1 & 0 & \ldots & 0 \\ 0 & - 1 & 1 & \ldots & 0 \\ \vdots & 0 & - 1 & 1 & 0 \\ 0 & 0 & \ldots & - 1 & 1 \end{pmatrix},y = \begin{pmatrix} s_{r} \\ 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} \in {\mathbb{R}}^{2T - 1}$$

Nesse formato, o valor ótimo $s^{\ast}$ para o sinal $s$ é obtido com a solução de mínimos quadrados $s^{\ast} = \left( X^{T}X \right)^{- 1}X^{T}y$. As figuras abaixo mostram a solução ótima para valores de $\mu \in \left\{ 0,100,20000 \right\}$. Para $\mu = 0$, a solução ótima é o próprio sinal ruidoso. Com $\mu = 20000$, o sinal fica muito suave, tendendo a um sinal constante. Finalmente, para $\mu = 100$, temos um sinal filtrado com eliminação da componente de ruído.

![](assets/denoising.png)

<a id="perspectiva-probabilistica"></a>
<a id="secao-13"></a>

## Perspectiva Probabilística

Podemos obter o mesmo estimador de mínimos quadrados se assumirmos o seguinte modelo observacional para cada resposta dado sua respectiva entrada: $$y_{n}\vert x_{n} \sim N\left( \theta^{T}x_{n},\sigma^{2} \right)\forall n = 1,\ldots,N$$<a id="modelo-observacional"></a> podemos então procurar o estimador de [máxima verossimilhança](../inferencia-estatistica/estatistica-frequentista.md#secao-14) ${\hat{\theta}}_{\text{ML}}$ para $\theta$: $$\begin{aligned} \Rightarrow f_{n}\left( y\vert x,\theta \right) & = \prod_{n = 1}^{N}f\left( y_{n}\vert x_{n},\theta \right) = \left( \frac{1}{\left( \sqrt{2\pi\sigma^{2}} \right)^{N}} \right)\exp( - \sum_{n = 1}^{N}\frac{\left( y_{n} - \theta^{T}x_{n} \right)^{2}}{2\sigma^{2}}) \end{aligned}$$ $$\Rightarrow \log f_{n}\left( y\vert x,\theta \right) = - \frac{N}{2}\log(2\pi\sigma^{2}) - \frac{1}{2\sigma^{2}}\sum_{n = 1}^{N}\left( y_{n} - \theta^{T}x_{n} \right)^{2}$$ $$\Rightarrow {\hat{\theta}}_{\text{ML }} = \text{ argmax}_{\theta \in {\mathbb{R}}^{D + 1}}\log f_{n}\left( y\vert x,\theta \right) = \text{ argmin}_{\theta \in {\mathbb{R}}^{D + 1}}\underset{N \cdot \mathcal{l}(\theta)}{\underbrace{\sum_{n = 1}^{N}\left( y_{n} - \theta^{T}x_{n} \right)^{2}}}$$

ou seja, a estimativa que máximiza a verossimilhança do modelo descrito pela equação [\[modelo-observacional\]](#modelo-observacional) é equivalente à estimativa obtida minimizando a média dos erros quadrados. Mais importante, note que, quando fazemos regressão linear, estamos parametrizando um parâmetro (a média) do nosso modelo observacional como uma transformação linear do vetor de entrada.

<a id="modelo-com-expansao-de-base"></a>
<a id="secao-14"></a>

## Modelo com expansão de base

O método de mínimos quadrados aplicado a modelos lineares é atraente por sua simplicidade e pelo fato de admitir uma solução ótima analítica. No entanto, a consideração que a relação entre as variáveis de entrada e de saída é linear pode não ser válida em diversos problemas. Um das formas de combinar a vantagem de termos uma solução ótima analítica com um modelo mais geral e flexível do que o linear é utilizar uma transformação não-linear das variáveis de entrada.

Nessa abordagem, de forma geral, o primeiro passo consiste em transformar as variáveis de entrada $x$ através de uma função $\Phi:{\mathbb{R}}^{D} \rightarrow {\mathbb{R}}^{M}$ , em que normalmente $M$ é maior que $D$. Em seguida, aplicamos um transformação linear sobre as variáveis transformadas para obtermos as predições $\hat{y}$ para as variáveis de saída $y$. Ou seja, considere as variáveis transformadas $z ≔ \Phi(x)$, o modelo preditivo é dado por: $$\hat{y} = \theta^{T}z = \theta^{T}\Phi(x)$$ onde o vetor $\theta \in {\mathbb{R}}^{M}$ denota os parâmetros do modelo

Note que o modelo é não linear com relação às entradas originais $x$, mas é linear no espaço das variáveis $z$. Quando a transformação $\Phi$ é fixa, sem parâmetros a serem aprendidos, o modelo é dito ser linear nos parâmetros. Nesses casos, a solução de mínimos quadrados é obtida simplesmente substituindo a matriz original de regressores $X$ por uma matriz $Z = \left\lbrack z_{1},\ldots,z_{N} \right\rbrack^{T}$ de entradas transformadas na equação [\[hat-theta-ls\]](#hat-theta-ls): $${\hat{\theta}}_{\text{LS }} = \left( Z^{T}Z \right)^{- 1}Z^{T}y$$ A transformação $\Phi$ atua como um pré-processamento das entradas $x_{1},\ldots,x_{N}$ . A seguir, estudaremos algumas das escolhas mais comuns para $\Phi$

**Por que $M > D$?**: As variáveis de entrada $x$ representam atributos de um objeto sob o qual queremos realizar predições. Em geral quando aplicamos a transformação não-linear $\Phi$ queremos encontrar novos atributos $z$ que permitam ao modelo linear ser preciso. Dessa forma, é natural trabalharmos em espaços com dimensões maiores, aumentando a chance de encontrarmos atributos relevantes. Vale ressaltar que isso não constitui uma regra. Conforme veremos adiante, o aumento do valor M pode gerar problemas, especialmente quando temos poucas amostras proporcionalmente a $M$

<a id="secao-15"></a>

### Polinômios

Funções de expansão de base podem ser utilizadas para construir modelos polinômiais. Para entradas e saídas escalares, podemos descrever um modelo de regressão polinomial de grau dois como: $$\hat{y} = \theta_{3} + \theta_{2}x + \theta_{1}x^{2} = \theta^{T}\Phi(x) = \theta^{T}z$$ onde $z = \Phi(x)$ é dado por: $$z = \Phi(x) = \begin{pmatrix} x^{2} \\ x \\ 1 \end{pmatrix}$$ O mesmo pode ser feito para entradas multivariadas (A função $\Phi$ fica um pouco mais complexa) e qualquer expansão de grau polinomial finito. Por exemplo, para entradas bidimensionais, obtemos um modelo de grau 2 se: $$\Phi(x) = \begin{pmatrix} x_{1}^{2} \\ x_{2}^{2} \\ x_{1}x_{2} \\ x_{1} \\ x_{2} \\ 1 \end{pmatrix}$$

**Exemplo: Regressão Polinomial em funções não-lineares**

Considere o problema de regressão univariada $(D = 1)$ em que as entradas pertencem ao intervalo $\lbrack - 10,10\rbrack$ e a função alvo é dada por $f(x) = \sin(x)/x$, também conhecida como função *sinc*. Além disso, utilizamos um conjunto de dados com $200$ pares de entrada-saída $\left( x_{i},y_{i} \right)$, em que as saídas estão corrompidas por um ruído aditivo gaussiano, ou seja, $y = f(x) + \varepsilon$ com $\varepsilon \sim N(0,0.05)$. Nesse exemplo, empregamos modelos polinomiais com grau $d \in \left\{ 1,2,5,10 \right\}$.

A Figura abaixxo mostra as predições obtidas com os diferentes modelos. Observe que, para $d = 1$, temos o modelo de regressão linear básico que estudamos anteriormente, e a aproximação consiste em uma reta. Note que, à medida que aumentamos o grau do polinômio, o modelo se torna mais flexível, conseguindo aproximar melhor os dados (represen- tados por pequenos círculos pretos), e portanto o melhor modelo possui $d = 10$ (curva em vermelho)

![](assets/polynomial-regression.png)

<a id="secao-16"></a>

### Funções de base radiais

Vamos agora estudar um novo formato para a transformação $\Phi$. De forma simples, ele consiste em escolher $M$ pontos $c_{1},c_{2},\ldots,c_{M}$ do ${\mathbb{R}}^{D}$, também chamado de centros ou protótipos, e então criar o vetor de regressores $z = \Phi(x)$ combinando funções radiais em torno de cada um dos centros.

**Definição: Função radial no RR^D**

Dada uma métrica $\| \cdot \|$ no ${\mathbb{R}}^{D}$ e $c \in {\mathbb{R}}^{D}$, dizemos que $f_{c}:{\mathbb{R}}^{D} \rightarrow {\mathbb{R}}$ é radial se existe uma função $f:\lbrack 0,\infty) \rightarrow {\mathbb{R}}$ tal que $f_{c}(x) = f\left( \| x - c\| \right)$

Podemos então construir uma transformação $\Phi$ que utiliza $M$ funções radiais da forma: $$\Phi(x) = \begin{pmatrix} f_{c_{1}}(x) \\ f_{c_{2}}(x) \\ \vdots \\ f_{c_{M}}(x) \end{pmatrix} = \begin{pmatrix} f\left( \| x - c_{1}\| \right) \\ f\left( \| x - c_{2}\| \right) \\ \vdots \\ f\left( \| x - c_{M}\| \right) \end{pmatrix}$$

Quando as funções $f_{c_{1}}(x),...f_{c_{M}}(x)$ são linearmente independentes, e a matriz $$\begin{pmatrix} f_{c_{1}}\left( c_{1} \right) & f_{c_{2}}\left( c_{1} \right) & \ldots & f_{c_{M}}\left( c_{1} \right) \\ f_{c_{1}}\left( c_{2} \right) & f_{c_{2}}\left( c_{2} \right) & \ldots & f_{c_{M}}\left( c_{2} \right) \\ \vdots \\ f_{c_{1}}\left( c_{M} \right) & f_{c_{2}}\left( c_{M} \right) & \ldots & f_{c_{M}}\left( c_{M} \right) \end{pmatrix}$$ é não-singular, essas funções são chamadas de funções de base radiais (radial basis functions, RBFs). modelo de regressão linear com transformações através de funções de base radiais constitui uma classe de rede neurais chamada redes RBF [(Broomhead & Lowe, 1988)](https://sci2s.ugr.es/keel/pdf/algorithm/articulo/1988-Broomhead-CS.pdf)

A completa definição da transformação $\Phi$ envolve duas escolhas: a localização dos centros $c_{1},\ldots,c_{M}$ e a função de base radial.

**Escolhendo os centros**. Um das formas mais simples de escolher $M$ protótipos consiste em selecionar aleatoriamente entradas $x_{i}$ do próprio conjunto de dados. Nessa abordagem, o conjunto de centros é um subconjunto $\left\{ c_{1},...,c_{M} \right\} \subseteq \left\{ x_{1},...,x_{N} \right\}$ qualquer de tamanho $M$.

No entanto, a estratégia mais comum e que se tornou padrão consiste em selecionar centros de forma a capturar a densidade dos vetores de entrada. Para isso, normalmente empregamos métodos de análise de agrupamentos (clustering), tais como o k-médias (Lloyd, 1982). A discussão sobre o impacto da escolha dos centros está fora do escopo deste material

**Escolhendo a função de base radial**. Existem diversas escolhas possíveis para $f_{c_{i}}$ , algumas das mais notórias são:

1.  Gaussiana:

$$f_{c_{i}}(x) = e^{- \gamma\| x - c_{i}\|_{2}^{2}}$$ onde $\gamma > 0$ é uma constante;

2.  Multi-quadrática:

$$f_{c_{i}}(x) = \sqrt{1 + \varepsilon\| x - c_{i}\|_{2}^{2}}$$ onde $\varepsilon > 0$ é uma constante.

**Redes RBF e interpolação**: As redes RBF foram originalmente propostas para resolver problemas de interpolação: Dado um conjunto de $N$ pares entrada saída $\left( x_{i},y_{i} \right)$, queremos encontrar uma função $g$ tal que $$g\left( x_{i} \right) = y_{i},\text{\quad\quad}i = 1,...,N$$

Escolhendo $g$ tal que $g(x) = \theta^{T}\Phi(x) = \theta^{T}z$ com $N$ funções de base radiais e $c_{i} = x_{i}$ para todo $i = 1,\ldots,N$ , a matriz de regressores $Z:Z_{ij} = f_{c_{j}}\left( x_{i} \right)$ é quadrada e a condição de interpolação equivale ao sistema linear: $$Z\theta = y\text{ com }Z = \begin{pmatrix} f_{c_{1}}\left( x_{1} \right) & f_{c_{2}}\left( x_{1} \right) & \ldots & f_{c_{N}}\left( x_{1} \right) \\ f_{c_{1}}\left( x_{2} \right) & f_{c_{2}}\left( x_{2} \right) & \ldots & f_{c_{N}}\left( x_{2} \right) \\ \vdots \\ f_{c_{1}}\left( x_{N} \right) & f_{c_{2}}\left( x_{N} \right) & \ldots & f_{c_{N}}\left( x_{N} \right) \end{pmatrix}$$ Dessa forma, obtemos um interpolador com a rede RBF desde que a matriz $Z$ seja não-singular. Micchelli (1986) mostrou que matrizes $Z$ formadas usando tanto funções radiais gaussianas quanto multi-quadráticas são não-singulares (possuem inversa), e a única condição para isso é que os centros (ou equivalentemente as entradas) sejam distintos. Como consequência, no caso em que $M < N$ e os centros são um subconjunto das entradas, a matriz $Z^{T}Z$ utilizada na solução dos mínimos quadrados possui inversa.

**Exemplo: Redes RBF**

Este exemplo ilustra o impacto do número de funções de base na aproximação realizada por redes RBF com função radial Gaussiana. Para isso, vamos utilizar novamente o problema de regressão com função alvo *sinc*, com exatamente a mesma configuração descrita no último exemplo. Os centros das RBFs foram selecionados de forma igualmente espaçados no intervalo $\lbrack - 10,10\rbrack$.

A Figura abaixo (lado esquerdo) mostra a aproximação obtida usando uma rede RBF com $M \in \left\{ 5,20 \right\}$ e $\gamma = 1$. Note que o modelo com $k = 20$ aproxima melhor os dados. O aumento no número de funções de base aumenta a flexibilidade do modelo em se ajustar aos dados. Na Figura à direita, percebemos que o aumento no valor de $\gamma$ produz funções radiais com variância (ou largura de banda) pequena, resultando em um aspecto oscilatório da curva de aproximação

![](assets/rbf-regression.png)

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Conteúdos relacionados

- [Problemas de Mínimos Quadrados — Álgebra Linear Numérica](../algebra-linear-numerica/problemas-de-minimos-quadrados.md)


## Percurso de estudo

[Trilha: A1](../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Método dos Vizinhos mais próximos (k-NN)](metodo-dos-vizinhos-mais-proximos-k-nn.md)
- Próximo: [Regressão Logística](regressao-logistica.md)
