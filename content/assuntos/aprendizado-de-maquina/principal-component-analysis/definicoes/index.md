---
layout: "default"
title: "Definições — Principal Component Analysis"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 6
---

[Aprendizado de Máquina](../../index.md) · [Principal Component Analysis](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-6"></a>

# Definições

O PCA pode ser interpretado como duas definições distintas que dão origem ao mesmo resultado

- Projeção ortogonal dos dados em um espaço de menor dimensão (Subespaço Principal) de forma que a variância dos dados seja maximizada

- Projeção Linear que minimiza o custo médio de projeção

Antes de entrarmos em detalhes sobre essas definições, vamos colocar algumas definições úteis que, nós já sabemos, mas refrescar a nossa memória nunca é demais

**Definição: Projetar sobre um subespaço**

Dado um ponto $x \in {\mathbb{R}}^{D}$, sua projeção ortogonal no subespaço é o ponto $\hat{x}$ nesse subespaço mais próximo de $x$. Como consequência, temos que $$\left( x - \hat{x} \right)^{T}u = 0$$ onde é um vetor qualquer no subespaço

**Teorema: Projeção ortogonal**

Seja $X$ uma matriz ${\mathbb{R}} \times {\mathbb{R}}$, a projeção do vetor $y$ no espaço coluna de $X$ é dada por: $$\hat{y} = {X\left( X^{T}X \right)}^{- 1}X^{T}y$$ se $X$ é ortogonal, então $$\hat{y} = XX^{T}y$$

<a id="base-coefficients"></a>

**Teorema: Coeficientes de Base**

Seja $\left\{ q_{1},\ldots,q_{D} \right\}$ uma base ortogonal do ${\mathbb{R}}^{D}$ e $x \in {\mathbb{R}}^{D}$ tal que $$x = \sum_{i = 1}^{D}\alpha_{i}q_{i}$$ então temos que $$Qx = \begin{pmatrix} \alpha_{1} & \ldots & \alpha_{D} \end{pmatrix}^{T}$$ onde $Q$ é a matriz cujas colunas são os vetores da base.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Introdução](../introducao/index.md)
- Próximo: [Máxima Variância](../maxima-variancia/index.md)
