---
layout: "default"
title: "Exercise 3"
tipo: "exercicio"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Exercices/lecture_8/exercises.md"
trilha: "../../../trilhas/estrutura-de-dados/exercicios-aula-8.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 3
---

[Estrutura de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# Exercise 3

<a id="secao-8"></a>

## Solution

<a id="secao-9"></a>

### a)

``` cpp
int a = 0, b = 0;
for (i = 0; i < n; i++) {
    a = a + i;
}
for (j = 0; j < m; j++) {
    b = b + j;
}
```

The algorithm operates in $O(n) + O(m)$, the first

    for

grows linearly with $n$ and the second one grows with $m$.

<a id="secao-10"></a>

### b)

``` cpp
float what2(int *arr, int n) {
    int a = 0;
    for (int i = 0; i < n; i++) {
        if(arr[i] > 10) {
            for (int j = 0; j < n; j++) {
                a += n / 2;
            }
        } else {
            printf("ok :(")
        }
    }
}
```

The algorithm has 2

    for's

with n operations each in a worst-case scenario, therefore it is precisely $\in O(n²)$.

<a id="secao-11"></a>

### c)

``` cpp
int a = 0;
for (int i = 0; i < n; i++) {
    for (int j = n; j > i; j--) {
        a += i + j;
    }
}
```

For $i = 0$ , $j$ goes from $n$ to 0, and the operation a += n/2 is executed $n$ times, for $i = 1$ , $n$ goes from $n$ to 1 and the operation is executed $n - 1$ times and so on, so we have:

$$\sum_{i = 1}^{n - 1}n - i = \frac{n(n + 1)}{2}$$

So the algorithm is $\in O(n²)$.

<a id="secao-12"></a>

### d)

``` cpp
float what4(int *arr, int n) {
    int a = 0;
    for (int i = 0; i < 1000; i++) {
        for (int j = 0; j < 5000; j++) {
            a += i + j;
        }
    }
}
```

Both loops have constant limits, so the total complexity is $O(1)$.

<a id="secao-13"></a>

### e)

``` cpp
int a = 0;
for (int i = n/2; i <= n; i++) {
    for (int j = 2; j <= n; j = j * 2) {
        a += i + j;
    }
}
```

The external loop executes $O(n)$ times, and the internal one $O\left( \log n \right)$. So the total complexity is $O\left( n\log n \right)$.

<a id="secao-14"></a>

### f)

``` cpp
int a = 0, i = n;
while (i > 0) {
    a += i;
    i /= 2;
}
```

At each iteration, i is divided by 2: i = n, n/2, n/4, $\ldots$, 1.

This loop executes $\log_{2}n$ times, and each step does constant work.

Therefore, the time complexity is:

$$O\left( \log_{2}n \right)$$

<a id="secao-15"></a>

### g)

``` cpp
int a = 0, i = n;
while (i > 0) {
    for (int j = 0; j < i; j++) {
        a += i;
    }
    i /= 2;
}
```

At each iteration of the while, the value of i is divided by 2. In the first iteration, the for executes n times, then n/2, n/4, …, until i = 1. The total sum of operations is:

$$T(n) = n + \frac{n}{2} + \frac{n}{4} + \ldots + 1 = 2n - 1inO(n)$$

Therefore, the time complexity of the algorithm is $O(n)$.

<a id="secao-16"></a>

### h)

``` cpp
float soma(float *arr, int n) {
    float total = 0;
    for (int i = 0; i < n; i++) {
        total += arr[i];
    }
    return total;
}
```

The algorithm traverses the array of size $n$ once, performing one addition per element. Therefore, its complexity is linear: $O(n)$.

<a id="secao-17"></a>

### i)

``` cpp
int buscaSequencial(int *arr, int n, int x) {
    for (int i = 0; i < n; i++){
        if (arr[i] == x) {
            return i;
        }
    }
    return -1;
}
```

In the worst case (when $x$ is not in the array), the algorithm goes through all $n$ elements. Thus, its worst-case complexity is $O(n)$.

<a id="secao-18"></a>

#### j)

``` cpp
int buscaBinaria(int *arr, int x, int i, int j) {
    if (i >= j) {
        return ‐1;
    }

    int m = (i + j) / 2;
    if (arr[m] == x) {
        return m;
    } else if ( x < arr[m] ) {
        return buscaBinaria (arr, x, i, m‐1);
    } else {
        return buscaBinaria (arr, x, m+1, j);
    }
}
```

At each recursive call the search space is halved. Thus, the worst-case complexity of binary search is $O\left( \log_{2}n \right)$.

<a id="secao-19"></a>

#### k)

``` cpp
void multiplicacaiMatriz(float **a, float **b, int n, int p, int m, float **x) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            x[i][j] = 0.0;
            for (int k = 0; k < p; k++) {
                x[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}
```

The multiplication of matrices of dimensions $np$ by $pm$ performs $nmp$ multiplications. Therefore, the complexity is $O(nmp)$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Exercícios — aula 8](../../../trilhas/estrutura-de-dados/exercicios-aula-8.md) · [Apresentação e contexto da fonte](../../../trilhas/estrutura-de-dados/exercicios-aula-8.md#apresentacao-original)

- Anterior: [Exercise 2](../exercise-2-exercicios-aula-8/index.md)
- Próximo: [Exercise 4](../exercise-4-exercicios-aula-8/index.md)
