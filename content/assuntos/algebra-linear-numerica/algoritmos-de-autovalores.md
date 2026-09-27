---
layout: "default"
title: "Algoritmos de Autovalores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 27
---

[Álgebra Linear Numérica](index.md)

<!-- wiki:original:inicio -->

<a id="secao-27"></a>

# Algoritmos de Autovalores


<a id="algoritmos-obvios-ou-nem-tanto"></a>
<a id="secao-28"></a>

## Algoritmos óbvios (Ou nem tanto)

Por mais que os autovetores e autovalores tenham propriedades bonitas e simples, calcular eles de uma maneira numericamente estável não é algo tão simples e os algoritmos não são os mais óbvios. O mais óbvio que pensamos é calcular o polinômio característico da matriz e achar suas raízes, acontece que isso é uma péssima ideia, já que achar as raízes de um polinômio é um problema mal-condicionado.

Agora a gente pode tirar vantagem do fato que a sequência $$\frac{x}{\| x\|},\frac{Ax}{\| Ax\|},\frac{A^{2}x}{\| A^{2}x\|},\ldots,\frac{A^{n}x}{\| A^{n}x\|}$$ converge, sobre certas condições, para o maior autovalor (Em valor absoluto) de $A$. Esse método é chamado de **Iteração sob Potências**, mas não é um método muito eficiente e não é utilizado em situações muito usuais.

Ao invés dessas ideias, é mais comum, para propósitos gerais, os algoritmos seguirem um princípio diferente: A computação de uma fatoração explícita de autovalores de $A$, onde um dos fatores da fatoração tem os autovalores de $A$ como entradas. A gente viu 3 desses métodos na última lecture (Diagonalização, Diagonalização Unitária e Fatoração de Schur). Na prática, os algoritmos vão aplicando transformações em $A$ de forma que eles inserem 0 nas colunas e entradas corretas (Tipo o que a gente viu no método de Householder)

<a id="uma-dificuldade-fundamental"></a>
<a id="secao-29"></a>

## Uma dificuldade fundamental

Acontece que **todo algoritmo para calcular autovalores deve ser iterativo**. Ué, por quê? Lembra que problemas de autovalores podem ser reduzidos a problemas de achar as raízes de um polinômio? Pois é, o inverso também é válido. O livro mostra isso criando um polinômio e expressando ele como o determinante de uma matriz e que as raízes do polinômio são os **autovalores** dessa matriz, mas isso não é o foco aqui. O foco é fazer a associação.

É bem conhecido o fato de que, para polinômios com grau maior ou igual a 5, não existe uma sequência de fórmulas com somas, subtrações, etc. (Fórmula fechada) que encontre suas raízes. O que isso quer dizer? Quer dizer que, se o problema de raízes de polinômios pode ser reduzido para um problema de autovalores, matrizes com dimensão maior ou igual a 5 não podem ter seus autovalores expressos em uma sequência finita de passos.

Por issos que os algoritmos de autovalores devem ser algoritmos iterativos que **convergem** para a solução

<a id="fatoracao-e-diagonalizacao-de-schur"></a>
<a id="secao-30"></a>

## Fatoração e Diagonalização de Schur

A maioria dos algoritmos de fatoração atuais envolvem o uso da fatoração de Schur de uma matriz. A gente pega a matriz $A$ e vai aplicando transformações nela com matrizes unitárias $Q_{j}$ (Transformação $X \mapsto Q_{j}^{\ast}XQ_{j}$) de forma que o produto: $$Q_{j}^{\ast}\ldots Q_{2}^{\ast}Q_{1}^{\ast}AQ_{1}Q_{2}\ldots Q_{j}$$<a id="upper-triangular-transformation"></a> Converja para uma matriz triangular superior $T$ conforme $j \rightarrow \infty$

O livro fala também que é possível utilizar de alguns truques para computar os autovalores complexos e que os algoritmos que veremos também podem ser usados, em matrizes Hermitianas, para obter sua diagonalização unitária.

<a id="duas-fases-da-computacao-de-autovalores"></a>
<a id="secao-31"></a>

## Duas fases da computação de Autovalores

A sendo Hermitiana ou não, a gente separa a sequência [\[upper-triangular-transformation\]](../fatoracao-e-diagonalizacao-de-schur/index.md#upper-triangular-transformation) em duas partes.

1.  A primeira fase consiste em produzir diretamente uma matriz **upper-Hessenberg**, isto é, uma matriz com zeros em baixo da primeira subdiagonal

2.  Uma iteração é aplicada para que uma sequência formal de matrizes de Hessenberg converjam para uma matriz triangular superior. O processo se parece com isso:

$$
\underset{A \neq A^{\ast}}{\underbrace{\begin{pmatrix} \times & \times & \times & \times & \times \\ \times & \times & \times & \times & \times \\ \times & \times & \times & \times & \times \\ \times & \times & \times & \times & \times \\ \times & \times & \times & \times & \times \end{pmatrix}}} \rightarrow \underset{H}{\underbrace{\begin{pmatrix} \times & \times & \times & \times & \times \\ \times & \times & \times & \times & \times \\ & \times & \times & \times & \times \\ & & \times & \times & \times \\ & & & \times & \times \end{pmatrix}}} \rightarrow \underset{T}{\underbrace{\begin{pmatrix} \times & \times & \times & \times & \times \\ & \times & \times & \times & \times \\ & & \times & \times & \times \\ & & & \times & \times \\ & & & & \times \end{pmatrix}}}
$$

Se $A$ é hermitiana, isso fica ainda mais rápido já que vamos ter uma matriz tri-diagonal e, logo depois, uma diagonal

$$
\underset{A = A^{\ast}}{\underbrace{\begin{pmatrix} \times & \times & \times & \times & \times \\ \times & \times & \times & \times & \times \\ \times & \times & \times & \times & \times \\ \times & \times & \times & \times & \times \\ \times & \times & \times & \times & \times \end{pmatrix}}} \rightarrow \underset{H}{\underbrace{\begin{pmatrix} \times & \times & & & \\ \times & \times & \times & & \\ & \times & \times & \times & \\ & & \times & \times & \times \\ & & & \times & \times \end{pmatrix}}} \rightarrow \underset{T}{\underbrace{\begin{pmatrix} \times & & & & \\ & \times & & & \\ & & \times & & \\ & & & \times & \\ & & & & \times \end{pmatrix}}}
$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Problemas de Autovalores](problemas-de-autovalores.md)
- Próximo: [Redução à forma de Hessenberg](reducao-a-forma-de-hessenberg.md)
