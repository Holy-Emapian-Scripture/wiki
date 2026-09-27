---
layout: "default"
title: "Transformação — ETL e OLAP"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A1.md"
trilha: "../../../../trilhas/modelagem-informacional/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 15
---

[Modelagem Informacional](../../index.md) · [ETL e OLAP](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-29"></a>

# Transformação

Transformar a estrutura de dados coletada das fontes em estruturas compatíveis com o Data Warehouse modelado. O controle e melhoría da qualidade dos dados também estão inseridos nessa etapa.

<a id="secao-30"></a>

## Transformações Ativas

Após a transformação da estrutura de dados retornada pela **fonte**, a nova estrutura possui um número diferente de linhas (Quantidade de informações)

**Exemplo**

Remoção de duplicatas, agregação de linhas, dimensões de mudança lenta (Tipo 2), etc.

<a id="secao-31"></a>

## Transformações Passivas

Após a transformação da estrutura de dados retornada pela **fonte**, a nova estrutura não possui alterações no número de linhas (Quantidade de informações)

**Exemplo**

Gerar surrogate keys, atributos derivados, etc.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/modelagem-informacional/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/modelagem-informacional/a1.md#apresentacao-original)

- Anterior: [Extrair](../extrair/index.md)
- Próximo: [Load/Carga](../load-carga/index.md)
