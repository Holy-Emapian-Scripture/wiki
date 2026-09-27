---
layout: "default"
title: "Gaussian and Bernoulli Mixture Models"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../trilhas/aprendizado-de-maquina/a3.md"
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

# Gaussian and Bernoulli Mixture Models


<a id="algoritmo-em-variacional"></a>
<a id="secao-13"></a>

## Algoritmo EM Variacional

O Algorimto EM que vimos agora é uma aplicação de uma versão mais geral do algoritmo EM. Ele tem como objetivo achar a verossimilhança de modelos com variáveis latentes

Representamos o conjunto de dados por uma matriz $X$ onde a $n$-ésima linha é representada por $x_{n}^{T}$. De forma similar, definimos o conjunto de variáveis latentes como uma matriz $Z$ onde a $n$-ésima linha é representada por $z_{n}^{T}$. A função de log-verossimilhança do modelo é então dada por: $$\ln p\left( X~\vert ~\theta \right) = \ln\left\{ \sum_{Z}p\left( X,Z~\vert ~\theta \right) \right\}$$<a id="x-marginal-log-likelihood"></a>

Note que nossa discussão também se aplica com variáveis latentes contínuas trocando a soma interna por uma integral. O problema central aqui é que o somatório/integral no interior do log torna a maximização da verossimilhança difícil. Chamamos o conjunto $\left\{ X,Z \right\}$ de **dataset completo**, enquanto chamamos o conjunto $\left\{ X \right\}$ de **dataset incompleto**. O problema é que não podemos observar $Z$, nosso conhecimento sobre as variáveis latentes se dá apenas a partir da posteriori $p\left( Z~\vert ~X,\theta \right)$. Como não conseguimos olhar diretamente para $\ln p\left( X,Z\vert \theta \right)$, então consideramos seu valor esperado sobre a distribuição posteriori de $Z$ dado $X$ e os parâmetros atuais $\theta^{(t)}$. O foco desse capítulo não é dar uma derivação formal do algoritmo EM, porém, vamos deixar o framework geral escrito e mostrar ele sendo aplicado novamente ao caso das GMMs.

**Algoritmo EM (Geral)**

1.  **function** *EM*($X$) {

    1.  **initialize** $\theta^{(0)}$

    2.  **repeat** {

        1.  **// Passo E**

        2.  *calcular* $p\left( Z~\vert ~X,\theta^{(t)} \right)$

        3.  

        4.  **// Passo M**

        5.  $\mathcal{Q}(\theta,\theta^{(t)}) = \sum_{z}p\left( z~\vert ~X,\theta^{(t)} \right)\ln p\left( X,z~\vert ~\theta \right)$

        6.  $\theta^{(t + 1)} = \text{ argmax}_{\theta}Q\left( \theta,\theta^{(t)} \right)$

        7.  **// Checando se convergiu**

        8.  **if** **not** converged **yet** {

            1.  $\theta^{(t)} = \theta^{(t + 1)}$

        9.  }

2.  }

Revisitando o caso das GMMs, vamos primeiro considerar o problema de maximizar a verossimilhança do dataset completo, que é dado por: $$p\left( X,Z~\vert ~\mu,\Sigma,\pi \right) = \prod_{n = 1}^{N}\prod_{k = 1}^{K}\left\{ \pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right) \right\}^{z_{nk}}$$ aplicando log $$\ln p\left( X,Z~\vert ~\mu,\Sigma,\pi \right) = \sum_{n = 1}^{N}\sum_{k = 1}^{K}z_{nk}\left\{ \ln\pi_{k} + \ln N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right) \right\}$$ podemos ver que, em comparação com a equação [\[x-marginal-log-likelihood\]](#x-marginal-log-likelihood), o log da verossimilhança tem o somatório do lado de fora, o que facilita a derivada. O problema é que não podemos observar $Z$, então vamos considerar o valor esperado do log da verossimilhança do dataset completo sobre a distribuição posteriori de $Z$ dado $X$.

Pelo teorema de bayes, vamos chegar que a posteriori é obtida com: $$p\left( Z~\vert ~X,\mu,\Sigma,\pi \right) \propto p\left( X,Z~\vert ~\mu,\Sigma,\pi \right) = \prod_{n = 1}^{N}\prod_{k = 1}^{K}\left\{ \pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right) \right\}^{z_{nk}}$$ perceba que isso mostra que cada $z_{n}$ é independente dos outros $z_{m}$ dado $x_{n}$. Então podemos escrever a média de $z_{nk}$ sobre o regime da posteriori como: $$\begin{aligned} {\mathbb{E}}_{z_{nk} \sim p\left( z_{n}\vert x_{n},\ldots \right)}\left\lbrack z_{nk} \right\rbrack & = \frac{\sum_{z_{nk}}z_{nk}\left\lbrack \pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right) \right\rbrack^{z_{nk}}}{\sum_{z_{nj}}\left\lbrack \pi_{j}N\left( x_{n}~\vert ~\mu_{j},\Sigma_{j} \right) \right\rbrack^{z_{nj}}} \\ & = \frac{\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\sum_{j = 1}^{K}\pi_{j}N\left( x_{n}~\vert ~\mu_{j},\Sigma_{j} \right)} = \gamma(z_{nk}) \end{aligned}$$

Então vamos ter que a esperança da log-verossimilhança do dataset completo sobre a distribuição posteriori de $Z$ dado $X$ é: $${\mathbb{E}}_{Z \sim p\left( Z\vert X,\mu,\Sigma,\pi \right)}\left\lbrack \ln p\left( X,Z~\vert ~\mu,\Sigma,\pi \right) \right\rbrack = \sum_{n = 1}^{N}\sum_{k = 1}^{K}\gamma(z_{nk})\left\{ \ln\pi_{k} + \ln N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right) \right\}$$<a id="mean-log-likelihood-complete-data"></a>

Dado essa equação, podemos fixar valores iniciais para $\mu$, $\Sigma$ e $\pi$ para calcular $\gamma(z_{nk})$, depois maximizamos os valores dos parâmetros do modelo com base na equação [\[mean-log-likelihood-complete-data\]](#mean-log-likelihood-complete-data) com as fórmulas já vistas anteriormente no [\[optimal-mean-k\]](../expectation-maximization-em-para-gmms/index.md#optimal-mean-k), [\[optimal-covariance-k\]](../expectation-maximization-em-para-gmms/index.md#optimal-covariance-k) e [\[optimal-mixing-coefficient-k\]](../expectation-maximization-em-para-gmms/index.md#optimal-mixing-coefficient-k) e repetimos esse processo até que a convergência seja alcançada. Esse é o algoritmo EM aplicado aos GMMs.

<a id="bernoulli-mixture-models"></a>
<a id="secao-14"></a>

## Bernoulli Mixture Models

Agora que vimos os GMMs e como derivar o algoritmo de resolução do problema, que tal analisarmos o caso de variáveis com distribuições discretas? Vamos considerar o caso de variáveis binárias, que podem ser modeladas com distribuições de Bernoulli. Esse modelo também é conhecido como **Análise de Classe Latentes**

**Definição: Vetor Bernoulli**

Considere um conjunto de $D$ variáveis aleatórias binárias $X = \left\{ x_{1},x_{2},\ldots,x_{D} \right\}$, onde cada variável $x_{i}$ segue uma distribuição de Bernoulli com parâmetro $\mu_{i}$, ou seja, ${\mathbb{P}}(x_{i} = 1) = \mu_{i}$ e ${\mathbb{P}}(x_{i} = 0) = 1 - \mu_{i}$. O vetor aleatório $x$ é chamado de vetor Bernoulli e sua função de probabilidade conjunta é dada por: $$p\left( x\vert \mu \right) = \prod_{i = 1}^{D}\mu_{i}^{x_{i}}\left( 1 - \mu_{i} \right)^{1 - x_{i}}$$ onde $x \in {\mathbb{R}}^{D}$ e $\mu \in {\mathbb{R}}^{D}$

**Teorema: Validade da distribuição**

Seja $p\left( x\vert \mu \right)$ um Modelo de Mistura de Bernoulli. Então, $p\left( x\vert \mu \right)$ é uma distribuição de probabilidade válida, ou seja, $p\left( x\vert \mu \right) \geq 0$ para todo $x$ e $\sum_{x \in \left\{ 0,1 \right\}^{D}}p\left( x\vert \mu \right) = 1$.

**Demonstração**

Para mostrar que $p\left( x\vert \mu \right) \geq 0$, note que cada termo na multiplicação é não-negativo, pois $\mu_{i}^{x_{i}} \geq 0$ e $\left( 1 - \mu_{i} \right)^{1 - x_{i}} \geq 0$. Portanto, $p\left( x\vert \mu \right) \geq 0$ para todo $x$.

Para mostrar que a soma de $p\left( x\vert \mu \right)$ sobre todos os possíveis vetores binários de dimensão $D$ é igual a 1, usamos a propriedade da distribuição de Bernoulli: $$\sum_{x \in \left\{ 0,1 \right\}^{D}}p\left( x\vert \mu \right) = \sum_{x \in \left\{ 0,1 \right\}^{D}}\prod_{i = 1}^{D}\mu_{i}^{x_{i}}\left( 1 - \mu_{i} \right)^{1 - x_{i}}$$ Como cada termo na multiplicação é independente dos outros termos, podemos reescrever a soma como um produto de somas: $$= \prod_{i = 1}^{D}\sum_{x_{i} \in \left\{ 0,1 \right\}}\mu_{i}^{x_{i}}\left( 1 - \mu_{i} \right)^{1 - x_{i}}$$ Cada soma interna é igual a 1, pois: $$\sum_{x_{i} \in \left\{ 0,1 \right\}}\mu_{i}^{x_{i}}\left( 1 - \mu_{i} \right)^{1 - x_{i}} = \mu_{i} + \left( 1 - \mu_{i} \right) = 1$$ Portanto, temos: $$\sum_{x \in \left\{ 0,1 \right\}^{D}}p\left( x\vert \mu \right) = \prod_{i = 1}^{D}1 = 1$$

Conseguimos ver também que: $$\begin{aligned} {\mathbb{E}}\lbrack x\rbrack & = \mu \\ \text{Cov}\lbrack x\rbrack & = \text{ diag}\left( \mu_{i}\left( 1 - \mu_{i} \right) \right) \end{aligned}$$

**Definição: Modelo de Mistura de Bernoulli**

Um Modelo de Mistura de Bernoulli é definido como: $$p\left( x\vert \mu,\pi \right) = \sum_{k = 1}^{K}\pi_{k}p\left( x\vert \mu_{k} \right) = \sum_{k = 1}^{K}\pi_{k}\prod_{i = 1}^{D}\mu_{ki}^{x_{i}}\left( 1 - \mu_{ki} \right)^{1 - x_{i}}$$ onde $\pi_{k}$ são os pesos dos clusters, que satisfazem $\sum_{k = 1}^{K}\pi_{k} = 1$, e $\mu_{ki}$ são os parâmetros da distribuição de Bernoulli para o cluster $k$.

**Teorema: Validade da distribuição**

Seja $p\left( x\vert \mu,\pi \right)$ um Modelo de Mistura de Bernoulli com $K$ componentes. Então, $p\left( x\vert \mu,\pi \right)$ é uma distribuição de probabilidade válida, ou seja, $p\left( x\vert \mu,\pi \right) \geq 0$ para todo $x$ e $\sum_{x \in \left\{ 0,1 \right\}^{D}}p\left( x\vert \mu,\pi \right) = 1$.

**Demonstração**

Para mostrar que $p\left( x\vert \mu,\pi \right) \geq 0$, note que cada termo na soma é não-negativo, pois $\pi_{k} \geq 0$ e $p\left( x\vert \mu_{k} \right) \geq 0$. Portanto, $p\left( x\vert \mu,\pi \right) \geq 0$ para todo $x$.

Para mostrar que a soma de $p\left( x\vert \mu,\pi \right)$ sobre todos os possíveis vetores binários de dimensão $D$ é igual a 1, usamos a linearidade da soma: $$\sum_{x \in \left\{ 0,1 \right\}^{D}}p\left( x\vert \mu,\pi \right) = \sum_{x \in \left\{ 0,1 \right\}^{D}}\sum_{k = 1}^{K}\pi_{k}p\left( x\vert \mu_{k} \right)$$ Podemos trocar a ordem das somas: $$= \sum_{k = 1}^{K}\pi_{k}\sum_{x \in \left\{ 0,1 \right\}^{D}}p\left( x\vert \mu_{k} \right)$$ Cada soma interna é igual a 1, pois $p\left( x\vert \mu_{k} \right)$ é uma distribuição de probabilidade válida. Portanto, temos: $$= \sum_{k = 1}^{K}\pi_{k} \ast 1 = \sum_{k = 1}^{K}\pi_{k} = 1$$

A média e covariância dessa distribuição de mistura é dada por: $$\begin{aligned} {\mathbb{E}}\lbrack x\rbrack & = \sum_{k = 1}^{K}\pi_{k}\mu_{k} \\ \text{Cov}\lbrack x\rbrack & = \sum_{k = 1}^{K}\pi_{k}\left( \Sigma_{k} + \mu_{k}\mu_{k}^{T} \right) - {\mathbb{E}}\lbrack x\rbrack{\mathbb{E}}\lbrack x\rbrack^{T} \end{aligned}$$

onde $\Sigma_{k} = \text{ diag}\left( \mu_{ki}\left( 1 - \mu_{ki} \right) \right)$. Dado um conjunto de dados $X = \left\{ x_{1},\ldots,x_{N} \right\}$ que segue o modelo de mistura de Bernoulli, a função de log-verossimilhança é dada por: $$\ln p\left( X~\vert ~\mu,\pi \right) = \sum_{n = 1}^{N}\ln p\left( x_{n}~\vert ~\mu,\pi \right) = \sum_{n = 1}^{N}\ln\left\{ \sum_{k = 1}^{K}\pi_{k}p\left( x_{n}~\vert ~\mu_{k} \right) \right\}$$

vemos novamente a mesma dificuldade de maximizar a verossimilhança diretamente, então vamos encontrar as fórmulas de atualização para o algoritmo EM aplicado ao modelo de mistura de Bernoulli.

Para isso, definimos, assim como no caso de mistura de gaussianas, a variável latente $z_{n}$ que indica de qual cluster o ponto $x_{n}$ foi gerado. A distribuição condicional de $x_{n}$ dado $z_{n}$ é dada por: $$p\left( x_{n}\vert z_{n},\mu \right) = \prod_{k = 1}^{K}{p\left( x\vert \mu_{k} \right)}^{z_{nk}}$$ e priori aqui é a mesma usada no caso de mistura de gaussianas: $$p\left( z_{n}\vert \pi \right) = \prod_{k = 1}^{K}\pi_{k}^{z_{nk}}$$

Antes de enunciarmos os teoremas com os valores ótimos, precisamos escrever a função de log-verossimilhança do dataset completo, que é dada por: $$\ln p\left( X,Z~\vert ~\mu,\pi \right) = \sum_{n = 1}^{N}\sum_{k = 1}^{K}z_{nk}\left\{ \ln\pi_{k} + \sum_{i = 1}^{D}\left\lbrack x_{ni}\ln\mu_{ki} + \left( 1 - x_{ni} \right)\ln\left( 1 - \mu_{ki} \right) \right\rbrack \right\}$$

E a esperança da log-verossimilhança do dataset completo sobre a distribuição posteriori de $Z$ dado $X$ é: $${\mathbb{E}}_{Z \sim p\left( Z\vert X,\mu,\pi \right)}\left\lbrack \ln p\left( X,Z~\vert ~\mu,\pi \right) \right\rbrack = \sum_{n = 1}^{N}\sum_{k = 1}^{K}\gamma(z_{nk})\left. \begin{array}{r} \{\ln\pi_{k} \\ + \sum_{i = 1}^{D}\left\lbrack x_{ni}\ln\mu_{ki} + \left( 1 - x_{ni} \right)\ln\left( 1 - \mu_{ki} \right) \right\rbrack\} \end{array} \right.$$ onde $\gamma(z_{nk})$ é a probabilidade de $z_{nk} = 1$ sob a distribuição posteriori. No passo **E** do algoritmo, isso é calculado com o teorema de bayes: $$\gamma(z_{nk}) = \frac{p\left( z_{nk} = 1 \right)p\left( x_{n}~\vert ~z_{nk} = 1,\mu_{k} \right)}{p\left( x_{n}~\vert ~\mu,\pi \right)} = \frac{\pi_{k}p\left( x_{n}~\vert ~\mu_{k} \right)}{\sum_{j = 1}^{K}\pi_{j}p\left( x_{n}~\vert ~\mu_{j} \right)}$$

**Teorema: Valor ótimo de $\mu$**

Fixando os parâmetros do modelo e variando apenas $\mu$, o valor ótimo de $\mu_{ki}$ é dado por: $$\mu_{ki} = \frac{\sum_{n = 1}^{N}\gamma(z_{nk})x_{ni}}{\sum_{n = 1}^{N}\gamma(z_{nk})} = \frac{1}{N_{k}}\sum_{n = 1}^{N}\gamma(z_{nk})x_{ni}$$ ou $$\mu_{k} = \frac{\sum_{n = 1}^{N}\gamma(z_{nk})x_{n}}{\sum_{n = 1}^{N}\gamma(z_{nk})} = \frac{1}{N_{k}}\sum_{n = 1}^{N}\gamma(z_{nk})x_{n}$$

**Demonstração**

Para encontrar o valor ótimo de $\mu_{ki}$, derivamos a função de log-verossimilhança em relação a $\mu_{ki}$ e igualamos a zero: $$\frac{\partial\ln p\left( X,Z~\vert ~\mu,\pi \right)}{\partial\mu_{ki}} = \sum_{n = 1}^{N}\gamma(z_{nk})\frac{x_{ni} - \mu_{ki}}{\mu_{ki}\left( 1 - \mu_{ki} \right)} = 0$$ Rearranjando os termos, obtemos: $$\sum_{n = 1}^{N}\gamma(z_{nk})x_{ni} = \mu_{ki}\sum_{n = 1}^{N}\gamma(z_{nk})$$ Dividindo ambos os lados por $\sum_{n = 1}^{N}\gamma(z_{nk})$, obtemos a expressão desejada para $\mu_{ki}$.

**Teorema: Valor ótimo de $\pi$**

Fixando os parâmetros do modelo e variando apenas $\pi$, o valor ótimo de $\pi_{k}$ é dado por: $$\pi_{k} = \frac{\sum_{n = 1}^{N}\gamma(z_{nk})}{N} = \frac{N_{k}}{N}$$

**Demonstração**

Sabendo que $\sum_{k}\pi_{k} = 1$, usamos de multiplicadores de lagrange para encontrar o valor ótimo de $\pi_{k}$. Definimos a função lagrangiana como: $$L(\pi,\lambda) = \ln p\left( X,Z~\vert ~\mu,\pi \right) + \lambda\left( \sum_{k = 1}^{K}\pi_{k} - 1 \right)$$ Derivando em relação a $\pi_{k}$ e igualando a zero, obtemos: $$\frac{\partial L}{\partial\pi_{k}} = \frac{\gamma(z_{nk})}{\pi_{k}} + \lambda = 0$$ Isolando $\pi_{k}$, obtemos: $$\pi_{k} = - \frac{\lambda}{\gamma(z_{nk})}$$ Usando a condição de normalização $\sum_{k}\pi_{k} = 1$, podemos encontrar o valor de $\lambda$: $$\sum_{k = 1}^{K} - \frac{\lambda}{\gamma(z_{nk})} = 1$$ Resolvendo para $\lambda$, obtemos: $$\lambda = - \frac{1}{\sum_{k = 1}^{K}\frac{1}{\gamma(z_{nk})}}$$ Substituindo esse valor de $\lambda$ na expressão para $\pi_{k}$, obtemos: $$\pi_{k} = \frac{\gamma(z_{nk})}{\sum_{j = 1}^{K}\gamma(z_{nj})} = \frac{N_{k}}{N}$$

<a id="expectation-maximization-em-para-gmms"></a>
<a id="secao-12"></a>

## Expectation-Maximization (EM) para GMMs

Para facilitar o entendimento das contas, defina $N_{k} = \sum_{n = 1}^{N}\gamma(z_{nk})$

<a id="optimal-mean-k"></a>

**Teorema**

Fixando os parâmetros do modelo e variando apenas $\mu$, o valor ótimo de $\mu_{k}$ é dado por: $$\mu_{k} = \frac{\sum_{n = 1}^{N}\gamma(z_{nk})x_{n}}{\sum_{n = 1}^{N}\gamma(z_{nk})} = \frac{1}{N_{k}}\sum_{n = 1}^{N}\gamma(z_{nk})x_{n}$$

**Demonstração**

Para encontrar o valor ótimo de $\mu_{k}$, derivamos a função de log-verossimilhança em relação a $\mu_{k}$ e igualamos a zero: $$\frac{\partial\ln p\left( X~\vert ~\mu,\Sigma,\pi \right)}{\partial\mu_{k}} = \sum_{n = 1}^{N}\underset{\gamma(z_{nk})}{\underbrace{\frac{\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\sum_{j = 1}^{K}\pi_{j}N\left( x_{n}~\vert ~\mu_{j},\Sigma_{j} \right)}}}\frac{1}{N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}\frac{\partial N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\partial\mu_{k}} = 0$$ A derivada da densidade gaussiana em relação a $\mu_{k}$ é dada por: $$\frac{\partial N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\partial\mu_{k}} = N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)\Sigma_{k}^{- 1}\left( x_{n} - \mu_{k} \right)$$ Substituindo isso na equação anterior, obtemos: $$\sum_{n = 1}^{N}\gamma(z_{nk})\Sigma_{k}^{- 1}\left( x_{n} - \mu_{k} \right) = 0$$ Multiplicando ambos os lados por $\Sigma_{k}$, obtemos: $$\sum_{n = 1}^{N}\gamma(z_{nk})\left( x_{n} - \mu_{k} \right) = 0$$ Rearranjando os termos, obtemos: $$\mu_{k}\sum_{n = 1}^{N}\gamma(z_{nk}) = \sum_{n = 1}^{N}\gamma(z_{nk})x_{n}$$ Dividindo ambos os lados por $\sum_{n = 1}^{N}\gamma(z_{nk})$, obtemos a expressão desejada para $\mu_{k}$.

<a id="optimal-covariance-k"></a>

**Teorema**

Fixando os parâmetros do modelo e variando apenas $\Sigma$, o valor ótimo de $\Sigma_{k}$ é dado por: $$\Sigma_{k} = \frac{\sum_{n = 1}^{N}\gamma(z_{nk})\left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T}}{\sum_{n = 1}^{N}\gamma(z_{nk})} = \frac{1}{N_{k}}\sum_{n = 1}^{N}\gamma(z_{nk})\left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T}$$

**Demonstração**

Para encontrar o valor ótimo de $\Sigma_{k}$, derivamos a função de log-verossimilhança em relação a $\Sigma_{k}$ e igualamos a zero: $$\frac{\partial\ln p\left( X~\vert ~\mu,\Sigma,\pi \right)}{\partial\Sigma_{k}} = \sum_{n = 1}^{N}\underset{\gamma(z_{nk})}{\underbrace{\frac{\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\sum_{j = 1}^{K}\pi_{j}N\left( x_{n}~\vert ~\mu_{j},\Sigma_{j} \right)}}}\frac{1}{N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}\frac{\partial N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\partial\Sigma_{k}} = 0$$ A derivada da densidade gaussiana em relação a $\Sigma_{k}$ é dada por: $$\frac{\partial N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\partial\Sigma_{k}} = \frac{1}{2}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)\left( \Sigma_{k}^{- 1}\left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T}\Sigma_{k}^{- 1} - \Sigma_{k}^{- 1} \right)$$ Substituindo isso na equação anterior, obtemos: $$\sum_{n = 1}^{N}\gamma(z_{nk})\left( \Sigma_{k}^{- 1}\left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T}\Sigma_{k}^{- 1} - \Sigma_{k}^{- 1} \right) = 0$$ Multiplicando ambos os lados por $\Sigma_{k}$, obtemos: $$\sum_{n = 1}^{N}\gamma(z_{nk})\left( \left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T}\Sigma_{k}^{- 1} - I \right) = 0$$ Rearranjando os termos, obtemos: $$\sum_{n = 1}^{N}\gamma(z_{nk})\left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T} = \sum_{n = 1}^{N}\gamma(z_{nk})\Sigma_{k}$$ Dividindo ambos os lados por $\sum_{n = 1}^{N}\gamma(z_{nk})$, obtemos a expressão desejada para $\Sigma_{k}$.

<a id="optimal-mixing-coefficient-k"></a>

**Teorema**

Fixando os parâmetros do modelo e variando apenas $\pi$, o valor ótimo de $\pi_{k}$ é dado por: $$\pi_{k} = \frac{\sum_{n = 1}^{N}\gamma(z_{nk})}{N} = \frac{N_{k}}{N}$$

**Demonstração**

Sabendo que $\sum_{k}\pi_{k} = 1$, usamos de multiplicadores de lagrange para encontrar o valor ótimo de $\pi_{k}$. Definimos a função lagrangiana como: $$L(\pi,\lambda) = \ln p\left( X~\vert ~\mu,\Sigma,\pi \right) + \lambda\left( \sum_{k = 1}^{K}\pi_{k} - 1 \right)$$ Derivando em relação a $\pi_{k}$ e igualando a zero, obtemos: $$\frac{\partial L}{\partial\pi_{k}} = \frac{\gamma(z_{nk})}{\pi_{k}} + \lambda = 0$$ Isolando $\pi_{k}$, obtemos: $$\pi_{k} = - \frac{\lambda}{\gamma(z_{nk})}$$ Usando a condição de normalização $\sum_{k}\pi_{k} = 1$, podemos encontrar o valor de $\lambda$: $$\sum_{k = 1}^{K} - \frac{\lambda}{\gamma(z_{nk})} = 1$$ Resolvendo para $\lambda$, obtemos: $$\lambda = - \frac{1}{\sum_{k = 1}^{K}\frac{1}{\gamma(z_{nk})}}$$ Substituindo esse valor de $\lambda$ na expressão para $\pi_{k}$, obtemos: $$\pi_{k} = \frac{\gamma(z_{nk})}{\sum_{j = 1}^{K}\gamma(z_{nj})} = \frac{N_{k}}{N}$$

Vale ressaltar que o [\[optimal-mean-k\]](#optimal-mean-k), [\[optimal-covariance-k\]](#optimal-covariance-k) e [\[optimal-mixing-coefficient-k\]](#optimal-mixing-coefficient-k) não representam formas fechadas dos parâmetros do modelo, pois eles dependem de $\gamma(z_{nk})$, que por sua vez depende dos próprios parâmetros do modelo. Portanto, não podemos resolver essas equações diretamente. Em vez disso, usamos o algoritmo EM, que alterna entre calcular $\gamma(z_{nk})$ com os parâmetros atuais (passo E) e atualizar os parâmetros do modelo usando as fórmulas acima (passo M).

**Algoritmo EM**

1.  **function** *EM*($X$) {

    1.  **initialize** $\mu_{k},\Sigma_{k},\pi_{k}$

    2.  **// Passo E**

    3.  $\gamma(z_{nk}) = \frac{\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\sum_{j = 1}^{K}\pi_{j}N\left( x_{n}~\vert ~\mu_{j},\Sigma_{j} \right)}$

    4.  **// Passo M**

    5.  $N_{k} = \sum_{n = 1}^{N}\gamma(z_{nk})$

    6.  $\mu_{k} = \frac{1}{N_{k}}\sum_{n = 1}^{N}\gamma(z_{nk})x_{n}$

    7.  $\Sigma_{k} = \frac{1}{N_{k}}\sum_{n = 1}^{N}\gamma(z_{nk})\left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T}$

    8.  $\pi_{k} = \frac{N_{k}}{N}$

    9.  **// Calcular a log-verossimilhança**

    10. $\ln p\left( X~\vert ~\mu,\Sigma,\pi \right) = \sum_{n = 1}^{N}\ln\left\{ \sum_{k = 1}^{K}\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right) \right\}$

2.  }

<a id="introducao-e-definicao"></a>
<a id="secao-10"></a>

## Introdução e Definição

No k-means, cada ponto é atribuído a um único cluster, o que significa que a fronteira entre os clusters é rígida. No entanto, em muitos casos, pode ser mais apropriado permitir que cada ponto tenha uma probabilidade de pertencer a cada cluster. Isso nos leva aos Modelos de Mistura Gaussiana (GMMs), que é uma generalização do K-means.

Aqui, nós supomos que cada ponto **pode** ter saído de um dos $K$ clusters, mas não sabemos de qual, cada cluster esse sendo representado por uma distribuição gaussiana. Cada cluster $k$ é caracterizado por uma média $\mu_{k}$ e uma matriz de covariância $\Sigma_{k}$. Além disso, cada cluster tem um peso $\pi_{k}$, que representa a proporção de pontos que pertencem a esse cluster.

**Definição: Modelo de Mistura Gaussiana**

Um Modelo de Mistura Gaussiana é definido como: $$p(x) = \sum_{k = 1}^{K}\pi_{k}N\left( x~\vert ~\mu_{k},\Sigma_{k} \right)$$ onde $N\left( x~\vert ~\mu_{k},\Sigma_{k} \right)$ é a densidade da distribuição gaussiana com média $\mu_{k}$ e covariância $\Sigma_{k}$, e $\pi_{k}$ são os pesos dos clusters, que satisfazem $\sum_{k = 1}^{K}\pi_{k} = 1$.

**Teorema: Validade da distribuição**

Seja $p(x)$ um Modelo de Mistura Gaussiana com $K$ componentes. Então, $p(x)$ é uma distribuição de probabilidade válida, ou seja, $p(x) \geq 0$ para todo $x$ e $\int p(x)dx = 1$.

**Demonstração**

Para mostrar que $p(x) \geq 0$, note que cada termo na soma é não-negativo, pois $\pi_{k} \geq 0$ e $N\left( x~\vert ~\mu_{k},\Sigma_{k} \right) \geq 0$. Portanto, $p(x) \geq 0$ para todo $x$.

Para mostrar que a integral de $p(x)$ sobre todo o espaço é igual a 1, usamos a linearidade da integral: $$\begin{aligned} \int p(x)dx & = \int\sum_{k = 1}^{K}\pi_{k}N\left( x~\vert ~\mu_{k},\Sigma_{k} \right)dx \\ & = \sum_{k = 1}^{K}\pi_{k}\int N\left( x~\vert ~\mu_{k},\Sigma_{k} \right)dx \\ & = \sum_{k = 1}^{K}\pi_{k} \ast 1 \\ & = \sum_{k = 1}^{K}\pi_{k} \\ & = 1 \end{aligned}$$

Vamos também introduzir o conceito de **variável latente**. Intuitivamente, uma variável latente é uma variável que não observamos diretamente, mas que influencia os dados que observamos. Por exemplo, a classe de um documento em uma análise de tópicos, já que podemos não saber que um documento fala sobre biologia, mas ele influencia nosso modelo a aprender sobre o assunto.

No caso dos GMMs, podemos introduzir uma variável latente $z_{n}$ para cada ponto $x_{n}$, que indica de qual cluster o ponto foi gerado. Especificamente, $z_{n}$ é um vetor one-hot de dimensão $K$, onde $z_{nk} = 1$ se o ponto $x_{n}$ foi gerado pelo cluster $k$, e $z_{nj} = 0$ para $k \neq j$.

Vamos definir a distribuição conjunta de $x_{n}$ e $z_{n}$ como: $$p\left( x_{n},z_{n} \right) = p\left( z_{n} \right)p\left( x_{n}~\vert ~z_{n} \right)$$

a distribuição marginal de $z_{n}$ é definida em termo dos coeficientes de mistura $\pi_{k}$: $${\mathbb{P}}(z_{nk} = 1) = \pi_{k}$$

de forma que $\pi_{k} \geq 0$ e $\sum_{k = 1}^{K}\pi_{k} = 1$ para que $p\left( z_{n} \right)$ seja uma distribuição de probabilidade válida. Por conta da forma que definimos $z_{n}$ como vetor one-hot, podemos reescrever sua distribuição como: $$p\left( z_{n} \right) = \prod_{k = 1}^{K}\pi_{k}^{z_{nk}}$$

Similarmente, a distribuição condicional de $x_{n}$ dado $z_{nk} = 1$ é definida como: $$p\left( x_{n}~\vert ~z_{nk} = 1 \right) = N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)$$

que também pode ser escrita na forma: $$p\left( x_{n}~\vert ~z_{n} \right) = \prod_{k = 1}^{K}{N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}^{z_{nk}}$$

A distribuição conjunta é escrita então como $p\left( z_{n} \right)p\left( x_{n}~\vert ~z_{n} \right)$ e a marginal sobre $x$ é obtida somando sobre todas as possíveis configurações de $z_{n}$: $$p\left( x_{n} \right) = \sum_{z_{n}}p\left( x_{n},z_{n} \right) = \sum_{z_{n}}p\left( z_{n} \right)p\left( x_{n}~\vert ~z_{n} \right) = \sum_{k = 1}^{K}\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)$$

Pode até parecer que, representando a distribuição de $x_{n}$ como uma mistura de gaussianas, estamos apenas complicando as coisas, mas a introdução da variável latente $z_{n}$ nos permite trabalhar com a conjunta (que vai se mostrar ser bem mais fácil de lidar) e também nos dá uma interpretação probabilística do modelo.

Outra quantidade que será importante é a probabilidade posterior de $z_{n}$ dado $x_{n}$ (chamaremos de $\gamma(z_{nk})$), que é dada pelo Teorema de Bayes: $$\begin{aligned} \gamma(z_{nk}) & = {\mathbb{P}}(z_{nk} = 1~\vert ~x_{n}) \\ & = \frac{p\left( z_{nk} = 1 \right)p\left( x_{n}~\vert ~z_{nk} = 1 \right)}{p\left( x_{n} \right)} \\ & = \frac{\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\sum_{j = 1}^{K}\pi_{j}N\left( x_{n}~\vert ~\mu_{j},\Sigma_{j} \right)} \end{aligned}$$

Vamos interpretar $\pi_{k}$ como a probabilidade de que o ponto $x_{n}$ tenha sido gerado pelo cluster $k$ **a posteriori** e $\gamma(z_{nk})$ como a probabilidade de que o ponto $x_{n}$ pertença ao cluster $k$ **a posteriori**. Também podemos chamar $\gamma(z_{nk})$ de *responsabilidade* do cluster $k$ pelo ponto $x_{n}$, pois ela indica o quanto o cluster $k$ é responsável por gerar o ponto $x_{n}$.

<a id="maxima-verossimilhanca"></a>
<a id="secao-11"></a>

## Máxima Verossimilhança

Suponha que temos um conjunto de dados $X = \left\{ x_{1},x_{2},\ldots,x_{N} \right\}$ com $x_{i} \in {\mathbb{R}}^{D}$ e queremos modelar essa matriz $N \times D$ como uma mistura de $K$ gaussianas. As variáveis latentes $Z = \left\{ z_{1},z_{2},\ldots,z_{N} \right\}$ que indicam de qual cluster cada ponto foi gerado também serão representadas por uma matriz $N \times K$ de vetores one-hot. A função de log-verossimilhança do modelo é então dada por: $$\ln p\left( X~\vert ~\mu,\Sigma,\pi \right) = \sum_{n = 1}^{N}\ln p\left( x_{n}~\vert ~\mu,\Sigma,\pi \right) = \sum_{n = 1}^{N}\ln\left\{ \sum_{k = 1}^{K}\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right) \right\}$$

Acaba que maximizar essa verossimilhança diretamente é difícil, pois a presença da soma dentro do log torna a derivada complicada. Uma alternativa válida é maximizar a verossimilhança por métodos de otimização de gradiente, porém, nós vamos utilizar o algoritmo Expectation-Maximization (EM), que é um método iterativo para encontrar estimativas de máxima verossimilhança em modelos com variáveis latentes.

<a id="singularidades-e-identificabilidade"></a>
<a id="secao-15"></a>

## Singularidades e Identificabilidade

É válido ressaltar a existência desse problema, que é intrínsseco do algoritmo que utilizamos (variáveis latentes) no problema de mistura de gaussianas. Para simplicidade e ilustrar o problema (também se aplica à casos mais gerais), considere uma mistura de gaussianas cujos componentes de covariância são matrizes escalares, ou seja, $\Sigma_{k} = \sigma_{k}^{2}I$. Suponha também que um dos componentes da mistura (digamos, o $j$-ésimo) tem sua média $\mu_{j}$ exatamente igual a algum dos pontos do banco ($x_{n} = \mu_{j}$). Esse ponto então vai contribuir para a verossimilhança um termo: $$N\left( x_{n}~\vert ~\mu_{j},\Sigma_{j} \right) = \frac{1}{(2\pi)^{\frac{1}{2}}\sigma_{j}}$$ se considerarmos $\sigma_{j} \rightarrow 0$, então o termo vai para $\infty$ assim como a verossimilhança. Ou seja, o problema de maximização da log-verossimilhança não é bem definido, pois não existe um máximo global. Esse problema é conhecido como **singularidade** e é um problema clássico do algoritmo EM aplicado a modelos de mistura de gaussianas.

Outro problema é que, dado um ponto (não-degenerado) no espaço dos parâmetros, existem permutações dos parâmetros que geram a mesma distribuição de probabilidade. Por exemplo, considere uma mistura de duas gaussianas com parâmetros $\mu_{1},\Sigma_{1},\pi_{1}$ e $\mu_{2},\Sigma_{2},\pi_{2}$. Se permutarmos os índices das gaussianas, ou seja, trocarmos $\mu_{1}$ com $\mu_{2}$, $\Sigma_{1}$ com $\Sigma_{2}$ e $\pi_{1}$ com $\pi_{2}$, a distribuição de probabilidade gerada será a mesma. Esse problema é conhecido como **identificabilidade** e é um problema clássico do algoritmo EM aplicado a modelos de mistura de gaussianas.

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A3](../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Minimzando o Erro de Projeção](../principal-component-analysis/index.md#minimzando-o-erro-de-projecao)
- Próximo: [Variational Autoencoders](../variational-autoencoders/index.md)
