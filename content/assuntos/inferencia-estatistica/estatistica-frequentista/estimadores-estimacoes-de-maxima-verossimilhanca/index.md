---
layout: "default"
title: "Estimadores/Estimações de Máxima Verossimilhança — Estatística Frequentista"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 14
---

[Inferência Estatística](../../index.md) · [Estatística Frequentista](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-14"></a>

# Estimadores/Estimações de Máxima Verossimilhança

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

<!-- wiki:original:fim -->

## Conteúdos relacionados

- [Máxima Verossimilhança — Aprendizado de Máquina](../../../aprendizado-de-maquina/gaussian-and-bernoulli-mixture-models/maxima-verossimilhanca/index.md)

## Percurso de estudo

[Trilha: A1](../../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Estatística Frequentista](../index.md)
- Próximo: [Propriedades](../propriedades/index.md)
