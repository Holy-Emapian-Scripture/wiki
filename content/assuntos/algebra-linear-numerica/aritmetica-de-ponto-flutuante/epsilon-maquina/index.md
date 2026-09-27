---
layout: "default"
title: "Épsilon Máquina — Aritmética de Ponto Flutuante"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 42
---

[Álgebra Linear Numérica](../../index.md) · [Aritmética de Ponto Flutuante](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-51"></a>

# Épsilon Máquina

Vamos ver a primeira definição do livro, que é: $$\varepsilon_{\text{machine}} = \frac{1}{2}\beta^{1 - t}$$ Mas o que isso significa? Por que ele definiu assim? Primeiro, $\varepsilon_{\text{machine}}$ é o número que, se fizermos essa operação em $F$, será válida $$1 + \varepsilon_{\text{machine}} > 1$$ Isso significa que, se somarmos 1 com um número menor que $\varepsilon_{\text{machine}}$, mesmo que por uma diferença infinitesimal, o número retornado será arredondado ou truncado para $1$ em $F$. O livro diz que essa definição é a distância entre 2 números representáveis em $F$, mas por que isso?

**Teorema**

A distância entre 2 números representáveis em $F$ é $\beta^{1 - t}$

**Demonstração**

Se temos $x$ escrito na notação da base $\beta$ com precisão $t$, escrevemo-lo como: $$x = 0,d_{1}d_{2.}..{d_{t}}_{\beta}$$ Se queremos incrementar algo nesse número, mas sem fazer com que ele saia da precisão possível e fazendo o menor incremento possível, podemos adicionar $1$ a $d_{t}$. Então vamos fazer isso e ver o que acontece, escrevendo $x$: $$x = d_{1}\beta^{- 1} + d_{2}\beta^{- 2} + \ldots + d_{t}\beta^{1 - t}$$ Se somarmos $1$ a $d_{t}$: $$\alpha = d_{1}\beta^{- 1} + d_{2}\beta^{- 2} + \ldots + \left( d_{t} + 1 \right)\beta^{1 - t}$$ $$\Leftrightarrow \alpha = d_{1}\beta^{- 1} + d_{2}\beta^{- 2} + \ldots + d_{t}\beta^{1 - t} + \beta^{1 - t}$$ Mas observe como podemos reescrever isso como $$\alpha = x + \beta^{1 - t}$$ Isso significa que $\alpha$ (o próximo número representável), é $x + \mathbf{\beta^{1 - t}}$, ou seja, a distância entre eles

Agora podemos visualizá-lo como uma linha, onde temos os números representáveis e, se tentarmos representar um número que está no intervalo entre eles, o computador o arredondará com base em $\varepsilon_{\text{machine}}$

![](../../assets/Epsilon_Machine.jpg)

Os pontos azul-ciano representam números reais que não podem ser representados inteiramente por $F$, e as setas mostram para onde o computador os arredonda. Mudaremos essa definição mais tarde, e você entenderá por que depois.

O livro nos mostra uma desigualdade que todo $\varepsilon_{\text{machine}}$ deve satisfazer, mas essa desigualdade pode ser reescrita:

**Definição**

Seja $F$ um conjunto de ponto flutuante. $\text{fl}:{\mathbb{R}} \rightarrow F$ é uma função que retorna a aproximação arredondada da entrada $x$ no conjunto $F$

<a id="floating_point_conversion"></a>

**Teorema: Conversão de Ponto Flutuante**

$\forall x \in {\mathbb{R}}$, existe $\varepsilon$ com $\vert \varepsilon\vert  \leq \varepsilon_{\text{machine}}$ tal que: $$\text{ fl}(x) = x(1 + \varepsilon)$$

O que isso significa? Significa que, sempre que arredondamos um número real para ajustá-lo em $F$, o número arredondado é equivalente a multiplicar $x$ por $1 +$ um número muito pequeno, você pode visualizá-lo olhando para a representação em linha de $F$ que mostrei antes

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Números não em $F$](../numeros-nao-em-f/index.md)
- Próximo: [Aritmética de Ponto Flutuante](../aritmetica-de-ponto-flutuante/index.md)
