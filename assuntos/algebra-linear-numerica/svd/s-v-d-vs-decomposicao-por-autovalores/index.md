---
layout: "default"
title: "S.V.D vs Decomposição por Autovalores — SVD"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 12
---

[Álgebra Linear Numérica](../../index.md) · [SVD](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-12"></a>

# S.V.D vs Decomposição por Autovalores

Podemos fazer algo semelhante com a decomposição por autovalores. Dada $A \in {\mathbb{C}}^{m \times m}$ com autovetores linearmente independentes, ou seja, podemos expressar $A = S\Lambda S^{- 1}$ com as colunas de $S$ sendo os autovetores de $A$ e $\Lambda$ sendo uma matriz diagonal com os autovalores de $A$ como entradas.

Definindo $b,x \in {\mathbb{C}}^{m}$ satisfazendo $b = Ax$, podemos escrever:

$\lbrack b\rbrack_{s^{- 1}} = S^{- 1}b$ e $\lbrack x\rbrack_{s^{- 1}} = S^{- 1}x$

Onde estou denotando $s^{- 1}$ como a base expressa pelas colunas de $S^{- 1}$, então a nova expressão expandida é:

$b = Ax \Leftrightarrow S^{- 1}b = S^{- 1}Ax = S^{- 1}S\Lambda S^{- 1}x \Leftrightarrow S^{- 1}b = \Lambda S^{- 1}x$

$\lbrack b\rbrack_{s^{- 1}} = \Lambda\lbrack x\rbrack_{s^{- 1}}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Mudança de base](../mudanca-de-base/index.md)
- Próximo: [Propriedades de matrizes com SVD](../propriedades-de-matrizes-com-svd/index.md)
