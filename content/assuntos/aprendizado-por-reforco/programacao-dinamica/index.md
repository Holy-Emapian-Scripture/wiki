---
layout: "default"
title: "Programação Dinâmica"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 28
---

[Aprendizado por Reforço](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-30"></a>

# Programação Dinâmica

------------------------------------------------------------------------

Podemos utilizar de algoritmos de programação dinâmica para resolver MDPs, mas eles exigem um modelo completo do ambiente, ou seja, a função de transição $p\left( s',r\vert s,a \right)$ deve ser conhecida. Além do fato que $\mathcal{S},\mathcal{R}$ e $\mathcal{A}$ devem ser finitos, o que não é o caso em muitos problemas práticos, mas vale a pena conhecer os algoritmos de programação dinâmica, pois eles formam a base para muitos outros algoritmos de aprendizado por reforço.

A base deses algorimtos é pegar as equações de Bellman e usá-las como atualizações iterativas para aproximar as funções de valor. Por exemplo, a equação de Bellman para $v_{\pi}$ pode ser reescrita como:

$$
v_{\pi}(s) = \sum_{a}\pi(a\vert s)\sum_{r,s'}p\left( s',r\vert s,a \right)\left\lbrack r + \gamma v_{\pi}(s') \right\rbrack
$$
<!-- wiki:original:fim -->

## Conteúdos relacionados

- [Programação Dinâmica — Projeto e Análise de Algoritmos](../../projeto-e-analise-de-algoritmos/tecnicas-de-projeto-a2/index.md#programacao-dinamica)

## Percurso de estudo

[Trilha: Revisão geral](../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [Otimização e aproximação](../processos-de-decisao-de-markov-finitos/index.md#otimizacao-e-aproximacao)
