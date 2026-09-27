---
layout: "default"
title: "Busca em um vetor ordenado — Algoritmos de busca"
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
ordem_na_trilha: 8
---

[Projeto e Análise de Algoritmos](../../index.md) · [Algoritmos de busca](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-8"></a>

# Busca em um vetor ordenado

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

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Algoritmos de busca](../index.md)
- Próximo: [Árvores](../arvores/index.md)
