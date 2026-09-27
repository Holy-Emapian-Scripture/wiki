---
layout: "default"
title: "Como um Data Warehouse é estruturado? — Data Warehouses"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A1.md"
trilha: "../../../../trilhas/modelagem-informacional/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 4
---

[Modelagem Informacional](../../index.md) · [Data Warehouses](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Como um Data Warehouse é estruturado?

![Passo-a-passo da montagem de um Data Warehouse](../../assets/data-warehouse-structure.png)

*Figura 6. Passo-a-passo da montagem de um Data Warehouse*

<a id="secao-5"></a>

## DWH Requirements

Elicitação de requisitos, definições e visualização – deve especificar as capacidades e funcionalidades desejadas do futuro DW

- Os requisitos são embasados nas necessidades analíticas que podem ser supridas pelos dados dos sistemas de origem disponíveis, tanto internos quanto externos

- A coleta de requisitos é feita através de entrevistas com vários stakeholders

- Além das entrevistas, métodos adicionais para elicitação de requisitos podem ser usados, tais como grupos focais, surveys, observações de processos existentes, etc

- A coleta de requisitos deve ser definida e escrita claramente em um documento, e então visualizada como um modelo de dados conceitual.

<a id="secao-6"></a>

## DWH Modeling

Modelagem do data warehouse (modelagem lógica do DW) – criação do modelo de dados do DW que é implementável em um SGBD

- Logo após a etapa de coleta de requisitos inicia-se a modelagem do DW, de onde serão criados modelos implementáveis no SGBD escolhido.

- O Modelo de dados lógico ou modelo de dados de implementação leva em conta a lógica particular do software de gerenciamento de banco de dados escolhido.

<a id="secao-7"></a>

## Creating DWH

Criação do DW – usar um SGBD para implementar o modelo de dados do DW

- Tipicamente, os data warehouses são implementados usando os mesmos SGBDs dos bancos operacionais, tais como MS SQL, Oracle,

- No entanto, existem SGBDs especializados em processar grandes volumes de dados, tais como Teradara e Vertica

<a id="secao-8"></a>

## ETL Infraestructure

- Criar procedimentos e códigos para:

  - Extração automática de dados relevantes das fontes de dados operacionais

  - Transformação dos dados extraídos, de forma que a qualidade seja assegurada e a estrutura seja aderente ao modelo de DW implementado

  - A carga contínua dos dados transformados para dentro do data warehouse

- Devido à quantidade de detalhes que devem ser considerados, a criação da infraestrutura ETL costuma ser a parte que mais consome tempo e recursos do processo de desenvolvimento do data warehouse.

<a id="secao-9"></a>

## Developing Front-End Applications

Desenvolvimento de aplicações front-end (BI) - projetar e criar aplicativos para uso indireto pelos usuários finais

- Os aplicativos front-end estão incluídos na maioria dos DW e são frequentemente chamados de aplicativos de inteligência de negócios (BI)

- Os aplicativos front-end contêm interfaces (como formulários e relatórios) acessíveis por meio de um mecanismo de navegação (como um menu)

<a id="secao-10"></a>

## DWH Deployment

Liberar o DW e seus aplicativos front-end (BI) para uso dos usuários finais

<a id="secao-11"></a>

## DWH Use

Uso do data warehouse - a leitura dos dados no data warehouse

- Uso indireto

  - Via front-end (BI) applications

- Uso direto

  - Via SGBD

  - Via OLAP (BI) tool

<a id="secao-12"></a>

## SWH Administration and Maintenance

Administração e manutenção do data warehouse - realizar atividades que dão suporte ao usuário final do DW, incluindo o tratamento de questões técnicas, tais como:

- Fornecer segurança para as informações contidas no data warehouse

- Garantir espaço suficiente no disco rígido para o conteúdo do data warehouse

- Implementar os procedimentos de backup e recuperação

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/modelagem-informacional/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/modelagem-informacional/a1.md#apresentacao-original)

- Anterior: [O que é?](../o-que-e/index.md)
- Próximo: [Modelo Dimensional](../modelo-dimensional/index.md)
