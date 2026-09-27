---
layout: "default"
title: "Testes $t$ como testes de razão de verossimilhança — Testes $t$"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 33
---

[Inferência Estatística](../../index.md) · [Testes $t$](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-33"></a>

# Testes $t$ como testes de razão de verossimilhança

**Exemplo: Teste da Razão de Verossimilhança para Hipóteses Unilaterais sobre a Média de uma Distribuição Normal**

Considere as hipóteses unilaterais sobre a média de uma distribuição normal: $$H_{0}:\mu \leq \mu_{0}\text{\quad\quad}H_{1}:\mu > \mu_{0}$$

Neste caso, $\Omega_{0} = \left\{ \left( \mu,\sigma^{2} \right):\mu \leq \mu_{0} \right\}$ e $\Omega_{1} = \left\{ \left( \mu,\sigma^{2} \right):\mu > \mu_{0} \right\}$. A função de verossimilhança é: $$f_{n}\left( \underline{x}\vert \mu,\sigma^{2} \right) = \frac{1}{\left( 2\pi\sigma^{2} \right)^{\frac{n}{2}}}\exp\left\lbrack - \frac{1}{2\sigma^{2}}\sum_{i = 1}^{n}\left( x_{i} - \mu \right)^{2} \right\rbrack$$

Após observar os valores $x_{1},\ldots,x_{n}$, a estatística de teste de razão de verossimilhança é: $$\Lambda(x) = \frac{\sup\limits_{\left\{ \left( \mu,\sigma^{2} \right) \in \Omega_{0} \right\}}f_{n}\left( \underline{x}\vert \mu,\sigma^{2} \right)}{\sup\limits_{\left\{ \left( \mu,\sigma^{2} \right) \in \Omega \right\}}f_{n}\left( \underline{x}\vert \mu,\sigma^{2} \right)}$$

Chamemos ${\hat{\mu}}_{0}$ e ${\hat{\sigma}}_{0}^{2}$ os EMVs de $\mu$ e $\sigma^{2}$ sob $H_{0}$, e $\hat{\mu}$ e ${\hat{\sigma}}^{2}$ os EMVs de $\mu$ e $\sigma^{2}$ sob o espaço paramétrico completo.

Suponha primeiro que os valores amostrais observados são tais que ${\overline{x}}_{n} \leq \mu_{0}$. Então temos que $\left( \hat{\mu},{\hat{\sigma}}^{2} \right) \in \Omega_{0}$, se isso acontecer, então temos que ${\hat{\mu}}_{0} = \hat{\mu}$ e ${\hat{\sigma}}_{0}^{2} = {\hat{\sigma}}^{2}$, por tanto, nesse cenário, $\Lambda(\underline{x})$ é igual a $1$.

Agora, suponha que os valores amostrais observados são tais que ${\overline{x}}_{n} > \mu_{0}$, logo, $\left( \hat{\mu},{\hat{\sigma}}^{2} \right) \notin \Omega_{0}$. Nesse cenário, é possível demonstrar que $f_{n}\left( \underline{x}\vert \mu,\sigma^{2} \right)$ atinge seu valor máximo entre os pontos $\left( \mu,\sigma^{2} \right) \in \Omega_{0}$ se escolhermos $\mu$ o mais próximo possível de ${\overline{x}}_{n}$. O valor de $\mu$ mais próximo de ${\overline{x}}_{n}$ é $\mu_{0}$, pois $\mu_{0}$ é o valor máximo possível de $\mu$ sob $H_{0}$, por isso ${\hat{\mu}}_{0} = \mu_{0}$. Logo, podemos mostrar que: $${\hat{\sigma}}_{0}^{2} = \frac{1}{n}\sum_{i = 1}^{n}\left( x_{i} - \mu_{0} \right)^{2}$$ nesse cenário, o valor do numerador de $\Lambda(\underline{x})$ é: $$\sup\limits_{\left\{ \left( \mu,\sigma^{2} \right)\vert \mu > \mu_{0} \right\}}f_{n}\left( \underline{x}\vert \mu,\sigma^{2} \right) = \frac{1}{\left( 2\pi{\hat{\sigma}}^{2} \right)^{n/2}}\exp( - \frac{n}{2})$$

Tirando a razão em ambos os casos mencionados anteriormente, temos que: $$\Lambda(\underline{x}) = \begin{cases} \left( \frac{{\hat{\sigma}}^{2}}{{\hat{\sigma}}_{0}^{2}} \right)^{n/2} \rightarrow {\overline{x}}_{n} > \mu_{0} \\ 1 \rightarrow \text{ do contrário } \end{cases}$$

Agora, usamos seguinte relação: $$\sum_{i = 1}^{n}\left( x_{i} - \mu_{0} \right)^{2} = \sum_{i = 1}^{n}\left( x_{i} - {\overline{x}}_{n} \right)^{2} + {n\left( {\overline{x}}_{n} - \mu_{0} \right)}^{2}$$ para reescrever a parte de cima da estatística $\Lambda(\underline{x})$ como: $$\left\lbrack 1 + \frac{{n\left( {\overline{x}}_{n} - \mu_{0} \right)}^{2}}{\sum_{i = 1}^{n}\left( x_{i} - {\overline{x}}_{n} \right)^{2}} \right\rbrack^{- n/2}$$

Se $u$ é o valor observado da estatística $U$ (Equação [\[u-statistic\]](../testando-hipoteses-sobre-a-media-de-uma-normal-quando-a-variancia-e-desconhecida/index.md#u-statistic)), então podemos checar que: $$\frac{{n\left( {\overline{x}}_{n} - \mu_{0} \right)}^{2}}{\sum_{i = 1}^{n}\left( x_{i} - {\overline{x}}_{n} \right)^{2}} = \frac{u^{2}}{n - 1}$$

Ou seja, segue que $\Lambda(\underline{x})$ é uma função **não-crescente** de $u$. Por isso, para $k < 1$, $\Lambda(\underline{x}) \leq k \Leftrightarrow u \geq c$ onde: $$c = \sqrt{(n - 1) \cdot \left( \left( \frac{1}{k} \right)^{2/n} - 1 \right)}$$ Segue então que o teste de razão de verossimilhança é um teste $t$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Testando uma alternativa bilateral](../testando-uma-alternativa-bilateral/index.md)
- Próximo: [Comparando as médias de duas Distribuições Normais](../../comparando-as-medias-de-duas-distribuicoes-normais/index.md)
