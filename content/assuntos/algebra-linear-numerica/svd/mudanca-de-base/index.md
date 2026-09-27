---
layout: "default"
title: "Mudança de base — SVD"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 11
---

[Álgebra Linear Numérica](../../index.md) · [SVD](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-11"></a>

# Mudança de base

Dado $b \in {\mathbb{C}}^{m}$, $x \in {\mathbb{C}}^{n}$ e $A \in {\mathbb{C}}^{m \times n},A = U\Sigma V^{\ast}$ podemos obter as coordenadas de $b$ na base das colunas de $U$ e $x$ nas colunas de $V$. Só para lembrar:

**Definição**

Dado $w \in V$ onde $V$ é um Espaço Vetorial, $\exists!x_{1},\ldots,x_{n} \in {\mathbb{C}}$ tal que $w = v_{1}x_{1} + \ldots + v_{n}x_{n}$ onde $\left\{ v_{j} \right\}$ é uma base de $V$. O vetor $\begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix}$, também denotado como $\lbrack w\rbrack_{v}$, é o **vetor de coordenadas** de $w$ na base $v$

Voltando, podemos expressar $\lbrack b\rbrack_{u} = U^{\ast}b$ e $\lbrack x\rbrack_{v} = V^{\ast}x$, mas por quê?

**Teorema**

Dada uma base ortonormal $\left\{ v_{k} \right\}$ de $V$ e $w \in V$, então

$\left( \lbrack w\rbrack_{v} \right)_{j} = v_{j}^{\ast}w$

**Demonstração**

$w = \alpha_{1}v_{1} + \ldots + \alpha_{n}v_{n}$

$v_{j}^{\ast}w = \alpha_{1}v_{j}^{\ast}v_{1} + \ldots + \alpha_{n}v_{j}^{\ast}v_{n}$

Sabendo que $\left\{ v_{j} \right\}$ é uma base ortonormal, o produto $\alpha_{i}v_{j}^{\ast}v_{i}$ é igual a 0 se $j \neq i$ e igual a $\alpha_{i}$ se $j = i$, ou seja:

$v_{j}^{\ast}w = \alpha_{j}$

Ok, agora que lembramos todas essas propriedades, podemos expressar a relação $b = Ax$ em termos de $\lbrack b\rbrack_{u}$ e $\lbrack x\rbrack_{v}$, vamos ver:

$b = Ax \Leftrightarrow U^{\ast}b = U^{\ast}Ax = U^{\ast}U\Sigma V^{\ast}x \Leftrightarrow U^{\ast}b = \Sigma V^{\ast}x$

$\Leftrightarrow \lbrack b\rbrack_{u} = \Sigma\lbrack x\rbrack_{v}$

Então podemos reduzir $A$ à matriz $\Sigma$ e $b$ e $x$ às suas coordenadas nas bases $u$ e $v$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Definição formal](../definicao-formal/index.md)
- Próximo: [S.V.D vs Decomposição por Autovalores](../s-v-d-vs-decomposicao-por-autovalores/index.md)
