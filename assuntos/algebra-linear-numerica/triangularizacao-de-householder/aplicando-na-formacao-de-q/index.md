---
layout: "default"
title: "Aplicando na formação de Q — Triangularização de Householder"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 33
---

[Álgebra Linear Numérica](../../index.md) · [Triangularização de Householder](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-33"></a>

# Aplicando na formação de Q

Observe que não construímos a matriz $Q$ inteira no algoritmo, apenas aplicamos: $$Q^{\ast} = Q_{n}\ldots Q_{1} \Leftrightarrow Q = Q_{1.}..Q_{n}$$ (Não há asteriscos faltando, porque cada $Q_{j}$ é hermitiana!)

Fazemos isso porque construir $Q$ requer trabalho extra, então trabalhamos diretamente com $Q_{j}$. Por exemplo, lembra que podemos reescrever $b = Ax$ como $Q^{\ast}b = Rx$? Bem, podemos fazer isso como no algoritmo anterior:

1.  **para** $k = 1$ **até** $n$

    1.  $b_{k:m} = b_{k:m} - 2v_{k}\left( v_{k}^{\ast}b_{k:m} \right)$

Observe que fizemos o mesmo processo que fizemos com $A$, só não explicitei as partes onde defini $v_{k}$ e o normalizei.

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [O Algoritmo](../o-algoritmo/index.md)
- Próximo: [Problemas de Mínimos Quadrados](../../problemas-de-minimos-quadrados/index.md)
