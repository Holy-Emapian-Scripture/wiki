---
layout: "default"
title: "Insertion Sort — Algoritmos de Ordenação"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A1.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
revisao: "Thalis Ambrosim Falqueto"
ano_original: 2025
ordem_na_trilha: 18
---

[Projeto e Análise de Algoritmos](../../index.md) · [Algoritmos de Ordenação](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-23"></a>

# Insertion Sort

Parecido com o algoritmo de **Selection Sort**, que acabamos de ver. Porém, a ideia é fixar uma posição $i$ e avaliar o valor naquela posição, procurando dentre as posições $\lbrack 0,i - 1\rbrack$ qual deveria ser a posição que o valor da posição $i$ deveria estar:

![Exemplificação do algoritmo Insertion Sort](../../assets/insertion-sort-exemplification.png)

*Figura 19. Exemplificação do algoritmo Insertion Sort*

**Exemplo**

![Exemplo do algoritmo Insertion Sort](../../assets/insertion-sort-example.png)

*Figura 20. Exemplo do algoritmo Insertion Sort*

**IMPLEMENTAÇÃO**

``` cpp
void insertionSort(int v[], int n) {
  for (int i = 1; i < n; i++) {
    int currentValue = v[i];
    int j;
    for (j = i - 1; j >= 0 && v[j] > currentValue; j--) {
      v[j + 1] = v[j]; 
    }
    v[j + 1] = currentValue;
  }
}
```

O loop externo começa no segundo elemento porque o primeiro já forma uma sublista ordenada. A cada iteração, o valor `v[i]` é guardado em `currentValue`. O loop interno percorre da direita para a esquerda os elementos da sublista ordenada, deslocando todos os valores maiores que `currentValue` uma posição à direita. O algoritmo para quando encontramos um elemento menor ou igual a `currentValue` ou quando chegamos ao início do vetor. Assim, a posição `j+1` é o local correto para inserir o `currentValue`, garantindo que, ao final da iteração, os elementos de `v[0..i]` estejam ordenados. A complexidade desse algoritmo também é expressa na forma: $$T(n) = \sum_{j = 1}^{n - 1}j = \frac{n(n - 1)}{2} = \Theta(n^{2})$$ já que o loop de dentro apresenta um range parecido com o do algoritmo Selection Sort. Perceba que, no melhor caso, $T(n) = \Theta(n)$, pois o loop de dentro sempre será quebrado em $O(1)$.

<!-- wiki:original:fim -->

## Conteúdos relacionados

- [3.3 Insertion Sort — Estrutura de Dados](../../../estrutura-de-dados/ordenacao/insertion-sort/index.md)

## Percurso de estudo

[Trilha: A1](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Selection Sort](../selection-sort/index.md)
- Próximo: [Mergesort](../mergesort/index.md)
