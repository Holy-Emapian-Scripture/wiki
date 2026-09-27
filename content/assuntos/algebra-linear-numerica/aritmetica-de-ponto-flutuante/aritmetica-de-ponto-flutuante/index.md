---
layout: "default"
title: "Aritmética de Ponto Flutuante — Aritmética de Ponto Flutuante"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 43
---

[Álgebra Linear Numérica](../../index.md) · [Aritmética de Ponto Flutuante](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-52"></a>

# Aritmética de Ponto Flutuante

Precisamos fazer operações com números, certo? Mas temos o mesmo problema, os computadores precisam arredondar porque não conseguem entender todos os números em um intervalo, então como podemos tornar as operações o mais precisas possível? Construímos um computador baseado neste princípio (alguns computadores podem ter mais princípios em seu núcleo, então algumas operações podem ser ainda mais precisas, mas vamos focar apenas neste):

<a id="fundamental_axiom_of_floating_point_arithmetic"></a>

**Definição: Axioma Fundamental da Aritmética de Ponto Flutuante**

Dado que $+$, $-$, $\times$ e $\div$ representam operações em $\mathbb{R}$, considere $\oplus$, $\ominus$, $\otimes$ e $⨸$ sendo operações em $F$. Seja $\circledast$ definir qualquer uma das operações anteriores em $F$, então definimos um computador que realiza a operação $x \circledast y$ como $$x \circledast y = \text{ fl}(x \ast y) = (x \ast y)$$ Isso significa que construímos um computador tal que $\forall x,y \in F$, existe $\varepsilon$ com $\vert \varepsilon\vert  \leq \varepsilon_{\text{machine}}$ tal que $$x \circledast y = (x \ast y)(1 + \varepsilon)$$

Em outras palavras, toda operação em $F$ tem um erro com tamanho **no máximo** $\varepsilon_{\text{machine}}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Épsilon Máquina](../epsilon-maquina/index.md)
- Próximo: [Mais sobre Épsilon Máquina](../mais-sobre-epsilon-maquina/index.md)
