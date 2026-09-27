---
layout: "default"
title: "Intervalo de confiança para outros parâmetros — Intervalos de Confiança"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 11
---

[Inferência Estatística](../../index.md) · [Intervalos de Confiança](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-11"></a>

# Intervalo de confiança para outros parâmetros

Até agora, só vimos a aplicação de intervalos de confiança para a distribuição normal, mas por quê? Pois a normal possui propriedades que tornam encontrar os intervalos de confiança mais fáceis, como por exemplo, encontrarmos estatísticas (Por exemplo $T = \sqrt{n}({\overline{X}}_{n} - \mu)/\sigma'$) que não dependem do parâmetro que queremos estimar, e isso na verdade é uma definição útil que pode nos ajudar:

**Definição: Pivô**

Seja $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ uma amostra de uma distribuição parametrizada por $\theta$ e $V\left( \theta,\underline{X} \right)$ uma variável aleatória tal que sua distribuição **não depende de $\theta$** e é a mesma $\forall\theta$, então chamamos $V\left( \theta,\underline{X} \right)$ de **quantidade pivotal** ou **pivô**

Podemos então utilizar dessa definição para construir intervalos de confiança. Porém, para isso, precisamos de uma “função inversa” desse $V$, algo do tipo: $$r\left( V\left( \theta,\underline{X} \right),\underline{X} \right) = g(\theta)$$<a id="v-pseudo-inverse"></a>

**Teorema**

Seja $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ uma amostra de uma distribuição parametrizada por $\theta$. Suponha que existe um pivô $V$. Seja $F_{V}(v)$ a CDF de $V$ e contínua. Assuma também que a função $r$ tal qual a equação [\[v-pseudo-inverse\]](#v-pseudo-inverse) existe e é estritamente crescente em $v$ para cada $\underline{x}$. Seja $\gamma \in (0,1)$ e $\gamma_{2} > \gamma_{1}$ tal que $\gamma_{2} - \gamma_{1} = \gamma$, então as seguintes estatísticas são endpoints de um invervalo de confiança $\gamma$-exato para $g(\theta)$ $$\begin{array}{r} A = r\left( F_{V}^{- 1}\left( \gamma_{1} \right),\underline{x} \right) \\ B = r\left( F_{V}^{- 1}\left( \gamma_{2} \right),\underline{x} \right) \end{array}$$ Se $r$ é estritamente decrescente, então invertemos $A$ e $B$

**Demonstração**

Se $r\left( \theta,\underline{x} \right)$ é estritamente crescente em $v$ para todo $\underline{x}$, então: $$V\left( \theta,\underline{X} \right) < c \Leftrightarrow g(\theta) < r\left( c,\underline{X} \right)$$ Defina $c = F_{V}^{- 1}\left( \gamma_{i} \right)$ para $i = 1,2$, então obtemos: $$\begin{array}{r} {\mathbb{P}}(g(\theta) < A) = \gamma_{1} \\ {\mathbb{P}}(g(\theta) < B) = \gamma_{2} \end{array}$$<a id="intervals-pivots"></a> Como $V$ tem distribuição contínua e $r$ é estritamente crescente, então: $${\mathbb{P}}(A = g(\theta)) = {\mathbb{P}}(V\left( \theta,\underline{X} \right) = F_{V}^{- 1}\left( \gamma_{1} \right)) = 0$$ Similarmente com ${\mathbb{P}}(B = g(\theta))$, então combinamos as duas equações na equação [\[intervals-pivots\]](#intervals-pivots) para obter ${\mathbb{P}}(A < g(\theta) < B) = \gamma$

**Exemplo**

Seja $X_{1},\ldots,X_{n}$ uma amostra aleatória de uma distribuição normal com média $\mu$ e variância $\sigma^{2}$ desconhecidos. Vimos anteriormente que: $$V\left( \theta,\underline{X} \right) = \frac{1}{\sigma^{2}}\sum_{i = 1}^{n}\left( X_{i} - {\overline{X}}_{n} \right)^{2} \sim Χ_{n - 1}^{2}\text{\quad\quad}\forall\theta = \left( \mu,\sigma^{2} \right)$$ Logo, $V$ é um pivô, de forma que conseguimos utilizá-lo para achar intervalos de confiança para $\sigma^{2}$

Porém é bem comum que o pivô não exista em casos discretos

**Exemplo**

Seja $\theta$ a proporção de sucessos em uma população muito grande de pacientes tratados com imipramina. Suponha que os clínicos desejem uma variável aleatória $A$ tal que, para todo $\theta$, tenhamos $$\Pr(A < \theta) \geq 0.9$$

Isto é, eles querem ter **$90\%$ de confiança** de que a proporção de sucesso seja **pelo menos $A$**. Os dados observáveis consistem no número $X$ de sucessos em uma amostra aleatória de **$n = 40$** pacientes. Nenhuma variável pivotal existe neste exemplo, e os intervalos de confiança são mais difíceis de construir

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Intervalos de Confiança Unilaterais](../intervalos-de-confianca-unilaterais/index.md)
- Próximo: [Análise Bayesiana de Amostras Normais](../../analise-bayesiana-de-amostras-normais/index.md)
