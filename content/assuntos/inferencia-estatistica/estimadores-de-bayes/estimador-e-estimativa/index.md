---
layout: "default"
title: "Estimador e Estimativa — Estimadores de Bayes"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 9
---

[Inferência Estatística](../../index.md) · [Estimadores de Bayes](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-9"></a>

# Estimador e Estimativa

Com estimadores, queremos, a partir, puramente, de nossas observações dos dados gerar uma função que, ao longo prazo, converge para uma medida de nosso interesse (Um parâmetro de distribuição, por exemplo)

**Definição: Estimador/Estimativa**

Seja $X_{1},\ldots,X_{n}$ os dados observados que a distribuição conjunta é indexada por um parâmetro $\theta$ e assume valores em um conjunto $\Omega$ na reta real (Cada observação $X_{i}$). Um estimador do parâmetro $\theta$ é uma função $\delta:\Omega^{n} \rightarrow {\mathbb{R}}$ ($\delta(X_{1},\ldots,X_{n})$). Se $X_{1} = x_{1},\ldots,X_{n} = x_{n}$ são observados, então $\delta(x_{1},\ldots,x_{n})$ é uma estimativa de $\theta$

Vale ressaltar a diferença entre **estimador** e **estimativa**. O **estimador** é uma função das variáveis aleatórias, ou seja, ele também é uma variável aleatória e pode ter sua distribuição derivada da distribuição conjunta de $X_{1},\ldots,X_{n}$. Já uma **estimativa** é o resultado de $\delta(\underline{X})$ após serem observado os valores $x_{1},\ldots,x_{n}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Estimadores de Bayes](../index.md)
- Próximo: [Função de Perda](../funcao-de-perda/index.md)
