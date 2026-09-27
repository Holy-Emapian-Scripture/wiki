---
layout: "default"
title: "Estimador de Bayes — Estimadores de Bayes"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 11
---

[Inferência Estatística](../../index.md) · [Estimadores de Bayes](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-11"></a>

# Estimador de Bayes

Supondo agora que nós temos acesso as observações $\underline{x}$. Então também temos acesso à distribuição posteriori $\xi(\theta\vert x_{1},\ldots,x_{n})$, então podemos escolher uma estimativa $a$ tal que ela minimize: $${\mathbb{E}}\left\lbrack L(\theta,a)\vert \underline{x} \right\rbrack = \int_{\Omega}L(\theta,a)\xi(\theta\vert \underline{x})d\theta$$

**Definição: Estimador de Bayes**

Seja $L(\theta,a)$ uma função de perca. Para cada valor possível $\underline{x}$ de $\underline{X}$, deixe que $\delta^{\ast \left( \underline{x} \right)}$ ser o valor de $a$ que minimiza ${\mathbb{E}}\left\lbrack L(\theta,a) \right\rbrack$ é minimizado. Então $\delta^{\ast}$ é chamado de **Estimador de Bayes** de $\theta$. Uma vez que $\underline{X} = \underline{x}$ é observado, chamamos $\delta^{\ast \left( \underline{x} \right)}$ de **estimativa bayesiana** de $\theta$

Podemos também descrever como, para todos os valores possíveis de $\underline{x}$, queremos: $${\mathbb{E}}(L\left( \theta,\delta^{\ast \left( \underline{x} \right)}\vert \underline{x} \right)) = \min\limits_{\text{Todos }a}{\mathbb{E}}(L(\theta,a)\vert \underline{x})$$

Algumas percas de função muito comum são: $$L(\theta,a) = (\theta - a)^{2}$$<a id="min-squared-error"></a> $$L(\theta,a) = \vert \theta - a\vert$$<a id="median-error"></a>

**Teorema**

Seja $L(\theta,a) = (\theta - a)^{2}$, então $\delta^{\ast \left( \underline{x} \right)} = {\mathbb{E}}(\theta\vert \underline{x})$

**Demonstração**

Queremos provar que $${\mathbb{E}}\left\lbrack (X - \mu)^{2} \right\rbrack \leq {\mathbb{E}}\left\lbrack (X - d)^{2} \right\rbrack\text{\quad\quad}\forall d \in {\mathbb{R}}$$ E a igualdade só vale quando $\mu = d$. Ou seja: $$\mu = \text{ argmin}_{d \in {\mathbb{R}}}{\mathbb{E}}\left\lbrack (X - d)^{2} \right\rbrack$$ Então: $$\begin{array}{r} {\mathbb{E}}\left\lbrack (X - d)^{2} \right\rbrack = {\mathbb{E}}\left\lbrack X^{2} - 2Xd + d^{2} \right\rbrack \\ {\mathbb{E}}\left\lbrack X^{2} \right\rbrack - 2d{\mathbb{E}}\lbrack X\rbrack + d^{2} = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack - 2d\mu + d^{2} \end{array}$$ Como queremos minimizar isso, com relação a $d$, vamos derivar: $$\frac{\partial}{\partial d}\left( {\mathbb{E}}\left\lbrack X^{2} \right\rbrack - 2d\mu + d^{2} \right) = - 2\mu + 2d$$ E isso é igual a $0$ quando $d = \mu$

**Teorema**

Seja $L(\theta,a) = \vert \theta - a\vert$, então $\delta^{\ast \left( \underline{x} \right)}$ é a mediana de $\theta\vert \underline{x}$

**Demonstração**

$${\mathbb{E}}\vert X - a\vert  \geq {\mathbb{E}}\vert X - m\vert \text{\quad\quad}\forall a \in {\mathbb{R}}$$ Então queremos provar que $${\mathbb{E}}\vert X - a\vert  - {\mathbb{E}}\vert X - m\vert  \geq 0$$ Vamos assumir que $m < a$ ($m > a$ é análogo)

Se $X \leq m$, então: $\vert X - a\vert  - \vert X - m\vert  = a - X - (m - X) = a - m$

Se $X > m$, então: $\vert X - a\vert  - \vert X - m\vert  = X - a - X + m = m - a$

Defina então $Y = \vert X - a\vert  - \vert X - m\vert$. Defina também: $${\mathbb{I}}_{X} = \begin{cases} 1\text{ se }X \leq m \\ 0\text{ se }X > m \end{cases}$$ Então teremos que: $$\begin{aligned} {\mathbb{E}}(Y) & = {\mathbb{E}}(Y \cdot {\mathbb{I}}_{X}) + {\mathbb{E}}(Y \cdot \left( 1 - {\mathbb{I}}_{X} \right)) \\ & \geq (a - m){\mathbb{E}}({\mathbb{I}}_{X}) + (m - a){\mathbb{E}}(1 - {\mathbb{I}}_{X}) \\ & = (a - m){\mathbb{P}}(X \leq m) + (m - a){\mathbb{P}}(X > m) \\ & = (a - m){\mathbb{P}}(X \leq m) - (a - m)\left( 1 - {\mathbb{P}}(X \leq m) \right) \\ & = (a - m)\left( 2{\mathbb{P}}(X \leq m) - 1 \right) \geq 0 \end{aligned}$$ Porém essa equação final é satisfeita pela definição de mediana!

Quando estamos tentando tentando estimar um parâmetro $\theta$, queremos que, quanto mais amostras tivermos, ou seja, quando $n \rightarrow \infty$, o nosso estimador vai convergindo para $\theta$

**Definição: Consistência**

Quando uma sequência $\left( \delta_{n} \right)_{n \geq 1}$ converge para o valor verdadeiro do parâmetro $\theta$, dizemos que $\left( \delta_{n} \right)_{n \geq 1}$ é consistente para $\theta$

Ou seja, com grandes quantidades de dados, a probabilidade do estimador $\hat{\theta}$ estar **muito** próximo de $\theta$ é alta

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Função de Perda](../funcao-de-perda/index.md)
- Próximo: [Estimadores para Parâmetros mais gerais](../estimadores-para-parametros-mais-gerais/index.md)
