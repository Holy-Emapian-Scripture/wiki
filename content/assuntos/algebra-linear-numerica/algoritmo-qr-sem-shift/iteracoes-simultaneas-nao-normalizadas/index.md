---
layout: "default"
title: "Iterações Simultâneas Não-normalizadas — Algoritmo QR sem Shift"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 45
---

[Álgebra Linear Numérica](../../index.md) · [Algoritmo QR sem Shift](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-45"></a>

# Iterações Simultâneas Não-normalizadas

A gente vai tentar relacionar (Eu vou tentar traduzir o que o livro fala né) o [\[iteration-qr\]](../o-algoritmo-qr/index.md#iteration-qr) com um algoritmo chamado **iterações simultâneas** que tem um comportamento mais simples de visualizar (De acordo com o livro, pq tudo pra ele é fácil né)

A ideia do algoritmo é aplicar o [\[power-iteration\]](../../quociente-de-rayleigh-e-iteracao-inversa/iteracao-por-potencias/index.md#power-iteration) (Iteração por Potências) para vários vetores simultaneamente. Vamo supor que a gente tem $n$ vetores LI iniciais $v_{1}^{(0)},\ldots,v_{n}^{(0)}$. Se a gente aplica $A^{k}v_{1}^{(0)}$, conforme $k \rightarrow \infty$, isso converge para o autovetor correspondente ao autovalor de maior valor absoluto (Com algumas condições adequadas), meio que parece plausível que $\text{span}\left\{ A^{k}v_{1}^{(0)},A^{k}v_{2}^{(0)},\ldots,A^{k}v_{n}^{(0)} \right\}$ converge para $\text{span}\left\{ q_{1},\ldots,q_{n} \right\}$ que é o espaço formado pelos autovetores associados aos $n$ (Novamente com condições adequadas). Ué, mas quando eu aplico o método a um único vetor ele não converge pro maior? Como que aplicar a vários muda isso? Vou primeiro definir uma estrutura importante no algoritmo e depois faço uma explicação mais simplificada e uma analogia pra entender isso melhor

Na notação matricial, fazemos: $$V^{(0)} = \begin{pmatrix} & \vert  & & \vert  & \\ v_{1}^{(0)} & \vert  & \ldots & \vert  & v_{n}^{(0)} \\ & \vert  & & \vert  & \end{pmatrix}$$<a id="simultanious-iterations-step-1"></a>

E definimos $$V^{(k)} = A^{k}V^{(0)} = \begin{pmatrix} & \vert  & & \vert  & \\ v_{1}^{(k)} & \vert  & \ldots & \vert  & v_{n}^{(k)} \\ & \vert  & & \vert  & \end{pmatrix}$$

Vamos tentar entender a pergunta que fiz antes. Quando a gente aplica o algoritmo a um único vetor, ele vai se alinhando ao vetor dominante, porém, se a gente faz o mesmo com vários vetores **ao mesmo tempo**,ou seja, eu aplico na matriz, não faz muito sentido isso ocorrer. Pensa que se isso acontecesse, eu ia ter como resultado uma matriz que todas as colunas fossem iguais (Meio esquisito isso). O que acontece é que o espaço das colunas de $V^{(0)}$ vai “girando” e se alinhando ao espaço que falei dos autovetores de $A$

Imagine 3 agulhas em 3 direções diferentes (De forma que as agulhas representem vetores LI, e to falando apenas 3 pra representar ${\mathbb{R}}^{3}$, mas se aplica pra outros espaços). Aplicar o método de potência em um único vetor é como se aplicássemos um campo magnético que direciona todas as agulhas pra direção norte (Que seria a direção do autovetor associado ao maior autovalor). Aplicar na matriz $V^{(0)}$ seria aplicar um campo magnético complexo, em que cada vetor $v_{j}^{(0)}$ fica virado pra direção que ele “sente mais”

Beleza, vamos continuar então. A gente ta interessado em $C\left( V^{(k)} \right)$. Que tal a gente pegar uma boa base desse espaço? Uma boa ideia é a fatoração QR dessa matriz né? Já que as colunas de $Q$ são uma base ortonormal de $C\left( V^{(k)} \right)$ $${\hat{Q}}^{(k)}{\hat{R}}^{(k)} = V^{(k)}$$<a id="simultanious-iterations-step-2"></a>

Aqui estamos vendo a fatoração reduzida, logo, ${\hat{Q}}^{(k)}$ é $m \times n$ e ${\hat{R}}^{(k)}$ é $n \times n$. Bem, se as colunas de ${\hat{Q}}^{(k)}$ vão formando uma base do span dos autovetores que eu comentei antes, então faz sentido elas irem convergindo para os próprios autovetores de $A$ ($\pm q_{1},\ldots, \pm q_{n}$). A gente pode argumentar melhor sobre isso fazendo uma expansão das colunas de $V^{(0)}$ e $V^{(k)}$ como combinação linear dos autovetores de $A$ que nem a gente fez em uma lecture anterior $$\begin{array}{r} v_{j}^{(0)} = a_{1j}q_{1} + \ldots + a_{mj}q_{m} \\ v_{j}^{(k)} = \lambda_{1}^{k}a_{1j}q_{1} + \ldots + \lambda_{m}^{k}a_{mj}q_{m} \end{array}$$<a id="v_j-decomposition"></a> Mas não precisamos entrer em detalhes mais aprofundados. Assim como na lecture anterior, resultados vão convergir quando satisfazemos duas condições.

1.  A primeira é que, ao calcularmos $n$ autovalores, todos tenham valor absoluto distintos $$\vert \lambda_{1}\vert  > \vert \lambda_{2}\vert  > \ldots > \vert \lambda_{n}\vert  > \vert \lambda_{n + 1}\vert  \geq \vert \lambda_{n + 2}\vert  \geq \ldots \geq \vert \lambda_{m}\vert$$<a id="simultanious-iterations-assumption-1"></a>

2.  A segunda condição é que os valores $a_{ij}$ na decomposição dos $v_{j}^{(i)}$ que comentei antes sejam, de certa forma, não-singulares. O que isso quer dizer? Significa que eu preciso formar uma boa mistura dos meus autovetores originais. Tipo, se eu formar $v_{j}^{(i)}$ ortogonal a algum autovetor, ele não vai ser muito bem aproximado pelo meu algoritmo. Vou formarlizar essa condição um pouco. Vamos definir $\hat{Q}$ como a matriz $m \times n$ que as colunas são os autovetores $q_{1},\ldots,q_{n}$ de $A$. Então podemos formalizar isso escrevendo: $$\text{ Todas as submatrizes consequentes de }{\hat{Q}}^{T}V^{(0)}\text{ são inversíveis }$$<a id="simultanious-iterations-assumption-2"></a> Eu posso definir como essa multiplicação pois eu vou ter que o elemento $ij$ dessa matriz vai ser $q_{i}^{T}v_{j}^{(0)}$, que ao olharmos para a Equação [\[v_j-decomposition\]](#v_j-decomposition), é igual a $a_{ij}$

<a id="simultanious-iteration-convergence"></a>

**Teorema**

Suponha que a iteração [\[simultanious-iterations-step-1\]](#simultanious-iterations-step-1) e [\[simultanious-iterations-step-2\]](#simultanious-iterations-step-2) é realizada e as condições \[simultanious-iterations-assumption-1\] e \[simultanious-iterations-assumption-2\] são satisfeitas. Conforme $k \rightarrow \infty$, as colunas da matriz $Q^{(k)}$ vão convergindo linearmente para os autovetores de $A$: $$\| q_{j}^{(k)} - \pm q_{j}\| = O\left( C^{k} \right)$$ para cada $j$ com $1 \leq j \leq n$ e $C < 1$ é a constante $\max\limits_{1 \leq k \leq n}\left( \vert \lambda_{k + 1}\vert /\vert \lambda_{k}\vert  \right)$

**Demonstração**

Vamos transformar $\hat{Q} \in {\mathbb{R}}^{m \times n}$ em $Q \in {\mathbb{R}}^{m \times m}$, de forma que $Q$ tenha como colunas todos os autovetores de $A$. Definimos também $\Lambda$ como a matriz de autovalores de $A$ de tal forma que $A = Q\Lambda Q^{T}$. Defina também $\hat{\Lambda}$ como sendo o bloco $n \times n$ de $\Lambda$ com os autovalores associados a matriz $\hat{Q}$. $$V^{(k)} = A^{k}V^{(0)} = Q\Lambda^{k}Q^{T}V^{(0)} = \hat{Q}\Lambda^{k}{\hat{Q}}^{T}V^{(0)} + O\left( \vert \lambda_{k + 1}\vert  \right)$$ Se a condição \[simultanious-iterations-assumption-2\] for satisfeita, podemos fazer uma manipulação simples $$V^{(k)} = \left( \hat{Q}\Lambda^{k} + O\left( \vert \lambda_{k + 1}\vert  \right)\left( {\hat{Q}}^{T}V^{(0)} \right)^{- 1} \right){\hat{Q}}^{T}V^{(0)}$$ Como ${\hat{Q}}^{T}V^{(0)}$ é inversível, $C\left( V^{(k)} \right) = C\left( \hat{Q}\Lambda^{k} + O\left( \vert \lambda_{k + 1}\vert  \right)\left( {\hat{Q}}^{T}V^{(0)} \right)^{- 1} \right)$. Ou seja, a gente consegue perceber que o espaço vai convergindo para o span dos autovetores de $A$. A gente pode até tentar quantificar a convergência, mas não tem necessidade

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [O Algoritmo QR](../o-algoritmo-qr/index.md)
- Próximo: [Iteração Simultânea](../iteracao-simultanea/index.md)
