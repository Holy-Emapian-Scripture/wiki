---
layout: "default"
title: "ACF e ACVF — Estacionariedade e ACF"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 23
---

[Séries Temporais](../../index.md) · [Estacionariedade e ACF](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-28"></a>

# ACF e ACVF

Como falamos, a covariância de uma série temporal estacionária fraca depende apenas da diferença entre os instantes, então podemos definir a função de covariância como uma função do lag $h = \vert r - s\vert$, assim:

**Definição: ACVF**

Dada a série temporal $\left\{ Y_{t} \right\}$ estacionária fraca, definimos a função de autocovariância como $$\gamma_{Y}(h) = {\mathbb{E}}\left\lbrack \left( Y_{r} - \mu_{Y} \right)\left( Y_{r + h} - \mu_{Y} \right) \right\rbrack$$

**Definição: ACF**

Dada a série temporal $\left\{ Y_{t} \right\}$ estacionária fraca, definimos a função de autocorrelação como $$\rho_{Y}(h) = \frac{\gamma_{Y}(h)}{\gamma_{Y}(0)}$$

A ACF é uma função que mede a correlação entre os valores da série temporal em diferentes lags. Ela nos ajuda a identificar padrões de dependência temporal e a determinar a ordem de modelos AR e MA, é como se ela fosse a função que mede a **memória** da série temporal. Vale ressaltar que não é porque uma série tem estacionaridade fraca que ela não possui memória, como vimos no caso do AR, que é estacionário fraco, mas possui memória curta. O mesmo não ocorre com o passeio aleatório, que não é estacionário fraco e possui memória longa

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Conceitos](../conceitos/index.md)
- Próximo: [IID v.s Ruído Branco](../iid-v-s-ruido-branco/index.md)
