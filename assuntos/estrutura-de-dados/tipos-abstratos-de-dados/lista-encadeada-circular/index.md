---
layout: "default"
title: "2.6 Lista encadeada circular — 2. Tipos Abstratos de Dados"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 11
---

[Estrutura de Dados](../../index.md) · [2. Tipos Abstratos de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-11"></a>

# 2.6 Lista encadeada circular

Nesse caso, basta colocar um ponteiro tail na struct SingleLinkedList apontando para a cauda (tail), e atualizar nas funções mostradas anteriormente. Como a lista não tem um tamanho pré-fixado, também não é necessário tratar casos com o módulo da lista, etc. Fica a cargo do leitor.

- **Obs.1:**

Uma limitação da lista encadeada simples é que ela só vê o próximo elemento, o que é problemático em situações como remoção de um nó ou verificação do elemento anterior numa lista. Para solucionar esse problema, basta adicionarmos um ponteiro tail em cada um dos nós da lista!

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [2.5 Lista (simplesmente) encadeada](../lista-simplesmente-encadeada/index.md)
- Próximo: [2.7 Lista duplamente encadeada](../lista-duplamente-encadeada/index.md)
