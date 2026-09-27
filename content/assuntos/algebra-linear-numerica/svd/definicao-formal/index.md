---
layout: "default"
title: "Definição formal — SVD"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 10
---

[Álgebra Linear Numérica](../../index.md) · [SVD](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-10"></a>

# Definição formal

**Definição**

Dada $A \in {\mathbb{C}}^{m \times n}$ com $m \geq n$, a Decomposição por Valores Singulares de $A$ é:

$A = U\Sigma V^{\ast}$

onde $U \in {\mathbb{C}}^{m \times m}$ é unitária, $V \in {\mathbb{C}}^{n \times n}$ é unitária e $\Sigma \in {\mathbb{C}}^{m \times n}$ é diagonal. Para **conveniência**, denotamos:

$\sigma_{1} \geq \sigma_{2} \geq \sigma_{3} \geq \ldots \geq \sigma_{n}$

Onde $\sigma_{j}$ é a j-ésima entrada de $\Sigma$

Ok, vimos um método intuitivo para ver que toda matriz tem essa decomposição, mas como provamos isso matematicamente?

**Teorema**

Toda matriz $A \in {\mathbb{C}}^{m \times n}$ tem uma decomposição S.V.D

**Demonstração**

Seja $\left\{ v_{j} \right\}$ uma base ortonormal de ${\mathbb{C}}^{n}$, $\left\{ u_{j} \right\}$ uma base ortonormal de ${\mathbb{C}}^{m}$, $Av_{j} = \sigma_{j}u_{j}$, $U_{1}$ e $V_{1}$ matrizes unitárias de colunas $\left\{ u_{j} \right\}$ e $\left\{ v_{j} \right\}$ respectivamente e que, para toda matriz com menos de $m$ linhas e $n$ colunas, a fatoração é válida:

$A = U_{1}SV_{1}^{\ast} \Leftrightarrow U_{1}^{\ast}AV_{1} = S$

Então temos $S = \begin{pmatrix} \sigma_{1} & w^{\ast} \\ 0 & B \end{pmatrix}$ onde $\sigma_{1}$ é $1 \times 1$, $w^{\ast}$ é $1 \times (n - 1)$ e $B$ é $(m - 1) \times (n - 1)$. Beleza, mas o que é $w$? Bem, podemos chegar nesse resultado fazendo algumas manipulações com $\|\begin{pmatrix} \sigma_{1} & w^{\ast} \\ 0 & B \end{pmatrix}\begin{pmatrix} \sigma_{1} \\ w \end{pmatrix}\|_{2}$:

$\|\begin{pmatrix} \sigma_{1} & w^{\ast} \\ 0 & B \end{pmatrix}\begin{pmatrix} \sigma_{1} \\ w \end{pmatrix}\|_{2}^{2} \geq \sigma_{1}^{2} + w^{\ast}w$

O quê? Por que isso é válido? Porque:

$\| Mx\|_{2} \leq \| M\|_{2}\| x\|_{2} \Rightarrow \| M\|_{2} \geq \frac{\| Mx\|_{2}}{\| x\|_{2}}$

Se definirmos $x = \begin{pmatrix} \sigma_{1} \\ w \end{pmatrix}$ e $M = S$, então temos:

$Mx = \begin{pmatrix} \sigma_{1}^{2} + \| w\|^{2} \\ Bw \end{pmatrix} \Rightarrow \| M\|_{2} \geq \frac{\vert \sigma_{1}^{2} + \| w\|^{2}\vert ^{2} + \| Bw\|^{2}}{\sigma_{1}^{2} + \| w\|^{2}}$

Mas observe que o numerador é sempre maior que o denominador, então isso significa

$\frac{\vert \sigma_{1}^{2} + \| w\|^{2}\vert ^{2} + \| Bw\|^{2}}{\sigma_{1}^{2} + \| w\|^{2}} \geq \sigma_{1}^{2} + \| w\|^{2} = \left( \sigma_{1}^{2} + w^{\ast}w \right)^{\frac{1}{2}}\|\begin{pmatrix} \sigma_{1} \\ w \end{pmatrix}\|$

Agora podemos voltar para ver o que é $w$! Bem, agora é fácil! Sabemos que $\| S\|_{2} = \| U_{1}^{\ast}AV_{1}\|_{2} = \| A\|_{2} = \sigma_{1}$ porque $U_{1}$ e $V_{1}$ são ortogonais. Isso significa $\| S\|_{2} \geq \left( \sigma_{1}^{2} + \| w\|^{2} \right)^{\frac{1}{2}} \Rightarrow \sigma_{1} \geq \left( \sigma_{1}^{2} + \| w\|^{2} \right)^{\frac{1}{2}} \Leftrightarrow \sigma_{1}^{2} \geq \sigma_{1}^{2} + \| w\|^{2} \Rightarrow w = 0$.

Pela hipótese indutiva descrita no início da prova, sabemos que $B = U_{2}\Sigma_{2}V_{2}^{\ast}$, então podemos facilmente escrever $A$ como

$A = U_{1}\begin{pmatrix} 1 & 0 \\ 0 & U_{2} \end{pmatrix}\begin{pmatrix} \sigma_{1} & 0 \\ 0 & \Sigma_{2} \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & V_{2}^{\ast} \end{pmatrix}^{\ast}V_{1}^{\ast}$

Isso é uma S.V.D de $A$, usando o caso base de $m = 1$ e $n = 1$, terminamos a prova da existência

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [SVD completa](../svd-completa/index.md)
- Próximo: [Mudança de base](../mudanca-de-base/index.md)
