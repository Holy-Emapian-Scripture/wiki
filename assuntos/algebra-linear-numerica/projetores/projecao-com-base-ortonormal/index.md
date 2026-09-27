---
layout: "default"
title: "Projeção com base ortonormal — Projetores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 18
---

[Álgebra Linear Numérica](../../index.md) · [Projetores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-18"></a>

# Projeção com base ortonormal

Vimos na prova de [\[orthogonal-projectors\]](../projetores-ortogonais/index.md#orthogonal-projectors) que alguns valores singulares de $P$ são $0$, então poderíamos remover essas linhas de $\Sigma$ e reduzi-lo a $I$, também removendo as colunas e linhas de $Q$, obtendo: $$P = \widehat{Q}{\widehat{Q}}^{\ast}$$ Seja $\left\{ q_{1},\ldots,q_{n} \right\}$ qualquer conjunto de vetores ortonormais em ${\mathbb{C}}^{m}$ e sejam eles as colunas de $\widehat{Q}$, sabemos que, para qualquer vetor $v \in {\mathbb{C}}^{m}$: $$v = r + \sum_{i = 1}^{n}q_{i}q_{i}^{\ast}v$$ O quê? Quando vimos isso? Calma, deixe-me recapitular para você:

**Teorema**

Seja $\left\{ q_{1},\ldots,q_{n} \right\}$ qualquer conjunto de vetores ortonormais em ${\mathbb{C}}^{m}$, então qualquer $v \in {\mathbb{C}}^{m}$ pode ser expresso como $$v = r + \sum_{i = 1}^{n}q_{i}q_{i}^{\ast}v$$ Com $r$ sendo outro vetor em $C^{m}$ ortogonal a $\left\{ q_{1},\ldots,q_{n} \right\}$ e, $\rightarrow n = m \Rightarrow r = 0$ e o conjunto de vetores escolhido é uma base para ${\mathbb{C}}^{m}$

**Demonstração**

Você sabe que, dada uma base de ${\mathbb{C}}^{m}$, qualquer vetor pode ser expresso como uma combinação linear desses vetores. Imagine a base canônica (com algumas rotações, essa lógica pode ser expandida para outras bases ortonormais), você pode imaginar que, se projetar o vetor que você tem sobre qualquer vetor da base canônica, obterá um vetor que, se somar com outro vetor $r$, obterá seu vetor original novamente! E podemos continuar esse processo até fazermos isso com $n$ vetores da base canônica, obtendo o $r$ original que, se somarmos todas as nossas projeções, obtemos o vetor original novamente, ou seja: $$v = r + \sum_{i = 1}^{n}q_{i}q_{i}^{\ast}v$$

Ok, sabendo que um vetor pode ser expresso assim, podemos ver que a parte da soma é a mesma que fazer: $$\widehat{Q}{\widehat{Q}}^{\ast}v$$ Ou seja, $\sum_{i = 1}^{n}q_{i}q_{i}^{\ast}v$ é um projetor sobre $C\left( \widehat{Q} \right)$

**Teorema**

O complemento de um projetor ortogonal também é um projetor ortogonal

**Demonstração**

1.  $\left( I - \widehat{Q}{\widehat{Q}}^{\ast} \right)^{2} = I - 2\widehat{Q}{\widehat{Q}}^{\ast} + \left( \widehat{Q}{\widehat{Q}}^{\ast} \right)^{2} = I - 2\widehat{Q}{\widehat{Q}}^{\ast} + \widehat{Q}{\widehat{Q}}^{\ast} = I - \widehat{Q}{\widehat{Q}}^{\ast}$

2.  $\left( I - \widehat{Q}{\widehat{Q}}^{\ast} \right)^{\ast} = I - \left( \widehat{Q}{\widehat{Q}}^{\ast} \right)^{\ast} = I - \widehat{Q}{\widehat{Q}}^{\ast}$

Um caso especial é o projetor ortogonal de posto um, que pega o vetor e obtém o componente em uma única direção $q$, que pode ser escrito: $$P_{q} = qq^{\ast}$$ E seu complemento é a matriz de posto ($m - 1$) $$P_{\bot q} = I - qq^{\ast}$$ Esse conceito também é válido para vetores não unitários: $$P_{a} = \frac{aa^{\ast}}{a^{\ast}a}$$ $$P_{\bot a} = I - \frac{aa^{\ast}}{a^{\ast}a}$$ Só para esclarecer as coisas. Se projetarmos um vetor $v$ sobre um vetor $a$, estamos restringindo $v$ na direção da projeção, então, se projetarmos no complemento de $a$, é como se pudéssemos expressar $v$ como uma combinação linear de $a$ e alguns outros vetores, e então remover a parte de $a$ nessa combinação linear, tendo apenas os outros vetores expressando um novo vetor.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Projeção ortogonal sobre um vetor](../projecao-ortogonal-sobre-um-vetor/index.md)
- Próximo: [Projeção em base arbitrária](../projecao-em-base-arbitraria/index.md)
