---
layout: "default"
title: "Poder do Teste — Comparando as médias de duas Distribuições Normais"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 36
---

[Inferência Estatística](../../index.md) · [Comparando as médias de duas Distribuições Normais](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-36"></a>

# Poder do Teste

Para cada parâmetro do vetor $\theta = \left( \mu_{X},\mu_{Y},\sigma^{2} \right)$, a função de poder do teste $t$ biamostral pode ser computada usando a distribuição $t$ não-central

**Teorema: Poder do teste $t$ biamostral**

Seja a estatística $U$ ser definida como na equação [\[two-sample-u-statistic\]](../o-t-teste-biamostral/index.md#two-sample-u-statistic), então $U$ tem distribuição não-central $t$ com $m + n - 2$ graus de liberdade e parâmetro de não-centralidade $$\psi = \frac{\mu_{X} - \mu_{Y}}{\sigma\left( \frac{1}{m} + \frac{1}{n} \right)^{1/2}}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [O $t$-teste biamostral](../o-t-teste-biamostral/index.md)
- Próximo: [Alternativas Bilaterais](../alternativas-bilaterais/index.md)
