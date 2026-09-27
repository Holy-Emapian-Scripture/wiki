---
layout: "default"
title: "A interface do agente-ambiente — Processos de Decisão de Markov Finitos"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 21
---

[Aprendizado por Reforço](../../index.md) · [Processos de Decisão de Markov Finitos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-23"></a>

# A interface do agente-ambiente

MDPs são uma formulação direta do problema de aprender de interações para alcançar um objetivo. O tomador de decisão é chamado de agente. A coisa que interage com ele, compreendendo tudo de fora do agente, é chamado de ambiente. Eles interagem continuamente, com o agente selecionando ações e o ambiente reagindo a essas ações e retornando outras situações e retornando recompensas.

![O agente e o ambiente interagindo em um Processo de Decisão de Markov.](../../assets/mdpenvironment.png)

*Figura 9. O agente e o ambiente interagindo em um Processo de Decisão de Markov.*

Mais especificamente, o agente e o ambiente interagem a cada sequência de passos discreta, $t = 1,2,\ldots$(restringindo a uma quantidade discreta para entendermos melhor). A cada passo $t$, o agente recebe alguma representação sobre o $\text{estado}$ do ambiente, $S_{t} \in \mathcal{S}$, e com base nisso seleciona uma ação, $A_{t} \in \mathcal{A}(s)$. Após a ação selecionada, o agente recebe uma recompensa numérica $R_{t + 1} \in \mathcal{R} \subset {\mathbb{R}}$ e acha para si mesmo um novo estado, $S_{t + 1}$. O agente e o ambiente numa MDP faz uma trajetória desse tipo:

$$S_{0},A_{0},R_{1},S_{1},A_{1},R_{2},S_{2},A_{2},R_{3},\ldots$$

Em um MDP finito, o conjunto de ações e recompensas têm um número finito de elementos. Nesse caso, conseguimos definir variáveis aleatórias discretas $R_{t}$ e $S_{t}$ dependendo apenas do estado e ação anterior. Ou seja, para $s' \in \mathcal{S}\text{ and  }r \in \mathcal{R}$, existe uma probabilidade desses valores ocorrerem no tempo $t$, dado valores do estado e ação:

$$p\left( s',r\vert s,a \right)\dot{=}\Pr\left\{ S_{t} = s',R_{t} = r\vert S_{t - 1} = s,A_{t - 1} = a \right\}$$

para todo $s',s \in \mathcal{S},r \in \mathcal{R}$ e $a \in \mathcal{A}(s)$. Essa probabilidade significa basicamente: depois de estar no estado $s$ e tomar a ação $a$, o ambiente responda com a recompensa $r$ e transite para o estado $s'$. Lembre-se que $p$ especifica uma distribuição de probabilidade para cada escolha de $s$ e $a$, ou seja

$$\sum_{s' \in \mathcal{S}}\sum_{r \in \mathcal{R}}p\left( s',r~\vert ~s,a \right) = 1,\text{   para todo }s \in \mathcal{S},a \in \mathcal{A}(s)$$

Em MDPs, a probabilidade caracteriza completamente a dinâmica do ambiente. Ou seja, a probabilidade de cada valor possível para $R_{t}$ e $S_{t}$ depende apenas no estado e ação imediatamente anterior $S_{t - 1}$ e $R_{t - 1}$. Note então que o estado deve incluir todas as informações relevantes sobre as interações passadas entre o agente e o ambiente que possam influenciar no futuro. Dizemos que, se isso acontece, o estado tem a propriedade de Markov, e assumiremos essa propriedade durante o resumo.

Podemos calcular outras quantidades válidas baseado nessa probabilidade geral, como a probabilidade de transição de estado(como uma função de 3 arguentos $$p:\mathcal{S}$$ x $\mathcal{S}$ x $\mathcal{A} \rightarrow \lbrack 0,1\rbrack$):

$$p\left( s'\vert s,a \right)\dot{=}\Pr\left\{ S_{t} = s'~\vert ~S_{t - 1} = s,A_{t - 1} = a \right\} = \sum_{r \in \mathcal{R}}p\left( s',r~\vert ~s,a \right)$$

Nós também podemos podemos calcular as recompensas esperadas para pares estado-ação, definido como $r:\mathcal{S}$ x $\mathcal{A} \rightarrow {\mathbb{R}}$:

$$r(s,a)\dot{=}{\mathbb{E}}\left\lbrack R_{t}~\vert ~S_{t - 1} = s,A_{t - 1} = a \right\rbrack = \sum_{r \in \mathcal{R}}r\sum_{s' \in \mathcal{S}}p\left( s',r~\vert ~s,a \right)$$

E as recompensas esperadas condicionadas também ao próximo estado, como uma função de três argumentos $r:\mathcal{S}$ x $\mathcal{A}$ x $\mathcal{S} \rightarrow {\mathbb{R}}$:

$$r(s,a,s')\dot{=}{\mathbb{E}}\left\lbrack R_{t}~\vert ~S_{t - 1} = s,A_{t - 1} = a,S_{t} = s' \right\rbrack = \sum_{r \in \mathcal{R}}r\frac{p\left( s',r~\vert ~s,a \right)}{p\left( s'\vert s,a \right)}$$

O MDP pode ser um pouco abstrato e flexível às vezes, e pode ser aplicado a muitos tipos de maneiras diferentes. Os passos de tempo($t,t + 1$, etc.) não precisam corresponder a intervalos fixos de tempo real, eles podem se referir a estágios arbitrários e sucessivos de tomada de decisão e ação.

Por exemplo, as ações podem ser de baixo nível, como controles de voltagem de um braço robótico, ou alto nível, como decidir ou não se deve almoçar. A mesma coisa acontece para os estados, que podem ser de baixo nível, como leituras de sensores, ou podem ser mais abstratos e de alto nível, como descrições simbólicas de elementos numa sala. Ou seja, cada “time step” representa apenas uma unidade lógica de decisão e consequência.

Em geral, seguimos uma regra que diz o seguinte: tudo que não pode ser alterado arbitrariamente pelo agente é considerado parte do ambiente. Não assumimos que tudo no ambiente é desconhecido pelo agente, mas sempre consideramos o cálculo das recompensas como algo externo do agente. Por fim, em alguns casos o agente pode saber tudo sobre como o ambiente funciona e ainda assim enfrentar uma tarefa de aprendizado por reforço difícil, assim como podemos conhecer exatamente as regras de um cubo mágico e ainda assim não conseguir resolvê-lo.

A fronteira entre o agente e o ambiente pode ser localizado de diferentes lugares, para diferentes propósitos. Por exemplo, um agente pode tomar decisões de alto nível que formam parte dos estados enfrentados por um agente de nível mais baixo, que implementa as decisões de alto nível.

Um quadro de MDP é uma abstração considerável do problema de aprender com o objetivo de atingir metas a partir da interação. Esse modelo propõe que, qualquer problema de aprendizado de comportamento orientado a objetivos pode ser reduzido a três sinais trocados entre um agente e seu ambiente:

- Um sinal para representar as escolhas feitas pelo agente (as ações),

- Um sinal para representar a base sobre a qual as escolhas são feitas (os estados), e

- Um sinal para definir o objetivo do agente (as recompensas).

**Exemplo**

**Biorreator**

Suponha que o aprendizado por reforço esteja sendo aplicado para determinar, momento a momento, as temperaturas e taxas de agitação de um biorreator (um grande tanque de nutrientes e bactérias usado para produzir substâncias químicas úteis).

As ações, nesse tipo de aplicação, podem ser temperaturas-alvo e taxas de agitação-alvo que são passadas para sistemas de controle de baixo nível que, por sua vez, ativam diretamente elementos de aquecimento e motores para atingir esses valores.

Os estados provavelmente consistem em leituras de sensores (como termopares), possivelmente filtradas e atrasadas, além de entradas simbólicas representando os ingredientes no tanque e o produto químico desejado.

As recompensas podem ser medidas momento a momento da taxa de produção da substância útil pelo biorreator.

Note que aqui cada estado é uma lista (ou vetor) de leituras de sensores e entradas simbólicas, e cada ação é um vetor consistindo de uma temperatura-alvo e uma taxa de agitação. É típico em tarefas de aprendizado por reforço que estados e ações tenham representações estruturadas desse tipo. As recompensas, por outro lado, são sempre números únicos (escalares).

**Exemplo**

**Robô de Pegar e Colocar (Pick-and-Place)**

Considere o uso de aprendizado por reforço para controlar o movimento do braço de um robô em uma tarefa repetitiva de pegar e colocar objetos. Se quisermos aprender movimentos rápidos e suaves, o agente de aprendizado precisará controlar diretamente os motores e ter informações de baixa latência sobre as posições e velocidades atuais das articulações mecânicas.

As ações, nesse caso, podem ser as tensões elétricas aplicadas a cada motor em cada articulação, e os estados podem ser as leituras mais recentes dos ângulos e velocidades das juntas.

A recompensa pode ser +1 para cada objeto que o robô pegar e colocar com sucesso. Para encorajar movimentos suaves, a cada passo de tempo pode ser dada uma pequena recompensa negativa, em função da “tremedeira” (ou irregularidade) do movimento no momento.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Revisão geral](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [Processos de Decisão de Markov Finitos](../index.md)
- Próximo: [Metas e recompensas](../metas-e-recompensas/index.md)
