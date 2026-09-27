---
layout: "default"
title: "Sumário — Soluções de métodos tabulares"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 19
---

[Aprendizado por Reforço](../../index.md) · [Soluções de métodos tabulares](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-21"></a>

# Sumário

Foi apresentado várias formas de balancear exploration e exploitation, com o $\varepsilon$-greedy escolhendo uma ação aleatóriamente por uma pequena fração de tempo, enquanto o método UCB escolhe deterministicamente, mas alcançam a exploração enquanto favoreciam as ações que recebiam menos amostras. O gradiente estimava não valores, mas preferências e definem as melhores ações baseando-se na preferência utilizando a soft-max. Até inicializar as estivativas de recompensa otimistamente causa um bom método de exploração inicial.

É natural se questionar qual é o melhor método. Por isso, o autor fez uma plotagem de um treinamento completo em um problema de bandido k-armado, testando a média dos vários valores dos parâmetros de cada método após mil passos. Olhe:

![Desempenho médio da recompensa de todos os algoritmos do bandido k-armado após mil passos](../../assets/comparationbanditmethods.png)

*Figura 8. Desempenho médio da recompensa de todos os algoritmos do bandido k-armado após mil passos*

No geral, neste problema, o UCB parece apresentar o melhor desempenho.

Todos esses métodos são úteis mas não abrangem a solução de um problema completo de aprendizado por reforço, mas são a base que precisamos aprender. O autor termina a seção falando sobre outra forma de abordar o balanceamento de exploitation e exploration usando um método chamado “Gittins index” que usa distribuições a priori e posteriores, além de priores conjugadas.

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Revisão geral](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [Pesquisa associativa](../pesquisa-associativa/index.md)
- Próximo: [Processos de Decisão de Markov Finitos](../../processos-de-decisao-de-markov-finitos/index.md)
