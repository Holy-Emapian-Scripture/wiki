---
title: "Estimação de Critérios de Informação"
tags:
  - series-temporais
  - a1
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/Recaps/A1.typ"
trilha: "../../trilhas/series-temporais/a1.md"
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 12
nav_exclude: true
render_with_liquid: false
---

[Séries Temporais](index.md)

<!-- wiki:original:inicio -->
<a id="scripture-secao-83"></a>

# Estimação de Critérios de Informação

<a id="scripture-secao-84"></a>

## Estimação por Máxima Verossimilhança

Agora precisamos estimar se nossos modelos **explicam bem os dados** sem serem complexos demais. Dado $p$, $d$, $q$, os parâmetros $\varphi$, $\theta$, $C$ e $\sigma^{2}$ saem por **máxima verossimilhança**.

Diferente do modelo $\text{AR}(p)$ puro (cuja regressão linear possui solução em forma fechada), os erros passados $\varepsilon_{t - 1},\ldots,\varepsilon_{t - q}$ de um modelo $\text{ARMA}(p,q)$ não são diretamente observáveis, tornando a equação de verossimilhança estritamente não-linear e exigindo otimização numérica.

<a id="scripture-secao-85"></a>

## Critérios de Informação

Para comparar modelos sob o mesmo nível $d$ e escolher qual deles (com $p$ e $q$ diferentes) se ajusta melhor aos dados, utilizamos **critérios de informação** que penalizam a complexidade do modelo (número de parâmetros) e recompensam o ajuste (log-verossimilhança).

Para comparar modelos candidatos ajustados em uma mesma amostra de $n$ observações, utilizamos da minimização do risco da perda de informação, medida pela divergência Kullback-Leibler entre o modelo estimado e o modelo verdadeiro. A divergência Kullback-Leibler é definida como:

$$
D_{\text{KL }}\left( g\| f \right) = {\mathbb{E}}_{\text{g }}\left\lbrack \log(g(y)) - \log(f\left( y\vert \theta \right)) \right\rbrack
$$

 o problema passa a se tratar da maximização da esperança da log verossimilhança sob o modelo verdadeiro $g(y)$:

$$
Q(\theta) = {\mathbb{E}}_{\text{g }}\left\lbrack \log(f\left( y\vert \theta \right)) \right\rbrack
$$

Existem alguns critérios de análise que podemos citar para comparar modelos candidatos, como o **Akaike Information Criterion (AIC)** e **Bayesian Information Criterion (BIC)**. Todos eles seguem a mesma lógica de penalizar a complexidade do modelo e recompensar o ajuste.

**Definição: Akaike Information Criterion (AIC)**

O AIC é definido como:

$$
\text{ AIC } = - 2\log(L) + 2k
$$

 onde $L$ é a função de verossimilhança do modelo estimado e $k$ é o número de parâmetros livres do modelo.

**Corolário: AIC para ARIMA**

Para o modelo $\text{ARIMA}(p,d,q)$, o AIC é dado por:

$$
\text{ AIC } = - 2\log(L) + 2(p + q + K + 1)
$$

 onde $K = 1$ se $C$ for estimado e $K = 0$ se $C$ for fixado em zero.

**Definição: AIC Corrigiro por Amostras Finitas**

O AICc é definido como:

$$
\text{ AICc } = \text{ AIC } + \frac{2k(k + 1)}{n - k - 1}
$$

 onde $n$ é o tamanho da amostra. Esse segundo termo é um termo de correção para amostras pequenas

**Corolário: AICc para ARIMA**

Para o modelo $\text{ARIMA}(p,d,q)$, o AICc é dado por:

$$
\text{ AICc } = \text{ AIC } + \frac{2(p + q + K + 1)(p + q + K + 2)}{n - (p + q + K + 1) - 1}
$$

 onde $K = 1$ se $C$ for estimado e $K = 0$ se $C$ for fixado em zero.

**Definição: Bayesian Information Criterium**

O BIC é definido como:

$$
\text{ BIC } = - 2\log(L) + k\log(n)
$$

 onde $L$ é a função de verossimilhança do modelo estimado, $k$ é o número de parâmetros livres do modelo e $n$ é o tamanho da amostra.

**Corolário: BIC para ARIMA**

Para o modelo $\text{ARIMA}(p,d,q)$, o BIC é dado por:

$$
\text{ BIC } = - 2\log(L) + (p + q + K + 1)\log(n)
$$

 onde $K = 1$ se $C$ for estimado e $K = 0$ se $C$ for fixado em zero.

O AICc é o critério primário para a escolha de $p$ e $q$ (sob o mesmo $d$), de forma que $\text{AICc } \approx \text{ AIC}$ para amostras muito grandes. O $\text{BIC}$ deve ser utilizado em contextos que ter muitos parâmetros é realmente muito indesejável (parcimônia extrema). Existe uma regra prática de que, se dois modelos apresentarem uma diferença de AICc menor que $2$, eles são considerados **equivalentes** em termos de ajuste, e a escolha entre eles pode ser feita com base em outros critérios, como interpretabilidade ou simplicidade.

<a id="scripture-secao-86"></a>

## Incomparabilidade de Modelos com Diferentes $d$

O AICc e o BIC são comparáveis apenas entre modelos com o mesmo nível de diferenciação $d$. Modelos com diferentes valores de $d$ não podem ser comparados diretamente

<a id="different-d-invalidity"></a>

**Teorema: Incomparabilidade de Modelos com Diferentes $d$**

Seja $Y = \left( y_{1},\ldots,Y_{T} \right)^{T}$ o vetor de observações da série temporal original ($d = 0$), e seja $Y^{\ast} = \left( \Delta y_{2},\ldots,\Delta y_{T} \right)^{T}$ o vetor da série diferenciada ($d = 1$). É matematicamente **inválido** comparar o AIC de um modelo ajustado com $d = 0$ com o AIC de um modelo ajustado com $d = 1$, pois os valores de log-verossimilhança derivam de funções de densidade de probabilidade integradas sobre espaços de medida de dimensões e escalas distintas.

**Demonstração**

Vamos definir uma transformação linear bijetora $A$ entre o vetor original $Y$ e o vetor $Y^{\ast}$ de tal forma que $Y^{\ast} = AY$. Sabendo que $\Delta y_{t} = y_{t} - y_{t - 1}$, temos que $A$ é definida como

$$
A = \begin{pmatrix} - 1 & 1 & 0 & \ldots & 0 \\ 0 & - 1 & 1 & \ldots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \ldots & - 1 & 1 \end{pmatrix}
$$

No entanto, perceba que $A \in {\mathbb{R}}^{T - 1 \times T}$, representando uma transformação **não** bijetiva, pois o determinante **não é definido**. Como o determinante não se aplica aqui, não podemos expressar a verossimilhança de $Y$ em termos da verossimilhança de $Y^{\ast}$, e vice-versa. Portanto, os modelos com diferentes níveis de diferenciação $d$ não podem ser comparados diretamente em termos de AIC ou BIC por representarem funções de densidade de probabilidade em espaços de medida (em termos mais intuitivos, sistemas de coordenadas) distintos, tornando a comparação inválida.

<a id="scripture-secao-87"></a>

## Teste KPSS para Determinação de $d$

Assim como existem métodos para escolher $p$ e $q$ a partir de um $d$ fixo, existem métodos para escolher $d$ a partir da série original. A escolha de $d$ é crucial, pois ela determina se a série será estacionária ou não, e isso afeta diretamente a validade das inferências feitas a partir do modelo.

O método mais básico para determinar o valor de $d$ é o teste KPSS (Kwiatkowski-Phillips-Schmidt-Shin), que testa a hipótese nula de estacionariedade contra a alternativa de uma raiz unitária. Se o teste rejeitar a hipótese nula, isso sugere que a série não é estacionária e que uma diferenciação adicional pode ser necessária.

$$
\begin{array}{r} H_{0}:\text{ A série é estacionária } \\ H_{1}:\text{ A série possui uma raiz unitária (não estacionária) } \end{array}
$$

<a id="scripture-secao-88"></a>

### A Premissa

Esse teste se baseia na premissa que uma série temporal pode ser decomposta em $2$ componentes: uma tendência estocástica e um componente de ruído fracamente estacionário.

$$
\begin{array}{r} y_{t} = r_{t} + \varepsilon_{t} \\ r_{t} = r_{t - 1} + u_{t} \\ u_{t} \sim \text{ IID}\left( 0,\sigma_{u}^{2} \right) \end{array}
$$

a estacionariedade da série depende então da **variância de $u_{t}$**. Se $\sigma_{u}^{2} = 0$, a série é estacionária, caso contrário, a série possui uma raiz unitária e não é estacionária. Então as hipóteses podem ser reformuladas como

$$
\begin{array}{r} H_{0}:\sigma_{u}^{2} = 0 \\ H_{1}:\sigma_{u}^{2} > 0 \end{array}
$$

<a id="scripture-secao-89"></a>

### Estatística do Teste

Sob $H_{0}$, a média da série é **constante** e os valores oscilam em torno dela, então estima-se os resíduos da regressão:

$$
e_{t} = y_{t} - \overline{y}
$$

Definimos então $S_{t}$ como a **soma acumulada dos resíduos**:

$$
S_{t} = \sum_{i = 1}^{t}e_{i}
$$

agora vamos analisar como ela se comporta em ambos os cenários de hipóteses. Se a série for estacionária, a soma acumulada $S_{t}$ vai oscilar em torno de zero. Por outro lado, se a série não for estacionária, $S_{t}$ vai crescer mais rapidamente, refletindo a presença de uma tendência estocástica.

Para avaliar o comportamento global da série, pegamos o valor da soma acumulada $S_{t}$ em cada dia $t$, elevamos ao quadrado (para eliminar os sinais negativos) e somamos tudo:

$$
\sum_{t = 1}^{T}S_{t}^{2} = S_{1}^{2} + S_{2}^{2} + S_{3}^{2} + \ldots + S_{T}^{2}
$$

Se a série for estacionária: Como cada $S_{t}$ é pequeno, o somatório $\sum S_{t}^{2}$ resulta em um número PEQUENO.Se a série for não-estacionária: Como os $S_{t}$ são gigantescos, o somatório $\sum S_{t}^{2}$ resulta em um número ENORME.

Não podemos usar a soma bruta $\sum S_{t}^{2}$ diretamente porque ela sofre de dois problemas:

1.  Depende do tamanho do banco de dados ($T$): Quanto mais dados você tem, mais termos você está somando).

2.  Depende da escala dos dados: Se a série for medida em milhões de Reais vs. em gramas, a soma muda de tamanho.

Para resolver isso, dividimos por dois fatores de correção:

1.  Dividimos por $T^{2}$: Sob a hipótese de estacionariedade ($H_{0}$), a teoria provou estatisticamente que o crescimento da soma $\sum S_{t}^{2}$ em relação ao tamanho da amostra é proporcional a $T^{2}$. Dividir por $T^{2}$ faz com que a estatística não mude se você tiver $100$ ou $10.000$ dados.

2.  Dividimos pela Variância de Longo Prazo (${\hat{\sigma}}^{2}$: Dividimos pela variância dos resíduos $e_{t}$ para “cancelar” a unidade de medida dos dados, deixando o teste puramente adimensional

E no final, obtemos a estatística de teste

$$
\text{ KPSS } = \frac{1}{T^{2}{\hat{\sigma}}^{2}}\sum_{t = 1}^{T}S_{t}^{2}
$$

Essa estatística não possui uma distribuição padrão com forma analítica para o cálculo dos p-valores, então os valores críticos são obtidos por simulação Monte Carlo. A tabela de valores críticos do teste KPSS é amplamente disponível na literatura estatística e em pacotes de software, mas o padrão é que, para um nível de significância de 5%, o valor crítico é aproximadamente $0.463$. Se a estatística KPSS calculada for maior que esse valor crítico, rejeitamos a hipótese nula de estacionariedade. Como não há estacionariedade, **diferenciamos a série** e **aplicamos o teste novamente** até que a hipótese nula não seja rejeitada, determinando assim o valor apropriado de $d$ para o modelo ARIMA.

<a id="scripture-secao-90"></a>

## Algoritmo de Busca Automática

Especificado todos esses métodos de testagem de parâmetros, podemos sumarizar um algoritmo para encontrar um modelo ARIMA que modele bem os dados mantendo o princípio da parcimônia:

**Algoritmo de Busca Automática de Modelos ARIMA**

1.  **function** *automatic_search* (y) {

    1.  Aplico KPSS até não rejeitar a hipótese nula $H_{0}$

    2.  Defino $d$ como o número de diferenciações aplicadas

    3.  Crio modelos candidatos $\text{ARIMA}$ iniciais com os parâmetros

        1.  $(0,d,0),(1,d,0),(0,d,1),(2,d,2)$

    4.  Escolho o modelo com menor AICc

    5.  **while** (AICc do modelo atual \< AICc do modelo anterior) {

        1.  Crio modelos candidatos $\text{ARIMA}$ vizinhos com os parâmetros

            1.  $(p - 1,d,q),(p + 1,d,q),(p,d,q - 1),(p,d,q + 1)$

        2.  Escolho o modelo com menor AICc

        3.  Repito ou até convergir ou até ficar satisfeito

    6.  }

2.  }
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Modelo ARIMA](modelo-arima.md)

- Próximo: [SARIMA](sarima.md)
