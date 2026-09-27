---
layout: "default"
title: "Implementação incremental — Soluções de métodos tabulares"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 13
---

[Aprendizado por Reforço](../../index.md) · [Soluções de métodos tabulares](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-13"></a>

# Implementação incremental

Como computar de maneira eficiente todos esse valores de ações com menos cálculo e memória constante?

Vamos nos concentrar em somente uma ação. Considere que $R_{i}$ denota a recompensa recebida após a $i$ésima seleção dessa ação, e chame de $Q_{n}$ a estimativa do valor da ação depois de ela ser selecionada $n - 1$ vezes. Logo $$Q_{n}\frac{\dot{=}(R_{1} + R_{2} + \ldots R_{n - 1})}{n - 1}.$$<a id="mediaamostral"></a>

Parando para pensar, isso não resolveria o problema, já que mesmo assim, ao escolher a ação, teríamos que somar tudo novamente, guardar o valor novamente, etc… Mas, não precisamos disso, já que

$$\begin{aligned} Q_{n + 1} & = \frac{1}{n}\sum_{i = 1}^{n}R_{i} \\ & = \frac{1}{n}\left( R_{n} + \sum_{i = 1}^{n - 1}R_{i} \right) \\ & = \frac{1}{n}\left( R_{n} + (n - 1) \cdot \frac{1}{n - 1}\sum_{i = 1}^{n - 1}R_{i} \right) \\ & = \frac{1}{n}\left( R_{n} + (n - 1)Q_{n} \right) \\ & = \frac{1}{n}\left( R_{n} + nQ_{n} - Q_{n} \right) \\ & = Q_{n} + \frac{1}{n}\left\lbrack R_{n} - Q_{n} \right\rbrack \end{aligned}$$<a id="umsobreeni"></a>

Legal! Conseguimos chegar em uma equação pequena que depende apenas das estimativa da ação passada e da recompensa passada.

Generalizando ainda mais, nós chegamos em uma fórmula interessante:

$\text{NovaEstimativa } \leftarrow \text{ EstimativaAntiga } + \text{ PequenoPasso }\left\lbrack \text{ Alvo } - \text{ EstimativaAntiga } \right\rbrack.$

Que se parece bastante com a fórmula que vimos no Tic-Tac-Toe, mas agora entendemos de onde vêm.

- Colocar aqui o pseudocódigo talvez?

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Revisão geral](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [O banco de teste de 10 braços](../o-banco-de-teste-de-10-bracos/index.md)
- Próximo: [Monitorando um problema não estacionário](../monitorando-um-problema-nao-estacionario/index.md)
