---
layout: "default"
title: "Deep Learning (DL) — Modelagem Clássica aplicada ao Tempo"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 11
---

[Séries Temporais](../../index.md) · [Modelagem Clássica aplicada ao Tempo](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Deep Learning (DL)

Em deep learning, expressamos a relação entre $y_{t}$ e suas covariáveis através de uma função complexa $f$ $$y_{t} = f\left( x_{1t},\ldots,x_{pt} \right) + \varepsilon_{t}$$ onde $f$ é uma função altamente flexível modelada por uma rede neural, capazes de capturar padrões complexos e não-lineares dos dados

<a id="secao-16"></a>

## Janelas, Batches e Seta do Tempo

As redes neurais, durante seu treinamento, assumem uma hipótese que muitas vezes esquecemos, mas que são MUITO importantes no nosso contexto. Os dados **podem ser trocados**, eu posso embaralhar minhas amostras **sem perca de informação**. No entanto, o conceito de séries temporais não permite essa premissa, o que podemos fazer para mitigar isso? É aí que entram as **janelas**, onde empacotamos o passado e a dependência temporal entre elas. Por exemplo, imagine que temos a seguinte sequência: $$\left\{ 10,12,9,14,11,13,8,15... \right\}$$ para podermos alimentar essas informações em uma rede neural, vamos criar uma janela de tamanho $3$ e gerar nossos conjuntos de dados e alvo $$\begin{array}{r} \ Janela\ 1\  \rightarrow \left\{ 10,12,9 \right\} \rightarrow 14 \\ Janela\ 2\  \rightarrow \left\{ 11,13,8 \right\} \rightarrow 15 \end{array}$$

perceba que eu sempre pego um conjunto de $3$ valores e digo que o valor resultante (alvo) deve ser o seguinte e assim por diante. Dessa forma, a ordem **entre janelas** passa a ser irrelevante pois a informação de passado e como ele influencia na resposta está incorporada na própria janela. No entanto, vale ressaltar que a ordem **dentro da janela** é **sagrada** e **nunca deve ser alterada**, do contrário a informação temporal entre amostras **se perde**

Como nem tudo são flores, existem alguns pontos de atenção que devemos tomar cuidado. O primeiro é quando formos separar nossos dados nos conjuntos de **treino** e **teste**. Não podemos, ao realizar a divisão, criar janelas com dados em conjuntos diferentes. Por exemplo, se temos a seguinte série, e fazemos a seguinte separação: $$\left\{ \underset{\text{ TREINO}}{\underbrace{10,\ 12,\ 9,\ 14,\ 11}},\underset{\text{ TESTE}}{\underbrace{13,\ 8,\ 15}}\ldots \right\}$$ em hipótese alguma podemos, dentro das nossas janelas de treino, ter uma janela tipo $\left\{ 14,11,13 \right\}$, pois estariamos misturando pontos de treino e teste, de forma que nosso modelo estaria vendo o futuro fora do controlado

Além disso, devemos tomar cuidado com **janelas sobrepostas**. Como falei antes, criamos as janelas para que elas possam ser independentes, no entanto, é possível criar janelas que não são independentes (ainda podemos embaralhar elas como artimanha computacional). Por exemplo, dado a série: $$\left\{ 10,12,9,14,11,13,8,15,\ldots \right\}$$ as janelas $\left\{ 10,12,9 \right\}$ e $\left\{ 12,9,14 \right\}$ se sobrepõe, de tal forma que elas NÃO são independentes pois contém a mesma parcela do passado e como ela influencia nos valores internos. O ponto é que, para um SGD, você **pode** embaralhar essas janelas, mas isso não lhe permite tratá-las como **independentes**

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Generalized Additive Models (GAM)](../generalized-additive-models-gam/index.md)
- Próximo: [Diagnóstico Visual](../../diagnostico-visual/index.md)
