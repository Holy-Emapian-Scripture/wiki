---
layout: "default"
title: "2.5 Lista (simplesmente) encadeada — 2. Tipos Abstratos de Dados"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 10
---

[Estrutura de Dados](../../index.md) · [2. Tipos Abstratos de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-10"></a>

# 2.5 Lista (simplesmente) encadeada

Uma lista encadeada é uma lista que usa ponteiros que indicam o próximo elemento da lista, sem depender uma estrutura de dados pronta que define o tamanho da lista na inicialização.

Algumas aplicações:

1.  As mesmas de filas e pilhas(podem ser feitas com listas encadeadas);

2.  Tabelas Hash;

Vamos pra estrutura!

``` cpp
struct Node {
    Node* next;  
    int value; 
};

struct SingleLinkedList {
    Node* head;
    int size;
};
```

Note que agora são necessárias duas estruturas, uma para o nó, onde temos um inteiro que armazena o valor do nó(tal qual um elemento de um array) e o ponteiro para o próximo elemento, e outra para administrar a lista em si, que controla o ponteiro inicial, e um inteiro que informa o tamanho da lista.

Agora que você já está mais familiarizado com a aparência das funções(verificações básicas, interações com ponteiros), vou deixar de comentar algumas parte do código, já que são mais simples e, além disso, as funções acabam ficando maiores. Vamos as funções básicas:

- Inicialização da lista encadeada - Pela primeira vez, vemos uma atribuição de nullptr, que, como diz o próprio nome, aponta para um ponteiro nulo(todos os nullptr do mesmo código apontam para o mesmo local).

``` cpp
SingleLinkedList* InitializationSLList() {
    SingleLinkedList* list = new SingleLinkedList;
    list->head = nullptr;
    list->size = 0;
    return list;
}
```

- Push de um elemento:

  - Front - Como queremos adicionar na frente, apenas declaramos um novo nó e fazemos ele apontar para o head da lista, após isso atualizamos o head para ser o novo nó e incrementamos o tamanho.

  - End - Agora o next do novo nó será vazio, e se a lista não for vazia, criamos um nó temporário que serve para andar pela lista, começando pelo head. Enquanto next do nó temporário não for nullptr, significa que não chegamos ao final, e portanto, a lista não chegou ao fim. Quando chegamos ao ponteiro no fim da lista, então colocamos o next dessa lista como o nó criado

``` cpp
void pushFrontSLList(SingleLinkedList* list, int value) {
    Node* newNode = new Node;
    newNode->value = value;
    newNode->next = list->head;    
    list->head = newNode;
    list->size++;
}

void pushEndSLList(SingleLinkedList* list, int value) {
    Node* newNode = new Node;
    newNode->value = value;
    newNode->next = nullptr;
    if (list->head == nullptr) {
        list->head = newNode;
    } else {
        Node* temp = list->head;
        while(temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
    list->size++;
}
```

- Remoção de um elemento:

  - Front - Nesse caso, sequer precisamos saber o valor a ser deletado, já que será o elemento do início da lista. Salvamos o primeiro elemento da lista, e dizemos que agora a head da lista é o próximo elemento depois do head, e agora podemos deletar o elemento antes salvo.

  - Middle/end - Agora precisamos do valor a ser deletado, e após salvarmos o ponteiro atual da lista, fazemos um while que deve encontrar o valor exato, e, para isso, devemos verificar se o next do ponteiro é nulo e se o valor do ponteiro é exatamente o valor procurado. Se entrarno próximo if, significa que parou na primeira condição do while e, portanto, o ponteiro é nulo. Caso contrário, é porque encontramos o nó de valor desejado, portanto salvamos o ponteiro, atualizamos o current e deletamos o nó do valor.

``` cpp
void popFrontSLList(SingleLinkedList* list) {
    if (list->head == nullptr) {
        return -1; // Empty queue
    }
    Node* temp = list->head;
    list->head = list->head->next;
    delete temp;
    list->size--;
}

void popEndSLList(SingleLinkedList* list, int value) {
    if (list->head == nullptr) {
        return;
    }
    Node* current = list->head;
    while (current->next != nullptr && current->next->value != value) {
        current = current->next;
    }
    if (current->next == nullptr) {
        return;
    }
    Node* temp = current->next;
    current->next = current->next->next;
    delete temp;
    list->size--;
}
```

Note que aqui temos o popEnd seria análago ao popMiddle, já que, de qualquer forma, teríamos que percorrer a lista inteira para encontrar o elemento, dado que provavelmente não sabemos onde ele está.

- Busca de um elemento - Percorre toda a lista usando um ponteiro auxiliar até achar o valor, retornando true. Caso não achar, retorna false.

``` cpp
bool searchSLList(SingleLinkedList* list, int value) {
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

- Destruição da lista - Em geral isso não é muito útil, já que precisamos passar elemento a elemento para deletar, e que essa lista não usa uma estrutura pronta como array.

``` cpp
void deleteSLList(SingleLinkedList* list) {
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

- Anterior: [2.4 Comparação entre TADs](../comparacao-entre-tads/index.md)
- Próximo: [2.6 Lista encadeada circular](../lista-encadeada-circular/index.md)
