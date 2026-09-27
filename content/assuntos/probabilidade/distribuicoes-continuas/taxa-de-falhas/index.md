---
layout: "default"
title: "Taxa de Falhas — Distribuições Contínuas"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 12
---

[Probabilidade](../../index.md) · [Distribuições Contínuas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao_taxa_falhas"></a>

# Taxa de Falhas

**Definição**

Seja $T$ o tempo de vida de um equipamento, ou seja o instante da sua primeira falha, cuja FDS é $F(t)$. A **confiabilidade** do equipamento é dada por:

$$R(t) = P(T > t) = 1 - F(t)$$

<a id="definicao_confiabilidade"></a>

**Definição**

A **taxa média de falhas** de um equipamento num intevalo $\lbrack t,t + \Delta t\rbrack$, é a probabilidade de ele falhar nos próximos $\Delta t$, dado que ainda não falhou:

$$\begin{array}{r} \text{ TMF } = \frac{P\left( T \leq t + \Delta t~\vert ~T > t \right)}{\Delta}t = \frac{P(T \leq t + \Delta t)}{\Delta t \cdot P(T > t)} = \frac{F(t + \Delta t) - F(t)}{\Delta t\left\lbrack 1 - F(t) \right\rbrack} \\ = \frac{R(t + \Delta t) - R(t)}{R(t) \cdot \Delta t} \end{array}$$

Quando $\Delta t \rightarrow 0$, obtemos a **taxa de falhas**: $$\text{ TF } = \lim\limits_{\Delta t \rightarrow 0}\frac{R(t + \Delta t) - R(t)}{R(t) \cdot \Delta t} = \frac{- R'(t)}{R(t)}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [Distribuição Normal](../distribuicao-normal/index.md)
- Próximo: [Variáveis Aleatórias Contínuas Bidimensionais](../../variaveis-aleatorias-continuas-bidimensionais/index.md)
