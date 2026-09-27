---
layout: "default"
title: "Problemas multiclasse, classificador *softmax* — Regressão Logística"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 13
---

[Aprendizado de Máquina](../../index.md) · [Regressão Logística](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-20"></a>

# Problemas multiclasse, classificador *softmax*

Nesse capítulo, nos focamos em problemas de classificação binária, em que $\vert \mathcal{Y}\vert  = 2$. No entanto, é fácil generalizar as técnicas que discutimos para problemas multi-classe (i.e., $\vert \mathcal{Y}\vert  > 2$). Para tal, basta substituir o nosso modelo observacional Bernoulli por uma distribuição categórica. Lembre que a Bernoulli é parametrizada por um parâmetro escalar que dita a probabilidade de cada classe. No caso da categórica, precisamos de um vetor de probabilidades, i.e., um vetor $r$ de tamanho $L = \vert \mathcal{Y}\vert$, em que cada entrada $r_{l}$ denota a probabilidade da classe $l$. Naturalmente, todas as entradas de $r$ devem ser não-negativas e $\sum_{l = 1}^{L}r_{l} = 1$. Resta-nos, então, expressar $r$ como uma função de $x$. Para tal, podemos generalizar nosso o procedimento que usamos para regressão logística.

Primeiro, calculamos um vetor de logits $z$, desta vez usando uma transformação linear para cada uma das $L$ classes $$z = \begin{pmatrix} x^{T}\theta^{(1)} \\ x^{T}\theta^{(2)} \\ \vdots \\ x^{T}\theta^{(L)} \end{pmatrix}$$

Finalmente, aplicamos a função Softmax para transformar $z$ em um vetor de probabilidades e obter $r$, que é dado por: $$r_{l} = \text{ Softmax}(z) = \frac{e^{z_{l}}}{\sum_{l' = 1}^{L}e^{z_{l'}}}$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Regressão Logística Bayesiana](../regressao-logistica-bayesiana/index.md)
- Próximo: [Redes Neurais](../../redes-neurais/index.md)
