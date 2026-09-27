---
layout: "default"
title: "3.3 Insertion Sort — 3. Ordenação"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 17
---

[Estrutura de Dados](../../index.md) · [3. Ordenação](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-18"></a>

# 3.3 Insertion Sort

- **ideia**

  - Considera o primeiro elemento como ordenado;

  - Insere o próximo elemento na posição correta na parte ordenada;

  - Repete o processo para o restante dos elementos.

<a id="secao-19"></a>

## img

``` cpp
void insertionSort(int arr[], int n) {          // Custo  | Vezes
    int current;                                // 3      | 1
    for (int i = 1; i < n; i++) {               // 2      | n 
        current = arr[i];                       // 1      | n-1
        int j = i - 1;                          // 1      | n-1
        while (j >= 0 && arr[j] > current) {    // 3      | i-1 -> n-2
            arr[j+1] = arr[j];                  // 1      | i-1 -> n-2
            j = j - 1;                          // 1      | i-1 -> n-2
        }
        arr[j+1] = current;                     // 1      | n-1
    }
}
```

Pense em uma separação da mesma lista em duas, uma ordenada e a outra não. Olhando para o código começamos com a declaração do valor elemento que salvaremos, após isso abrimos um for para passar por toda a lista, salvamos o current como o elemento i e iniciamos o j como o índice do elemento antes de i. Então, se antes do elemento i está ordenado, basta achar o lugar certo para o elemento i.

É isso que fazemos com o while, olhamos enquanto não chegamos no índice j = 0(início da lista) e enquanto o eleme nto do array no índice j é maior que o item a direita dele. Quando ele não for, significa que é a posição ordenada, e atualizamos a posição fora do while.

Note que quando entramos no while mas não saímos, significa que ainda não encontramos o local exato do elemento, e para manter a estrutura da lista, atualizamos o array no indice j+1 como sendo o valor do elemento anterior.

- **Características:**

  - Complexidade de tempo de execução: $O\left( n^{2} \right)$ para o pior caso, dado o for e o while que iteram em função de n;

  - Complexidade de espaço: $O(1)$, pois usamos a mesma lista;

  - Estabilidade: é estável, trocas não alteram a ordem de elementos iguais já que fazemos a troca apenas quando o elemento é maior(\>), e não maior igual(\>=).

<!-- wiki:original:fim -->

## Conteúdos relacionados

- [Insertion Sort — Projeto e Análise de Algoritmos](../../../projeto-e-analise-de-algoritmos/algoritmos-de-ordenacao/insertion-sort/index.md)

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [3.2 Selection Sort](../selection-sort/index.md)
- Próximo: [3.4 Bubble Sort](../bubble-sort/index.md)
