---
layout: "default"
title: "Testes $t$"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 28
---

[Inferência Estatística](index.md)

<!-- wiki:original:inicio -->

<a id="secao-28"></a>

# Testes $t$

Nesse capítulo, vamos abordar um caso específico de teste de hipóteses para distribuições normais com média e variância desconhecida

<a id="hospital-example-t-test"></a>

**Exemplo**

Um instituto médico quer saber a distribuição de quantos dias um paciente internado em UTI’s de hospitais permanece internado. Foram coletadas informações de $n = 30$ hospitais por todo o estado. Vamos supor que modelamos a quantidade de dias que a pessoa se mantém internada como uma variável normal com média $\mu$ e variância $\sigma^{2}$. Vamos dizer também que queremos testar as hipóteses: $$H_{0}:\mu \geq 200\text{\quad\quad}H_{1}:\mu < 200$$ que teste seria apropriado de se utilizar? Quais são suas propriedades?



<a id="testando-hipoteses-sobre-a-media-de-uma-normal-quando-a-variancia-e-desconhecida"></a>
<a id="secao-29"></a>

## Testando Hipóteses sobre a Média de uma Normal quando a Variância é Desconhecida

Consideremos $X_{1},\ldots,X_{n}$ uma amostra de uma [distribuição normal](../probabilidade/distribuicoes-continuas.md#secao_dist_normal) com média $\mu$ e variância $\sigma^{2}$ desconhecidas, e também que trabalhamos com as hipóteses: $$\begin{array}{r} H_{0}:\mu \leq \mu_{0} \\ H_{1}:\mu > \mu_{0} \end{array}$$<a id="t-test-mu-hypothesis-1"></a>

O espaço paramétrico $\Omega$ suprime todo vetor bidimensiona $\left( \mu,\sigma^{2} \right)$ com $\mu \in ( - \infty,\infty)$ e $\sigma^{2} > 0$. Aqui, definimos a estatística de teste $U$ como: $$U = \sqrt{n} \cdot \frac{{\overline{X}}_{n} - \mu_{0}}{\sigma}'$$<a id="u-statistic"></a> onde o teste rejeita $H_{0}$ se $U \geq c$. Sabemos que a distribuição de $U$ é uma $t$ com $n - 1$ graus de liberdade, por isso os testes que utilizam de $U$ são chamados de **testes $t$**. Quando invertemos as hipóteses: $$\begin{array}{r} H_{0}:\mu \geq \mu_{0} \\ H_{1}:\mu < \mu_{0} \end{array}$$<a id="t-test-mu-hypothesis-2"></a> o teste vira da forma “rejeite $H_{0}$ quando $U \leq c$”

**Exemplo**

No [exemplo dos hospitais](#hospital-example-t-test), se a gente quisesse um teste de tamanho $\alpha_{0}$, a gente poderia usar o teste $t$ que rejeita $H_{0}$ se a estatística $U$ for menor ou igual a um $c$ (escolhemos $c$ de forma a fazer o teste ter tamanho $\alpha_{0}$)

<a id="secao-30"></a>

## Propriedades dos testes $t$

**Teorema: Nível e Viés dos testes $t$**

Seja $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ uma amostra aleatória de uma distribuição normal $X \sim N\left( \mu,\sigma^{2} \right)$ e $U$ ser a estatística definida anteriormente. Seja também $c$ o $1 - \alpha_{0}$ quantil da distribuição $t$ com $n - 1$ graus de liberdade. Seja $\delta$ o procedimento que rejeita $H_{0}$ na [formulação unilateral à direita do teste $t$](#t-test-mu-hypothesis-1) se $U \geq c$. A função de poder $\pi(\mu,\sigma^{2}\vert \delta)$ tem as seguintes propriedades:

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

Seja $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ uma amostra aleatória de uma distribuição normal $X \sim N\left( \mu,\sigma^{2} \right)$ e $U$ ser a estatística definida anteriormente. Seja também $c$ o $1 - \alpha_{0}$ quantil da distribuição $t$ com $n - 1$ graus de liberdade. Seja $\delta$ o procedimento que rejeita $H_{0}$ na [formulação unilateral à esquerda do teste $t$](#t-test-mu-hypothesis-2) se $U \leq c$. A função de poder $\pi(\mu,\sigma^{2}\vert \delta)$ tem as seguintes propriedades:

1.  $\pi(\mu,\sigma^{2}\vert \delta) = \alpha_{0}$ quando $\mu = \mu_{0}$

2.  $\pi(\mu,\sigma^{2}\vert \delta) > \alpha_{0}$ quando $\mu < \mu_{0}$

3.  $\pi(\mu,\sigma^{2}\vert \delta) < \alpha_{0}$ quando $\mu > \mu_{0}$

4.  $\pi(\mu,\sigma^{2}\vert \delta) \rightarrow 1$ conforme $\mu \rightarrow - \infty$

5.  $\pi(\mu,\sigma^{2}\vert \delta) \rightarrow 0$ conforme $\mu \rightarrow \infty$

Além disso, o teste $\delta$ tem tamanho $\alpha_{0}$ e é não-viezado

**Exemplo**

Para o [exemplo dos hospitais](#hospital-example-t-test), se quiséssemos um teste de nível de significância $\alpha_{0} = 0.1$, então pelas propriedades, rejeitariamos $H_{0}$ se $U \leq c$ onde $c = T_{n - 1}^{- 1}(0.1)$.

Calcular $p$-valores para os testes $t$ é bem direto ao ponto!

**Teorema: $p$-valores para testes $t$**

Suponha que estamos testando ou as hipóteses da [formulação unilateral à direita do teste $t$](#t-test-mu-hypothesis-1) ou da [formulação unilateral à esquerda do teste $t$](#t-test-mu-hypothesis-2). Seja $u$ o valor observado da estatística $U$ e $T_{n - 1}( \cdot )$ a cdf da distribuição $t_{n - 1}$. Então o $p$-valor para as hipóteses da [formulação unilateral à direita do teste $t$](#t-test-mu-hypothesis-1) é $1 - T_{n - 1}(u)$ e para as hipóteses da [formulação unilateral à esquerda do teste $t$](#t-test-mu-hypothesis-2) é $T_{n - 1}(u)$

**Demonstração**

Seja $T_{n - 1}^{- 1}( \cdot )$ a função quantil da $t_{n - 1}$. Nós rejeitaríamos a hipótese na [formulação unilateral à direita do teste $t$](#t-test-mu-hypothesis-1) em um nível $\alpha_{0}$ se, e somente se $u \geq T_{n - 1}^{- 1}\left( 1 - \alpha_{0} \right)$, que é equivalente a $\alpha_{0} \geq 1 - T_{n - 1}(u)$. Similarmente, rejeitamos as hipóteses da [formulação unilateral à esquerda do teste $t$](#t-test-mu-hypothesis-2) se, e somente se $u \leq T_{n - 1}^{- 1}\left( \alpha_{0} \right)$, que é equivalente a $\alpha_{0} \geq T_{n - 1}(u)$

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

<a id="secao-31"></a>

## Teste $t$ pareado

Em vários experimentos, podemos desejar comparar a mesma variável em condições distintas na mesma amostra, então estaríamos interessados em comparar qual condição possui maior média. Nesses casos é comum fazer a subtração entre os valores de cada condição e tratar como uma variável aleatória normal

**Exemplo:**

O **National Transportation Safety Board** coleta dados de testes de colisão referentes à quantidade e à localização dos danos em bonecos (**dummies**) colocados nos carros testados. Em uma série de testes, um boneco foi colocado no banco do motorista e outro no banco do passageiro dianteiro de cada carro. Uma das variáveis medidas foi o grau de lesão na cabeça de cada boneco. Entre outros aspectos, há interesse em saber se, e/ou em que medida, a quantidade de lesão na cabeça difere entre o banco do motorista e o banco do passageiro.

Sejam $\left( X_{1},\ldots,X_{n} \right)$ as diferenças entre os logaritmos das medidas de lesão na cabeça do lado do motorista e do lado do passageiro. Podemos modelar $\left( X_{1},\ldots,X_{n} \right)$ como uma amostra aleatória de uma distribuição normal com média ( $\mu$ ) e variância ( $\sigma^{2}$ ). Suponha que desejamos testar a hipótese nula ( $H_{0}:\mu \leq 0$ ) contra a alternativa ( $H_{1}:\mu > 0$ ), ao nível de significância ( $\alpha_{0} = 0.01$ ).

Há $n = 164$ carros. O teste consiste em rejeitar ( $H_{0}$ ) se $$U \geq T_{163}^{- 1}(0.99) = 2.35.$$

A média das diferenças é ${\overline{x}}_{n} = 0.2199$. O valor de $\sigma'$ é $0.5342$. A estatística $U$ é então igual a $5.271$. Esse valor é maior que $2.35$, e a hipótese nula seria rejeitada ao nível de $0.01$. De fato, o **p-valor** é menor que $1.0 \cdot 10^{- 6}$.

Suponha também que estamos interessados na função poder sob $H_{1}$ do teste de nível $0.01$. Suponha que a diferença média entre os logaritmos das lesões na cabeça do lado do motorista e do lado do passageiro seja $\frac{\sigma}{4}$. Então, o parâmetro de não centralidade é $\frac{(164)^{\frac{1}{2}}}{4} = 3.20$

<a id="secao-32"></a>

## Testando uma alternativa bilateral

**Exemplo**

Vamos retomar o [exemplo do comprimento das fibras](#length-fibers-example), mas agora vamos alterar as hipóteses para: $$H_{0}:\mu = 5.2,\text{\quad\quad}H_{1}:\mu \neq 5.2$$

Assumiremos novamente que os comprimentos de 15 fibras são medidos, e que o valor de $U$, calculado a partir dos valores observados, é 1,833. Testaremos as hipóteses ao nível de significância $\alpha_{0} = 0.05$.

Como $\alpha_{0} = 0.05$, nosso valor crítico será o quantil $1 - \frac{0.05}{2} = 0.975$ da distribuição **$t$** com $14$graus de liberdade. Pela tabela das distribuições **$t$** deste livro, encontramos $$T_{14}^{- 1}(0.975) = 2.145.$$

Assim, o teste **t** especifica a rejeição de $H_{0}$ se $U \leq - 2.145$ ou se $U \geq 2.145$. Como $U = 1.833$, a hipótese $H_{0}$ **não** seria rejeitada.

Os valores numéricos nos exemplos enfatizam a importância de decidir se a hipótese alternativa apropriada em um dado problema é unilateral (**one-sided**) ou bilateral (**two-sided**). Quando as hipóteses do [exemplo do comprimento das fibras](#length-fibers-example) foram testadas ao nível de significância $0.05$, a hipótese nula $H_{0}$, de que $\mu \leq 5.2$, foi rejeitada. Quando as hipóteses desse exemplo foram testadas ao mesmo nível de significância, utilizando os mesmos dados, a hipótese nula $H_{0}$, de que $\mu = 5.2$, não foi rejeitada.

**Teorema: Função de poder de testes $t$ bilaterais**

A função de [poder do teste](comparando-as-medias-de-duas-distribuicoes-normais.md#secao-36) $\delta$ que rejeita $H_{0}:\mu = \mu_{0}$ quando $\vert U\vert  \geq c$, onde $c = T_{n - 1}^{- 1}\left( 1 - \alpha_{0}/2 \right)$ pode ser encontrada utilizando a distribuição $t$ não-central. Se $\mu \neq \mu_{0}$, então $U$ tem distribuição $t$ não-central com $n - 1$ graus de liberdade e parâmetro de não-centralidade $\psi = \sqrt{n}(\mu - \mu_{0})/\sigma$. A função de poder é: $$\pi(\mu,\sigma^{2}\vert \delta) = T_{n - 1}\left( - c\vert \psi \right) + 1 - T_{n - 1}\left( c\vert \psi \right)$$

**Teorema: $p$-valores de testes $t$ bilaterais**

Suponha que estamos testando as hipóteses bilaterais $H_{0}:\mu = \mu_{0}$, $H_{1}:\mu \neq \mu_{0}$. Seja $u$ o valor observado da estatística $U$ e seja $T_{n - 1}( \cdot )$ a cdf de uma $t_{n - 1}$. Então o $p$-valor é $2\left\lbrack 1 - T_{n - 1}\left( \vert u\vert  \right) \right\rbrack$

**Demonstração**

Deixe $T_{n - 1}^{- 1}( \cdot )$ denotar a função quantil da $t_{n - 1}$. Nós rejeitariamos a hipótese nula no nível $\alpha_{0}$ se, e somente se, $\vert u\vert  \geq T_{n - 1}^{- 1}\left( 1 - \alpha_{0}/2 \right)$ que é equivalente a $T_{n - 1}\left( \vert u\vert  \right) \geq 1 - \alpha_{0}/2$ que é equivalente a $\alpha_{0} \geq 2\left\lbrack 1 - T_{n - 1}\left( \vert u\vert  \right) \right\rbrack$

<a id="testes-t-como-testes-de-razao-de-verossimilhanca"></a>
<a id="secao-33"></a>

## Testes $t$ como testes de razão de verossimilhança

**Exemplo: Teste da Razão de Verossimilhança para Hipóteses Unilaterais sobre a Média de uma Distribuição Normal**

Considere as hipóteses unilaterais sobre a média de uma distribuição normal: $$H_{0}:\mu \leq \mu_{0}\text{\quad\quad}H_{1}:\mu > \mu_{0}$$

Neste caso, $\Omega_{0} = \left\{ \left( \mu,\sigma^{2} \right):\mu \leq \mu_{0} \right\}$ e $\Omega_{1} = \left\{ \left( \mu,\sigma^{2} \right):\mu > \mu_{0} \right\}$. A função de verossimilhança é: $$f_{n}\left( \underline{x}\vert \mu,\sigma^{2} \right) = \frac{1}{\left( 2\pi\sigma^{2} \right)^{\frac{n}{2}}}\exp\left\lbrack - \frac{1}{2\sigma^{2}}\sum_{i = 1}^{n}\left( x_{i} - \mu \right)^{2} \right\rbrack$$

Após observar os valores $x_{1},\ldots,x_{n}$, a estatística de teste de razão de verossimilhança é: $$\Lambda(x) = \frac{\sup\limits_{\left\{ \left( \mu,\sigma^{2} \right) \in \Omega_{0} \right\}}f_{n}\left( \underline{x}\vert \mu,\sigma^{2} \right)}{\sup\limits_{\left\{ \left( \mu,\sigma^{2} \right) \in \Omega \right\}}f_{n}\left( \underline{x}\vert \mu,\sigma^{2} \right)}$$

Chamemos ${\hat{\mu}}_{0}$ e ${\hat{\sigma}}_{0}^{2}$ os EMVs de $\mu$ e $\sigma^{2}$ sob $H_{0}$, e $\hat{\mu}$ e ${\hat{\sigma}}^{2}$ os EMVs de $\mu$ e $\sigma^{2}$ sob o espaço paramétrico completo.

Suponha primeiro que os valores amostrais observados são tais que ${\overline{x}}_{n} \leq \mu_{0}$. Então temos que $\left( \hat{\mu},{\hat{\sigma}}^{2} \right) \in \Omega_{0}$, se isso acontecer, então temos que ${\hat{\mu}}_{0} = \hat{\mu}$ e ${\hat{\sigma}}_{0}^{2} = {\hat{\sigma}}^{2}$, por tanto, nesse cenário, $\Lambda(\underline{x})$ é igual a $1$.

Agora, suponha que os valores amostrais observados são tais que ${\overline{x}}_{n} > \mu_{0}$, logo, $\left( \hat{\mu},{\hat{\sigma}}^{2} \right) \notin \Omega_{0}$. Nesse cenário, é possível demonstrar que $f_{n}\left( \underline{x}\vert \mu,\sigma^{2} \right)$ atinge seu valor máximo entre os pontos $\left( \mu,\sigma^{2} \right) \in \Omega_{0}$ se escolhermos $\mu$ o mais próximo possível de ${\overline{x}}_{n}$. O valor de $\mu$ mais próximo de ${\overline{x}}_{n}$ é $\mu_{0}$, pois $\mu_{0}$ é o valor máximo possível de $\mu$ sob $H_{0}$, por isso ${\hat{\mu}}_{0} = \mu_{0}$. Logo, podemos mostrar que: $${\hat{\sigma}}_{0}^{2} = \frac{1}{n}\sum_{i = 1}^{n}\left( x_{i} - \mu_{0} \right)^{2}$$ nesse cenário, o valor do numerador de $\Lambda(\underline{x})$ é: $$\sup\limits_{\left\{ \left( \mu,\sigma^{2} \right)\vert \mu > \mu_{0} \right\}}f_{n}\left( \underline{x}\vert \mu,\sigma^{2} \right) = \frac{1}{\left( 2\pi{\hat{\sigma}}^{2} \right)^{n/2}}\exp( - \frac{n}{2})$$

Tirando a razão em ambos os casos mencionados anteriormente, temos que: $$\Lambda(\underline{x}) = \begin{cases} \left( \frac{{\hat{\sigma}}^{2}}{{\hat{\sigma}}_{0}^{2}} \right)^{n/2} \rightarrow {\overline{x}}_{n} > \mu_{0} \\ 1 \rightarrow \text{ do contrário } \end{cases}$$

Agora, usamos seguinte relação: $$\sum_{i = 1}^{n}\left( x_{i} - \mu_{0} \right)^{2} = \sum_{i = 1}^{n}\left( x_{i} - {\overline{x}}_{n} \right)^{2} + {n\left( {\overline{x}}_{n} - \mu_{0} \right)}^{2}$$ para reescrever a parte de cima da estatística $\Lambda(\underline{x})$ como: $$\left\lbrack 1 + \frac{{n\left( {\overline{x}}_{n} - \mu_{0} \right)}^{2}}{\sum_{i = 1}^{n}\left( x_{i} - {\overline{x}}_{n} \right)^{2}} \right\rbrack^{- n/2}$$

Se $u$ é o valor observado da estatística $U$ ([equação da estatística $U$](#u-statistic)), então podemos checar que: $$\frac{{n\left( {\overline{x}}_{n} - \mu_{0} \right)}^{2}}{\sum_{i = 1}^{n}\left( x_{i} - {\overline{x}}_{n} \right)^{2}} = \frac{u^{2}}{n - 1}$$

Ou seja, segue que $\Lambda(\underline{x})$ é uma função **não-crescente** de $u$. Por isso, para $k < 1$, $\Lambda(\underline{x}) \leq k \Leftrightarrow u \geq c$ onde: $$c = \sqrt{(n - 1) \cdot \left( \left( \frac{1}{k} \right)^{2/n} - 1 \right)}$$ Segue então que o teste de razão de verossimilhança é um teste $t$

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Análise e Teste de Hipóteses](analise-e-teste-de-hipoteses.md)
- Próximo: [Comparando as médias de duas Distribuições Normais](comparando-as-medias-de-duas-distribuicoes-normais.md)
