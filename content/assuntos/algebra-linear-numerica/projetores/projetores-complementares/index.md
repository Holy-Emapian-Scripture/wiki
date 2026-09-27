---
layout: "default"
title: "Projetores complementares — Projetores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 15
---

[Álgebra Linear Numérica](../../index.md) · [Projetores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Projetores complementares

Se $P$ é um projetor, $I - P$ é seu projetor complementar.

**Teorema**

$I - P$ projeta sobre null$(P)$ e $P$ projeta sobre null$(I - P)$

**Demonstração**

1.  $C(I - P) \subseteq N(P)$ porque $v - Pv \in N(P)$ e $C(I - P) \supseteq N(P)$ porque, se $Pv = 0$, podemos reescrever como $(I - P)v = v$, isso significa $N(P) = C(I - P)$

2.  Se reescrevermos a expressão como $P = I - (I - P)$, então, usando o mesmo argumento de antes, temos $C(P) = N(I - P)$

**Teorema**

$N(I - P) \cap N(P) = \left\{ 0 \right\}$

**Demonstração**

$N(A) \cap C(A) = \left\{ 0 \right\} \Rightarrow N(P) \cap C(P) = \left\{ 0 \right\} \Leftrightarrow N(P) \cap N(I - P) = \left\{ 0 \right\}$

Isso significa que, se temos um projetor $P$ em ${\mathbb{C}}^{m \times m}$, esse projetor separa ${\mathbb{C}}^{m}$ em dois espaços $S_{1}$ e $S_{2}$, de forma que $S_{1} \cap S_{2} = \left\{ 0 \right\}$ e $S_{1} + S_{2} = {\mathbb{C}}^{m}$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Projetores](../index.md)
- Próximo: [Projetores ortogonais](../projetores-ortogonais/index.md)
