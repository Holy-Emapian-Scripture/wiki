---
layout: "default"
title: "Método da árvore de recursão — Recorrência"
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
ordem_na_trilha: 4
---

[Projeto e Análise de Algoritmos](../../index.md) · [Recorrência](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Método da árvore de recursão

A ideia consiste em construir uma árvore definindo em cada nível os sub-problemas gerados pela iteração do nível anterior. A forma geral é encontrada ao somar o custo de todos os nós

- Cada nó representa um subproblema.

- Os filhos de cada nó representam as suas chamadas recursivas.

- O valor do nó representa o custo computacional do respectivo problema.

Esse método é útil para analisar algoritmos de divisão e conquista.

**Exemplo**

$$T(n) = \begin{cases} \theta(1)\text{ se }n = 1 \\ 2T\left( \frac{n}{2} \right) + n\text{ se }n > 1 \end{cases}$$

![Árvore de $T(n)$](../../assets/tree-example.png)

*Figura 2. Árvore de $T(n)$*

Temos então que: $$T(n) = \sum_{k = 0}^{\log(n)}2^{k}\frac{n}{2^{k}} = n\log(n) + n$$ Então temos que $T(n) = O\left( n\log(n) \right)$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Método da substituição](../metodo-da-substituicao/index.md)
- Próximo: [Método da Recorrência](../metodo-da-recorrencia/index.md)
