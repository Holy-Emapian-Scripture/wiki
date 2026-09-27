---
layout: "default"
title: "Método da Recorrência — Recorrência"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A1.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
revisao: "Thalis Ambrosim Falqueto"
ano_original: 2025
ordem_na_trilha: 5
---

[Projeto e Análise de Algoritmos](../../index.md) · [Recorrência](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Método da Recorrência

O método da iteração consiste em expandir a relação de recorrência até o $n$-ésimo termo, de forma que seja possível compreender a sua forma geral

**Exemplo**

$$T(n) = \begin{cases} \theta(1)\text{ se }n = 1 \\ 2T(n - 1) + n\text{ se }n > 1 \end{cases}$$

Expandindo, temos: $$\begin{array}{r} T(n) = 2T(n - 1) + n \\ T(n) = 2\left( 2T(n - 2) + n \right) + n \\ \vdots \\ T(n) = 2^{k}T(n - k) + \left( 2^{k} - 1 \right)n - \sum_{j = 1}^{k - 1}2^{j}j \end{array}$$ Para chegar na última iteração, temos que $k = n - 1$ $$T(n) = 2^{n - 1} + \left( 2^{n - 1} - 1 \right)n - \sum_{j = 1}^{n - 2}2^{j}j$$ Temos que: $\sum_{j = 1}^{n - 2}2^{j}j = \frac{1}{2}\left( 2^{n}n - 3 \cdot 2^{n} + 4 \right)$, então podemos fazer: $$\begin{array}{r} T(n) = 2^{n - 1} + 2^{n - 1}n - n - 2^{n - 1}n + 3 \cdot 2^{n - 1} - 2 \\ \Leftrightarrow T(n) = 2^{n - 1} - n + 3 \cdot 2^{n - 1} - 2 \\ \Leftrightarrow T(n) = 4 \cdot 2^{n - 1} - n - 2 = 2^{n + 1} - n - 2 \\ \Leftrightarrow T(n) = \Theta(2^{n}) \end{array}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Método da árvore de recursão](../metodo-da-arvore-de-recursao/index.md)
- Próximo: [Método mestre](../metodo-mestre/index.md)
