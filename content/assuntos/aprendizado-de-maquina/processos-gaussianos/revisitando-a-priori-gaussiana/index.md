---
layout: "default"
title: "Revisitando a priori Gaussiana — Processos Gaussianos"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 10
---

[Aprendizado de Máquina](../../index.md) · [Processos Gaussianos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-10"></a>

# Revisitando a priori Gaussiana

Como discutimos anteriormente, prioris gaussianas são extremamente populares em modelos Bayesianos para regressão. Uma escolha comum, por exemplo, é colocar uma priori isotrópica $N(0,cI)$ sobre o vetor de pesos $\theta$. Nesse caso, a priori sobre $\theta$ também induz implicitamente uma priori sobre $f(X') = X'\theta$ para qualquer $X' \in {\mathbb{R}}^{N' \times (D + 1)}$ e $N' \in {\mathbb{N}}^{+}$. Mais especificamente, como $f(X')$ é uma transformação linear de variáveis Gaussianas, essa priori é Gaussiana com vetor de médias $\mu(X')$ e matriz de covariância $\Sigma(X',X')$ dados por: $$\begin{aligned} \mu(X') & = {\mathbb{E}}_{\theta}\lbrack X'\theta\rbrack = X'{\mathbb{E}}_{\theta}\lbrack\theta\rbrack = 0 \\ \Sigma(X',X') & = {\mathbb{E}}_{\theta}\left\lbrack (X'\theta - 0)(X'\theta - 0)^{T} \right\rbrack = cX'X'^{T} \end{aligned}$$

Com essas observações em mente, podemos abstrair $\theta$ totalmente do nosso processo de aprendizado usando a seguinte priori sobre os valores de $f$: $$f(X') \sim N\left( 0,\Sigma(X',X') \right)\ \forall X' \in {\mathbb{R}}^{N' \times (D + 1)},\ N' \in {\mathbb{N}}^{+}$$<a id="priori-gp"></a> que é uma instância específica de um processo estocástico conhecido como **processo Gaussiano** (Gaussian process, GP). De forma geral, $\left( f(x) \right)_{x \in \mathcal{X}}$ define um processo Gaussiano se qualquer vetor $\left\lbrack f\left( x_{1} \right),\ldots,f\left( x_{N} \right) \right\rbrack^{T}$ com $x_{1},\ldots,x_{N} \in \mathcal{X}$ segue uma distribuição normal multivariada.

**Definição: Processo Gaussiano**

Seja $\mathcal{X}$ um espaço de entradas. Dizemos que $\left( f(x) \right)_{x \in \mathcal{X}}$ é um processo Gaussiano se, para qualquer conjunto finito de pontos $x_{1},\ldots,x_{N} \in \mathcal{X}$, o vetor $\mathbf{f} = \left\lbrack f\left( x_{1} \right),\ldots,f\left( x_{N} \right) \right\rbrack^{T}$ segue uma distribuição normal multivariada.

É importante ressaltar que a matriz de covariância $\Sigma(X',X')$ é proporcional à matriz Gramiana $K$ (de produtos internos) dos vetores linha de $X'$, i.e., $K_{ij} = x'_{i} \cdot x'_{j}$, onde $x'_{i}$ e $x'_{j}$ denotam os vetores nas linhas $i$ e $j$ de $X'$, respectivamente. Além disso, incorporar uma função de expansão de base $\Phi$ no modelo da Equação [\[priori-gp\]](#priori-gp) apenas implica em redefinir as entradas de $K$ como $K_{ij} = k\left( x'_{i},x'_{j} \right) = \Phi(x'_{i}) \cdot \Phi(x'_{j})$. Em outras palavras, nosso GP sobre $f$ pode ser completamente caracterizado por uma função de produto interno generalizada $k$ — também conhecida como **função de kernel**. Por simplicidade notacional, denotaremos que $f$ segue uma priori de GP como $f \sim \text{ GP}(0,k)$. Nesse capítulo, assumiremos que a média de $f$ é zero a priori; no entanto, seria possível utilizar uma função de média arbitrária $\mu( \cdot )$ com poucas alterações nos nossos desenvolvimentos.

Do ponto de vista de interpretação, funções de kernel nos permitem diretamente expressar como regularidades no espaço de entrada devem ser refletidas no espaço de saída. Além disso, existem casos em que $\Phi$ é computacionalmente intratável, mas seu kernel correspondente tem forma simples. Por exemplo, o kernel exponencial quadrático (ou Gaussiano), dado por $k(x,x') = \exp\left\{ - \| x - x'\frac{\|_{2}^{2}}{2\gamma^{2}} \right\}$ é gerado a partir de uma expansão de base “infinita” — veja a Seção 4.2 do livro texto de [Rasmussen e Williams (2006)](https://gaussianprocess.org/gpml/chapters/RW.pdf) para mais detalhes.

<a id="secao-11"></a>

## Funções de kernel comuns

Na literatura de GPs, existe uma variedade de funções de kernel criadas para modelar fenômenos distintos. No entanto, alguns kernels são extremamente populares, como:

1.  **Exponencial quadrático** (ou Gaussiano):

$$k(x,x') = e^{- \| x - x'\frac{\|_{2}^{2}}{2\gamma^{2}}}$$ onde $\gamma^{2}$ é um hiperparâmetro que controla a suavidade da função de kernel;

2.  **Racional quadrático**:

$$k(x,x') = \sigma^{2}\left( 1 + \frac{\| x - x'\|_{2}^{2}}{2\alpha\gamma^{2}} \right)^{- \alpha}$$ que corresponde a uma soma ponderada de kernels exponenciais quadráticos com diferentes larguras de banda;

3.  **Periódico**:

$$k(x,x') = e^{- 2\gamma^{- 2}\sin^{2}\left( \pi\| x - x'\frac{\|_{2}}{p} \right)}$$ que tem natureza periódica, com período $p$.

<a id="secao-12"></a>

## Construindo funções de kernel

A família das funções de kernel é fechada por um número de operações. Isto é, é possível manipular um kernel $k$ de várias maneiras diferentes e ainda assim obter um kernel válido. Isso é extremamente útil em cenários em que precisamos, e.g., combinar propriedades de diferentes funções de kernel para refletir um fenômeno. Por exemplo, as seguintes operações resultam em kernels válidos:

1.  Multiplicação por constante $c > 0$: $k'(x,x') = ck(x,x')$;

2.  Produto: $k'(x,x') = k_{1}(x,x')k_{2}(x,x')$;

3.  Soma: $k'(x,x') = k_{1}(x,x') + k_{2}(x,x')$;

4.  Exponenciação: $k'(x,x') = e^{k_{1}(x,x')}$;

5.  Multiplicação por função escalar avaliada em $x$ e $x'$: $k'(x,x') = f(x)f(x')k(x,x')$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Processos Gaussianos](../index.md)
- Próximo: [GPs para regressão](../gps-para-regressao/index.md)
