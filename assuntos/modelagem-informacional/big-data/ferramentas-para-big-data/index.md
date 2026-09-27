---
layout: "default"
title: "Ferramentas para Big Data — Big Data"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A2.md"
trilha: "../../../../trilhas/modelagem-informacional/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 6
---

[Modelagem Informacional](../../index.md) · [Big Data](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-6"></a>

# Ferramentas para Big Data

Eu comentei um pouco antes sobre o MapReduce e sua implementação, o Hadoop, mas existem várias abordagens para processamento de grandes volumes de dados

|  |  |  |
|:--:|:--:|:--:|
| **Ferramenta** | **O que é** | **Papel no Data Lake/Big Data** |
| **Hadoop** | Um **framework** de código aberto para armazenamento e processamento distribuído. | É o **sistema operacional** do Big Data. Fornece a base para construir o Data Lake. |
| **HDFS** | **Hadoop Distributed File System** | É o **sistema de arquivos** primário do Hadoop. Permite armazenar dados brutos e massivos de forma tolerante a falhas. É o **coração do armazenamento** do Data Lake. |
| **Gremlin** | Uma linguagem de consulta (**traversal language**) para **Bancos de Dados de Grafo**. | Usado para **analisar relacionamentos complexos**. É a linguagem mais **eficiente** para consultas que “caminham” por conexões profundas. |
| **Pachyderm** | Uma plataforma de **Data Versioning** e orquestração de **pipelines**. | Garante a **reprodutibilidade e governança** no **Data Lake** e em projetos de **Machine Learning** (MLOps). |
| **Contêiner** | Tecnologia para empacotar código e todas as suas dependências (Ex: Docker, Kubernetes). | Usado para **implantar** serviços de processamento de forma **isolada, escalável e portátil** dentro de um **cluster** de **Big Data**. |
| **Splunk** | Plataforma para **coletar, indexar e analisar dados de log, métricas e eventos** gerados por máquinas. | Otimizado para **observabilidade, segurança e solução de problemas**. Excelente para dados de **alta velocidade** (logs). |
| **Hive** | Um **software** que facilita a consulta e análise de grandes conjuntos de dados armazenados no HDFS. | Fornece uma camada de **SQL** sobre o Hadoop. Permite que analistas de dados consultem o Data Lake sem escrever código MapReduce/Spark. |

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/modelagem-informacional/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/modelagem-informacional/a2.md#apresentacao-original)

- Anterior: [Caracterização](../caracterizacao/index.md)
- Próximo: [Os SGBDs](../os-sgbds/index.md)
