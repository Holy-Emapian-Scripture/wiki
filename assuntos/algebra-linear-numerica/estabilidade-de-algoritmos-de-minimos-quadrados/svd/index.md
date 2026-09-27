---
layout: "default"
title: "SVD — Estabilidade de Algoritmos de Mínimos Quadrados"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 14
---

[Álgebra Linear Numérica](../../index.md) · [Estabilidade de Algoritmos de Mínimos Quadrados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-14"></a>

# SVD

O último algoritmo a ser mencionado foi utilizando a SVD de $A$, que nós vimos (no resumo 1) que parecia ser um algoritmo interessante:

**CÓDIGO**

``` python
U, S, Vh = np.linalg.svd(A, full_matrices=False)
S = np.diag(S)
x = (Vh.T * 1/S) @ (U.T @ b)
print(1-x[-1])
```

**SAÍDA**

    -2.3301211e-07

Olha só! Temos uma precisão ótima! (O algoritmo da SVD é o mais confiável e estável, mesmo que o erro mostrado seja maior do que alguns que obtivemos anteriormente)

**Teorema**

A solução do problema de mínimos quadrados com uma matriz $A$ de posto-completo utilizando o algoritmo de SVD é **backward stable**.

<!-- wiki:original:fim -->

## Conteúdos relacionados

- [Principal Component Analysis — Aprendizado de Máquina](../../../aprendizado-de-maquina/principal-component-analysis/index.md)

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Equações Normais](../equacoes-normais/index.md)
- Próximo: [Problemas de Mínimos Quadrados com Posto-Incompleto](../problemas-de-minimos-quadrados-com-posto-incompleto/index.md)
