---
layout: "default"
title: "Coeficiente de Clustering — Redes Aleatórias"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A1.md"
trilha: "../../../../trilhas/ciencia-de-redes/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 8
---

[Ciência de Redes](../../index.md) · [Redes Aleatórias](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-12"></a>

# Coeficiente de Clustering

Indica o quão agrupado um nó está dentro de uma rede. O grau de um nó não fala nada sobre a relação entre seus vizinhos, e é aí que o coeficiente de clustering entra

**Definição: Coeficiente de Clustering**

Dado uma rede $G(V,E)$, o coeficiente de clustering de um nó $v_{i} \in V$ é definido como: $$\text{ Cluster}\left( v_{i} \right) ≔ \frac{2 \cdot {\mathbb{L}}(v_{i})}{\delta(v_{i})\left( \delta(v_{i}) - 1 \right)}$$ Onde ${\mathbb{L}}(v_{i})$ é quantas arestas **entre si** os **vizinhos** de $v_{i}$ possuem e $\frac{\delta(v_{i})(\delta(v_{i}) - 1)}{2}$ é a quantidade **máxima** de arestas que poderiam estar interligando os vizinhos de $v_{i}$ (Quantidade de arestas em um grafo completo $K_{\delta(v_{i})}$)

Vamos tomar ${\mathbb{L}}(v_{i})$ como sendo a variável aleatória que indica quantas arestas os vizinhos de $v_{i}$ tem entre si. Novamente, como sempre, tomamos a variável indicadora ${\mathbb{I}}_{k}$ como sendo a variável indicadora que diz se a aresta $k$ faz parte desse grupo de links entre os vizinhos do nó $v_{i}$. Sabemos que ${\mathbb{P}}(I_{k} = 1) = p$, então ${\mathbb{L}}(v_{i})$ seria uma binomial, mas qual seria o parâmetro da quantidade? Quantas variáveis indicadoras ${\mathbb{I}}_{k}$ eu tenho que somar? Se pararmos para pensar, o **máximo** de links que podem existir entre os vizinhos de $v_{i}$ é o grafo completo formado por todos eles, então, no final, temos que: $${\mathbb{L}}(v_{i}) \sim \text{ Bin}\left( \begin{pmatrix} \hat{k} \\ 2 \end{pmatrix},p \right)$$ Então, no final, vamos ter que: $${\mathbb{E}}\left\lbrack {\mathbb{L}}(v_{i}) \right\rbrack \approx p\frac{\delta(v_{i})\left( \delta(v_{i}) - 1 \right)}{2} \Rightarrow \text{ Cluster}\left( v_{i} \right) = p = \frac{{\mathbb{E}}\lbrack K\rbrack}{\vert V\vert }$$

Só que sabemos que, em redes aleatórias, para que esse número seja alto, a probabilidade em si das arestas tem que ser alto, porém, se $p$ é alto, então a rede aleatória em si será um grande aglomerado, seria um único cluster enorme. Essa característica é um forte indicativo, por exemplo, de que redes como as **redes sociais** **não são** redes aleatórias. O livro do Barabás mostra um experimento e mostra que, em redes reais, o coeficiente de clustering é muito maior do que o esperado em redes aleatórias, de forma que, em redes reais, esse coeficiente costuma ser bastante independente de $N$, diferente do que encontramos agora há pouco

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Anterior: [Mundos pequenos](../mundos-pequenos/index.md)
- Próximo: [Grau Máximo e Grau Mínimo](../grau-maximo-e-grau-minimo/index.md)
