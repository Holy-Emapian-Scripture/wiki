---
layout: "default"
title: "Inferência Aproximada - O valor de uma premissa"
tipo: "conteudo"
disciplina: "Modelagem Estatística"
origem: "5 semestre/Modelagem Estatística/A1.md"
trilha: "../../../trilhas/modelagem-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 1
---

[Modelagem Estatística](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-1"></a>

# Inferência Aproximada - O valor de uma premissa

------------------------------------------------------------------------

Quando estávamos estudando Inferência Estatística, vimos que, em geral, nosso ponto de partida era um modelo e um conjunto de dados, e nosso trabalho era fazer boas inferências sobre o conjunto de dados e os parâmetros do modelo. No entanto, o quão bom os resultados são depende do quão bem o modelo se encaixa aos dados, dessa forma, erros podem ocorrer se o modelo não se adequar aos dados. Já na Modelagem Estatística, o ponto de partida é um conjunto de dados, e nosso trabalho é encontrar um modelo que se encaixe bem aos dados, para isso testamos diversos modelos. Nesse primeiro tópico, vamos ver na prática alguns processos que podem ser feito sobre poucas premissas acerca do processo gerador de dados (DGP - Data Generating Process, é o processo que gera os dados, e é o que queremos modelar).

Para isso vamos analisar medições da concentração (em partes por milhão - ppm) de um composto químico em $n = 10$ amostras de bateladas de um determinado produto. Para acessar o dataset, basta acessar o repositório do professor clicando \[aqui\](<https://github.com/maxbiostat/stats_modelling/tree/master/data>). O arquivo é um CSV, e as medições estão na coluna “ppm”.

``` python
import pandas as pd
data = pd.read_csv("data/ppm.csv")
```
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../trilhas/modelagem-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/modelagem-estatistica/a1.md#apresentacao-original)

