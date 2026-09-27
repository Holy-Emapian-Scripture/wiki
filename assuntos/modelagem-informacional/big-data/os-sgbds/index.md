---
layout: "default"
title: "Os SGBDs — Big Data"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A2.md"
trilha: "../../../../trilhas/modelagem-informacional/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 7
---

[Modelagem Informacional](../../index.md) · [Big Data](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# Os SGBDs

Além de ferramentas para utilizar dentro de um Data Lake, também podemos inserir os tipos de SGBDs, já que antes, vimos apenas os Transacionais (Otimizados para OLTP) e Analíticos (Otimizados para OLAP)

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| **Tipo de SGBD** | **Finalidade** | **Armazenamento** | **Característica Chave** |
| **Transacional** | OLTP (**Online Transaction Processing**): Suporte a operações diárias. | Row Store (Baseado em Linhas). | Garante **ACID** e alta concorrência de escritas. |
| **Analítico** | OLAP (**Online Analytical Processing**): Consultas complexas em grandes volumes de dados históricos. | Column Store (Baseado em Colunas). | Otimizado para **leituras rápidas** e agregações em muitas linhas. |
| **Cluster** | Arquitetura que distribui dados e processamento por múltiplos servidores (nós). | Distribuído/Particionado. | Oferece **alta escalabilidade horizontal** e tolerância a falhas. |
| **Row Store** | Armazena registros completos em blocos contínuos. | Linha por Linha. | **Eficiente para inserir ou atualizar** um registro completo (transações). |
| **Column Store** | Armazena valores de uma coluna juntos em blocos contínuos. | Coluna por Coluna. | **Eficiente para analisar** poucas colunas em milhões de linhas. Permite alta **compressão**. |

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/modelagem-informacional/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/modelagem-informacional/a2.md#apresentacao-original)

- Anterior: [Ferramentas para Big Data](../ferramentas-para-big-data/index.md)
- Próximo: [Arquiteturas](../arquiteturas/index.md)
