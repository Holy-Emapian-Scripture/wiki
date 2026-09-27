---
layout: "default"
title: "Limitando $\\| AB\\|$ — Normas"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 5
---

[Álgebra Linear Numérica](../../index.md) · [Normas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Limitando $\| AB\|$

Podemos limitar $\| AB\|$ como fazemos com normas de vetores.

**Teorema**

Dadas $A \in {\mathbb{C}}^{l \times m}$,$B \in {\mathbb{C}}^{m \times n}$ e $x \in {\mathbb{C}}^{n}$, então a norma induzida de $AB$ deve satisfazer:

$\| AB\|_{l \rightarrow n} \leq \| A\|_{l \rightarrow m}\| B\|_{m \rightarrow n}$

**Demonstração**

$\| ABx\|_{l} \leq \| A\|_{l \rightarrow m}\| Bx\|_{m} \leq \| A\|_{l \rightarrow m}\| B\|_{m \rightarrow n}\| x\|_{n}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Desigualdades de Cauchy-Schwarz e Hölder](../desigualdades-de-cauchy-schwarz-e-holder/index.md)
- Próximo: [Generalização das normas de matrizes](../generalizacao-das-normas-de-matrizes/index.md)
