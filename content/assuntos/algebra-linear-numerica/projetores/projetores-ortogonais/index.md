---
layout: "default"
title: "Projetores ortogonais — Projetores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 16
---

[Álgebra Linear Numérica](../../index.md) · [Projetores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-16"></a>

# Projetores ortogonais

Finalmente! Os projetores que ouvimos falar o tempo todo! Eles projetam um vetor em um espaço fazendo a direção formar um ângulo de 90 graus com a projeção.

![](../../assets/Orthogonal_Projector.jpg)

Isso significa $(Pv)^{\ast (v - Pv)} = 0$

<a id="orthogonal-projectors"></a>

**Teorema**

$P$ é um projetor ortogonal $\Leftrightarrow$ $P = P^{\ast}$

**Demonstração**

1.  $\Leftarrow )$ Dado $x,y \in {\mathbb{C}}^{m}$, então $x^{\ast}P^{\ast (I - P)}y = x^{\ast \left( P^{\ast} - P^{\ast}P \right)}y = x^{\ast \left( P - P^{2} \right)}y = x^{\ast (P - P)}y = 0$

2.  $\Rightarrow )$ Seja $\left\{ q_{1},\ldots,q_{m} \right\}$ uma base ortonormal de ${\mathbb{C}}^{m}$ onde $\left\{ q_{1},\ldots,q_{n} \right\}$ é base de $S_{1}$ e $\left\{ q_{n + 1},\ldots,q_{m} \right\}$ é base de $S_{2}$. Para $j \leq n$ temos $Pq_{j} = q_{j}$ e para $j > n$ temos $Pq_{j} = 0$, seja $Q$ a matriz com colunas $\left\{ q_{1},\ldots,q_{m} \right\}$, temos: $$Q = \begin{pmatrix} \vert  & & \vert  \\ q_{1} & \ldots & q_{m} \\ \vert  & & \vert \end{pmatrix} \Leftrightarrow PQ = \begin{pmatrix} \vert  & & \vert  & \vert  \\ q_{1} & \ldots & q_{n} & 0 & \ldots \\ \vert  & & \vert  & \vert \end{pmatrix} \Leftrightarrow Q^{\ast}PQ = \begin{pmatrix} 1 \\ & 1 \\ & & \ddots \\ & & & 1 \\ & & & & 0 \\ & & & & & \ddots \end{pmatrix}$$, o que significa que encontramos uma decomposição SVD para $P$:

$$P = Q\Sigma Q^{\ast} \Leftrightarrow P^{\ast} = Q\Sigma^{\ast}Q^{\ast} = Q\Sigma Q^{\ast} = P$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Projetores complementares](../projetores-complementares/index.md)
- Próximo: [Projeção ortogonal sobre um vetor](../projecao-ortogonal-sobre-um-vetor/index.md)
