---
layout: "default"
title: "Dependência de $m$ e $n$ — Estabilidade"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 47
---

[Álgebra Linear Numérica](../../index.md) · [Estabilidade](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-56"></a>

# Dependência de $m$ e $n$

Na prática, quando falamos de erros de arredondamento, a estabilidade de algoritmos envolvendo uma matriz $A$ não depende da própria $A$, mas de $m$ e $n$ (suas dimensões). Podemos ver isso analisando o seguinte problema:

Suponha que eu tenha um algoritmo para resolver um sistema não singular $m \times m$ $Ax = b$ para $x$ e garantimos que a solução $\widetilde{x}$ dada pelo algoritmo satisfaz $$\frac{\|\widetilde{x} - x\|}{\| x\|} = O\left( \kappa(A)\varepsilon_{\text{machine}} \right)$$ Isso significa que existe uma constante $C$ que satisfaz $$\|\widetilde{x} - x\| \leq C\kappa(A)\varepsilon_{\text{machine }}\| x\|$$ Isso mostra que, mesmo $C$ não dependendo nem de $A$ nem de $b$, acaba dependendo das dimensões de $A$ porque, se mudarmos $m$ ou $n$, os dados passados para o problema mudam, o que significa que teremos um **novo** problema porque estamos mudando seu domínio e $\kappa(A)$ também mudará se alterarmos suas dimensões!

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Definição Formal de $O\left( \varepsilon_{\text{machine}} \right)$](../definicao-formal-de-o-left-varepsilon-text-machine-right/index.md)
- Próximo: [Independência da Norma](../independencia-da-norma/index.md)
