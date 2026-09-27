---
layout: "default"
title: "Notação Unificada para Tarefas Contínuas e episódicas — Processos de Decisão de Markov Finitos"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 24
---

[Aprendizado por Reforço](../../index.md) · [Processos de Decisão de Markov Finitos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-26"></a>

# Notação Unificada para Tarefas Contínuas e episódicas

Para conseguirmos nos referir não só a Tarefas Contínuas mas também Episódicas sem perda de generalidade e na mesma notação, precisamos nos referir não apenas a $S_{t}$, a representação no tempo $t$, mas sim a $S_{t,i}$, a representação do estado $t$ no episódio $i$(Análogo para $A_{t,i}$, $R_{t,i}$, etc.).

Agora, precisamos apenas de mais uma convenção de notação única que cubra tanto as tarefas episódicas quanto as contínuas. Os dois casos podem ser unificados se considerarmos que a terminação de um episódio corresponde à entrada de um estado especial absorvente, que faz transição apenas para si mesmo e gera recompensas iguais a zero.

![Exemplo de unificação dos casos](../../assets/unifinotation.png)

*Figura 11. Exemplo de unificação dos casos*

No exemplo acima, vemos que o quadrado é exatamente o estado que descrevemos, e que ao somar as recompensas, obtemos o mesmo retorno se somarmos até $T = 3$ ou se somarmos a sequência infinita completa.

Assim, podemos definir o retorno em geral da forma:

$$G_{t}\dot{=}\sum_{k = t + 1}^{T}\gamma^{k - t - 1}R_{k}$$

Incluindo a probabilidade de $T = \infty$ ou $\gamma = 1$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Revisão geral](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [Retornos e episódios](../retornos-e-episodios/index.md)
- Próximo: [Políticas e Funções de valor](../politicas-e-funcoes-de-valor/index.md)
