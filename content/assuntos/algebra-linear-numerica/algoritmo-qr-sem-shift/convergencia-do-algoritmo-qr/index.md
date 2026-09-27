---
layout: "default"
title: "Convergência do algoritmo QR — Algoritmo QR sem Shift"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 48
---

[Álgebra Linear Numérica](../../index.md) · [Algoritmo QR sem Shift](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-48"></a>

# Convergência do algoritmo QR

Show, agora a gente pode entender melhor como que esse algoritmo acha os autovalores e autovetores. A parte dos autovetores a gente consegue visualizara pela equação [\[unshifted-qr-eigenvectors-estimative\]](../iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md#unshifted-qr-eigenvectors-estimative), e pelo [\[unshifted-qr-and-sumultanious-iteration-equivalence\]](../iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md#unshifted-qr-and-sumultanious-iteration-equivalence), já que, se o método de iteração simultânea converge para autovetores e tanto ele quanto o algoritmo QR geram as mesmas matrizes, obviamente ambos vão ter as matrizes $Q$ convergindo para a matriz de colunas sendo os autovetores. Como $Q$ converge pra matriz de autovetores, por consequência, se eu faço $Q^{T}AQ$, isso vai convergir pra matriz com os autovalores de $A$ na diagonal (Diagonalização)

**Teorema**

Deixe que o [\[unshifted-qr-algorithm\]](../iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md#unshifted-qr-algorithm) seja aplicado em uma matriz real simétrica $A$ que os autovalores satisfazem $\vert \lambda_{1}\vert  > \vert \lambda_{2}\vert  > \ldots > \vert \lambda_{m}\vert$ e que a matriz de autovetores correspondente $Q$ não tem blocos singulares (Todos os blocos da matriz formam matrizes inversíveis). Então, conforme $k \rightarrow \infty$, $A^{(k)}$ converge linearmente com constante $\max\limits_{j\left( \vert \lambda_{j + 1}\vert /\vert \lambda_{j}\vert  \right)}$ para a matriz com os autovalores na diagonal e $Q^{(k)}$ converge na mesma velocidade para $Q$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Iteração Simultânea $\Leftrightarrow$ Algoritmo QR](../iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md)
- Próximo: [Algoritmo QR com Shifts](../../algoritmo-qr-com-shifts/index.md)
