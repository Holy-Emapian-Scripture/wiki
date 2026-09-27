---
layout: "default"
title: "Métodos simples de previsão (baseline) — Previsão e Baselines"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 28
---

[Séries Temporais](../../index.md) · [Previsão e Baselines](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-33"></a>

# Métodos simples de previsão (baseline)

Um baseline estabelece o padrão mínimo. Se um modelo sofisticado perde para aa média ou para o último valor (previsores que vimos anteriormente), o sofisticado ainda não justificou sua complexidade. O baseline estabelece um **limite inferior** para o desempenho de modelos mais complexos.

**Definição**

${\hat{Y}}_{T + h\vert T}$ representa a previsão do valor futuro $Y_{T + h}$ dado os dados observados até o instante $T$.

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Método da média](metodo-da-media/index.md)
2. [Método ingênuo (Passeio aleatório sem tendência)](metodo-ingenuo-passeio-aleatorio-sem-tendencia/index.md)
3. [Método ingênuo sazonal](metodo-ingenuo-sazonal/index.md)
4. [Método do desvio (drift)](metodo-do-desvio-drift/index.md)

## Percurso de estudo

[Trilha: A1](../../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Previsão via Autocorrelação $\rho(h)$ e Esperança Condicional](../previsao-via-autocorrelacao-rho-h-e-esperanca-condicional/index.md)
- Próximo: [Método da média](metodo-da-media/index.md)
