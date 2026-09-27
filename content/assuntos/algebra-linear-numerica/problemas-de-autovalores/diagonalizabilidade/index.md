---
layout: "default"
title: "Diagonalizabilidade — Problemas de Autovalores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 22
---

[Álgebra Linear Numérica](../../index.md) · [Problemas de Autovalores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-22"></a>

# Diagonalizabilidade

**Teorema: Diagonalizabilidade**

Uma matriz $A \in {\mathbb{C}}^{m \times m}$ é não-deficiente $\Leftrightarrow$ ela tem uma decomposição $A = X\Lambda X^{- 1}$

**Demonstração**

$\Leftarrow$) Dada uma decomposição $A = X\Lambda X^{- 1}$, sabemos, pelo [\[similarity-theorem\]](../transformacoes-similares/index.md#similarity-theorem), que $\Lambda$ sendo similar a $A$, logo, $A$ tem os mesmos autovalores, MA e MG de $\Lambda$. Como $\Lambda$ é diagonal, eu tenho que $\Lambda$ é não-deficiente, logo, o mesmo vale para $A$

$\Rightarrow$) Uma matriz não-deficiente deve ter $m$ autovetores linearmente independentes, pois autovetores com diferentes autovalores precisam ser L.I, e cada autovalor pode se associar com autovetores a quantidade de vezes que sua MA permitir. Se esses $m$ autovetores independentes formam as colunas de uma matriz $X$, então X é inversível e $A = X\Lambda X^{- 1}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Autovalores e Matrizes Deficientes](../autovalores-e-matrizes-deficientes/index.md)
- Próximo: [Determinante e Traço](../determinante-e-traco/index.md)
