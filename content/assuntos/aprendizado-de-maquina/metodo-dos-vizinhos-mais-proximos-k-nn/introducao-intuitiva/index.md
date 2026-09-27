---
layout: "default"
title: "Introdução Intuitiva — Método dos Vizinhos mais próximos (k-NN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 2
---

[Aprendizado de Máquina](../../index.md) · [Método dos Vizinhos mais próximos (k-NN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-2"></a>

# Introdução Intuitiva

O método dos vizinhos mais próximos (k-NN) é um algoritmo de aprendizado de máquina simples e eficaz usado para classificação e regressão. Ele funciona com base na ideia de que objetos semelhantes estão próximos uns dos outros no espaço de características. Para classificar um novo ponto, o k-NN identifica os k pontos mais próximos no conjunto de treinamento e atribui a classe mais comum entre esses vizinhos ao novo ponto.

O valor de k é um hiperparâmetro que pode ser ajustado para melhorar o desempenho do modelo. O k-NN é fácil de entender e implementar, mas pode ser computacionalmente caro para grandes conjuntos de dados, pois requer o cálculo das distâncias entre o novo ponto e todos os pontos do conjunto de treinamento.

Um das hipóteses fundamentais em ML é que existe algum nível de suavidade no mapeamento entre o espaço de entrada $\mathcal{X}$ e o de saída $\mathcal{Y}$. Em outras palavras, se dois elementos $x,x' \in \mathcal{X}$ são semelhantes, então eles devem ter saídas $y,y' \in \mathcal{Y}$ similares. O método dos k vizinhos mais próximos (k nearest neighbors, k-NN), proposto por Cover e Hart (1967), aplica diretamente esse conceito.

Nesse capítulo, vamos estudar como k-NN pode ser usados para problemas de classificação e regressão. Discutiremos o impacto do k e também da escolha de distância (ou métrica) para o espaço $\mathcal{X}$, que é primordial para a aplicação do método. Finalmente, estudaremos o comportamento do método k-NN quando a dimensionalidade do espaço $\mathcal{X}$ é alta

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Método dos Vizinhos mais próximos (k-NN)](../index.md)
- Próximo: [Classificação](../classificacao/index.md)
