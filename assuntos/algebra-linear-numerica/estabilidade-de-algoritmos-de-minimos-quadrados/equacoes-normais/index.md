---
layout: "default"
title: "Equações Normais — Estabilidade de Algoritmos de Mínimos Quadrados"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 13
---

[Álgebra Linear Numérica](../../index.md) · [Estabilidade de Algoritmos de Mínimos Quadrados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-13"></a>

# Equações Normais

A gente pode resolver por equações normais, que é o passo inicial para todos os outros métodos né? Vamos ver o que obtemos:

**CÓDIGO**

``` python
x = np.linalg.solve(A.T @ A, A.T @ b)
print(1-x[-1])
```

**SAÍDA**

    1.35207472

Meu amigo, esse erro é **TENEBROSO**, não chegou nem **PERTO** do resultado. Claramente as equações normais são um método **instável** de calcular mínimos quadrados. Vamos dar uma visualizada no porquê isso ocorre:

Suponha que nós temos um algoritmo **backward stable** para o problema de mínimos quadrados com uma matriz $A$ de posto-completo que retorna uma solução $\widetilde{x}$ satisfazendo $\|(A + \delta A)\widetilde{x} - b\| = \min$ para algum $\delta A$ com $\|\delta A\|/\| A\| = O\left( \varepsilon_{\text{machine}} \right)$. Pelo teorema da acurácia de algoritmos backward stable (Resumo 1) e o [\[conditioning-min-squared-problems\]](../../condicionando-problemas-de-minimos-quadrados/o-teorema/index.md#conditioning-min-squared-problems) temos: $$\frac{\|\widetilde{x} - x\|}{\| x\|} = O\left( \left( \kappa + \frac{\kappa^{2}\tan(\theta)}{\eta} \right)\varepsilon_{\text{machine}} \right)$$<a id="normal-equation-algorithm-x-partialerence"></a>

Suponha que $A$ é mal-condicionada. Dependendo dos valores dos híperparâmetros, podem acontecer duas situações diferentes. Se $\tan(\theta)$ for de ordem $1$, então o lado direito da equação [\[normal-equation-algorithm-x-partialerence\]](#normal-equation-algorithm-x-partialerence) troca e fica $O\left( \kappa^{2}\varepsilon_{\text{machine}} \right)$. Porém, se $\tan(\theta)$ é próximo de 0, ou $\eta$ é próximo de $\kappa$, então então a equação muda para $O\left( \kappa\varepsilon_{\text{machine}} \right)$ (Usa um teorema mais la pra frente, mas é engraçado ver como tudo tá muito interconectado). Porém, a matriz $A^{\ast}A$ tem número de condicionamento ${\kappa(A)}^{2}$, então o máximo que podemos esperar do problema é $O\left( \kappa^{2}\varepsilon_{\text{machine}} \right)$

**Teorema**

A solução de um problema de mínimos quadrados com uma matriz $A$ de posto-completo utilizando de equações normais é **instável**. Porém a estabilidade pode ser alcançada ao restringir para uma classe de problemas onde $\kappa(A)$ é pequeno ou $\frac{\tan(\theta)}{\eta}$ é pequeno.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Ortogonalização de Gram-Schmidt](../ortogonalizacao-de-gram-schmidt/index.md)
- Próximo: [SVD](../svd/index.md)
