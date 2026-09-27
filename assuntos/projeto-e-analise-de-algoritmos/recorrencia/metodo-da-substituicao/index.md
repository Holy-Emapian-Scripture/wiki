---
layout: "default"
title: "Método da substituição — Recorrência"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A1.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
revisao: "Thalis Ambrosim Falqueto"
ano_original: 2025
ordem_na_trilha: 3
---

[Projeto e Análise de Algoritmos](../../index.md) · [Recorrência](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-3"></a>

# Método da substituição

A ideia é provar por **indução** que $T(n)$ é $O$ de uma função **pressuposta**. Por isso, é claro, só é passível de uso quando se tem uma hipótese da solução, e provamos exatamente a hipótese na indução. Pode ser usado para limites superiores e inferiores.

**Exemplo**

$$T(n) = \begin{cases} \theta(1)\text{ se }n = 1 \\ 2T\left( \frac{n}{2} \right) + n\text{ se }n > 1 \end{cases}$$ Vamos pressupor que $T(n) = O\left( n^{2} \right)$. Queremos então provar $T(n) \leq cn^{2}$.

**Caso base**: $n = 1 \Rightarrow T(1) = 1 \leq cn^{2}$

**Passo Indutivo**: Vamos supor que vale para $\frac{n}{2}$, e ver se vale para $n$. Então temos: $$T\left( \frac{n}{2} \right) \leq c\frac{n^{2}}{4}$$ Vamos testar para $T(n)$ então $$\begin{array}{r} T(n) = 2T\left( \frac{n}{2} \right) + n \Rightarrow T(n) \leq 2c\frac{n^{2}}{4} + n \\ \Leftrightarrow T(n) \leq \frac{cn^{2}}{2} + n \\ \Leftrightarrow \frac{cn^{2}}{2} + n \leq cn^{2} \\ \Leftrightarrow 2n \leq 2cn^{2} - cn^{2} \\ \Leftrightarrow \frac{n}{2} \leq c \end{array}$$ Ou seja, conseguimos escolher um $c$ e um $n_{0}$ de forma que $\forall n \geq n_{0}$, $T(n) \leq cn^{2}$, logo, $T(n) = O\left( n^{2} \right)$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Recorrência](../index.md)
- Próximo: [Método da árvore de recursão](../metodo-da-arvore-de-recursao/index.md)
