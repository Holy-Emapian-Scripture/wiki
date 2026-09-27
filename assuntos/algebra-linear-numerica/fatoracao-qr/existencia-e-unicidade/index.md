---
layout: "default"
title: "Existência e unicidade — Fatoração QR"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 24
---

[Álgebra Linear Numérica](../../index.md) · [Fatoração QR](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-24"></a>

# Existência e unicidade

**Teorema**

Toda $A \in {\mathbb{C}}^{m \times n},\ (m \geq n)$ tem uma fatoração QR completa, portanto também uma fatoração QR reduzida

**Demonstração**

Se rank$(A) = n$, podemos construir a fatoração reduzida usando Gram-Schmidt como fizemos antes. O único problema aqui é se, em algum momento, $v_{j} = a_{j} - \sum_{k = 1}^{j - 1}q_{k}q_{k}^{\ast}a_{j} = 0$ e, portanto, não pode ser normalizado. Se isso acontecer, significa que $A$ não tem posto completo, o que significa que posso escolher qualquer vetor ortogonal que quiser para continuar o processo.

**Teorema**

Cada $A \in {\mathbb{C}}^{m \times n}\ (m \geq n)$ de posto completo tem uma fatoração QR reduzida única $A = \widehat{Q}\widehat{R}$ com $r_{jj} > 0$

**Demonstração**

Sabemos que, se $A$ é de posto completo $\Rightarrow r_{jj} \neq 0$ e, portanto, em cada passo sucessivo $j$, as fórmulas mostradas anteriormente determinam $r_{ij}$ e $q_{j}$ completamente, o único problema é o sinal de $r_{jj}$, uma vez que dizemos $r_{jj} > 0$, esse problema é resolvido

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Ortonormalização de Gram-Schmidt](../ortonormalizacao-de-gram-schmidt/index.md)
- Próximo: [Ortonormalização de Gram-Schmidt](../../ortonormalizacao-de-gram-schmidt/index.md)
