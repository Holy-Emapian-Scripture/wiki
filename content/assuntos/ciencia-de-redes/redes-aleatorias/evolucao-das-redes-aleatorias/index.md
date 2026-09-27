---
layout: "default"
title: "Evolução das Redes Aleatórias — Redes Aleatórias"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A1.md"
trilha: "../../../../trilhas/ciencia-de-redes/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 5
---

[Ciência de Redes](../../index.md) · [Redes Aleatórias](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Evolução das Redes Aleatórias

Conforme iniciamos um grafo com um grau médio $0$ e vamos aumentando ele aos poucos, nós percebemos que a partir de um ponto chave, os nós começam a se agrupar em algo que chamamos de **componente gigante**, que seria a maior componente conexa da rede.

![Gráfico que mostra a fração de nós dentro de uma grande componente conexa em função do grau médio](../../assets/mean-degree-and-big-component-fraction.png)

*Figura 3. Gráfico que mostra a fração de nós dentro de uma grande componente conexa em função do grau médio*

Quanto $\hat{k} < 1$, então a quantidade de nós na componente gigante é desprezível em relação à quantidade de nós na rede, porém, a partir de $\hat{k} = 1$, isso indica que temos, pelo menos, $\frac{n}{2}$ componentes conexas, o que já começa a fazer uma diferença no gráfico. Esse é um argumento utilizado por Erdös e Renyi em um paper por eles publicado

**Teorema: Ponto Crítico**

Temos uma componente gigante $\Leftrightarrow$ ${\mathbb{E}}\lbrack K\rbrack \geq 1$

**Demonstração**

Dado uma rede $G(V,E)$, vamos definir a fração de nós que **não está** na componente gigante como: $$u = 1 - \frac{N_{G}}{\vert V\vert }$$

De forma que $N_{G}$ é a quantidade de nós dentro dessa componente gigante, vamos definir essa componente como $\Psi \subseteq V$. Se um nó $v_{i} \in \Psi$, então ele deve estar interligado com outro nó $v_{j}$, que também deve satisfazer $v_{j} \in \Psi$. Por isso, se $v_{i} \notin \Psi$, então isso pode ocorrer por duas razões:

- $\left\{ v_{i},v_{j} \right\} \notin E$. A probabilidade de isso acontecer é $1 - p$

- $\left\{ v_{i},v_{j} \right\} \in E$, porém $v_{j} \notin \Psi$. A probabilidade de isso acontecer é $pu$

Então temos: $${\mathbb{P}}(v_{i} \notin \Psi) = 1 - p + pu$$

Então a probabilidade de que $v_{i}$ não esteja linkado a $\Psi$ por qualquer nó é de $(1 - p + pu)^{\vert V\vert  - 1}$, já que temos outros $\vert V\vert  - 1$ nós que poderiam fazer com que $v_{i}$ se interligasse a componente gigante.

Sabemos que $u$ é a fração de nós que não está em $\Psi$, para qualquer $p$ e $\vert V\vert$, a solução da equação <!-- Expressão matemática vazia no original. --> $$u = (1 - p + pu)^{\vert V\vert  - 1}$$

nos dá o tamanho da componente gigante por meio de $N_{G} = \vert V\vert (1 - u)$. Usando $p = \frac{\hat{k}}{\vert V\vert  - 1}$ e tirando $\log$ de ambos os lados, para $\hat{k} \ll \vert V\vert$ (Grau médio **muito** menor que $\vert V\vert$), obtemos: $$\begin{array}{r} \ln(u) \approx \left( \vert V\vert  - 1 \right)\ln\left\lbrack 1 - \frac{\hat{k}}{\vert V\vert  - 1}(1 - u) \right\rbrack \\ \text{Tiramos exponencial e obtemos: } \\ u \approx \exp\left\{ - \frac{\hat{k}}{1 - u} \right\} \end{array}$$

Se denotarmos $S = \frac{N_{G}}{\vert V\vert }$, obtemos que: $$S = 1 - e^{- \hat{k} \cdot S}$$

Agora obtemos o tamanho da componente gigante em função do **grau médio**. O ponto crítico ocorre na mudança de fase do sistema (Tópico mais complicado que não compreendo, estou apenas falando o que o livro do Barabas fala), que é quando os dois lados da igualdade tem a mesma derivada, então: $$\begin{aligned} \frac{d}{dS}\left( 1 - e^{\hat{k}S} \right) & = 1 \\ \hat{k}e^{- \hat{k}S} = 1 \end{aligned}$$ Onde, colocando $S = 0$, descobrimos que o ponto crítico é $\hat{k} = 1$

Na verdade esse resultado é bem intuitivo. Faz sentido dizer que para que uma componente gigante exista, todos os nós precisam ter pelo menos grau 1, já que eles precisam estar conectados com algum outro nó, porém, o que não é muito intuitivo, é que todos eles terem grau 1 é **suficiente** para que a componente gigante apareça

A gente pode reescrever ${\mathbb{E}}\lbrack K\rbrack = 1$ como: $${\mathbb{E}}\lbrack K\rbrack = 1 \Leftrightarrow p(N - 1) = 1 \Leftrightarrow p = \frac{1}{N - 1} \approx N$$ E o que isso significa? Isso mostra outro resultado intuitivo. Quanto maior é minha rede, **menos probabilidade eu preciso para que uma componente gigante apareça**

Algo interessante que podemos fazer é analisar como a proporção $\frac{N_{G}}{N}$ (Porcentagem de nós dentro da componente gigante) se comporta conforme nós aumentamos ${\mathbb{E}}\lbrack K\rbrack$. Nós fazemos isso dividindo esse processo em 4 fases (Ou 4 **regimes**), veja a imagem abaixo:

![Crescimento da compoente conexa em função do grau médio](../../assets/network-evolution.png)

*Figura 4. Crescimento da compoente conexa em função do grau médio*

<a id="secao-6"></a>

## Regime Subcrítico ($0 < \hat{k} < 1$)

Quando $\hat{k} = 0$, temos $N$ nós soltos na rede e conforme aumentamos $\hat{k}$, mas mantemos ele menor que $1$, temos a formação de vários nós soltos e pequenos agrupamentos (Coisa pouca mesmo). Dessa forma, mesmo escolhendo a componente gigante como o maior desses agrupamentos, a proporção $N_{G}/N$ ainda vai ser muito baixa. O Barabás aproxima essa relação como $$\frac{N_{G}}{N} \approx \frac{\ln(N)}{N} \rightarrow 0\text{ quando }N \rightarrow \infty$$ Pois podemos considerar essas componentes menores como várias árvores (Também pequenas)

<a id="secao-7"></a>

## Ponto Crítico

É a transição do momento onde não há uma componente gigante para o momento que há uma. Porém o tamanho relativo dela ($N_{G}/N$) ainda é muito próximo de $0$. O livro do Barabás afirma que $N_{G} \approx N^{\frac{2}{3}}$, então $N_{G}$ cresce muito mais devagar se comparado a $N$, logo: $$\frac{N_{G}}{N} \approx N^{- \frac{1}{3}} = O(N)$$

Porém, perceba que o salto de diferença de tamanho pode ser enorme dependendo da rede. Se pegarmos uma rede de tamanho $N = 7 \times 10^{9}$ (Parecido com a rede mundial), para $\hat{k} < 1$, a gente teria que o tamanho da componente gigante era de ordem: $$N_{G} \approx \ln(N) \approx 22.7$$ Em contraste, se $\hat{k} = 1$, então teriamos que $$N_{G} \approx N^{\frac{2}{3}} \approx 3 \times 10^{6}$$ Que é uma diferença notável no tamanho das componentes gigantes

<a id="secao-8"></a>

## Regime Supercrítico ($\hat{k} > 1$)

Esse regime tem mais relevância para redes reais, já que a componente gigante começa a se parecer realmente com uma rede. Aqui, o tamanho $N_{G}$ pode ser dado como: $$N_{G} = \left( p - p_{c} \right)N$$ Onde $p_{c} = 1/(N)$. Ou seja, conforme eu aumentar meu grau médio, menor vai ficar meu $p$ e maior será a fração de nós que pertencem à componente gigante. Em resumo, nesse regime, várias componentes conexas coexistem junto da componente gigante, onde a componente gigante é uma rede comum, enquanto as outras componentes conexas são mais prováveis de serem árvores

<a id="secao-9"></a>

## Regime Conexo ($\hat{k} > \ln(N)$)

Agora, nesse regime, temos que o grafo é (ou quase) conexo, logo, todos os nós fazem parte da componente conexa (Ou a maioria, logo $N_{G} \approx N$)

**Teorema**

Se $N_{G} \approx N$, o valor de $\hat{k}$ que satisfaz a propriedade de **a maior parte dos nós estarem na componente gigante** é: $$\hat{k} = \ln(N) \Rightarrow p = \frac{\ln(N)}{N}$$

**Demonstração**

Para determinar o valor de $\hat{k}$ no qual a maior parte dos nós fazem parte da componente gigante, temos que saber a probabilidade de que um **nó aleatório não tenha um link para a componente gigante**, e isso é: $$(1 - p)^{N_{G}} \approx (1 - p)^{N}$$ Já que eu tenho exatamente $N_{G}$ nós na componente gigante e eu não quer me ligar com nenhum deles. Novamente, tomando ${\mathbb{I}}_{k}$ sendo a variável indicadora de que um nó $k$ **não** na componente gigante ($1$ quando ele não está), temos que a **quantidade de nós que não estão na componente gigante** tem uma distribuição **binomial** com parâmetros $N$, $(1 - p)^{N}$, então, se considerarmos $L_{G}$ sendo essa quantidade, temos que: $${\mathbb{E}}\left\lbrack L_{G} \right\rbrack = {N(1 - p)}^{N} = {N\left( 1 - \frac{Np}{N} \right)}^{N} \approx Ne^{- Np}$$ Queremos então chegar no ponto em que temos, para um $p$ suficientemente próximo de $1$, que apenas 1 único nó esteja fora da componente conexa, então gostaríamos de analisar em que ponto: $${\mathbb{E}}\left\lbrack L_{G} \right\rbrack = 1 \Leftrightarrow Ne^{- Np} = 1$$ Logo, tirando $\ln$ em ambos os lados, chegamos que: $$p = \frac{\ln(N)}{N}$$ Ou seja $$\hat{k} = \ln(N)$$

Esse resultado é de grande impacto! Quando analisamos muitas das redes reais, a maioria segue esse padrão de $\hat{k} = \ln(N)$, logo, as **redes reais são supercríticas**. Veja a tabela presente no livro do Barabás:

| **Rede** | **N** | **L** | ${\mathbb{E}}\lbrack K\rbrack$ | $\ln(N)$ |
|----|----|----|----|----|
| Internet | $192244$ | $609066$ | $6.34$ | $12.17$ |
| Power Grid | $4,941$ | $6,594$ | $2.67$ | $8.51$ |
| Science Collaboration | $23,133$ | $94,437$ | $8.08$ | $10.05$ |
| Actor Network | $702,388$ | $29,397,908$ | $83.71$ | $13.46$ |
| Protein Interactions | $2,018$ | $2,930$ | $2.90$ | $7.61$ |

Tabela de redes no Barabás

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Anterior: [Ideia Inicial](../ideia-inicial/index.md)
- Próximo: [Distribuição de tamanhos de Cluster](../distribuicao-de-tamanhos-de-cluster/index.md)
