---
layout: "default"
title: "Iteração Simultânea $\\Leftrightarrow$ Algoritmo QR — Algoritmo QR sem Shift"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 47
---

[Álgebra Linear Numérica](../../index.md) · [Algoritmo QR sem Shift](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-47"></a>

# Iteração Simultânea $\Leftrightarrow$ Algoritmo QR

Beleza, agora a gente pode tentar entender o algoritmo QR (Não é um algoritmo pra calcular a fatoração QR, mas usa ela para calcular os autovalores e autovetores de A). A gente vai aplicar a iteração simultânea na identidade, assim, a gente até remove os acentos de ${\hat{Q}}^{(k)}$ e ${\hat{R}}^{(k)}$. A gente vai fazer umas substituições que eu vou explicar direitinho depois.

Primeiro de tudos, temos um algoritmo de iteração simultânea com uma leve adaptação, mostraremos que ele e o algoritmo qr são equivalentes

<a id="modified-simultanious-iteration"></a>

1.  **function** ModifiedSimultaniousAlgorithm($A \in {\mathbb{C}}^{m \times m}$) {

    1.  ${\underline{Q}}^{(0)} = I$

    2.  **for** $k = 1,2,3,\ldots$

        1.  $Z = A{\underline{Q}}^{(k - 1)}$

        2.  ${\underline{Q}}^{(k)},R^{(k)} = \text{ qr}(Z)$

        3.  $A^{(k)} = \left( {\underline{Q}}^{(k)} \right)^{T}A{\underline{Q}}^{(k)}$

        4.  ${\underline{R}}^{(k)} = R^{(k)}R^{(k - 1)}\ldots R^{(1)}$

2.  }

*Figura 16. Iteração Simultânea Modificada*

Aqui, a gente colocou ${\underline{Q}}^{(k)}$ com esse traço em baixo só pra diferenciar o $Q$ do algoritmo de iteração simultânea e do algoritmo QR

<a id="unshifted-qr-algorithm"></a>

1.  **function** UnshiftedQRAlgorithm($A \in {\mathbb{C}}^{m \times m}$) {

    1.  $A^{(0)} = A$

    2.  **for** $k = 1,2,3,\ldots$

        1.  $Q^{(k)},R^{(k)} = \text{ qr}\left( A^{(k - 1)} \right)$

        2.  $A^{(k)} = R^{(k)}Q^{(k)}$

        3.  ${\underline{Q}}^{(k)} = Q^{(1)}Q^{(2)}\ldots Q^{(k)}$

        4.  ${\underline{R}}^{(k)} = R^{(k)}R^{(k - 1)}\ldots R^{(1)}$

2.  }

*Figura 17. Algoritmo QR sem Shift*

Agora podemos visualizar a convergência de ambos os algoritmos.

<a id="unshifted-qr-and-sumultanious-iteration-equivalence"></a>

**Teorema**

O [\[modified-simultanious-iteration\]](#modified-simultanious-iteration) e [\[unshifted-qr-algorithm\]](#unshifted-qr-algorithm) geram a mesma sequência de matrizes ${\underline{Q}}^{(k)}$, ${\underline{R}}^{(k)}$ e $A^{(k)}$, de tal forma que: $$A^{k} = {\underline{Q}}^{(k)}{\underline{R}}^{(k)}$$<a id="unshifted-qr-eigenvectors-estimative"></a> junto da projeção $$A^{(k)} = \left( {\underline{Q}}^{(k)} \right)^{T}A{\underline{Q}}^{(k)}$$<a id="unshifted-qr-eigenvalues-estimative"></a>

**Demonstração**

Vamos fazer indução em $k$

- Caso base ($k = 1$): Trivial, já que $A^{(0)} = {\underline{Q}}^{(0)} = {\underline{R}}^{(0)} = I$ e $A^{(0)} = A$

- Passo indutivo ($k > 1$): A parte de que $A^{(k)} = \left( {\underline{Q}}^{(k)} \right)^{T}A{\underline{Q}}^{(k)}$ por definição de $A^{k}$ ([\[modified-simultanious-iteration\]](#modified-simultanious-iteration)). Então só precisamos conferir que $A^{k} = {\underline{Q}}^{(k)}{\underline{R}}^{(k)}$, e fazemos isso, primeiro, considerando o algoritmo de iteração simultânea (Assumindo que isso é válido para $A^{k - 1}$): $$A^{k} = A{\underline{Q}}^{(k - 1)}{\underline{R}}^{(k - 1)} = {\underline{Q}}^{(k)}R^{(k)}{\underline{R}}^{(k - 1)} = {\underline{Q}}^{(k)}{\underline{R}}^{(k)}$$ Agora, faremos o mesmo assumindo o algoritmo QR $$A^{k} = A{\underline{Q}}^{(k - 1)}{\underline{R}}^{(k - 1)} = {\underline{Q}}^{(k - 1)}A^{(k - 1)}{\underline{R}}^{(k - 1)} = {\underline{Q}}^{(k)}{\underline{R}}^{(k)}$$ Então verificamos que $$A^{(k)} = \left( Q^{(k)} \right)^{T}A^{(k - 1)}Q^{(k)} = \left( {\underline{Q}}^{(k)} \right)^{T}A{\underline{Q}}^{(k)}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Iteração Simultânea](../iteracao-simultanea/index.md)
- Próximo: [Convergência do algoritmo QR](../convergencia-do-algoritmo-qr/index.md)
