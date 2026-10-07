---
title: "Combinatória"
tags:
  - probabilidade
  - a1
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A1.typ"
trilha: "../../trilhas/probabilidade/a1.md"
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 1
nav_exclude: true
render_with_liquid: false
---

[Probabilidade](index.md)

<!-- wiki:original:inicio -->
<a id="secao-1"></a>

# Combinatória

<a id="secao-2"></a>

## Contagem

A probabilidade é muito derivada do conceito de contar todas as saídas possíveis de um experimento/teste, por conta disso, é **fundamental** que fiquemos **craques** em contagem. A contagem é uma ferramenta que nos permite organizar e estruturar as possibilidades de um experimento, e assim, calcular a probabilidade de um evento ocorrer (depois vemos como fazer isso). O importante agora é entendermos os principais princípios dessa área da matemática.

**Teorema: Princípio Fundamental da Contagem**

Dada uma decisão $D_{1}$ com $x$ escolhas, e uma decisão **consecutiva** $D_{2}$ com $y$ escolhas, de forma que cada decisão $x$ tomada tem $y$ opções disponíveis, o número total de maneiras de realizar ambas as decisões é $x \cdot y$.

**Demonstração**

Vamos demonstrar por *indução*. Para uma única etapa (caso base), existem exatamente $a_{1}$ opções. Suponha que para $n$ etapas, o número de maneiras de realizar todas as decisões seja $a_{1} \cdot \ldots \cdot a_{n}$. Agora vamos adicionar uma nova decisão $D_{n + 1}$ com $a_{n + 1}$ escolhas. Se visualizarmos as primeiras $n$ decisões como uma única decisão com $a_{1} \cdot \ldots \cdot a_{n}$ possibilidades, então o número total de maneiras de realizar todas as decisões é $\left( a_{1} \cdot \ldots \cdot a_{n} \right) \cdot a_{n + 1} = a_{1} \cdot \ldots \cdot a_{n} \cdot a_{n + 1}$, como queríamos demonstrar.

Isso nos tráz uma estratégia de abordagem de problemas bem definida

- **Postura**: Sempre colocar no papel o que se sabe e o que se quer, e tentar organizar as informações de forma a facilitar a visualização do problema.

- **Divisãu**: Sempre que possível, dividir o problema em subproblemas menores, e resolver cada um deles separadamente.

- **Não adiar dificuldades**: Se uma das decisões a serem tomadas for mais restrita que as demais, esta deve ser tomada primeiro, para que as demais decisões possam ser tomadas com mais liberdade.

<a id="secao-3"></a>

## Permutação

Usamos a permutação para saber de quantas maneiras podemos organizar um conjunto de elementos de forma ordenada.

**Definição: Permutação de elementos **distintos****

Se temos $n$ elementos distintos, o número de maneiras de organizá-los em uma sequência ordenada é dado por

$$
P_{n} = n! = n \cdot (n - 1) \cdot \ldots \cdot 2 \cdot 1
$$

**Exemplo**

Quantos anagramas existem na palavra *“VIDRO”*? A palavra *“VIDRO”* possui 5 letras distintas, então o número de anagramas é $5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120$.

Mas essa situação é um pouco mais complicada quando temos elementos repetidos, como na palavra *“MAMÃO”*. Nesse caso, temos 5 letras, mas a letra *“A”* se repete 2 vezes.

**Definição: Permutação de elementos **distintos****

Se temos $n$ elementos, dos quais $n_{1}$ são idênticos, $n_{2}$ são idênticos, …, $n_{k}$ são idênticos, o número de maneiras de organizá-los em uma sequência ordenada é dado por

$$
P_{n}^{n_{1},n_{2},\ldots,n_{k}} = \frac{n!}{n_{1}! \cdot n_{2}! \cdot \ldots \cdot n_{k!}}
$$

Vamos tentar pensar no porquê dessa fórmula! Imagina que eu tenho uma palavra qualquer, e nela eu tenho DUAS letras repetidas. Se eu fixo uma das letras em um lugar, a outra letra pode ir para qualquer posição da palavra. No entanto, se eu fixo a segunda letra, a primeira **também** pode ir para qualquer posição, e eu acabo contando as **mesmas** palavras duas vezes. Por exemplo:

$$
\mathbf{A}BCA \rightarrow ABC\mathbf{A}
$$

 mesma palavra, mas com as posições do $A$ trocadas, logo, foi contabilizada duas vezes. Se eu tivesse $3$ letras repetidas, eu teria contado a mesma palavra $3!$ vezes, e assim por diante. Por isso, para corrigir isso, eu divido pelo fatorial do número de letras repetidas.

**Exemplo**

Quantos anagramas existem na palavra *“MAMÃO”*? A palavra *“MAMÃO”* possui 5 letras, das temos $2$ letras *“A”* e $2$ letras *“M”* repetidas, então o número de anagramas é

$$
P_{5}^{2,2} = \frac{5!}{2! \cdot 2!} = \frac{120}{2 \cdot 2} = 30
$$

<a id="secao-4"></a>

## Arranjos

Dado um grupo de $n$ elementos, eu quero selecionar $k$ elementos distintos e organizá-los em uma sequência ordenada, de forma que, ao trocar a ordem dos elementos, eu obtenha uma **sequência diferente**. Por exemplo, se eu quiser saber, dentro dos meus **competidores**, quantas combinações possívels de **primeiro**, **segundo** e **terceiro** lugar existem, se eu troco o **primeiro** pelo **segundo**, então vira uma sequência diferente, e portanto, é um arranjo diferente.

**Definição: Arranjo de tamanho $k$ para $n$ elementos**

O arranjjo de tamanho $k$ para $n$ elementos distintos é dado por

$$
A_{n}^{k} = n(n - 1)\ldots(n - k + 1) = \frac{n!}{(n - k)!}
$$

Por que seria essa fórmula? Bom, se eu tenho $n$ elementos, para o primeiro elemento da sequência eu tenho $n$ opções. Para o segundo elemento, eu já usei um elemento, então eu tenho $n - 1$ opções. Para o terceiro elemento, eu já usei dois elementos, então eu tenho $n - 2$ opções. E assim por diante, até que eu tenha escolhido $k$ elementos. Então, o número total de maneiras de escolher e organizar esses $k$ elementos é dado pelo produto $n(n - 1)\ldots(n - k + 1)$.

<a id="secao-5"></a>

## Combinações

Dado um grupo de $n$ elementos, eu quero selecionar $k$ elementos distintos, mas agora a ordem não importa. Por exemplo, se eu quero saber a combinação de ingredientes para o meu sanduíche, se eu coloco o **hamburguer** antes do **queijo**, ou o **queijo** antes do **alface**, isso não faz diferença nenhuma.

**Definição: Combinação de $n$ elementos escolhendo $k$**

O número de combinações de $n$ elementos distintos escolhendo $k$ elementos é dado por

$$
C_{n}^{k} = \frac{n!}{k! \cdot (n - k)!} = \frac{A_{n}^{k}}{k!} = \begin{pmatrix} n \\ k \end{pmatrix}
$$

A lógica aqui é montarmos justamente o arranjo anterior, primeiro calculamos de quantas formas podemos organizar $k$ elementos onde a **ordem** influencia na contagem. Depois disso, queremos compensar as contagens extras que realizamos, ou seja, se eu tenho $k$ elementos, eu posso organizá-los de $k!$ formas diferentes, e todas essas formas são a mesma combinação. Então, para compensar isso, dividimos pelo fatorial de $k$.

Existe uma propriedade muito interessante que podemos usar para calcular combinações, ela mostra que, se eu quero escolher um grupo de $k$ elementos de um conjunto de $n$ elementos, o número de maneiras de fazer isso é o mesmo que escolher $n - k$ elementos do mesmo conjunto. Ou seja, $C_{n}^{k} = C_{n}^{n - k}$.

<a id="combination-simetry"></a>

**Teorema**

$$
C_{n}^{k} = C_{n}^{n - k}
$$

**Demonstração**

Queremos mostrar que

$$
\begin{pmatrix} n \\ k \end{pmatrix} = \begin{pmatrix} n \\ n - k \end{pmatrix}
$$

 vamos desenvolver ambos os lados

$$
\begin{pmatrix} n \\ k \end{pmatrix} = \frac{n!}{k!(n - k)!}
$$

$$
\begin{pmatrix} n \\ n - k \end{pmatrix} = \frac{n!}{(n - k)!\left( n - (n - k) \right)!} = \frac{n!}{k!(n - k)!}
$$

<a id="secao-6"></a>

## Permutação Circular

De quantas formas podemos organizar $n$ elementos distintos em um círculo? Para isso usamos a permutação circular.

**Definição: Permutação circular de $n$ elementos**

A permutação circular de $n$ elementos distintos é dada por

$$
P_{n}^{\text{circ }} = (n - 1)!
$$

Para entender melhor a lógica vamos para um exemplo. Suponha que eu tenho $5$ pessoas, $A$, $B$, $C$, $D$ e $E$. Vamos agora organizar elas em um circulo.

$$
A \rightarrow B \rightarrow C \rightarrow D \rightarrow E \rightarrow A
$$

 perfeito! Mas e se eu organizar elas assim?

$$
B \rightarrow C \rightarrow D \rightarrow E \rightarrow A \rightarrow B
$$

 percebe que é a mesma organização, só que com outro ponto de referência? Então, para cada permutação linear de $n$ elementos, existem $n$ permutações circulares equivalentes. Por isso, para calcular a permutação circular, dividimos a permutação linear por $n$, ou seja, $P_{n}^{\text{circ }} = \frac{P_{n}}{n} = \frac{n!}{n} = (n - 1)!$.

<a id="secao-7"></a>

## Ferramentas de Contagem

Daqui a pouco, vamos definir melhor uma definição ingênua sobre probabilidade, mas de antemão, ela envolve **a contagem de todas as possibilidades que um experimento pode ter**. no mundo real, é impossível contar todas as saídas possíveis de um experimento na mão, mas isso não é um problema! Mesmo quando as saídas de um **experimento** são **numerosas** e **complexas de se contar na mão**, ainda podemos utilizar algumas ferramentas na área da contagem para nos ajudar a calcular as possibilidades!

<a id="secao-8"></a>

### Tabela Amostral

A tabela amostral é muito útil para organizar **quais ferramentas** de contagem utilizamos sob **determinadas condições** de um **experimento**.

|  |  |  |
|:--:|:--:|:--:|
|  | Ordem Importa | Ordem não Importa |
| Reposição | $n^{k}$ | $\begin{pmatrix} n + k - 1 \\ k \end{pmatrix}$ |
| Sem Reposição | $\frac{n!}{(n - k)!}$ | $\begin{pmatrix} n \\ k \end{pmatrix}$ |

Antes de explicar a origem de cada fórmula, vou enunciar as **restrições** associadas à cada fórmula

- **Ordem Importa**: A ordem dos elementos escolhidos influencia na contagem, ou seja, se eu escolher os elementos $a$ e $b$, a sequência $(a,b)$ é diferente da sequência $(b,a)$.

- **Ordem não Importa**: A ordem dos elementos escolhidos não influencia na contagem, ou seja, se eu escolher os elementos $a$ e $b$, a sequência $(a,b)$ é igual à sequência $(b,a)$.

- **Reposição**: Cada elemento escolhido volta para o conjunto de elementos disponíveis, ou seja, posso escolher o mesmo elemento mais de uma vez.

- **Sem Reposição**: Cada elemento escolhido não volta para o conjunto de elementos disponíveis, ou seja, não posso escolher o mesmo elemento mais de uma vez.

<a id="secao-9"></a>

#### Ordem Importa e Reposição

Se a ordem importa, então estamos lidando com arranjos. Se há reposição, então para cada elemento escolhido, ele volta para o conjunto de elementos disponíveis, ou seja, na primeira retirada, eu tenho $n$ elementos disponíveis, na segunda, eu ainda tenho $n$ pois o anterior foi colocado de volta, e assim por diante. Logo, o número de maneiras de escolher $k$ elementos com reposição é dado por $n^{k}$.

<a id="secao-10"></a>

#### Ordem Importa e Sem Reposição

Estamos lidando literalmente com os arranjos como já vimos antes, então será a mesma fórmula do arranjo, ou seja, $\frac{n!}{(n - k)!}$.

<a id="secao-11"></a>

#### Ordem não Importa e Sem Reposição

É exatamente o caso da combinação padrão que discutimos anteriormente, ou seja, $\begin{pmatrix} n \\ k \end{pmatrix}$.

<a id="secao-12"></a>

#### Ordem não Importa e Reposição

Esse caso é um pouco mais complicado. Você saber de quantas formas possíveis você pode escolher $k$ elementos de um conjunto de $n$ elementos, mas agora você pode escolher o mesmo elemento mais de uma vez, isso é equivalente a **perguntar de quantos jeitos diferentes é possível distribuir $k$ partículas independentes em $n$ caixas diferentes**, mas por quê? Isso não parece nada intuitivo.

Interprete uma associação, cada partícula é um **sorteio** e cada caixa é um **elemento do conjunto**. Quando eu falo **partícula $i$ vai ficar na caixa $p$**, isso quer dizer em termos do sorteio que, no $i$-ésimo sorteio, o elemento escolhido foi o $p$-ésimo elemento do conjunto. Então, se eu tenho $k$ partículas e $n$ caixas, isso é equivalente a dizer que eu tenho $k$ sorteios e $n$ elementos disponíveis para escolher. Como eu posso escolher um mesmo elemento mais de uma vez, isso é equivalente a dizer que eu posso colocar mais de uma partícula na mesma caixa. Para fazer o cálculo de fato, utilizamos a abordagem de pontos e traços, tenha em mente a seguinte divisão

$$
\cdot \cdot \cdot / \cdot / \cdot \cdot \cdot / \cdot / \cdot
$$

 Essa representação é o mesmo que dizer que na primeira caixa, eu tenho $3$ partículas, na segunda eu tenho $1$ e assim em diante, a quantidade de pontos entre os traços representa a quantidade de partículas em cada caixa. Como temos $k$ partículas, temos $k$ pontos, e como temos $n$ caixas, temos $n - 1$ traços. Logo, o número total de maneiras de organizar esses pontos e traços vai ser o número de maneiras de escolher $k$ pontos dentre todos os $k + n - 1$ elementos, ou seja, $\begin{pmatrix} n + k - 1 \\ k \end{pmatrix}$.

<a id="secao-13"></a>

### Identidades Úteis

Mesmo com as ferramentas de contagem que vimos antes, existem diversas situações complexas na área que ainda exigem certas **sacadas**. As identidades que vamos mostrar são **justamente essas sacadas**.

<a id="choice-of-leader"></a>

**Teorema**

$$
n\begin{pmatrix} n - 1 \\ k - 1 \end{pmatrix} = k\begin{pmatrix} n \\ k \end{pmatrix}
$$

**Demonstração**

Queremos saber de quantas formas podemos escolher $k$ pessoas de um grupo de $n$ pessoas, e dentre essas $k$ pessoas, queremos escolher uma pessoa para ser o **líder**.

No lado direito da igualdade, quando fazemos

$$
k\begin{pmatrix} n \\ k \end{pmatrix}
$$

 primeiro fazemos a contagem de quantas formas podemos escolher $k$ pessoas de um grupo de $n$ pessoas (combinação) e, dentro dessas $k$, quantas podem ser o **líder**.

Já no lado esquerdo, quando fazemos

$$
n\begin{pmatrix} n - 1 \\ k - 1 \end{pmatrix}
$$

 primeiro eu vou escolher o **líder** do grupo dentre as $n$ pessoas, e das $n - 1$ que sobraram, eu vou montar um grupo de $k - 1$ para completar $k$ com o líder que eu escolhi.

**Teorema: Identidade de Vandermonde**

$$
\begin{pmatrix} m + n \\ k \end{pmatrix} = \sum_{j = 0}^{k}\begin{pmatrix} m \\ j \end{pmatrix}\begin{pmatrix} n \\ k - j \end{pmatrix}
$$

**Demonstração**

Eu quero escolher $k$ pessoas de um grupo de $m + n$ pessoas. Eu posso dividir esse grupo em dois subgrupos, um com $m$ pessoas e outro com $n$ pessoas. Depois disso, posso dividir em duas etapas, primeiro eu escolho $j$ pessoas do grupo de $m$ pessoas, e depois eu escolho $k - j$ pessoas do grupo de $n$ pessoas, assim completo um grupo de $k$ pessoas. Como $j$ pode variar de $0$ até $k$, eu somo todas as possibilidades, e assim obtenho a **Identidade de Vandermonde**.

<a id="secao-14"></a>

## Contagem do Complementar

Essa técnica parece até boba, mas muitas vezes deixamos passar situações que são mais fáceis de serem resolvidas quando pensamos no **complementar** do que queremos. Essa estratégia consiste em, se eu não sei como calcular o total de possibilidades de uma situação específica, eu posso tentar calcular o da situação **oposta**. Por exemplo, eu quero saber de quantas formas possíveis, dentro de uma sala com $n$ pessoas, existem pelo menos $2$ pessoas com o mesmo aniversário. Calcular isso diretamente é bem difícil, no entanto, o complementar é muito fácil, que é **de quantas formas eu garanto que todos tem um dia diferente de aniversário**, que se resume a aplicar uma combinação de $n$ nos $365$ dias do ano. Dessa forma, calcular de quantas formas eu posso garantir que pelo menos $2$ pessoas tem o mesmo aniversário é muito mais fácil, pois é só fazer $365^{n} - \begin{pmatrix} 365 \\ n \end{pmatrix}$
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../trilhas/probabilidade/a1.md#apresentacao-original)

- Próximo: [Primeiros passos em Probabilidade](primeiros-passos-em-probabilidade.md)
