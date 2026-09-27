---
layout: "default"
title: "Algoritmos do Bandido Baseado em gradiente — Soluções de métodos tabulares"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 17
---

[Aprendizado por Reforço](../../index.md) · [Soluções de métodos tabulares](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-18"></a>

# Algoritmos do Bandido Baseado em gradiente

Nessa seção, vamos considerar aprender uma preferência numérica para cada ação $a$, denotada $H_{t}(a)$. Quanto maior a preferência, mais a ação será tomada, mas a preferência não tem interpretação em termos de recompensa. Perceba que apenas a preferência relativa de uma ação sobre a outra é importante, e ela é definida de acordo com uma $\text{distribuição soft-max}$ como se segue: $$\Pr\left\{ A_{t} = a \right\}\dot{=}\frac{e^{H_{t}(a)}}{\sum_{b = 1}^{k}e^{H_{t}(b)}}\dot{=}\pi_{t}(a)$$

onde $$\pi_{t}(a)$$ é definido como a probabilidade de tomar a ação $a$ no tempo $t$. Inicialmente todas as preferências são as mesmas (ou seja, $H_{1}(a) = 0$, para todo $a$). Logo todas as ações tem mesma probabilidade. Existe uma fórmula natural de aprender melhor as preferências, baseando-se na ideia do gradiente estocástico ascendente:

$$\begin{aligned} H_{t + 1}\left( A_{t} \right) & \dot{=}H_{t}\left( A_{t} \right) + \alpha\left( R_{t} - {\overset{-}{R}}_{t} \right)\left( 1 - \pi_{t}\left( A_{t} \right) \right),\text{     and} \\ H_{t + 1}(a) & \dot{=}H_{t}(a) - \alpha\left( R_{t} - {\overset{-}{R}}_{t} \right)\pi_{t}(a)\text{               for all a } \neq A_{t} \end{aligned}$$

onde $\alpha > 0$ é um $\text{step-size}$, e $\overline{R_{t}}$ é a média de todas as recompensas incluindo o tempo $t$. O $\overline{R_{t}}$ funciona como referência, ou seja, se a recompensa é maior do que a média de recompensas, então a preferência para ela aumenta, e vice-versa. As ações não selecionadas se movem na direção oposta.

A Figura 7 mostra o resultados do algoritmo do gradiente ascendente em uma variante do bandido 10-armado onde as recompensas são escolhidas de uma distribução ${\mathbb{N}}(4,1)$. Essa mudança não faz com que o algoritmo que usa a referência (${\overset{-}{R}}_{t}$) sofra algum efeito, mas se a referência for omitida, ou seja, se $$\begin{aligned} H_{t + 1}\left( A_{t} \right) & \dot{=}H_{t}\left( A_{t} \right) + \alpha R_{t}\left( 1 - \pi_{t}\left( A_{t} \right) \right) \end{aligned}$$, a performance será significativamente pior, como mostra a figura.

![Desempenho médio do algoritmo do bandido 10-armado de gradiente com e sem referência quando $q_{\ast}$(a) está perto de 4 e não perto de 0.](../../assets/baseline.png)

*Figura 7. Desempenho médio do algoritmo do bandido 10-armado de gradiente com e sem referência quando $q_{\ast}$(a) está perto de 4 e não perto de 0.*

<a id="secao-19"></a>

## olhar no livro a explicação e explicar dps

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Revisão geral](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [Seleção de Ação por Nível Superior de Confiança](../selecao-de-acao-por-nivel-superior-de-confianca/index.md)
- Próximo: [Pesquisa associativa](../pesquisa-associativa/index.md)
