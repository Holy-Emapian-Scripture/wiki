---
layout: "default"
title: "Árvores Binárias de Busca — Algoritmos de busca"
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
ordem_na_trilha: 10
---

[Projeto e Análise de Algoritmos](../../index.md) · [Algoritmos de busca](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-10"></a>

# Árvores Binárias de Busca

**Definição: Árvores de busca**

São uma classe específica de árvores que seguem algumas características:

- A chave de cada nó é maior ou igual a chave da raiz da sub-árvore esquerda.

- A chave de cada nó é menor ou igual a chave da raiz da sub-árvore direita

`left.key <= key <= right.key`

![Exemplo de árvore binária de busca(ordenada)](../../assets/binary-tree-example.png)

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

[Trilha: A1](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Árvores](../arvores/index.md)
- Próximo: [Tabela Hash](../../tabela-hash/index.md)
