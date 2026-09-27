---
layout: "default"
title: "Estatística Frequentista"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 13
---

[Inferência Estatística](index.md)

<!-- wiki:original:inicio -->

<a id="secao-13"></a>

# Estatística Frequentista


<a id="estimadores-estimacoes-de-maxima-verossimilhanca"></a>
<a id="secao-14"></a>

## Estimadores/Estimações de Máxima Verossimilhança

Já que estamos trabalhando com um valor fixo, sem distribuições nem nada do gênero, os métodos que vimos para a estimação de parâmetros não vai funcionar. Porém, tem algum método para que eu consiga fazer essa estimação sem ter uma distribuição priori/posteriori? **SIM**. Vamos pensar de uma maneira **intuitiva**, o que vou falar aqui é apenas uma aproximação intuitiva de como funciona o método, mas depois eu vou explicar o porquê de não ser exatamente o que estou dizendo

Quando jogamos uma moeda, e observamos uma proporção de **caras** de $1/20$, por exemplo, obviamente pensamos: “Essa moeda ta muito viciada”. E então pensamos que a probabilidade de cair cara seja de **aproximadamente** $1/20$. Essa intuição que temos é isso (Não exatamente) o que o método da **Estimação por Máxima Verossimilhança** faz

**Definição: Estimadores/Estimação de Máxima Verossimilhança**

Seja $f\left( \underline{X}\vert \theta \right)$ a p.f ou a p.d.f de $X_{1},\ldots,X_{n}\vert \theta$ e $\theta \in \Omega \subset {\mathbb{R}}^{m}$, a função $\delta(\underline{X}) = \max\limits_{\theta}f\left( \underline{X}\vert \theta \right)$ é chamada de **Estimador de Máxima Verossimilhança**. Quando os valores $\underline{x} = \left( x_{1},\ldots,x_{n} \right)$ são observados, então $\delta(\underline{x}) = \max\limits_{\theta}f\left( \underline{x}\vert \theta \right)$ é chamado de **Estimativa de Máxima Verossimilhança**

Essa definição parece ser bem intuitiva, correto? Vamos ver um exemplo:

**Exemplo**

Suponha que você tem $n$ variáveis de tal forma que: $$X_{1},\ldots,X_{n}~\vert ~\theta \sim \text{ Bern}(\theta)$$ De forma que $\theta$ é desconhecido. Para todos os valores $x_{1},\ldots,x_{n}$ observados, temos que a p.m.f conjunta é: $$f\left( \underline{x}\vert \theta \right) = \prod_{i = 1}^{n}\theta^{x_{i}}(1 - \theta)^{1 - x_{i}}$$ Em vez de maximizar esse troço, vamos maximizar o $\log$ dele, já que, como ela é crescente, o máximo do $\log$ também é o máximo da função em si. Tirando o log, temos: $$\begin{aligned} \ln(f\left( \underline{x}\vert \theta \right)) & = \sum_{i = 1}^{n}x_{i}\ln(\theta) + \left( 1 - x_{i} \right)\ln(1 - \theta) \\ & = \left( \sum_{i = 1}^{n}x_{i} \right)\ln(\theta) + \left( n - \sum_{i = 1}^{n}x_{i} \right)\ln(1 - \theta) \end{aligned}$$ Derivando isso em relação a $\theta$ e igualando a $0$, vamos ter que: $$\begin{aligned} 0 & = \left( \sum_{i = 1}^{n}x_{i} \right)\frac{1}{\theta} - \left( n - \sum_{i = 1}^{n}x_{i} \right)\frac{1}{1 - \theta} \\ 0 & = \left( n{\overset{-}{x}}_{n} \right)\frac{1}{\theta} - n\left( 1 - {\overset{-}{x}}_{n} \right)\frac{1}{1 - \theta} \\ 0 & = \frac{{\overset{-}{x}}_{n}}{\theta} - \frac{1 - {\overset{-}{x}}_{n}}{1 - \theta} \end{aligned}$$ $$\begin{aligned} 0 & = (1 - \theta){\overset{-}{x}}_{n} - \left( 1 - {\overset{-}{x}}_{n} \right)\theta \\ 0 & = {\overset{-}{x}}_{n} - \theta{\overset{-}{x}}_{n} - \theta + \theta{\overset{-}{x}}_{n} \\ \theta & = {\overset{-}{x}}_{n} \end{aligned}$$

Ou seja, chegamos a uma conclusão razoável que o estimador que minimiza a verossimilhança é a média das variáveis de Bernoulli

Porém, nem sempre essa abordagem é viável, vamos ver um exemplo:

**Exemplo**

Suponha que temos uma amostra $X_{1},\ldots,X_{n}\vert \theta \sim \text{ Unif}\lbrack 0,\theta\rbrack$, de forma que a distribuição é levemente alterada para ser da forma: $$f\left( x\vert \theta \right) = \begin{cases} \frac{1}{\theta}\text{ para }0 < x < \theta \\ 0\text{ caso contrário } \end{cases}$$ Temos então que a máxima verossimilhança é: $$f\left( \underline{x}\vert \theta \right) = \begin{cases} \frac{1}{\theta^{n}}\text{ para }0 < x_{i} < \theta\ (i = 1,\ldots,n) \\ 0\text{ caso contrário } \end{cases}$$ Como $1/\theta^{n}$ é uma função decrescente, o valor de $\theta$ que maximiza a função e ainda se encaixa na restrição $\theta > \max\left\{ x_{1},\ldots,x_{n} \right\}$ seria $\theta = \max\left\{ x_{1},\ldots,x_{n} \right\}$, porém, não podemos usar esse valor por conta da desigualdade **estrita** na função de verossimilhança. O que isso quer dizer? Que esse caso **não possui um Estimador de Máxima Verossimilhança**

O livro também aborda outros casos em que um mesmo caso pode ter **vários** estimadores ou casos em que um estimador, mesmo existindo, não demonstra ser um valor interessante/desejado.

Mas eu falei antes que esses estimadores formalizavam a ideia de “O parâmetro $\theta$ parece ser esse daqui”, mas não é bem assim que funciona. A gente viu que ele é o parâmetro que **maximiza** a probabilidade daquela observação ocorrer. E qual é a diferença disso pro que falei antes? Simples, quando vemos os valores de observações, o fato de eles aparecerem daquela forma, não significa que o valor que $\theta$ mais aparenta ser seja o real. Ué, como assim? Muitos fatores podem estar envolvidos, fatores que, logo de cara, não conseguimos observar apenas nos dados. Para que isso ocorresse, os dados deveriam conter muito mais informação do que tinhamos à priori (Antes das observações)

<a id="propriedades"></a>
<a id="secao-15"></a>

## Propriedades

**Teorema**

Se $\hat{\theta} \in \Omega$ é o Estimador de Máxima Verossimilhança (EMV) de $\theta$ e $g$ é uma função bijetiva, então $g\left( \hat{\theta} \right)$ é o EMV de $g(\theta)$

**Demonstração**

Seja $\Gamma$ o novo espaço paramétrico, ou seja, $g:\Omega \rightarrow \Gamma$. Vamos definir $h$ como sendo a função inversa, ou seja $\theta = h(\psi)$. Se expressarmos a p.d.f em função de $\psi$, vamos obter $f\left( x\vert h(\psi) \right)$ e a função de verossimilhança será $f\left( \underline{x}\vert h(\psi) \right)$.

Sabemos que o EMV $\hat{\psi}$ de $\psi$ é vai ser o valor de $\psi$ que maximiza $f\left( \underline{x}\vert h(x) \right)$. Como $f\left( x\vert \theta \right)$ é maximizada quando $\theta = \hat{\theta}$, então $h(\psi) = \hat{\theta}$ maximiza a verossimilhança. Porém, aplicando $g$ em ambos os lados, obtemos que: $$\hat{\psi} = g\left( \hat{\theta} \right)$$

Essa propriedade é algo ótimo! Tendo em vista que no método anterior, o [estimador de Bayes](estimadores-de-bayes.md#secao-11) de $1/\theta$ podia ser diferente de $1/\hat{\theta}$. Porém, podemos estender esse teorema para casos em que a função $g$ não é bijetiva. Vamos então definir o **estimador de uma função**

**Definição: MVE de uma Função**

Seja $g(\theta)$ uma função arbitrária do parâmetro com $g:\Omega \rightarrow G$. Para cada $t \in G$, defina $G_{t} ≔ \left\{ \theta:g(\theta) = t \right\}$ e $L^{\ast \left( \hat{t} \right)} ≔ \max\limits_{\theta \in G_{t}}\log f\left( \underline{x}\vert \theta \right)$, defina então o EMV de $g(\theta)$ como $\hat{t}$ como: $$L^{\ast \left( \hat{t} \right)} = \max\limits_{t \in G_{t}}L^{\ast (t)}$$

**Teorema**

Dado $\hat{\theta}$ sendo o EMV de $\theta$ e $g:\Omega \rightarrow G$, então: $$\hat{g(\theta)} = g\left( \hat{\theta} \right)$$

**Demonstração**

Como $L^{\ast (t)}$ é o máximo de $\log f\left( \underline{x}\vert \theta \right)$ em $\theta$ num subconjunto de $\Omega$, e como $\log f\left( \underline{x}\vert \hat{\theta} \right)$ é o máximo sob todos os $\theta$, então sabemos que $L^{\ast (t)} \leq \log f\left( \underline{x}\vert \theta \right)\ \forall t \in G$. Denote $\hat{t} = g\left( \hat{\theta} \right)$. Perceba que $\hat{\theta} \in G_{\hat{t}}$. Como $\hat{\theta}$ maximiza $f\left( \underline{x}\vert \theta \right)$ em todos $\theta$, então ele também maximiza $f\left( \underline{x}\vert \theta \right)$ sob todos os $\theta \in G_{\hat{t}}$. Por isso, $L^{\ast \left( \hat{t} \right)} = \log f\left( \underline{x}\vert \hat{\theta} \right)$ e $\hat{t} = g\left( \hat{\theta} \right)$ é um EVM de $g(\theta)$

<a id="computacao-numerica"></a>
<a id="secao-16"></a>

## Computação Numérica

Muitos problemas possuem um EVM $\hat{\theta}$ de um parâmetro $\theta$, porém esses não podem ser computados com fórmulas fechadas. Nesses casos, precisamos utilizar de métodos numéricos para aproximações. Existem **inúmeros** métodos de aproximação numérica de funções, porém, aqui vamos abordar brevemente apenas um

**Definição: [Método de Newton](../otimizacao-para-ciencia-de-dados/metodo-de-newton.md)**

Seja $f(\theta)$ uma função real de uma variável e suponha que nós desejamos resolver a equação $f(\theta) = 0$. Seja $\theta_{0}$ um chute inicial da solução e $\theta_{t}$ o valor obtido na $t$-ésima iteração do programa. O método de Newton atualiza nossa resposta da seguinte forma: $$\theta_{t + 1} = \theta_{t} - \frac{f\left( \theta_{t} \right)}{f'\left( \theta_{t} \right)}$$

Se pararmos para interpretar, o que o algoritmo faz é checar se eu tenho que mexer $\theta_{t}$ para frente ou para trás dependendo do sinal e da inclinação de $f$. Quando $f\left( \theta_{t} \right)$ é negativo e $f'\left( \theta_{t} \right)$ é positivo, então eu preciso mover para a direita para poder chegar próximo a raíz, e aí vai

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Estimadores de Bayes](estimadores-de-bayes.md)
- Próximo: [Método dos Momentos](metodo-dos-momentos.md)
