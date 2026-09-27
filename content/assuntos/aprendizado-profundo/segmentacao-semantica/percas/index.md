---
layout: "default"
title: "Percas — Segmentação Semântica"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 18
---

[Aprendizado Profundo](../../index.md) · [Segmentação Semântica](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-24"></a>

# Percas


<a id="balanced-cross-entropy-loss"></a>
<a id="secao-26"></a>

## Balanced Cross Entropy Loss

Para resolver o problema citado, podemos utilizar a **balanced cross entropy loss**, que atribui pesos diferentes para cada classe, penalizando mais os erros nas classes minoritárias. $$\text{ BCE } = - \frac{1}{N}\sum_{i = 1}^{N}\omega_{t_{i}}\log(p_{i})$$

o peso $\omega_{t_{i}}$ é pré-calculado de forma inversamente proporcional à frequência da classe $t_{i}$ no dataset, de forma que classes minoritárias tenham pesos maiores e classes majoritárias tenham pesos menores. Isso força a rede a prestar mais atenção às classes minoritárias durante o treinamento. Podemos ter uma formulação binária também $$\text{ BCE } = - \frac{1}{N}\left( \sum_{i \in \text{ positivos}}\omega_{\text{pos }}\log(p_{i}) + \sum_{i \in \text{ negativos}}\omega_{\text{neg }}\log(p_{i}) \right)$$

<a id="balanced-focal-loss"></a>
<a id="secao-28"></a>

## Balanced Focal Loss

Combina as duas soluções, ponderando cada pixel de acordo com sua classe e aplicando penalidade em pixels fáceis, de forma que a rede foque nos pixels mais difíceis e nas classes minoritárias. $$\text{ FL}_{\text{bal }} = - \frac{1}{N}\sum_{i = 1}^{N}\omega_{t_{i}}\left( 1 - p_{i} \right)^{\gamma}\log(p_{i})$$

<a id="cross-entropy-loss"></a>
<a id="secao-25"></a>

## Cross Entropy Loss

A primeira que vamos ver é a mais padrão para problemas de classificação, a **cross entropy loss**. Ela é definida como $$\text{ CE } = - \frac{1}{N}\sum_{i = 1}^{N}\log(p_{i})$$

se o modelo prevê alta probabilidade para a classe correta do pixel, o $\log(p_{i})$ será próximo de $0$, e a loss será pequena. Se o modelo prevê baixa probabilidade para a classe correta do pixel, o $\log(p_{i})$ será negativo e a loss será grande. O objetivo do treinamento é minimizar essa loss, ajustando os pesos da rede para que ela preveja corretamente as classes dos pixels.

No entanto, essa loss carrega um problema. Quando existe um desbalanceamento de classes dentro do meu dataset, pode acontecer de a rede aprender a prever apenas a classe majoritária, ignorando as classes minoritárias.

<a id="focal-loss"></a>
<a id="secao-27"></a>

## Focal Loss

Essa loss serve para resolver um problema sutíl. A loss anterior resolve o problema de desbalanceamento de classes, mas não resolve o problema de **hard examples**, ou seja, exemplos que são difíceis de classificar e quais são esses pixeis? São justamente os que estão cada vez mais próximos das bordas do elemento. No entanto, os pixeis fáceis costumam ser os mais presentes, e a soma do gradiente de sua contribuição pode atrapalhar no aprendizado dos pixeis mais difíceis. A **focal loss** resolve esse problema, diminuindo a contribuição dos pixeis fáceis para o gradiente, permitindo que a rede foque nos pixeis mais difíceis. $$\text{ FL } = - \frac{1}{N}\sum_{i = 1}^{N}\left( 1 - p_{i} \right)^{\gamma}\log(p_{i})$$

- **Comportamento do pixel fácil**: Consideremos $p_{i} = 0.95$ e $\gamma = 2$, então o fator de peso fica $0.0025$, a perda desse pixel é reduzida em $99.75\%$, fazendo com que ele quase não afete o treinamento

- **Comportamento do pixel difícil**: Consideremos $p_{i} = 0.2$ e $\gamma = 2$, então o fator de peso fica $0.64$, a perda desse pixel é mantida relevante

$\gamma$ é o parâmetro focal, quanto maior ele é, mais severa é a penalidade aplicada aos pixels fáceis, e quanto menor ele é, mais leve é a penalidade aplicada aos pixels fáceis. O valor padrão de $\gamma$ é $2$, mas ele pode ser ajustado dependendo do problema e do dataset.

<a id="loss-function-for-regression"></a>
<a id="secao-29"></a>

## Loss Function for Regression

A saída por pixel pode não necessariamente ser um label de classe, mas um valor numérico. Por exemplo, se a rede estiver tentando estimar a profundidade aplicada àquela foto, então utilizamos as losses $L_{1}$ e $L_{2}$ $$\begin{aligned} L_{1} & = \frac{1}{N}\sum_{i = 1}^{N}\vert y_{i} - t_{i}\vert  \\ L_{2} & = \frac{1}{N}\sum_{i = 1}^{N}\left( y_{i} - t_{i} \right)^{2} \end{aligned}$$

onde $y_{i}$ é o valor predito pelo modelo e $t_{i}$ é o valor verdadeiro.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Deeplab V3 & V3+](../arquiteturas/index.md#deeplab-v3-v3)
- Próximo: [Pontos Práticos](../pontos-praticos/index.md)
