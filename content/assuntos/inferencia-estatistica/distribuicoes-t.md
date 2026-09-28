---
layout: "default"
title: "Distribuições $t$"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 6
---

[Inferência Estatística](index.md)

<!-- wiki:original:inicio -->

<a id="secao-6"></a>

# Distribuições $t$


<a id="secao-7"></a>

## Propriedades

**Teorema**

Se $T \sim t_{m}$, então: $$\begin{aligned} & {\mathbb{E}}\lbrack T\rbrack = 0\text{\quad\quad}(m > 1) \\ & {\mathbb{V}}\lbrack T\rbrack = \frac{m}{m - 2}\text{\quad\quad}(m > 2) \end{aligned}$$

**Demonstração**

Seja $Z \sim N(0,1)$ e $W \sim Χ_{m}^{2}$, sabemos que $$T = \frac{Z}{\sqrt{\frac{W}{m}}} \sim t_{m}$$ porém, temos que $T\vert W = w \sim N\left( 0,\frac{m}{w} \right)$, logo: $${\mathbb{E}}\left\lbrack T\vert W = w \right\rbrack = 0$$ pela lei de adão: $${\mathbb{E}}\left\lbrack {\mathbb{E}}\left\lbrack T\vert W = w \right\rbrack \right\rbrack = {\mathbb{E}}\lbrack T\rbrack = {\mathbb{E}}\lbrack 0\rbrack = 0$$

No mesmo raciocínio, lembrando a lei de EVA $$\begin{array}{r} {\mathbb{V}}\lbrack X\rbrack = {\mathbb{E}}\left\lbrack {\mathbb{V}}\left\lbrack X\vert Y \right\rbrack \right\rbrack + {\mathbb{V}}\left\lbrack {\mathbb{E}}\left\lbrack X\vert Y \right\rbrack \right\rbrack \\ \Rightarrow {\mathbb{V}}\lbrack T\rbrack = {\mathbb{E}}\left\lbrack {\mathbb{V}}\left\lbrack T\vert W \right\rbrack \right\rbrack + {\mathbb{V}}\left\lbrack {\mathbb{E}}\left\lbrack T\vert W \right\rbrack \right\rbrack \end{array}$$ sabemos que ${\mathbb{E}}\left\lbrack T\vert W \right\rbrack = 0$, então basta calcularmos ${\mathbb{V}}\left\lbrack T\vert W \right\rbrack$ que, como vimos antes, vai ser $\frac{W}{m}$, então: $${\mathbb{V}}\lbrack T\rbrack = {\mathbb{E}}\left\lbrack \frac{m}{W} \right\rbrack$$ Sabemos que $W$ é uma $\Gamma(\frac{m}{2},\frac{1}{2})$, então $W^{- 1}$ é uma Gamma Inversa, logo, sua média vai ser: $${\mathbb{E}}\left\lbrack W^{- 1} \right\rbrack = \frac{\frac{1}{2}}{\frac{m}{2} - 1} = \frac{\frac{1}{2}}{\frac{m - 2}{2}} = \frac{1}{m - 2}$$ logo: $${\mathbb{V}}\lbrack T\rbrack = \frac{m}{m - 2}$$

<a id="moments-divergence"></a>

**Teorema: Divergência dos Momentos**

Se $T \sim t_{m}$, então ${\mathbb{E}}⟦T\vert ^{p}\rbrack$ diverge se $p \geq m$. Se $m$ é inteiro, então apenas os $m - 1$ primeiros momentos existem

**Teorema**

Sejam $X_{1},\ldots,X_{n} \sim N\left( \mu,\sigma^{2} \right)$ e $\sigma' = \left( \frac{1}{n - 1}{\sum(X_{i} - {\overline{X}}_{n})}^{2} \right)^{\frac{1}{2}}$, então $$\frac{\sqrt{n}\left( {\overline{X}}_{n} - \mu \right)}{\sigma}' \sim t_{n - 1}$$

**Demonstração**

Defina $S_{n}^{2} = {\sum(X_{i} - {\overline{X}}_{n})}^{2}$, $Z - \sqrt{n}({\overline{X}}_{n} - \mu)/\sigma$ e $Y = S_{n}^{2}/\sigma^{2}$. Sabemos que $Y$ e $Z$ são independentes e $Y \sim Χ_{n - 1}^{2}$. Definimos então: $$U = \frac{Z}{\sqrt{\frac{Y}{n - 1}}}$$ que é uma $t_{n - 1}$ por definição. Porém, perceba que: $$U = \frac{\frac{\sqrt{n}\left( {\overline{X}}_{n} - \mu \right)}{\sigma}}{\frac{1}{\sigma}\sqrt{\frac{S_{n}^{2}}{n - 1}}} = \frac{\sqrt{n}\left( {\overline{X}}_{n} - \mu \right)}{\sigma}'$$

Essa propriedade é interessante, pois saímos de variáveis que dependiam diretamente de $\sigma$ para uma variável que tem distribuição que **não depende** de $\sigma$

**Teorema**

Uma distribuição $t_{1}$ é equivalente a uma distribuição de *Cauchy*

**Definição: Distribuição de Cauchy**

Se $X \sim \text{ Cauchy}\left( x_{0},\gamma \right)$, então temos: $$f_{X}(x) = \frac{1}{\pi\gamma\left\lbrack 1 + \left( \frac{x - x_{0}}{\gamma} \right)^{2} \right\rbrack}$$ $$F_{X}(x) = \frac{1}{\pi}\arctan(\frac{x - x_{0}}{\gamma}) + \frac{1}{2}$$ Além do fato que: $${\mathbb{E}}⟦X\vert ^{k}\rbrack = \infty\text{\quad\quad}\forall k$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Distribuição Conjunta da Média e Variância Amostral](distribuicao-conjunta-da-media-e-variancia-amostral.md)
- Próximo: [Intervalos de Confiança](intervalos-de-confianca.md)
