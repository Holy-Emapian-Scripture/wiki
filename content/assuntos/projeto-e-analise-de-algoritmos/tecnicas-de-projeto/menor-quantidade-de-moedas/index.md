---
layout: "default"
title: "Menor quantidade de moedas — Técnicas de Projeto"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 3
---

[Projeto e Análise de Algoritmos](../../index.md) · [Técnicas de Projeto](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Menor quantidade de moedas

**Dado um valor $v$ e uma lista de denominações de moedas (de um sistema canônico), encontre o número de moedas para formar $v$.**

Nesse problema, vamos usar o paradigma Guloso. Considerando a lista de moedas **ordenada**, declaramos duas váriaveis, e para cada moeda da lista, se

``` v
v_fake
```

for 0 (significa que nossa soma de moedas chegou no valor que queríamos), acabamos o código. Caso contrário, pegamos a divisão inteira, que no caso significa quantas vezes cada moeda consegue fazer parte do valor, subtraímos do que falta em

``` v
v_fake
```

e incrementamos a contagem.

``` py
def coin_problem(v, coins):
    counting_coins = 0
    v_fake = v

    for coin in coins:
        if v_fake == 0:
            break
        qtd = v_fake // coin 
        if qtd > 0:
            v_fake -= qtd * coin
            counting_coins += qtd

    return counting_coins
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios de slides](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Maior subsequência de Strings](../maior-subsequencia-de-strings/index.md)
- Próximo: [Menor quantidade de comparações](../menor-quantidade-de-comparacoes/index.md)
