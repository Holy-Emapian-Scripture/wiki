---
layout: "default"
title: "Máxima Verossimilhança — Gaussian and Bernoulli Mixture Models"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 11
---

[Aprendizado de Máquina](../../index.md) · [Gaussian and Bernoulli Mixture Models](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-11"></a>

# Máxima Verossimilhança

Suponha que temos um conjunto de dados $X = \left\{ x_{1},x_{2},\ldots,x_{N} \right\}$ com $x_{i} \in {\mathbb{R}}^{D}$ e queremos modelar essa matriz $N \times D$ como uma mistura de $K$ gaussianas. As variáveis latentes $Z = \left\{ z_{1},z_{2},\ldots,z_{N} \right\}$ que indicam de qual cluster cada ponto foi gerado também serão representadas por uma matriz $N \times K$ de vetores one-hot. A função de log-verossimilhança do modelo é então dada por: $$\ln p\left( X~\vert ~\mu,\Sigma,\pi \right) = \sum_{n = 1}^{N}\ln p\left( x_{n}~\vert ~\mu,\Sigma,\pi \right) = \sum_{n = 1}^{N}\ln\left\{ \sum_{k = 1}^{K}\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right) \right\}$$

Acaba que maximizar essa verossimilhança diretamente é difícil, pois a presença da soma dentro do log torna a derivada complicada. Uma alternativa válida é maximizar a verossimilhança por métodos de otimização de gradiente, porém, nós vamos utilizar o algoritmo Expectation-Maximization (EM), que é um método iterativo para encontrar estimativas de máxima verossimilhança em modelos com variáveis latentes.

<!-- wiki:original:fim -->

## Conteúdos relacionados

- [Estimadores/Estimações de Máxima Verossimilhança — Inferência Estatística](../../../inferencia-estatistica/estatistica-frequentista/estimadores-estimacoes-de-maxima-verossimilhanca/index.md)

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Introdução e Definição](../introducao-e-definicao/index.md)
- Próximo: [Expectation-Maximization (EM) para GMMs](../expectation-maximization-em-para-gmms/index.md)
