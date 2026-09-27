---
layout: "default"
title: "O Algoritmo — Triangularização de Householder"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 32
---

[Álgebra Linear Numérica](../../index.md) · [Triangularização de Householder](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-32"></a>

# O Algoritmo

Agora podemos reescrevê-lo como um algoritmo, mas antes disso:

**Definição**

Dada a matriz $A$, $A_{i:i',j:j'}$ é a submatriz $(i' - i + 1) \times (j' - j + 1)$ de $A$ com o elemento do canto superior esquerdo igual a $(A)_{ij}$ e o elemento do canto inferior direito igual a $(A)_{i'j'}$. Se a submatriz for um vetor linha ou coluna, podemos escrevê-lo como $A_{i,j:j'}$ ou $A_{i:i',j}$

Dada essa definição, vamos reescrever o algoritmo

1.  **para** $k = 1$ **até** $n$

    1.  $x = A_{k:m,k}$

    2.  $v_{k} = \text{ sign}\left( x_{1} \right)\| x\| e_{1} + x$

    3.  $v_{k} = \frac{v_{k}}{\| v_{k}\|}$

    4.  $A_{k:m,k:n} = A_{k:m,k:n} - 2v_{k}\left( v_{k}^{\ast}A_{k:m,k:n} \right)$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [O Melhor de Dois Refletores](../o-melhor-de-dois-refletores/index.md)
- Próximo: [Aplicando na formação de Q](../aplicando-na-formacao-de-q/index.md)
