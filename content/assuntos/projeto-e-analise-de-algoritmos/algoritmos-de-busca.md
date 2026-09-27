---
layout: "default"
title: "Algoritmos de busca"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A1.md"
trilha: "../../../trilhas/projeto-e-analise-de-algoritmos/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
revisao: "Thalis Ambrosim Falqueto"
ano_original: 2025
ordem_na_trilha: 7
---

[Projeto e Análise de Algoritmos](index.md)

<!-- wiki:original:inicio -->

<a id="secao-7"></a>

# Algoritmos de busca


<a id="busca-em-um-vetor-ordenado"></a>
<a id="secao-8"></a>

## Busca em um vetor ordenado

Dado um vetor ordenado de inteiros:

``` cpp
int* v = { 2, 5, 9, 18, 23, 27, 32, 33, 37, 41, 43, 45 };
```

Queremos escrever um algoritmo que recebe o vetor $v$, um número $x$ e retorna o índice de $x$ no vetor $v$ se $x \in v$. Temos dois algorimtos principais para esse problema

**BUSCA LINEAR**

``` cpp
int linear_search(const int v[], int size, int x) {
  for (int i = 0; i < size; i++) {
    if (v[i] == x) {
      return i;
    }
  }
  return -1;
}
```

No pior caso, esse algoritmo tem complexidade $\Theta(n)$

- Nota: Um erro comum de interpretação é se perguntar por quê foi usado um $\Theta(n)$ se, claramente, o algoritmo é $\Omega(1)$. Acontece que estamos analisando o pior caso, ou seja, quando o elemento é o último da lista. Por isso, não existem análises de pior e melhor caso se sabemos que teremos que percorrer $n$ elementos até chegar no inteiro que estamos procurando, por isso, no caso do pior caso, o algoritmo tem complexidade $\Theta(n)$.

Porém, se considerarmos uma lista ordenada, podemos fazer algo mais inteligente. Começamos comparando o elemento do meio do vetor e dependendo se o valor que queremos buscar é maior ou menor comparado ao avaliado, podemos ignorar a parte oposta do vetor.Ou seja, o algoritmo consiste em avaliar se o elemento buscado ($x$) é o elemento no meio do vetor ($m$), e caso não seja executar a mesma operação sucessivamente para a metade superior (caso $x > m$) ou inferior (caso $x < m$).

**BUSCA BINÁRIA**

``` cpp
int search(int v[], int leftInx, int rightInx, int x) {
  int midInx = (leftInx + rightInx) / 2;
  int midValue = v[midInx];
  if (midValue == x) {
    return midInx;
  }
  if (leftInx >= rightInx) {
    return -1;
  }
  if (x > midValue) {
    return search(v, midInx + 1, rightInx, x);
  } else {
    return search(v, leftInx, midInx - 1, x);
  }
}
```

Podemos escrever a complexidade da função como: $$T(n) = T\left( \frac{n}{2} \right) + c$$

Pense no método de Árvore de Recursão, que aprendemos há pouco. Note que, nesse caso, $T(n)$ só se separa em um termo, e, a cada iteração, temos o tamanho do vetor dividido por $2$ e um termo $+ c$. Portanto, nosso custo é $\frac{n}{2^{k}}$ e queremos achar o k que satisfaz esse termo chegar ao caso base, $T(1)$. Logo, $$\frac{n}{2^{k}} = 1 \Rightarrow \log(n) - \log(2^{k}) = 0 \Rightarrow \log(n) = k\log(2) \Rightarrow k = \frac{\log(n)}{\log(2)}$$

Portanto, temos o custo por nó de $c$, e assim o custo total fica: $$\sum_{k = 1}^{\log(n)}c = c\sum_{k = 1}^{\log(n)} = c\log(n)$$

Então, obtemos que $T(n) = O\left( \log(n) \right)$ Num contexto de melhor caso, acharíamos o valor na primeira iteração e, portanto, $T(n) = \Omega(1)$.

<a id="arvores"></a>
<a id="secao-9"></a>

## Árvores

Uma árvore binária consiste em uma estrutura de dados capaz de armazenar um conjunto de nós.

- Todo nó possui uma chave;

- Opcionalmente um valor (dependendo da aplicação);

- Cada nó possui referências para dois filhos;

- Sub-árvores da direita e da esquerda;

- Toda sub-árvore também é uma árvore.

![Exemplo de árvore binária](assets/tree-example.png)

*Figura 3. Exemplo de árvore binária*

Um nó sem pai é uma **raíz**, enquanto um nó sem filhos é um nó **folha**

**Definição: Altura do nó**

Distância entre um nó e a folha mais afastada. A altura de uma árvore é a algura do nó raíz

![Exemplificação de altura em árvore binária](assets/node-height-example.png)

*Figura 4. Exemplificação de altura em árvore binária*

**Teorema**

Dada uma árvore de altura $h$, a quantidade máxima de nós $n_{\text{max}}$ e mínima $n_{\text{min}}$ são: $$\begin{array}{r} n_{\text{min }} = h + 1 \\ n_{\text{max }} = 2^{h + 1} - 1 \end{array}$$

Para $n_{\text{min}}$, pense apenas numa lista encadeada. Ela é uma árvore, certo? Ela é o menor caso possível intuitivamente e tem $h + 1$ nós.

Para $n_{\text{max}}$, pense numa árvore completa, claro. Se isso ocorrer, temos $2^{0}$ nós na altura $0$, $2^{1}$ nós na altura $1$, e assim sucessivamente. Temos então um somatório de nós até a altura $h$:

$$
S_{h} = \sum_{k = 0}^{k = h}2^{k} = 1.\frac{2^{h + 1} - 1}{2 - 1} = 2^{h + 1} - 1
$$

pela forma da soma da PG.

**Definição**

Uma árvore está **balanceada** quando a altura das subárvores de um nó apresentam uma diferença de, no máximo, $1$

**Teorema**

Dada uma árvore com $n$ nós e balanceada, a sua altura $h$ será, no máximo: $$h = \log(n)$$

**Demonstração**

Seja $N(h)$ o número mínimo de nós de uma árvore balanceada de altura $h$. Temos a [recorrência](recorrencia.md) (pior caso):

$$
N(h) = 1 + N(h - 1) + N(h - 2)
$$

O $1$ vem da raiz, $N(h - 1)$ de alguma das sub-árvores, e $N(h - 2)$ vem da outra sub-árvore, com a distância entre as duas de $1$.

Ainda, temos que $N(0) = 1$ e $N(1) = 2$,

**Hipótese:** $N(h) \geq 2^{\frac{h}{2}}$ para todo $h \geq 0$.

**Base:** Para $h = 0$: $N(0) = 1 \geq 2^{0}$. Para $h = 1$: $N(1) = 2 \geq 2^{\frac{1}{2}}$.

**Passo indutivo:** suponha válido para $h - 1$ e $h - 2$. Então

$$
N(h) \geq N(h - 1) + N(h - 2) \geq 2^{\frac{h - 1}{2}} + 2^{\frac{h - 2}{2}} = 2^{\frac{h - 2}{2}}\left( 2^{\frac{1}{2}} + 1 \right).
$$

Como $2^{\frac{1}{2}} + 1 > 2$, segue $N(h) \geq 2^{\frac{h}{2}}$.

Se a árvore tem $n$ nós então $n \geq N(h) \geq 2^{\frac{h}{2}}$, logo

$$
n \geq 2^{\frac{h}{2}} \Rightarrow \log_{2}(n) \geq \frac{h}{2}\log_{2}(2) \Rightarrow h \leq 2\log_{2}(n)
$$

Portanto, $h = O\left( \log n \right)$.

Essa hipótese é um pouco não trivial, mas se quiser, também é possível provar reconhecendo que os temos $N(h) = N(h - 1) + N(h - 2)$ lembram bastante Fibonacci.

Agora, vamos ver algumas formas de andar por essa árvore binária, ou seja, andar corretamente de nó em nó usando a estrutura que criamos, além de formas para descobrir sua altura. Para códigos posteriores, considere a seguinte estrutura:

``` cpp
class Node {
  public:
    Node(int key, char data)
      : m_key(key)
      , m_data(data)
      , m_leftNode(nullptr)
      , m_rightNode(nullptr)
      , m_parentNode(nullptr) {}
    Node & leftNode() const { return * m_leftNode; }
    void setLeftNode(Node * node) { m_leftNode = node; }

    Node & rightNode() const { return * m_rightNode; }
    void setRightNode(Node * node) { m_rightNode = node; }

    Node & parentNode() const { return * m_parentNode; }
    void setParentNode(Node * node) { m_parentNode = node; }

  private:
    int m_key;
    char m_data;
    Node * m_leftNode;
    Node * m_rightNode;
    Node * m_parentNode;
};
```

Temos alguns tipos de problemas para trabalhar em cima das árvores e suas soluções:

**Problema**: Dada uma árvore binária A com n nós encontre a sua altura

``` cpp
int nodeHeight(Node * node) {
  if (node == nullptr) {
    return -1;
  }

  int leftHeight = nodeHeight(node->leftNode());
  int rightHeight = nodeHeight(node->rightNode());

  if (leftHeight < rightHeight) {
    return rightHeight + 1;
  } else {
    return leftHeight + 1;
  }
}
```

A complexidade dessa solução é $\Theta(n)$, pois independente da ideia, precisamos passar por todos os nós para termos certeza da altura.

**Problema**: Dada uma árvore binária $A$ imprima a chave de todos os nós através da busca em profundidade. Desenvolva o algoritmo para os 3 casos: Em ordem, pré-ordem, pós-ordem

Relembrando os 3 casos que você provavelmente já viu em Estrutura de Dados:

- Em ordem: Esquerda -\> Raizz -\> Direita

**EM ORDEM**

``` cpp
void printTreeDFSInorder(class Node * node) {
  if (node == nullptr) {
    return;
  }
  printTreeDFSInorder(node->leftNode());
  cout << node->key() << " ";
  printTreeDFSInorder(node->rightNode());
}
```

- Pré-ordem : Raiz -\> Esquerda -\> Direita

**PRÉ-ORDEM**

``` cpp
void printTreeDFSPreorder(class Node * node) {
  if (node == nullptr) {
    return;
  }
  cout << node->key() << " ";
  printTreeDFSPreorder(node->leftNode());
  printTreeDFSPreorder(node->rightNode());
}
```

- Pós - ordem: Esquerda -\> Direita -\> Raiz

**PÓS-ORDEM**

``` cpp
void printTreeDFSPostorder(class Node * node) {
  if (node == nullptr) {
    return;
  }
  printTreeDFSPostorder(node->leftNode());
  printTreeDFSPostorder(node->rightNode());
  cout << node->key() << " ";
}
```

**Problema**: dada uma árvore binária $A$ imprima a chave de todos os nós através da busca em largura. Imagino que você saiba, mas relembrando, busca em largura nada mais é que a busca de altura em altura, começando pela raiz.

``` cpp
void printTreeBFSWithQueue(Node * root) {
  if (root == nullptr) {
    return;
  }
  queue<Node*> queue;
  queue.push(root);
  while (!queue.empty()) {
    Node * node = queue.front();
    cout << node->key() << " ";
    queue.pop();
    Node * childNode = node->leftNode();
    if (childNode) {
      queue.push(childNode);
    }
    childNode = node->rightNode();
    if (childNode) {
      queue.push(childNode);
    }
  }
}
```

<a id="arvores-binarias-de-busca"></a>
<a id="secao-10"></a>

## Árvores Binárias de Busca

**Definição: Árvores de busca**

São uma classe específica de árvores que seguem algumas características:

- A chave de cada nó é maior ou igual a chave da raiz da sub-árvore esquerda.

- A chave de cada nó é menor ou igual a chave da raiz da sub-árvore direita

`left.key <= key <= right.key`

![Exemplo de árvore binária de busca(ordenada)](assets/binary-tree-example.png)

*Figura 5. Exemplo de árvore binária de busca(ordenada)*

Então queremos utilizar essa árvore para poder procurar valores. Na verdade, ela é bem parecida com o caso de aplicar uma busca binária em um vetor ordenado.

**Problema**: dada uma árvore binária de busca $A$ com altura $h$ encontre o nó cuja chave seja $k$.

**BUSCA EM ÁRVORE BINÁRIA (RECURSÃO)**

``` cpp
Node * binaryTreeSearchRecursive(Node * node, int key) {
  if (node == nullptr || node->key() == key) {
    return node;
  }
  if (node->key() > key) {
    return binaryTreeSearchRecursive(node->leftNode(), key);
  } else {
    return binaryTreeSearchRecursive(node->rightNode(), key);
  }
}
```

Esse algoritmo tem complexidade $\Theta(h)$ no pior caso.

**BUSCA EM ÁRVORE BINÁRIA (ITERATIVO)**

``` cpp
Node * binaryTreeSearchIterative(Node * node, int key) {
  while (node != nullptr && node->key() != key) {
    if (node->key() > key) {
      node = node->leftNode();
    } else {
      node = node->rightNode();
    }
  }
  return node;
}
```

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Recorrência](recorrencia.md)
- Próximo: [Tabela Hash](tabela-hash.md)
