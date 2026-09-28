---
layout: "default"
title: "Percolação e Robustez"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A2.md"
trilha: "../../../trilhas/ciencia-de-redes/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 5
---

[Ciência de Redes](index.md)

<!-- wiki:original:inicio -->

<a id="secao-5"></a>

# Percolação e Robustez


<a id="percolacao"></a>
<a id="secao-6"></a>

## Percolação

Em nosso contexto, vamos definir da seguinte forma. Queremos olhar a **capacidade da rede** de **se manter conexa após perder uma fração de seus nós**. Para começar, não vamos partir para a teoria em si, vamos analisar **um caso específico** primeiro para pegar a noção

<a id="square-lattice"></a>

![Rede quadrada onde cada cruzamento representa um nó (Pode ou não existir)](assets/square-lattice.png)

*Figura 3. Rede quadrada onde cada cruzamento representa um nó (Pode ou não existir)*

Vamos imaginar um grid onde cada intersecção de linhas é um nó que pode ou não existir com probabilidade $p$ e há uma aresta entre dois nós se eles forem vizinhos. Podemos fazer então duas perguntas:

- Qual o tamanho esperado do maior cluster?

- Qual o tamanho médio dos clusters?

Olhando o gráfico presente na [rede quadrada](#square-lattice), o tamanho médio dos clusters não muda gradativamente de acordo com o valor de $p$, mas ele se explode conforme se aproxima de um valor crítico $p_{c}$. Isso ocorre porque, conforme $p \rightarrow p_{c}$, os pequenos clusters se aglutinam e formam uma componente maior muito grande

Então, de acordo com o observado podemos fazer algumas definições e observações:

- Tamanho médio de clusters:

$$
{\mathbb{E}}\lbrack S\rbrack \propto \vert p - p_{c}\vert ^{- \gamma_{p}}
$$

- Parâmetro de ordem (Probabilidade de um nó selecionado aleatoriamente pertencer ao maior cluster):

$$
p_{\infty} \propto \left( p - p_{c} \right)^{\beta_{p}}
$$

- Correlação de tamanho (Distância média entre dois nós do mesmo cluster):

$$
\xi \propto \vert p - p_{c}\vert ^{- \upsilon}
$$

Perceba que, em $p_{c}$, o maior cluster tem tamanho infinito, assim ele cobre todo o quadriculado. $\gamma_{p},\beta_{p}$ e $\upsilon$ são chamados de expoentes críticos e a teoria da percolação diz que eles são universais (Não dependem da natureza do grid, pode ser triangular, hexagonal, enfim)

Agora que entendemos um pouco melhor o comportamento do nosso caso específico, vamos analisar ele como uma rede em si. Imagine que vamos remover uma fração $f$ dos nós da rede antes mencionada. Conforme aumentamos a fração $f$, em algum momento, a componente gigante vai se desfazer e, para algum $f_{c}$, vale que $\forall f > f_{c} \Rightarrow p_{\infty} = 0$, logo, não há mais uma componente gigante

Para [redes aleatórias](redes-aleatorias.md), **sob falhas aleatórias**, compartilham os mesmos expoentes críticos que uma rede de percolação dimensional-infinita: $$\gamma_{p} = 1\text{\quad\quad}\beta_{p} = 1\text{\quad\quad}\upsilon = \frac{1}{2}$$

Já em uma rede livre-de-escala, os expoentes são: $$\beta_{p} = \begin{cases} \frac{1}{3 - \gamma}\text{ se }2 < \gamma < 3 \\ \frac{1}{\gamma - 3}\text{ se }3 < \gamma < 4 \\ 1\text{ se }4 < \gamma \end{cases}\text{\quad\quad}\gamma_{p} = \begin{cases} 1\text{ se }\gamma > 3 \\ - 1\text{ se }2 < \gamma < 3 \end{cases}$$

Perceba que no regime $2 < \gamma < 3$ **sempre há uma componente gigante**. Temos também a relação da **quantidade de componentes de tamanho $s$** ($n_{s}$) $$n_{s} \propto s^{- \tau}e^{- s/s^{\ast}}$$ $$s^{\ast} \propto \vert p - p_{c}\vert ^{- \sigma}$$ $$\tau = \begin{cases} \frac{5}{2}\text{ se }\gamma > 4 \\ \frac{2\gamma - 3}{\gamma - 2}\text{ se }2 < \gamma < 4 \end{cases}$$ $$\sigma = \begin{cases} \frac{3 - \gamma}{\gamma - 2}\text{ se }2 < \gamma < 3 \\ \frac{\gamma - 3}{\gamma - 2}\text{ se }3 < \gamma < 4 \\ \frac{1}{2}\text{ se }\gamma > 4 \end{cases}$$

<a id="robustez"></a>
<a id="secao-7"></a>

## Robustez

Vimos um exemplo específico com redes quadriculadas, mas e se não seguirmos esse padrão? O que fazemos? Na verdade a ideia é bem parecida! Isso nos vai revelar um comportamento muito interessante sobre as redes livre-de-escala.

![Comparação do tamanho relativo de uma rede livre-de-escala qualquer e da rede de internet conforme removemos uma fração **aleatória** $f$ de seus nós](assets/scale-free-network-and-internet.png)

*Figura 4. Comparação do tamanho relativo de uma rede livre-de-escala qualquer e da rede de internet conforme removemos uma fração **aleatória** $f$ de seus nós*

Os gráficos acima indicam uma resistência muito forte das redes livre-de-escala contra falhas aleatórias dentro da mesma. Será que podemos encontrar um meio matemático de entender o porquê que isso acontece?

<a id="criterio-de-molloy-reed"></a>
<a id="secao-8"></a>

## Critério de Molloy-Reed

**Teorema: Critério de Molloy-Reed**

Dado que $K$ é a variável aleatória que representa o grau de um nó selecionado aleatoriamente dentro de uma rede $G(V,E)$. Para que uma componente gigante exista dentro dessa rede, ela deve satisfazer: $${\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack \geq 2$$

**Demonstração**

Para que minha rede tenha uma componente gigante, um nó **da componente** deve ter grau médio maior ou igual a $2$, já que caso contrário, quer dizer que muitos nós possuem apenas uma ou menos conexões. Defina ${\mathbb{P}}(\delta(v_{i}) = k_{i}\vert v_{i} \leftarrow > v_{j})$ como a probabilidade de que $v_{i}$ tem grau $k$ dado que ele se liga com $j$ **e $j$ está na componente gigante**. Por questões de simplificação de notação, chamemos a probabilidade antes definida como ${\mathbb{P}}(k_{i}\vert i \leftarrow > j)$. Temos que: $${\mathbb{E}}\left\lbrack K = k_{i}\vert i \leftarrow > j \right\rbrack = \sum_{k_{i}}k_{i}{\mathbb{P}}(k_{i}\vert i \leftarrow > j) \geq 2$$ Vamos calcular alguns termos. Sabemos que: $${\mathbb{P}}(k_{i}\vert i \leftarrow > j) = \frac{{\mathbb{P}}(i \leftarrow > j\vert k_{i}) \cdot {\mathbb{P}}(k_{i})}{{\mathbb{P}}(i \leftarrow > j)}$$ E também temos que: $${\mathbb{P}}(i \leftarrow > j) = \frac{\vert E\vert }{\begin{pmatrix} \vert V\vert  \\ 2 \end{pmatrix}} = {\mathbb{E}}\frac{\lbrack K\rbrack}{\vert V\vert  - 1}$$ Além de que: $${\mathbb{P}}(i \leftarrow > j\vert k_{i}) = \frac{k_{i}}{\vert V\vert  - 1}$$ Então, substituindo, vamos ter: $${\mathbb{E}}\left\lbrack K = k_{i}\vert i \leftarrow > j \right\rbrack = \sum_{k_{i}}k_{i}\frac{k_{i}p\left( k_{i} \right)}{{\mathbb{E}}\lbrack K\rbrack} = {\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack \geq 2$$

Olhando o caso específico de **redes aleatórias**, nós vamos obter que: $${\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack \geq 2 \Leftrightarrow {\mathbb{E}}\lbrack K\rbrack\frac{1 + {\mathbb{E}}\lbrack K\rbrack}{\mathbb{E}}\lbrack K\rbrack \geq 2 \Leftrightarrow {\mathbb{E}}\lbrack K\rbrack \geq 1$$

O que coincide com os resultados vistos no primeiro resumo

<a id="limite-critico"></a>
<a id="secao-9"></a>

## Limite Crítico

Vamos agora utilizar do critério visto anteriormente para entender o porquê de as redes livre-de-escala serem robustas a falhas aleatórias. Primeiro de tudo, ao remover uma fração dos nós de uma rede **aleatoriamente**, existem duas consequências:

- Altera o grau de alguns nós \[$k' \leq k$\]

- Muda a [distribuição dos graus](modelo-biaconi-barabasi.md#secao-34) \[$p_{k} \rightarrow p'_{k}'$\]

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

<a id="tolerancia-a-ataques"></a>
<a id="secao-10"></a>

## Tolerância a Ataques

Até agora, vimos apenas falhas aleatórias, na rede de internet, por exemplo, se alguns roteadores falharem aleatoriamente, a rede tem estrutura suficiente para se manter, porém, e se um ataque planejado for feito e derrubar todos os pontos com maiores conexões? Esse é o contexto que vamos analisar, em vez de retirarmos nós aleatoriamente, vamos retirar sempre os nós com **maior grau**

![Tamanho relativo do maior cluster conforme retiramos os nós seguindo o regime de falhas aleatórias e de ataques em uma rede **livre-de-escala**](assets/scale-free-network-random-failure-vs-attacks.png)

*Figura 5. Tamanho relativo do maior cluster conforme retiramos os nós seguindo o regime de falhas aleatórias e de ataques em uma rede **livre-de-escala***

Perceba que, para redes livre-de-escala, elas são **muito** mais sucetíveis a ataques direcionados. O que faz bastante sentido, já que a presença de hubs é muito marcante nesse tipo de rede.

Agora a gente gostaria de entender como que a remoção dos hubs afeta a rede e o limite para que ela colapse. Para entender isso, devemos saber que remover um hub afeta a rede de duas formas:

- Muda o grau máximo de $k_{\text{max}}$ para $k'_{\text{max}}$

- A distribuição de graus muda de $p_{k}$ para $p'_{k}'$

Lembrando que, para o problema das redes livre-de-escala, temos: $$\begin{array}{r} p_{k} = ck^{- \gamma} \\ k \in \left\{ k_{\text{min}},\ldots,k_{\text{max}} \right\} \\ c \approx \frac{\gamma - 1}{k_{\text{min}}^{- \gamma + 1} - k_{\text{max}}^{- \gamma + 1}} \end{array}$$

Após removermos a fração $f$ de nós, temos que: $$\begin{aligned} f & = {\int_{k'_{\max}}^{k}}_{\max}p_{k}dk \\ & = (\gamma - 1)k_{\text{min}}^{\gamma - 1}{\int_{k'_{\max}}^{k}}_{\max}k^{- \gamma}dk \\ & = (\gamma - 1)k_{\text{min}}^{\gamma - 1}\left\lbrack \frac{k^{1 - \gamma}}{1 - \gamma} \right\rbrack_{k'_{\text{max}}}^{k_{\text{max}}} \\ & = k_{\text{min}}^{\gamma - 1}\left( k'_{\text{max}}^{1 - \gamma} - k_{\text{max}}^{1 - \gamma} \right) \end{aligned}$$

Normalmente em redes livre-de-escala, o cutoff natural é MUITO grande ($k_{\text{max }} \gg k'_{\text{max}}$), ou seja, o termo $k_{\text{max}}^{1 - \gamma}$ é desprezível, logo, a expressão se torna: $$f \approx \left( k\frac{'_{\max}}{k_{\min}} \right)^{1 - \gamma}$$

Então chegamos na relação: $$k'_{\max} \approx k_{\min}f^{\frac{1}{1 - \gamma}}$$<a id="finding-the-cutoff"></a>

Agora vamos olhar para a segunda consequência, que é a alteração da distribuição dos graus da rede. Na absência da correlação entre os nós, vamos assumir que os links dos hubs se ligam aleatoriamente entre si. Vamos agora tentar encontrar a fração de **links** removidos da rede: $$\begin{aligned} \widetilde{f} & = \frac{\int_{k'_{\max}}^{k_{\max}}kp_{k}dk}{{\mathbb{E}}\lbrack K\rbrack} \\ & = \frac{c}{\mathbb{E}}\lbrack K\rbrack\int_{k'_{\max}}^{k_{\max}}k^{- \gamma + 1}dk \\ & = \frac{1}{\mathbb{E}}\lbrack K\rbrack \cdot \frac{1 - \gamma}{2 - \gamma} \cdot \frac{k'_{\max}^{- \gamma + 2} - k_{\max}^{- \gamma + 2}}{k_{\min}^{- \gamma + 1} - k_{\max}^{- \gamma + 2}} \end{aligned}$$

Como sabemos que o cutoff natural costuma ser muito maior, então podemos ignorar $k_{\max}$ e, usando o fato que: $${\mathbb{E}}\lbrack K\rbrack \approx \frac{\gamma - 1}{\gamma - 2}k_{\min}$$ vamos obter que: $$\widetilde{f} \approx \left( k\frac{'_{\max}}{k_{\min}} \right)^{- \gamma + 2}$$ e assim, juntando com a equação [expressão para o corte](#finding-the-cutoff), vamos obter que: $$\widetilde{f} \approx f^{\frac{2 - \gamma}{1 - \gamma}}$$ O que essa fração nos diz? Conforme $\gamma \rightarrow 2$, temos que $\widetilde{f} \rightarrow 1$, ou seja, em redes que $\gamma \approx 2$, remover uma pequena parte dos hubs já remove quase todas as arestas (O que é compatível com a teoria vista no último resumo).

Agora vamos encontrar a nova distribuição dos graus! Usando o mesmo raciocínio visto para as falhas aleatórias, vamos assumir que $K$ é a variável aleatória de um nó selecionado aleatoriamente antes de remover a fração $f$ e $K'$ após remover a fração de vértices. Sabemos que, dado que eu selecionei um vértice que tem $K = k$, ele possui exatamente $k$ vizinhos, e depois da remoção dos vértices, cada um dos vértices vizinhos ao que escolhi **pode** ou **não** sobreviver e não ser removidos (com probabilidade $1 - \widetilde{f}$), logo, temos uma soma de $k$ variáveis de bernoulli que representam quantos vizinhos meu nó tem após o ataque na rede: $$\begin{aligned} & {\mathbb{P}}(K' = k'\vert K = k) = \begin{pmatrix} k \\ k' \end{pmatrix}{\widetilde{f}}^{k - k'}\left( 1 - \widetilde{f} \right)^{k'} \\ & \Rightarrow {\mathbb{P}}(K' = k') = \sum_{k' = k_{\min}}^{k'_{\max}}{\mathbb{P}}(K = k)\begin{pmatrix} k \\ k' \end{pmatrix}{\widetilde{f}}^{k - k'}\left( 1 - \widetilde{f} \right)^{k'} \end{aligned}$$

Agora que eu tenho essas informações, posso tentar achar o critério de Molloy-Reed da rede: $$\kappa = {\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack = \frac{2 - \gamma}{3 - \gamma}k_{\min}\left( \frac{f^{\frac{3 - \gamma}{1 - \gamma} - 1}}{f^{\frac{2 - \gamma}{1 - \gamma} - 1}} \right)$$

Então consegumos chegar no limiar crítico da fração de nós $$f_{c}^{\frac{2 - \gamma}{1 - \gamma}} = 2 + \frac{2 - \gamma}{3 - \gamma}k_{\min}\left( f_{c}^{\frac{3 - \gamma}{1 - \gamma} - 1} \right)$$

Perceba que, se $\gamma \rightarrow \infty$, então $f_{c} \rightarrow 1 - \frac{1}{k_{\min} - 1}$

<a id="melhorando-a-robustez"></a>
<a id="secao-11"></a>

## Melhorando a Robustez

Certo, temos uma rede, é possível melhorar a sua tolerância, tanto a ataques, quanto a falhas aleatórias? Um primeiro pensamento que opdemos ter é conectar todos os nós periféricos em um hub, além de conectar eles entre si. Porém, na vida real, isso pode não ser aplicável, tendo em vista que, se cada aresta tem um custo para ser mantida, o custo de manutenção da rede pode exceder o viável

Da para maximizar a robustez para ataques e falhas aleatórias sem alterar o custo? Queremos aumentar o limite $f_{c}$, então temos que aumentar ${\mathbb{E}}\left\lbrack K^{2} \right\rbrack$ sem alterar o custo médio ${\mathbb{E}}\lbrack K\rbrack$. Isso vai ocorrer em uma distribuição **bimodal** onde todo nó tem grau $k_{\min}$ ou $k_{\max}$, seguindo a seguinte distribuição: $$p(k) = (1 - r)\delta(k - k_{\min}) + r\delta(k - k_{\max})$$

onde $r$ é a fração de nós com grau $k_{\max}$. Então vamos querer maximizar: $$f_{c}^{\text{tot}} = f_{c}^{\text{rand}} + f_{c}^{\text{targ}}$$

onde $f_{c}^{\text{rand}}$ é o limite crítico de falhas aleatórias e $f_{c}^{\text{targ}}$ o limite crítico dos ataques direcionados. Dado a distribuição bimodal citada anteriormente: $$\begin{aligned} {\mathbb{E}}\lbrack K\rbrack & = (1 - r)k_{\min} + rk_{\max} \\ {\mathbb{E}}\left\lbrack K^{2} \right\rbrack & = (1 - r)k_{\min}^{2} + rk_{\max}^{2} \end{aligned}$$

substituindo isso em $f_{c}^{\text{rand}}$ $$f_{c}^{\text{rand }} = 1 - \frac{1}{{\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack - 1} = \frac{{\mathbb{E}}\lbrack K\rbrack^{2} - 2rk_{\max}{\mathbb{E}}\lbrack K\rbrack - 2(1 - r){\mathbb{E}}\lbrack K\rbrack + rk_{\max}^{2}}{{\mathbb{E}}\lbrack K\rbrack^{2} - 2rk_{\max}{\mathbb{E}}\lbrack K\rbrack - (1 - r){\mathbb{E}}\lbrack K\rbrack + rk_{\max}^{2}}$$

Agora, para achar $f_{c}^{\text{targ}}$, vamos fazer uma análise mais cuidadosa $$\begin{array}{r} f_{c}^{\text{targ}} > r \Rightarrow \text{ Todos os hubs foram removidos } \\ \Rightarrow f_{c}^{\text{targ}} = r + \frac{1 - r}{{\mathbb{E}}\lbrack K\rbrack - rk_{\max}}\left( {\mathbb{E}}\lbrack K\rbrack\frac{{\mathbb{E}}\lbrack K\rbrack - rk_{\max} - 2(1 - r)}{{\mathbb{E}}\lbrack K\rbrack - rk_{\max} - (1 - r)} - rk_{\max} \right) \end{array}$$ $$\begin{array}{r} f_{c}^{\text{targ}} < r \Rightarrow \text{ Sobrou alguns hubs } \\ \Rightarrow f_{c}^{\text{targ}} = \frac{{\mathbb{E}}\lbrack K\rbrack^{2} - 2r{\mathbb{E}}\lbrack K\rbrack k_{\max} + rk_{\max}^{2} - 2(1 - r){\mathbb{E}}\lbrack K\rbrack}{k_{\max}\left( k_{\max} - 1 \right)(1 - r)} \end{array}$$

E nós estamos procurando o valor de $k$ que maximiza $f_{c}^{\text{tot}}$. Usando as equações encontradas para $f_{c}^{\text{targ}}$ e $f_{c}^{\text{rand}}$, descobrimos que podemos aproximar $k_{\max}$ por: $$\begin{aligned} k_{\max} & \approx Ar^{- \frac{2}{3}} \\ A & = \left\lbrack \frac{2\left( {\mathbb{E}}\lbrack K\rbrack \right)^{2}\left( {\mathbb{E}}\lbrack K\rbrack - 1 \right)^{2}}{2{\mathbb{E}}\lbrack K\rbrack - 1} \right\rbrack^{\frac{1}{3}} \end{aligned}$$

então obtemos que, para $r$ pequeno: $$f_{c}^{\text{tot }} = 2 - \frac{1}{{\mathbb{E}}\lbrack K\rbrack - 1} - \frac{3{\mathbb{E}}\lbrack K\rbrack}{A^{2}}r^{\frac{1}{3}} + O\left( r^{\frac{2}{3}} \right)$$

Para uma rede com $N$ nós, o máximo de $f_{c}^{\text{tot}}$ ocorre com $r = \frac{1}{N}$ $$\Rightarrow k_{\max} = AN^{\frac{2}{3}}$$ ou seja, em redes em que apenas $1$ nó possui grau $k_{\max}$ enquanto o resto possui $k_{\min}$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/ciencia-de-redes/a2.md) · [Apresentação e contexto da fonte](../../trilhas/ciencia-de-redes/a2.md#apresentacao-original)

- Anterior: [Correlação de Graus](correlacao-de-graus.md)
