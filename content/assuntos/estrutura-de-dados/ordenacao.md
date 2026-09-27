---
layout: "default"
title: "3. Ordenação"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 14
---

[Estrutura de Dados](index.md)

<!-- wiki:original:inicio -->

<a id="secao-14"></a>

# 3. Ordenação


<a id="caracteristicas-relevantes"></a>
<a id="secao-15"></a>

## 3.1 - Características relevantes:

A utilidade dos [algoritmos de ordenação](../projeto-e-analise-de-algoritmos/algoritmos-de-ordenacao.md) que vamos ver podem ser medidos através de:

- Complexidade de tempo de execução;

- Complexidade de espaço utilizado: quantidade de espaço adicional de memória necessária (além do array de entrada);

- Estabilidade: se mantém a ordem relativa dos elementos iguais na entrada;

  - Exemplo: No caso do exemplo do hospital, se cada elemento(pessoa) tem uma prioridade, é esperado que pessoas de mesma prioridade continuem na mesma ordem que chegaram. Portanto, ao ordenar pela prioridade, o algoritmo é estável se cada elemento de mesma prioridade se mantém na mesma ordem antes de ordenar.

- In-place vs Out-of-place:

  - In-place: Não requer memória extra significativa.

  - Out-of-place: Requer uma estrutura auxiliar para armazenar os elementos ordenados;

- Performance em diferentes tamanhos de entrada: Alguns algoritmos podem ser melhores que outros para quantidades pequenas ou grandes de dados.

Existem outros tipos de características relevantes, como adaptabilidade e paralelização, mas não serão abordados aqui. Legal, vamos para os algoritmos!

<a id="selection-sort"></a>
<a id="secao-16"></a>

## 3.2 Selection Sort

- **Ideia**

  - Percorre a lista até encontrar o menor elemento;

  - Troca esse elemento com o primeiro da lista;

  - Repete a ideia para os próximos elementos.

<a id="secao-17"></a>

## img

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

<a id="insertion-sort"></a>
<a id="secao-18"></a>

## 3.3 Insertion Sort

- **ideia**

  - Considera o primeiro elemento como ordenado;

  - Insere o próximo elemento na posição correta na parte ordenada;

  - Repete o processo para o restante dos elementos.

<a id="secao-19"></a>

### img

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

<a id="bubble-sort"></a>
<a id="secao-20"></a>

## 3.4 Bubble Sort

- **ideia**

  - Percorre a lista e compara elementos adjacentes, trocando se estiverem fora de ordem;

  - Repete o processo até que esteja ordenado(pense que se tivessemos o maior elemento como primeiro da fila, teríamos n trocas).

<a id="secao-21"></a>

### img

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

<a id="comparacao-entre-algoritmos-de-ordenacao"></a>
<a id="secao-22"></a>

## 3.5 Comparação entre algoritmos de ordenação

Esses algoritmos, embora didáticos, são ineficientes para grandes conjuntos de dados. Nas próximas seções, abordaremos algoritmos mais avançados, como Merge Sort e Quick Sort, que possuem melhor desempenho. Vamos comparar os algoritmos que vemos até agora:

|                |                 |                         |          |           |
|----------------|-----------------|-------------------------|----------|-----------|
| Algoritmo      | Melhor caso     | Pior caso               | Estável? | In-place? |
| Selection Sort | $\Omega(n^{2})$ | $O\left( n^{2} \right)$ | Não      | Sim       |
| Insertion Sort | $\Omega(n)$     | $O\left( n^{2} \right)$ | Sim      | Sim       |
| Bubble Sort    | $\Omega(n)$     | $O\left( n^{2} \right)$ | Sim      | Sim       |

Fazendo uma rápida análise, vemos que não temos diferenças aparentes nas características entre Insertion Sort e Bubble Sort, enquanto o Selection Sort é pior que os dois.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [2. Tipos Abstratos de Dados](tipos-abstratos-de-dados.md)
- Próximo: [4.0 Ordeanção avançada](ordeancao-avancada.md)
