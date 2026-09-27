---
layout: "default"
title: "2.3 Fila circular — 2. Tipos Abstratos de Dados"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 8
---

[Estrutura de Dados](../../index.md) · [2. Tipos Abstratos de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-8"></a>

# 2.3 Fila circular

Analisando a função popQueue da fila comum, notamos que existe um for para a realocação dos elementos da fila. Isso causa um problema de uma complexidade de execução de $O(n)$. Para contornar isso, uma boa ideia é a implementação de uma fila circular, com head(cabeça/ponta) e tail(cauda/fim).

As aplicações são as mesmas, portanto, vamos para a estrutura desse TAD:

``` cpp
struct CircularQueue {
    int *data;
    int maxSize;
    int size;
    int head;
    int tail;
};
```

A estrutura é semelhante à fila, a menos de que, agora, temos dois novos inteiros que marcam os índices do head e do tail da fila.

Vamos analisar o que mudam as funções básicas da fila circular:

- Inicialização da fila circular - Análogo a fila, apenas declara as outras variáveis adicionadas na estrutura.

``` cpp
CircularQueue * initializationCircularQueue(int maxSize) {
    CircularQueue * cq = new CircularQueue();
    cq->data = new int[maxSize];
    cq->head = 0;
    cq->tail = -1;
    cq->size = 0;
}
```

- Push de um elemento - Aqui a diferença é que temos que atualizar o tail da fila. Para isso, incrementamos o tail, pois adicionamos algo ao final da fila, e tiramos o módulo em relação ao tamanho da lista, para que o tail “resete” quando o array da fila circular chega ao fim.

``` cpp
int pushCircularQueue(CircularQueue *cq, int value) {
    if (cq->size == cq->maxSize) {
        return 0; // Full circular queue
    }
    cq->tail = (cq->tail + 1) % cq->maxSize;
    cq->data[cq->tail] = value;
    cq->size++;
    return 1;
}
```

- Remoção de um elemento - Agora, não precisamos mais do for, e após salvar o valor no ponteiro de value, atualizamos a cabeça da cauda. Como queremos tirar(não tiramos, já que não deletamos o valor) o primeiro valor da fila, apenas incrementamos o head(usando o mesmo argumento do módulo no push), passando assim a apontar a head para o próximo valor imediatamente após o head antigo.

``` cpp
int popCircularQueue(CircularQueue *cq, int *value) {
    if (cq->size == 0) {
        return 0; // Empty circular queue
    }
    *value = cq->data[cq->head];
    cq->head = (cq->head + 1) % cq->maxSize;
    cq->size--;
    return 1;
}
```

- Busca de um elemento - Nada para mudar aqui.

``` cpp
int peekCicularQueue(CircularQueue *cq, int *value) {
    if (cq->size == 0) {
        return 0; // Empty circular queue
    }
    *value = cq->data[cq->head];
    return 1; 
}
```

- Destruição da fila - Nada para mudar aqui.

``` cpp
void destroyCircularQueue(CircularQueue *cq) {
    delete[] cq->data;
    delete cq;
}
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [2.2 Filas](../filas/index.md)
- Próximo: [2.4 Comparação entre TADs](../comparacao-entre-tads/index.md)
