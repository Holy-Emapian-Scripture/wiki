---
layout: "default"
title: "2.4 Comparação entre TADs — 2. Tipos Abstratos de Dados"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 9
---

[Estrutura de Dados](../../index.md) · [2. Tipos Abstratos de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-9"></a>

# 2.4 Comparação entre TADs

Para cada propósito ao qual cada TAD é designado, quase todas as principais operações são $O(1)$. Veja:

|          |        |                |                         |
|----------|--------|----------------|-------------------------|
| Operação | Pilha  | Fila com array | Fila com array circular |
| inserir  | $O(1)$ | $O(1)$         | $O(1)$                  |
| Remover  | $O(1)$ | $O(n)$         | $O(1)$                  |
| Buscar   | $O(1)$ | $O(1)$         | $O(1)$                  |

Mas, até agora, todas as estruturas de dados que aprendemos têm em geral, um problema: Todas elas são baseadas num array de tamanho fixo, passado na inicialização do TAD. Isso é um problema por dois dois motivos:

1.  Excesso de espaço dependendo do caso;

2.  Falta de espaço dependendo do caso.

Como solucionar esse problema?

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [2.3 Fila circular](../fila-circular/index.md)
- Próximo: [2.5 Lista (simplesmente) encadeada](../lista-simplesmente-encadeada/index.md)
