---
layout: "default"
title: "Iteração Simultânea — Algoritmo QR sem Shift"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 46
---

[Álgebra Linear Numérica](../../index.md) · [Algoritmo QR sem Shift](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-46"></a>

# Iteração Simultânea

Conforme $k \rightarrow \infty$, os vetores $v_{j}^{(k)}$ vão convergindo para múltiplos do autovetor dominante (Associado ao autovalor). Quando eu digo múltiplos, eu quero dizer muito próximos. Por mais que o span deles converja para algo útil, eles em si formam uma base muito mal condicionada.

Vamos fazer uma alteração então, vamos construir uma sequência de matrizes $Z^{(k)}$ tal que $C\left( Z^{(k)} \right) = C\left( V^{(k)} \right)$

<a id="simultanious-iteration"></a>

1.  **function** SimultaniousAlgorithm($A \in {\mathbb{C}}^{m \times m}$) {

    1.  Escolha ${\hat{Q}}^{(0)} \in {\mathbb{R}}^{m \times n}$ com colunas ortonormais

    2.  **for** $k = 1,2,3,\ldots$

        1.  $Z = A{\hat{Q}}^{(k - 1)}$

        2.  ${\hat{Q}}^{(k)},{\hat{R}}^{(k)} = \text{ qr}(Z)$ \# Fatoração Reduzida

2.  }

*Figura 15. Iteração Simultânea*

Assim é mais tranquilo de ver que $C\left( Z^{(k)} \right) = C\left( {\hat{Q}}^{(k)} \right) = C\left( A^{k}{\hat{Q}}^{(0)} \right)$. Matematicamente falando, esse novo método converge igual o método anterior (Sob as mesmas circunstâncias)

**Teorema**

O [\[simultanious-iteration\]](#simultanious-iteration) gera as mesmas matrizes ${\hat{Q}}^{(k)}$ que os passos de iteração [\[simultanious-iterations-step-1\]](../iteracoes-simultaneas-nao-normalizadas/index.md#simultanious-iterations-step-1) ~ [\[simultanious-iterations-step-2\]](../iteracoes-simultaneas-nao-normalizadas/index.md#simultanious-iterations-step-2) considerados no [\[simultanious-iteration-convergence\]](../iteracoes-simultaneas-nao-normalizadas/index.md#simultanious-iteration-convergence) e sob as mesmas condições \[simultanious-iterations-assumption-1\] e \[simultanious-iterations-assumption-2\]

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Iterações Simultâneas Não-normalizadas](../iteracoes-simultaneas-nao-normalizadas/index.md)
- Próximo: [Iteração Simultânea $\Leftrightarrow$ Algoritmo QR](../iteracao-simultanea-leftrightarrow-algoritmo-qr/index.md)
