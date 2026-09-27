---
layout: "default"
title: "Estimadores não-viezados"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 16
---

[Inferência Estatística](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-16"></a>

# Estimadores não-viezados

------------------------------------------------------------------------

Nosso principal objetivo quando estamos fazendo inferência é fazer um estimador $\delta(\underline{X})$ de $g(\theta)$ que a distribuição se concentra bem próximo de $\theta$, ou seja, na maior parte do tempo, os valores retornados pelo estimador são próximos do verdadeiro valor de $g(\theta)$. É com esse objetivo que criamos estimadores **não-viezados**

**Definição: Estimador não-viezado**

Um estimador $\delta(\underline{X})$ é não-viezado para $g(\theta)$ se ${\mathbb{E}}_{\theta}\left\lbrack \delta(\underline{X}) \right\rbrack = g(\theta)\ \forall\theta$

**Definição: Viés**

O viés de um estimador $\delta(\underline{X})$ tem o seu **viés** definido como $$\text{ Bias}\left( g(\theta) \right) = {\mathbb{E}}_{\theta}\left\lbrack \delta(\underline{X}) \right\rbrack - g(\theta)$$

Porém, um estimador **não-viezado** não significa que ele é um **bom** estimador ou sequer um estimador viável para a situação. Por exemplo, um estimador que subestima $g(\theta)$ em $1000$ unidades ou superestima vai ser não-viezado, mas sempre retornará valores ruins de aproximação frequentemente. Então para um estimador ser **bom**, ele necessita ter uma baixa variância

**Teorema**

Seja $\delta$ um estimador de variância finita, então ${\mathbb{E}}_{\theta}\left\lbrack \left( \delta - g(\theta) \right)^{2} \right\rbrack = {\mathbb{V}}_{\theta}\lbrack\delta\rbrack + \left( \text{Bias}\left( \delta,g(\theta) \right) \right)^{2}$

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Estimador não-viezado da Variância](estimador-nao-viezado-da-variancia/index.md)
2. [Limitações](limitacoes/index.md)

## Percurso de estudo

[Trilha: A2](../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Distribuições Impróprias](../analise-bayesiana-de-amostras-normais/distribuicoes-improprias/index.md)
- Próximo: [Estimador não-viezado da Variância](estimador-nao-viezado-da-variancia/index.md)
