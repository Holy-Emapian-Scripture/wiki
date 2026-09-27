---
layout: "default"
title: "Conjunto de Ponto Flutuante — Aritmética de Ponto Flutuante"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 40
---

[Álgebra Linear Numérica](../../index.md) · [Aritmética de Ponto Flutuante](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-46"></a>

# Conjunto de Ponto Flutuante

O conjunto de números que um computador pode entender e representar é chamado de **Conjunto de Ponto Flutuante**. O livro nos dá uma definição bem complicada, então vou te dar uma mais simples e, depois, entender a definição do livro:

**Definição: Definição Simples**

Um **Conjunto de Ponto Flutuante** é definido como: $$F = \left\{ \pm 0,d_{1}d_{2.}..d_{t} \ast \beta^{e}/e \in {\mathbb{Z}} \right\}$$ Onde $0,d_{1.}..d_{t}$ é a **mantissa**, $t \in {\mathbb{N}}^{\ast}$ é a **precisão** da mantissa, $\beta \in {\mathbb{N}}(\beta \geq 2)$ é a base, $d_{j}\left( 0 \leq d_{j} < \beta \right)$ são os dígitos da mantissa e $e \in {\mathbb{Z}}$ é o **expoente**. Em computadores, **nós** definimos um intervalo para $t$, $e$ e uma base específica $\beta$

Vamos analisar tudo. Primeiro, definimos tudo, mas o que e por que defini essas coisas?

<a id="secao-47"></a>

## Mantissa

É o núcleo de um número, um número nesse conjunto tem apenas uma mantissa, mas uma mantissa pode estar associada a vários números, por exemplo, podemos representar $1$ no sistema decimal como $0,1 \ast 10$ e podemos representar 10 como $0,1 \ast 10^{2}$, isso significa que a mesma mantissa pode representar muitos números. É importante dizer que a mantissa é sempre escrita na base $\beta$, veremos o que isso significa agora

<a id="secao-48"></a>

## Base e Precisão

**Definição**

Se temos $x \in {\mathbb{R}}$, escrever $x$ na base $\beta$ significa escolher coeficientes $\ldots,\alpha_{- 1},\alpha_{0},\alpha_{1},\ldots$ com $0 \leq \alpha_{j} < \beta$ e $\alpha_{j}$ são inteiros tais que: $$x = \ldots + \alpha_{2}\beta^{2} + \alpha_{1}\beta^{1} + \alpha_{0}\beta^{0} + \alpha_{- 1}\beta^{- 1} + \alpha_{- 2}\beta^{- 2} + \ldots$$ Então escrevemos $x$ na base $\beta$ como $\ldots\alpha_{2}\alpha_{1}\alpha_{0},\alpha_{- 1}\alpha_{- 2}\ldots_{\beta}$, onde cada $\alpha_{j}$ é um dígito

Essa é uma maneira de representar cada número real, mas o computador é limitado a uma certa quantidade de $\alpha_{j}$, ele não pode armazenar, por exemplo, 1 bilhão de $\alpha_{j}$, é aí que entra a precisão, ela diz ao computador quantos dígitos a mantissa pode representar!

Espere… mas vimos que a mantissa só armazena números após a *”,”*, então como o conjunto representa números maiores que 1? É aí que entra o **expoente**

<a id="secao-49"></a>

## Expoente

O expoente indica a ordem do nosso número, por exemplo, com uma mantissa $0,d_{1}d_{2}d_{3}$, podemos representar 4 números diferentes: $0,d_{1}d_{2}d_{3}$, $d_{1},d_{2}d_{3}$, $d_{1}d_{2},d_{3}$, $d_{1}d_{2}d_{3}$, eles têm expoentes $0,1,2$ e $3$, respectivamente. Mas, se eu tenho uma mantissa $0,d_{1.}..d_{t}$, por que multiplicá-la por $\beta^{e}$ move a vírgula por $e$ dígitos? (Só para fazer um paralelo, é exatamente assim que nosso sistema decimal funciona, se você tem $0,1$, multiplicá-lo por 10 dá $1$)

**Teorema**

Se você tem $x$ escrito na base $\beta$, multiplicá-lo por $\beta^{e}$ moverá a vírgula, na notação da base $\beta$, $e$ dígitos para a direita

**Demonstração**

$$x = \ldots + \alpha_{2}\beta^{2} + \alpha_{1}\beta^{1} + \alpha_{0}\beta^{0} + \alpha_{- 1}\beta^{- 1} + \alpha_{- 2}\beta^{- 2} + \ldots$$ $$\Leftrightarrow \beta^{e}x = \left( \ldots + \alpha_{2}\beta^{2} + \alpha_{1}\beta^{1} + \alpha_{0}\beta^{0} + \alpha_{- 1}\beta^{- 1} + \alpha_{- 2}\beta^{- 2} + \ldots \right)\beta^{e}$$ $$\Leftrightarrow \beta^{e}x = \ldots + \alpha_{2}\beta^{2}\beta^{e} + \alpha_{1}\beta^{1}\beta^{e} + \alpha_{0}\beta^{0}\beta^{e} + \alpha_{- 1}\beta^{- 1}\beta^{e} + \alpha_{- 2}\beta^{- 2}\beta^{e} + \ldots$$ $$\Leftrightarrow \beta^{e}x = \ldots + \alpha_{2}\beta^{e + 2} + \alpha_{1}\beta^{e + 1} + \alpha_{0}\beta^{e} + \alpha_{- 1}\beta^{e - 1} + \alpha_{- 2}\beta^{e - 2} + \ldots$$ Observe como todos os $\alpha_{j}$ moveram $e$ dígitos para a esquerda, isso significa que a vírgula move $e$ dígitos para a direita

Vamos analisar um exemplo para entender melhor:

**Exemplo**

Criei uma máquina que representa meus números por um conjunto de ponto flutuante $F$ com base decimal ($\beta = 10$), precisão $3$ e $e \in \lbrack - 5,5\rbrack$, responda estas perguntas:

1.  Qual é o menor número positivo que $F$ pode representar?

    Bem, se $F$ tem precisão 3, minha mantissa é assim: $$0,d_{1}d_{2}{d_{3}}_{\beta}$$ Então, se queremos o mínimo, precisamos tornar $d_{j}$ o menor possível, mas ainda diferente de $0$, isso significa que fazemos o último dígito ($d_{3}$) igual a 1 e o resto igual a $0$, isso significa que a menor mantissa que podemos ter é: $$0,001$$ Mas ainda podemos representar um número maior usando o expoente, o menor expoente que temos é $- 5$, isso significa que o menor número positivo que esse conjunto pode representar é $$0,001 \ast 10^{- 5} = 0,00000001$$

2.  Qual é o maior número positivo que $F$ pode representar?

    Seguindo a mesma lógica, a maior mantissa que podemos ter é: $$0,999$$ Usando o maior expoente possível, o maior número que nosso conjunto pode representar é: $$0,999 \ast 10^{5} = 99900$$

3.  O número -3921 está no conjunto?

    Vamos testar, se o decompusermos: $$- 3921 = - 0,3921 \ast 10^{4}$$ O expoente está no intervalo $\lbrack - 5,5\rbrack$, mas a mantissa tem precisão $4$, isso significa que $- 3921$ **NÃO ESTÁ NO CONJUNTO $F$**

4.  O número 738000000 está no conjunto?

    Decompondo, temos: $738000000 = 0,738 \ast 10^{9}$, como podemos ver, a mantissa tem a precisão desejada, mas o expoente é maior que o intervalo dado, isso significa que 738000000 **NÃO ESTÁ NO CONJUNTO $F$**

Agora que entendemos essa definição de conjunto de ponto flutuante, vamos ver a definição do livro:

**Definição: Definição do Livro**

Sendo $F \subset {\mathbb{R}}$, definimos como: $$F = \left\{ \pm \left( \frac{m}{\beta^{t}} \right)\beta^{e} \right\}$$ Onde $t$, $e$ e $\beta$ significam a mesma coisa com as mesmas restrições da definição anterior

Qual é a diferença e por que o livro define assim? Há apenas uma grande diferença aqui: Por que ele está definindo a **mantissa** como $\frac{m}{\beta^{t}}$? Lembre-se de quando provamos que, se escrevemos $x$ na base $\beta$ e multiplicamos $x$ por $\beta^{e}$, a vírgula move $e$ dígitos para a direita? O mesmo se aplica se $e < 0$, mas a vírgula vai para a esquerda, e por que estou dizendo isso? Porque, o que o livro não nos diz, é que escrevemos $m$ **NA BASE $\beta$**, e essa divisão por $\beta^{t}$ faz com que obtenhamos apenas os primeiros $t$ dígitos do número, significando que obtemos apenas os dígitos que desejamos, SÓ ISSO (Sim, o livro explica isso mal)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Aritmética de Ponto Flutuante](../index.md)
- Próximo: [Números não em $F$](../numeros-nao-em-f/index.md)
