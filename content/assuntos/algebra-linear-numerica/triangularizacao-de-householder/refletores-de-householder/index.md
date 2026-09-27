---
layout: "default"
title: "Refletores de Householder — Triangularização de Householder"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 30
---

[Álgebra Linear Numérica](../../index.md) · [Triangularização de Householder](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-30"></a>

# Refletores de Householder

Ok, entendemos como o algoritmo vai funcionar, mas que tipo de matrizes pode fazer tal coisa? É aqui que entram em cena os **refletores de Householder**! Cada $Q_{k}$ terá esta estrutura: $$Q_{k} = \begin{pmatrix} I & 0 \\ 0 & F \end{pmatrix}$$ Onde $I$ é a matriz identidade de tamanho $k - 1 \times k - 1$ e $F$ é uma matriz unitária $m - k + 1 \times m - k + 1$. Mas por que essa estrutura, onde vimos isso? Bem, lembre-se que, como vimos antes, quando multiplicamos $Q_{k - 1}\ldots Q_{1}A$ por $Q_{k}$, queremos manter as linhas $1$ a $k - 1$ intocadas, então, para fazer isso, criamos uma matriz bloco $k - 1 \times k - 1$ da identidade para manter essas linhas intocadas.

E por que $F$ é uma matriz unitária? Bem, sabemos que, por causa dos zeros abaixo de $I$ e acima de $F$, as colunas de $F$ serão ortogonais às colunas de $I$ independentemente do que eu colocar ali, mas queremos que $Q_{k}$ seja ortogonal, então, se as colunas de $I$ já são ortonormais, só precisamos que as colunas de $F$ também sejam ortonormais, ou seja, $F$ deve ser ortogonal.

Ok, mas agora a parte mais difícil, precisamos que, quando multiplicarmos por $F$, ela introduza zeros abaixo da $k$-ésima entrada da diagonal e ainda seja ortogonal. Vamos fazer $F$ estar em ${\mathbb{C}}^{m - k + 1 \times m - k + 1}$ e afetar vetores de ${\mathbb{C}}^{m - k + 1}$ (podemos ver as linhas abaixo das $k$-ésimas entradas de vetores desse espaço), então queremos que a primeira entrada dos vetores seja diferente de 0 e o resto seja 0, sabendo que matrizes ortogonais são rotações em um espaço, podemos fazer $F$ fazer isso:

$$x = \begin{pmatrix} x \\ x \\ x \\ \vdots \\ x \end{pmatrix} \rightarrow Fx = \begin{pmatrix} \| x\| \\ 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} = \| x\| e_{1}$$

Como mostrado nesta figura: ![](../../assets/Householder_Reflector.jpg)

Observe que projetar $v$ para obter $\| v\| e_{1}$ não nos dará uma projeção ortogonal, mas podemos projetá-lo na linha azul, que é a bissetriz do ângulo entre $v$ e $\| v\| e_{1}$. Essa bissetriz forma um ângulo de 90 graus com $\| v\| e_{1} - v$. Este é um plano 2D, então é a bissetriz do ângulo, mas em um espaço de dimensão maior, será um hiperplano ortogonal a $\| v\| e_{1} - v$. Vamos definir $w = \| v\| e_{1} - v$, então, se $H$ é o hiperplano ortogonal a $w$, podemos projetar $v$ sobre $H$ fazendo:

$$Pv = I - \frac{ww^{\ast}}{w^{\ast}w}v$$

Mas, como podemos ver, se projetarmos $v$ sobre $H$, para chegar a $\| v\| e_{1}$, precisamos percorrer duas vezes a distância que acabamos de percorrer, então, a equação final para o refletor de Householder é:

$$F = I - 2\frac{ww^{\ast}}{w^{\ast}w}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Triangularização por Introdução de Zeros](../triangularizacao-por-introducao-de-zeros/index.md)
- Próximo: [O Melhor de Dois Refletores](../o-melhor-de-dois-refletores/index.md)
