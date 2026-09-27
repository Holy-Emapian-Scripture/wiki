---
layout: "default"
title: "Algoritmo QR com Shifts"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 49
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-49"></a>

# Algoritmo QR com Shifts


<a id="conexao-com-a-iteracao-do-quociente-de-rayleigh"></a>
<a id="secao-52"></a>

## Conexão com a Iteração do Quociente de Rayleigh

Beleza, vimos que os shifts são bem poderosos para o cálculo das matrizes, mas aí tu pode tá se perguntando: “Q djabo eu faço pra escolher meus shift? Eu tenho q ser Mãe de Ná?”. E você está corretíssimo, precisamos de um método para escolher shifts interessantes para o algoritmo.

Faz sentido a gente tentar usar o quociente de Rayleigh pra isso. A gente quer tentar fazer com que a última coluna de ${\underline{Q}}^{(k)}$ converja. Então faz sentido a gente usar o Quociente de Rayleigh com essa última coluna né? $$\mu^{(k)} = \frac{\left( q_{m}^{(k)} \right)^{T}Aq_{m}^{(k)}}{{q_{m}^{(k)}}^{T}q_{m}^{(k)}} = \left( q_{m}^{(k)} \right)^{T}Aq_{m}^{(k)})$$

Se escolhermos esse valor, as estimativas $\mu^{(k)}$ (Estimativa de autovalor) e $q_{m}^{(k)}$ estimativa de autovetor são identicos àqueles computados pela iteração do quociente de rayleigh com o vetor inicial sendo $e_{m}$

Tem um negócio bem massa que a gente pode ver com isso. Que o valor $A_{mm}^{(k)}$ é igual a $r\left( q_{m}^{(k)} \right)$ ($r$ sendo a função do quociente de rayleigh), a gente pode visualizar assim: $$A_{mm}^{(k)} = e_{m}^{T}A^{(k)}e_{m} = e_{m}^{T}\left( {\underline{Q}}^{(k)} \right)^{T}A{\underline{Q}}^{(k)}e_{m} = {q_{m}^{(k)}}^{T}Aq_{m}^{(k)}$$

Ou seja, escolher $\mu^{(k)}$ como sendo o coeficiente de rayleigh de $q_{m}^{(k)}$ é a mesma coisa que escolher ele como sendo a última entrada de $A^{(k)}$. A gente chama isso de **Shift do Quociente de Rayleigh**.

<a id="conexao-com-a-iteracao-reversa"></a>
<a id="secao-50"></a>

## Conexao com a Iteração Reversa

A gente tinha visto que o algoritmo QR unshifted ([\[unshifted-qr-algorithm\]](../../algoritmo-qr-sem-shift/iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md#unshifted-qr-algorithm)) era a mesma coisa que aplicar a iteração reversa na matriz identidade. Tem um porém, o [\[unshifted-qr-algorithm\]](../../algoritmo-qr-sem-shift/iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md#unshifted-qr-algorithm) também é equivalente a aplicar a iteração inversa simultânea numa matriz identidade “invertida” P. Vamo tentar desenvolver melhor essa ideia:

Seja $Q^{(k)}$, assim como na última lecture, o fator ortogonal no $k$-ésimo passo da iteração do algoritmo QR. Mostramos antes que o produto acumulado dessas matrizes forma: $${\underline{Q}}^{(k)} = \prod_{j = 1}^{k}Q^{(j)} = \begin{pmatrix} q_{1}^{(k)} & \vert  & \ldots & \vert  & q_{m}^{(k)} \end{pmatrix}$$

É a mesma matriz ortogonal que aparece no $k$-ésimo passo do algoritmo de iteração simultânea. $$A^{k} = {\underline{Q}}^{(k)}{\underline{R}}^{(k)}$$

Se a gente inverte essa fórmula, temos $$A^{- k} = \left( {\underline{R}}^{(k)} \right)^{- 1}\left( {\underline{Q}}^{(k)} \right)^{T} = {\underline{Q}}^{(k)}\left( {\underline{R}}^{(k)} \right)^{- T}$$

Essa segunda igualdade a gente tira porque $A^{- 1}$ é simétrica (Ainda tamo usando que $A$ é simétrica). Deixe $P$ ser a matriz de permutação que troca a ordem de todas as linhas e colunas: $$P = \begin{pmatrix} & & & 1 \\ & & ⋰ \\ & 1 \\ 1 \end{pmatrix}$$

Bem, como $P^{2} = I$, a gente pode reescrever a equação que tinhamos anteriormente como: $$A^{- k}P = \left( {\underline{Q}}^{(k)}P \right)\left( {P\left( {\underline{R}}^{(k)} \right)}^{- T}P \right)$$

Perceba que ${\underline{Q}}^{(k)}P$ é ortogonal (${\underline{Q}}^{(k)}$ é ortogonal e $P$ também) e ${P\left( {\underline{R}}^{(k)} \right)}^{- T}P$ é triangular superior ($\left( {\underline{R}}^{(k)} \right)^{- T}$ é triangular inferior, daí eu inverto a ordem das colunas, e depois a ordem das linhas, aí fica triangular superior), ou seja, a equação anterior pode ser interpretada como uma fatoração QR de $A^{- k}P$. Isso que fizemos é a mesma coisa que aplicar o agloritmo QR na matriz $A^{- 1}$ usando a matriz $P$ como ponto de partida do algoritmo.

<a id="conexao-com-o-algoritmo-de-iteracao-reversa-com-shifts"></a>
<a id="secao-51"></a>

## Conexão com o Algoritmo de Iteração Reversa com Shifts

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

<a id="estabilidade-e-precisao"></a>
<a id="secao-54"></a>

## Estabilidade e Precisão

Como esperado, os algoritmos vistos anteriormente são **backward stable**, ou seja, calcular os autovalores de uma matriz $A$ com os algoritmos é o mesmo que calcular os autovalores de uma matriz levemente perturbada $\overset{\sim}{A}$ do modo puramente matemático. O teorema a seguir pode ser provado, mas não é o intuito:

<a id="qr-algorithm-stability-and-precision"></a>

**Teorema**

Deixe uma matriz real, simétrica e tridiagonal $A \in {\mathbb{R}}^{m \times m}$ ser diagonalizada pelo algoritmo QR ([\[shifted-qr-with-well-known-shifts\]](../../algoritmo-qr-sem-shift/o-algoritmo-qr/index.md#shifted-qr-with-well-known-shifts)) em um computador ideal. Deixe $\overset{\sim}{\Lambda}$ ser a matriz de autovalores de $A$ computada por aritmética de ponto flutuante e $\overset{\sim}{Q}$ a matriz exatamente ortogonal associada ao produto dos refletores de householder e rotações utilizadas nos algoritmos, temos que: $$\overset{\sim}{Q}\overset{\sim}{\Lambda}\overset{\sim}{Q} = A + \delta A$$ onde $$\frac{\|\delta A\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$ para algua $\delta A \in {\mathbb{C}}^{m \times m}$

Isso mostra que temos resultados muito bom! Inclusive, juntando com alguns outros teoremas que vimos ([\[qr-algorithm-stability-and-precision\]](#qr-algorithm-stability-and-precision) e [\[householder-stability-and-precision\]](../../reducao-a-forma-de-hessenberg/estabilidade/index.md#householder-stability-and-precision)), temos que, para todo autovalor $\lambda_{j}$, o autovalor computado $\overset{\sim}{\lambda_{j}}$ satisfaz: $$\frac{\vert \overset{\sim}{\lambda_{j}} - \lambda_{j}\vert }{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$

------------------------------------------------------------------------

<a id="wilkinson-shift"></a>
<a id="secao-53"></a>

## Wilkinson Shift

A gente tem um problema com o método anterior. Nem sempre escolhermos $A_{mm}^{(k)}$ ou $r\left( q_{m}^{(k)} \right)$ como os shifts para convergência funciona. Um exemplo disso é a matriz: $$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

Isso ocorre porque temos uma simetria nos autovalores ($1$ e $- 1$) e $A_{mm}^{(k)} = 0$, o que acarreta que ao escolhermos esse valor como shift, o algoritmo tende a beneficiar ambos os autovalores igualmente (Ou seja, eu não tá mais próximo de nenhum, vou ta igualmente distante dos dois). A gente precisa de uma estimativa que quebre a simetria, vamo fazer o seguinte então:

Deixe $B$ ser definida pelo bloco $2 \times 2$ inferior direito da matriz $A^{(k)}$ $$B = \begin{pmatrix} a_{m - 1} & b_{m - 1} \\ b_{m - 1} & a_{m} \end{pmatrix}$$

O **Shift de Wilkinson** é definido como o autovalor mais próximo de $a_{m}$. Em caso de empate, eu seleciono qualquer um dos dois autovalores arbitrariamente. Aqui tem uma fórmula numericamente estável pra achar esses autovalores: $$\mu = a_{m} - \frac{\text{sign}(\delta)b_{m - 1}^{2}}{\vert \delta\vert  + \sqrt{\delta^{2} + b_{m - 1}^{2}}}$$

onde $\delta = \frac{a_{m - 1} - a_{m}}{2}$. Se $\delta = 0$, eu posso definir $\text{sign}(\delta)$ como sendo $1$ ou $- 1$ arbitrariamente. O **Shift de Wilkinson** também atinge convergência cúbica e, nos piores casos, pelo menos quadrática (Pode ser mostrado). Em partiular, o algoritmo QR com shift de Wilkinson sempre converge.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Convergência do algoritmo QR](../algoritmo-qr-sem-shift/index.md#convergencia-do-algoritmo-qr)
- Próximo: [Estabilidade e Precisão](#estabilidade-e-precisao)
