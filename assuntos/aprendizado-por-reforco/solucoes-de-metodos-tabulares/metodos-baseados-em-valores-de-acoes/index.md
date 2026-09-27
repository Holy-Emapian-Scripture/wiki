---
layout: "default"
title: "Métodos baseados em valores de ações — Soluções de métodos tabulares"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 11
---

[Aprendizado por Reforço](../../index.md) · [Soluções de métodos tabulares](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-11"></a>

# Métodos baseados em valores de ações

Qual seria uma forma natural de estimar o valor de uma ação selecionada $Q_{t}(a)$? Intuitivamente, uma boa resposta seria a média das recompensas de quando a ação $a$ foi escolhida, ou seja:

$$Q_{t}(a)\dot{=}\frac{\text{ soma das recompensas quando a é tomada antes de t}}{\text{número de vezes que a foi tomada antes de t }} = \frac{\sum_{i = 1}^{t - 1}R_{i} \cdot \mathbb{1}_{A_{i} = a}}{\sum_{i = 1}^{t - 1}\mathbb{1}_{A_{i} = a}}$$

onde $\mathbb{1}_{\text{acão}}$ denota a variável aleatória que é 1 se $\text{ação}$ é verdadeiro e 0 caso contrário. Se o denominador for zero, então definimos $Q_{t}(a)$ como quisermos, normalmente 0. Se o denominador tender à infinito, pela Lei dos Grandes Números, $Q_{t(a)}$ converge a $q_{\ast}(a)$. É claro que essa não é a única abordagem para estimar o valor de uma ação, e muito menos a melhor métrica.

A ação mais simples normalmente é apenas selecionar a ação de maior valor, e em caso de empate, sortear, ou ainda selecionar alguma arbitráriamente. Nós escrevemos essa seleção de ação ganansiosa como:

$$A_{t}\dot{=}\operatorname{argmax}\limits_{a}Q_{t(a)}$$

onde $\text{argmax}_{a}$ denota a ação $a$ para a qual a expressão acima é maximizada. Ok, mas como explicado na seção anterior, normalmente escolher apenas a melhor ação sempre não é a melhor ideia.

Uma alternativa simples para escolher é se comportar de maneira gananciosa na maior parte do tempo, mas de vez em quando, com uma pequena probabilidade $\varepsilon$, selecionarmos aleatoriamente entre todas as ações com probabilidade igual, independentemente das estimativas de valor das ações. Nós chamamos métodos que usam essa regra de seleção quase-greedy de métodos $\varepsilon$-greedy.

Uma vantagem desses métodos é que, no limite, à medida que o número de passos aumenta, toda ação será amostrada um número infinito de vezes, garantindo assim que todas as estimativas convirjam para o valor verdadeiro. Isso implica que a probabilidade de selecionar a ação ótima convirja para maior que $1 - \varepsilon$ ou seja, para quase certeza.(como?)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Revisão geral](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [O problema do bandido k-armado](../o-problema-do-bandido-k-armado/index.md)
- Próximo: [O banco de teste de 10 braços](../o-banco-de-teste-de-10-bracos/index.md)
