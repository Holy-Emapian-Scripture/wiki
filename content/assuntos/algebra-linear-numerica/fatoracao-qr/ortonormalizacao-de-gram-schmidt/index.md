---
layout: "default"
title: "Ortonormalização de Gram-Schmidt — Fatoração QR"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 23
---

[Álgebra Linear Numérica](../../index.md) · [Fatoração QR](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-23"></a>

# Ortonormalização de Gram-Schmidt

Nossa… a assustadora… Vamos com muita calma. Vimos anteriormente uma maneira de calcular todos os $q_{j}$, vamos relembrar: $$a_{1} = r_{11}q_{1}$$ $$a_{2} = r_{12}q_{1} + r_{22}q_{2}$$ $$\vdots$$ $$a_{n} = r_{1n}q_{1} + r_{2n}q_{2} + \ldots + r_{nn}q_{n}$$ Bem, isso sugere um algoritmo para calcular o próximo $q_{j}$, vamos pensar, temos todos os $a_{j}$, e cada $q_{j}$ precisa dos vetores $\left\{ q_{1},\ldots,q_{j - 1} \right\}$. Bem, podemos ter alguma liberdade aqui! Vamos ver o que acontece quando tentamos calcular $q_{j}$: $$a_{j} = r_{1j}q_{1} + \ldots + r_{jj}q_{j}$$ Vamos isolar $q_{j}$: $$q_{j} = \frac{a_{j} - r_{1j}q_{1} - r_{2j}q_{2} - \ldots - r_{2(j - 1)}q_{j - 1}}{r_{jj}}$$ Bem, isso sugere que $r_{jj}$ é a norma do vetor $a_{j} - \sum_{k = 1}^{j - 1}r_{ij}q_{i}$, mas o que é $r_{ij}$? Lembra da decomposição em fatores ortogonais? Sim, aquela, $v = r + \sum_{i = 1}^{n}q_{i}q_{i}^{\ast}v$. Se trocarmos $v$ por $a_{j}$, temos quase a mesma coisa que definimos anteriormente! $$a_{j} - \sum_{k = 1}^{j - 1}r_{ij}q_{i},\ v - \sum_{i = 1}^{k}q_{i}q_{i}^{\ast}v$$ E você lembra que $r$ é ortogonal a span$\left\{ q_{1},\ldots,q_{k} \right\}$? Isso é exatamente o que $q_{j}$ é! Tudo isso que acabei de dizer sugere que posso definir $r_{ij}$ como $q_{i}^{\ast}a_{j}\ (i \neq j)$. E nosso algoritmo está pronto! Vamos recapitular tudo aqui:

$$q_{1} = \frac{a_{1}}{\| a_{1}\|_{2}}$$ $$q_{2} = \frac{a_{2} - q_{1}q_{1}^{\ast}a_{2}}{\| a_{2} - q_{1}q_{1}^{\ast}a_{2}\|_{2}}$$ $$q_{3} = \frac{a_{3} - q_{1}q_{1}^{\ast}a_{3} - q_{2}q_{2}^{\ast}a_{3}}{\| a_{3} - q_{1}q_{1}^{\ast}a_{3} - q_{2}q_{2}^{\ast}a_{3}\|_{2}}$$ $$\vdots$$ $$q_{n} = \frac{a_{n} - \sum_{i = 1}^{n - 1}q_{i}q_{i}^{\ast}a_{n}}{\| a_{n} - \sum_{i = 1}^{n - 1}q_{i}q_{i}^{\ast}a_{n}\|_{2}}$$

Escrevendo na forma de um algoritmo:

1.  **para** $j = 1$ **até** $n$

    1.  $v_{j} = a_{j}$

    2.  **para** $i = 1$ **até** $j - 1$

        1.  $r_{ij} = q_{i}^{\ast}a_{j}$

        2.  $v_{j} = v_{j} - r_{ij}q_{i}$

    3.  $r_{jj} = \| v_{j}\|_{2}$

    4.  $q_{j} = \frac{v_{j}}{r_{jj}}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Fatoração QR completa](../fatoracao-qr-completa/index.md)
- Próximo: [Existência e unicidade](../existencia-e-unicidade/index.md)
