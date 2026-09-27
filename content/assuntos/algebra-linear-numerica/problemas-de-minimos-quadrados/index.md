---
layout: "default"
title: "Problemas de Mínimos Quadrados"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 34
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-34"></a>

# Problemas de Mínimos Quadrados

------------------------------------------------------------------------

Qual é o problema que estamos tentando analisar aqui? Bem, temos um conjunto de $m$ equações com $n$ variáveis, e temos mais equações do que variáveis $(m \geq n)$, e queremos encontrar uma solução para esse sistema! Mas você concorda comigo, se fizermos a fatoração $QR$ de $A$, a maioria dessas equações não terá solução, certo? Porque as entradas abaixo da $n$-ésima linha de $R$ serão iguais a $0$, então, para o vetor $Q^{\ast}b$ ter todas as entradas iguais a zero abaixo da $n$-ésima linha, apenas algumas escolhas específicas de $b$ satisfarão isso! $$A = QR \Rightarrow Ax = b \Leftrightarrow Rx = Q^{\ast}b$$ Então, o que podemos fazer com esse sistema? Ignorá-lo? Bem, de forma alguma! Sabemos que $b$ terá uma solução apenas se estiver em $C(A)$, isso significa que, se $b \notin C(A)$, temos: $$b - Ax = r\ (r \neq 0)$$ Então, poderíamos encontrar uma maneira de tornar $r$ o menor possível, então nosso novo objetivo é **minimizar** $b - Ax$. Para medir quão pequeno é $r$, podemos escolher qualquer norma, mas a norma 2 é uma boa escolha e tem algumas propriedades boas para trabalhar.

Dado $A \in {\mathbb{C}}^{m \times n}$, $m \geq n$ e $b \in {\mathbb{C}}^{m}$

encontrar $x \in {\mathbb{C}}^{n}$ tal que $\| b - Ax\|_{2}$ seja minimizado

Então, como resolvemos isso? Existe uma maneira fixa para resolver esse problema? O que fazemos? Na verdade, existe uma maneira fixa para resolvê-lo, e ela gira em torno da **projeção ortogonal**

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Projeções Ortogonais e as Equações Normais](projecoes-ortogonais-e-as-equacoes-normais/index.md)

## Conteúdos relacionados

- [Regressão Linear — Aprendizado de Máquina](../../aprendizado-de-maquina/regressao-linear/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Aplicando na formação de Q](../triangularizacao-de-householder/aplicando-na-formacao-de-q/index.md)
- Próximo: [Projeções Ortogonais e as Equações Normais](projecoes-ortogonais-e-as-equacoes-normais/index.md)
