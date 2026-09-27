---
layout: "default"
title: "3.2 Selection Sort — 3. Ordenação"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 16
---

[Estrutura de Dados](../../index.md) · [3. Ordenação](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-16"></a>

# 3.2 Selection Sort

- **Ideia**

  - Percorre a lista até encontrar o menor elemento;

  - Troca esse elemento com o primeiro da lista;

  - Repete a ideia para os próximos elementos.

<a id="secao-17"></a>

# img

``` cpp
void selectionSort(int arr[], int n) {      // Custo  | Vezes
    int minIndex, temp;                     // 2      | 1
    for (int i = 0; i < n - 1; i++) {       // 2      | n-1
        minIndex = i;                       // 1      | n-1
        for (int j = i + 1; j < n; j++) {   // 2      | n-i+1 -> n-1, 
            if (arr[j] < arr[minIndex]) {   // 1      | n-i+1 -> n-1,
                minIndex = j;               // 1      | n-i+1 -> n-1, 
            }
        }
        temp = arr[minIdx];                 // 1      | n-1
        arr[minIdx] = arr[i];               // 1      | n-1
        arr[i] = temp;                      // 1      | n-1
    }
}
```

Note que precisamos de dois inteiros, um para salvar o índice do menor elemento, e outro para fazer a troca de elementos. O primeiro for passará por toda a lista, e o segundo for comparará os elementos subjacentes ao indíce i, pois antes desse índice os elementos já foram ordenados. Fazemos a comparação do valor do índice i com todos os posteriores, e atualizamos o índice j. Após cada comparação, salvamos o valor do menor elemento, atualizamos o valor do índice do menor elemento como o elemento do índice i, e por fim atualizamos o valor do índice i como o menor elemento.

- **Características:**

  - Complexidade de tempo de execução: $O\left( n^{2} \right)$ para o pior caso, dado dois fors que iteram praticamente até $n$;

  - Complexidade de espaço: $O(1)$, pois não precisamos criar nada;

  - Estabilidade: não é estável, trocas alteram a ordem de elementos iguais.

<!-- wiki:original:fim -->

## Conteúdos relacionados

- [Selection Sort — Projeto e Análise de Algoritmos](../../../projeto-e-analise-de-algoritmos/algoritmos-de-ordenacao/selection-sort/index.md)

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [3.1 - Características relevantes:](../caracteristicas-relevantes/index.md)
- Próximo: [3.3 Insertion Sort](../insertion-sort/index.md)
