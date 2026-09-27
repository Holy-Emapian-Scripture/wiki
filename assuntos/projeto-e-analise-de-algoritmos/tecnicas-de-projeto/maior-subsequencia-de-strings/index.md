---
layout: "default"
title: "Maior subsequência de Strings — Técnicas de Projeto"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 2
---

[Projeto e Análise de Algoritmos](../../index.md) · [Técnicas de Projeto](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-2"></a>

# Maior subsequência de Strings

**Dadas duas strings, encontre o comprimento da maior subsequência comum entre elas.**

Essa solução usa o paradigma da Programação Dinâmica, onde usaremos uma matriz para guardar os valores de cada sub string. Por exemplo, a matriz no índice $i\text{ x }j$ será o tamanho da maior subsequênciade string dado que nossas substrings são $string1$

    [:i]

e $string2$

    [:j]

.

Após construir a matriz, passamos completando cada elemento. Caso as letras sejam iguais, nós atualizamos a tabela somando o valor de um e o valor das substrings passadas, quando não tínhamos nenhuma das duas letras comparadas. Caso contrário, pegamos o maior entre $string1$

    [:i-1]

e $string2$

    [:j]

<a id="secao-3"></a>

## explicar melhor os casos e pq funciona

``` py
def string_problem(string1, string2):
    str1 = list(string1)
    str2 = list(string2)
    len_str1 = len(str1)
    len_str2 = len(str2)
    M = [[0] * (len_str1 + 1) for _ in range(len_str2 + 1)]

    for j in range (1, len_str2 + 1):
        for i in range (1, len_str1 + 1):
            if str1[i - 1] == str2[j - 1]:
                M[j][i] = 1 + M[j-1][i-1]
            else:
                M[j][i] = max(M[j][i - 1], M[j - 1][i])

    return M[len_str2][len_str1]
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios de slides](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Técnicas de Projeto](../index.md)
- Próximo: [Menor quantidade de moedas](../menor-quantidade-de-moedas/index.md)
