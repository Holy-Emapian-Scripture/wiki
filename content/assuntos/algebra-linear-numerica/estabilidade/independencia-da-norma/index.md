---
layout: "default"
title: "Independência da Norma — Estabilidade"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 48
---

[Álgebra Linear Numérica](../../index.md) · [Estabilidade](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-57"></a>

# Independência da Norma

Você pode ter notado que, quando estamos definindo coisas em estabilidade com normas, denotamos $\| \cdot \|$ como **qualquer** tipo de norma, mas, se escolhermos uma certa norma, a definição pode não ser válida, certo? Como, pode ser válida para $\| \cdot \|_{2}$, mas não para $\| \cdot \|_{3}$, certo? Na verdade, errado! Podemos mostrar que **precisão**, **estabilidade** e **estabilidade retroativa** mantêm suas propriedades para **qualquer** tipo de norma! Isso significa que, quando escolhemos uma norma, podemos escolher uma que facilite os cálculos!

**Teorema**

Para problemas $f$ e seus algoritmos $\widetilde{f}$ em espaços normados de dimensão finita $X$ e $Y$, as propriedades de **precisão**, **estabilidade** e **estabilidade retroativa** são válidas ou não independentemente de qual norma eu escolher para fazer a análise

**Demonstração**

Se provarmos que, se $\| \cdot \|$ e $\| \cdot \|'$ são duas normas em $X$ e $Y$, então $\exists c_{1},c_{2}$ tais que: $$c_{1}\| x\| \leq \| x\|' \leq c_{2}\| x\|$$ então o teorema mostrado antes é válido, porque isso mostra:

1.  Se uma sequência converge ou é muito pequena em uma norma, ela será em todas as outras normas também

2.  Pequenos erros em uma norma serão pequenos em todas as outras normas também

Mas precisamos provar a afirmação anterior, certo? Vamos fazer isso! (O livro apenas diz que é fácil, lol)

Primeiro, vamos reduzir o problema a uma esfera unitária das normas, vamos definir: $$S = \left\{ x \in {\mathbb{C}}^{n}/\| x\| = 1 \right\}$$ esse conjunto é **fechado** porque a norma é **contínua** e é **limitado** (uma esfera, lol). Agora vamos definir a função $f(x) = \| x\|'$, porque $f(x)$ é contínua em ${\mathbb{C}}^{n}$ e $S$ é fechado e limitado, podemos encontrar o **máximo** e o **mínimo** valor de $f$ em $S$, vamos definir:

1.  $m = \min\limits_{x \in S}\| x\|'$

2.  $M = \max\limits_{x \in S}\| x\|'$

$m > 0$ porque $0 \notin S$. Agora, vamos tentar generalizar em ${\mathbb{C}}^{n}$. Se queremos generalizar para todo $x \neq 0 \in {\mathbb{C}}^{n}$, vamos escrever: $$x = \| x\|\left( \frac{x}{\| x\|} \right)$$ Você pode ver claramente que $\frac{x}{\| x\|} \in S$ porque $\|\frac{x}{\| x\|}\| = 1$. Então, vamos ver o que acontece se tomarmos $\| x\|'$: $$\| x\|' = \|\| x\|\left( \frac{x}{\| x\|} \right)\|' = \| x\|\|\frac{x}{\| x\|}\|'$$ Se você olhar de perto, $\frac{x}{\| x\|}$ é um vetor em $S$, isso significa que $\|\frac{x}{\| x\|}\|' \in \lbrack m,M\rbrack$ e, por causa de $\| x\|$ (número escalar positivo), podemos ver que $$\| x\|\|\frac{x}{\| x\|}\|' \in \left\lbrack \| x\| m,\| x\| M \right\rbrack$$ Podemos reescrever isso como $$m\| x\| \leq \| x\|' \leq M\| x\|$$ Isso significa que essas duas constantes existem e provam o teorema estabelecido antes

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Dependência de $m$ e $n$](../dependencia-de-m-e-n/index.md)
- Próximo: [Estabilidade da Aritmética de Ponto Flutuante](../estabilidade-da-aritmetica-de-ponto-flutuante/index.md)
