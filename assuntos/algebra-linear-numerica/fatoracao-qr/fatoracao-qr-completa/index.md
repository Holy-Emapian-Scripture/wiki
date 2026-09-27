---
layout: "default"
title: "Fatoração QR completa — Fatoração QR"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 22
---

[Álgebra Linear Numérica](../../index.md) · [Fatoração QR](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-22"></a>

# Fatoração QR completa

Vai um pouco além. Sabemos que $\left\{ q_{1},\ldots,q_{n} \right\}$ é um conjunto de vetores ortonormais de ${\mathbb{C}}^{m}$, isso significa que temos mais $m - n$ vetores ortonormais aos que tínhamos antes, então podemos criar uma base para ${\mathbb{C}}^{m}$, adicionando esses vetores como colunas de $\widehat{Q}$, temos uma matriz ortogonal $Q$. Mas o que fazemos para $A$ permanecer a mesma? Podemos simplesmente adicionar linhas de 0 abaixo de $\widehat{R}$, criando $R \in {\mathbb{C}}^{m \times n}\ (m \geq n)$, obtendo

$$A = QR$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [A ideia da fatoração reduzida](../a-ideia-da-fatoracao-reduzida/index.md)
- Próximo: [Ortonormalização de Gram-Schmidt](../ortonormalizacao-de-gram-schmidt/index.md)
