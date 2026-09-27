---
layout: "default"
title: "Decomposição em Autovalores — Problemas de Autovalores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 18
---

[Álgebra Linear Numérica](../../index.md) · [Problemas de Autovalores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-18"></a>

# Decomposição em Autovalores

Uma **decomposição em autovalores** de uma matriz $A \in {\mathbb{C}}^{m \times n}$ é uma fatoração:

$$A = X\Lambda X^{- 1}$$ <a id="decomposicao_autovalores"></a>

Onde $\Lambda$ é diagonal e $\det(X) \neq 0$.

Isso é equivalente a:

$$\underset{A}{\underbrace{\begin{pmatrix} \  & \  & \  & \  \\ \  & \  & A & \  & \  \\ \  & \  & \  & \ \end{pmatrix}}} \cdot \underset{X}{\underbrace{\begin{pmatrix} \vert  & \vert  & \vert  & \vert  & \\ x_{1} & x_{2} & \ldots & x_{n} \\ \vert  & \vert  & \vert  & \vert \end{pmatrix}}} = \underset{\Lambda}{\underbrace{\begin{pmatrix} \lambda_{1} & 0 & \ldots & 0 \\ 0 & \lambda_{2} & \ldots & 0 \\ 0 & 0 & \ldots & 0 \end{pmatrix}}} \cdot \underset{X}{\underbrace{\begin{pmatrix} \vert  & \vert  & \vert  & \vert  & \\ x_{1} & x_{2} & \ldots & x_{n} \\ \vert  & \vert  & \vert  & \vert \end{pmatrix}}}$$ <a id="eq_decomposicao_autovalores_matricial"></a>

Da [\[eq_decomposicao_autovalores_matricial\]](#eq_decomposicao_autovalores_matricial) e da [\[def_autovalor_autovetor\]](../definicoes/index.md#def_autovalor_autovetor), decorre que $Ax_{i} = \lambda_{i}x_{i}$, então a i-ésima coluna de $X$ é um autovetor de $A$ e $\lambda_{i}$ é o autovalor associado a $x_{i}$.

A decomposição apresentada pode representar uma mudança de base: Considere $Ax = b$ e $A = X\Lambda X^{- 1}$, então:

$$Ax = b \Leftrightarrow X\Lambda X^{- 1}x = b \Leftrightarrow \Lambda\left( X^{- 1}x \right) = X^{- 1}b$$

Então para calcular $Ax$, podemos expandir $x$ como combinação das colunas de $X$ e aplicar $\Lambda$. Como $\Lambda$ é diagonal, o resultado ainda vai ser uma combinação das colunas de $X$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Definições](../definicoes/index.md)
- Próximo: [Multiplicidades Algébrica e Geométrica](../multiplicidades-algebrica-e-geometrica/index.md)
