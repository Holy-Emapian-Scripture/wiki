---
layout: "default"
title: "Teorema — Estabilidade da Triangularização de Householder"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 3
---

[Álgebra Linear Numérica](../../index.md) · [Estabilidade da Triangularização de Householder](../index.md)

<!-- wiki:original:inicio -->
<a id="section_householder_stability_theorem"></a>

# Teorema

Vamos ver que, de fato, o algoritmo de **Householder** é **backwards stable** para toda e qualquer matriz $A$. Fazendo a análise de backwards stable, nosso resultado precisa ter esse formato aqui: $$\widetilde{Q}\widetilde{R} = A + \delta A$$ com $\|\delta A\|/\| A\| = O\left( \varepsilon_{\text{machine}} \right)$. Ou seja, calcular a $QR$ de $A$ pelo algoritmo é o mesmo que calcular a $QR$ de $A + \delta A$ da forma matemática. Mas aqui temos uns adendos.

A matriz $\widetilde{R}$ é como imaginamos, a matriz triangular superior obtida pelo algoritmo, onde as entradas abaixo de 0 podem não ser exatamente 0, mas **muito próximas**.

Porém, $\widetilde{Q}$ **não é aproximadamente** ortogonal, ela é **perfeitamente** ortogonal, mas por quê? Pois no algoritmo de Householder, não calculamos essa matriz diretamente, ela fica “*implícita*” nos cálculos, logo, podemos assumir que ela é perfeitamente ortogonal, já que o computador não a calcula, ou seja, não há erros de arredondamento. Vale lembrar também que $\widetilde{Q}$ é definido por: $$\widetilde{Q} = {\widetilde{Q}}_{1}{\widetilde{Q}}_{2.}..{\widetilde{Q}}_{n}$$ De forma que $\widetilde{Q}$ é perfeitamente unitária e cada matriz ${\widetilde{Q}}_{j}$ é definida como o refletor de householder no vetor de floating point $\widetilde{v_{k}}$ (Olha a página 73 do livro pra você relembrar direitinho o que é esse vetor $\widetilde{v_{k}}$ no algoritmo). Lembrando que $\widetilde{Q}$ é perfeitamente ortogonal, já que eu não calculo ela no computador diretamente, se eu o fizesse, então ela não seria perfeitamente ortogonal, teriam pequenos erros.

**Teorema: Householder's Backwards Stability**

Deixe que a fatoração QR de $A \in {\mathbb{C}}^{m \times n}$ seja dada por $A = QR$ e seja computada pelo algoritmo de **Householder**, o resultado dessa computação são as matrizes $\widetilde{Q}$ e $\widetilde{R}$ definidas anterioremente. Então temos: $$\widetilde{Q}\widetilde{R} = A + \delta A$$ Tal que: $$\frac{\|\delta A\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$ para algum $\delta A \in {\mathbb{C}}^{m \times n}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [O Experimento](../o-experimento/index.md)
- Próximo: [Algoritmo para resolver $Ax = b$](../algoritmo-para-resolver-ax-b/index.md)
