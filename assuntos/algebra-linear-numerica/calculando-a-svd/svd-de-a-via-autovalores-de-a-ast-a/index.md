---
layout: "default"
title: "SVD de A via autovalores de $A^{\\ast}A$ — Calculando a SVD"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 61
---

[Álgebra Linear Numérica](../../index.md) · [Calculando a SVD](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-61"></a>

# SVD de A via autovalores de $A^{\ast}A$

Calcular a SVD de $A$ usando que $A^{\ast}A = V\Sigma^{\ast}\Sigma V$ igual a um sagui disléxico não é a melhor ideia. O algoritmo padrão seria:

1.  Calcule $A^{\ast}A$

2.  Calcular $A^{\ast}A = V\Lambda V$

3.  Defina $\Sigma$ como a matriz $m \times n$ não-negativa que é a raíz de $\Lambda$

4.  Resolva $U\Sigma = AV$ para uma $U$ unitária

Só que a gente pode mostrar que esse algoritmo não é ideal é instável. Pelo Exercício 26.3 (b) do livro, temos o seguinte:

**Teorema**

Suponha que $A$ é normal. Para cada autovalor ${\widetilde{\lambda}}_{j}$ de $A + \delta A$, existe um autovalor $\lambda_{j}$ de $A$ tal que $$\vert {\widetilde{\lambda}}_{j} - \lambda_{j}\vert  < \|\delta A\|_{2}$$

Usando esse teorema, fazemos uma perturbação $\delta B$ em $A^{\ast}A$, de forma que: $$\vert \lambda_{k}\left( A^{\ast}A + \delta B \right) - \lambda_{k}\left( A^{\ast}A \right)\vert  \leq \|\delta B\|_{2}$$

Agora vamos supor um algoritmo **backward stable** que calcula os valores singulares de $A$. Esse algoritmo vai retornar valores $\widetilde{\sigma}$ tais que: $${\widetilde{\sigma}}_{k} = \sigma_{k}(A + \delta A),\ \frac{\|\delta A\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$

ou seja, temos que $$\vert {\widetilde{\sigma}}_{k} - \sigma_{k}\vert  = O\left( \varepsilon_{\text{machine }} \cdot \| A\| \right)$$

Porém, a gente também pode supor um algoritmo **backward stable** para calcular os autovalores de $A^{\ast}A$, então esse algoritmo nos daria valores $\widetilde{\lambda}$ tais que: $$\vert {\widetilde{\lambda}}_{k} - \lambda_{k}\vert  = O\left( \varepsilon_{\text{machine }} \cdot \| A^{\ast}A\| \right) = O\left( \varepsilon_{\text{machine }} \cdot \| A\|^{2} \right)$$

Então a gente pode tirar a raíz desses valores computados, correto? $$\vert \widetilde{\sigma_{k}} - \sigma_{k}\vert  = O\left( \vert {\widetilde{\lambda}}_{k} - \lambda_{k}\vert /\sqrt{\lambda_{k}} \right) = O\left( \varepsilon_{\text{machine }}\| A\|^{2}/\sigma_{k} \right)$$

E isso é pior do que antes, ou seja, mesmo que utilizemos algoritmos estáveis para calcular os autovalores de $A^{\ast}A$ e tirar sua raíz quadrada, ainda teríamos erros maiores do que algoritmos diretos para calcular os valores singulares.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Calculando a SVD](../index.md)
- Próximo: [Redução para um problema de Autovalores](../reducao-para-um-problema-de-autovalores/index.md)
