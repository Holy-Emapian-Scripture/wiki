---
layout: "default"
title: "2.7 Lista duplamente encadeada — 2. Tipos Abstratos de Dados"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 12
---

[Estrutura de Dados](../../index.md) · [2. Tipos Abstratos de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-12"></a>

# 2.7 Lista duplamente encadeada

Sabendo que você provavelmente já entendeu o conceito, vamos às aplicações:

1.  Todas as outras anteriores;

2.  Botões de “avançar” e “voltar” num site;

3.  Músicas/filmes de uma playlist.

Legal, vamos para sua estrutura:

``` cpp
struct Node {
    int value;
    Node* next;
    Node* prev;
};

struct DoubleLinkedList {
    Node* head;
    Node* tail;
    int size;
};
```

Bastante semelhante a lista simplesmente encadeada, a menos do ponteiro representando o anterior no nó(chamado de prev) e na lista(chamado de tail).

- Inicialização da lista duplamente encadeada - Análogo a simplesmente encadeada, a menos do tail.

``` cpp
DoubleLinkedList* InitializationDLList() {
    DoubleLinkedList* list = new DoubleLinkedList;
    list->head = nullptr;
    list->tail = nullptr;
    list->size = 0;
    return list;
}
```

- Push de um elemento:

  - Front - Aqui, quando verificamos se a lista não é vazia, como queremos atualizar na frente, apontamos o previous do head para o nó a ser adicionado, e depois atualizamos o head da lista como o novo nó. Depois verificamos se ela está vazia e, se estiver, após adicionar o nó como head, colocamos o nó como tail e incrementamos o size.

  - End - Criamos o novo nó, verificamos se a lista é nula e, caso for, colocamos ele como o head. Após isso, verificamos se o tail não é nulo, ou seja, se a lista não é vazia. Caso não seja, então o tail da lista aponta para o nó adicionado. Atualizamos o tail após isso e incrementamos o size.

``` cpp
void pushFrontDLList(DoubleLinkedList* list, int value) {
    Node* newNode = new Node{};
    newNode->value = value;
    newNode->next = list->head;
    newNode->prev = nullptr;
    if (list->head != nullptr) {
        list->head->prev = newNode;
    }
    list->head = newNode;
    if (list->tail == nullptr) {
        list->tail = newNode;
    }
    list->size++;
}

void pushEndDLList(DoubleLinkedList* list, int value) {
    Node* newNode = new Node{};
    newNode->value = value;
    newNode->next = nullptr;
    newNode->prev = list->tail;

    if (list->head == nullptr) {
        list->head = newNode;
    }
    if (list->tail != nullptr) {
        list->tail->next = newNode;
    }
    list->tail = newNode;
    list->size++;
}
```

- Remoção de um elemento:

  - Front - Após verificarmos se a lista não esta vazia, criamos um ponteiro temporário que salvará o ponteiro a ser deletado, logo após atualizamos o head da lista, e com ela atualizada, verificamos se o head atual não é nulo, pois caso ele não seja, devemos atualizar também o prev da nova head. Caso ele seja nulo, então o tail também deve ser atualizado como nulo. Deletamos o ponteiro antigo e decrementamos o size.

  - End - Fazemos literalmente a mesma coisa, só que olhando para o tail. Note como a estrutura é parecida

``` cpp
void popFrontDLList(DoubleLinkedList* list) {
    if (list->head == nullptr) {
        return;
    }
    Node* temp = list->head;
    list->head = list->head->next;
    if (list->head != nullptr) {
        list->head->prev = nullptr;
    } else {
        list->tail = nullptr;
    }
    delete temp;
    list->size--;
}

void popEndDLList(DoubleLinkedList* list) {
    if (list->tail == nullptr) {
        return;
    }
    Node* temp = list->tail;
    list->tail = list->tail->prev;
    if (list->tail != nullptr) {
        list->tail->next = nullptr;
    } else {
        list->head = nullptr;
    }
    delete temp;
    list->size--;
}
```

Note que não colocamos as funções de push e pop no meio da lista, já que isso quebraria a ideia dessas operações serem $O(1)$, pois teríamos que percorrer toda a lista até encontrar o elemento do meio, se fosse o caso. Além disso, um push no meio não faz sentido, seria algo como furar fila, enquanto o pop no meio de uma fila pode realmente acontecer, como uma desistência. Aqui vai o código do pop no meio da lista:

``` cpp
void popMiddleDLList(DoubleLinkedList* list, int value) {
    if (list->head == nullptr) {
        return;
    }
    Node* current = list->head;
    while (current != nullptr && current->value != value) {
        current = current->next;
    }
    if (current == nullptr) {
        return;
    }
    current->prev->next = current->next;
    if (current->next != nullptr) {
        current->next->prev = current->prev;
    }
    delete current;
    list->size--;
}
```

- Busca de um elemento - Análogo a lista simplesmente encadeada.

``` cpp
bool searchDLList(DoubleLinkedList* list, int value) {
    Node* current = list->head;
    while (current != nullptr) {
        if (current->value == value) {
            return true;
        }
        current = current->next;
    }
    return false;
}
```

- Destruição da lista - Análogo a lista simplesmente encadeada.

``` cpp
void deleteDLList(DoubleLinkedList* list) {
    Node* current = list->head;
    while (current != nullptr) {
        Node* temp = current;
        current = current->next;
        delete temp;
    }
    delete list;
}
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [2.6 Lista encadeada circular](../lista-encadeada-circular/index.md)
- Próximo: [2.8 Comparação entre arrays e listas encadeadas](../comparacao-entre-arrays-e-listas-encadeadas/index.md)
