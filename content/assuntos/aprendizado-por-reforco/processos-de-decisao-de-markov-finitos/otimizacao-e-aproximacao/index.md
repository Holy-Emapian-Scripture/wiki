---
layout: "default"
title: "Otimização e aproximação — Processos de Decisão de Markov Finitos"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 27
---

[Aprendizado por Reforço](../../index.md) · [Processos de Decisão de Markov Finitos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-29"></a>

# Otimização e aproximação

Um agente que aprende uma política ótima teve um excelente desempenho. Mas, na prática, isso só acontece com alto custo computacional. Mesmo que tenhamos um modelo completo e preciso das dinâmicas do ambiente, geralmente não é possível simplesmente calcular uma política ótima resolvendo a equação de otimalidade de Bellman.

Por exemplo, jogos de tabuleiro como o xadrez representam apenas uma fração minúscula da experiência humana, e mesmo assim grandes computadores especialmente projetados ainda não conseguem calcular as jogadas ótimas. Os principais aspectos que limitam são o poder computacional de tempo e memória.

Em casos tabulares(pequenos e finitos), é possível resolver e armazenas em arrays ou tabelas. Porém, em casos práticos, existem muitos mais estados do que os possíveis de armazenar. Nesses casos, as funções precisam ser aproximadas, usando alguma forma de representação funcional mais compacta e parametrizada.

A natureza online(significa com atualização constante dos dados) do aprendizado por reforço torna possível aproximar políticas ótimas de forma que se dedique mais esforço a aprender boas decisões para estados frequentemente encontrados, à custa de menos esforço para estados raramente encontrados.

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Revisão geral](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [Políticas Ótimas e Funções de Valor Ótimas](../politicas-otimas-e-funcoes-de-valor-otimas/index.md)
- Próximo: [Programação Dinâmica](../../programacao-dinamica/index.md)
