---
layout: "default"
title: "Mergesort — Algoritmos de Ordenação"
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
ordem_na_trilha: 19
---

[Projeto e Análise de Algoritmos](../../index.md) · [Algoritmos de Ordenação](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-24"></a>

# Mergesort

A ideia do algoritmo consiste em dividir a sequência em duas partes, executar chamadas recursivas para cada sub-sequência, até que o tamanho das sequências sejam tão pequenas que caiam no caso trivial de se ordenar, e juntá-las (merge) de forma ordenada. Esse algoritmo depende de um algoritmo auxiliar de intercalação (merge)

![Exemplificação do algoritmo Mergesort](../../assets/mergesort-exemplification.png)

*Figura 21. Exemplificação do algoritmo Mergesort*

**FUNÇÃO DE INTERCALAÇÃO**

``` cpp
void merge(int v[], int startA, int startB, int endB) {
  int r[endB - startA];
  int aInx = startA;
  int bInx = startB;
  int rInx = 0;
  while (aInx < startB && bInx < endB) {
    if (v[aInx] <= v[bInx]) {
      r[rInx++] = v[aInx++];
    } else {
      r[rInx++] = v[bInx++];
    }
  }
  while (aInx < startB) { 
    r[rInx++] = v[aInx++]; 
  }
  while (bInx < endB) {
    r[rInx++] = v[bInx++]; 
  }
  for (aInx = startA; aInx < endB; ++aInx) {
    v[aInx] = r[aInx - startA];
  }
}
```

- Nota: em qualquer código `vector[índice++]`, o ++ incrementa automaticamente o índice depois da ação especificada, enquanto `vector[++índice]` incrementa antes.

Cria-se um vetor r do tamanho da lista passada antes da separação, e definimos alguns inteiros para não alterarmos os tamanhos originais e conseguirmos saber o que estamos fazendo com a lista. Sabemos que no vetor `v`, a parte `startA` até `startB - 1` está ordenada corretamente, e o mesmo vale para `startB` até `endB`.

O primeiro while serve para usar a ordem criada nas duas subsequências a nosso favor, ou seja, verificamos até alguma das duas chegar em seu tamanho final e, enquanto isso não acontece, comparamos cada elemento inicial de cada sub-sequência, e sabendo que estão ordenadas, não precisamos verificar outros elementos. O vetor `r` fica completamete ordenado, mas em caso de alguma contagem de índice(`aIdx` ou `bIdx`) acabar antes de outra, significa que alguns elementos do outro índice não foram passados para `r` ainda, e é para isso que servem os outros dois whiles no final. Por fim, o último for serve apenas para passar os elementos na ordem correta de `r` para o vetor original e ainda não ordenado `v`.

Os 3 whiles somam $n$ operações, e o for final outras $n$. Logo, a complexidade é $$T(n) = \Theta(n)$$

Agora que temos uma função que junta duas listas ordenadamente, conseguimos fazer o mergeSort. O algoritmo consiste em dividir a sequência do vetor $V$ em duas subsequências $A$ e $B$, fazendo isso recursivamente até que $V$ esteja ordenado.

**IMPLEMENTAÇÃO**

``` cpp
void mergeSort(int v[], int startInx, int endInx) {
  if (startInx < endInx - 1) {
    int midInx = (startInx + endInx) / 2;
    mergeSort(v, startInx, midInx);
    mergeSort(v, midInx, endInx);
    merge(v, startInx, midInx, endInx);
  }
}
```

Olhando o algoritmo, note que ele chama a recursão do mergeSort até que a diferença entre os dois index sejam um, portanto essa recursão acontece até que tenhamos $n$ listas de tamanho $1$, e o merge fará todo o trabalho de “ordenar”. Olhe o exemplo:

![Exemplo do algoritmo MergeSort](../../assets/mergesort-example.png)

*Figura 22. Exemplo do algoritmo MergeSort*

Podemos então avaliar a função de complexidade: $$T(n) = 2T\left( \frac{n}{2} \right) + n$$

E já vimos em capítulos anteriores que isso é $T(n) = \Theta(n\log(n))$. Perceba que ele não compara todos os pares mesmo no pior caso, porém, ele exige um espaço de memória $O(n)$ **adicional** para a ordenação.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Insertion Sort](../insertion-sort/index.md)
- Próximo: [Quicksort](../quicksort/index.md)
