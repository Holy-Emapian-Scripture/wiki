---
layout: "default"
title: "Aritmética de Ponto Flutuante"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 39
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-45"></a>

# Aritmética de Ponto Flutuante

------------------------------------------------------------------------

Quando estamos analisando algoritmos e computadores, temos um problema **realmente** grande. Computadores são máquinas discretas, o que significa que, quando falamos de números reais, eles não podem representar **todos** eles, há uma quantidade finita de números que podem representar, dependendo de como esses computadores são construídos. A maioria dos computadores usa um sistema binário para representar números reais, mas eles poderiam usar outros sistemas. Existem dois grandes problemas na representação de números reais:

1.  **Underflow & Overflow**: Como eu disse, um computador pode representar um número finito de números reais, isso significa que há um máximo e um mínimo nesse conjunto. Se eu tentar representar um número maior que esse máximo, terei um erro de **overflow**, portanto, tentar representar um número menor, terei um erro de **underflow**. Hoje em dia, isso não é um grande problema, a maioria dos computadores é capaz de armazenar números muito grandes e muito pequenos, suficientes para os problemas com os quais vamos trabalhar

2.  **Gap**: Quando tentamos representar números reais, há um problema, porque entre dois números reais, existem infinitos outros números reais, o que nos leva ao problema do **gap**, porque, se o conjunto de números que o computador pode representar é finito, podemos contá-los, e se podemos contá-los, podemos obter uma infinidade de outros números reais entre eles. O problema do **gap** não é realmente um **PROBLEMA**, mas quando estamos criando algoritmos, queremos que eles sejam o mais precisos possível, porque um algoritmo instável pode nos levar a grandes erros de arredondamento

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Conjunto de Ponto Flutuante](conjunto-de-ponto-flutuante/index.md)
2. [Números não em $F$](numeros-nao-em-f/index.md)
3. [Épsilon Máquina](epsilon-maquina/index.md)
4. [Aritmética de Ponto Flutuante](aritmetica-de-ponto-flutuante/index.md)
5. [Mais sobre Épsilon Máquina](mais-sobre-epsilon-maquina/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Condicionamento de Matrizes e Vetores](../condicionamento-e-numeros-de-condicao/condicionamento-de-matrizes-e-vetores/index.md)
- Próximo: [Conjunto de Ponto Flutuante](conjunto-de-ponto-flutuante/index.md)
