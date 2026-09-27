---
layout: "default"
title: "Redução para um problema de Autovalores — Calculando a SVD"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 62
---

[Álgebra Linear Numérica](../../index.md) · [Calculando a SVD](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-62"></a>

# Redução para um problema de Autovalores

Por conta disso, reduzimos o problema de SVD a um problema de autovalores, que é sensível à perturbações.

Um algoritmo estável para calcular a SVD de $A$, usa a matriz

$$H = \begin{pmatrix} 0 & A \\ A^{\ast} & 0 \end{pmatrix}$$

Se $A = U\Sigma V^{\ast}$ é uma SVD de $A$, então $AV = \Sigma U$ e $A^{\ast}U = \Sigma^{\ast}V = \Sigma V$, portanto $$\begin{pmatrix} 0 & A \\ A^{\ast} & 0 \end{pmatrix} \cdot \begin{pmatrix} V & V \\ U & - U \end{pmatrix} = \begin{pmatrix} V & V \\ U & - U \end{pmatrix} \cdot \begin{pmatrix} \Sigma & 0 \\ 0 & - \Sigma \end{pmatrix}$$

Ou:

$$H = \begin{pmatrix} 0 & A \\ A^{\ast} & 0 \end{pmatrix} = \begin{pmatrix} V & V \\ U & - U \end{pmatrix} \cdot \begin{pmatrix} \Sigma & 0 \\ 0 & - \Sigma \end{pmatrix} \cdot \begin{pmatrix} V & V \\ U & - U \end{pmatrix}^{- 1}$$

É uma decomposição em autovalores de $H$, e fica claro que os autovalores de $H$ são os valores singulares de $A$, em módulo.

Agora note que ao calcular os autovalores de $H$, pagamos $\kappa(A)$, e não $\kappa^{2}(A)$, Pois

$$\kappa(H) = \left\| H \right\|_{2} \cdot \left\| H^{- 1} \right\|_{2} = \frac{\sigma_{1}(H)}{\sigma_{m}(H)} = \frac{\sigma_{1}(A)}{\sigma_{m}(A)} = \kappa(A).$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [SVD de A via autovalores de $A^{\ast}A$](../svd-de-a-via-autovalores-de-a-ast-a/index.md)
- Próximo: [Divisão em duas fases](../divisao-em-duas-fases/index.md)
