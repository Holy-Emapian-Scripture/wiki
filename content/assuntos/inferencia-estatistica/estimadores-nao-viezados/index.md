---
layout: "default"
title: "Estimadores não-viezados"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 16
---

[Inferência Estatística](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-16"></a>

# Estimadores não-viezados


<a id="estimador-nao-viezado-da-variancia"></a>
<a id="secao-17"></a>

## Estimador não-viezado da Variância

**Teorema**

Seja $X_{1},\ldots,X_{n}$ uma amostra de uma distribuição indexada por $\theta$ e ${\mathbb{V}}\left\lbrack X_{i} \right\rbrack = \sigma^{2}$, então o seguinte estimador é não-viezado: $${\hat{\sigma}}^{2} = \frac{1}{n - 1}\sum_{i = 1}^{n}\left( X_{i} - {\overline{X}}_{n} \right)^{2}$$

**Demonstração**

Vamos utilizar do fato que: $$\sum_{i = 1}^{n}\left( X_{i} - \mu \right)^{2} = \sum_{i = 1}^{n}\left( X_{i} - {\overline{X}}_{n} \right)^{2} + {n\left( {\overline{X}}_{n} - \mu \right)}^{2}$$ Então vamos ter que (Tirando a esperança nos dois lados da equação mostrada anteriormente): $$\begin{aligned} {\mathbb{E}}\left\lbrack {\hat{\sigma}}_{0}^{2} \right\rbrack & = \sigma^{2} - \frac{\sigma^{2}}{n} \\ & = \frac{n - 1}{n}\sigma^{2} \end{aligned}$$ logo, vamos ter que: $$\frac{n}{n - 1}{\mathbb{E}}\left\lbrack {\hat{\sigma}}_{0}^{2} \right\rbrack = {\mathbb{E}}\left\lbrack {\hat{\sigma}}^{2} \right\rbrack = \sigma^{2}$$

Esse estimador citado agora é chamado de **variância amostral** em diversas literaturas (No livro do DeGroot, a variância amostral é o estimador com $1/n$)

<a id="limitacoes"></a>
<a id="secao-18"></a>

## Limitações

- Muitas vezes os estimadores não-viezados possuem uma variância maior que os estimadores viezados, um bom exemplo é que ${\mathbb{V}}\left\lbrack {\hat{\sigma}}^{2} \right\rbrack \geq {\mathbb{V}}\left\lbrack {\hat{\sigma}}_{0}^{2} \right\rbrack$

- Não há garantia que estimadores não-viezados existam em toda situação. Um exemplo é que, se $X_{1},\ldots,X_{n} \sim \text{ Bern}(p)$, não existe estimador **não-viezado** de $\sqrt{p}$

- Estimadores inapropriados, mesmo sendo não-viezados. Por exemplo, se eu tenho uma sequência de bernoullis, e tentar estimar $p$ pela quantidade de erros até o primeiro sucesso $X$ (Geométrica). O estimador não viezado seria: $$\delta(X) = \begin{cases} 1\text{ se }X = 0 \\ 0\text{ se }X = 1 \end{cases}$$

- Os estimadores podem ignorar informações. Se você for medir a votlagem de um sistema com um multímetro, e ele retornar $2.5$, então podemos pensar que $\theta$ é $2.5$, mas e se o multímetro arredonda tudo que é maior que $3$ para $3$? Isso muda completamente a distribuição da informação

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Distribuições Impróprias](../analise-bayesiana-de-amostras-normais/index.md#distribuicoes-improprias)
- Próximo: [Análise e Teste de Hipóteses](../analise-e-teste-de-hipoteses/index.md)
