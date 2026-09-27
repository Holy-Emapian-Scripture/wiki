---
layout: "default"
title: "Monitorando um problema não estacionário — Soluções de métodos tabulares"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 14
---

[Aprendizado por Reforço](../../index.md) · [Soluções de métodos tabulares](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-14"></a>

# Monitorando um problema não estacionário

Os métodos discutidos anteriormente foram para problemas de bandidos estacionários, ou seja, problemas em que as recompensas não mudam de acordo com o tempo. No caso não estacionário, talvez seja melhor dar um peso maior às recompensas mais recentes. Uma sugestão para fazer isso é mudando o PequenoPasso(step-size) da atualização da estimativa da recompensa, ou seja:

$$Q_{n + 1} = Q_{n} + \alpha\left\lbrack R_{n} - Q_{n} \right\rbrack$$

onde $\alpha \in (0,1\rbrack$ e é constante. Note que essa equação é uma média ponderada das recompensas passadas e da estimativa inicial $Q_{1}$:

$$\begin{aligned} Q_{n + 1} & = Q_{n} + \alpha\left\lbrack R_{n} - Q_{n} \right\rbrack \\ & = \alpha R_{n} + (1 - \alpha)Q_{n} \\ & = \alpha R_{n} + (1 - \alpha)\left\lbrack \alpha R_{n - 1} + (1 - \alpha)Q_{n - 1} \right\rbrack \\ & = \alpha R_{n} + (1 - \alpha)\alpha R_{n - 1} + (1 - \alpha)^{2}Q_{n - 1} \\ & = \alpha R_{n} + (1 - \alpha)\alpha R_{n - 1} + (1 - \alpha)^{2}\alpha R_{n - 2} + \cdots \\ & \quad + (1 - \alpha)^{n - 1}\alpha R_{1} + (1 - \alpha)^{n}Q_{1} \\ & = (1 - \alpha)^{n}Q_{1} + \sum_{i = 1}^{n}\alpha(1 - \alpha)^{n - i}R_{i} \end{aligned}$$<a id="alpha"></a>

Às vezes vale a pena variar o step-size de ação para ação. Considere que $\alpha_{n}(a)$ o parâmetro step-size na $n$-ésina seleção da ação a. Um resultado conhecido na aproximação estocástica nos dá as condições requeridas para garantir convergência para o valor real da ação com probabilidade 1.

$$\sum_{n = 1}^{\infty}\alpha_{n}(a) = \infty\text{   e   }\sum_{n = 1}^{\infty}\alpha_{n}(a)^{2} < \infty$$

A primeira condição garante que os passos sejam grandes o suficiente para eventualmente superar qualquer condição inicial ou flutuações aleatórias. A segunda condição garante que eventualmente os passos sejam pequenos o suficiente para garantir convergência. Geralmente essas condições são pouco usadas na prática pois podem demorar demais.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Revisão geral](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [Implementação incremental](../implementacao-incremental/index.md)
- Próximo: [Valores Iniciais Ótimos](../valores-iniciais-otimos/index.md)
