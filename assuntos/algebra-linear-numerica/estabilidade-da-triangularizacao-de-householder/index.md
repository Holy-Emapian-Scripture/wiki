---
layout: "default"
title: "Estabilidade da Triangularização de Householder"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 1
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-1"></a>

# Estabilidade da Triangularização de Householder

------------------------------------------------------------------------

Nesse capítulo, a gente tem uma visão mais aprofundada da análise de **erro retroativo** (Backwards Stable). Dando uma breve recapitulada, para mostrar que um algoritmo $\widetilde{f}:X \rightarrow Y$ é **backwards stable**, você tem que mostrar que, ao aplicar $\widetilde{f}$ em uma entrada $x$, o resultado retornado seria o mesmo que aplicar o problema original $f:X \rightarrow Y$ em uma entrada levemente perturbada $x + \Delta x$, de forma que $\Delta x = O\left( \varepsilon_{\text{machine}} \right)$.

<!-- wiki:original:fim -->

## Tópicos desta página

1. [O Experimento](o-experimento/index.md)
2. [Teorema](teorema/index.md)
3. [Algoritmo para resolver $Ax = b$](algoritmo-para-resolver-ax-b/index.md)

## Percurso de estudo

[Trilha: A2](../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Próximo: [O Experimento](o-experimento/index.md)
