---
layout: "default"
title: "Forma de Schur — Problemas de Autovalores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 25
---

[Álgebra Linear Numérica](../../index.md) · [Problemas de Autovalores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-25"></a>

# Forma de Schur

Essa forma é **muito útil** em análise numérica tendo em vista que **toda matriz quadrada** pode ser fatorada assim

**Definição: Fatoração de Schur**

Dada uma matriz $A \in {\mathbb{C}}^{m \times m}$, sua fatoração de schur é tal que: $$A = QTQ^{\ast}$$ onde $Q$ é ortogonal e $T$ é triangular superior

**Teorema**

Toda matriz quadrada $A$ tem uma fatoração de Schur

**Demonstração**

Vamos fazer indução em $m$.

- **Casos base**: $m = 1$ é trivial, então suponha que $m \geq 2$.

- **Passo Indutivo**: Deixe $x$ ser um autovetor de $A$ com autovalor $\lambda$. Normalize $x$ e faça com que seja a primeira coluna de uma matriz ortogonal $U$. Então podemos fazer as contas e conferir que o produto $U^{\ast}AU$ é tal que: $$U^{\ast}AU = \begin{pmatrix} \lambda & B \\ 0 & C \end{pmatrix}$$ Pela hipótese indutiva, existe uma fatoração $VTV^{\ast}$ de $C$, agora escrevemos: $$Q = U\begin{pmatrix} 1 & 0 \\ 0 & V \end{pmatrix}$$ $Q$ é uma matriz unitária e temos que $$Q^{\ast}AQ = \begin{pmatrix} \lambda & BV \\ 0 & T \end{pmatrix}$$ Essa era a fatoração de Schur que procurávamos

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Diagonalização Unitária](../diagonalizacao-unitaria/index.md)
- Próximo: [Fatoração de Cholesky](../fatoracao-de-cholesky/index.md)
