---
title: "Probabilidade Condicional"
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
ordem_na_trilha: 3
nav_exclude: true
render_with_liquid: false
---

[Probabilidade](index.md)

<!-- wiki:original:inicio -->
<a id="secao-22"></a>

# Probabilidade Condicional

<a id="secao-23"></a>

## Como o Conhecimento influencia na Probabilidade

Em probabilidade, conseguimos utilizar conhecimento do que aconteceu agora no nosso experimento para entender as chances dos eventos que estão para acontecer.

**Exemplo**

Ao jogarmos um dado justo $2$ vezes, dado que eu sei que a soma de ambos os valores que caíram é $6$, mas não sei qual o valor de cada lançamento, qual é a probabilidade de que o primeiro valor seja $2$? Sabemos que a soma de ambos os valores que caíram é $6$, então o espaço amostral é reduzido para

$$
(1,5),(2,4),(3,3),(4,2),(5,1)
$$

 dentro das possibilidades, a probabilidade vai ser

$$
{\mathbb{P}}(primeiro\ valor\ é\ 2\ ~\vert ~soma\ é\ 6) = \frac{1}{5}
$$

**Exemplo**

Jogamos uma moeda $100$ vezes, mas não sabemos se ela é viciada ou não. Sabemos que, se a moeda for justa, nós deveríamos observar uma proporção de $1/2$ para o número de caras e coroas. No entanto, suponha que nós observamos $70$ caras e $30$ coroas. Isso faz parecer que essa moeda **está viciada** de alguma forma. Essa informação passada me faz crer que a chance do meu lançamento agora, não é mais $1/2$.

**Definição: Probabilidade Condicional**

Dado um espaço amostral $S$ e dois eventos $A,B \subseteq S$, a probabilidade de $A$ ocorrer dado que $B$ ocorreu é dada por

$$
{\mathbb{P}}(A~\vert ~B) = \frac{{\mathbb{P}}(A \cap B)}{{\mathbb{P}}(B)}
$$

**Exemplo**

Voltando no exemplo do dado com soma $6$, vamos separar o problema em dois eventos para aplicar a definição de probabilidade condicional. Seja $A$ o evento de que o primeiro valor seja $2$, e seja $B$ o evento de que a soma dos valores seja $6$. Então, temos que

$$
{\mathbb{P}}(B) = \frac{5}{36}\quad{\mathbb{P}}(A \cap B) = \frac{1}{36}
$$

 então aplicando a definição:

$$
{\mathbb{P}}(A~\vert ~B) = \frac{{\mathbb{P}}(A \cap B)}{{\mathbb{P}}(B)} = \frac{\frac{1}{36}}{\frac{5}{36}} = \frac{1}{5}
$$

<a id="secao-24"></a>

## Independência

Agora que enunciamos o conceito de condicionamento e como **saber** de um evento influencia na probabilidade de outro, podemos formalizar melhor a definição de independência. Quando dizemos que um evento não influencia na probabilidade de outro, isso nos indica que, **se eu sei do resultado do evento $A$**, isso não me dá **nenhuma informação** sobre o resultado do evento $B$. Ou seja, a probabilidade de $B$ ocorrer **não muda** se eu sei que $A$ ocorreu. Formalizando isso, temos a seguinte definição.

**Definição: Eventos Independentes**

Dois eventos $A$ e $B$ são independentes quando

$$
{\mathbb{P}}(A \cap B) = {\mathbb{P}}(A) \cdot {\mathbb{P}}(B)
$$

Ué, a definição que eu falei não parece ter muito a ver com o que eu acabei de escrever, mas na verdade, ela tem sim!

**Teorema**

Se $A$ e $B$ são independentes, então

$$
{\mathbb{P}}(A~\vert ~B) = {\mathbb{P}}(A)
$$

**Demonstração**

Pela definição:

$$
{\mathbb{P}}(A~\vert ~B) = \frac{{\mathbb{P}}(A \cap B)}{{\mathbb{P}}(B)}
$$

 Como são independentes:

$$
{\mathbb{P}}(A~\vert ~B) = \frac{{\mathbb{P}}(A) \cdot {\mathbb{P}}(B)}{{\mathbb{P}}(B)} = {\mathbb{P}}(A)
$$

Assim, conseguimos formalizar a ideia de **não fornecimento de informação** de um evento sobre outro.

Outro conceito importante que podemos formalizar é que a probabilidade de **dois eventos ocorrerem** simultaneamente é a mesma que a probabilidade de **um evento ocorrer dado que o outro ocorreu** multiplicado pela probabilidade do **outro evento ocorrer**.

<a id="intersection-and-conditional-equality"></a>

**Teorema**

$$
{\mathbb{P}}(A \cap B) = {\mathbb{P}}(A~\vert ~B) \cdot {\mathbb{P}}(B) = {\mathbb{P}}(B~\vert ~A) \cdot {\mathbb{P}}(A)
$$

**Demonstração**

Sabemos que ${\mathbb{P}}(A \cap B) = {\mathbb{P}}(B \cap A)$, manipulando então a definição de probabilidade condicional, temos que

$$
{\mathbb{P}}(A\vert B) = \frac{{\mathbb{P}}(A \cap B)}{{\mathbb{P}}(B)} \Leftrightarrow {\mathbb{P}}(A \cap B) = {\mathbb{P}}(A~\vert ~B) \cdot {\mathbb{P}}(B)
$$

 da mesma forma:

$$
{\mathbb{P}}(B\vert A) = \frac{{\mathbb{P}}(B \cap A)}{{\mathbb{P}}(A)} \Leftrightarrow {\mathbb{P}}(B \cap A) = {\mathbb{P}}(B~\vert ~A) \cdot {\mathbb{P}}(A)
$$

É o que mermão? Qual que é a lógica disso? Imagine que nós **sabemos** que um evento $A$ ocorreu, se sabemos que $A$ ocorreu, qual seria a probabilidade que, dentro do universo de $A$, o evento $B$ ocorra também? No entanto, para que isso aconteça, precisamos que $A$ ocorra também, logo, pelo princípio da multiplicação, precisamos múltiplicar ambas as probabilidades (queremos que as representar a chance dos **dois** eventos ocorrerem), ambas que são dadas justamente por

$$
{\mathbb{P}}(B~\vert ~A) \cdot {\mathbb{P}}(A)
$$

<a id="secao-25"></a>

## Lei da Probabilidade Total

A lei da probabilidade total mostra como podemos representar a probabilidade de um evento $B$ ocorrer em função da sua chance de acontecer sob a perspectiva da ocorrência de outros eventos disjuntos no **mesmo espaço amostral**.

<a id="law-of-total-probability"></a>

**Teorema: Lei da Probabilidade Total**

Sejam $A_{1},A_{2},\ldots,A_{n}$ eventos disjuntos $2$ a $2$, ou seja, $A_{i} \cap A_{j} = \varnothing$ para $i \neq j$ e $\bigcup_{i = 1}^{n}A_{i} = S$ onde $S$ é o espaço amostral, então para qualquer evento $B$, desde que ${\mathbb{P}}(A_{i})$ e ${\mathbb{P}}(B\vert A_{i})$ existam e sejam conhecidos, temos que

$$
{\mathbb{P}}(B) = \sum_{i = 1}^{n}{\mathbb{P}}(B~\vert ~A_{i}) \cdot {\mathbb{P}}(A_{i})
$$

**Demonstração**

$$
\begin{aligned} {\mathbb{P}}(B) & = {\mathbb{P}}(B \cap S) \\ & = {\mathbb{P}}(B \cap \left( A_{1} \cup A_{2} \cup \ldots \cup A_{n} \right)) \\ & = {\mathbb{P}}(\left( B \cap A_{1} \right) \cup \left( B \cap A_{2} \right) \cup \ldots \cup \left( B \cap A_{n} \right)) \\ & = {\mathbb{P}}(B \cap A_{1}) + {\mathbb{P}}(B \cap A_{2}) + \ldots + {\mathbb{P}}(B \cap A_{n}) \\ & = {\mathbb{P}}(B~\vert ~A_{1}) \cdot {\mathbb{P}}(A_{1}) + \ldots + {\mathbb{P}}(B~\vert ~A_{n}) \cdot {\mathbb{P}}(A_{n}) \end{aligned}
$$

Como podemos ver isso de forma intuitiva? Para uma explicação intuitiva, acesse esse vídeo: [PREENCHER — link pendente na origem]

Esse teorema é muito útil quando temos informações sobre outros eventos, mas não temos sobre o evento objetivo que gostaríamos de conhecer.

**Exemplo**

Suponha que eu queira saber a probabilidade de uma pessoa ter câncer, mas eu não tenho essa informação. No entanto, eu sei que a pessoa é fumante, e que a probabilidade de uma pessoa ter câncer **dado** que ela é fumante é $0.1$, e que a probabilidade de uma pessoa ter câncer dado que ela não é fumante é $0.01$. Além disso, eu sei que a probabilidade de uma pessoa ser fumante é $0.2$. Então, podemos calcular a probabilidade de uma pessoa ter câncer utilizando a lei da probabilidade total:

$$
\begin{array}{r} {\mathbb{P}}(\text{câncer}) = {\mathbb{P}}(\text{câncer }~\vert ~\text{fumante}) \cdot {\mathbb{P}}(\text{fumante}) + {\mathbb{P}}(\text{câncer }~\vert ~\text{não fumante}) \cdot {\mathbb{P}}(\text{não fumante}) \\ = 0.1 \cdot 0.2 + 0.01 \cdot 0.8 = 0.02 + 0.008 = 0.028 \end{array}
$$

Conseguimos expandir esse teorema para o caso de múltiplas condições, mas antes de fazer isso, vamos enunciar um teorema que vai nos ajudar a fazer isso.

<a id="conditional-probability-is-a-probability"></a>

**Teorema: Equivalência probabilística do condicionamento**

A função $\widetilde{\mathbb{P}}(A) = {\mathbb{P}}(A\vert E)$ com $E$ sendo um evento possível qualquer, é uma probabilidade.

**Demonstração**

Para que a função seja uma probabilidade, ela precisa estar sujeita aos axiomas da probabilidade, ou seja, ela precisa satisfazer as seguintes condições:

1.  $\widetilde{\mathbb{P}}(S) = 1$

2.  $\widetilde{\mathbb{P}}(A) \geq 0$

3.  $\widetilde{\mathbb{P}}(\bigcup_{j = 1}^{n}A_{j}) = \sum_{j = 1}^{n}\widetilde{\mathbb{P}}(A_{j})$

**Provando $\widetilde{\mathbb{P}}(S) = 1$**: Se sabemos que o evento $E$ ocorreu, então nosso espaço amostral é reduzido para **todos os eventos em que $E$ ocorreu**, ou seja, o nosso espaço amostral vira $E$.

$$
\widetilde{\mathbb{P}}(E) = {\mathbb{P}}(E\vert E) = \frac{{\mathbb{P}}(E \cap E)}{{\mathbb{P}}(E)} = \frac{{\mathbb{P}}(E)}{{\mathbb{P}}(E)} = 1
$$

**Provando $\widetilde{\mathbb{P}}(A) \geq 0$**: Pela definição de probabilidade condicional, temos que

$$
\widetilde{\mathbb{P}}(A) = {\mathbb{P}}(A\vert E) = \frac{{\mathbb{P}}(A \cap E)}{{\mathbb{P}}(E)}
$$

 como a função de cima e a de baixo são maiores que $0$, a divisão inteira será maior que $0$.

**Provando $\widetilde{\mathbb{P}}(\bigcup_{j = 1}^{n}A_{j}) = \sum_{j = 1}^{n}\widetilde{\mathbb{P}}(A_{j})$**: Pela definição de probabilidade condicional, temos que

$$
\begin{aligned} \widetilde{\mathbb{P}}(\bigcup_{j = 1}^{n}A_{j}) & = {\mathbb{P}}(\bigcup_{j = 1}^{n}A_{j}~\vert ~E) \\ & = \frac{{\mathbb{P}}(\left( \bigcup_{j = 1}^{n}A_{j} \right) \cap E)}{{\mathbb{P}}(E)} \\ & = \frac{{\mathbb{P}}(\bigcup_{j = 1}^{n}\left( A_{j} \cap E \right))}{{\mathbb{P}}(E)} \\ & = \frac{\sum_{j = 1}^{n}{\mathbb{P}}(A_{j} \cap E)}{{\mathbb{P}}(E)} \\ & = \sum_{j = 1}^{n}\frac{{\mathbb{P}}(A_{j} \cap E)}{{\mathbb{P}}(E)} \\ & = \sum_{j = 1}^{n}\widetilde{\mathbb{P}}(A_{j}) \end{aligned}
$$

Com esse teorema, podemos expandir a lei da probabilidade total

**Teorema: Lei da Probabilidade Total com Condicionamento Extra**

Sejam $A_{1},A_{2},\ldots,A_{n}$ eventos disjuntos $2$ a $2$, ou seja, $A_{i} \cap A_{j} = \varnothing$ para $i \neq j$ e $\bigcup_{i = 1}^{n}A_{i} = S$ onde $S$ é o espaço amostral, então para qualquer evento $B$ e $E$, desde que ${\mathbb{P}}(A_{i}\vert E)$ e ${\mathbb{P}}(B\vert A_{i} \cap E)$ existam e sejam conhecidos, temos que

$$
{\mathbb{P}}(B~\vert ~E) = \sum_{i = 1}^{n}{\mathbb{P}}(B~\vert ~A_{i} \cap E) \cdot {\mathbb{P}}(A_{i}~\vert ~E)
$$

**Demonstração**

Pelo [teorema da probabilidade condicional](#conditional-probability-is-a-probability), podemos renomear $\widetilde{\mathbb{P}}(B) = {\mathbb{P}}(B\vert E)$, então podemos aplicar a lei da probabilidade total para essa função, ou seja, temos que

$$
\begin{array}{r} \widetilde{\mathbb{P}}(B) = \sum_{i = 1}^{n}\widetilde{\mathbb{P}}(B~\vert ~A_{i}) \cdot \widetilde{\mathbb{P}}(A_{i}) \\ \Leftrightarrow \\ {\mathbb{P}}(B~\vert ~E) = \sum_{i = 1}^{n}{\mathbb{P}}(B~\vert ~A_{i} \cap E) \cdot {\mathbb{P}}(A_{i}~\vert ~E) \end{array}
$$

Esse teorema nos permite utilizar a lei da probabilidade total em problemas mais complexos e com mais restrições.

**Exemplo: Qual a chance de vir vermelha?**

Considere duas urnas diferentes

$$
\begin{array}{r} A_{1} = \ 3\ bolas\ vermelhas\ e\ 1\ azul\  \\ A_{2} = \ 1\ bola\ vermelha\ e\ 3\ azuis\ \end{array}
$$

 Uma das urnas é escolhida ao acaso, e uma bola é retirada da urna escolhida com

$$
{\mathbb{P}}(A_{1}) = {\mathbb{P}}(A_{2}) = 0.5
$$

 em seguida, retiramos duas bolas da urna escolhida **sem reposição**. Queremos saber então qual é a **probabilidade** de que do valor da segunda bola dado o da primeira. Por exemplo

$$
\begin{array}{r} V_{1} = \text{ primeira bola é vermelha } \\ V_{2} = \text{ segunda bola é vermelha } \end{array}
$$

 quero saber então

$$
{\mathbb{P}}(V_{2}~\vert ~V_{1}) = {\mathbb{P}}(V_{2}~\vert ~V_{1},A_{1}) \cdot {\mathbb{P}}(A_{1}~\vert ~V_{1}) + {\mathbb{P}}(V_{2}~\vert ~V_{1},A_{2}) \cdot {\mathbb{P}}(A_{2}~\vert ~V_{1})
$$

 calcular apenas ${\mathbb{P}}(V_{2}~\vert ~V_{1})$ é difícil, mas se condicionarmos em **qual urna nós tiramos a bola**, conseguimos calcular facilmente. Vamos calcular as probabilidades termo a termo.

$$
{\mathbb{P}}(V_{2}~\vert ~V_{1},A_{1}) = \frac{2}{3}\quad{\mathbb{P}}(V_{2}~\vert ~V_{1},A_{2}) = \frac{0}{1}
$$

 o primeiro pois, se estamos na primeira urna, e já tiramos uma bola vermelha, restam $2$ bolas vermelhas e $1$ azul, logo a chance de tirar uma vermelha é de $\frac{2}{3}$. Já na segunda urna, se já tiramos a única bola vermelha, não há mais bolas vermelhas, logo a chance de tirar uma vermelha é de $0$. Como a segunda deu $0$, nem precisamos calcular ${\mathbb{P}}(A_{2}~\vert ~V_{1})$. Agora, vamos calcular ${\mathbb{P}}(A_{1}~\vert ~V_{1})$, para isso, vamos usar o [teorema de Bayes](#bayes-theorem):

$$
{\mathbb{P}}(A_{1}~\vert ~V_{1}) = \frac{{\mathbb{P}}(V_{1}~\vert ~A_{1}) \cdot {\mathbb{P}}(A_{1})}{{\mathbb{P}}(V_{1}~\vert ~A_{1}) \cdot {\mathbb{P}}(A_{1}) + {\mathbb{P}}(V_{1}~\vert ~A_{2}) \cdot {\mathbb{P}}(A_{2})} = \frac{\frac{3}{4} \cdot 0.5}{\frac{3}{4} \cdot 0.5 + \frac{1}{4} \cdot 0.5} = \frac{3}{4}
$$

 logo, temos que

$$
{\mathbb{P}}(V_{2}~\vert ~V_{1}) = \frac{2}{3} \cdot \frac{3}{4} + 0 \cdot \frac{1}{4} = \frac{1}{2}
$$

<a id="secao-26"></a>

## O Teorema de Bayes

Suponha que esteja acontecendo a suspeita de um possível **futuro** surto de malária no Rio de Janeiro, e que o governo está preocupado com a situação. Para isso, eles vão realizar um teste de malária em toda a população da cidade, mas o teste não é perfeito! Acontece que meu resultado deu positivo, isso quer dizer que tenho malária? Será que agora eu vou morrer? A verdade é bem mais tranquilizante, e o **teorema de bayes** no mostra essa relação.

<a id="bayes-theorem"></a>

**Teorema: Teorema de Bayes**

Sejam $A$ e $B$ dois eventos, então temos que

$$
{\mathbb{P}}(A~\vert ~B) = \frac{{\mathbb{P}}(B~\vert ~A) \cdot {\mathbb{P}}(A)}{{\mathbb{P}}(B)}
$$

**Demonstração**

Aplicando o [teorema da interseção e da probabilidade condicional](#intersection-and-conditional-equality), temos que

$$
{\mathbb{P}}(A\vert B) = \frac{{\mathbb{P}}(A \cap B)}{{\mathbb{P}}(B)} = \frac{{\mathbb{P}}(B~\vert ~A) \cdot {\mathbb{P}}(A)}{{\mathbb{P}}(B)}
$$

Vamos considerar, no contexto do nosso problema, que

- Apenas $1\%$ da população tem malária

- O teste acerta $99\%$ dos doentes

- O teste acerta $99\%$ dos saudáveis

Analisando rapidamente, se o teste der positivo, isso parece falar que **a chance de eu ter malária é de $99\%$**, mas isso **não é verdade**. A minha primeira fala se refere à seguinte probabilidade:

$$
{\mathbb{P}}(\text{Positivo}\vert \text{Doente}) = 0.99
$$

 No entanto, meu exame deu positivo e eu não sei se estou mesmo doente ou não, logo, a probabilidade que eu quero saber é

$$
{\mathbb{P}}(\text{Doente}\vert \text{Positivo})
$$

 pelo [teorema de Bayes](#bayes-theorem), temos que

$$
{\mathbb{P}}(\text{Doente}\vert \text{Positivo}) = \frac{{\mathbb{P}}(\text{Positivo}\vert \text{Doente}) \cdot {\mathbb{P}}(\text{Doente})}{{\mathbb{P}}(\text{Positivo})} = \frac{0.99 \cdot 0.01}{{\mathbb{P}}(\text{Positivo})}
$$

 para calcular ${\mathbb{P}}(\text{Positivo})$, usamos o [teorema da lei da probabilidade total](#law-of-total-probability), mas ela diz que podemos expressar essa probabilidade como

$$
\begin{aligned} {\mathbb{P}}(\text{Positivo}) & = {\mathbb{P}}(\text{Positivo}\vert \text{Doente}) \cdot {\mathbb{P}}(\text{Doente}) + {\mathbb{P}}(\text{Positivo}\vert \text{Saudável}) \cdot {\mathbb{P}}(\text{Saudável}) \\ & = 0.99 \cdot 0.01 + 0.01 \cdot 0.99 = 0.0198 \end{aligned}
$$

 voltando para a fórmula anterior

$$
{\mathbb{P}}(\text{Doente}\vert \text{Positivo}) = \frac{0.99 \cdot 0.01}{0.0198} = 0.5
$$

 então se eu sei que meu teste deu positivo, na verdade, a chance de eu ter malária é de apenas $50\%$, e não $99\%$ como parecia inicialmente. Isso é um exemplo clássico de como o Teorema de Bayes nos ajuda a atualizar nossas previsões com base em informações novas.

<a id="secao-27"></a>

### Falácia do Promotor

Um caso muito famoso onde essa confusão teve consequências graves, foi o caso de *Sally Clark*. Em $1999$, ela estava sendo julgada pelo assassinato de seus dois bebês, que morreram de *Síndrome da Morte Súbita Infantil*.

![Sally Clark](assets/A1/sally.png)

*Figura 2. Sally Clark*

O promotor do caso alegou que a probabilidade de duas crianças morrerem de *Síndrome da Morte Súbita Infantil* na mesma família era de $1$ em $73$ milhões, e que isso provava que ela era culpada. No entanto, essa alegação foi baseada em uma falácia estatística, pois não considerou outros fatores, como histórico familiar, condições de saúde e outros fatores de risco. Resumidamente, ele confundiu

$$
{\mathbb{P}}(\text{Evidência}\vert \text{Inocência})
$$

 com

$$
{\mathbb{P}}(\text{Inocência}\vert \text{Evidência})
$$

 Anos depois a condenação foi anulada. Diversos estatísticos apontaram que houve uso incorreto de probabilidade no julgamento.

<a id="secao-28"></a>

## Armadilhas
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../trilhas/probabilidade/a1.md) · [Apresentação e contexto da fonte](../../trilhas/probabilidade/a1.md#apresentacao-original)

- Anterior: [Primeiros passos em Probabilidade](primeiros-passos-em-probabilidade.md)

- Próximo: [Variáveis Aleatórias Discretas](variaveis-aleatorias-discretas.md)
