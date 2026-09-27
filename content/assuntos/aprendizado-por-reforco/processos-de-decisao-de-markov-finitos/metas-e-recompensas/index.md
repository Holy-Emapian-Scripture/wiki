---
layout: "default"
title: "Metas e recompensas — Processos de Decisão de Markov Finitos"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 22
---

[Aprendizado por Reforço](../../index.md) · [Processos de Decisão de Markov Finitos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-24"></a>

# Metas e recompensas

Em teoria, o objetivo do agente é maximizar o total de recompensas que recebe. Como mostrado em seções anteriores, isso não significa maximizar apenas a recompensa imediata, mas a recompensa acumulada ao longo do tempo.

O autor diz: “Tudo o que entendemos por metas e propósitos pode ser considerado como a maximização do valor esperado da soma cumulativa de um sinal escalar recebido (chamado recompensa.”

Em particular, o sinal de recompensa não deve ser usado para transmitir ao agente conhecimento prévio sobre como alcançar um objetivo. Por exemplo, um agente que joga xadrez deve ser recompensado apenas por vencer o jogo, e não por sub-objetivos intermediários como capturar peças ou controlar o centro do tabuleiro. Se esses sub-objetivos fossem recompensados separadamente, o agente poderia encontrar uma maneira de atingi-los sem alcançar o verdadeiro objetivo — por exemplo, capturar várias peças, mas ainda assim perder a partida, o que não traria o resultado esperado.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Revisão geral](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [A interface do agente-ambiente](../a-interface-do-agente-ambiente/index.md)
- Próximo: [Retornos e episódios](../retornos-e-episodios/index.md)
