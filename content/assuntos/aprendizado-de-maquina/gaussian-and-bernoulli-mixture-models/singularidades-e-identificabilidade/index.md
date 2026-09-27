---
layout: "default"
title: "Singularidades e Identificabilidade — Gaussian and Bernoulli Mixture Models"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 15
---

[Aprendizado de Máquina](../../index.md) · [Gaussian and Bernoulli Mixture Models](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Singularidades e Identificabilidade

É válido ressaltar a existência desse problema, que é intrínsseco do algoritmo que utilizamos (variáveis latentes) no problema de mistura de gaussianas. Para simplicidade e ilustrar o problema (também se aplica à casos mais gerais), considere uma mistura de gaussianas cujos componentes de covariância são matrizes escalares, ou seja, $\Sigma_{k} = \sigma_{k}^{2}I$. Suponha também que um dos componentes da mistura (digamos, o $j$-ésimo) tem sua média $\mu_{j}$ exatamente igual a algum dos pontos do banco ($x_{n} = \mu_{j}$). Esse ponto então vai contribuir para a verossimilhança um termo: $$N\left( x_{n}~\vert ~\mu_{j},\Sigma_{j} \right) = \frac{1}{(2\pi)^{\frac{1}{2}}\sigma_{j}}$$ se considerarmos $\sigma_{j} \rightarrow 0$, então o termo vai para $\infty$ assim como a verossimilhança. Ou seja, o problema de maximização da log-verossimilhança não é bem definido, pois não existe um máximo global. Esse problema é conhecido como **singularidade** e é um problema clássico do algoritmo EM aplicado a modelos de mistura de gaussianas.

Outro problema é que, dado um ponto (não-degenerado) no espaço dos parâmetros, existem permutações dos parâmetros que geram a mesma distribuição de probabilidade. Por exemplo, considere uma mistura de duas gaussianas com parâmetros $\mu_{1},\Sigma_{1},\pi_{1}$ e $\mu_{2},\Sigma_{2},\pi_{2}$. Se permutarmos os índices das gaussianas, ou seja, trocarmos $\mu_{1}$ com $\mu_{2}$, $\Sigma_{1}$ com $\Sigma_{2}$ e $\pi_{1}$ com $\pi_{2}$, a distribuição de probabilidade gerada será a mesma. Esse problema é conhecido como **identificabilidade** e é um problema clássico do algoritmo EM aplicado a modelos de mistura de gaussianas.

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Bernoulli Mixture Models](../bernoulli-mixture-models/index.md)
- Próximo: [Variational Autoencoders](../../variational-autoencoders/index.md)
