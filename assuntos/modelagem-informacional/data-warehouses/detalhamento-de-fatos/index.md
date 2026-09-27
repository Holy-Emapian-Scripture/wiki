---
layout: "default"
title: "Detalhamento de Fatos — Data Warehouses"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A1.md"
trilha: "../../../../trilhas/modelagem-informacional/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 9
---

[Modelagem Informacional](../../index.md) · [Data Warehouses](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-17"></a>

# Detalhamento de Fatos

Antes disso, precisamos entender melhor sobre a **granularidade** da tabela. A granularidade e refere a o que uma única linha de uma tabela se refere. Tabelas de fato com um refinamento alto de granularidade expressam um único fato, enquanto tabelas com granularidade maior expressam, em suma, um conjunto de fatos agrupado. Por conta desse detalhamento v.s agrupamento, ambas possuem suas vantagens e desvantagens

Com base na granularidade da tabela, podemos classificá-la em duas:

- **Line-item detailed fact table**: Cada linha representa uma linha de item de uma transação em particular

- **Transaction-level detailed fact table**: Cada linha representa uma transação em particular

Um exemplo fica melhor de compreender

**Exemplo**

Vamos imaginar que temos um negócio de aluguel de carro, e que nós alugamos o carro de forma que o nosso cliente pode escolher alguns acessórios a mais (Por exemplo, ele vai pagar $R\$ 40,00$ adicionais para colocar uma cadeirinha de bebê). Como cada transação pode ter características diferentes, faz sentido que cada fato de transação tenha uma especificação dizendo os itens específicos que foram juntos, então teríamos uma **line-item detailed fact table**.

Mas vamos supor que você não da essa opção aos clientes, e eles tenham que escolher baseado em categorias (Por exemplo, a categoria A é mais barata, não tem ar-condicionado, não tem gps, entre outras coisas e eu tenho outras categorias também), então não faz muito sentido adicionar **na tabela fatos** todas as coisas inclusas nas categorias, e sim adicionar isso na **dimensão** do fato, já que não é algo que varia de fato para fato. Nesse caso, teríamos uma **transaction-level detailed fact table**

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/modelagem-informacional/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/modelagem-informacional/a1.md#apresentacao-original)

- Anterior: [Galáxia de Estrelas](../galaxia-de-estrelas/index.md)
- Próximo: [Dimensões Lentamente Alteráveis](../dimensoes-lentamente-alteraveis/index.md)
