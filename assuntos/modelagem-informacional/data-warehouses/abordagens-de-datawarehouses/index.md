---
layout: "default"
title: "Abordagens de Datawarehouses — Data Warehouses"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A1.md"
trilha: "../../../../trilhas/modelagem-informacional/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 12
---

[Modelagem Informacional](../../index.md) · [Data Warehouses](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-23"></a>

# Abordagens de Datawarehouses

Vimos esse meio de se criar o Data Warehouse utilizando dos modelos estrela e floco de neve, porém, existem alguns métodos para abordar os Data Warehouses de formas diferentes. Porém, quando falamos de formas diferentes, não estamos dizendo que, por exemplo, se escolhermos uma dessas formas, automaticamente não podemos usar um modelo estrela, mas são algumas abordagens extras que podemos integrar dependendo do contexto

<a id="secao-24"></a>

## Data Warehouses Normalizados

Data warehouses utilizando de práticas-padrão de modelagem ER, de forma que ele mesmo serve como fonte para outros Data Warehouses que utilizam da modelagem dimensional e Data Marts dentro da empresa

![Data Warehouse Normalizado](../../assets/normalized-data-warehouse.png)

*Figura 16. Data Warehouse Normalizado*

<a id="secao-25"></a>

## Data Warehouse em Modelo Dimensional

Foi o que vimos na criação de Data Warehouses até esse momento, dividido em tabelas de dimensões e tabelas de fatos, onde um fato representa um acontecimento de interesse dentro do contexto do negócio e as dimensões são informações externas ao fato, mas que tem participação interna à ele

<a id="secao-26"></a>

## Data Marts Independentes

É quando vários **Data Marts** são criados em instâncias e setores diferentes da empresa, todos independentes um do outro. Consequentemente, isso faz com que **vários ETL’s** sejam criados

![Data Marts Independentes](../../assets/independent-data-marts.png)

*Figura 17. Data Marts Independentes*

Essa abordagem é considerada inferior, já que inviabiliza uma análise **direto-ao-ponto** de toda a empresa e a existência de **vários** ETL’s **não relacionados**

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/modelagem-informacional/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/modelagem-informacional/a1.md#apresentacao-original)

- Anterior: [Modelo Floco de Neve (Snowflake)](../modelo-floco-de-neve-snowflake/index.md)
- Próximo: [ETL e OLAP](../../etl-e-olap/index.md)
