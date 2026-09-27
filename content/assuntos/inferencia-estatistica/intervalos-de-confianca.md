---
layout: "default"
title: "Intervalos de Confiança"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 8
---

[Inferência Estatística](index.md)

<!-- wiki:original:inicio -->

<a id="secao-8"></a>

# Intervalos de Confiança


<a id="intervalo-de-confianca-para-a-media-de-uma-normal"></a>
<a id="secao-9"></a>

## Intervalo de Confiança para a média de uma Normal

Dada a amostra $X_{1},\ldots,X_{n} \sim N\left( \mu,\sigma^{2} \right)$, sabemos que $U = \sqrt{n}(\overline{X} - \mu)/\sigma' \sim t_{n - 1}$. Eu gostaria de achar um intervalo no qual eu tenho uma chance boa de encontrar minha média, então eu gostaria de algo do tipo: $${\mathbb{P}}( - c < U < c) = \gamma$$<a id="normal-mean-conficence-interval"></a> O método mais comum é calcular diretamente o $c$ que torna a equação [\[normal-mean-conficence-interval\]](#normal-mean-conficence-interval) verdadeira. Isso é equivalente a dizer: $${\mathbb{P}}({\overline{X}}_{n} - \frac{c\sigma'}{\sqrt{n}} < \mu < {\overline{X}}_{n} + \frac{c\sigma'}{\sqrt{n}}) = \gamma$$ Vale ressaltar que essa probabilidade é referente a distribuição conjunta de ${\overline{X}}_{n}$ e $\sigma'$ para valores **fixos** de $\mu$ e $\sigma$ (Independentemente de sabermos eles ou não). Então vamos tentar achar o $c$ que satisfaz isso $${\mathbb{P}}( - c < U < c) = \gamma \Leftrightarrow T_{n - 1}(c) - T_{n - 1}( - c) = \gamma$$ Pela simetria de $t$ em $0$, posso reescrever como: $$2T_{n - 1}(c) - 1 = \gamma \Rightarrow c = T_{n - 1}^{- 1}\left( \frac{1 + \gamma}{2} \right)$$ Então, depois que descobrimos $c$, nosso intervalo de confiança vira: $$\begin{array}{r} A = {\overline{X}}_{n} - \sigma\frac{'}{\sqrt{n}}\ T_{n - 1}^{- 1}\left( \frac{1 + \gamma}{2} \right) \\ B = {\overline{X}}_{n} + \sigma\frac{'}{\sqrt{n}}\ T_{n - 1}^{- 1}\left( \frac{1 + \gamma}{2} \right) \end{array}$$

Dada essa noção inicial, vamos definir formalmente esses intervalos:

**Definição: Intervalo de confiança**

Seja $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ uma amostra de uma distribuição indexada pelo(s) parâmetro(s) $\theta$ e seja $g(\theta):\Omega \rightarrow {\mathbb{R}}$. Seja também $A$ e $B$ duas estatísticas $(A \leq B)$ que satisfazem: $${\mathbb{P}}(A < g(\theta) < B) \geq \gamma$$<a id="confidence-interval-property"></a> O intervalo aleatório $(A,B)$ é chamado de intervalo de confiança $\gamma$ para $g(\theta)$ ou de intervalo de confiança $100\gamma\%$ para $g(\theta)$. Depois que $X_{1},\ldots,X_{n}$ foi observado e o intervalo $A = a$ e $B = b$ foi computado, chamamos o valor observado do intervalo de **valor observado do intervalo de confiança**. Se a equação [\[confidence-interval-property\]](#confidence-interval-property) vale a igualdade $\forall c \in (A,B)$, então chamamos esse intervalo de **exato**

Aqui eu vou definir melhor a interpretação com relação a essa definição, que pode ser um pouco confusa. A interpretação do intervalo $A,B$ em si é bem direta, representa um intervalo **aleatório** que tem probabilidade $\gamma$ de conter $g(\theta)$. Porém, ao observamos as amostras e calcularmos $A = a$ e $B = b$, o intervalo $(a,b)$ **não necessariamente contém $g(\theta)$ com probabilidade $\gamma$**, como assim? Lembra que $(A,B)$ é um intervalo **aleatório**, enquanto $(a,b)$ é uma das muitas possíveis ocorrências desse intervalo! A interpretação correta é, que quanto mais repetimos o experimento e computamos $(a,b)$ e armazenamos esses valores observados de intervalo, uma fração $\gamma$ deles contém $g(\theta)$, porém, **não sabemos dizer quais contém e quais não contém**

**Teorema**

Dada a amostra $X_{1},\ldots,X_{n} \sim N\left( \mu,\sigma^{2} \right)$. $\forall\gamma \in \lbrack 0,1\rbrack$, o intervalo $(A,B)$ com seguintes pontos: $$\begin{array}{r} A = {\overline{X}}_{n} - \sigma\frac{'}{\sqrt{n}}\ T_{n - 1}^{- 1}\left( \frac{1 + \gamma}{2} \right) \\ B = {\overline{X}}_{n} + \sigma\frac{'}{\sqrt{n}}\ T_{n - 1}^{- 1}\left( \frac{1 + \gamma}{2} \right) \end{array}$$ é um intervalo de confiança $\gamma$-exato

<a id="intervalos-de-confianca-unilaterais"></a>
<a id="secao-10"></a>

## Intervalos de Confiança Unilaterais

Nós vimos como encontrar intervalos aleatórios $(A,B)$ que tem probabilidade $\gamma$ de conter o parâmetro $\theta$, porém, podem acontecer situações que apenas obter um limite superior ou inferior seja suficiente para nós

Dados $\gamma_{1}$ e $\gamma_{2}$ com $\gamma_{2} > \gamma_{1}$ e $\gamma_{2} - \gamma_{1} = \gamma$, então: $${\mathbb{P}}(T_{n - 1}^{- 1}\left( \gamma_{1} \right) < U < T_{n - 1}^{- 1}\left( \gamma_{1} \right)) = \gamma$$ E então obtemos que, perante todos os intervalos aleatórios possíveis, o intervalo de confiança $\gamma$ com o menor tamanho é o simétrico $$\gamma_{1} = 1 - \gamma_{2}$$ Porém, há casos que um intervalo não-simétrico é útil (Como mencionei o caso anterior de apenas limites superiores ou intefiores)

**Definição: Intervalo de Confiança Generalizado**

Seja $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ uma amostra de uma distribuição parametrizada por $\theta$. Seja $g(\theta):\Omega \rightarrow {\mathbb{R}}$ e seja $A$ uma estatística tal que: $${\mathbb{P}}(A < g(\theta)) \geq \gamma\text{\quad\quad}\forall\theta$$ Então o intervalo aleatório $(A, + \infty)$ é chamado de intervalo de confiança unilateral $\gamma$ de limite inferior $A$. A mesma definição vale para a estatística $B$ tal que: $${\mathbb{P}}(g(\theta) < B) \geq \gamma$$ Então o intervalo aleatório $( - \infty,B)$ é chamado de intervalo de confiança unilateral $\gamma$ de limite superior $B$. Se a desigualdade “$\geq \gamma$” é uma igualdade para todo $\theta$, então tanto o intervalo quanto os limites são chamados de exatos

**Teorema: Intervalo unilateral da média da normal**

Seja $X_{1},\ldots,X_{n} \sim N\left( \mu,\sigma^{2} \right)$, as estatísticas a seguir são, respectivamente, limites inferior e superior exatos com coeficiente $\gamma$ para $\mu$: $$\begin{array}{r} A = {\overline{X}}_{n} - T_{n - 1}^{- 1}(\gamma)\sigma\frac{'}{\sqrt{n}} \\ B = {\overline{X}}_{n} + T_{n - 1}^{- 1}(\gamma)\sigma\frac{'}{\sqrt{n}} \end{array}$$

<a id="intervalo-de-confianca-para-outros-parametros"></a>
<a id="secao-11"></a>

## Intervalo de confiança para outros parâmetros

Até agora, só vimos a aplicação de intervalos de confiança para a [distribuição normal](../probabilidade/distribuicoes-continuas.md#secao_dist_normal), mas por quê? Pois a normal possui propriedades que tornam encontrar os intervalos de confiança mais fáceis, como por exemplo, encontrarmos estatísticas (Por exemplo $T = \sqrt{n}({\overline{X}}_{n} - \mu)/\sigma'$) que não dependem do parâmetro que queremos estimar, e isso na verdade é uma definição útil que pode nos ajudar:

**Definição: Pivô**

Seja $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ uma amostra de uma distribuição parametrizada por $\theta$ e $V\left( \theta,\underline{X} \right)$ uma variável aleatória tal que sua distribuição **não depende de $\theta$** e é a mesma $\forall\theta$, então chamamos $V\left( \theta,\underline{X} \right)$ de **quantidade pivotal** ou **pivô**

Podemos então utilizar dessa definição para construir intervalos de confiança. Porém, para isso, precisamos de uma “função inversa” desse $V$, algo do tipo: $$r\left( V\left( \theta,\underline{X} \right),\underline{X} \right) = g(\theta)$$<a id="v-pseudo-inverse"></a>

**Teorema**

Seja $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ uma amostra de uma distribuição parametrizada por $\theta$. Suponha que existe um pivô $V$. Seja $F_{V}(v)$ a CDF de $V$ e contínua. Assuma também que a função $r$ tal qual a equação [\[v-pseudo-inverse\]](#v-pseudo-inverse) existe e é estritamente crescente em $v$ para cada $\underline{x}$. Seja $\gamma \in (0,1)$ e $\gamma_{2} > \gamma_{1}$ tal que $\gamma_{2} - \gamma_{1} = \gamma$, então as seguintes estatísticas são endpoints de um invervalo de confiança $\gamma$-exato para $g(\theta)$ $$\begin{array}{r} A = r\left( F_{V}^{- 1}\left( \gamma_{1} \right),\underline{x} \right) \\ B = r\left( F_{V}^{- 1}\left( \gamma_{2} \right),\underline{x} \right) \end{array}$$ Se $r$ é estritamente decrescente, então invertemos $A$ e $B$

**Demonstração**

Se $r\left( \theta,\underline{x} \right)$ é estritamente crescente em $v$ para todo $\underline{x}$, então: $$V\left( \theta,\underline{X} \right) < c \Leftrightarrow g(\theta) < r\left( c,\underline{X} \right)$$ Defina $c = F_{V}^{- 1}\left( \gamma_{i} \right)$ para $i = 1,2$, então obtemos: $$\begin{array}{r} {\mathbb{P}}(g(\theta) < A) = \gamma_{1} \\ {\mathbb{P}}(g(\theta) < B) = \gamma_{2} \end{array}$$<a id="intervals-pivots"></a> Como $V$ tem distribuição contínua e $r$ é estritamente crescente, então: $${\mathbb{P}}(A = g(\theta)) = {\mathbb{P}}(V\left( \theta,\underline{X} \right) = F_{V}^{- 1}\left( \gamma_{1} \right)) = 0$$ Similarmente com ${\mathbb{P}}(B = g(\theta))$, então combinamos as duas equações na equação [\[intervals-pivots\]](#intervals-pivots) para obter ${\mathbb{P}}(A < g(\theta) < B) = \gamma$

**Exemplo**

Seja $X_{1},\ldots,X_{n}$ uma amostra aleatória de uma distribuição normal com média $\mu$ e variância $\sigma^{2}$ desconhecidos. Vimos anteriormente que: $$V\left( \theta,\underline{X} \right) = \frac{1}{\sigma^{2}}\sum_{i = 1}^{n}\left( X_{i} - {\overline{X}}_{n} \right)^{2} \sim Χ_{n - 1}^{2}\text{\quad\quad}\forall\theta = \left( \mu,\sigma^{2} \right)$$ Logo, $V$ é um pivô, de forma que conseguimos utilizá-lo para achar intervalos de confiança para $\sigma^{2}$

Porém é bem comum que o pivô não exista em casos discretos

**Exemplo**

Seja $\theta$ a proporção de sucessos em uma população muito grande de pacientes tratados com imipramina. Suponha que os clínicos desejem uma variável aleatória $A$ tal que, para todo $\theta$, tenhamos $$\Pr(A < \theta) \geq 0.9$$

Isto é, eles querem ter **$90\%$ de confiança** de que a proporção de sucesso seja **pelo menos $A$**. Os dados observáveis consistem no número $X$ de sucessos em uma amostra aleatória de **$n = 40$** pacientes. Nenhuma variável pivotal existe neste exemplo, e os intervalos de confiança são mais difíceis de construir

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Distribuições $t$](distribuicoes-t.md)
- Próximo: [Análise Bayesiana de Amostras Normais](analise-bayesiana-de-amostras-normais.md)
