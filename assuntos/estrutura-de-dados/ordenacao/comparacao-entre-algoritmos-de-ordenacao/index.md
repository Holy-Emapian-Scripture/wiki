---
layout: "default"
title: "3.5 Comparação entre algoritmos de ordenação — 3. Ordenação"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 19
---

[Estrutura de Dados](../../index.md) · [3. Ordenação](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-22"></a>

# 3.5 Comparação entre algoritmos de ordenação

Esses algoritmos, embora didáticos, são ineficientes para grandes conjuntos de dados. Nas próximas seções, abordaremos algoritmos mais avançados, como Merge Sort e Quick Sort, que possuem melhor desempenho. Vamos comparar os algoritmos que vemos até agora:

|                |                 |                         |          |           |
|----------------|-----------------|-------------------------|----------|-----------|
| Algoritmo      | Melhor caso     | Pior caso               | Estável? | In-place? |
| Selection Sort | $\Omega(n^{2})$ | $O\left( n^{2} \right)$ | Não      | Sim       |
| Insertion Sort | $\Omega(n)$     | $O\left( n^{2} \right)$ | Sim      | Sim       |
| Bubble Sort    | $\Omega(n)$     | $O\left( n^{2} \right)$ | Sim      | Sim       |

Fazendo uma rápida análise, vemos que não temos diferenças aparentes nas características entre Insertion Sort e Bubble Sort, enquanto o Selection Sort é pior que os dois.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [3.4 Bubble Sort](../bubble-sort/index.md)
- Próximo: [4.0 Ordeanção avançada](../../ordeancao-avancada/index.md)
