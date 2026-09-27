---
layout: "default"
title: "Determinante e Traço — Problemas de Autovalores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 23
---

[Álgebra Linear Numérica](../../index.md) · [Problemas de Autovalores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-23"></a>

# Determinante e Traço

**Teorema**

Seja $\lambda_{j}$ um autovalor de $A \in {\mathbb{C}}^{m \times m}$: $$\begin{array}{r} \det(A) = \prod_{j = 1}^{m}\lambda_{j} \\ \operatorname{tr}(A) = \sum_{j = 1}^{m}\lambda_{j} \end{array}$$

**Demonstração**

$$\det(A) = ( - 1)^{m}\det( - A) = ( - 1)^{m}p_{A(0)} = \prod_{j = 1}^{m}\lambda_{j}$$ Olhando a equação [\[characteristical-polynomial\]](../multiplicidades-algebrica-e-geometrica/index.md#characteristical-polynomial), podemos observar que o coeficiente do termo $\lambda^{m - 1}$ é igual a $- \sum_{j = 1}^{m}\lambda_{j}$ e na equação [\[eq_polinimio_caracteristico\]](../multiplicidades-algebrica-e-geometrica/index.md#eq_polinimio_caracteristico) o termo é o negativo da soma dos termos da diagonal, ou seja, $- \operatorname{tr}(A)$, ou seja, $\operatorname{tr}(A) = \sum_{j = 1}^{m}\lambda_{j}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Diagonalizabilidade](../diagonalizabilidade/index.md)
- Próximo: [Diagonalização Unitária](../diagonalizacao-unitaria/index.md)
