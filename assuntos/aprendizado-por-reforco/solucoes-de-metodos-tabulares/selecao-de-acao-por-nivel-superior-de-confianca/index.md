---
layout: "default"
title: "Seleção de Ação por Nível Superior de Confiança — Soluções de métodos tabulares"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 16
---

[Aprendizado por Reforço](../../index.md) · [Soluções de métodos tabulares](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-16"></a>

# Seleção de Ação por Nível Superior de Confiança

Como dito e reforçado por vezes, exploração é necessário e precisamos que ela aconteça, mas que tal se explorassemos não de forma arbitrária (como no $\varepsilon$-greedy), mas buscando agora selecionar as ações de acordo com a seu potencial de serem ótimas, levando em conta o quão perto a estimativa está perto de ser máxima e também a incerteza de cada estimativa. Um jeito bom de fazer isso é pela fórmula $$A_{t}\dot{=}\operatorname{argmax}\limits_{a}\left\lbrack Q_{t}(a) + c\sqrt{\frac{\ln(t)}{N_{t}(a)}} \right\rbrack,$$ onde $\ln(t)$ significa o logarítmo natural de $t$, $N_{t}(a)$ significa o número de vezes que a ação $a$ foi escolhida antes do tempo $t$, e o número $c > 0$ controla o grau de exploração. Se $N_{t}(a) = 0$, então $a$ é uma ação maximizada.

<a id="secao-17"></a>

## de onde vem isso

A ideia do UCB(Upper Confidence Bound), resumidamente, é que o termo da direita é um termo de incerteza que diminui quanto mais você seleciona a ação, e o mesmo termo aumenta quando você não escolhe a ação, fazendo o agente não se esquecer de nenhuma ação.

![Performance média do método UCB para o problema do bandido 10-armado.](../../assets/ucbmethod.png)

*Figura 6. Performance média do método UCB para o problema do bandido 10-armado.*

O UCB pode performar bem no testes do bandido 10-armado, mas o autor afirma que em problemas reais com grande espaços de estado ou com problemas não estacionários o método pode não performar bem, porque seria inviável guardar e gerenciar os valoroes de $N_{t}(a)$ e porque simplesmente não faz sentido usar o UCB como confiança da recompensa se as recompensas mudam, respectivamente.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Revisão geral](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [Valores Iniciais Ótimos](../valores-iniciais-otimos/index.md)
- Próximo: [Algoritmos do Bandido Baseado em gradiente](../algoritmos-do-bandido-baseado-em-gradiente/index.md)
