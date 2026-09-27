---
layout: "default"
title: "Transformações Similares — Problemas de Autovalores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 20
---

[Álgebra Linear Numérica](../../index.md) · [Problemas de Autovalores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-20"></a>

# Transformações Similares

**Definição: Transformação Similar**

Se $X \in {\mathbb{C}}^{m \times m}$ é inversível, então o mapeamento $A \mapsto X^{- 1}AX$ é chamado de **transformação similar** de A.

Dizemos que duas matrizes $A$ e $B$ são **similares** se existe uma matriz inversível $X$ que relacione as transformações similares entre $A$ e $B$, i.e: $$A = X^{- 1}BX$$

<a id="similarity-theorem"></a>

**Teorema**

Se $A \in {\mathbb{C}}^{m \times m}$ é inversível, então $A$ e $X^{- 1}AX$ o mesmo polinômio característico, os mesmos autovalores e multiplicidades geométrica e algébrica.

**Demonstração**

$$\begin{array}{r} p_{X^{- 1}AX}(z) = \det(zI - X^{- 1}AX) = \det(X^{- 1}(zI - A)X) \\ = \det(X^{- 1})\det(zI - A)\det(X) = \det(zI - A) = p_{A(z)}) \end{array}$$

Suponha que $E_{\lambda}$ é o autoespaço de $A$, então $X^{- 1}E_{\lambda}$ é autoespaço de $X^{- 1}AX$, ou seja, ambos tem mesma multiplicidade geométrica

Agora podemos correlacionar a multiplicidade geométrica e a algébrica

**Teorema**

A multiplicidade algébrica de um autovalor $\lambda$ é sempre maior ou igual a sua multiplicidade geométrica

**Demonstração**

Deixe $n$ ser a multiplicidade gemétrica de $\lambda$ para a matriz $A$. Forme uma matriz $\hat{V} \in {\mathbb{C}}^{m \times n}$ de tal forma que as suas $n$ colunas formam uma base ortonormal do autoespaço $\left\{ x:Ax = \lambda x \right\}$. Se extendermos $\widetilde{V}$ para uma matriz ortogonal quadrada, temos: $$B = V^{\ast}AV = \begin{pmatrix} \lambda I & C \\ 0 & D \end{pmatrix}$$ Pela definição e propriedades do determinante (Não cabe mostrá-las aqui), temos que: $$\det(\mu I - B) = \det(\mu I - \lambda I)\det(\mu I - D) = (\mu - \lambda)^{n}\det(\mu I - D)$$ Ou seja, a multiplicidade algébrica de $\lambda$ como um autovalor de $B$ é, no mínimo, $B$. Como transformações similares mantém a multiplicidade, o mesmo vale para $A$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Multiplicidades Algébrica e Geométrica](../multiplicidades-algebrica-e-geometrica/index.md)
- Próximo: [Autovalores e Matrizes Deficientes](../autovalores-e-matrizes-deficientes/index.md)
