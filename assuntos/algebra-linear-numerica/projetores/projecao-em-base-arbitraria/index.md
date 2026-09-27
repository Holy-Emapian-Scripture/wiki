---
layout: "default"
title: "Projeção em base arbitrária — Projetores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 19
---

[Álgebra Linear Numérica](../../index.md) · [Projetores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-19"></a>

# Projeção em base arbitrária

Dada uma base arbitrária $\left\{ a_{j} \right\}$, deixamos os vetores dessa base serem as colunas de $A$. Dado $v$ com $Pv = y \in$ $C(A)$, isso significa $y - v\bot$ $C(A)$, ou seja, $a_{j}^{\ast (y - v)} = 0\ \forall j$. Sabemos que $y \in$ $C(A)$, então vamos escrevê-lo como $Ax = y$, então podemos reescrever $a_{j}^{\ast (y - v)} = 0\ \forall j$ como: $$A^{\ast (Ax - v)} = 0 \Leftrightarrow A^{\ast}Ax - A^{\ast}v = 0 \Leftrightarrow A^{\ast}Ax = A^{\ast}v \Leftrightarrow x = \left( A^{\ast}A \right)^{- 1}A^{\ast}v$$ $$Ax = {A\left( A^{\ast}A \right)}^{- 1}A^{\ast}v \Leftrightarrow y = {A\left( A^{\ast}A \right)}^{- 1}A^{\ast}v$$ $$\Rightarrow P = {A\left( A^{\ast}A \right)}^{- 1}A^{\ast}$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Projeção com base ortonormal](../projecao-com-base-ortonormal/index.md)
- Próximo: [Fatoração QR](../../fatoracao-qr/index.md)
