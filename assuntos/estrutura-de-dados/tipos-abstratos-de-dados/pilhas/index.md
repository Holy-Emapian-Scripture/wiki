---
layout: "default"
title: "2.1 Pilhas — 2. Tipos Abstratos de Dados"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 6
---

[Estrutura de Dados](../../index.md) · [2. Tipos Abstratos de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-6"></a>

# 2.1 Pilhas

Uma pilha é uma Estrutura de Dados que segue a política LIFO(Last in, First Out), ou seja, o último elemento adicionado da pilha é o primeiro a ser removido.

Algumas aplicações:

1.  Controle de chamadas de funções;

2.  Fazer/Desfazer (ctrl y/ctrl z);

3.  Navegação;

Enfim, vamos analisar a estrutura de dados desse TAD:

``` cpp
struct Stack {
    int * data;
    int maxSize;
    int top;
};
```

Temos um ponteiro que aponta para a pilha, um inteiro que guarda o tamanho máximo da pilha e um inteiro e outro inteiro que aponta para o topo(a quantidade de elementos na pilha atualmente).

Além disso, aqui vai algumas funções básicas dessa Estrutura:

- Inicialização da Pilha - apenas declaramos uma nova pilha, apontamos cada elemento da lista para seu respectivo elemento e a retornamos:

``` cpp
Stack* initializationStack(int maxSize) {
    Stack * s = new Stack();
    s->data = new int[maxSize];
    s->maxSize = maxSize;
    s->top = -1;
    return s;
}
```

- Push de um elemento - Se a pilha não estiver cheia, incrementamos a contagem do topo e acessamos o próximo elemento após o topo e colocamos o value lá:

``` cpp
int pushStack(Stack *s, int value) {
    if (s->top == s->maxSize - 1) {
        return 0; // Full stack
    }
    s->top += 1;
    s->data[s->top] = value;
    return 1;
}
```

- Remoção de um elemento - Caso a pilha não esteja vazia, acessamos o ponteiro value usando o último elemento da pilha e decrementamos da contagem de topo:

``` cpp
int popStack(Stack *s, int *value) {
    if (s->top == -1) {
        return 0; // Empty stack
    }
    *value = s->data[s->top];
    s->top -= 1;
    return 1;
}
```

- Busca de um elemento - Se a pilha não estiver vazia, apenas retornamos o último elemento colocado da lista:

``` cpp
int peekStack(const Stack *s, int *value) {
    if (s->top == -1){
        return 0; // Empty stack
    }
    *value = s->data[s->top];
    return 1;
}
```

- Destruição da pilha - Deleta o array e a pilha:

``` cpp
void destroyStack(Stack* s) {
    delete[] s->data;
    delete s;
}
```

O básico é isso, terão coisas mais legais nos exercícios.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [2. Tipos Abstratos de Dados](../index.md)
- Próximo: [2.2 Filas](../filas/index.md)
