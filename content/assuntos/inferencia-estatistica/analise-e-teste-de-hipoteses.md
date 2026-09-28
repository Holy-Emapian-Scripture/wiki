---
layout: "default"
title: "Análise e Teste de Hipóteses"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 19
---

[Inferência Estatística](index.md)

<!-- wiki:original:inicio -->

<a id="secao-19"></a>

# Análise e Teste de Hipóteses


<a id="hipoteses-nula-e-alternativa"></a>
<a id="secao-20"></a>

## Hipóteses Nula e Alternativa

Nós temos $\theta \in \Omega$ e vamos particionar o espaço em dois conjuntos disjuntos $\Omega_{0}$ e $\Omega_{1}$ e queremos testar as duas hipóteses: $$H_{0}:\theta \in \Omega_{0}\text{\quad\quad}H_{1}:\theta \in \Omega_{1}$$

**Definição**

$H_{0}$ é chamada de **hipótese nula** e $H_{1}$ a **hipótese alternativa**. Se decidirmos que $\theta \in \Omega_{1}$, então nós **REJEITAMOS** $H_{0}$, se $\theta \in \Omega_{0}$, nós **NÃO REJEITAMOS** $H_{0}$

Ué, porque não falamos que **aceitamos** a hipótese $H_{0}$? Esse modo de visualizar o teste de hipóteses foi popularizado por Ronald Fisher, Jerzy Neyman e Egon Pearson. Essa visualização de assemelha muito ao sistema jurídico, onde seguimos o princípio da presunção de inocência:

- **Hipótese Nula $H_{0}$**: Representa o status quo, a crença estabelecida, o “nenhum efeito” ou a “igualdade”. É a hipótese que se presume verdadeira até que haja evidência [estatística suficiente](estatistica-suficiente.md) para o contrário. (Ex: “O réu é inocente”)

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

<a id="regiao-critica-e-testes-estatisticos"></a>
<a id="secao-21"></a>

## Região Crítica e Testes Estatísticos

Considere o problema de testar as hipóteses: $$H_{0}:\theta \in \Omega_{0}\text{\quad\quad}H_{1}:\theta \in \Omega_{1}$$ Seja $\underline{X} = \left\lbrack X_{1},\ldots,X_{n} \right\rbrack$ uma amostra indexada por $\theta$ desconhecido e $S$ o conjunto de **todas as saídas possíveis de** $\underline{X}$. Um estatístico pode especificar um procedimento de teste particionando $S$ em dois grupos, onde $S_{1}$ contém os valores de $\underline{X}$ onde $H_{0}$ será rejeitada e $S_{0}$ os valores que $H_{0}$ não é rejeitada

**Definição: Região Crítica**

O conjunto $S_{1}$ é chamado de **região crítica**

Na maioria dos problemas, $S_{1}$ é definido usando uma estatística $T = r\left( \underline{X} \right)$

**Definição: Estatística de Teste e Região de Rejeição**

Seja $T = r\left( \underline{X} \right)$ uma estatística e $R \subset {\mathbb{R}}$. Suponha que o procedimento de teste das hipóteses seja de forma “Rejeite $H_{0}$ se $T \in R$”, então $T$ é uma **estatística de teste** e $R$ é a **região de rejeição**

Se definirmos o teste em termos de $T$ e $R$ como na definição, então a região crítica é: $$S_{1} ≔ \left\{ \underline{x}\vert r\left( \underline{x} \right) \in R \right\}$$

**Exemplo**

Ainda na linha de raciocínio do exemplo da atividade física pro combate na depressão, vamos supor que definimos o procedimento $\delta$ como:

“Rejeite $H_{0}$ (Correr não afeta os sintomas da depressão) se o número de pessoas com os sintomas afetados for maior que um valor $c$”

Então podemos definir a estatística de teste como $\overline{X}$ e a região de rejeição é $R \subset {\mathbb{R}}$ com os valores reais maiores que $c$. Logo, a região crítica é dada por: $$S_{1} ≔ \left\{ \underline{x}\vert \overline{X} \in R \right\}$$

<a id="funcao-de-poder-e-tipos-de-erro"></a>
<a id="secao-22"></a>

## Função de Poder e Tipos de Erro

Seja $\delta$ um procedimento de teste como definimos antes

<a id="power-function"></a>

**Definição: Função de Poder**

A função $\pi(\theta\vert \delta)$ é chamada de **função de poder**. Se $S_{1}$ é a região crítica de $\delta$, então: $$\pi(\theta\vert \delta) = {\mathbb{P}}(\underline{X} \in S_{1}\vert \theta)\text{ ou }{\mathbb{P}}(T \in R\vert \theta)$$

Ou seja, é a probabilidade de que a minha amostra esteja na região crítica dado os meus parâmetros, ou seja, a probabilidade de que vou rejeitar $H_{0}$. A função de poder especial é aquela que: $$\begin{array}{r} \pi(\theta\vert \delta) = 0\text{\quad\quad}\forall\theta \in \Omega_{0} \\ \pi(\theta\vert \delta) = 1\text{\quad\quad}\forall\theta \in \Omega_{1} \end{array}$$

Lembrando: Para cada valor $\theta \in \Omega_{0}$, rejeitar $H_{0}$ é uma decisão **incorreta** e o mesmo para cada valor $\theta \in \Omega_{1}$ e não rejeitar $H_{0}$

**Definição: Tipos de Erro**

A decisão errônea de rejeitar uma hipótese nula **verdadeira** é de **Tipo I** (ou primeira ordem). Uma decisão errônea de **não rejeitar** uma hipótese nula **falsa** é chamada de **Tipo II** (ou segunda ordem)

|  | **Aceitar a hipótese nula** | **Rejeitar a hipótese nula** |
|----|----|----|
| **Hipótese nula é verdadeira** | ✅ | Erro de Tipo I |
| **Hipótese nula é falsa** | Erro de Tipo II | ✅ |

Se $\theta \in \Omega_{0}$, $\pi(\theta\vert \delta)$ é a probabilidade de cometermos um erro de Tipo I, já que ele representa a probabilidade de que a amostra esteja na região crítica (rejeitar $H_{0}$) e, se $\theta \in \Omega_{1}$, $1 - \pi(\theta\vert \delta)$ é a probabilidade de cometermos um erro de Tipo II. No geral, queremos achar $\delta$ tal que $\pi(\theta\vert \delta)$ seja baixo para $\theta \in \Omega_{0}$ e alto para $\theta \in \Omega_{1}$, já que isso representa diminuir a probabilidade de cometer cada um dos erros.

Um método muito usado é escolher $\alpha_{0} \in (0,1\rbrack$ tal que: $$\pi(\theta\vert \delta) \leq \alpha_{0}\text{\quad\quad}\forall\theta \in \Omega_{0}$$<a id="level"></a> e depois procurar o teste que **maximiza** $\pi(\theta\vert \delta)$ satisfazendo a condição (para $\theta \in \Omega_{1}$)

**Definição: Tamanho de um Teste**

Um teste que satisfaz a equação [nível do teste](#level) é chamado de **teste de nível $\alpha_{0}$** e que o teste tem nível de significância $\alpha_{0}$. O tamanho $\alpha(\delta)$ de um teste $\delta$ é definido por: $$\alpha(\delta) = \sup\limits_{\theta \in \Omega_{0}}\pi(\theta\vert \delta)$$

Ou seja, o tamanho de um teste é a maior probabilidade de cometermos um erro de **Tipo I** possível (já que fazemos o supremo dentre todos os valores de $\Omega_{0}$) e um teste ter nível de significância $\alpha_{0}$ significa que, independente de qual parâmetro de $H_{0}$ seja o verdadeiro da distribuição, a chance de cometermos um erro de **Tipo I** sempre será menor que $\alpha_{0}$

**Corolário**

Um teste $\delta$ é de nível $\alpha_{0} \Leftrightarrow \alpha(\delta) \leq \alpha_{0}$

Se a hipótese nula é simples ($H_{0}:\theta = \theta_{0}$), então $\alpha(\delta) = \pi(\theta_{0}\vert \delta)$

<a id="induzindo-um-nivel-de-significancia"></a>
<a id="secao-23"></a>

## Induzindo um nível de significância

Nós queremos testar: $$\begin{array}{r} H_{0}:\theta \in \Omega_{0} \\ H_{1}:\theta \in \Omega_{1} \end{array}$$

Seja $T$ uma estatística e suponha que vamos rejeitar $H_{0}$ se $T \geq c$. Vamos supor que queremos que nosso teste tenha um nível específico de significância $\alpha_{0}$. Temos: $$\pi(\theta\vert \delta) = {\mathbb{P}}(T \geq c\vert \theta)\underset{\text{ Queremos}}{\underbrace{\rightarrow}}\sup\limits_{\theta \in \Omega_{0}}{\mathbb{P}}(T \geq c\vert \theta) \leq \alpha_{0}$$

perceba que o lado direito é não-crescente em $c$, então a desigualdade é satisfeita para altos valores de $c$, então devemos fazer $c$ o menor possível sem que a desigualdade seja desfeita, e também queremos que $\pi(\theta\vert \delta)$ seja o maior possível para $\theta \in \Omega_{1}$. Quando $T$ tem distribuição contínua, costuma ser fácil achar um $c$ apropriado

<a id="secao-24"></a>

## p-valor

**Definição: p-valor**

O p-valor é o menor nível $\alpha_{0}$ ao qual rejeitaríamos a hipótese nula no nível $\alpha_{0}$ **com os dados observados**. Também chamamos o p-valor de **nível de significância observado**

É o que, macho? Essa definição está muito objetiva e densa, então simplificando um pouco: p-valor é a **probabilidade** de se obter o padrão de resultados que encontramos no nosso estudo ou resultados mais extremos, **considerando a hipótese nula como verdadeira**. Vamos supor que observamos uma amostra $\underline{x}$ e não fixamos um valor $\alpha$ para rejeitarmos $H_{0}$, então nos perguntamos “Qual é o menor nível para o qual esses dados ainda seriam considerados extremos o suficiente para rejeitar $H_{0}$?”. Então o $p$-valor segue uma linha diferente do procedimento de teste estabelecido anteriormente. Original:

- Escolhemos um nível $\alpha$

- Define-se a **região crítica** associada a esse $\alpha$

- Calcula-se a estatística de teste

- Verificamos se ela cai na região crítica

Agora nós invertemos a lógica

- Em vez de fixar um $\alpha$, vamos perguntar “rejeito ou não?”

- Fixamos os dados

- Para quais valores de $\alpha$ eu rejeitaria? O menor desses será meu $p$-valor

Mas por que essa definição é útil? Usamos isso pois, se eu faço um teste em um nível $\alpha_{0}$ e rejeito $H_{0}$, simplesmente dizer que rejeitei $H_{0}$ no nível $\alpha_{0}$ parece vago. Isso não diz o quão perto estávamos de tomar a outra decisão.

Um experimentador que rejeita a hipótese nula $\Leftrightarrow$ o p-valor é no máximo $\alpha_{0}$, está usando um teste de significância $\alpha_{0}$

<a id="secao-25"></a>

## Calculando p-valores

Se nossos testes são da forma “Rejeite $H_{0}$ quando $T \geq c$” para uma única estatística de teste, tem um jeito direto de calcular p-valores. Para cada $t$, deixe $\delta_{t}$ o teste que rejeita $H_{0}$ quando $T \geq t$. Então o p-valor quando $T = t$ é observado é o tamanho do teste $\delta_{t}$, ou seja, o p-valor é: $$\sup\limits_{\theta \in \Omega_{0}}\pi(\theta\vert \delta_{t}) = \sup\limits_{\theta \in \Omega_{0}}{\mathbb{P}}(T \geq t\vert \theta)$$

<a id="equivalencia-de-testes-e-conjuntos-de-confianca"></a>
<a id="secao-26"></a>

## Equivalência de testes e conjuntos de confiança

Os teoremas a seguir mostram a equivalência de intervalos e conjuntos de confiança (o nome é bem intuitivo). Intuitivamente, um [intervalo de confiança](intervalos-de-confianca.md) é um tipo específico de conjunto de confiança (com um tipo específico de regra)

**Teorema**

Seja $\underline{X} = \left\lbrack X_{1},\ldots,X_{n} \right\rbrack$ uma amostra de uma distribuição indexada por um parâmetro $\theta$. Seja $g(\theta)$ uma função e suponha que para todo possível valor $g_{0}$ de $g(\theta)$, existe um teste $\delta_{g_{0}}$ de nível $\alpha_{0}$ da hipótese $$\begin{array}{r} H_{0,g_{0}}:g(\theta) = g_{0} \\ H_{1,g_{0}}:g(\theta) \neq g_{0} \end{array}$$ Para cada possível valor de $\underline{x}$ de $\underline{X}$, defina: $$\omega(\underline{x}) = \left\{ g_{0}\vert \delta_{g_{0}}\text{ não rejeita }H_{0,g_{0}}\text{ se }\underline{X} = \underline{x}\text{ é visto} \right\}$$ e seja $\gamma = 1 - \alpha_{0}$, então o conjunto aleatório $w\left( \underline{X} \right)$ satisfaz $${\mathbb{P}}(g\left( \theta_{0} \right) \in \omega(\underline{X})\vert \theta = \theta_{0}) \geq \gamma\text{\quad\quad}\forall\theta_{0} \in \Omega$$

**Demonstração**

Seja $\theta_{0} \in \Omega$ um elemento arbitrário e defina $g_{0} = g\left( \theta_{0} \right)$. Como $\delta_{g_{0}}$ é um teste de nível $\alpha_{0}$, sabemos que: $${\mathbb{P}}(\delta_{g_{0}}\text{ não rejeitar }H_{0,g_{0}}\vert \theta = \theta_{0}) \geq 1 - \alpha_{0} = \gamma$$ Para cada $\underline{x}$, $g\left( \theta_{0} \right) \in \omega(\underline{x}) \Leftrightarrow$ o teste $\delta_{g_{0}}$ não rejeitar $H_{0,g_{0}}$ quando $\underline{X} = \underline{x}$ é visto $$\Rightarrow {\mathbb{P}}(g\left( \theta_{0} \right) \in \omega(\underline{X})\vert \theta = \theta_{0}) = A$$

**Definição: Conjunto de confiança**

Se um conjunto aleatório $\omega(\underline{X})$ satisfaz $${\mathbb{P}}(g\left( \theta_{0} \right) \in \omega(\underline{X})\vert \theta = \theta_{0}) \geq \gamma\text{\quad\quad}\forall\theta_{0} \in \Omega$$ então o chamamos de conjunto de confiança com coeficiente $\gamma$ para $g(\theta)$. Se a desigualdade for igualdade, o chamamos de exato

**Teorema**

Seja $X_{1},\ldots,X_{n}$ uma amostra aleatória de uma distribuição indexada por $\theta$ e $g:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ e seja $\omega(\underline{X})$ um conjunto de confiança $\gamma$ para $g(\theta)$. Para cada possível valor $g_{0}$ de $g(\theta)$, construa o teste $\delta_{g_{0}}$: $\delta_{g_{0}}$ não rejeita $H_{0,g_{0}} \Leftrightarrow g_{0} \in \omega(\underline{X})$. Então $\delta_{g_{0}}$ é um teste de nível $\alpha_{0} = 1 - \gamma$

<a id="testes-de-razao-de-verossimilhanca"></a>
<a id="secao-27"></a>

## Testes de razão de verossimilhança

Não vou explicar formalmente todos os pontos da teoria, mas dar uma ideia intuitiva. Como vimos nos Estimadores de [Máxima Verossimilhança](estatistica-frequentista.md#secao-14), quanto mais próximo do verdadeiro valor de $\theta$ a minha amostra estiver, maior será a verossimilhança. Então, intuitivamente, se a minha amostra tem uma verossimilhança muito maior para um valor de $\theta$ que pertence a $H_{1}$ do que para um valor de $\theta$ que pertence a $H_{0}$, isso é uma evidência contra $H_{0}$. O teste de razão de verossimilhança é justamente isso, ele rejeita $H_{0}$ quando a razão entre a máxima verossimilhança sob $H_{1}$ e a máxima verossimilhança sob $H_{0}$ é grande o suficiente. Como comentei antes, a gente tenta sempre achar evidências contra $H_{0}$ $$\begin{array}{r} H_{0}:\theta \in \Omega_{0} \\ H_{1}:\theta \in \Omega_{1} \end{array}$$

**Definição: Teste de razão de verossimilhança**

A estatística $$\Lambda(\underline{x}) = \frac{\sup\limits_{\theta \in \Omega_{0}}f_{n}\left( \underline{x}\vert \theta \right)}{\sup\limits_{\theta \in \Omega}f_{n}\left( \underline{x}\vert \theta \right)}$$ é chamada de **estatística de teste de razão de verossimilhança** e o teste que rejeita $H_{0}$ quando $\Lambda(\underline{X}) \leq k$ para alguma constante $k$ é chamado de **teste de razão de verossimilhança**

Botando em palavras simples, o teste de razão de verossimilhança rejeita $H_{0}$ quando a razão entre a máxima verossimilhança sob $\Omega_{0}$ e a máxima verossimilhança sob $\Omega$ é menor que um dado valor. Normalmente escolhemos $k$ de forma que o teste tenha nível de significância $\alpha_{0}$, quando possível

**Exemplo: Teste da Razão de Verossimilhança para Hipóteses Bilaterais sobre um Parâmetro de Bernoulli**

Suponha que observemos $Y$, o número de sucessos em $n$ ensaios de Bernoulli independentes com parâmetro desconhecido $\theta$. Considere as hipóteses $$H_{0}:\theta = \theta_{0}\text{\quad\quad}\text{ versus }\text{\quad\quad}H_{1}:\theta \notin \theta_{0.}$$

Após observar o valor $Y = y$, a função de verossimilhança é $$f\left( y\vert \theta \right) = \binom{n}{y}\theta^{y}(1 - \theta)^{n - y}.$$

Neste caso, o espaço paramétrico sob $H_{0}$ é $\Theta_{0} = \left\{ \theta_{0} \right\}$ e o espaço paramétrico completo é $\Theta = \lbrack 0,1\rbrack$. A estatística da razão de verossimilhança é

$$
\Lambda(y) = \frac{\theta_{0}^{y}\left( 1 - \theta_{0} \right)^{n - y}}{\sup\limits_{\theta \in \lbrack 0,1\rbrack}\theta^{y}(1 - \theta)^{n - y}}.
$$

O máximo do denominador ocorre quando $\theta$ é igual ao estimador de máxima verossimilhança (EMV), isto é, $$\hat{\theta} = \frac{y}{n}.$$

Assim, $$\Lambda(y) = \frac{\theta_{0}^{y}\left( 1 - \theta_{0} \right)^{n - y}}{\left( \frac{y}{n} \right)^{y}\left( 1 - \frac{y}{n} \right)^{n - y}} = \left( \frac{n\theta_{0}}{y} \right)^{y}\left( \frac{n\left( 1 - \theta_{0} \right)}{n - y} \right)^{n - y}$$

Não é difícil ver que $\Lambda(y)$ é pequeno para valores de $y$ próximos de $0$ ou de $n$, e é maior quando $y$ está próximo de $n\theta_{0}$.

Como exemplo específico, suponha que $n = 10$ e $\theta_{0} = 0.3$. A tabela abaixo apresenta os $11$ possíveis valores de $\Lambda(y)$ para $y = 0,\ldots,10$.

|  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|
| **y** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| **$\Lambda(y)$** | $0.028$ | $0.312$ | $0.773$ | $1.000$ | $0.797$ | $0.418$ | $0.147$ | $0.034$ | $0.005$ | $3 \times 10^{- 4}$ | $6 \times 10^{- 5}$ |
| **${\mathbb{P}}(Y = y\vert \theta = 0.3)$** | $0.028$ | $0.121$ | $0.233$ | $0.267$ | $0.200$ | $0.103$ | $0.037$ | $0.009$ | $0.001$ | $1 \times 10^{- 4}$ | $6 \times 10^{- 6}$ |

Se desejarmos um teste com nível de significância $\alpha_{0}$, ordenaríamos os valores de $y$ de acordo com os valores de $\Lambda(y)$, do menor para o maior, e escolheríamos $k$ de modo que a soma das probabilidades $${\mathbb{P}}(Y = y\vert \theta = 0.3)$$ correspondentes aos valores de $y$ tais que $\Lambda(y) \leq k$, fosse no máximo $\alpha_{0}$.

Por exemplo, se $\alpha_{0} = 0.05$, vemos na Tabela 9.1 que podemos somar as probabilidades correspondentes a $y = 10,9,8,7,0$, obtendo $0.039$. Entretanto, se incluirmos $y = 6$, correspondente ao próximo menor valor de $\Lambda(y)$, a soma salta para $0.076$, que é maior do que $0.05$.

O conjunto $$\left\{ 10,9,8,7,0 \right\}$$ corresponde a $\Lambda(y) \leq k$ para todo $k$ no intervalo semiaberto $\lbrack 0.028,0.147)$.

O tamanho do teste que rejeita $H_{0}$ quando $$y \in \left\{ 10,9,8,7,0 \right\}$$ é $0.039$

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Estimadores não-viezados](estimadores-nao-viezados.md)
- Próximo: [Testes $t$](testes-t.md)
