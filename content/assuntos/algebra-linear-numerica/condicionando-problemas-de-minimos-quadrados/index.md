---
layout: "default"
title: "Condicionando Problemas de Mínimos Quadrados"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 7
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# Condicionando Problemas de Mínimos Quadrados

------------------------------------------------------------------------

**Nota**: Nessa lecture, quando escrevemos $\| \cdot \|$, estamos nos referindo a norma 2, **não a qualquer norma**, logo, $\| \cdot \| = \| \cdot \|_{2}$

Vamos relembrar o problema dos mínimos quadrados?

$$\begin{array}{r} \text{ Dada }A \in {\mathbb{C}}^{m \times n}\text{ de posto completo, }m \geq n\text{  e  }b \in {\mathbb{C}}^{m}, \\ \text{ache }x \in {\mathbb{C}}^{n}\text{ tal que }\| b - Ax\|_{2}\text{ seja a menor possível } \end{array}$$<a id="min-squares"></a>

No resumo passado, vimos que o $x$ que satisfaz esse problema é $$x = \left( A^{\ast}A \right)^{- 1}A^{\ast}b \Rightarrow y = {A\left( A^{\ast}A \right)}^{- 1}A^{\ast}b \Leftrightarrow y = Pb$$<a id="min-squares-equations"></a> Ou seja, a projeção ortogonal de $b$ em $A$ resulta no vetor $y$. Queremos então saber o condicionamento de [\[min-squares\]](#min-squares) de acordo com perturbações em $b$, $A$, $y$ e $x$. Tenha em mente que o problema recebe dois parâmetros, $A$ e $b$ e retorna as soluções $x$ e $y$

<!-- wiki:original:fim -->

## Tópicos desta página

1. [O Teorema](o-teorema/index.md)

## Percurso de estudo

[Trilha: A2](../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Teorema da Estabilidade Retroativa (Backward Stability)](../estabilidade-da-back-substitution/teorema-da-estabilidade-retroativa-backward-stability/index.md)
- Próximo: [O Teorema](o-teorema/index.md)
