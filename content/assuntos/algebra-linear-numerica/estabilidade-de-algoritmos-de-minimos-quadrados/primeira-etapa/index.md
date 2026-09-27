---
layout: "default"
title: "Primeira Etapa — Estabilidade de Algoritmos de Mínimos Quadrados"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 10
---

[Álgebra Linear Numérica](../../index.md) · [Estabilidade de Algoritmos de Mínimos Quadrados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-10"></a>

# Primeira Etapa

Vamos fazer isso na prática. Vamos montar um cenário para a aplicação de cada um dos algoritmos. Vamos pegar $m$ pontos igualmente espaçados entre $0$ e $1$, montamos a <u>[matriz de vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix)</u> desses pontos e aplicamos uma função que tentaremos prever com polinômios:

**CÓDIGO**

<a id="min-squared-algorithms-init"></a>

``` python
import numpy as np
m = 100
n = 15
t = np.linspace(0, 1, m)
A = np.vander(t, n, True)
b = np.exp(np.sin(4*t))/2.00678728e+03
```

Oxe, por que que tem essa divisão esquisita no final? Quando a gente não faz essa divisão, ao fazer a previsão dos coeficientes que aproximam a função, temos que o último coeficiente previsto ($x_{15}$) é igual a `2.00678728e+03`, então, nós dividimos $b$ por esse valor para que o último coeficiente seja igual a $1$ no caso matematicamente correto (Sem erros numéricos), assim poderemos fazer comparações apenas visualizando o último número dos coeficientes calculados.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Estabilidade de Algoritmos de Mínimos Quadrados](../index.md)
- Próximo: [Householder](../householder/index.md)
