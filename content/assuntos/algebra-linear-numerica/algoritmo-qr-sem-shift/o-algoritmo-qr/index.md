---
layout: "default"
title: "O Algoritmo QR — Algoritmo QR sem Shift"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 44
---

[Álgebra Linear Numérica](../../index.md) · [Algoritmo QR sem Shift](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-44"></a>

# O Algoritmo QR

A versão mais simplificada parece coisa de doido.

<a id="iteration-qr"></a>

1.  **function** QRIteration($A \in {\mathbb{C}}^{m \times m}$) {

    1.  $A^{(0)} = A$

    2.  **for** $k = 1,2,3,\ldots$

        1.  $Q^{(k)},R^{(k)} = \text{ qr}\left( A^{(k - 1)} \right)$

        2.  $A^{(k)} = R^{(k)}Q^{(k)}$

2.  }

*Figura 13. Algoritmo QR*

É um algoritmo estupidamente simples, mas sobre certas circunstâncias, esse algoritmo converge para a forma de Schur de uma matriz (Triangular superior se for arbitrária e diagonal se for simétrica). Por questão de simplicidade, vamos continuar assumindo que $A$ é simétrica

Pra que a redução a forma diagonal seja útil pra achar autovalor, a gente precisa que transformações similares estejam envolvidas. “Oxe, daonde?”. Quando a gente faz $A^{(k)} = R^{(k)}Q^{(k)}$, a gente pode substituir $R^{(k)}$ por $\left( Q^{(k)} \right)^{T}A^{(k - 1)}$, ou seja: $A^{(k)} = \left( Q^{(k)} \right)^{T}A^{(k - 1)}Q^{(k)}$ (Mesmo que $M^{- 1}AM$). O [\[iteration-qr\]](#iteration-qr) converge cubicamente assim como o do [\[rayleigh-quotient-iteration\]](../../quociente-de-rayleigh-e-iteracao-inversa/iteracao-do-quociente-de-rayleigh/index.md#rayleigh-quotient-iteration), porém, para o algoritmo ser prático, precisamos introduzir **shifts**. Introdução de **shifts** é 1 de 3 modificações que fazemos nesse algoritmo para que ele fique prático.

1.  Antes de iniciar a iteração, $A$ é reduzida a forma tridiagonal

2.  Em vez de $A^{(k)}$, usamos uma matriz trocada $A^{(k)} - \mu^{(k)}I$ que é fatorada a cada iteração e $\mu^{(k)}$ é uma estimativa de autovalor

3.  Quando possível (Especialmente quando um autovalor é encontrado) nós quebramos $A^{(k)}$ em submatrizes

<a id="shifted-qr-with-well-known-shifts"></a>

1.  **function** ShiftedQR($A \in {\mathbb{C}}^{m \times m}$) {

    1.  $\left( Q^{(0)} \right)^{T}A^{(0)}Q^{(0)} = A$

    2.  **for** $k = 1,2,3,\ldots$

        1.  Escolha um shift $\mu^{(k)}$

        2.  $Q^{(k)},R^{(k)} = \text{ qr}\left( A^{(k - 1)} - \mu^{(k)}I \right)$

        3.  $A^{(k)} = R^{(k)}Q^{(k)} + \mu^{(k)}I$

        4.  **Se** qualquer elemento $A_{j,j + 1}^{(k)}$ fora da diagonal é suficientemente próximo de 0

            1.  $A_{j,j + 1} = A_{j + 1,j} = 0$ para obter

            2.  $\begin{pmatrix} A_{1} & 0 \\ 0 & A_{2} \end{pmatrix} = A^{(k)}$

            3.  e agora aplicamos o algoritmo em $A_{1}$ e $A_{2}$

2.  }

*Figura 14. Algoritmo QR com **shifts***

Esse é um algoritmo muito usado desde 1960. Mas perceba que precisamos ter uma noção prévia de quanto vale os autovalores da matriz, pois necessitamos ter aproximações particularmente boas de $\mu^{(k)}$ para que o algoritmo tenha uma boa convergência.Porém, nos anos 1990 um competidor surgiu (Vai ser discutido na lecture 30 e a gente detalha o algoritmo com shifts na próxima lecture).

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Algoritmo QR sem Shift](../index.md)
- Próximo: [Iterações Simultâneas Não-normalizadas](../iteracoes-simultaneas-nao-normalizadas/index.md)
