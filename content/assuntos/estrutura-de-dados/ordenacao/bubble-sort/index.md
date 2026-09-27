---
layout: "default"
title: "3.4 Bubble Sort — 3. Ordenação"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 18
---

[Estrutura de Dados](../../index.md) · [3. Ordenação](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-20"></a>

# 3.4 Bubble Sort

- **ideia**

  - Percorre a lista e compara elementos adjacentes, trocando se estiverem fora de ordem;

  - Repete o processo até que esteja ordenado(pense que se tivessemos o maior elemento como primeiro da fila, teríamos n trocas).

<a id="secao-21"></a>

## img

``` cpp
void bubbleSort(int arr[], int n) {
    int temp;                                     // Custo | Vezes
    for (int i = 0; i < n - 1; i++) {             // 2     | n-1
        for (int j = 0; j < n - i - 1; j++) {     // 2     | n-i-1 ->  1
            if (arr[j] > arr[j + 1]) {            // 1     | n-i-1 ->  1
                temp = arr[j];                    // 1     | n-i-1 ->  1
                arr[j] = arr[j + 1];              // 1     | n-i-1 ->  1
                arr[j + 1] = temp;                // 1     | n-i-1 ->  1
            }
        }
    }
}
```

Como explicado, a ideia é simples, o que faz com que o algoritmo também seja. Salvamos um int para fazer a troca entre elementos subjacentes. O primeiro for fará com que a verificação seja feita n - 1 vezes, e o segundo for fará a comparação entre todos os elementos subjacentes escolhendo o maior e levando-o ao final da fila, por isso j vai até $n - i - 1$, o $- 1$ serve para não sair da lista(fazemos j + 1 no if), e o $- i$ está ali pois o if carrega o maior elemento da lista até o fim dela a cada iteração, portanto não precisamos mais ordenar ele.

- **Características:**

  - Complexidade de tempo de execução: $O\left( n^{2} \right)$ no pior caso;

  - Complexidade de espaço: $O(1)$ (in-place);

  - Estabilidade: estável, pois só trocamos se for maior que o próximo elemento.

<!-- wiki:original:fim -->

## Conteúdos relacionados

- [Bubble Sort — Projeto e Análise de Algoritmos](../../../projeto-e-analise-de-algoritmos/algoritmos-de-ordenacao/bubble-sort/index.md)

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [3.3 Insertion Sort](../insertion-sort/index.md)
- Próximo: [3.5 Comparação entre algoritmos de ordenação](../comparacao-entre-algoritmos-de-ordenacao/index.md)
