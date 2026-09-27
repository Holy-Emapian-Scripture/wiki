---
layout: "default"
title: "Balanço Viés-Variância — Modelagem Clássica aplicada ao Tempo"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 6
---

[Séries Temporais](../index.md) · [Modelagem Clássica aplicada ao Tempo](index.md)

<!-- wiki:original:inicio -->
<a id="secao-10"></a>

# Balanço Viés-Variância

Vale relembrar que dentro do ramo da estatística (inclusive das séries temporais), sempre existirá o balanço **viés e variância**. O erro mais comum de se minimizar em contextos estatísticos é o erro quadrático médio $${\mathbb{E}}\left\lbrack \left( y_{t} - {\hat{y}}_{t} \right)^{2} \right\rbrack = {\text{ Bias}\left( {\hat{y}}_{t} \right)}^{2} + {\mathbb{V}}\left\lbrack {\hat{y}}_{t} \right\rbrack^{2} + \sigma^{2}$$

Obter modelos mais precisos na previsão de $y_{t}$ (com menos viés) acaba resultando em modelos com variação alta (mudanças pequenas nos dados podem impactar muito os resultado) e vice-versa

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Modelo linear padrão](modelo-linear-padrao.md)
- Próximo: [Regularização Lasso e Ridge](regularizacao-lasso-e-ridge.md)
