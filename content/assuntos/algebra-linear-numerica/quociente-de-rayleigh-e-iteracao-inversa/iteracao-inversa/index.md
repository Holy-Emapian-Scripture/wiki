---
layout: "default"
title: "Iteração Inversa — Quociente de Rayleigh e Iteração Inversa"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 41
---

[Álgebra Linear Numérica](../../index.md) · [Quociente de Rayleigh e Iteração Inversa](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-41"></a>

# Iteração Inversa

Antes de entendermos o que a iteração inversa faz, vamos conferir um teorema:

**Teorema**

Dado $\mu \in {\mathbb{R}}$ tal que $\mu$ **não é** autovalor de $A$, então os autovetores de $(A - \mu I)^{- 1}$ são os mesmos de $A$, onde os autovalores correspondentes são $\left\{ \left( \lambda_{j} - \mu \right)^{- 1} \right\}$ de tal forma que $\lambda_{j}$ são os autovalores de $A$

**Demonstração**

Muito importante ressaltar que, como $\mu$ **não é** autovalor de $A$, então $A - \mu I$ é **inversível**. $$\begin{array}{r} Av = \lambda v \\ Av - \mu Iv = \lambda v - \mu Iv \\ (A - \mu I)v = (\lambda - \mu)v\begin{array}{r} \\ (A - \mu I) \end{array}^{- 1}(A - \mu I)v = (A - \mu I)^{- 1}(\lambda - \mu)v \\ \frac{1}{\lambda - \mu}v = (A - \mu I)^{- 1}v \end{array}$$

E isso nos dá uma ideia! Se aplicarmos a iteração de potências em $(A - \mu I)^{- 1}$, o valor convergirá rapidamente para $q_{j}$ (Autovetor de $A$)

<a id="inverse-power-iteration"></a>

1.  **function** ReverseIteration($A \in {\mathbb{C}}^{m \times m}$, $v^{(0)}\text{ com }\| v^{(0)}\| = 1$) {

    1.  **for** $k = 1,2,3,\ldots$

        1.  Resolva $(A - \mu I)w = v^{(k - 1)}$ para $w$

        2.  $v^{(k)} = w/\| w\|$

        3.  $\lambda^{(k)} = \left( v^{(k)} \right)^{T}Av^{(k)}$

2.  }

*Figura 10. Iteração Inversa*

Você pode estar se perguntando: “Mas e se $\mu$ for um autovalor de $A$? Isso vai fazer com que $A - \mu I$ não seja inversível! Ou de $\mu$ for muito próximo de um autovalor de $A$, se isso acontecer, $A - \mu I$ vai ser **muito** mal-condicionada e vai ser quase impossível uma inversa precisa! Isso não vai quebrar o algoritmo?”. São perguntas válidas, mas não, isso não quebra o algoritmo! Há um exercício no livro que aborda isso (Se eu conseguir resolver antes da A2, eu coloco aqui).

Aqui o algoritmo também é um pouco mais interessante pois, dependendo do $\mu$ que escolhermos, podemos encontrar um autovalor diferente, ou seja, podemos escolher qual autovalor encontrar se fizermos a escolha certa de $\mu$

**Teorema**

Suponha que $\lambda_{J}$ é o autovalor **mais próximo** de $\mu$ e $\lambda_{K}$ é o **segundo** mais próximo. Suponha então que $q_{J}^{T}v^{(0)} \neq 0$, então as iterações do [\[inverse-power-iteration\]](#inverse-power-iteration) satisfazem: $$\begin{array}{r} \| v^{(k)} - \left( \pm q_{J} \right)\| = O\left( \vert \frac{\mu - \lambda_{J}}{\mu - \lambda_{K}}\vert ^{k} \right) \\ \vert \lambda^{(k)} - \lambda_{J}\vert  = O\left( \vert \frac{\mu - \lambda_{J}}{\mu - \lambda_{K}}\vert ^{2k} \right) \end{array}$$ Conforme $k \rightarrow \infty$ e $\pm$ tem o mesmo significado que [\[power-iteration-stability\]](../iteracao-por-potencias/index.md#power-iteration-stability)

Esse algoritmo, como mencionado, é muito útil se os autovalores são conhecidos ou se tem uma noção de quanto eles valem aproximadamente ($\mu$ converge para o mais próximo)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Iteração por Potências](../iteracao-por-potencias/index.md)
- Próximo: [Iteração do Quociente de Rayleigh](../iteracao-do-quociente-de-rayleigh/index.md)
