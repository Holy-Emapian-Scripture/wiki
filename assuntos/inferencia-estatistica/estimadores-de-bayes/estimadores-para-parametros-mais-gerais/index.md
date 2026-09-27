---
layout: "default"
title: "Estimadores para Parâmetros mais gerais — Estimadores de Bayes"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 12
---

[Inferência Estatística](../../index.md) · [Estimadores de Bayes](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-12"></a>

# Estimadores para Parâmetros mais gerais

Até agora nós vimos estimadores para os parâmetros em si, porém, as vezes podemos estar interessados em outras generalizações. Um exemplo de generalização é para estimar, por exemplo, dois parâmetros de uma só vez, como estimar uma média e uma variância (Saída multivariada) ou uma função do parâmetro em si, por exemplo, se $\theta$ é a taxa de falha, então podemos querer estimar $1/\theta$ que é a média de falhas

**Definição: Estimador/Estimativa**

Seja $X_{1},\ldots,X_{n}$ serem dados observados em que a distribuição conjunta é dado um parâmetro $\theta \in \Omega \subset {\mathbb{R}}^{k}$. Defina $h:\Omega \rightarrow {\mathbb{R}}^{d}$. Defina $\psi = h(\theta)$. Um **estimador** de $\psi$ é a função $\delta(X_{1},\ldots,X_{n}):{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{d}$. Se $X_{1} = x_{1},\ldots,X_{n} = x_{n}$ são observados, então $\delta(x_{1},\ldots,x_{n})$ é uma **estimativa** de $\psi$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Estimador de Bayes](../estimador-de-bayes/index.md)
- Próximo: [Estatística Frequentista](../../estatistica-frequentista/index.md)
