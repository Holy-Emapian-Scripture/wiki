---
layout: "default"
title: "Algoritmos óbvios (Ou nem tanto) — Algoritmos de Autovalores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 28
---

[Álgebra Linear Numérica](../../index.md) · [Algoritmos de Autovalores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-28"></a>

# Algoritmos óbvios (Ou nem tanto)

Por mais que os autovetores e autovalores tenham propriedades bonitas e simples, calcular eles de uma maneira numericamente estável não é algo tão simples e os algoritmos não são os mais óbvios. O mais óbvio que pensamos é calcular o polinômio característico da matriz e achar suas raízes, acontece que isso é uma péssima ideia, já que achar as raízes de um polinômio é um problema mal-condicionado.

Agora a gente pode tirar vantagem do fato que a sequência $$\frac{x}{\| x\|},\frac{Ax}{\| Ax\|},\frac{A^{2}x}{\| A^{2}x\|},\ldots,\frac{A^{n}x}{\| A^{n}x\|}$$ converge, sobre certas condições, para o maior autovalor (Em valor absoluto) de $A$. Esse método é chamado de **Iteração sob Potências**, mas não é um método muito eficiente e não é utilizado em situações muito usuais.

Ao invés dessas ideias, é mais comum, para propósitos gerais, os algoritmos seguirem um princípio diferente: A computação de uma fatoração explícita de autovalores de $A$, onde um dos fatores da fatoração tem os autovalores de $A$ como entradas. A gente viu 3 desses métodos na última lecture (Diagonalização, Diagonalização Unitária e Fatoração de Schur). Na prática, os algoritmos vão aplicando transformações em $A$ de forma que eles inserem 0 nas colunas e entradas corretas (Tipo o que a gente viu no método de Householder)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Algoritmos de Autovalores](../index.md)
- Próximo: [Uma dificuldade fundamental](../uma-dificuldade-fundamental/index.md)
