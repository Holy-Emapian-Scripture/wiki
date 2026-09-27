---
layout: "default"
title: "Fatoração e Diagonalização de Schur — Algoritmos de Autovalores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 30
---

[Álgebra Linear Numérica](../../index.md) · [Algoritmos de Autovalores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-30"></a>

# Fatoração e Diagonalização de Schur

A maioria dos algoritmos de fatoração atuais envolvem o uso da fatoração de Schur de uma matriz. A gente pega a matriz $A$ e vai aplicando transformações nela com matrizes unitárias $Q_{j}$ (Transformação $X \mapsto Q_{j}^{\ast}XQ_{j}$) de forma que o produto: $$Q_{j}^{\ast}\ldots Q_{2}^{\ast}Q_{1}^{\ast}AQ_{1}Q_{2}\ldots Q_{j}$$<a id="upper-triangular-transformation"></a> Converja para uma matriz triangular superior $T$ conforme $j \rightarrow \infty$

O livro fala também que é possível utilizar de alguns truques para computar os autovalores complexos e que os algoritmos que veremos também podem ser usados, em matrizes Hermitianas, para obter sua diagonalização unitária.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Uma dificuldade fundamental](../uma-dificuldade-fundamental/index.md)
- Próximo: [Duas fases da computação de Autovalores](../duas-fases-da-computacao-de-autovalores/index.md)
