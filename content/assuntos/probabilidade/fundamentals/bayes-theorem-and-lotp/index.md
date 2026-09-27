---
layout: "default"
title: "Baye’s Theorem and LOTP — Fundamentals"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1_recap.md"
trilha: "../../../../trilhas/probabilidade/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
data_original: "27/09/2026"
ordem_na_trilha: 2
---

[Probabilidade](../../index.md) · [Fundamentals](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-2"></a>

# Baye’s Theorem and LOTP

Baye’s theorem states that $\forall A,B \subset \Omega$:

$$P\left( A\vert B \right) = \frac{P\left( B\vert A \right)P(A)}{P(B)}$$

This follows directly from the **Law of Total Probability(LOTP)**:

$$P(A) = \sum_{i = 1}^{n}P\left( A\vert B_{i} \right)P\left( B_{i} \right) = \sum_{i = 1}^{n}P\left( A \cap B_{i} \right).$$

Given $B_{i}$ a partition of $\Omega$.

Notice that the function $P_{C}:\Omega \rightarrow \lbrack 0,1\rbrack$, $P_{C}(A) = P\left( A\vert C \right)$, given $C \subset \Omega$ is also a probability in the same space $E$, so both Baye’s theorem and LOTP assume conditional versions written in terms of $P_{C}$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Fundamentals](../index.md)
- Próximo: [Discrete Random Variables, Indicator Random Variables](../discrete-random-variables-indicator-random-variables/index.md)
