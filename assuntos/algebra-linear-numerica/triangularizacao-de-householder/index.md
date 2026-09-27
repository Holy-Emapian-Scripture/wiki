---
layout: "default"
title: "Triangularização de Householder"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 28
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-28"></a>

# Triangularização de Householder

------------------------------------------------------------------------

NÃOOOO, HOUSEHOLDER NÃOOOOO! Espere, espere, espere, vamos entrar nisso passo a passo! Vimos no último capítulo que o algoritmo de Gram-Schmidt pode ser escrito como uma série de multiplicações por matrizes triangulares superiores, certo? Bem, o algoritmo de triangularização de Householder é muito semelhante, mas, como o nome sugere, em vez de obtermos uma matriz ortogonal no final, terminamos com uma matriz triangular superior $$Q_{1}Q_{2.}..Q_{n}A = R$$ É fácil ver que $Q_{n}^{\ast}\ldots Q_{2}^{\ast}Q_{1}^{\ast}$ é uma matriz unitária, o que significa que $A = Q_{n}^{\ast}\ldots Q_{2}^{\ast}Q_{1}^{\ast}R$ é uma fatoração QR completa de $A$

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Triangularização por Introdução de Zeros](triangularizacao-por-introducao-de-zeros/index.md)
2. [Refletores de Householder](refletores-de-householder/index.md)
3. [O Melhor de Dois Refletores](o-melhor-de-dois-refletores/index.md)
4. [O Algoritmo](o-algoritmo/index.md)
5. [Aplicando na formação de Q](aplicando-na-formacao-de-q/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Gram-Schmidt como Ortonormalização Triangular](../ortonormalizacao-de-gram-schmidt/gram-schmidt-como-ortonormalizacao-triangular/index.md)
- Próximo: [Triangularização por Introdução de Zeros](triangularizacao-por-introducao-de-zeros/index.md)
