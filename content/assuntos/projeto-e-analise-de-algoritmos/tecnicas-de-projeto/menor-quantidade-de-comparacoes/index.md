---
layout: "default"
title: "Menor quantidade de comparações — Técnicas de Projeto"
tipo: "exercicio"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Exercises/ExSlides.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 4
---

[Projeto e Análise de Algoritmos](../../index.md) · [Técnicas de Projeto](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Menor quantidade de comparações

**Dado um array $A$ com $n$ elementos, encontre simultaneamente o maior e o menor elemento usando o menor número possível de comparações.**

Uma solução genérica, mas que não atende a menor quantidade de comparações possível é se tivermos duas variáveis, uma para o mínimo e outra para o máximo, e passar pela lista em apenas um for. Infelizmente, a cada elemento o algoritmo deve verificar se o número é o menor ou o maior dentre o valor das variáveis anteriores. Desde que isso traz duas verificações por elementos, ao fim temos $2n$ comparações. Mas essa não é a solução ótima.

<a id="secao-6"></a>

## Solução (recursiva):

Essa solução, assim como a outra, depende de uma sacada interessante, em que queremos reduzir a quantidade de comparações $(2n)$ do algoritmo ingênuo. Para isso, usaremos uma estratégia de comparação entre **pares**, utilizando o paradigma Dividir e Conquistar. Tratamos os dois casos base na função e dividimos a lista ao meio para fazer isso recursivamente, até que tenhamos apenas $1$ ou $2$ elementos a serem analisad os, e isso nos traz 3 verificações por elemento (uma para o par

``` arr
arr[left] < arr[right]
```

), duas para comparar com os mínimos globais(uma pro máximo, outra pro mínimo), trazendo $\approx 3\frac{n}{2}$ comparações.

``` py
def max_min(arr, left, right):
    if left == right:
        return arr[left], arr[right]
    if left == right - 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]

    mid = (left + right) // 2
    min1, max1 = max_min(arr, left, mid)
    min2, max2 = max_min(arr, mid+1, right)

    min_global = min(min1, min2)
    max_global = max(max1, max2)

    return (min_global, max_global)
```

<a id="secao-7"></a>

## Solução (pairwise):

Essa solução é interativa, e usa uma ideia parecida com o algoritmo anterior. Foi separada em duas funções para evitar duplicação de código. Declaramos algumas variáveis para tracking dos mínimos e máximos, e vemos se o tamanho da lista é par ou ímpar. Se for par, então teremos uma quantidade de pares sem nenhuma sobra, e assim executamos

    pairwise

, que passa na lista de elementos de par em par e verifica o maior (e menor) entre a dupla (uma verificação) e atualiza o máximo e mínimo global (2 verificações).

Para o caso de uma lista de tamanho ímpar, apenas é feita a mesma verificação para o último elemento ainda não verificado.

``` py
def pairwise(arr, max_local, min_local, max_global, min_global):
    for i in range(0, len(arr) - 1, 2):
        if arr[i] >= arr[i+1]:
            max_local = arr[i]
            min_local = arr[i + 1]
        else: 
            max_local = arr[i + 1]
            min_local = arr[i]

        if max_local > max_global:
            max_global = max_local
        if min_local < min_global:
            min_global = min_local

    return min_global, max_global

def comparation_problem(arr):
    max_global = -float('inf')
    min_global = float('inf')
    max_local = 0
    min_local = 0

    if len(arr) % 2 == 0:
        min_global, max_global = pairwise(arr, max_local, min_local, max_global, min_global)
    else:
        min_global, max_global = pairwise(arr, max_local, min_local, max_global, min_global)

        k = len(arr) - 1 
        max_local = arr[k]
        min_local = arr[k]

        if max_local > max_global:
            max_global = max_local
        if min_local < min_global:
            min_global = min_local

    return (min_global, max_global)
```

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios de slides](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md#apresentacao-original)

- Anterior: [Menor quantidade de moedas](../menor-quantidade-de-moedas/index.md)
- Próximo: [Grafos](../../grafos/index.md)
