---
layout: "default"
title: "Caracterização — Big Data"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A2.md"
trilha: "../../../../trilhas/modelagem-informacional/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 5
---

[Modelagem Informacional](../../index.md) · [Big Data](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Caracterização

Após toda essa caracterização de um Data Lake, é interessante compararmos lado a lado com os bancos operacionais e data warehouses, então, a partir dos V definidos anteriormente, vamos montar tabelas de comparações para termos uma noção das diferenças entre os bancos operacionais, data warehouses e data lakes:

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| **Característica** | **Bancos Operacionais** | **Data Warehouse** | **Data Lakes / Big Data** |
| **Variedade** | Baixa (Homogênea) | Moderada a Alta (Integrada) | Extremamente Alta (Heterogênea) |
| **Velocidade** | Alta (Transacional em Tempo Real/Quase Real) | Baixa (Processamento em Lotes/Agendado) | Altíssima (Streaming Contínuo e Lotes Massivos) |
| **Volume** | Baixo a Moderado | Alto (Histórico Agregado) | Massivo (Petabytes/Exabytes) |
| **Veracidade** | Mais Alta (Garantida por ACID) | Alta (Garantida por ETL/Limpeza) | Baixa a Moderada (Bruteza, Inconsistência Inerente) |
| **Valor** | Baixo (Tático e Imediato) | Alto (Estratégico, Histórico) | Altíssimo (Preditivo, Inovação, MLOps) |
| **Variabilidade** | Muito Baixa (Estável, Esquema Fixo) | Baixa (Controlada via ETL) | Alta (Inconsistente, Mudança Contínua de Estrutura) |
| **Visualização** | Simples (Detalhada, Telas de Sistema) | Direta (BI Tools, Dashboards) | Complexa (Exploratória, Requer Processamento Prévio) |

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/modelagem-informacional/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/modelagem-informacional/a2.md#apresentacao-original)

- Anterior: [Data Lake](../data-lake/index.md)
- Próximo: [Ferramentas para Big Data](../ferramentas-para-big-data/index.md)
