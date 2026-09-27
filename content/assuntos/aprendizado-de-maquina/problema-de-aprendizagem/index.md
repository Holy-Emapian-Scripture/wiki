---
layout: "default"
title: "Problema de Aprendizagem"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 1
---

[Aprendizado de Máquina](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-1"></a>

# Problema de Aprendizagem


<a id="dilema-vies-variancia"></a>
<a id="secao-3"></a>

## Dilema viés-variância

De maneira geral, aprendemos $h$ usando o conjunto de treino $D$ com $N$ amostras (i.e., $\vert D\vert  = N$), mas queremos que $h$ apresente boa performance em novas observações de $x \sim {\mathbb{P}}_{x}$. Em outras palavras, gostaríamos de um modelo que minimiza uma função de perda $\mathcal{l}$ média ${\mathbb{E}}_{x}\left\lbrack \mathcal{l}(h(x),f(x)) \right\rbrack$. Esse valor é comumente chamado de erro de generalização.

Para a seguinte discussão, assuma que $\mathcal{l}$ é o erro quadrático — i.e., $\mathcal{l}(y,\hat{y}) = \left( y - \hat{y} \right)^{2}$. Portanto o erro de generalização é dado por ${\mathbb{E}}_{x}\left\lbrack \left( h(x) - f(x) - \varepsilon \right)^{2} \right\rbrack$ ($\varepsilon$ é um ruído de **média $0$**). Como $h$ é o resultado de um processo de aprendizado, ele depende diretamente dos exemplos em $D$. Por exemplo, se estamos fazendo regressão linear, $h$ pode ser obtida aplicando via máxima verossimilhança. No entanto, podemos analisar $h$ de maneira mais geral, sem se prender aos valores específicos em $D$. Para tal, calculamos o valor esperado do erro tratando $D$ como uma variável aleatória. Isto é, calculamos uma média ponderada sobre todos os possíveis bancos de dado de tamanho $N$ — com pesos dados por ${\mathbb{P}}_{x,y}$. Usando a linearidade do operador de esperança e a independência de $D$ e $x$, segue que: $$\begin{aligned} {\mathbb{E}}_{x,D,\varepsilon}\left\lbrack \left( h_{D}(x) - f(x) - \varepsilon \right)^{2} \right\rbrack & = {\mathbb{E}}_{x}\left\lbrack {\mathbb{E}}_{D,\varepsilon}\left\lbrack \left( h_{D(x)} - f(x) - \varepsilon \right)^{2} \right\rbrack \right\rbrack \\ & = {\mathbb{E}}_{x}\left\lbrack {\mathbb{E}}_{D}\left\lbrack \left( h_{D}(x) - f(x) \right)^{2} \right\rbrack + {\mathbb{E}}_{\varepsilon}\left\lbrack \varepsilon^{2} \right\rbrack \right\rbrack \\ & = {\mathbb{E}}_{x}\left\lbrack {\mathbb{V}}_{D}\left\lbrack h_{D}(x) \right\rbrack \right\rbrack + {\mathbb{E}}_{x}\left\lbrack \left( {\mathbb{E}}_{D}\left\lbrack h_{D}(x) \right\rbrack - f(x) \right)^{2} \right\rbrack + {\mathbb{E}}_{\varepsilon}\left\lbrack \varepsilon^{2} \right\rbrack \end{aligned}$$

Como isso muda nossa vida? Na maioria das aplicações, temos pouca informação sobre $f$. Nesse caso, nosso primeiro instinto talvez fosse escolher um método capaz de gerar aproximações arbitrariamente intrincadas. No entanto, métodos mais flexíveis costumam estar associados à uma maior variância no processo de aprendizado, o que influencia negativamente a performance esperada para novos dados de entrada. Por outro lado, métodos simples como regressão linear possuem baixa variância, mas podem apresentar alto viés caso f não possa ser bem aproximada por um (hiper-)plano. Em suma, não existe uma bala de prata. Precisamos de protocolos empíricos bem definidos para escolher o método mais adequado para cada situação.

------------------------------------------------------------------------

<a id="introducao"></a>
<a id="secao-2"></a>

## Introdução

Em aprendizado supervisionado, o objetivo principal é criar uma aproximação $h:\mathcal{X} \rightarrow \mathcal{Y}$ para uma função $f:\mathcal{X} \rightarrow \mathcal{Y}$ a partir de amostras $D = \left\{ \left( x_{n},y_{n} \right) \right\}_{n = 1}^{N}$, onde cada exemplo de treinamento é uma amostra independente proveniente de ${\mathbb{P}}_{x,y}$ e $y_{n}$ é uma observação (possivelmente ruidosa) de $f\left( x_{n} \right)$. No caso de regressão, poderíamos usar vários métodos distintos para construir $h$. Alguns exemplos que já vimos são $k$-NN, regressão linear e redes neurais RBF. Além disso, podemos alterar drasticamente o comportamento desses modelos alterando hiper-parâmetros. Isso nos leva às duas perguntas estruturantes desse capítulo:

1.  Qual é a melhor classe de modelos (e.g., regressão linear, rede RBF) para cada problema?

2.  Como escolher escolher os melhores híper-parâmetros para cada classe de modelos?

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Próximo: [Dilema viés-variância](#dilema-vies-variancia)
