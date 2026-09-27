---
layout: "default"
title: "Ortogonalização de Gram-Schmidt — Estabilidade de Algoritmos de Mínimos Quadrados"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 12
---

[Álgebra Linear Numérica](../../index.md) · [Estabilidade de Algoritmos de Mínimos Quadrados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-12"></a>

# Ortogonalização de Gram-Schmidt

A gente também pode tentar resolver pelo método de Gram-Schmidt modificado, vamos ver o que a gente consegue:

**CÓDIGO**

``` python
Q, R = modified_gram_schmidt(A)
x = np.linalg.solve(R, Q.T @ b)
print(1-x[-1])
```

**SAÍDA**

    -0.01726542

Meu amigo, esse erro é **terrível**. O resultado obtido é tenebroso de ruim. O livro comenta também de outro método que envolve fazer umas manipulações em $Q$, mas como o próprio diz que envolve trabalho extra, desnecessário e não deveria ser usado na prática, nem vou comentar sobre aqui.

Mas a gente pode usar um método parecido com o que fizemos antes em unir $A$ e $b$ numa única matriz:

**CÓDIGO**

``` python
Q, R = modified_gram_schmidt(np.c_[A, b])
Qb = R[0:n, n]
R = R[0:n, 0:n]
x = np.linalg.solve(R, Qb)
print(1-x[-1])
```

**SAÍDA**

    -1.3274502852489434e-07

Olha só! Já deu uma melhorada no algoritmo!

**Teorema**

Solucionar o problema de mínimos quadrados de uma matriz $A$ com posto completo utilizando o algoritmo de Gram-Schmidt (Fazendo de acordo como o código anterior mostra em que $Q^{\ast}b$ é implícito) é **backward stable**

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Householder](../householder/index.md)
- Próximo: [Equações Normais](../equacoes-normais/index.md)
