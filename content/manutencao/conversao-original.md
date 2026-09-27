---
layout: "default"
title: "Registro da conversão original"
nav_exclude: true
search_exclude: true
---

> Registro histórico da importação. Os comandos e caminhos descritos abaixo pertencem ao projeto de origem. Os links do catálogo foram atualizados para as trilhas da wiki.

# Acervo em Markdown

Conversão dos **35 arquivos Typst** do projeto, organizada com os mesmos nomes de pastas e documentos. Os originais continuam nas pastas anteriores; aqui a extensão passa de `.typ` para `.md`.

Foram convertidos 910 títulos, 10595 expressões matemáticas, 222 blocos de código, 13 tabelas e 295 ocorrências de imagens (292 arquivos de imagem distintos).

## Como ler

Use um leitor Markdown compatível com matemática LaTeX e HTML, como o GitHub ou o Obsidian. As fórmulas usam `$…$` no texto e `$$…$$` em blocos. Cada documento que tinha sumário recebeu links para suas seções. As imagens e bibliografias foram copiadas com caminhos relativos, de modo que esta pasta pode ser movida inteira.

## Adaptação dos elementos

- Títulos, listas, ênfases, links e código viraram seus equivalentes em Markdown. A indentação interna dos códigos foi preservada, removendo apenas o recuo comum do contêiner Typst.
- Fórmulas, matrizes, casos, símbolos e funções matemáticas foram traduzidos para LaTeX.
- Teoremas, definições, propriedades, corolários, exemplos e demonstrações mantêm seus títulos e conteúdo em blocos de texto. Referências internas usam âncoras explícitas em vez da numeração automática dos pacotes Typst.
- Figuras mantêm imagem e legenda. As tabelas usam Markdown; o cabeçalho que ocupava quatro colunas virou um título imediatamente acima da tabela, preservando seu conteúdo e sua associação às colunas.
- Pseudocódigos mantêm títulos, listas aninhadas, passos e expressões. Colunas e grades de apresentação viraram conteúdo sequencial, na ordem original, inclusive os cabeçalhos de código e saída.
- Citações têm links para a bibliografia formatada; os arquivos `.bib` também estão incluídos.
- Quebras de página viraram separadores. Fontes, cores, dimensões de página, caixas decorativas e paginação não têm equivalente portátil em Markdown e foram substituídas por estrutura textual. Datas calculadas por `datetime.today()` correspondem ao dia em que a conversão foi executada.

## Verificação e reprodução

O [relatório de conversão](conversao-original.json) registra contagens, recursos e verificações de cada documento. A conversão verifica a releitura das fórmulas e códigos no Markdown, a tradução das fórmulas para MathML, os destinos internos e os hashes das imagens copiadas.

Três expressões matemáticas vazias do original foram representadas por comentários HTML, sem conteúdo visível a omitir.

Uma duplicação de rótulo já presente no original de Otimização para CD / A2 foi desambiguada: a segunda ocorrência de `gradient-descent` recebe `gradient-descent-2`; referências ao nome original apontam à primeira ocorrência.

O conversor está em `../scripts/convert_typst.py` e usa Python 3 e Pandoc 3.8.3 (versão utilizada nesta conversão). Na raiz do projeto, execute:

```sh
python3 scripts/convert_typst.py --pandoc /caminho/para/pandoc
```

O script atualiza os arquivos gerados em `Markdown/`. Ele não altera os documentos Typst. A licença do projeto está em [LICENSE](../LICENSE).

## Documentos


### 3 semestre

- [Cálculo Vetorial / Recaps / A1_recap](../trilhas/calculo-vetorial/a1.md)
- [Cálculo Vetorial / Recaps / A2_recap](../trilhas/calculo-vetorial/a2.md)
- [EDO / RecapA2](../trilhas/equacoes-diferenciais-ordinarias/a2.md)
- [Estrutura de Dados / Exercices / lecture_10 / exercises](../trilhas/estrutura-de-dados/exercicios-aula-10.md)
- [Estrutura de Dados / Exercices / lecture_12 / exercises](../trilhas/estrutura-de-dados/exercicios-aula-12.md)
- [Estrutura de Dados / Exercices / lecture_7 / exercises](../trilhas/estrutura-de-dados/exercicios-aula-7.md)
- [Estrutura de Dados / Exercices / lecture_8 / exercises](../trilhas/estrutura-de-dados/exercicios-aula-8.md)
- [Estrutura de Dados / Recap / A1](../trilhas/estrutura-de-dados/a1.md)
- [Probabilidade / Recaps / A1_recap](../trilhas/probabilidade/a1.md)
- [Probabilidade / Recaps / A2_recap](../trilhas/probabilidade/a2.md)
- [Álgebra Linear Numérica / Recaps / A1](../trilhas/algebra-linear-numerica/a1.md)
- [Álgebra Linear Numérica / Recaps / A2](../trilhas/algebra-linear-numerica/a2.md)

### 4 semestre

- [Ciência de Redes / Recaps / A1](../trilhas/ciencia-de-redes/a1.md)
- [Ciência de Redes / Recaps / A2](../trilhas/ciencia-de-redes/a2.md)
- [Inferência Estatística / Recaps / A1](../trilhas/inferencia-estatistica/a1.md)
- [Inferência Estatística / Recaps / A2](../trilhas/inferencia-estatistica/a2.md)
- [Modelagem Informacional / Recaps / A1](../trilhas/modelagem-informacional/a1.md)
- [Modelagem Informacional / Recaps / A2](../trilhas/modelagem-informacional/a2.md)
- [Otimização para CD / Recaps / A1](../trilhas/otimizacao-para-ciencia-de-dados/a1.md)
- [Otimização para CD / Recaps / A2](../trilhas/otimizacao-para-ciencia-de-dados/a2.md)
- [Projeto e Análise de Algoritmos / Exercises / ExListas](../trilhas/projeto-e-analise-de-algoritmos/exercicios-listas.md)
- [Projeto e Análise de Algoritmos / Exercises / ExSlides](../trilhas/projeto-e-analise-de-algoritmos/exercicios-slides.md)
- [Projeto e Análise de Algoritmos / Recaps / A1](../trilhas/projeto-e-analise-de-algoritmos/a1.md)
- [Projeto e Análise de Algoritmos / Recaps / A2](../trilhas/projeto-e-analise-de-algoritmos/a2.md)

### 5 semestre

- [Machine Learning / A1](../trilhas/aprendizado-de-maquina/a1.md)
- [Machine Learning / A2](../trilhas/aprendizado-de-maquina/a2.md)
- [Machine Learning / A3](../trilhas/aprendizado-de-maquina/a3.md)
- [Modelagem Estatística / A1](../trilhas/modelagem-estatistica/a1.md)

### 6 semestre

- [Deep Learning / A1](../trilhas/aprendizado-profundo/a1.md)
- [Engenharia de Software / Exp](../trilhas/engenharia-de-software/notas-de-aula.md)
- [Processamento de Linguagem Natural / A1](../trilhas/processamento-de-linguagem-natural/a1.md)
- [Séries Temporais / A1](../trilhas/series-temporais/a1.md)

### Eletivas

- [Computação na Nuvem / A1](../trilhas/computacao-na-nuvem/a1.md)

### Mestrado

- [Aprendizado por Reforço / Recap](../trilhas/aprendizado-por-reforco/revisao-geral.md)
- [Causalidade / Recap](../trilhas/causalidade/revisao-geral.md)
