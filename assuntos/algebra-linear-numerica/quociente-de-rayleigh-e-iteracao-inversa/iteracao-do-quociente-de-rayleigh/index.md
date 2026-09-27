---
layout: "default"
title: "Iteração do Quociente de Rayleigh — Quociente de Rayleigh e Iteração Inversa"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 42
---

[Álgebra Linear Numérica](../../index.md) · [Quociente de Rayleigh e Iteração Inversa](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-42"></a>

# Iteração do Quociente de Rayleigh

Beleza, a gente ja bisoiou 2 métodos, um que a gente tem uma estimativa inicial de autovetor, e vai aproximando o autovalor, depois uma que a gente tem uma aproximação de um autovalor e vamos aproximando um autovetor, combinar as duas ideias me parece uma **boa ideia**.

![Iteração do Quociente de Rayleigh](../../assets/rayleigh-iteration.png)

*Figura 11. Iteração do Quociente de Rayleigh*

A ideia é a gente ficar melhorando a estimativa de autovalores que temos pra que o algoritmo de **iteração reversa** tenha uma convergência muito mais rápida

<a id="rayleigh-quotient-iteration"></a>

1.  **function** RayleighQuotientIteration($A \in {\mathbb{C}}^{m \times m}$) {

    1.  $v^{(0)}\text{ com }\| v^{(0)}\| = 1$

    2.  $\lambda^{(0)} = \left( v^{(0)} \right)^{T}Av^{(0)}$

    3.  **for** $k = 1,2,3,\ldots$

        1.  Resolva $\left( A - \lambda^{(k - 1)}I \right)w = v^{(k - 1)}$ para $w$

        2.  $v^{(k)} = w/\| w\|$

        3.  $\lambda^{(k)} = \left( v^{(k)} \right)^{T}Av^{(k)}$

2.  }

*Figura 12. Iteração do Quociente de Rayleigh*

A convergência do algoritmo é ótima, a cada iteração o valor de precisão triplica.

**Teorema**

Quando o algoritmo de iteração do quociente de rayleigh converge para um autovalor $\lambda_{J}$ e um autovetor $q_{J}$ de $A$ de forma que: $$\begin{array}{r} \| v^{(k + 1)} - \left( \pm q_{J} \right)\| = O\left( \| v^{(k)} - \left( \pm q_{J} \right)\|^{3} \right) \\ \vert \lambda^{(k + 1)} - \lambda_{J}\vert  = O\left( \vert \lambda^{(k)} - \lambda_{J}\vert ^{3} \right) \end{array}$$

Não há necessidade de uma demonstração formal, apenas a ideia de que há uma **ótima** conversão do algoritmo

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Iteração Inversa](../iteracao-inversa/index.md)
- Próximo: [Algoritmo QR sem Shift](../../algoritmo-qr-sem-shift/index.md)
