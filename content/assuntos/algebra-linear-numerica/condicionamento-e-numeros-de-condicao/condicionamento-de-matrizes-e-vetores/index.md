---
layout: "default"
title: "Condicionamento de Matrizes e Vetores — Condicionamento e Números de Condição"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 38
---

[Álgebra Linear Numérica](../../index.md) · [Condicionamento e Números de Condição](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-41"></a>

# Condicionamento de Matrizes e Vetores

Agora, um conceito importante para estabilidade e condicionamento é como a multiplicação de vetores e matrizes é condicionada, as multiplicações de vetores são *bem-condicionadas*? *mal-condicionadas*? Como as matrizes são condicionadas? Vamos ver

<a id="secao-42"></a>

## Condição da Multiplicação Matriz-Vetor

<a id="condition_number_matrix_vector_multiplication"></a>

**Teorema**

Dado $A \in {\mathbb{C}}^{m \times n}$ fixo, o problema de calcular $Ax$ com $x$ no espaço normado de dados, o número de condição do problema da matriz é

$$\kappa = \| A\|\frac{\| x\|}{\| Ax\|}$$

Se $A$ é quadrada e inversível:

$$\kappa \leq \| A\|\| A^{- 1}\|$$

**Demonstração**

Fixe $A \in {\mathbb{C}}^{m \times n}$ e o problema de calcular $Ax$, com $x$ sendo os dados, ou seja, calcularemos a condição desse problema com base em perturbações de $x$, não de $A$, $A$ será fixo o tempo todo. $$\kappa = \sup\limits_{\Delta x}\left( \frac{\| f(x + \Delta x) - f(x)\|}{\| f(x)\|}\frac{\| x\|}{\|\Delta x\|} \right) = \sup\limits_{\Delta x}\left( \frac{\| A(x + \Delta x) - Ax\|}{\| Ax\|}\frac{\| x\|}{\|\Delta x\|} \right) = \sup\limits_{\Delta x}\left( \frac{\| A\Delta x\|}{\| Ax\|}\frac{\| x\|}{\|\Delta x\|} \right)$$ $$\kappa \leq \sup\limits_{\Delta x}\left( \frac{\| A\|\|\Delta x\|}{\| Ax\|}\frac{\| x\|}{\|\Delta x\|} \right) = \| A\frac{\|\left( \| x\| \right)}{\| Ax\|}$$

Se $A$ é quadrada e inversível, podemos usar o fato de que $\frac{\| x\|}{\| Ax\|} \leq \| A^{- 1}\|$ (prová-lo-emos depois), para expressar $\kappa$ como:

$$\kappa \leq \| A\|\| A^{- 1}\| \vee \kappa = \alpha\| A\|\| A^{- 1}\|$$

**Corolário**

Seja $A \in {\mathbb{C}}^{m \times n}$ não singular e considere a equação $Ax = b$. O problema de calcular $b$ dado $x$ tem número de condição $$\kappa = \| A\frac{\|\left( \| x\| \right)}{\| b\|}$$

**Teorema**

$$\frac{\| x\|}{\| Ax\|} \leq \| A^{- 1}\|$$

**Demonstração**

Escreva $x$ como $x = A^{- 1}(Ax)$, isso significa $$\| x\| = \| A^{- 1}Ax\| \leq \| A^{- 1}\|\| Ax\| \Leftrightarrow \frac{\| x\|}{\| Ax\|} \leq \| A^{- 1}\|$$

<a id="secao-43"></a>

## Número de Condição de uma Matriz

O quê? Por que podemos dar um número de condição a uma matriz? Porque elas são **funções**! Por quê? Lembre-se que podemos representar toda **transformação linear** como uma **multiplicação matricial**? Isso implica que, se uma matriz $A$ está em ${\mathbb{C}}^{m \times n}$, então ela pode ser representada como $A:{\mathbb{C}}^{n} \rightarrow {\mathbb{C}}^{m}$! Agora que entendemos por que elas podem ter um número de condição, vamos defini-lo

**Definição**

Dado $A \in {\mathbb{C}}^{m \times m}$ não singular, o número de condição de $A$, denotado como $\kappa(A)$, é: $$\kappa(A) = \| A\|\| A^{- 1}\|$$ Se $A$ é singular $$\kappa(A) = \infty$$ Se $A$ é retangular $$\kappa(A) = \| A\|\| A^{+}\|,\ \left( A^{+} = \left( A^{\ast}A \right)^{- 1}A \right)$$

<a id="secao-44"></a>

## Condição de Sistemas de Equações

**Teorema**

Dado um sistema $Ax = b$, vamos manter $b$ fixo e considerar o problema $A \mapsto x = A^{- 1}b$, o número de condição desse problema é: $$\kappa(A)$$

**Demonstração**

Se perturbarmos $A$ e $x$, fazemos: $$(A + \Delta A)(x + \Delta x) = b$$ $$\Leftrightarrow Ax + A(\Delta x) + (\Delta A)x + (\Delta A)(\Delta x) = b$$ $$\Leftrightarrow b + A(\Delta x) + (\Delta A)x + (\Delta A)(\Delta x) = b$$ $$\Leftrightarrow A(\Delta x) + (\Delta A)x + (\Delta A)(\Delta x) = 0$$

Sabemos que $(\Delta A)(\Delta x)$ é duplamente infinitesimal e ambos estão indo para 0, então podemos descartá-lo, e obtemos

$$A(\Delta x) + (\Delta A)x = 0 \Leftrightarrow \Delta x = - A^{- 1}(\Delta A)x$$ Esta equação implica que $$\|\Delta x\| \leq \| A^{- 1}\|\|\Delta A\|\| x\| \Leftrightarrow \|\Delta x\|\| A\| \leq \| A^{- 1}\|\| A\|\|\Delta A\|\| x\|$$ $$\frac{\|\Delta x\|}{\| x\|}\frac{\| A\|}{\|\Delta A\|} \leq \| A^{- 1}\|\| A\|$$

Se fizermos $\Delta x \rightarrow 0$ e $\Delta A \rightarrow 0$, temos $$\kappa = \| A\|\| A^{- 1}\| = \kappa(A)$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Condicionamento de um Problema](../condicionamento-de-um-problema/index.md)
- Próximo: [Aritmética de Ponto Flutuante](../../aritmetica-de-ponto-flutuante/index.md)
