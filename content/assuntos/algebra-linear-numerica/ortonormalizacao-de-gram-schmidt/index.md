---
layout: "default"
title: "Ortonormalização de Gram-Schmidt"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 25
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-25"></a>

# Ortonormalização de Gram-Schmidt

------------------------------------------------------------------------

Podemos descrever o algoritmo de Gram-Schmidt usando projetores, mas por que quereríamos isso? Na verdade, isso é uma introdução para outro algoritmo que veremos mais tarde. Quando falamos de algoritmos, queremos que eles sejam estáveis, no sentido de que, se inserirmos uma entrada no computador, ele nos retornará uma resposta próxima da correta (computadores não resolvem problemas contínuos exatamente), e o processo de Gram-Schmidt não é estável (falaremos sobre isso nas próximas aulas).

Lembre-se que eu disse que, se você tem um vetor $v$ e o decompõe como $$v = r + \sum_{k = 1}^{n}q_{k}q_{k}^{\ast}v$$ A parte $\sum_{k = 1}^{n}q_{k}q_{k}^{\ast}$ é um projetor que projeta na matriz $\widehat{Q}{\widehat{Q}}^{\ast}$ ($\widehat{Q}$ tem colunas $\left\{ q_{1},\ldots,q_{n} \right\}$)? Bem, acontece que podemos expressar os passos do algoritmo de Gram-Schmidt da mesma forma! Vamos relembrar. No $j$-ésimo passo, temos: $$q_{j} = \frac{a_{j} - \sum_{i = 1}^{j - 1}q_{i}q_{i}^{\ast}a_{j}}{\| a_{j} - \sum_{i = 1}^{j - 1}q_{i}q_{i}^{\ast}a_{j}\|_{2}}$$ Isso significa que podemos reescrever isso como $$q_{j} = \frac{\left( I - {\widehat{Q}}_{j - 1}{\widehat{Q}}_{j - 1}^{\ast} \right)a_{j}}{\|\left( I - {\widehat{Q}}_{j - 1}{\widehat{Q}}_{j - 1}^{\ast} \right)a_{j}\|_{2}}$$ Onde ${\widehat{Q}}_{j - 1} = \begin{pmatrix} \vert  & & \vert  \\ q_{1} & & q_{j - 1} \\ \vert  & & \vert \end{pmatrix}$. Vamos definir, para simplificação, o projetor $P_{j}$ como: $$P_{j} = I - {\widehat{Q}}_{j - 1}{\widehat{Q}}_{j - 1}^{\ast}$$

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Algoritmo de Gram-Schmidt Modificado](algoritmo-de-gram-schmidt-modificado/index.md)
2. [Gram-Schmidt como Ortonormalização Triangular](gram-schmidt-como-ortonormalizacao-triangular/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Existência e unicidade](../fatoracao-qr/existencia-e-unicidade/index.md)
- Próximo: [Algoritmo de Gram-Schmidt Modificado](algoritmo-de-gram-schmidt-modificado/index.md)
