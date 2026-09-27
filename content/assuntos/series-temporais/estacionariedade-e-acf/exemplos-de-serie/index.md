---
layout: "default"
title: "Exemplos de Série — Estacionariedade e ACF"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 21
---

[Séries Temporais](../../index.md) · [Estacionariedade e ACF](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-26"></a>

# Exemplos de Série

Esses serão os exemplos que vamos utilizar de forma recorrente

**Exemplo: Ruído Branco**

$$Y_{t} = \varepsilon_{t}$$ Não existe memória, cada instante contém um ruído que não conseguimos traçar a partir dos anteriores

![](../../assets/A1/whitenoise.png)

**Exemplo: AR**

$$Y_{t} = \varphi Y_{t - 1} + \varepsilon_{t},\text{\quad\quad}\vert \varphi\vert  < 1$$ Depende diretamente do valor anterior, mas não de valores mais antigos. A memória é curta, mas existe

![](../../assets/A1/AR.png)

**Exemplo: Passeio Aleatório**

$$Y_{t} = Y_{t - 1} + \varepsilon_{t}$$ Acumula os ruídos passados, de forma que a memória é longa e o valor atual depende de todos os valores anteriores

![](../../assets/A1/randomwalk.png)

**Exemplo: Tendência Linear**

$$Y_{t} = \beta_{0} + \beta_{1}t + \varepsilon_{t}$$ A tendência linear é um caso especial de passeio aleatório, onde o valor atual depende do tempo e de todos os valores anteriores

![](../../assets/A1/lineartrend.png)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Introdução](../introducao/index.md)
- Próximo: [Conceitos](../conceitos/index.md)
