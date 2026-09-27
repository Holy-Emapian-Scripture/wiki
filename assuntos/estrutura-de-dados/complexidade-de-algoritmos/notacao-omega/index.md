---
layout: "default"
title: "1.2 Notação $\\Omega$ — 1. Complexidade de algoritmos"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 4
---

[Estrutura de Dados](../../index.md) · [1. Complexidade de algoritmos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# 1.2 Notação $\Omega$

Ok, entendemos que $O\left( . \right)$ significa a análise do tempo geral de execução no pior caso, mas como seria para analisar o melhor caso? Para isso, usamos a notação $\Omega(.)$.

Exemplo:

``` cpp
int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            return i; 
        }
    }
    return -1; 
}
```

Note que, nesse caso se o elemento estiver no início da fila, teremos a nossa busca satisfeita imediatamente, no caso, $\Omega(1)$. E fica fácil analisar que o pior caso é $O(n)$. Logo, o melhor caso é denotado $\Omega(1)$ e o pior caso é $O(n)$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [1.1 Notação Big O](../notacao-big-o/index.md)
- Próximo: [2. Tipos Abstratos de Dados](../../tipos-abstratos-de-dados/index.md)
