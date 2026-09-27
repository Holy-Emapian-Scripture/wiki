---
layout: "default"
title: "Definição — Tabela Hash"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A1.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
revisao: "Thalis Ambrosim Falqueto"
ano_original: 2025
ordem_na_trilha: 13
---

[Projeto e Análise de Algoritmos](../../index.md) · [Tabela Hash](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Definição

Agora que entendemos toda a ideia da hash table, podemos fazer uma definição melhor para ela

**Definição: Hash Table**

A **tabela hash** é uma estrutura de dados baseada em um vetor de $M$ posições acessado através de endereçamento direto

**Definição: Função de Espalhamento/Hashing**

É uma função que mapeia uma chave em um índice $\lbrack 0,M - 1\rbrack$ do vetor. O resultado dessa função é comumente chamado de **hash**. O objetivo da função de espalhamento é reduzir o intervalo de índices de forma que M seja muito menor que o tamanho do universo U.

**Exemplo**

    hash(key) = key % M

**Definição: Colisão**

É quando a função de espalhamento gera os mesmos hashes para chaves diferentes. Existem várias abordagens para resolver esse problema

Uma função de hash é considerada **boa** quando minimiza as colisões (Mas, pelo princípio da casa dos pombos, elas são inevitáveis, pois quase sempre existem mais elementos do que chaves).

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Desafio](../desafio/index.md)
- Próximo: [Soluções para colisão](../solucoes-para-colisao/index.md)
