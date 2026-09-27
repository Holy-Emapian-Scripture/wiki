---
layout: "default"
title: "Normas de matrizes — Normas"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 3
---

[Álgebra Linear Numérica](../../index.md) · [Normas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-3"></a>

# Normas de matrizes

O QUÊ?? MATRIZES TÊM NORMAS???? Sim, meu jovem Padawan! O livro diz que podemos ver uma matriz como um vetor em um espaço $m \times n$, e podemos usar qualquer norma $mn$ para medi-la, mas algumas normas são mais úteis do que as já discutidas.

**Definição: Norma induzida**

Dada $A \in {\mathbb{C}}^{m \times n}$, a norma induzida $\| A\|_{m \rightarrow n}$ é o menor inteiro para o qual a desigualdade é válida:

$\| Ax\|_{m} \leq C\| x\|_{n}$

Em outras palavras:

$\| A\|_{m \rightarrow n} = \sup\limits_{x \neq 0}\frac{\| Ax\|_{m}}{\| x\|_{n}}$

Essa definição pode parecer inútil e estúpida por enquanto, mas será muito útil quando falarmos sobre erros e condicionamento.

Uma norma útil que podemos mencionar é a norma $\infty$ de uma matriz.

**Definição: Norma infinita de uma matriz**

Dada $A \in {\mathbb{C}}^{m \times n}$, se $a_{j}$ é a $j^{th}$ linha de $A$, $\| A\|_{\infty}$ é definida por:

$\| A\|_{\infty} = \max\limits_{1 \leq i \leq m}\| a_{i}\|_{1}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Normas de vetores](../normas-de-vetores/index.md)
- Próximo: [Desigualdades de Cauchy-Schwarz e Hölder](../desigualdades-de-cauchy-schwarz-e-holder/index.md)
