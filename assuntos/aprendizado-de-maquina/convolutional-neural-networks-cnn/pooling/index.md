---
layout: "default"
title: "Pooling — Convolutional Neural Networks (CNN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 30
---

[Aprendizado de Máquina](../../index.md) · [Convolutional Neural Networks (CNN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-40"></a>

# Pooling

Para as definições a baixo, vamos considerar janelas já transformadas em colunas após a operação de im2col, e o stride já aplicado. Ou seja, a entrada da operação de pooling será um vetor $x \in {\mathbb{R}}^{m}$, de forma que a operação é aplicada em cada coluna da matriz $X_{\text{col}}$

**Definição: Max Pooling**

Seja $x \in {\mathbb{R}}^{m}$ a saída da camada de max pooling é dada por: $$Y_{ij} = \max x$$

**Teorema: Não-linearidade**

A operação de max pooling é não-linear, ou seja, não podemos expressá-la como uma combinação linear das entradas. Isso significa que a operação de pooling não pode ser representada como uma multiplicação de matrizes, o que dificulta a análise teórica da operação

**Definição: Adjunto do Max Pooling**

O adjunto do max pooling consiste em você armazenar a posição da última entrada máxima de cada janela de pooling, e no backward, você propaga o gradiente apenas para essa posição, enquanto as demais posições recebem gradiente zero. Isso garante que o gradiente seja propagado corretamente através da operação de max pooling, permitindo que a rede aprenda padrões invariantes à posição do objeto na imagem

**Exemplo**

$$\begin{pmatrix} a & b & c & d \end{pmatrix}$$ Supondo que $b$ é o maior valor, o max pooling vai retornar $$b$$ Então no backward, a matriz gerada será: $$\begin{pmatrix} 0 & \delta & 0 & 0 \end{pmatrix}$$

**Definição: Average Pooling**

Seja $x \in {\mathbb{R}}^{k^{2}}$ a coluna representando uma janela $k \times ₭$ a saída da camada de average pooling é dada por: $$y = \left( \frac{1}{k^{2}} \right)\sum_{i}^{k^{2}}x_{i}$$

**Teorema: Linearidade do Average Pooling**

A operação de average pooling é linear, ou seja, podemos expressá-la como uma combinação linear das entradas. Isso significa que a operação de pooling pode ser representada como uma multiplicação de matrizes

**Demonstração**

Definindo a matriz $$Q = \frac{1}{k^{2}}\begin{pmatrix} 1 & 1 & 1 & \ldots & 1 \end{pmatrix}$$ podemos escrever $$y = Qx$$ assim, ainda obtemos seu adjunto como $Q^{T}$, espalhando o erro igualmente para todas as camadas $$Q^{T}\delta = \frac{1}{k^{2}}\begin{pmatrix} \delta \\ \delta \\ \delta \\ \ldots \\ \delta \end{pmatrix} = \frac{\delta}{k^{2}}\begin{pmatrix} 1 \\ 1 \\ 1 \\ \ldots \\ 1 \end{pmatrix}$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Otimizações Computacionais](../otimizacoes-computacionais/index.md)
- Próximo: [Referências](../../referencias/index.md)
