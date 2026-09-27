---
layout: "default"
title: "Conexão com o Algoritmo de Iteração Reversa com Shifts — Algoritmo QR com Shifts"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 51
---

[Álgebra Linear Numérica](../../index.md) · [Algoritmo QR com Shifts](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-51"></a>

# Conexão com o Algoritmo de Iteração Reversa com Shifts

Ok, a gente viu então que o algoritmo QR é tipo uma mistureba da iteração reversa e da iteração simultânea reversa. O negócio é que a gente viu em umas lectures anteriores que o último que mencionei pode ser melhorado com o uso de shifts ([\[shifted-qr-with-well-known-shifts\]](../../algoritmo-qr-sem-shift/o-algoritmo-qr/index.md#shifted-qr-with-well-known-shifts)). Isso é como inserir shifts nos dois algoritmos que comentei anterioremente. Vou escrever o algoritmo aqui novamente (Omiti a parte final de obter as submatrizes):

1.  **function** ShiftedQR($A \in {\mathbb{C}}^{m \times m}$) {

    1.  $\left( Q^{(0)} \right)^{T}A^{(0)}Q^{(0)} = A$

    2.  **for** $k = 1,2,3,\ldots$

        1.  Escolha um shift $\mu^{(k)}$

        2.  $Q^{(k)},R^{(k)} = \text{ qr}\left( A^{(k - 1)} - \mu^{(k)}I \right)$

        3.  $A^{(k)} = R^{(k)}Q^{(k)} + \mu^{(k)}I$

        4.  …

2.  }

Deixe que $\mu^{(k)}$ seja a aproximação de autovalor que a gente escolhe no $k$-ésimo passo do algoritmo QR. De acordo com o [\[shifted-qr-with-well-known-shifts\]](../../algoritmo-qr-sem-shift/o-algoritmo-qr/index.md#shifted-qr-with-well-known-shifts), a relação entre os passos $k - 1$ e $k$ do algoritmo é: $$\begin{array}{r} A^{(k - 1)} - \mu^{(k)}I = Q^{(k)}R^{(k)} \\ A^{(k)} = R^{(k)}Q^{(k)} + \mu^{(k)}I \end{array}$$

Isso nos dá o seguinte (Só fazer umas substituições): $$A^{(k)} = \left( Q^{(k)} \right)^{T}A^{(k - 1)}Q^{(k)}$$

Aí se a gente aplica uma indução, temos: $$A^{(k)} = \left( {\underline{Q}}^{(k)} \right)^{T}A{\underline{Q}}^{(k)}$$

Se você para pra olhar, é a mesma coisa que a gente definiu no [\[unshifted-qr-and-sumultanious-iteration-equivalence\]](../../algoritmo-qr-sem-shift/iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md#unshifted-qr-and-sumultanious-iteration-equivalence) (Segunda equação). O problema é que a primeira equação não vale mais, ela vai ser substituida por: $$\prod_{j = k}^{1}\left( A - \mu^{(j)}I \right) = {\underline{Q}}^{(k)}{\underline{R}}^{(k)}$$

Aí a gente não precisa entrar em detalhes da prova dessa equivalência. Isso acarreta que as colunas de ${\underline{Q}}^{(k)}$ aos poucos vão convergindo para autovetores de A. O livro da uma ênfase na primeira e na última coluna, onde cada uma é equivalente a apliar o algoritmo da iteração reversa com shifts nos vetores canônicos $e_{1}$ e $e_{m}$ respectivamente.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Conexao com a Iteração Reversa](../conexao-com-a-iteracao-reversa/index.md)
- Próximo: [Conexão com a Iteração do Quociente de Rayleigh](../conexao-com-a-iteracao-do-quociente-de-rayleigh/index.md)
