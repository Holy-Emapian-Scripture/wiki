---
layout: "default"
title: "Estatística Bayesiana"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 2
---

[Inferência Estatística](index.md)

<!-- wiki:original:inicio -->

<a id="secao-2"></a>

# Estatística Bayesiana


<a id="introducao"></a>
<a id="secao-3"></a>

## Introdução

Nesse primeiro momento, iremos fazer experimentos assumindo que, ao fazer experimentos e obter resultados $X_{j}$ eles estão saindo de uma distribuição com parâmetro (ou vetor paramétrico) $\theta$, e esse $\theta$ é uma variável aleatória da qual desconhecemos.

<a id="distribuicoes-priori-e-posteriori"></a>
<a id="secao-4"></a>

## Distribuições Priori e Posteriori

Quando fazemos um experimento em que $\theta$ é uma V.A., é interessante chutar uma distribuição para ele antes de observar qualquer dado.

**Definição: Distribuição a priori**

Dado um modelo estatístico com parâmetro $\theta$, se $\theta$ for uma variável aleatória, a distribuição de $\theta$ antes de qualquer dado é chamada de distribuição a priori (Podemos denotar $\xi(\theta)$ ou $f_{\theta}(\theta)$).

Quando estamos trabalhando com observações $X_{1},\ldots,X_{k}$, denotamos a distribuição a priori dos dados como $X_{1},\ldots,X_{k}\vert \theta \sim \text{ Dist}(\theta)$ onde **Dist** representa qualquer distribuição, Ué, como que condicionamos $X_{j}$ em $\theta$? Qual o sentido disso? Imagine que cada experimento é o output de uma máquina industrial, porém, para que essa máquina funcione, alguém precisa passar algumas informações para ela, porém, o seu chefe não mandou você colocar as informações, então você não sabe quais são elas, mas você está vendo os resultados da máquina, e sabe que aqueles resultados só estão acontecendo porque aquela configuração foi colocada, então por mais que não sabemos o $\theta$, ele os valores de $X_{1},\ldots,X_{k}$ só sairam como estamos vendo porque o parâmetro da distribuição é $\theta$ (Que ainda queremos descobrir)

Assim como especificamos uma distribuição para θ antes de qualquer dado ser observado, podemos atualizar a distribuição conforme observamos dados.

**Definição: Função de verossimilhança**

A função de verossimilhança ${\mathbb{L}}(\theta)$ é definida por $${\mathbb{L}}(\theta) = f_{X\vert \theta}\left( x_{1},\ldots,x_{k} \mid \theta \right)$$ De forma que $f_{X\vert \theta}\left( \underline{x}\vert \theta \right)$ é a f.d.p de $X_{1},\ldots,X_{k}$

**Definição: Distribuição a posteriori**

Dado um modelo estatístico com variáveis aleatórias observáveis $X_{1},\ldots,X_{n}$, a distribuição de $X_{1},\ldots,X_{n}\vert \theta$ é chamada de distribuição a posteriori

E agora, com o teorema de bayes, podemos relacionar essas nossas definições

**Teorema: Bayes**

Suponha que $X_{1},\ldots,x_{k}$ são amostras de uma população com distribuição conhecida de parâmetro $\theta$ tal que sua f.d.p é $f_{X\vert \theta}\left( x_{1},\ldots,x_{k}\vert \theta \right)$. Suponha também que $\theta$ é desconhecido e a distribuição a priori de $\theta$ é tal que sua f.d.p é $f_{\theta}(\theta)$, então a posteriori de $\theta$ é tal que: $$f_{\theta}\left( \theta\vert x_{1},\ldots,x_{k} \right) = \frac{f_{X}\left( x_{1},\ldots,x_{k}\vert \theta \right)f_{\theta}(\theta)}{f_{X}\left( x_{1},\ldots,x_{k} \right)}$$ ou $$f_{\theta}\left( \theta\vert x_{1},\ldots,x_{k} \right) = \frac{{\mathbb{L}}(\theta)\xi(\theta)}{\int{\mathbb{L}}(\theta)\xi(\theta)d\theta}$$ Perceba porém, que o termo do denominador não depende de $\theta$, ou seja, podemos reescrever isso tudo como: $$f_{\theta}\left( \theta\vert x_{1},\ldots,x_{k} \right) \propto {\mathbb{L}}(\theta)\xi(\theta)$$

**Demonstração**

Usar teorema de Bayes

Por conta do teorema acima, todos os termos constantes que encontramos em nossa distribuição nós podemos pegar e jogar fora e, ao final, encontramos um termo constante geral, já que para descobrir essa constante $C$ basta fazer: $$\frac{1}{C} = \int_{\vert \Theta\vert }{\mathbb{L}}(\theta)\xi(\theta)d\theta$$<a id="finding-the-constant"></a>

<a id="observacoes-sequenciais-e-predicoes"></a>
<a id="secao-5"></a>

## Observações sequenciais e predições

Porém, perceba que, até agora, eu vi o caso em que eu tenho todas as amostras de uma vez, porém se, por exemplo, eu quero descobrir se uma vacina é eficaz, isso é inviável, faz muito mas sentido eu ir atualizando minha distribuição conforme recebo mais informações, mas será que isso vai dar a mesma coisa?

Vamos fazer com duas observações condicionalmente independentes, para generalizar se faz analogamente. Como vimos, a posteriori de $\theta$ após eu observar o dado $x_{1}$ se dá como: $$f_{\theta}\left( \theta\vert x_{1} \right) \propto f_{X\vert \theta}\left( x_{1}\vert \theta \right)f_{\theta}(\theta)$$

Agora queremos obter $f_{\theta}\left( \theta\vert x_{1},x_{2} \right)$. Pelo teorema de bayes para várias condicionais, temos que: $$f_{\theta}\left( \theta\vert x_{1},x_{2} \right) \propto f_{\theta}\left( \theta\vert x_{1} \right)f_{X}\left( x_{2}\vert x_{1},\theta \right)$$

Porém, estamos assumindo que eles são condicionalmente independentes, ou seja: $$\begin{array}{r} f_{X}\left( x_{2}\vert \theta,x_{1} \right) = f_{X}\left( x_{2}\vert \theta \right) \\ \Rightarrow f_{\theta}\left( \theta\vert x_{1},x_{2} \right) \\ \propto f_{\theta}\left( \theta\vert x_{1} \right)f_{X}\left( x_{2}\vert \theta \right) \\ \propto f_{\theta}(\theta)f_{X\vert \theta}\left( x_{1}\vert \theta \right)f_{X}\left( x_{2}\vert \theta \right) \\ \propto f_{\theta}(\theta)f_{X\vert \theta}\left( x_{1},x_{2}\vert \theta \right) \end{array}$$

Ou seja, independentemente se eu estou recebendo dado após o outro ou se eu tenho todos de uma vez para trabalhar, o resultado final deve ser o mesmo.

Porém, se voltarmos na equação [\[finding-the-constant\]](../distribuicoes-priori-e-posteriori/index.md#finding-the-constant), podemos perceber algo interessante. Lembra da **Lei da Probabilidade Total**? $${\mathbb{P}}(A) = \sum_{i = 1}^{n}{\mathbb{P}}(B_{i}){\mathbb{P}}(A\vert B_{i})$$ Com $B_{i}$ sendo disjuntos. Porém, temos também a versão contínua do teorema: $$f_{X}(x) = \int_{\Omega}f_{X\vert Y}\left( x\vert y \right)f_{Y}(y)dy$$ Porém, se fizermos algumas substituições, nós obtemos: $$f\left( x_{k}\vert x_{1},\ldots,x_{k - 1} \right) = \int_{\vert \Theta\vert }f\left( x_{k}\vert \theta \right)\xi\left( \theta\vert x_{1},\ldots,x_{k - 1} \right)d\theta$$

Ou seja, podemos utilizar essa equação caso tenhamos $n$ observações e estamos interessados em prever o resultado da próxima observação.

<a id="distribuicoes-a-priori-conjugadas"></a>
<a id="secao-6"></a>

## Distribuições à Priori Conjugadas

São famílias de distribuições de tal forma que, quando selecionamos elas como distribuições para um modelo estatístico, a posteriori também será daquela distribuição

**Definição: Famílias/Hiperparâmetros Conjugados**

Seja $X_{1},X_{2},\ldots\vert \theta$ serem **i.i.d** com mesma f.d.p ou f.m.p $f\left( x\vert \theta \right)$. Seja $\Psi$ uma família de distribuições no espaço paramétrico $\Theta$. Suponha que, não importa qual seja a distribuição à priori $\xi$ que eu escolher de $\Psi$, não importa quantas observações $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ nós registramos e não importa seus valores observados $\underline{x} = \left( x_{1},\ldots,x_{n} \right)$, a distribuição à posteriori $\xi(\theta\vert \underline{x})$ está em $\Psi$. Então $\Psi$ é chamada de uma **família de distribuições à priori conjugadas** para amostras de com distribuições $f\left( x\vert \theta \right)$. Finalmente, se as distribuições em $\Psi$ possuem parâmetros associados, estes são chamados de **hiperparâmetros à priori** e os associados à distribuição posteriori são **hiperparâmetros à posteriori**

Vamos ver as principais famílias de distribuições conjugadas

**Teorema**

Suponha que $X_{1},\ldots,X_{n}\vert \theta$ são uma amostra aleatória de variáveis de Bernoulli com parâmetro $\theta$ (Desconhecido). Suponha também que a distribuição a priori de $\theta$ é uma **beta** com parâmetros $\alpha > 0$ e $\beta > 0$. Então a distribuição a posteriori de $\theta\vert x_{1},\ldots,x_{n}$ é a distribuição beta com parâmetros $\alpha + \sum_{i = 1}^{n}x_{i}$ e $\beta + n - \sum_{i = 1}^{n}x_{i}$

**Demonstração**

$$f\left( \theta\vert x_{1},\ldots,x_{n} \right) \propto \xi(\theta)f\left( x_{1},\ldots,x_{n}\vert \theta \right)$$ $$\Leftrightarrow f\left( \theta\vert x_{1},\ldots,x_{n} \right) \propto \theta^{\alpha - 1}(1 - \theta)^{\beta - 1}\prod_{i = 1}^{n}\theta^{x_{i}}(1 - \theta)^{1 - x_{i}}$$ $$\Leftrightarrow f\left( \theta\vert x_{1},\ldots,x_{n} \right) \propto \theta^{\alpha - 1 + \sum_{i = 1}^{n}x_{i}}(1 - \theta)^{\beta - 1 + n - \sum_{i = 1}^{n}x_{i}}$$ Ou seja, $\theta\vert x_{1},\ldots,x_{n} \sim \text{ Beta}\left( \alpha + \sum_{i = 1}^{n}x_{i},\ \beta + n - \sum_{i = 1}^{n}x_{i} \right)$

**Teorema**

Suponha que $X_{1},\ldots,X_{n}\vert \theta$ são uma amostra aleatória de variáveis com distribuição Poisson com parâmetro $\theta$ (Desconhecido). Suponha também que a distribuição a priori de $\theta$ é uma **Gamma** com parâmetros $\alpha > 0$ e $\beta > 0$. Então a distribuição a posteriori de $\theta\vert x_{1},\ldots,x_{n}$ é a distribuição Gamma com parâmetros $\alpha + \sum_{i = 1}^{n}x_{i}$ e $\beta + n$

**Demonstração**

Seja $y = \sum_{i = 1}^{n}x_{i}$, então a função de verossimilhança de ${\mathbb{L}}(\theta)$ satisfaz: $${\mathbb{P}}(\underline{x}\vert \theta) \propto e^{- n\theta}\theta^{y}$$ A priori $\xi(\theta)$ se estrutura assim: $$\xi(\theta) \propto \theta^{\alpha - 1}e^{- \beta\theta}\text{ para }\theta > 0$$ Temos então que: $$\begin{array}{r} f\left( \theta\vert \underline{x} \right) \propto e^{- n\theta}\theta^{y}\theta^{\alpha - 1}e^{- \beta\theta} \\ \Leftrightarrow f\left( \theta\vert \underline{x} \right) \propto \theta^{\alpha + y - 1}e^{- (n + \beta)\theta} \end{array}$$ Ou seja, $\theta\vert \underline{x} \sim \text{ Gamma}(\alpha + y,n + \beta)$

**Teorema**

Suponha que $X_{1},\ldots,X_{n}\vert \theta$ são uma amostra aleatória de variáveis com distribuição Normal com média $\theta$ (Desconhecido) e variância $\sigma^{2} > 0$ conhecido. Suponha também que a distribuição a priori de $\theta$ é uma **Normal** com média $\mu_{0}$ e variância $v_{0}^{2}$. Então a distribuição a posteriori de $\theta\vert x_{1},\ldots,x_{n}$ é a distribuição normal com média $\mu_{1}$ e variância $v_{1}^{2}$ onde: $$\mu_{1} = \frac{\sigma^{2}\mu_{0} + nv_{0}^{2}{\widetilde{x}}_{n}}{\sigma^{2} + nv_{0}^{2}}$$<a id="normal-posterior-mu1"></a> e $$v_{1}^{2} = \frac{\sigma^{2}v_{0}^{2}}{\sigma^{2} + nv_{0}^{2}}$$<a id="normal-posterior-v0-squared"></a>

**Demonstração**

Temos que: $${\mathbb{L}}(\theta) \propto \exp( - \frac{1}{2\sigma^{2}}\sum_{i = 1}^{n}\left( x_{i} - \theta \right)^{2})$$ Temos que: $$\sum_{i = 1}^{n}\left( x_{i} - \theta \right)^{2} = \sum_{i = 1}^{n}x_{i}^{2} - 2x_{i}\theta + \theta^{2}$$ Definimos então ${\widetilde{x}}_{n} ≔ \frac{1}{n}\sum_{i = 1}^{n}x_{i}$ e assim temos que: $$\begin{array}{r} \sum_{i = 1}^{n}x_{i}^{2} - 2x_{i}\theta + \theta^{2} = n\theta^{2} - 2n{\widetilde{x}}_{n}\theta + \sum_{i = 1}^{n}x_{i}^{2} \\ = n\left( \theta^{2} - 2\theta{\widetilde{x}}_{n} \right) + \sum_{i = 1}^{n}x_{i}^{2} = n\left( \theta^{2} - 2\theta{\widetilde{x}}_{n} + {\widetilde{x}}_{n}^{2} \right) - n{\widetilde{x}}_{n} + \sum_{i = 1}^{n}x_{i}^{2} \\ = {n\left( \theta - {\widetilde{x}}_{n} \right)}^{2} + \sum_{i = 1}^{n}\left( x_{i} - {\widetilde{x}}_{n} \right)^{2} \end{array}$$

Temos então: $$\begin{array}{r} {\mathbb{L}}(\theta) \propto \exp( - \frac{1}{2\sigma^{2}}\sum_{i = 1}^{n}\left( x_{i} - \theta \right)^{2}) \\ \Leftrightarrow {\mathbb{L}}(\theta) \propto \exp( - \frac{1}{2\sigma^{2}}\left( {n\left( \theta - {\widetilde{x}}_{n} \right)}^{2} + \sum_{i = 1}^{n}\left( x_{i} - {\widetilde{x}}_{n} \right)^{2} \right)) \end{array}$$ Temos que $\sum_{i = 1}^{n}\left( x_{i} - {\widetilde{x}}_{n} \right)^{2}$ não depende de $\theta$ então pode ir para a constante de proporcionalidade. De forma que $${\mathbb{L}}(\theta) \propto \exp( - \frac{n}{2\sigma^{2}}\left( \theta - {\widetilde{x}}_{n} \right)^{2})$$ Sabemos que a priori de $\theta$ segue a forma: $$\xi(\theta) \propto \exp( - \frac{1}{2v_{0}^{2}}\left( \theta - \mu_{0} \right)^{2})$$ Então temos que $$f\left( \theta\vert \underline{x} \right) \propto \exp\left\{ - \frac{1}{2}\left\lbrack \frac{n}{\sigma^{2}}\left( \theta - {\widetilde{x}}_{n} \right)^{2} + \frac{1}{v_{0}^{2}}\left( \theta - \mu_{0} \right)^{2} \right\rbrack \right\}$$ Se abrirmos os termos em quadrado, retirar as constantes, e completar os quadrados, chegamos nos resultados das equações [\[normal-posterior-mu1\]](#normal-posterior-mu1) e [\[normal-posterior-v0-squared\]](#normal-posterior-v0-squared), de forma que: $$f\left( \theta\vert \underline{x} \right) \propto \exp\left\lbrack - \frac{1}{2v_{1}^{2}}\left( \theta - \mu_{1} \right)^{2} \right\rbrack$$ Ou seja, $f\left( \theta\vert \underline{x} \right) \sim N\left( \mu_{1},v_{1}^{2} \right)$

Conseguimos dividir $\mu_{1}$ da seguinte forma: $$\mu_{1} = \frac{\sigma^{2}}{\sigma^{2} + nv_{0}^{2}}\mu_{0} + \frac{nv_{0}^{2}}{\sigma^{2} + nv_{0}^{2}}{\widetilde{x}}_{n}$$ Isso nos mostra que, conforme nossa amostra vai aumentando, o termo da direita referente à média amostral vai dominando. Mas o que isso quer dizer? Quer dizer que, independente do quanto você acredita que $\mu_{0}$ seja a média verdadeira de $\theta$, mais a média após a observação dos dados vai se aproximando de ${\widetilde{x}}_{n}$, de forma que acabamos mudando de ideia aos poucos

**Teorema**

Suponha que $X_{1},\ldots,X_{n}\vert \theta$ são uma amostra aleatória de variáveis com distribuição Exponencial com parâmetro $\theta > 0$ (Desconhecido). Suponha também que a distribuição a priori de $\theta$ é uma **Gamma** com parâmetros $\alpha > 0$ e $\beta > 0$. Então a distribuição a posteriori de $\theta\vert x_{1},\ldots,x_{n}$ é a distribuição Gamma com parâmetros $\alpha + n$ e $\beta + \sum_{i = 1}^{n}x_{i}$

**Demonstração**

Novamente vamos chamar $y ≔ \sum_{i = 1}^{n}x_{i}$. Então temos que a função de verossimilhança é: $${\mathbb{L}}(\theta) = \theta^{n}e^{- \theta y}$$ E a priori tem a forma: $$\xi(\theta) \propto \theta^{\alpha - 1}e^{- \beta\theta}\text{ para }\theta > 1$$ Então temos que: $$\begin{array}{r} f\left( \theta\vert \underline{x} \right) \propto \theta^{\alpha - 1}e^{- \beta\theta}\theta^{n}e^{- \theta y} \\ \Leftrightarrow f\left( \theta\vert \underline{x} \right) \propto \theta^{n + \alpha - 1}e^{- (\beta + y)\theta} \end{array}$$ Ou seja, $f\left( \theta\vert \underline{x} \right) \sim \text{ Gamma}(n + \alpha,\ \beta + y)$

<a id="distribuicoes-improprias"></a>
<a id="secao-7"></a>

## Distribuições Impróprias

**Definição: Distribuição Imprópria**

Seja $\xi:C \rightarrow {\mathbb{R}}$ uma função não-negativa cujo domínio inclui o espaço paramétrico ($\Omega \subset C$) de um modelo estatístico. Suponha também que: $$\int_{C}\xi(\theta)d\theta = \infty$$ Se nós imaginarmos que $\xi$ é a f.d.p à priori de $\theta$, então $\xi$ é uma **distribuição imprória** de $\theta$

Um bom exemplo é utilizar a distribuição **beta** assumindo que $\alpha = \beta = 0$. Mesmo que isso viole a condição da distribuição beta, o resultado da posteriori ainda sim é uma distribuição beta. Porém, existem diversos métodos para se escolher uma distribuição imprópria para $\theta$. O mais comum é se utilizar de uma família de conjugados para o modelo estatístico, e forma a adaptarmos seus parâmetros para obter uma distribuição imprópria.

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Conteúdos relacionados

- [Regressão Logística Bayesiana — Aprendizado de Máquina](../aprendizado-de-maquina/regressao-logistica.md#regressao-logistica-bayesiana)


## Percurso de estudo

[Trilha: A1](../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Definições](definicoes.md)
- Próximo: [Estimadores de Bayes](estimadores-de-bayes.md)
