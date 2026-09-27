---
layout: "default"
title: "Householder — Estabilidade de Algoritmos de Mínimos Quadrados"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 11
---

[Álgebra Linear Numérica](../../index.md) · [Estabilidade de Algoritmos de Mínimos Quadrados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-11"></a>

# Householder

O algoritmo padrão para problemas de mínimos quadrados. Vejamos:

**CÓDIGO**

``` python
Q, R = householder_qr(A)
x = np.linalg.solve(R, Q.T @ b)
print(1-x[-1])  # Erro relativo
```

**SAÍDA**

    1.9845992627054443e-09

Temos um erro de grandeza $10^{9}$, porém, no Python, trabalhamos com precisão IEEE 754 ($\varepsilon = 2.220446049250313e - 16$), o que nos mostra um erro de precisão MUITO grande (Ordem de $10^{7}$ de diferença). Porém, aqui nós calculamos $Q$ explicitamente e, no resumo 1, foi comentado que isso normalmente não acontece, então vamos ver se o erro muda ao trocarmos $Q$ por uma versão implícita

**CÓDIGO**

``` python
Q, R = householder_qr(np.c_[A, b])
print(R.shape)
Qb = R[0:n, n]
R = R[0:n, 0:n]
x = np.linalg.solve(R, Qb)
print(1-x[-1])
```

**SAÍDA**

    1.989168163518684e-09

Deu pra ver que da quase a mesma coisa do resultado anterior, ou seja, os erros da fatoração de $A$ são maiores que os de $Q$. Pode ser provado que essas duas variações são **backward stable**. O mesmo vale para uma terceira variação que utiliza do **pivotamento** de colunas (Não é discutido nem no livro, tampouco nesse resumo)

**Teorema**

Deixe um problema de mínimos quadrados em uma matriz de posto completo $A$ ser resolvida por fatoração **Householder** em um computador ideal. O algoritmo é **backward stable** tal que: $$\|(A + \delta A)\widetilde{x} - b\| = \min,\ \ \frac{\|\delta A\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$ para algum $\delta A \in {\mathbb{C}}^{m \times n}$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Primeira Etapa](../primeira-etapa/index.md)
- Próximo: [Ortogonalização de Gram-Schmidt](../ortogonalizacao-de-gram-schmidt/index.md)
