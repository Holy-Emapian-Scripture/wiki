---
layout: "default"
title: "ETL e OLAP"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A1.md"
trilha: "../../../trilhas/modelagem-informacional/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 13
---

[Modelagem Informacional](index.md)

<!-- wiki:original:inicio -->

<a id="secao-27"></a>

# ETL e OLAP


<a id="extrair"></a>
<a id="secao-28"></a>

## Extrair

O ETL vai recuperar os dados analíticos úteis das devidas fontes e, eventualmente, serão carregados no Data Warehouse. O que vai ser extraído é **determinado na etapa de requisitos**

<a id="transformacao"></a>
<a id="secao-29"></a>

## Transformação

Transformar a estrutura de dados coletada das fontes em estruturas compatíveis com o Data Warehouse modelado. O controle e melhoría da qualidade dos dados também estão inseridos nessa etapa.

<a id="secao-30"></a>

### Transformações Ativas

Após a transformação da estrutura de dados retornada pela **fonte**, a nova estrutura possui um número diferente de linhas (Quantidade de informações)

**Exemplo**

Remoção de duplicatas, agregação de linhas, dimensões de mudança lenta (Tipo 2), etc.

<a id="secao-31"></a>

### Transformações Passivas

Após a transformação da estrutura de dados retornada pela **fonte**, a nova estrutura não possui alterações no número de linhas (Quantidade de informações)

**Exemplo**

Gerar surrogate keys, atributos derivados, etc.

<a id="load-carga"></a>
<a id="secao-32"></a>

## Load/Carga

Insere (Carrega) os novos dados de qualidade garantida no Data Warehouse. É um processo automatico que deve ser idealizado para que o usuário não tenha que se preocupar com o processo

Temos dois tipos de Load em um ETL:

**Definição: Carga Inicial**

Preenche um Data Warehouse vazio. Pode envolver grandes quantidades de dados, dependendo de qual é o horizonte de tempo desejado dos dados no data warehouse recém-iniciado

**Definição: Carga de Atualização**

Atualiza um Data Warehouse já iniciado. Feito em um período pré-determinado pela empresa (**Ciclo de Atualização**). Em **Data Warehouses ativos**, essas cargas ocorrem continuamente (Em microlotes)

<a id="infraestrutura-de-um-etl"></a>
<a id="secao-33"></a>

## Infraestrutura de um ETL

Normalmente, o processo de criação da infraestrutura ETL inclui o uso de ferramentas de software ETL especializadas e/ou código salvos. Devido à quantidade de detalhes que deve ser considerada, a criação de infraestrutura ETL é muitas vezes a parte que mais consome tempo e recursos no processo de desenvolvimento do data warehouse. Embora trabalhoso, o processo de criação da infraestrutura ETL é essencialmente predeterminado pelos resultados dos processos de coleta de requisitos e modelagem de data warehouse que especificam as fontes e o destino

<a id="processamentos"></a>
<a id="secao-34"></a>

## Processamentos

Temos dois tipos de processamento de informações, na disciplina de Banco de Dados, analisamos os conceitos de OLTP, em Modelagem Informacional, estamos abordando a OLAP

**Definição: Online Transaction Processing (OLTP)**

Atualização (Inserção, Remoção, Modificação), consultar e apresentar dados para fins operacionais

**Definição: Online Analytical Processing (OLAP)**

Consultar e apresentar dados de Data Warehouses e/ou Data Marts para fins analíticos

e temos os chamados **OLAB / BI Tools** que são ferramentas que permitem os usuários fazer alterações estruturais de forma intuitiva em um Data Warehouse, como apenas com cliques no mouse. Basicamente um frontend para mexer num Data Warehouse diretamente

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../trilhas/modelagem-informacional/a1.md) · [Apresentação e contexto da fonte](../../trilhas/modelagem-informacional/a1.md#apresentacao-original)

- Anterior: [Data Warehouses](data-warehouses.md)
