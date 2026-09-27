---
layout: "default"
title: "Distribuições à Priori Conjugadas — Estatística Bayesiana"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 6
---

[Inferência Estatística](../../index.md) · [Estatística Bayesiana](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-6"></a>

# Distribuições à Priori Conjugadas

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

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Observações sequenciais e predições](../observacoes-sequenciais-e-predicoes/index.md)
- Próximo: [Distribuições Impróprias](../distribuicoes-improprias/index.md)
