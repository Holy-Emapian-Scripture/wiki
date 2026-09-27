---
layout: "default"
title: "Limite Crítico — Percolação e Robustez"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A2.md"
trilha: "../../../../trilhas/ciencia-de-redes/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 9
---

[Ciência de Redes](../../index.md) · [Percolação e Robustez](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-9"></a>

# Limite Crítico

Vamos agora utilizar do critério visto anteriormente para entender o porquê de as redes livre-de-escala serem robustas a falhas aleatórias. Primeiro de tudo, ao remover uma fração dos nós de uma rede **aleatoriamente**, existem duas consequências:

- Altera o grau de alguns nós \[$k' \leq k$\]

- Muda a distribuição dos graus \[$p_{k} \rightarrow p'_{k}'$\]

Vamos primeiro descobrir a nova distribuição dos graus após a remoção da fração $f$. Vamos fixar que estamos analisando um nó $v \in V$ que, antes da remoção, tem grau $k$, ou seja, tem $k$ vizinhos. Para saber quantos vizinhos vão sobrar após remover a fração, definimos uma variável indicadora para cada um dos vizinhos do nó $v$ $${\mathbb{I}}_{j} = \begin{cases} 1\text{ se o vizinho NÃO foi removido com probabilidade }1 - f \\ 0\text{ se o vizinho foi removido com probabilidade }f \end{cases}$$

então a quantidade de vizinhos de $v$ APÓS A REMOÇÃO dos $f$ nós é: $$\sum_{j = 1}^{k}{\mathbb{I}}_{j}$$

e como isso é uma soma de bernoullis independentes, essa soma nos dá uma distribuição $\text{Binomial}(k,1 - f)$, então temos que: $${\mathbb{P}}(K' = k'\vert K = k) = \begin{pmatrix} k \\ k' \end{pmatrix}f^{k - k'}(1 - f)^{k}'$$

Considere que $K$ é a variável aleatória do grau de um nó selecionado aleatoriamente na rede ANTERIOR à remoção da fração $f$ e $K'$ é selecionando um nó na rede POSTERIOR à remoção da fração. Então para achar a nova distribuição dos graus após as remoções, apenas fazemos: $$\begin{aligned} {\mathbb{P}}(K' = k') & = \sum_{i}^{\infty}{\mathbb{P}}(K' = k'\vert K = i){\mathbb{P}}(K = i) \\ & = \sum_{i}^{\infty}{\mathbb{P}}(K = i)\begin{pmatrix} i \\ k' \end{pmatrix}f^{i - k'}(1 - f)^{k'} \end{aligned}$$

Agora vamos assumir que sabemos ${\mathbb{E}}\lbrack K\rbrack$ e ${\mathbb{E}}\left\lbrack K^{2} \right\rbrack$ (distribuição original), e queremos calcular ${\mathbb{E}}\lbrack K'\rbrack$ e ${\mathbb{E}}\left\lbrack K'^{2} \right\rbrack$, então fazemos: $${\mathbb{E}}\lbrack K'\rbrack = {\mathbb{E}}\lbrack\underset{\text{ Bin}(k,1 - f)}{\underbrace{{\mathbb{E}}\left\lbrack K'\vert K \right\rbrack}}\rbrack = {\mathbb{E}}\left\lbrack (1 - f)K \right\rbrack = (1 - f){\mathbb{E}}\lbrack K\rbrack$$ $$\begin{aligned} {\mathbb{E}}\left\lbrack K'^{2} \right\rbrack & = {\mathbb{V}}\lbrack K'\rbrack + \left( {\mathbb{E}}\lbrack K'\rbrack \right)^{2} \\ & = {\mathbb{V}}\lbrack K'\rbrack + (1 - f)^{2}\left( {\mathbb{E}}\lbrack K\rbrack \right)^{2} \\ {\mathbb{V}}\lbrack K'\rbrack & = {\mathbb{E}}\left\lbrack {\mathbb{V}}\left\lbrack K'\vert K \right\rbrack \right\rbrack + {\mathbb{V}}\left\lbrack {\mathbb{E}}\left\lbrack K'\vert K \right\rbrack \right\rbrack \\ & = (1 - f)f{\mathbb{E}}\lbrack K\rbrack + (1 - f)^{2}{\mathbb{V}}\lbrack K\rbrack \end{aligned}$$ $$\begin{aligned} \Rightarrow {\mathbb{E}}\left\lbrack K'^{2} \right\rbrack & = (1 - f)f{\mathbb{E}}\lbrack K\rbrack + (1 - f)^{2}\left( {\mathbb{V}}\lbrack K\rbrack + {\mathbb{E}}\lbrack K\rbrack^{2} \right) \\ & = (1 - f)f{\mathbb{E}}\lbrack K\rbrack + (1 - f)^{2}{\mathbb{E}}\left\lbrack K^{2} \right\rbrack \end{aligned}$$

Agora que sabemos os momentos da distribuição após a remoção dos $f$, podemos aplicar o critério de Molloy-Reed na rede posterior à remoção $$\begin{array}{r} {\mathbb{E}}\frac{\left\lbrack K'^{2} \right\rbrack}{\mathbb{E}}\lbrack K'\rbrack = 2 \Leftrightarrow \frac{(1 - f)f{\mathbb{E}}\lbrack K\rbrack + (1 - f)^{2}{\mathbb{E}}\left\lbrack K^{2} \right\rbrack}{(1 - f){\mathbb{E}}\lbrack K\rbrack} = 2 \\ f + {\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack - f{\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack = 2 \\ f\left( 1 - {\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack \right) = 2 - {\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack \\ f = 1 - \frac{1}{{\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack - 1} \end{array}$$

Note que a fração limite depende única e exclusivamente das informações da distribuição. Se olharmos o caso **específico** das redes aleatórias: $$f_{c} = 1 - \frac{1}{{\mathbb{E}}\lbrack K\rbrack}$$

Ou seja, quanto mais densa a rede, maior a fração crítica de nós necessários para a remoção. Agora, para redes livre-de-escala, vamos fazer um passo-a-passo diferente. Vamos primeiro calcular o $m$-ésimo momento do grau de uma rede livre-de-escala: $$\begin{aligned} {\mathbb{E}}\left\lbrack K^{m} \right\rbrack & = (\gamma - 1)k_{\text{min}}^{\gamma - 1}\int_{k_{\text{min}}}^{k_{\text{max}}}k^{m - \gamma}dk \\ & = \frac{\gamma - 1}{m - \gamma + 1}k_{\text{min}}^{\gamma - 1}\left\lbrack k^{m - \gamma + 1} \right\rbrack_{k_{\text{min}}}^{k_{\text{max}}} \\ & = \frac{\gamma - 1}{m - \gamma + 1}k_{\text{min}}^{\gamma - 1}\left\lbrack k_{\text{max}}^{m - \gamma + 1} - k_{\text{min}}^{m - \gamma + 1} \right\rbrack \end{aligned}$$

Agora calculamos o limite crítico $f_{c}$ $$\kappa = {\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack = \frac{(2 - \gamma)k_{\text{max}}^{3 - \gamma} - k_{\text{min}}^{3 - \gamma}}{(3 - \gamma)k_{\text{max}}^{2 - \gamma} - k_{\text{min}}^{2 - \gamma}}$$ então, obtemos: $$\kappa = \vert \frac{2 - \gamma}{3 - \gamma}\vert \begin{cases} k_{\text{min }}\text{ se }\gamma > 3 \\ k_{\text{max}}^{3 - \gamma}k_{\text{min}}^{\gamma - 2}\text{ se }2 < \gamma < 3 \\ k_{\text{max }}\text{ se }1 < \gamma < 2 \end{cases}$$ daí, utilizando todas as contas que vimos agora relebrando o fato, visto no último resumo, que: $$k_{\text{max }} = k_{\text{min }}N^{\frac{1}{\gamma - 1}}$$

vamos obter que: $$\begin{aligned} f_{c} & = 1 - \frac{1}{\kappa - 1} \\ & = 1 - \frac{C}{N^{\frac{3 - \gamma}{\gamma - 1}}} \end{aligned}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/ciencia-de-redes/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a2.md#apresentacao-original)

- Anterior: [Critério de Molloy-Reed](../criterio-de-molloy-reed/index.md)
- Próximo: [Tolerância a Ataques](../tolerancia-a-ataques/index.md)
