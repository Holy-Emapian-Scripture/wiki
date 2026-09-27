---
layout: "default"
title: "Problemas de Autovalores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 16
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-16"></a>

# Problemas de Autovalores


<a id="definicoes"></a>
<a id="secao-17"></a>

## Definições

Dada uma matriz $A \in {\mathbb{C}}^{m \times n}$, pela decomposição SVD $A = U\Sigma V^{\ast}$ sabemos que $A$ é uma transformação que **estica** e **rotaciona** vetores. Por isso, estamos interessados em subespaços de ${\mathbb{C}}^{m}$ nos quais a matriz age como uma multiplicação escalar, ou seja, estamos interessados nos $x \in {\mathbb{C}}^{n}$ que são somente esticados pela matriz. Como $Ax \in {\mathbb{C}}^{m}$ e $\lambda x \in {\mathbb{C}}^{n}$, concluimos que $m = n$: A matriz **deve ser quadrada**. Afinal, não faz sentido se $\lambda x$ e $Ax$ estiverem em conjuntos distintos. Com isso, prosseguimos com a definição:

**Definição: Autovalores e Autovetores**

Dada $A \in {\mathbb{C}}^{m \times m}$, um **autovetor** de $A$ é $x \in {\mathbb{C}}^{m} \smallsetminus \left\{ 0 \right\}$ que satisfaz:

$$Ax = \lambda x$$ <a id="eq_autovalores_autovetores"></a>

$\lambda \in {\mathbb{C}}$ é dito **autovalor** associado a $x$.

<a id="def_autovalor_autovetor"></a>

<a id="decomposicao-em-autovalores"></a>
<a id="secao-18"></a>

## Decomposição em Autovalores

Uma **decomposição em autovalores** de uma matriz $A \in {\mathbb{C}}^{m \times n}$ é uma fatoração:

$$A = X\Lambda X^{- 1}$$ <a id="decomposicao_autovalores"></a>

Onde $\Lambda$ é diagonal e $\det(X) \neq 0$.

Isso é equivalente a:

$$\underset{A}{\underbrace{\begin{pmatrix} \  & \  & \  & \  \\ \  & \  & A & \  & \  \\ \  & \  & \  & \ \end{pmatrix}}} \cdot \underset{X}{\underbrace{\begin{pmatrix} \vert  & \vert  & \vert  & \vert  & \\ x_{1} & x_{2} & \ldots & x_{n} \\ \vert  & \vert  & \vert  & \vert \end{pmatrix}}} = \underset{\Lambda}{\underbrace{\begin{pmatrix} \lambda_{1} & 0 & \ldots & 0 \\ 0 & \lambda_{2} & \ldots & 0 \\ 0 & 0 & \ldots & 0 \end{pmatrix}}} \cdot \underset{X}{\underbrace{\begin{pmatrix} \vert  & \vert  & \vert  & \vert  & \\ x_{1} & x_{2} & \ldots & x_{n} \\ \vert  & \vert  & \vert  & \vert \end{pmatrix}}}$$ <a id="eq_decomposicao_autovalores_matricial"></a>

Da [\[eq_decomposicao_autovalores_matricial\]](#eq_decomposicao_autovalores_matricial) e da [\[def_autovalor_autovetor\]](../definicoes/index.md#def_autovalor_autovetor), decorre que $Ax_{i} = \lambda_{i}x_{i}$, então a i-ésima coluna de $X$ é um autovetor de $A$ e $\lambda_{i}$ é o autovalor associado a $x_{i}$.

A decomposição apresentada pode representar uma mudança de base: Considere $Ax = b$ e $A = X\Lambda X^{- 1}$, então:

$$
Ax = b \Leftrightarrow X\Lambda X^{- 1}x = b \Leftrightarrow \Lambda\left( X^{- 1}x \right) = X^{- 1}b
$$

Então para calcular $Ax$, podemos expandir $x$ como combinação das colunas de $X$ e aplicar $\Lambda$. Como $\Lambda$ é diagonal, o resultado ainda vai ser uma combinação das colunas de $X$.

<a id="multiplicidades-algebrica-e-geometrica"></a>
<a id="secao-19"></a>

## Multiplicidades Algébrica e Geométrica

Como mencionado anteriormente, definimos os conjuntos nos quais a matriz atua como multiplicação escalar:

**Definição: Autoespaço**

Dada $A \in {\mathbb{C}}^{m \times n},\lambda \in {\mathbb{C}}$, definimos $S_{\lambda} \in {\mathbb{C}}^{m}$ como sendo o **autoespaço** gerado por todos os $v \in {\mathbb{C}}^{m}$ tais que $Av = \lambda v$

<a id="def_autoespaço"></a>

Interpretaremos $\dim(S_{\lambda})$ como a maior quantidade de autovetores L.I associados a um único $\lambda$, e chamaremos isso de *multiplicidade geométrica* de $\lambda$. Então temos:

**Definição**

(Multiplicidade Geométrica) A multiplicidade geométrica de $\lambda$ é $\dim(S_{\lambda})$

<a id="def_multiplicidade_geometrica"></a>

Note que da equação [\[eq_autovalores_autovetores\]](../definicoes/index.md#eq_autovalores_autovetores):

$$
Ax = \lambda x \Leftrightarrow Ax - \lambda x = 0 \Leftrightarrow (A - \lambda I)x = 0
$$

Mas como $x \neq 0$ e $x \in N(A - \lambda I)$, $(A - \lambda I)$ não é injetiva. Logo não é inversível:

$$\det(A - \lambda I) = 0$$ <a id="eq_polinimio_caracteristico"></a>

**Definição: Polinômio Característico**

A equação [\[eq_polinimio_caracteristico\]](#eq_polinimio_caracteristico) se chama **polinômio característico** de $A$ e é um polinômio de grau $m$ em $\lambda$. Pelo teorema fundamental da Álgebra, se $\lambda_{1},\ldots,\lambda_{n}$ são raízes de [\[eq_polinimio_caracteristico\]](#eq_polinimio_caracteristico), então podemos escrever isso como: $$p(\lambda) = \left( \lambda - \lambda_{1} \right)\left( \lambda - \lambda_{2} \right)\ldots\left( \lambda - \lambda_{n} \right)$$<a id="characteristical-polynomial"></a> (Nota: $\lambda$ é uma variável, enquanto $\lambda_{j}$ é uma raíz do polinômio, fique atento)

Com isso, prosseguimos com:

**Definição: Multiplicidade Algébrica**

A multiplicidade algébrica de $\lambda$ é a multiplicidade de $\lambda$ como raiz do polinômio característico de $A$

<a id="def_multiplicidade_algebrica"></a>

A definição de polinômio característico e de multiplicidade algébrica faz a gente ter um jeito muito fácil de contar a quantidade de autovalores de uma matriz

**Teorema**

Se $A \in {\mathbb{C}}^{m \times m}$, então $A$ tem $m$ autovalores, contando com a multiplicidade algébrica.

Isso mostra que **toda matriz** possui **pelo menos** 1 autovalor

<a id="transformacoes-similares"></a>
<a id="secao-20"></a>

## Transformações Similares

**Definição: Transformação Similar**

Se $X \in {\mathbb{C}}^{m \times m}$ é inversível, então o mapeamento $A \mapsto X^{- 1}AX$ é chamado de **transformação similar** de A.

Dizemos que duas matrizes $A$ e $B$ são **similares** se existe uma matriz inversível $X$ que relacione as transformações similares entre $A$ e $B$, i.e: $$A = X^{- 1}BX$$

<a id="similarity-theorem"></a>

**Teorema**

Se $A \in {\mathbb{C}}^{m \times m}$ é inversível, então $A$ e $X^{- 1}AX$ o mesmo polinômio característico, os mesmos autovalores e multiplicidades geométrica e algébrica.

**Demonstração**

$$
\begin{array}{r} p_{X^{- 1}AX}(z) = \det(zI - X^{- 1}AX) = \det(X^{- 1}(zI - A)X) \\ = \det(X^{- 1})\det(zI - A)\det(X) = \det(zI - A) = p_{A(z)}) \end{array}
$$

Suponha que $E_{\lambda}$ é o autoespaço de $A$, então $X^{- 1}E_{\lambda}$ é autoespaço de $X^{- 1}AX$, ou seja, ambos tem mesma multiplicidade geométrica

Agora podemos correlacionar a multiplicidade geométrica e a algébrica

**Teorema**

A multiplicidade algébrica de um autovalor $\lambda$ é sempre maior ou igual a sua multiplicidade geométrica

**Demonstração**

Deixe $n$ ser a multiplicidade gemétrica de $\lambda$ para a matriz $A$. Forme uma matriz $\hat{V} \in {\mathbb{C}}^{m \times n}$ de tal forma que as suas $n$ colunas formam uma base ortonormal do autoespaço $\left\{ x:Ax = \lambda x \right\}$. Se extendermos $\widetilde{V}$ para uma matriz ortogonal quadrada, temos: $$B = V^{\ast}AV = \begin{pmatrix} \lambda I & C \\ 0 & D \end{pmatrix}$$ Pela definição e propriedades do determinante (Não cabe mostrá-las aqui), temos que: $$\det(\mu I - B) = \det(\mu I - \lambda I)\det(\mu I - D) = (\mu - \lambda)^{n}\det(\mu I - D)$$ Ou seja, a multiplicidade algébrica de $\lambda$ como um autovalor de $B$ é, no mínimo, $B$. Como transformações similares mantém a multiplicidade, o mesmo vale para $A$

<a id="autovalores-e-matrizes-deficientes"></a>
<a id="secao-21"></a>

## Autovalores e Matrizes Deficientes

Um autovalor é deficiente quando sua MA é maior que sua MG. Se uma matriz $A$ tem autovalor deficiente, ela é uma matriz deficiente. Matrizes deficientes não podem ser diagonalizáveis (Próximo tópico)

<a id="diagonalizabilidade"></a>
<a id="secao-22"></a>

## Diagonalizabilidade

**Teorema: Diagonalizabilidade**

Uma matriz $A \in {\mathbb{C}}^{m \times m}$ é não-deficiente $\Leftrightarrow$ ela tem uma decomposição $A = X\Lambda X^{- 1}$

**Demonstração**

$\Leftarrow$) Dada uma decomposição $A = X\Lambda X^{- 1}$, sabemos, pelo [\[similarity-theorem\]](../transformacoes-similares/index.md#similarity-theorem), que $\Lambda$ sendo similar a $A$, logo, $A$ tem os mesmos autovalores, MA e MG de $\Lambda$. Como $\Lambda$ é diagonal, eu tenho que $\Lambda$ é não-deficiente, logo, o mesmo vale para $A$

$\Rightarrow$) Uma matriz não-deficiente deve ter $m$ autovetores linearmente independentes, pois autovetores com diferentes autovalores precisam ser L.I, e cada autovalor pode se associar com autovetores a quantidade de vezes que sua MA permitir. Se esses $m$ autovetores independentes formam as colunas de uma matriz $X$, então X é inversível e $A = X\Lambda X^{- 1}$

<a id="determinante-e-traco"></a>
<a id="secao-23"></a>

## Determinante e Traço

**Teorema**

Seja $\lambda_{j}$ um autovalor de $A \in {\mathbb{C}}^{m \times m}$: $$\begin{array}{r} \det(A) = \prod_{j = 1}^{m}\lambda_{j} \\ \operatorname{tr}(A) = \sum_{j = 1}^{m}\lambda_{j} \end{array}$$

**Demonstração**

$$\det(A) = ( - 1)^{m}\det( - A) = ( - 1)^{m}p_{A(0)} = \prod_{j = 1}^{m}\lambda_{j}$$ Olhando a equação [\[characteristical-polynomial\]](../multiplicidades-algebrica-e-geometrica/index.md#characteristical-polynomial), podemos observar que o coeficiente do termo $\lambda^{m - 1}$ é igual a $- \sum_{j = 1}^{m}\lambda_{j}$ e na equação [\[eq_polinimio_caracteristico\]](../multiplicidades-algebrica-e-geometrica/index.md#eq_polinimio_caracteristico) o termo é o negativo da soma dos termos da diagonal, ou seja, $- \operatorname{tr}(A)$, ou seja, $\operatorname{tr}(A) = \sum_{j = 1}^{m}\lambda_{j}$

<a id="diagonalizacao-unitaria"></a>
<a id="secao-24"></a>

## Diagonalização Unitária

Acontece as vezes que, ao fazer a diagonalização de uma matriz, nós podemos cair com um conjunto de autovetores ortogonais entre si.

**Definição**

$A$ é diagonalizável unitariamente quando $A = Q\Lambda Q^{\ast}$ com $Q$ ortogonal e $\Lambda$ diagonal (Pode ter entradas complexas)

**Teorema: Teorema Espectral**

Uma matriz hermitiana é diagonalizável unitariamente e seus autovalores são reais.

Não cabe aqui a prova desse teorema, porém um resumo de Álebra Linear do 2º período será feito e essa demonstração estará lá.

**Definição: Matrizes Normais**

Uma matriz $A$ é normal se $A^{\ast}A = AA^{\ast}$

**Teorema**

Uma matriz é diagonalizável unitariamente $\Leftrightarrow$ ela é normal

<a id="forma-de-schur"></a>
<a id="secao-25"></a>

## Forma de Schur

Essa forma é **muito útil** em análise numérica tendo em vista que **toda matriz quadrada** pode ser fatorada assim

**Definição: Fatoração de Schur**

Dada uma matriz $A \in {\mathbb{C}}^{m \times m}$, sua fatoração de schur é tal que: $$A = QTQ^{\ast}$$ onde $Q$ é ortogonal e $T$ é triangular superior

**Teorema**

Toda matriz quadrada $A$ tem uma fatoração de Schur

**Demonstração**

Vamos fazer indução em $m$.

- **Casos base**: $m = 1$ é trivial, então suponha que $m \geq 2$.

- **Passo Indutivo**: Deixe $x$ ser um autovetor de $A$ com autovalor $\lambda$. Normalize $x$ e faça com que seja a primeira coluna de uma matriz ortogonal $U$. Então podemos fazer as contas e conferir que o produto $U^{\ast}AU$ é tal que: $$U^{\ast}AU = \begin{pmatrix} \lambda & B \\ 0 & C \end{pmatrix}$$ Pela hipótese indutiva, existe uma fatoração $VTV^{\ast}$ de $C$, agora escrevemos: $$Q = U\begin{pmatrix} 1 & 0 \\ 0 & V \end{pmatrix}$$ $Q$ é uma matriz unitária e temos que $$Q^{\ast}AQ = \begin{pmatrix} \lambda & BV \\ 0 & T \end{pmatrix}$$ Essa era a fatoração de Schur que procurávamos

<a id="fatoracao-de-cholesky"></a>
<a id="secao-26"></a>

## Fatoração de Cholesky

Ainda na vibe da forma de Schur, temos também a fatoração de Cholesky. A ideia é que, dado uma matriz $A$ simétrica e definida positiva, podemos escrever:

$$A = LL^{\ast}$$ <a id="equation_cholesky"></a>

onde $L$ é triangular inferior com diagonal positiva.

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Estabilidade de Algoritmos de Mínimos Quadrados](../estabilidade-de-algoritmos-de-minimos-quadrados/index.md)
- Próximo: [Algoritmos de Autovalores](../algoritmos-de-autovalores/index.md)
