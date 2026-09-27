---
layout: "default"
title: "Normas de vetores — Normas"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 2
---

[Álgebra Linear Numérica](../../index.md) · [Normas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-2"></a>

# Normas de vetores

**Definição: Norma**

Uma **norma** é uma função $\| \cdot \|:{\mathbb{C}}^{m} \rightarrow {\mathbb{R}}$ que satisfaz 3 propriedades:

1.  $\| x\| \geq 0$, e $\| x\| = 0 \Leftrightarrow x = 0$

2.  $\| x + y\| \leq \| x\| + \| y\|$

3.  $\|\alpha x\| = \vert \alpha\|\vert x\|$

Normalmente vemos a norma-2, ou a **Norma Euclidiana**, que representa o **tamanho** de um vetor. Com base nisso, podemos definir uma **norma-p**.

**Definição: Norma-p**

A **norma-p** de $x \in {\mathbb{C}}^{n}$ (ou $\| x\|_{p}$) é definida como:

$\| x\|_{p} = \left( \sum_{i = 1}^{n}\vert x_{i}\vert ^{p} \right)^{\frac{1}{p}}$

Então, podemos ter vários tipos de normas, de 1 até $\infty$, e também definimos isso!

**Definição: Norma infinita**

A **norma infinita** de $x \in {\mathbb{C}}^{n}$ (ou $\| x\|_{\infty}$) é definida como:

$\| x\|_{\infty} = \max\vert x_{i}\vert$

Você provavelmente está se perguntando “por que eu precisaria de algo assim”? Mas acredite, será útil no futuro! Existe um tipo de norma muito útil (de acordo com o livro), chamada **norma ponderada**.

**Definição: Norma ponderada**

A **norma ponderada** de $x \in {\mathbb{C}}^{n}$ é:

$\| x\|_{W} = \| Wx\| = \left( \sum_{i = 1}^{n}\vert w_{ii}x_{i}\vert ^{p} \right)^{\frac{1}{p}}$

Onde $W$ é uma **matriz diagonal** e $p$ é um número arbitrário

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Normas](../index.md)
- Próximo: [Normas de matrizes](../normas-de-matrizes/index.md)
