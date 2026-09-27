---
layout: "default"
title: "Propriedades dos testes $t$ — Testes $t$"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 30
---

[Inferência Estatística](../../index.md) · [Testes $t$](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-30"></a>

# Propriedades dos testes $t$

**Teorema: Nível e Viés dos testes $t$**

Seja $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ uma amostra aleatória de uma distribuição normal $X \sim N\left( \mu,\sigma^{2} \right)$ e $U$ ser a estatística definida anteriormente. Seja também $c$ o $1 - \alpha_{0}$ quantil da distribuição $t$ com $n - 1$ graus de liberdade. Seja $\delta$ o procedimento que rejeita $H_{0}$ na equação [\[t-test-mu-hypothesis-1\]](../testando-hipoteses-sobre-a-media-de-uma-normal-quando-a-variancia-e-desconhecida/index.md#t-test-mu-hypothesis-1) se $U \geq c$. A função de poder $\pi(\mu,\sigma^{2}\vert \delta)$ tem as seguintes propriedades:

1.  $\pi(\mu,\sigma^{2}\vert \delta) = \alpha_{0}$ quando $\mu = \mu_{0}$

2.  $\pi(\mu,\sigma^{2}\vert \delta) < \alpha_{0}$ quando $\mu < \mu_{0}$

3.  $\pi(\mu,\sigma^{2}\vert \delta) > \alpha_{0}$ quando $\mu > \mu_{0}$

4.  $\pi(\mu,\sigma^{2}\vert \delta) \rightarrow 0$ conforme $\mu \rightarrow - \infty$

5.  $\pi(\mu,\sigma^{2}\vert \delta) \rightarrow 1$ conforme $\mu \rightarrow \infty$

Além disso, o teste $\delta$ tem tamanho $\alpha_{0}$ e é não-viezado

**Demonstração**

Se $\mu = \mu_{0}$, então $U \sim t_{n - 1}$, portanto: $$\pi(\mu_{0},\sigma^{2}\vert \delta) = {\mathbb{P}}(U \geq c\vert \mu_{0},\sigma^{2}) = \alpha_{0}$$ lembrando que a função de poder, quando $\theta \in \Omega_{0}$ é a probabilidade de rejeitarmos $H_{0}$ (Erro de **Tipo I**), então vai ser a probabilidade de $U \geq c$. Isso prova (i)

Para provar (ii) e (iii), defina: $$U^{\ast} = \sqrt{n} \cdot \frac{{\overline{X}}_{n} - \mu}{\sigma}'\text{\quad\quad}W = \frac{\sqrt{n}(\mu_{0} - \mu)}{\sigma}'$$ Logo, $U = U^{\ast} - W$. Primeiramente, assuma que $\mu < \mu_{0}$, então $W > 0$, então segue que: $$\begin{aligned} \pi(\mu,\sigma^{2}\vert \delta) & = {\mathbb{P}}(U \geq c\vert \mu,\sigma^{2}) = {\mathbb{P}}(U^{\ast} - W\vert \mu,\sigma^{2}) \\ & = {\mathbb{P}}(U^{\ast} \geq c + W\vert \mu,\sigma^{2}) < {\mathbb{P}}(U^{\ast} \geq c\vert \mu,\sigma^{2}) \end{aligned}$$ Como $U^{\ast}$ tem distribuição $t_{n - 1}$, a última probabilidade da equação é igual a $\alpha_{0}$. Isso prova (ii). Para provar (iii), basta assumir que $\mu > \mu_{0}$, logo $W < 0$, então o sinal de **menor que** no final da equação vira um **maior que**. A prova de (iv) e (v) são mais complicadas e não serão abordadas

**Corolário**

Seja $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ uma amostra aleatória de uma distribuição normal $X \sim N\left( \mu,\sigma^{2} \right)$ e $U$ ser a estatística definida anteriormente. Seja também $c$ o $1 - \alpha_{0}$ quantil da distribuição $t$ com $n - 1$ graus de liberdade. Seja $\delta$ o procedimento que rejeita $H_{0}$ na equação [\[t-test-mu-hypothesis-2\]](../testando-hipoteses-sobre-a-media-de-uma-normal-quando-a-variancia-e-desconhecida/index.md#t-test-mu-hypothesis-2) se $U \leq c$. A função de poder $\pi(\mu,\sigma^{2}\vert \delta)$ tem as seguintes propriedades:

1.  $\pi(\mu,\sigma^{2}\vert \delta) = \alpha_{0}$ quando $\mu = \mu_{0}$

2.  $\pi(\mu,\sigma^{2}\vert \delta) > \alpha_{0}$ quando $\mu < \mu_{0}$

3.  $\pi(\mu,\sigma^{2}\vert \delta) < \alpha_{0}$ quando $\mu > \mu_{0}$

4.  $\pi(\mu,\sigma^{2}\vert \delta) \rightarrow 1$ conforme $\mu \rightarrow - \infty$

5.  $\pi(\mu,\sigma^{2}\vert \delta) \rightarrow 0$ conforme $\mu \rightarrow \infty$

Além disso, o teste $\delta$ tem tamanho $\alpha_{0}$ e é não-viezado

**Exemplo**

Para o [\[hospital-example-t-test\]](../index.md#hospital-example-t-test), se quiséssemos um teste de nível de significância $\alpha_{0} = 0.1$, então pelas propriedades, rejeitariamos $H_{0}$ se $U \leq c$ onde $c = T_{n - 1}^{- 1}(0.1)$.

Calcular $p$-valores para os testes $t$ é bem direto ao ponto!

**Teorema: $p$-valores para testes $t$**

Suponha que estamos testando ou as hipóteses da equação [\[t-test-mu-hypothesis-1\]](../testando-hipoteses-sobre-a-media-de-uma-normal-quando-a-variancia-e-desconhecida/index.md#t-test-mu-hypothesis-1) ou da [\[t-test-mu-hypothesis-2\]](../testando-hipoteses-sobre-a-media-de-uma-normal-quando-a-variancia-e-desconhecida/index.md#t-test-mu-hypothesis-2). Seja $u$ o valor observado da estatística $U$ e $T_{n - 1}( \cdot )$ a cdf da distribuição $t_{n - 1}$. Então o $p$-valor para as hipóteses da equação [\[t-test-mu-hypothesis-1\]](../testando-hipoteses-sobre-a-media-de-uma-normal-quando-a-variancia-e-desconhecida/index.md#t-test-mu-hypothesis-1) é $1 - T_{n - 1}(u)$ e para as hipóteses da equação [\[t-test-mu-hypothesis-2\]](../testando-hipoteses-sobre-a-media-de-uma-normal-quando-a-variancia-e-desconhecida/index.md#t-test-mu-hypothesis-2) é $T_{n - 1}(u)$

**Demonstração**

Seja $T_{n - 1}^{- 1}( \cdot )$ a função quantil da $t_{n - 1}$. Nós rejeitaríamos a hipótese na equação [\[t-test-mu-hypothesis-1\]](../testando-hipoteses-sobre-a-media-de-uma-normal-quando-a-variancia-e-desconhecida/index.md#t-test-mu-hypothesis-1) em um nível $\alpha_{0}$ se, e somente se $u \geq T_{n - 1}^{- 1}\left( 1 - \alpha_{0} \right)$, que é equivalente a $\alpha_{0} \geq 1 - T_{n - 1}(u)$. Similarmente, rejeitamos as hipóteses da equação [\[t-test-mu-hypothesis-2\]](../testando-hipoteses-sobre-a-media-de-uma-normal-quando-a-variancia-e-desconhecida/index.md#t-test-mu-hypothesis-2) se, e somente se $u \leq T_{n - 1}^{- 1}\left( \alpha_{0} \right)$, que é equivalente a $\alpha_{0} \geq T_{n - 1}(u)$

<a id="length-fibers-example"></a>

**Exemplo: Tamanho de Fibras**

Suponha que os comprimentos, em milímetros, de fibras metálicas produzidas por um determinado processo tenham distribuição normal, com média desconhecida ( $\mu$ ) e variância desconhecida ( $\sigma^{2}$ ), e que as seguintes hipóteses devam ser testadas: $$H_{0}:\mu \leq 5.2\text{\quad\quad}H_{1}:\mu > 5.2$$

Suponha que os comprimentos de 15 fibras selecionadas aleatoriamente sejam medidos e que se observe que a média amostral ( ${\overline{X}}_{15}$ ) é $5.4$ e que ( $\sigma' = 0.4226$ ). Com base nessas medições, realizaremos um teste **$t$** ao nível de significância ( $\alpha_{0} = 0.05$ ).

Como ( $n = 15$ ) e ( $\mu_{0} = 5.2$ ), a estatística ( $U$ ) terá distribuição **$t$** com $14$ graus de liberdade quando ( $\mu = 5.2$ ). Verifica-se na tabela da distribuição **$t$** que $$T_{14}^{- 1}(0.95) = 1.761.$$ Assim, a hipótese nula ( $H_{0}$ ) será rejeitada se ( $U > 1.761$ ). Como o valor numérico de ( $U$ ) é 1,833, a hipótese nula ( $H_{0}$ ) seria rejeitada ao nível de $0.05$.

Com o valor observado ( $u = 1.833$ ) para a estatística ( $U$ ) e ( $n = 15$ ), podemos calcular o **p-valor** para as hipóteses utilizando um software computacional que inclua a função de distribuição acumulada das várias distribuições **$t$**. Em particular, obtemos $$1 - T_{14}(1.833) = 0.0441.$$

Legal, mas será que conseguimos dizer algo sobre a **função poder** de um teste $t$? Se conseguirmos determinar a distribuição de $U$, nós conseguimos sim!

**Definição: Distribuição $t$ não-central**

Seja $Y$ e $W$ variáveis aleatórias independentes onde $W \sim N(\psi,1)$ e $Y \sim Χ_{m}^{2}$, então a distribuição de: $$X = \frac{W}{\left( \frac{Y}{m} \right)^{1/2}}$$ é chamada de **distribuição $t$ não-central com $m$ graus de liberdade e parâmetro de não-centralidade $\psi$**. Chamaremos a sua cdf de $T_{m}\left( t\vert \psi \right)$ ($T_{m}\left( t\vert \psi \right) = {\mathbb{P}} \ast (X \leq t)$)

**Teorema**

Seja $X_{1},\ldots,X_{n}$ uma amostra aleatória de uma distribuição normal com média $\mu$ e variância $\sigma^{2}$. A distribuição da estatística $U$ é dada por uma distribuição $t$ não-central com $n - 1$ graus de liberdade e parâmetro de não-centralidade $\psi = \sqrt{n}(\mu - \mu_{0})/\sigma$. Seja $\delta$ o teste que rejeita $H_{0}:\mu \leq \mu_{0}$ quando $U \geq c$. Então a função de poder de $\delta$ é $\pi(\mu,\sigma^{2}\vert \delta) = 1 - T_{n - 1}\left( c\vert \psi \right)$. Seja $\delta'$ o teste que rejeita $H_{0}:\mu \geq \mu_{0}$ quando $U \leq c$, então a função de poder de $\delta'$ é $\pi(\mu,\sigma^{2}\vert \delta') = T_{n - 1}\left( c\vert \psi \right)$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Testando Hipóteses sobre a Média de uma Normal quando a Variância é Desconhecida](../testando-hipoteses-sobre-a-media-de-uma-normal-quando-a-variancia-e-desconhecida/index.md)
- Próximo: [Teste $t$ pareado](../teste-t-pareado/index.md)
