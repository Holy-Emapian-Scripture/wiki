---
layout: "default"
title: "Ideia Inicial — Redes Aleatórias"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A1.md"
trilha: "../../../../trilhas/ciencia-de-redes/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 4
---

[Ciência de Redes](../../index.md) · [Redes Aleatórias](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Ideia Inicial

Também chamadas de **Redes Erdös-Renyi** ou **Redes de Poisson**, são tipos de redes que vão se montando aleatoriamente. Por exemplo, imagine que você está em uma festa e o anfitrião está fornecendo um vinho da melhor qualidade, mas ele não avisou ninguém. Um convidado curioso, por acidente, provou desse vinho e **adorou**, então ele vai contar para as pessoas da festa. A pergunta é, para quem ele vai falar? Ele vai falar para todos? Vai sobrar vinho para você?

Em cima disso conseguimos montar as redes aleatórias, onde cada par de nós (Aresta) é formado de acordo com uma **probabilidade**

**Definição: Rede Aleatória**

Uma rede aleatória é um grafo $G(V,E)$ de $\vert V\vert  = N$ nós onde cada par de nós é conectado por uma probabilidade **$p$**

Considere, agora, uma rede aleatória $G(V,E)$ com $\vert V\vert  = N$. Sendo $L$ a variável aleatória que representa a quantidade de arestas em $E$, queremos descobrir sua distribuição. Como cada aresta tem uma probabilidade $p$ de aparecer, podemos interpretar como ela aparecer ou não sendo uma variável indicadora, de forma que o número total de arestas segue uma distribuição binomial (Soma de variáveis de bernoulli independentes). Ou seja, a probabilidade a quantidade de arestas ser $L = l$ é: $${\mathbb{P}}(L = l) = \begin{pmatrix} \begin{pmatrix} N \\ 2 \end{pmatrix} \\ l \end{pmatrix}p^{l}(1 - p)^{\frac{N(N - 1)}{2} - l}$$ Podemos aplicar a mesma ideia para o grau de um vértice também. Vamos definir que $K$ é a variável aleatória que representa o **grau de um vértice arbitrário**, então: $${\mathbb{P}}(K = k) = \begin{pmatrix} N - 1 \\ k \end{pmatrix}p^{k}(1 - p)^{N - 1 - k}$$ Já que meu vértice pode se ligar a $N - 1$ vértices com probabilidade $p$, então isso vira a soma das variáveis indicadores que são $1$ quando o meu vértice se liga com outro vértice (${\mathbb{P}}({\mathbb{I}} = 1) = p$), de forma que eu tenho a soma de $N - 1$ variáveis de bernoulli independentes

Com isso, nós podemos definir o grau médio de $G$ como ${\mathbb{E}}\lbrack K\rbrack$: $$\delta_{\text{med }}(G) = {\mathbb{E}}\lbrack K\rbrack = (N - 1)p$$

E podemos obter também a variância dos graus $${\mathbb{V}}(K) = (N - 1)p(1 - p)$$

Então, apenas para resumir, temo que: $$\begin{array}{r} L \sim \text{ Bin}\left( \begin{pmatrix} N \\ 2 \end{pmatrix},p \right) \\ K \sim \text{ Bin}(N - 1,p) \end{array}$$

Porém, em redes reais, elas são **esparsas**, ou seja, eu tenho **muitos** nós e graus pequenos ($N \gg {\mathbb{E}}\lbrack K\rbrack$ notação que diz que $N$ é **muito maior** que ${\mathbb{E}}\lbrack K\rbrack$). E lembra qual é a distribuição que é a binomial com $n$ muito grande? Exato, a **Poisson**! Essas redes aleatórias também são chamadas de **redes de poisson**. Vamos, a partir de agora, denotar $\delta_{\text{med }}(G) = {\mathbb{E}}\lbrack K\rbrack = \hat{k}$ $${\mathbb{P}}(\delta(v) = k) = e^{- \hat{k}}\frac{{\hat{k}}^{k}}{k!}$$ Ou seja, para $N$ muito grande e $k$ pequeno com relação a $N$, podemos estimar de forma que: $$K \sim \text{ Poisson}\left( \hat{k} \right)$$

E isso tudo nos dá um resultado bem condizente e intuitivo, que é que, conforme nós aumentamos a probabilidade $p$ de uma aresta existir, então a rede vai ficando cada vez mais densa

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Anterior: [Redes Aleatórias](../index.md)
- Próximo: [Evolução das Redes Aleatórias](../evolucao-das-redes-aleatorias/index.md)
