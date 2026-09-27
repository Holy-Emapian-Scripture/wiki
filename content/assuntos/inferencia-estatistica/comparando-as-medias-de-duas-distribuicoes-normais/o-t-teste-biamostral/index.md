---
layout: "default"
title: "O $t$-teste biamostral — Comparando as médias de duas Distribuições Normais"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 35
---

[Inferência Estatística](../../index.md) · [Comparando as médias de duas Distribuições Normais](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-35"></a>

# O $t$-teste biamostral

Primeiramente, considere o problema em que temos duas amostras de variáveis normais (com mesma variância) e queremos saber qual distribuição tem maior média. Especificamente, assumimos que $\underline{X} = \left( X_{1},\ldots,X_{m} \right)$ é uma amostra aleatória de $m$, onde $X \sim N\left( \mu_{X},\sigma^{2} \right)$ (com $\mu_{X}$ e $\sigma^{2}$ desconhecidos) e $\underline{Y} = \left( Y_{1},\ldots,Y_{n} \right)$ formam uma amostra independente da primeira de $n$ observações, onde $Y \sim N\left( \mu_{Y},\sigma^{2} \right)$. Estamos interessados em testar as hipóteses: $$H_{0}:\mu_{X} \leq \mu_{Y}\text{\quad\quad}H_{1}:\mu_{X} > \mu_{Y}$$<a id="two-sample-hypothesis-1"></a>

para cada procedimento $\delta$, vamos deixar que $\pi(\mu_{X},\mu_{Y},\sigma^{2}\vert \delta)$ seja a **power function** ([\[power-function\]](../../analise-e-teste-de-hipoteses/funcao-de-poder-e-tipos-de-erro/index.md#power-function)) de $\delta$. Vamos assumir que $\sigma^{2}$ é igual para ambas as distribuições, se esse requisito não fosse apropriado para o cenário analisado (posteriormente citarei um exemplo que esse caso é plausível), os testes $t$ que vamos derivar nas próximas seções não seriam apropriados.

Pensando em um $\delta$ intuitivo, se a diferença entre as médias ($\mu_{Y} - \mu_{X}$) for alta, faz sentido rejeitarmos $H_{0}$, certo?

**Teorema: Estatística $t$ para amostras duplas**

Assumindo a estrutura descrita nos parágrafos anteriores e definindo: $$\overline{X} = \frac{1}{m}\sum_{i = 1}^{m}X_{i}\text{\quad\quad}\overline{Y} = \frac{1}{n}\sum_{j = 1}^{n}X_{j}$$ $$S_{X}^{2} = \sum_{i = 1}^{m}\left( X_{i} - \overline{X} \right)^{2}\text{\quad\quad}S_{Y}^{2} = \sum_{j = 1}^{n}\left( Y_{j} - \overline{Y} \right)^{2}$$ defina então o teste estatístico: $$U = \frac{(m + n - 2)^{1/2}\left( \overline{X} - \overline{Y} \right)}{\left( \frac{1}{m} + \frac{1}{n} \right)^{1/2}\left( S_{X}^{2} + S_{Y}^{2} \right)^{1/2}}$$<a id="two-sample-u-statistic"></a> Para todos os valores de $\theta = \left( \mu_{X},\mu_{Y},\sigma^{2} \right)$ tais que $\mu_{X} = \mu_{Y}$, temos então que: $$U \sim t_{m + n - 2}$$

**Demonstração**

Assuma que $\mu_{X} = \mu_{Y}$. Defina as seguintes variáveis aleatórias: $$\begin{array}{r} Z = \frac{\overline{X} - \overline{Y}}{\left( \frac{1}{m} + \frac{1}{n} \right)^{1/2}\sigma} \\ W = \frac{S_{X}^{2} + S_{Y}^{2}}{\sigma^{2}} \end{array}$$ Agora podemos representar $U$ como: $$U = \frac{Z}{\left( W/(m + n - 2) \right)^{1/2}}$$ perceba que se provarmos que $Z \sim N(0,1)$, $W \sim Χ_{m + n - 2}^{2}$, e $Z$ e $W$ são independentes que o teorema está concluído. Desde o começo estamos assumindo que $X$ e $Y$ são independentes dado $\theta$. Desse fato, segue que toda função de $X$ é independente de toda função de $Y$, em particular, $\left( \overline{X},S_{X}^{2} \right)$ é independente de $\left( \overline{Y},S_{Y}^{2} \right)$. Pelo [\[sample-mean-and-sample-variance-independence\]](../../distribuicao-conjunta-da-media-e-variancia-amostral/independencia-da-media-e-variancia-amostrais/index.md#sample-mean-and-sample-variance-independence), sabemos que $\overline{X}$ e $S_{X}^{2}$ são independentes, assim como $\overline{Y}$ e $S_{Y}^{2}$, ou seja, todos $\overline{X}$, $\overline{Y}$, $S_{X}^{2}$ e $S_{Y}^{2}$ são independentes entre si, logo, $Z$ e $W$ também são independentes.

Segue também do [\[sample-mean-and-sample-variance-independence\]](../../distribuicao-conjunta-da-media-e-variancia-amostral/independencia-da-media-e-variancia-amostrais/index.md#sample-mean-and-sample-variance-independence) que: $$\frac{S_{X}^{2}}{\sigma^{2}} \sim Χ_{m - 1}^{2}\text{\quad\quad}\frac{S_{Y}^{2}}{\sigma^{2}} \sim Χ_{n - 1}^{2}$$ e pelas propriedades da $Χ^{2}$ ([\[sum-of-independent-chi-squares\]](../../distribuicao-chi-quadrado/propriedades/index.md#sum-of-independent-chi-squares)), temos que $W \sim Χ_{m + n - 2}^{2}$. Utilizando das propriedades que vimos no curso de Probabilidade, sabemos que $\overline{X} - \overline{Y}$ tem média $\mu_{X} - \mu_{Y} = 0$ e variância $\sigma^{2}/n + \sigma^{2}/m$, logo, segue que $Z \sim N(0,1)$

Um teste $t$ biamostral com nível de significância $\alpha_{0}$ é o procedimento $\delta$ que rejeita $H_{0}$ se $U \geq T_{m + n - 2}^{- 1}\left( 1 - \alpha_{0} \right)$. O próximo teorema estabelece algumas propriedades interessantes sobre a **função de poder** de testes $t$ biamostrais análogos aos do :

**Teorema: Nível e Viés de Testes $t$ biamostrais**

Seja $\delta$ um teste $t$ biamostral definido antes. A função de poder $\pi(\mu_{X},\mu_{Y},\sigma^{2}\vert \delta)$ tem as seguintes propriedades:

- $\pi(\mu_{X},\mu_{Y},\sigma^{2}\vert \delta) = \alpha_{0}$ quando $\mu_{X} = \mu_{Y}$

- $\pi(\mu_{X},\mu_{Y},\sigma^{2}\vert \delta) < \alpha_{0}$ quando $\mu_{X} < \mu_{Y}$

- $\pi(\mu_{X},\mu_{Y},\sigma^{2}\vert \delta) > \alpha_{0}$ quando $\mu_{X} > \mu_{Y}$

- $\pi(\mu_{X},\mu_{Y},\sigma^{2}\vert \delta) \rightarrow 0$ conforme $\mu_{X} - \mu_{Y} \rightarrow - \infty$

- $\pi(\mu_{X},\mu_{Y},\sigma^{2}\vert \delta) \rightarrow 1$ conforme $\mu_{X} - \mu_{Y} \rightarrow \infty$

além disso, o teste $\delta$ tem tamanho $\alpha_{0}$ e é não-viezado

Vale ressaltar que, se as hipóteses forem: $$H_{0}:\mu_{X} \geq \mu_{Y}\text{\quad\quad}H_{1}:\mu_{X} < \mu_{Y}$$<a id="two-sample-hypothesis-2"></a> o teste $\delta$ correspondente de tamanho $\alpha_{0}$ é **rejeitar $H_{0}$ quando $U \leq - T_{m + n - 2}^{- 1}\left( 1 - \alpha_{0} \right)$**. $P$-valores são computados de forma muito parecida da forma como se eles fossem de testes $t$ uniamostral

**Teorema: $p$-valores de testes $t$ biamostrais**

Suponha que estejamos testando as hipóteses da equação [\[two-sample-hypothesis-1\]](#two-sample-hypothesis-1) ou [\[two-sample-hypothesis-2\]](#two-sample-hypothesis-2). Seja $u$ o valor observado da estatística $U$ (equação [\[two-sample-u-statistic\]](#two-sample-u-statistic)) e seja $T_{m + n - 2}( \cdot )$ a cdf da distribuição $t$ com $m + n - 2$ graus de liberdade. Então o $p$-valor das hipóteses em [\[two-sample-hypothesis-1\]](#two-sample-hypothesis-1) é $1 - T_{m + n - 2}(u)$ e o $p$-valor das hipóteses em [\[two-sample-hypothesis-2\]](#two-sample-hypothesis-2) é $T_{m + n - 2}(u)$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Comparando as médias de duas Distribuições Normais](../index.md)
- Próximo: [Poder do Teste](../poder-do-teste/index.md)
