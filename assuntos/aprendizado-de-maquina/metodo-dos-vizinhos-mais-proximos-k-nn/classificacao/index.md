---
layout: "default"
title: "Classificação — Método dos Vizinhos mais próximos (k-NN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 3
---

[Aprendizado de Máquina](../../index.md) · [Método dos Vizinhos mais próximos (k-NN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-3"></a>

# Classificação

Seja $\mathcal{D} ≔ \left\{ \left( x_{1},y_{1} \right),\ldots,\left( x_{N},y_{N} \right) \right\} \subset \mathcal{X} \times \mathcal{Y}$ o conjunto de treinamento e $d:\mathcal{D} \times \mathcal{D} \rightarrow {\mathbb{R}}^{+} \cup \left\{ 0 \right\}$ uma função de **distância**. Vamos supor que queremos classificar um vetor $x \in \mathcal{X}$ arbitrário.

O método k-NN classifica o vetor $x$ atribuindo a ele a classe mais comum entre os rótulos dos pontos em $\mathcal{V}_{k}(x)$, ou seja: $$h(x) ≔ \text{ argmax}_{\left\{ y \in \mathcal{Y} \right\}}\sum_{\left\{ \left( x_{i},y_{i} \right) \in \mathcal{V}_{k}(x) \right\}}{\mathbb{I}}_{\left\{ y_{i} = y \right\}}$$ (De forma simplificada, o rótulo mais comum dentro do conjunto de vizinhos é o rótulo atribuído ao ponto $x$)

![Exemplo de classificação usando o método k-NN. O ponto $x$ é o ponto a ser classificado, os pontos azuis e vermelhos são os pontos do conjunto de treinamento, e as linhas tracejadas indicam as fronteiras de decisão do modelo. Aqui, se $k = 5$, ele vai classificar como **Classe 1** (vermelho)](../../assets/knn-classification.png)

*Figura 1. Exemplo de classificação usando o método k-NN. O ponto $x$ é o ponto a ser classificado, os pontos azuis e vermelhos são os pontos do conjunto de treinamento, e as linhas tracejadas indicam as fronteiras de decisão do modelo. Aqui, se $k = 5$, ele vai classificar como **Classe 1** (vermelho)*

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Introdução Intuitiva](../introducao-intuitiva/index.md)
- Próximo: [Regressão](../regressao/index.md)
