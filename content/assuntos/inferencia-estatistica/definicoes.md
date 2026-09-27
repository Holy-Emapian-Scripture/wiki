---
layout: "default"
title: "Definições"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 1
---

[Inferência Estatística](index.md)

<!-- wiki:original:inicio -->
<a id="secao-1"></a>

# Definições

------------------------------------------------------------------------

Primeiro de tudo, precisamos entender o que estuda a Inferência Estatística. Isso nada mais é que um nome bonitinho para “chutar”. Na probabilidade, tinhamos uma variável aleatória com uma distribuição e um parâmetro bem-definidos, porém, na vida real, não é muito bem o que ocorre. Imagine que queremos saber o tempo de vida que as lâmpadas da minha fábrica vivem, a única coisa que vou ter como me basear são as lâmpadas que já tenho, é dessas informações que eu tenho que fazer uma inferência, seja ela qual for, como por exemplo, qual sua distribuição e qual é o parâmetro a ela associado

**Definição: Modelo Estatístico**

Um modelo estatístico consiste em:

1.  Identificar variáveis de interesse (Sejam elas observáveis ou hipoteticamente observáveis, como um parâmetro de distribuição)

2.  Especificar a distribuição conjunta (Ou uma família de distribuições) para variáveis observáveis

3.  Identificar os parâmetros de interesse em (2)

4.  (Se desejado) especificar uma distribuição para os parâmetros descritos

**Definição: Inferência Estatística**

É um procedimento que produz afirmações probabilísticas sobre algumas ou todas as partes de um modelo estatístico

**Definição: Parâmetro e Espaço Paramétrico**

Em um problema de inferência estatística, uma característica (ou combinações de características) que determina(m) a distribuição conjunta da(s) variável(eis) de interesse é chamada de parâmetro. O conjunto $\Theta$ de todos os possíveis valores de um parâmetro $\theta$ (Ou vetor paramétrico $\left( \theta_{1},\ldots,\theta_{k} \right)$) é chamado de **espaço paramétrico**

Dentro da estatística, podemos dividir os problemas que encontramos em algumas categorias:

- **Predição**: Podemos tentar prever o resultado de uma variável aleatória com base nas observações anteriores. Quando a variável é um parâmetro, chamamos de Estimação.

- **Problemas de Decisão Estatística**: Depois que dados experimentais foram analisados, podemos querer tomar decisões com base nos resultados do experimento. As consequências da decisão dependem dos resultados.

- **Design Experimental**: Em alguns problemas de inferência estatística, temos controle sobre o tipo de dados ou quantidade de dados experimentais coletados.

**Definição: Estatística**

Suponha que as variáveis aleatórias observáveis de interesse são $X_{1},\ldots,X_{n}$. Seja $r:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$. Então a variável aleatória $T = r\left( X_{1},\ldots,X_{n} \right)$ é chamada de estatística.

Há também uma discussão sobre se os parâmetros que estamos procurando serem variáveis aleatórias ou valores fixos. Por enquanto, assumiremos que os parâmetros são variáveis aleatórias. Essa discussão está mais bem detalhada no livro do **DeGroot**

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Próximo: [Estatística Bayesiana](estatistica-bayesiana.md)
