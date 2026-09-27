---
layout: "default"
title: "Regressão — Método dos Vizinhos mais próximos (k-NN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 4
---

[Aprendizado de Máquina](../../index.md) · [Método dos Vizinhos mais próximos (k-NN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Regressão

O k-NN pode também ser empregado em problemas de regressão. Para isso, precisamos de uma forma de combinar as saídas em $\mathcal{V}_{k( \cdot )}$. Uma das estratégias mais comuns consiste em computar a média ponderada pelo inverso da distância: $$h(x) ≔ \frac{1}{Z}\sum_{(x',y') \in \mathcal{V}_{k}(x)}y\frac{'}{d(x,x')}\text{\quad\quad}Z ≔ \sum_{(x',y') \in \mathcal{V}_{k}(x)}\frac{1}{d(x,x')}$$

permitindo que pontos mais próximos a $x$ exerçam maior influência no cômputo da predição $h(x)$. Ideia semelhante pode também ser aplicada a classificação.

Observe que o algoritmo k-NN não necessita de treinamento, ou equivalentemente, o treinamento consiste em simplesmente armazenar o conjunto de dados $\mathcal{D}$. Por conta disso, k-NN é dito ser uma abordagem de lazy learning (Atkeson et al., 1997)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Classificação](../classificacao/index.md)
- Próximo: [Qual distância escolher?](../qual-distancia-escolher/index.md)
