---
layout: "default"
title: "Estabilidade e Precisão — Algoritmo QR com Shifts"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 54
---

[Álgebra Linear Numérica](../../index.md) · [Algoritmo QR com Shifts](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-54"></a>

# Estabilidade e Precisão

Como esperado, os algoritmos vistos anteriormente são **backward stable**, ou seja, calcular os autovalores de uma matriz $A$ com os algoritmos é o mesmo que calcular os autovalores de uma matriz levemente perturbada $\overset{\sim}{A}$ do modo puramente matemático. O teorema a seguir pode ser provado, mas não é o intuito:

<a id="qr-algorithm-stability-and-precision"></a>

**Teorema**

Deixe uma matriz real, simétrica e tridiagonal $A \in {\mathbb{R}}^{m \times m}$ ser diagonalizada pelo algoritmo QR ([\[shifted-qr-with-well-known-shifts\]](../../algoritmo-qr-sem-shift/o-algoritmo-qr/index.md#shifted-qr-with-well-known-shifts)) em um computador ideal. Deixe $\overset{\sim}{\Lambda}$ ser a matriz de autovalores de $A$ computada por aritmética de ponto flutuante e $\overset{\sim}{Q}$ a matriz exatamente ortogonal associada ao produto dos refletores de householder e rotações utilizadas nos algoritmos, temos que: $$\overset{\sim}{Q}\overset{\sim}{\Lambda}\overset{\sim}{Q} = A + \delta A$$ onde $$\frac{\|\delta A\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$ para algua $\delta A \in {\mathbb{C}}^{m \times m}$

Isso mostra que temos resultados muito bom! Inclusive, juntando com alguns outros teoremas que vimos ([\[qr-algorithm-stability-and-precision\]](#qr-algorithm-stability-and-precision) e [\[householder-stability-and-precision\]](../../reducao-a-forma-de-hessenberg/estabilidade/index.md#householder-stability-and-precision)), temos que, para todo autovalor $\lambda_{j}$, o autovalor computado $\overset{\sim}{\lambda_{j}}$ satisfaz: $$\frac{\vert \overset{\sim}{\lambda_{j}} - \lambda_{j}\vert }{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Wilkinson Shift](../wilkinson-shift/index.md)
- Próximo: [Discos de Gershgorin](../../discos-de-gershgorin/index.md)
