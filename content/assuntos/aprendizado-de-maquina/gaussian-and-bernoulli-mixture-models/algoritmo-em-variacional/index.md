---
layout: "default"
title: "Algoritmo EM Variacional — Gaussian and Bernoulli Mixture Models"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 13
---

[Aprendizado de Máquina](../../index.md) · [Gaussian and Bernoulli Mixture Models](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-13"></a>

# Algoritmo EM Variacional

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

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Expectation-Maximization (EM) para GMMs](../expectation-maximization-em-para-gmms/index.md)
- Próximo: [Bernoulli Mixture Models](../bernoulli-mixture-models/index.md)
