---
layout: "default"
title: "2.2 Filas — 2. Tipos Abstratos de Dados"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 7
---

[Estrutura de Dados](../../index.md) · [2. Tipos Abstratos de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# 2.2 Filas

Uma fila é um tipo de Estrutura de Dados que segue a política FIFO(First IN, First Out), ou seja, o primeiro alemento a ser adicionado na fila é também o primeiro a ser removido.

Algumas aplicações:

1.  Assistir mais tarde (YouTube);

2.  Gerenciamento de entrada em eventos;

3.  Sistema de atendimento de Bancos;

Enfim, vamos analisar a estrutura desse TAD:

``` cpp
struct Queue {
    int* data;
    int maxSize;
    int size;
};
```

Análogo a pilha, a estrutura contém um ponteiro para o array, um inteiro que guarda o tamanho máximo pilha e outro inteiro que guarda o tamanho atual da pilha.

Ok, vamos para as funções básicas dessa estrutura:

- Inicialização da fila - Apenas inicia uma nova fila e declara cada variável com seu respectivo valor, e, por fim, retorna a fila.

``` cpp
Queue * initializationQueue(int maxSize) {
    Queue * q = new Queue();
    q->data = new int[maxSize];
    q->maxSize = maxSize;
    q->size = 0;
    return q;
}
```

- Push de um elemento - Se a fila estiver cheia, não há nada mais a fazer, caso contrário, adicionamos no fim da fila o valor value e incrementamos a quantidade de elementos na lista.

``` cpp
int pushQueue(Queue *q, int value){
    if (q->size == q->maxSize) {
        return 0; // Full queue
    }
    q->data[q->size] = value;
    q->size += 1;
    return 1;
}
```

Remoção de um elemento - Caso a fila não esteja vazia, salva o primeiro valor adicionado na fila atual, e depois abrimos um for para mover cada item da fila um elemento atrás. Por fim, decrementa o tamanho da fila.

``` cpp
int popQueue(Queue *q, int *value) {
    if (q->size == 0) {
        return 0; // Empty queue
    }

    *value = q->data[0];
    for (int i = 1; i < q->size; i++) {
        q->data[i - 1] = q->data[i];
    }
    q->size -= 1;
    return 1;
}
```

- Busca de um elemento - Caso a fila não esteja vazia, apenas seleciona o primeiro elemento adicionado a fila atual e o aloca na variável value.

``` cpp
int peekQueue(const Queue *q, int *value) {
    if (q->size == 0) {
        return 0; // Empty queue
    } 
    *value = q->data[0];
    return 1;
}
```

- Destruição da fila - Destrói o array e depois a fila.

``` cpp
void destroy(Queue* q) {
    delete[] q->data;
    delete q;
}
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [2.1 Pilhas](../pilhas/index.md)
- Próximo: [2.3 Fila circular](../fila-circular/index.md)
