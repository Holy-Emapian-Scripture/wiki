---
layout: "default"
title: "Bucket Sort — Algoritmos de Ordenação"
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
ordem_na_trilha: 24
---

[Projeto e Análise de Algoritmos](../../index.md) · [Algoritmos de Ordenação](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-29"></a>

# Bucket Sort

Esse algoritmo vai utilizar de hash tables para fazer ordenação de números potencialmente uniformes. Vamos pegar uma sequência de números **fracionários** $v$ com $n$ elementos e dividí-la em $n$ grupos (baldes).

![Lista de valores em $\lbrack 0,1)$ para exemplificação do algoritmo Bucketsort](../../assets/fractions-list.png)

*Figura 35. Lista de valores em $\lbrack 0,1)$ para exemplificação do algoritmo Bucketsort*

Vamos pressupor que os valores estão **todos** normalizados entre $\lbrack 0,1\rbrack$

- Criar um vetor $b$ com tamanho $n$

  - Cada elemento de $b$ é uma lista encadeada

- Para cada elemento $v\lbrack i\rbrack$

  - Inserir em $b$ na posição $\left\lfloor {n \cdot v\lbrack i\rbrack} \right\rfloor$

- Para cada lista $b\lbrack i\rbrack$

  - Ordenar os seus elementos utilizando algum algoritmo conhecido

    - Ex: Insertion Sort

- Para cada lista $b\lbrack i\rbrack$

  - Para cada elemento $j$ de $b\lbrack i\rbrack$

    - Inserir na lista original $v$

``` cpp
void bucketSort(float v[], int n) {
  vector<float> b[n];
  for (int i = 0; i < n; i++) {
    int inx = n * v[i];
    b[inx].push_back(v[i]);
  }
  for (int i = 0; i < n; i++) {
    insertionSort(b[i]);
  }
  int index = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < b[i].size(); j++) {
      v[index++] = b[i][j];
    }
  }
}
```

O algoritmo inicia criando um vetor `b`(um array de n buckets, e cada bucket é um std::vector) de tamanho `n`, e após declara um **inteiro**(vai servir como a função piso) e multiplica o elemento no índice `i` por `n`, Exemplo: `v[i] = 0.23` e `n = 10`, então `inx = 2`.

Após adicionar cada elemento à seu respectivo bucket, ordena cada bucket com o algoritmo insertionSort e, por fim, faz dois fors, percorrendo cada bucket no de fora e cada elemento do bucket no de dentro, e como estão ordenados, apenas os adiciona na lista original.

Podemos avaliar o desempenho do algoritmo através da seguinte função: $$T(n) = \Theta(n) + \sum_{i = 0}^{n - 1}n_{i}^{2}$$ Portanto, temos que:

- O melhor caso é $\Theta(n)$ - cada balde recebe exatamente um elemento.

- O pior caso é $\Theta(n^{2})$ - um único balde recebe n elementos.

- O caso médio é $\Theta(n)$ - considerando a distribuição uniforme esperada, poucos elementos caem no mesmo balde.

- Exige $O(n)$ de espaço adicional.

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Radix Sort](../radix-sort/index.md)
- Próximo: [Algoritmos de Seleção](../../algoritmos-de-selecao/index.md)
