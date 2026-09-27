---
layout: "default"
title: "Projeção ortogonal sobre um vetor — Projetores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 17
---

[Álgebra Linear Numérica](../../index.md) · [Projetores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-17"></a>

# Projeção ortogonal sobre um vetor

Vamos usar o mesmo exemplo usado anteriormente

![](../../assets/Orthogonal_Projector.jpg)

Seja $q$ o vetor que gera $P$, sabemos que $Pv = \alpha q$ $$(v - Pv)^{\ast}q = 0 = (v - \alpha q)^{\ast}q = 0$$ Agora procuramos o $\alpha$ que torna esta equação válida $$v^{\ast}q - \alpha q^{\ast}q = 0 \Leftrightarrow v^{\ast}q = \alpha q^{\ast}q \Leftrightarrow \alpha = \frac{v^{\ast}q}{q^{\ast}q}$$ $$Pv = \alpha q \Leftrightarrow Pv = \frac{v^{\ast}q}{q^{\ast}q}q \Leftrightarrow Pv = \frac{q^{\ast}v}{q^{\ast}q}q \Leftrightarrow Pv = q\frac{q^{\ast}v}{q^{\ast}q} \Leftrightarrow Pv = \frac{qq^{\ast}}{q^{\ast}q}v \Rightarrow P = \frac{qq^{\ast}}{q^{\ast}q}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Projetores ortogonais](../projetores-ortogonais/index.md)
- Próximo: [Projeção com base ortonormal](../projecao-com-base-ortonormal/index.md)
