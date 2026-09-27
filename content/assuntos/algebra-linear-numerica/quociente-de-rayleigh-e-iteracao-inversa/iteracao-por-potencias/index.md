---
layout: "default"
title: "Iteração por Potências — Quociente de Rayleigh e Iteração Inversa"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 40
---

[Álgebra Linear Numérica](../../index.md) · [Quociente de Rayleigh e Iteração Inversa](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-40"></a>

# Iteração por Potências

Agora nós invertemo as bola. Suponha que $v^{(0)}$ é um vetor com $\| v^{(0)}\| = 1$. O processo de iteração por potência, citado antes como não muito bom, é esperado para convergir para o maior autovalor de $A$

<a id="power-iteration"></a>

1.  **function** PowerIteration($A \in {\mathbb{C}}^{m \times m}$, $v^{(0)}\text{ com }\| v^{(0)}\| = 1$) {

    1.  **for** $k = 1,2,3,\ldots$

        1.  $w = Av^{(k - 1)}$

        2.  $v^{(k)} = w/\| w\|$

        3.  $\lambda^{(k)} = \left( v^{(k)} \right)^{T}Av^{(k)}$

2.  }

*Figura 9. Iteração por potências*

<a id="power-iteration-stability"></a>

**Teorema**

Suponha que $\vert \lambda_{1}\vert  > \vert \lambda_{2}\vert  \geq \ldots \geq \vert \lambda_{m}\vert  > 0$ e $q_{1}^{T}v^{(0)} \neq 0$. Então as iterações do [\[power-iteration\]](#power-iteration) satisfazem: $$\| v^{k} - \left( \pm q_{1} \right)\| = O\left( \vert \frac{\lambda_{2}}{\lambda_{1}}\vert ^{k} \right),\vert \lambda^{(k)} - \lambda_{1}\vert  = O\left( \vert \frac{\lambda_{2}}{\lambda_{1}}\vert ^{2k} \right)$$ Conforme $k \rightarrow \infty$. O sinal $\pm$ significa que, a cada passo $k$, um dos dois sinais será escolhido para melhor estabilidade numérica

**Demonstração**

Escreva $v^{(0)} = a_{1}q_{1} + \ldots + a_{m}q_{m}$. Como $v^{(k)}$ é múltiplo de $A^{k}v^{(0)}$ temos que, para algumas contantes $c_{k}$ $$\begin{array}{r} v^{(k)} = c_{k}A^{k}v^{(0)} \\ = c_{k}\left( a_{1}\lambda_{1}^{k}q_{1} + \ldots + a_{m}\lambda_{m}^{k}q_{m} \right) \\ = c_{k}\lambda_{1}^{k}\left( a_{1}q_{1} + \ldots + a_{m}\left( \lambda_{1}/\lambda_{m} \right)^{k}q_{m} \right) \end{array}$$

A primeira equação se da ao fato de que, quando $\lim\limits_{k \rightarrow \infty}\left( \frac{\lambda_{j}}{\lambda_{1}} \right)^{k} = 0$, porém, como $\lambda_{2}$ é o maior entre $\lambda_{j}$, acaba que $\left( \frac{\lambda_{2}}{\lambda_{1}} \right)^{k}$ domina o fator de erro $v^{(k)} - \left( \pm q_{1} \right)$.

A segunda envolve uma análise complicada que não há necessidade prática de visualizarmos

O método de iteração por potências é bem ruim pois depende de alguns fatores específicos.

1.  Só pode encontrar o maior autovalor de uma matriz

2.  Se os dois maiores autovalores são próximos, a convergência demora muito

3.  Se os dois maiores autovalores possuem mesmo valor, então o algoritmo não converge

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Quociente de Rayleigh](../quociente-de-rayleigh/index.md)
- Próximo: [Iteração Inversa](../iteracao-inversa/index.md)
