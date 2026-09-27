---
layout: "default"
title: "Testes de razão de verossimilhança — Análise e Teste de Hipóteses"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 27
---

[Inferência Estatística](../../index.md) · [Análise e Teste de Hipóteses](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-27"></a>

# Testes de razão de verossimilhança

Não vou explicar formalmente todos os pontos da teoria, mas dar uma ideia intuitiva. Como vimos nos Estimadores de Máxima Verossimilhança, quanto mais próximo do verdadeiro valor de $\theta$ a minha amostra estiver, maior será a verossimilhança. Então, intuitivamente, se a minha amostra tem uma verossimilhança muito maior para um valor de $\theta$ que pertence a $H_{1}$ do que para um valor de $\theta$ que pertence a $H_{0}$, isso é uma evidência contra $H_{0}$. O teste de razão de verossimilhança é justamente isso, ele rejeita $H_{0}$ quando a razão entre a máxima verossimilhança sob $H_{1}$ e a máxima verossimilhança sob $H_{0}$ é grande o suficiente. Como comentei antes, a gente tenta sempre achar evidências contra $H_{0}$ $$\begin{array}{r} H_{0}:\theta \in \Omega_{0} \\ H_{1}:\theta \in \Omega_{1} \end{array}$$

**Definição: Teste de razão de verossimilhança**

A estatística $$\Lambda(\underline{x}) = \frac{\sup\limits_{\theta \in \Omega_{0}}f_{n}\left( \underline{x}\vert \theta \right)}{\sup\limits_{\theta \in \Omega}f_{n}\left( \underline{x}\vert \theta \right)}$$ é chamada de **estatística de teste de razão de verossimilhança** e o teste que rejeita $H_{0}$ quando $\Lambda(\underline{X}) \leq k$ para alguma constante $k$ é chamado de **teste de razão de verossimilhança**

Botando em palavras simples, o teste de razão de verossimilhança rejeita $H_{0}$ quando a razão entre a máxima verossimilhança sob $\Omega_{0}$ e a máxima verossimilhança sob $\Omega$ é menor que um dado valor. Normalmente escolhemos $k$ de forma que o teste tenha nível de significância $\alpha_{0}$, quando possível

**Exemplo: Teste da Razão de Verossimilhança para Hipóteses Bilaterais sobre um Parâmetro de Bernoulli**

Suponha que observemos $Y$, o número de sucessos em $n$ ensaios de Bernoulli independentes com parâmetro desconhecido $\theta$. Considere as hipóteses $$H_{0}:\theta = \theta_{0}\text{\quad\quad}\text{ versus }\text{\quad\quad}H_{1}:\theta \notin \theta_{0.}$$

Após observar o valor $Y = y$, a função de verossimilhança é $$f\left( y\vert \theta \right) = \binom{n}{y}\theta^{y}(1 - \theta)^{n - y}.$$

Neste caso, o espaço paramétrico sob $H_{0}$ é $\Theta_{0} = \left\{ \theta_{0} \right\}$ e o espaço paramétrico completo é $\Theta = \lbrack 0,1\rbrack$. A estatística da razão de verossimilhança é

$$\Lambda(y) = \frac{\theta_{0}^{y}\left( 1 - \theta_{0} \right)^{n - y}}{\sup\limits_{\theta \in \lbrack 0,1\rbrack}\theta^{y}(1 - \theta)^{n - y}}.$$

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

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Equivalência de testes e conjuntos de confiança](../equivalencia-de-testes-e-conjuntos-de-confianca/index.md)
- Próximo: [Testes $t$](../../testes-t/index.md)
