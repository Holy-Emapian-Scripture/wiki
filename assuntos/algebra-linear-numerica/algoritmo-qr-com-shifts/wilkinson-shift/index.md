---
layout: "default"
title: "Wilkinson Shift — Algoritmo QR com Shifts"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 53
---

[Álgebra Linear Numérica](../../index.md) · [Algoritmo QR com Shifts](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-53"></a>

# Wilkinson Shift

A gente tem um problema com o método anterior. Nem sempre escolhermos $A_{mm}^{(k)}$ ou $r\left( q_{m}^{(k)} \right)$ como os shifts para convergência funciona. Um exemplo disso é a matriz: $$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

Isso ocorre porque temos uma simetria nos autovalores ($1$ e $- 1$) e $A_{mm}^{(k)} = 0$, o que acarreta que ao escolhermos esse valor como shift, o algoritmo tende a beneficiar ambos os autovalores igualmente (Ou seja, eu não tá mais próximo de nenhum, vou ta igualmente distante dos dois). A gente precisa de uma estimativa que quebre a simetria, vamo fazer o seguinte então:

Deixe $B$ ser definida pelo bloco $2 \times 2$ inferior direito da matriz $A^{(k)}$ $$B = \begin{pmatrix} a_{m - 1} & b_{m - 1} \\ b_{m - 1} & a_{m} \end{pmatrix}$$

O **Shift de Wilkinson** é definido como o autovalor mais próximo de $a_{m}$. Em caso de empate, eu seleciono qualquer um dos dois autovalores arbitrariamente. Aqui tem uma fórmula numericamente estável pra achar esses autovalores: $$\mu = a_{m} - \frac{\text{sign}(\delta)b_{m - 1}^{2}}{\vert \delta\vert  + \sqrt{\delta^{2} + b_{m - 1}^{2}}}$$

onde $\delta = \frac{a_{m - 1} - a_{m}}{2}$. Se $\delta = 0$, eu posso definir $\text{sign}(\delta)$ como sendo $1$ ou $- 1$ arbitrariamente. O **Shift de Wilkinson** também atinge convergência cúbica e, nos piores casos, pelo menos quadrática (Pode ser mostrado). Em partiular, o algoritmo QR com shift de Wilkinson sempre converge.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Conexão com a Iteração do Quociente de Rayleigh](../conexao-com-a-iteracao-do-quociente-de-rayleigh/index.md)
- Próximo: [Estabilidade e Precisão](../estabilidade-e-precisao/index.md)
