---
layout: "default"
title: "Introdução às Séries Temporais"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/A1.md"
trilha: "../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 1
---

[Séries Temporais](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-1"></a>

# Introdução às Séries Temporais


<a id="definicoes"></a>
<a id="secao-2"></a>

## Definições

**Definição: Série Temporal de Tempo Discreto**

Conjunto de observações $y_{t}$ registradas em intervalos de tempo específico $t$ medidas de forma **discreta**. $$\left\{ y_{t} \right\}\vert _{t = 1}^{T}$$

**Exemplo**

A temperatura de uma região registrada **diariamente**

**Definição: Modelo de Séries Temporais**

Um modelo de séries temporais para $\left\{ y_{t} \right\}$ é a **especificação da distribuição conjunta** de uma **sequência de variáveis aleatórias** $\left\{ Y_{t} \right\}$ das quais $\left\{ y_{t} \right\}$ é esperada ser uma realização $${\mathbb{P}}(X_{1} \leq x_{1},\ldots,X_{n} \leq x_{n}), - \infty < x_{1},\ldots,x_{n} < \infty,n = 1,2,\ldots$$

Modelar essa distribuição é muito complexo, pois temos acesso apenas à uma realização da série temporal $\left\{ Y_{t} \right\}$. Para contornar essa limitação, focamos nos momentos de **primeira** e **segunda** ordem $${\mathbb{E}}\left\lbrack Y_{t} \right\rbrack\text{ e }{\mathbb{E}}\left\lbrack Y_{t}Y_{t + h} \right\rbrack$$

<a id="por-que-modelar-series-temporais-e-importante"></a>
<a id="secao-3"></a>

## Por que modelar séries temporais é importante?

Até agora, discutimos principalmente o tratamento de dados que não possuem uma estrutura temporal. No entanto, muitas vezes nos deparamos com dados onde o tempo desempenha um papel crucial.

<a id="secao-4"></a>

### Dependência Temporal dos Resíduos

Quando os modelos discutidos anteriormente não conseguem capturar completamente a estrutura dos dados, pode restar uma dependência temporal nos resíduos. Isso significa que as observações ao longo do tempo estão correlacionadas, e essa dependência não foi removida.

Modelar essa dependência temporal pode levar a previsões mais precisas, pois aproveitamos a informação contida na sequência temporal dos dados.

<a id="secao-5"></a>

### Como identificar dependência temporal nos resíduos?

Podemos utilizar ferramentas que vamos conhecer ao longo do curso, como gráficos de autocorrelação (ACF) e testes estatísticos (como o teste de Ljung-Box) para identificar padrões temporais nos resíduos. Esses métodos nos ajudam a verificar se há correlação significativa entre os resíduos em diferentes lags temporais.

<a id="secao-6"></a>

### Como modelar essa dependência?

Uma vez identificada a dependência temporal, podemos usar modelos de séries temporais, como por exemplo os modelos auto-regressivos (AR), modelos de média móvel (MA) ou modelos ARIMA, que são projetados para capturar e modelar essas dependências de maneira eficaz.

<a id="secao-7"></a>

### Usos

Existem $3$ usos complementares **principais** para séries temporais:

**Descrever**. Entender o que aconteceu na série: tendência, sazonalidade, choques, mudanças de regime. A pergunta é interpretativa — *o que o traço temporal revela?*

**Diagnosticar**. Avaliar se um modelo (clássico com covariáveis, baseline ingênuo, etc.) ainda deixou memória no tempo nos resíduos. Se os erros em $t$ e em $t + h$ ainda se relacionam de forma sistemática, a estrutura temporal não foi absorvida. Ferramentas formais de identificação (por exemplo ACF e testes como Ljung-Box) entram mais adiante no curso; o ponto conceitual já agora é: diagnóstico temporal é parte do trabalho, não um acessório opcional.

**Prever**. Produzir expectativas para $t + 1,\ldots,t + h$ com base no passado disponível até . Previsão boa não é apenas “ajustar bem o histórico”; é generalizar para a frente, sob a mesma seta do tempo

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/series-temporais/a1.md#apresentacao-original)

- Próximo: [Modelagem Clássica aplicada ao Tempo](../modelagem-classica-aplicada-ao-tempo/index.md)
