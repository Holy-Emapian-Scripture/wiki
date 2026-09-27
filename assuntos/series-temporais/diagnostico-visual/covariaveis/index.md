---
layout: "default"
title: "Covariáveis — Diagnóstico Visual"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 14
---

[Séries Temporais](../../index.md) · [Diagnóstico Visual](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-19"></a>

# Covariáveis

Dentro dessa estrutura, podem existir também **covariáveis explicativas** que influenciam a série temporal. Por exemplo, em uma série de vendas de um produto, fatores como campanhas de marketing, feriados ou eventos especiais podem afetar os valores observados. Incorporar essas covariáveis nos modelos pode melhorar a precisão das previsões e fornecer insights sobre os fatores que impactam a série. Ainda dentro do nosso framework visual, podemos introduzir essas covariáveis como $$y_{t} = \underset{\text{ Estrutura Temporal}}{\underbrace{T_{t} + S_{t}}} + \underset{\text{ Covariáveis}}{\underbrace{x_{t}^{T}\beta}} + R_{t}$$

Na prática, $T_{t}$ e $S_{t}$ são incorporados dentro de $x_{t}$ e não são derivados explicitamente, mas é importante entender que eles existem e como eles caracterizam a série temporal. A análise visual pode nos ajudar a identificar quais covariáveis podem ser relevantes para o modelo e como elas se relacionam com os padrões observados na série.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Introdução](../introducao/index.md)
- Próximo: [Tendência](../tendencia/index.md)
