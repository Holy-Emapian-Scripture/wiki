---
layout: "default"
title: "Distribuição Chi-Quadrado"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 2
---

[Inferência Estatística](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-2"></a>

# Distribuição Chi-Quadrado

------------------------------------------------------------------------

Essa distribuição é muito utilizada dentro da estatística serve como base para uma outra distribuição que veremos posteriormente. Ela vai ser útil no próximo capítulo também pois ela é a distribuição do estimador de máxima verossimilhança da variância de uma Normal com média $\mu$ conhecida $$\hat{\sigma^{2}} = \frac{1}{n}\sum_{i = 1}^{n}\left( X_{i} - \mu \right)^{2}$$

**Definição**

$\forall m \in {\mathbb{R}}$, uma distribuição Gamma$\left( \frac{m}{2},\frac{1}{2} \right)$ é também chamada de $Χ_{m}^{2}$ (Chi quadrado com $m$ graus de liberadade). Ou seja, se $X \sim Χ_{m}^{2}$: $$f_{X}(x) = \frac{\left( \frac{1}{2} \right)^{\frac{m}{2}}}{\Gamma(\frac{m}{2})}x^{\frac{m}{2} - 1}e^{- \frac{1}{2}x}$$

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Propriedades](propriedades/index.md)

## Percurso de estudo

[Trilha: A2](../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Distribuição Amostral de Estimadores](../distribuicao-amostral-de-estimadores/index.md)
- Próximo: [Propriedades](propriedades/index.md)
