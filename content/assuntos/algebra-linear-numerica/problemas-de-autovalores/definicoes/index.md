---
layout: "default"
title: "Definições — Problemas de Autovalores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 17
---

[Álgebra Linear Numérica](../../index.md) · [Problemas de Autovalores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-17"></a>

# Definições

Dada uma matriz $A \in {\mathbb{C}}^{m \times n}$, pela decomposição SVD $A = U\Sigma V^{\ast}$ sabemos que $A$ é uma transformação que **estica** e **rotaciona** vetores. Por isso, estamos interessados em subespaços de ${\mathbb{C}}^{m}$ nos quais a matriz age como uma multiplicação escalar, ou seja, estamos interessados nos $x \in {\mathbb{C}}^{n}$ que são somente esticados pela matriz. Como $Ax \in {\mathbb{C}}^{m}$ e $\lambda x \in {\mathbb{C}}^{n}$, concluimos que $m = n$: A matriz **deve ser quadrada**. Afinal, não faz sentido se $\lambda x$ e $Ax$ estiverem em conjuntos distintos. Com isso, prosseguimos com a definição:

**Definição: Autovalores e Autovetores**

Dada $A \in {\mathbb{C}}^{m \times m}$, um **autovetor** de $A$ é $x \in {\mathbb{C}}^{m} \smallsetminus \left\{ 0 \right\}$ que satisfaz:

$$Ax = \lambda x$$ <a id="eq_autovalores_autovetores"></a>

$\lambda \in {\mathbb{C}}$ é dito **autovalor** associado a $x$.

<a id="def_autovalor_autovetor"></a>

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Problemas de Autovalores](../index.md)
- Próximo: [Decomposição em Autovalores](../decomposicao-em-autovalores/index.md)
