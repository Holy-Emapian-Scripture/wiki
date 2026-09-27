---
layout: "default"
title: "1. Complexidade de algoritmos"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 2
---

[Estrutura de Dados](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-2"></a>

# 1. Complexidade de algoritmos


<a id="notacao-big-o"></a>
<a id="secao-3"></a>

## 1.1 Notação Big O

Para mensurar a quantidade de operações feita num algoritmo, é necessário introduzir a notação de Big O que permanecerá conosco até o fim desse resumo.

Em modos gerais, ela basicamente simplifica o cálculo de toda a função que determina o tempo de execução de um algoritmo pegando o termo de maior grandeza, que determina o pior caso no caso de uma quantidade grande de operações.

Exemplo: Qual a complexidade de execução desse algoritmo?

``` cpp
#include  <iostream>

float media(float arr[], int n) {    
    float total = 0;
    for(int i = 0; i < n; i++) {
        total += arr[i];
        total = total / i    
    }
    return total;
}
```

Vamos contar a quantidade de operações (ignorando que a definição da função, e contando cada operação de mesmo esforço computacional):

Temos a definição da variável total, somando $1$, e, dentro do for, temos outras duas operações feitas (soma e divisão), mas elas dependem do tamanho do array(que tem tamanho n), temos então $2n$ operações ali. Ao fim, damos um return, contando mais $1$.

Logo, chamando de $T(n)$ a função que determina a complexidade de execução total do algoritmo, temos: $T(n) = 1 + 2n + 1 = 2n + 2$

Agora, qual seria o pior caso? Aconteceria se n fosse muito grande, certo? Se n fosse muito grande(tendendo a infinito), as contantes 2 que somam e multiplicam a n não importariam o suficiente e, portanto, dizemos que esse algoritmo tem complexidade de execução $O(n).$

Por fim, a definição formal da notação big O para encontrar o pior caso é: Dizemos que a função $f(n) = O\left( g(n) \right)$ se existir uma constante $c$ e um valor $n_{0}$ tal que $f(n) \leq cg(n).$

<a id="notacao-omega"></a>
<a id="secao-4"></a>

## 1.2 Notação $\Omega$

Ok, entendemos que $O\left( . \right)$ significa a análise do tempo geral de execução no pior caso, mas como seria para analisar o melhor caso? Para isso, usamos a notação $\Omega(.)$.

Exemplo:

``` cpp
int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            return i; 
        }
    }
    return -1; 
}
```

Note que, nesse caso se o elemento estiver no início da fila, teremos a nossa busca satisfeita imediatamente, no caso, $\Omega(1)$. E fica fácil analisar que o pior caso é $O(n)$. Logo, o melhor caso é denotado $\Omega(1)$ e o pior caso é $O(n)$.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [Introdução](../introducao/index.md)
- Próximo: [2. Tipos Abstratos de Dados](../tipos-abstratos-de-dados/index.md)
