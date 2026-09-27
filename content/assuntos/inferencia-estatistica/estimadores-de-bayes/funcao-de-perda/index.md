---
layout: "default"
title: "Função de Perda — Estimadores de Bayes"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 10
---

[Inferência Estatística](../../index.md) · [Estimadores de Bayes](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-10"></a>

# Função de Perda

Muito comumente, criamos um estimador $\delta$ com o objetivo de aproximar um parâmetro $\theta$, ou seja, um bom estimador é aquele que $\delta(\underline{x}) - \theta \approx 0$

**Definição: Função de perca**

A função de perca é uma função real de duas variáveis $L(\theta,a)$, onde $\theta \in \Omega$ e $a \in {\mathbb{R}}$. A interpretação é que $L(\theta,a)$ decai conforme $a \rightarrow \theta$

Queremos estimar $\theta$ apenas com nossos valores observados, porém, vamos supor que não vimos nenhum ainda, então se escolhermos $a$ como uma estimativa, vamos ter: $${\mathbb{E}}\left\lbrack L(\theta,a) \right\rbrack = \int_{\Omega}L(\theta,a)\xi(\theta)d\theta\text{\quad\quad}\text{ (LOTUS) }$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Estimador e Estimativa](../estimador-e-estimativa/index.md)
- Próximo: [Estimador de Bayes](../estimador-de-bayes/index.md)
