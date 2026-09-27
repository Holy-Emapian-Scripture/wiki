---
layout: "default"
title: "Multiplicidades Algébrica e Geométrica — Problemas de Autovalores"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 19
---

[Álgebra Linear Numérica](../../index.md) · [Problemas de Autovalores](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-19"></a>

# Multiplicidades Algébrica e Geométrica

Como mencionado anteriormente, definimos os conjuntos nos quais a matriz atua como multiplicação escalar:

**Definição: Autoespaço**

Dada $A \in {\mathbb{C}}^{m \times n},\lambda \in {\mathbb{C}}$, definimos $S_{\lambda} \in {\mathbb{C}}^{m}$ como sendo o **autoespaço** gerado por todos os $v \in {\mathbb{C}}^{m}$ tais que $Av = \lambda v$

<a id="def_autoespaço"></a>

Interpretaremos $\dim(S_{\lambda})$ como a maior quantidade de autovetores L.I associados a um único $\lambda$, e chamaremos isso de *multiplicidade geométrica* de $\lambda$. Então temos:

**Definição**

(Multiplicidade Geométrica) A multiplicidade geométrica de $\lambda$ é $\dim(S_{\lambda})$

<a id="def_multiplicidade_geometrica"></a>

Note que da equação [\[eq_autovalores_autovetores\]](../definicoes/index.md#eq_autovalores_autovetores):

$$Ax = \lambda x \Leftrightarrow Ax - \lambda x = 0 \Leftrightarrow (A - \lambda I)x = 0$$

Mas como $x \neq 0$ e $x \in N(A - \lambda I)$, $(A - \lambda I)$ não é injetiva. Logo não é inversível:

$$\det(A - \lambda I) = 0$$ <a id="eq_polinimio_caracteristico"></a>

**Definição: Polinômio Característico**

A equação [\[eq_polinimio_caracteristico\]](#eq_polinimio_caracteristico) se chama **polinômio característico** de $A$ e é um polinômio de grau $m$ em $\lambda$. Pelo teorema fundamental da Álgebra, se $\lambda_{1},\ldots,\lambda_{n}$ são raízes de [\[eq_polinimio_caracteristico\]](#eq_polinimio_caracteristico), então podemos escrever isso como: $$p(\lambda) = \left( \lambda - \lambda_{1} \right)\left( \lambda - \lambda_{2} \right)\ldots\left( \lambda - \lambda_{n} \right)$$<a id="characteristical-polynomial"></a> (Nota: $\lambda$ é uma variável, enquanto $\lambda_{j}$ é uma raíz do polinômio, fique atento)

Com isso, prosseguimos com:

**Definição: Multiplicidade Algébrica**

A multiplicidade algébrica de $\lambda$ é a multiplicidade de $\lambda$ como raiz do polinômio característico de $A$

<a id="def_multiplicidade_algebrica"></a>

A definição de polinômio característico e de multiplicidade algébrica faz a gente ter um jeito muito fácil de contar a quantidade de autovalores de uma matriz

**Teorema**

Se $A \in {\mathbb{C}}^{m \times m}$, então $A$ tem $m$ autovalores, contando com a multiplicidade algébrica.

Isso mostra que **toda matriz** possui **pelo menos** 1 autovalor

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Decomposição em Autovalores](../decomposicao-em-autovalores/index.md)
- Próximo: [Transformações Similares](../transformacoes-similares/index.md)
