---
layout: "default"
title: "GPs para classificação — Processos Gaussianos"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 12
---

[Aprendizado de Máquina](../../index.md) · [Processos Gaussianos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# GPs para classificação

Para classificações, vamos reformular como as saídas se comportam. Dessa vez, assumimos que $$y_{i}~\vert ~f_{i},x_{i} \sim \text{ Bernoulli}\left( \sigma(f_{i}\left( x_{i} \right)) \right)$$ para simplificar notação, vou definir $\sigma_{i} = \sigma(f_{i}\left( x_{i} \right))$. Nós vamos aproximar $p\left( y\vert f,X \right)$ usando a aproximação de Laplace ou métodos de amostragem e depois achar a preditiva posteriori $p\left( y^{\ast}\vert X,y,x^{\ast} \right)$. Primeiro vamos achar a forma da verossimilhança $$p\left( y_{n}\vert f_{n},x_{n} \right) = \sigma_{n}^{y_{n}}\left( 1 - \sigma_{n} \right)^{1 - y_{n}} \Rightarrow p\left( y\vert f,X \right) = \prod_{n = 1}^{N}\sigma_{n}^{y_{n}}\left( 1 - \sigma_{n} \right)^{1 - y_{n}}$$ agora, vamos escrever a posteriori de $f$ dado $X$ e $y$ usando Bayes: $$p\left( f\vert X,y \right) \propto p\left( y\vert f,X \right)p\left( f\vert X \right)$$ escrevendo em forma de $\log$ para facilitar as contas $$\begin{aligned} \ln p\left( f\vert X,y \right) & = \ln p\left( y\vert f,X \right) + \ln p\left( f\vert X \right) + C \\ & = \sum_{n = 1}^{N}\left\{ y_{n}\ln\sigma_{n} + \left( 1 - y_{n} \right)\ln\left( 1 - \sigma_{n} \right) \right\} - \frac{1}{2}{f(x)}^{T}K^{- 1}f(x) + C \end{aligned}$$

Agora podemos derivar para conseguir achar a moda $m$ $$\begin{array}{r} \frac{\partial}{\partial f_{n}}\ln p\left( f\vert X,y \right) = y_{n}\left( 1 - \sigma_{n} \right) - \left( 1 - y_{n} \right)\sigma_{n} - \left( K^{- 1}f(x) \right)_{n} = 0 \\ \Rightarrow \nabla\ln p\left( f\vert X,y \right) = y - \sigma(f(x)) - K^{- 1}f(x) = 0 \end{array}$$

essa equação não tem solução analítica, então utilizamos de métodos numéricos para achar a moda $m$ que satisfaz $$y - \sigma(m) - K^{- 1}m = 0$$

Agora, para continuar com a aproximação de Laplace, precisamos achar a matriz Hessiana da posteriori de $f$ dado $X$ e $y$. A matriz Hessiana é dada por $$H = \nabla^{2}\ln p\left( f\vert X,y \right) = - W - K^{- 1}$$ onde $W$ é uma matriz diagonal com entradas $W_{nn} = \sigma_{n}\left( 1 - \sigma_{n} \right)$. A aproximação de Laplace nos diz que a posteriori de $f$ dado $X$ e $y$ pode ser aproximada por uma Gaussiana centrada na moda $m$ com covariância $\Sigma = - H^{- 1} = \left( K^{- 1} + W \right)^{- 1}$. Sabendo que $p\left( f\vert X,y \right) \approx \mathcal{N}(m,\Sigma)$, temos que: $$p\left( y^{\ast}\vert X,y,x^{\ast} \right) = \int\underset{\mathcal{N}(f^{\ast}\left( x^{\ast} \right),\sigma^{2})}{\underbrace{p\left( y^{\ast}\vert f^{\ast} \right)}}\underset{\mathcal{N}(m',\Sigma')}{\underbrace{p\left( f^{\ast}\vert X,y,x^{\ast} \right)}}df^{\ast}$$ $m'$ e $\Sigma'$ representam as mesmas contas que fizemos antes, porém adicionando o ponto $x^{\ast}$ no conjunto de dados. A integral acima não tem solução analítica, então podemos utilizar métodos de amostragem para aproximar a integral.

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [GPs para regressão](../gps-para-regressao/index.md)
- Próximo: [Graph Neural Networks](../../graph-neural-networks/index.md)
