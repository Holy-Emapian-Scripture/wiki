---
layout: "default"
title: "Conexao com a Iteração Reversa — Algoritmo QR com Shifts"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 50
---

[Álgebra Linear Numérica](../../index.md) · [Algoritmo QR com Shifts](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-50"></a>

# Conexao com a Iteração Reversa

A gente tinha visto que o algoritmo QR unshifted ([\[unshifted-qr-algorithm\]](../../algoritmo-qr-sem-shift/iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md#unshifted-qr-algorithm)) era a mesma coisa que aplicar a iteração reversa na matriz identidade. Tem um porém, o [\[unshifted-qr-algorithm\]](../../algoritmo-qr-sem-shift/iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md#unshifted-qr-algorithm) também é equivalente a aplicar a iteração inversa simultânea numa matriz identidade “invertida” P. Vamo tentar desenvolver melhor essa ideia:

Seja $Q^{(k)}$, assim como na última lecture, o fator ortogonal no $k$-ésimo passo da iteração do algoritmo QR. Mostramos antes que o produto acumulado dessas matrizes forma: $${\underline{Q}}^{(k)} = \prod_{j = 1}^{k}Q^{(j)} = \begin{pmatrix} q_{1}^{(k)} & \vert  & \ldots & \vert  & q_{m}^{(k)} \end{pmatrix}$$

É a mesma matriz ortogonal que aparece no $k$-ésimo passo do algoritmo de iteração simultânea. $$A^{k} = {\underline{Q}}^{(k)}{\underline{R}}^{(k)}$$

Se a gente inverte essa fórmula, temos $$A^{- k} = \left( {\underline{R}}^{(k)} \right)^{- 1}\left( {\underline{Q}}^{(k)} \right)^{T} = {\underline{Q}}^{(k)}\left( {\underline{R}}^{(k)} \right)^{- T}$$

Essa segunda igualdade a gente tira porque $A^{- 1}$ é simétrica (Ainda tamo usando que $A$ é simétrica). Deixe $P$ ser a matriz de permutação que troca a ordem de todas as linhas e colunas: $$P = \begin{pmatrix} & & & 1 \\ & & ⋰ \\ & 1 \\ 1 \end{pmatrix}$$

Bem, como $P^{2} = I$, a gente pode reescrever a equação que tinhamos anteriormente como: $$A^{- k}P = \left( {\underline{Q}}^{(k)}P \right)\left( {P\left( {\underline{R}}^{(k)} \right)}^{- T}P \right)$$

Perceba que ${\underline{Q}}^{(k)}P$ é ortogonal (${\underline{Q}}^{(k)}$ é ortogonal e $P$ também) e ${P\left( {\underline{R}}^{(k)} \right)}^{- T}P$ é triangular superior ($\left( {\underline{R}}^{(k)} \right)^{- T}$ é triangular inferior, daí eu inverto a ordem das colunas, e depois a ordem das linhas, aí fica triangular superior), ou seja, a equação anterior pode ser interpretada como uma fatoração QR de $A^{- k}P$. Isso que fizemos é a mesma coisa que aplicar o agloritmo QR na matriz $A^{- 1}$ usando a matriz $P$ como ponto de partida do algoritmo.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Algoritmo QR com Shifts](../index.md)
- Próximo: [Conexão com o Algoritmo de Iteração Reversa com Shifts](../conexao-com-o-algoritmo-de-iteracao-reversa-com-shifts/index.md)
