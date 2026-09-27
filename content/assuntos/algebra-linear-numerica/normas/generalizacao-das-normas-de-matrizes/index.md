---
layout: "default"
title: "Generalização das normas de matrizes — Normas"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 6
---

[Álgebra Linear Numérica](../../index.md) · [Normas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-6"></a>

# Generalização das normas de matrizes

Vimos que uma norma segue 3 propriedades, definimos uma norma geral de matriz da mesma forma!!

**Definição**

Dadas as matrizes $A$ e $B$, uma norma $\| \cdot \|:{\mathbb{C}}^{m \times n} \rightarrow {\mathbb{R}}^{+}$ é uma função que segue estas 3 propriedades:

1.  $\| A\| \geq 0$, e $\| A\| = 0 \Leftrightarrow A = 0$

2.  $\| A + A\| \leq \| A\| + \| B\|$

3.  $\|\alpha A\| = \vert \alpha\|\vert A\|$

A mais importante é a **Norma de Frobenius**, definida como:

**Definição**

Dada uma matriz $A \in {\mathbb{C}}^{m \times n}$, sua **Norma de Frobenius** é definida como:

$\| A\|_{F} = \left( \sum_{i = 1}^{m}\sum_{j = 1}^{n}\vert a_{ij}\vert ^{2} \right)^{\frac{1}{2}}$ = $\sqrt{tr\left( A^{\ast}A \right)}$ = $\sqrt{tr\left( AA^{\ast} \right)}$

**Teorema**

$\| AB\|_{F} \leq \| A\|_{F}\| B\|_{F}$

**Demonstração**

$\| AB\|_{F} = \left( \sum_{i = 1}^{m}\sum_{j = 1}^{n}\vert c_{ij}\vert ^{2} \right)^{\frac{1}{2}} \leq \left( \sum_{i = 1}^{m}\sum_{j = 1}^{n}\left( \| a_{i}\|_{2}\| b_{j}\|_{2} \right)^{2} \right)^{\frac{1}{2}} = \left( \sum_{i = 1}^{m}\| a_{i}\|_{2}^{2}\sum_{j = 1}^{n}\| b_{j}\|_{2}^{2} \right)^{\frac{1}{2}} = \| A\|_{F}\| B\|_{F}$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Limitando $\| AB\|$](../limitando-ab/index.md)
- Próximo: [SVD](../../svd/index.md)
