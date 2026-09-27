---
layout: "default"
title: "Políticas Ótimas e Funções de Valor Ótimas — Processos de Decisão de Markov Finitos"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 26
---

[Aprendizado por Reforço](../../index.md) · [Processos de Decisão de Markov Finitos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-28"></a>

# Políticas Ótimas e Funções de Valor Ótimas

Uma política $\pi$ é ótima se ela for melhor ou igual a qualquer outra política $\pi'$. Enunciando melhor, $\pi \geq \pi' \Leftrightarrow v_{\pi}(s) \geq v_{\pi}'(s)$ para todo $s \in \mathcal{S}$. Sabendo que podem existir mais do que uma, as políticas ótimas são denotadas como $\pi_{\ast}$. Elas compartilham a melhor função de estado-valor, chamada de função de estado-valor ótima e denotada como:

$$v_{\ast}(s)\dot{=}\max\limits_{\pi}v_{\pi}(s),\text{  para todo }s \in \mathcal{S}$$

Ainda, políticas ótimas compartilham as mesmas funções de ação-valor ótimos, definidas como:

$$q_{\ast}(s,a)\dot{=}\max\limits_{\pi}q_{\pi}(s,a),\text{  para todo }s \in \mathcal{S}\text{  e  }a \in \mathcal{A}$$

**Exemplo**

Continuação do exemplo de golfe

A imagem de baixo mostra uma possível função de valor-ótima, $q_{\ast}$. Como dito, o driver nos permite bater na bola mais longe, mas com menos precisão. Podemos alcançar o buraco em uma única tacada usando o driver apenas se estivermos bem perto, por isso, o contorno de valor $- 1$ de $q_{\ast}\left( s,\text{ driver} \right)$ cobre apenas uma pequena região ao redor da área verde.

Se tivermos duas tacadas, entretanto, podemos chegar ao buraco a partir de locais mais distantes, conforme mostrado pelo contorno de $- 2$. Nesse caso, não precisamos atingir diretamente o buraco com o driver, basta chegar até a área verde, onde então podemos usar o putter.

Da posição inicial (tee), o melhor conjunto de ações é duas tacadas com o driver e uma com o putter, totalizando três tacadas até o buraco.

Note que o valor de um estado sob a política ótima, deve ser igual ao retorno esperado de tomar a melhor ação possível a partir desse estado. Formalmente:

$$\begin{aligned} v_{\ast}(s) & = \max\limits_{a \in \mathcal{A}(s)}{q_{\pi}}_{\ast}(s,a) \\ & = \max\limits_{a}{{\mathbb{E}}_{\pi}}_{\ast}\left\lbrack G_{t}~\vert ~S_{t} = s,A_{t} = a \right\rbrack \\ & = \max\limits_{a}{{\mathbb{E}}_{\pi}}_{\ast}\left\lbrack R_{t + 1} + \gamma G_{t + 1}~\vert ~S_{t} = s,A_{t} = a \right\rbrack \\ & = \max\limits_{a}{{\mathbb{E}}_{\pi}}_{\ast}\left\lbrack R_{t + 1} + \gamma v_{\ast}\left( S_{t + 1} \right)~\vert ~S_{t} = s,A_{t} = a \right\rbrack \\ & = \max\limits_{a}\sum_{s',r}p\left( s',r~\vert ~s,a \right)\left\lbrack r + \gamma v_{\ast}(s') \right\rbrack \end{aligned}$$

Essa é a chamada equação de Bellman de otimalidade. O mesmo raciocínio segue para a equação de Bellman de otimalidade para $q_{\ast}$:

$$\begin{aligned} q_{\ast}(s,a) & = {\mathbb{E}}\left\lbrack R_{t + 1} + \gamma\max\limits_{a}'q_{\ast}\left( S_{t + 1},a' \right)~\vert ~S_{t} = s,A_{t} = a \right\rbrack \\ & = \sum_{s',r}p\left( s',r~\vert ~s,a \right)\left\lbrack r + \max\limits_{a}'q_{\ast}(s',a') \right\rbrack \end{aligned}$$

Os diagramas de backup são os mesmos usados anteriormente, exceto que os arcos nos pontos de escolha do agente tem um max.

![Diagramas anteriores, representando a equação de Bellman de otimalidade para $v_{\pi}$ e $q_{\pi}$, respectivamente.](../../assets/maxthebellman.png)

*Figura 15. Diagramas anteriores, representando a equação de Bellman de otimalidade para $v_{\pi}$ e $q_{\pi}$, respectivamente.*

Para MDPs finitos, a equação de otimalidade de Bellman tem uma única solução. Além disso, uma vez que se tenha $v_{\ast}$, é relativamente fácil determinar uma política ótima.

Para cada estado $s$, haverá uma ou mais ações nas quais o máximo é atingido na equação de otimalidade de Bellman. Qualquer política que atribua probabilidade diferente de zero a essas ações é uma política ótima.

Podemos pensar nisso como uma busca de um passo. Se temos a função de valor ótima $v_{\ast}$, então as ações que parecem melhores após uma busca de um passo já são ações ótimas.

Ter $q_{\ast}$ também torna a escolha das ações ótimas ainda mais fácil, pois, para qualquer estado $s$, o agente pode simplesmente encontrar a ação $a$ que maximiza $q_{\ast}(s,a)$. A função de valor-ação $q_{\ast}$ efetivamente armazena (faz cache) os resultados de todas as buscas de um passo à frente.

**Exemplo**

Continuação do exemplo de GridWorld

Suponha que resolvemos a equação de Bellman para $v_{\ast}$ para o grid simples introduzido no exemplo anterior. A figura do meio mostra a função ótima do valor, enquanto a função da direita mostra as políticas ótimas correspondentes.

![Solução ótima para o problema GridWorld](../../assets/maxgridworld.png)

*Figura 16. Solução ótima para o problema GridWorld*

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Revisão geral](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [Políticas e Funções de valor](../politicas-e-funcoes-de-valor/index.md)
- Próximo: [Otimização e aproximação](../otimizacao-e-aproximacao/index.md)
