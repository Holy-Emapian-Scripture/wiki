---
layout: "default"
title: "Hipóteses Nula e Alternativa — Análise e Teste de Hipóteses"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 20
---

[Inferência Estatística](../../index.md) · [Análise e Teste de Hipóteses](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-20"></a>

# Hipóteses Nula e Alternativa

Nós temos $\theta \in \Omega$ e vamos particionar o espaço em dois conjuntos disjuntos $\Omega_{0}$ e $\Omega_{1}$ e queremos testar as duas hipóteses: $$H_{0}:\theta \in \Omega_{0}\text{\quad\quad}H_{1}:\theta \in \Omega_{1}$$

**Definição**

$H_{0}$ é chamada de **hipótese nula** e $H_{1}$ a **hipótese alternativa**. Se decidirmos que $\theta \in \Omega_{1}$, então nós **REJEITAMOS** $H_{0}$, se $\theta \in \Omega_{0}$, nós **NÃO REJEITAMOS** $H_{0}$

Ué, porque não falamos que **aceitamos** a hipótese $H_{0}$? Esse modo de visualizar o teste de hipóteses foi popularizado por Ronald Fisher, Jerzy Neyman e Egon Pearson. Essa visualização de assemelha muito ao sistema jurídico, onde seguimos o princípio da presunção de inocência:

- **Hipótese Nula $H_{0}$**: Representa o status quo, a crença estabelecida, o “nenhum efeito” ou a “igualdade”. É a hipótese que se presume verdadeira até que haja evidência estatística suficiente para o contrário. (Ex: “O réu é inocente”)

- **Hipótese Alternativa ($H_{1}$)**: É a afirmação que o pesquisador está tentando encontrar evidências para suportar. (Ex: “O réu é culpado.”)

Ou seja, o teste foca em coletar dados que são **inconsistentes** a $H_{0}$. Vamos tentar esclarecer com um exemplo. Você quer saber se uma nova dieta reduziu o peso médio dos participantes.

- $H_{0}$: O peso médio não mudou (o efeito da dieta é zero).- $H_{1}$: O peso médio diminuiu.

Se os dados mostrarem uma grande redução de peso, você rejeita a $H_{0}$ e conclui que a dieta funcionou. Se os dados mostrarem apenas uma pequena redução, ou um aumento, você não rejeita a $H_{0}$. Você conclui: “Os dados não fornecem evidência suficiente para dizer que a dieta reduziu o peso.” Você não conclui: “A dieta definitivamente não teve efeito.”

**Exemplo: Exemplo simples**

Temos uma hipótese principal que é “Correr é diminui/intensifica os sintomas da depressão”, então vamos dividir essa hipótese geral nas duas hipóteses que mencionamos anteriormente

- $H_{0}$: Correr não afeta em nada os sintomas da depressão

- $H_{1}$: Correr diminui/intensifica os sintomas da depressão

Dividimos assim pois, até o momento, queremos comprovar que correr tem algum efeito nos sintomas da depressão, e enquanto não o comprovarmos, assumimos que a atividade física não faz efeito

**Definição: Hipótese Simples e Composta**

Se $\Omega_{i}$ contém apenas $1$ valor de $\theta$, então $H_{i}$ é simples. Se $\Omega_{i}$ contém mais que um valor, então $H_{i}$ é composta

Quando a hipótese é simples, a distribuição das observações é bem especificada. Já sob hipóteses compostas, dizemos que eles pertencem a uma classe. Uma hipótese nula simples tem a forma: $$H_{0}:\theta = \theta_{0}$$

**Definição: Hipótese unilateral e multilateral**

Seja $\theta \in R$, hipóteses nulas unidimensionais são da forma $H_{0}:\theta \leq \theta_{0}$ ou $H_{0}:\theta \geq \theta_{0}$. Já hipóteses nulas simples ($H_{0}:\theta = \theta_{0}$) tem hipóteses multilaterais alternativas ($H_{1}:\theta \neq \theta_{0}$)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Análise e Teste de Hipóteses](../index.md)
- Próximo: [Região Crítica e Testes Estatísticos](../regiao-critica-e-testes-estatisticos/index.md)
