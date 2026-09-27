---
layout: "default"
title: "Introdução — Big Data"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A2.md"
trilha: "../../../../trilhas/modelagem-informacional/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 2
---

[Modelagem Informacional](../../index.md) · [Big Data](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-2"></a>

# Introdução

Na primeira parte do curso, nós vimos uma expansão dos conceitos de Banco de Dados, como eles eram expandidos dependendo da sua finalidade. Vimos a extensão de bancos operacionais para bancos analíticos (Data Warehouses) e sua estruturação e aqui não será diferente! Porém, antes de entender como estruturar novos dados, temos que entender os tipos de dados que vamos armazenar nessa parte do curso

Quando vamos trabalhar com conjuntos de dados, podemos categorizar eles em 3 tipos

- Bancos operacionais

- Data Warehouses

- Big Data

E é exatamente essa terceira que iremos abordar. Big Data são os conjuntos de dados em corporações que tem grande volume e diversificação, além de rápido crescimento. Não são modelados formalmente para consulta e recuperação e não são acompanhados de metadados detalhados

Ou seja, são aqueles tipos de dados que não são bem estruturados. Podemos fazer uma sub-divisão também nessa classificação:

- **Não-estruturados**: Não tem metadados detalhados, exemplo: Documentos de Texto

- **Semi-estruturados**: Possuem alguns metadados, mas não o suficiente para descrever completamente o dado num todo, exemplo: Mensagens de texto (Você tem estruturas de destinatário, remetente, horário, etc., mas o texto da mensagem em si não tem uma estruturação)

A gente pode tentar descrever Big Data com o que chamamos de V’s. Porém, essa descrição não é algo $100\%$, já que esse conteúdo e o que é ou não um dado de Big Data vai bastante do contexto e da interpretação

- **Volume**

- **Variedade** (Fontes)

- **Velocidade** (Entrada dos dados)

- **Veracidade** (Qualidade)

- **Variabilidade** (Interpretação)

- **Value**

- **Visualization** (Elaborada e complexa)

**Definição: Big Data**

Grandes volumes de conjuntos de dados diversificados e de crescimento rápido que, quando comparados com bancos operacionais ou data warehouses:

- Consideravelmente menos estruturados (Poucos ou nenhum metadado)

- No geral: $+$Volume, $+$Velocidade, $+$Variabilidade

- Mais problemas na qualidade dos dados (Veracidade)

- Maiores as gamas de interpretações (Variabilidade)

- Abordagem mais exploratória e experimental para gerar Valor

- Se beneficia mais com visualizações elaboradas e inovadoras

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/modelagem-informacional/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/modelagem-informacional/a2.md#apresentacao-original)

- Anterior: [Big Data](../index.md)
- Próximo: [MapReduce e Hadoop](../mapreduce-e-hadoop/index.md)
