---
layout: "default"
title: "Melhorando um Estimador"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 20
---

[Inferência Estatística](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-20"></a>

# Melhorando um Estimador

------------------------------------------------------------------------

Como diz o título, nesse capítulo a gente tem como objetivo aprender a dizer quando um estimador é “bom”. Eu coloquei bom entre aspas pois, dando um certo spoiler, as vezes um estimador pode ser relativamente bom, e podemos nos contentar com ele, porém podem existir estimadores melhores

Primeiro de tudo, vamos definir nossa amostra $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ e ela tem uma pdf ou uma pmf $f\left( \underline{x}\vert \theta \right)$. Também vamos definir a esperança em $\theta$ como: $${\mathbb{E}}_{\theta}\lbrack Z\rbrack = \int_{- \infty}^{\infty}\ldots\int_{- \infty}^{\infty}g\left( \underline{x} \right)f\left( \underline{x}\vert \theta \right)dx_{1}\ldots dx_{n}$$ Onde, nesse caso, $Z = g\left( X_{1},\ldots,X_{n} \right)$ (E $f\left( \underline{x}\vert \theta \right)$ é uma pdf). Vale ressaltar também que, se $\theta$ é uma variável aleatória, ${\mathbb{E}}_{\theta}\lbrack Z\rbrack = {\mathbb{E}}\left\lbrack Z\vert \theta \right\rbrack$. Essas informações que eu dei foram apenas para contextualizar o nosso próximo objetivo (Ué, vai falar o próximo objetivo sem nem terminar o principal? É que a gente vai entender o principal a partir desse daqui)

O nosso objetivo agora (A partir dele a gente vai entender o principal que citei antes) é tentar estimar o valor de $h(\theta)$ (Estimar uma função qualquer de $\theta$). Show! Então a gente quer um estimador que seja bem próximo e o erro dele em relação a $h(\theta)$ é baixo. Vamos então tomar uma função de perca pra comparar eles dois! Vamos usar a clássima: $$L(\theta,a) = (\theta - a)^{2}$$ A **perca quadrática**. Então a gente quer um estimador que, ao longo prazo, faça com que essa perca seja pequena. Então faz sentido a gente ver a esperança desse erro com relação ao valor do $\theta$ $$R(\theta,\delta) = {\mathbb{E}}_{\theta}\left\lbrack L\left( h(\theta),\delta(\underline{X}) \right) \right\rbrack = {\mathbb{E}}_{\theta}\left\lbrack \left( h(\theta) - \delta(\underline{X}) \right)^{2} \right\rbrack$$ Macho, o que diabos isso significa? Só pra refrescar, tirar a esperança de uma variável é tipo saber qual valor ela mais vai retornar ao longo prazo. Então faz sentido a gente pegar o valor que esse erro vai me retornar ao longo prazo (Dado um valor de $\theta$) pra poder fazer comparações depois com outros estimadores.

**Definição: Risco**

Dada uma variável aleatória $X$ com uma distribuição indexada pelo parâmetro $\theta$ e uma amostra dela $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$, o risco de um estimador $\delta(\underline{X})$ de $h(\theta)$ é: $$R\left( h(\theta),\delta(\underline{X}) \right) = {\mathbb{E}}_{\theta}\left\lbrack L\left( h(\theta),\delta(\underline{X}) \right) \right\rbrack$$ Onde $L(x,y)$ é uma função de perca arbitrária

Se a gente não sabe uma distribuição priori de $\theta$, então a gente quer encontrar um estimador que faça com que a perca $L(\theta,\delta)$ seja pequena para todo valor de $\theta$ ou pelo menos para uma grande parte.

Dado esse contexto, a gente vai mostrar que, se um estátistico $A$ tem acesso a $X_{1},\ldots,X_{n}$ e o $B$ tem acesso a uma estatística $T$, se $A$ tenta estimar $h(\theta)$ usando $\delta(\underline{X})$, então o nosso mano $B$ consegue encontrar um outro estimador $\delta_{0}\left( \underline{X} \right)$ usando somente a estatística $T$ que ele é melhor ou tão bom quanto o estimador do $A$, ou em termos matemáticos: $$R\left( \theta,\delta_{0} \right) \leq R(\theta,\delta)$$

A gente vai definir o estimador do mano $B$ como: $$\delta_{0}\left( \underline{T} \right) = {\mathbb{E}}_{\theta}\left\lbrack \delta(\underline{X})\vert T \right\rbrack$$

Eu sei que parece que eu to colocando a carroça na frente dos bois ja entregando de bandeja qual é o estimador, mas a gente vai mostrar que esse carinha bate a descrição que eu comentei antes. Mas antes de tudo, a gente tem que saber se esse cara ao menos pode ser usado como estimador de $\theta$. Pra isso, ele não pode depender de $\theta$ (Afinal, não faz sentido estimar uma coisa usando ela mesma).

A gente sabe que $f\left( x_{1},\ldots,x_{n}\vert T,\theta \right) = f\left( x_{1},\ldots,x_{n}\vert T \right)$, então pra qualquer valor de $T$, eu vou ter que: $$\begin{aligned} {\mathbb{E}}_{\theta}\left\lbrack \delta(\underline{X})\vert T \right\rbrack & = \int_{- \infty}^{\infty}\ldots\int_{- \infty}^{\infty}\delta(\underline{x})f\left( \underline{x}\vert T,\theta \right)dx_{1}\ldots dx_{n} \\ & = \int_{- \infty}^{\infty}\ldots\int_{- \infty}^{\infty}\delta(\underline{x})f\left( \underline{x}\vert T \right)dx_{1}\ldots dx_{n} \end{aligned}$$

Ou seja, $\delta_{0}(T)$ não depende de $\theta$, então eu posso usar ele como estimador de $\theta$

Uma coisa que vale ressaltar, eu vou fazer um teorema que mostra essa propriedade, porém eu vou denotar a estatística suficiente como $\underline{T} = \left( T_{1},\ldots,T_{n} \right)$, de forma que $T_{i}$ são estatísticas conjuntamente suficientes (Elas sozinhas não dizem nada, porém, a união de todas elas forma uma estatística suficiente. Todos os teoremas que vimos anteriormente que usam estatísticas suficientes valem também para esse caso vetorial)

<a id="best-estimator-theorem"></a>

**Teorema**

Se $\delta(\underline{X})$ é um estimador e $\underline{T}$ uma estatística conjuntamente suficiente para $\theta$ e $\delta_{0}\left( \underline{T} \right) = {\mathbb{E}}_{\theta}\left\lbrack \delta(\underline{X})\vert \underline{T} \right\rbrack$, então vale que: $$R\left( \theta,\delta_{0} \right) \leq R(\theta,\delta)\text{\quad\quad}\forall\theta \in \Omega$$

**Demonstração**

Se $R(\theta,\delta)$ é infinito pra algum $\theta$, então a condição já é satisfeita ($\infty \leq \infty$)

Então vamos considerar que $R(\theta,\delta)$ é finito. Pela definição de variância, temos que: $${\mathbb{E}}_{\theta}\left\lbrack \left( \delta(\underline{X}) - \theta \right)^{2}\vert \underline{T} \right\rbrack \geq \left( {\mathbb{E}}_{\theta}\left\lbrack \delta(\underline{X}) - \theta\vert \underline{T} \right\rbrack \right)^{2}$$ Se esse passo deixou confusa, use a propriedade ${\mathbb{V}}\lbrack X\rbrack = {\mathbb{E}}\left\lbrack X^{2} \right\rbrack + \left( {\mathbb{E}}\lbrack X\rbrack \right)^{2}$ em $${\mathbb{V}}_{\theta}\left\lbrack \delta(\underline{X}) - \theta\vert \underline{T} \right\rbrack$$ Continuando, vamos ter que: $${\mathbb{E}}_{\theta}\left\lbrack \left( \delta(\underline{X}) - \theta \right)^{2}\vert \underline{T} \right\rbrack \geq \left( {\mathbb{E}}_{\theta}\left\lbrack \delta(\underline{X})\vert \underline{T} \right\rbrack - \theta \right)^{2}$$ Aplicando a esperança em relação a $\theta$ novamente em ambos os lados, pela Lei de Adão (${\mathbb{E}}\left\lbrack {\mathbb{E}}\left\lbrack X\vert Y \right\rbrack \right\rbrack = {\mathbb{E}}\lbrack X\rbrack$), temos que: $$\begin{array}{r} {\mathbb{E}}_{\theta}\left\lbrack \left( \delta(\underline{X}) - \theta \right)^{2} \right\rbrack \geq {\mathbb{E}}_{\theta}\left\lbrack \left( \delta(\underline{X})\vert \underline{T}\rbrack - \theta \right)^{2} \right\rbrack \\ {\mathbb{E}}_{\theta}\left\lbrack \left( \delta(\underline{X}) - \theta \right)^{2} \right\rbrack \geq {\mathbb{E}}_{\theta}\left\lbrack \delta_{0}\left( \underline{T} \right) - \theta)^{2} \right\rbrack \end{array}$$

Podemos criar uma definição interessante também:

**Definição: Estimador Admissível, Inadmissível e Dominante**

Suponha que $R(\theta,\delta)$ é definida utilizando a função de perca quadrática. Então dizemos que um estimador $\delta$ é **inadmissível** se existe um outro estimador $\delta_{0}$ tal que $R\left( \theta,\delta_{0} \right) \leq R(\theta,\delta)$ para todo valor $\theta \in \Omega$ e **existe a relação de desigualdade pra pelo menos 1 valor de $\theta$**. Se essas condições são satisfeitas, dizemos que o estimador $\delta_{0}$ **domina** o estimador $\delta$. Um estimador é **admissível** quando nenhum outro estimador o domina

Essa definição parece meio complicadinha, mas ela traz uma implicação bem fácil de entender. Um estimador $\delta$ que **não é** uma função de uma estatística suficiente $T$ apenas **deve ser inadmissível**. Além do fato que o teorema [\[best-estimator-theorem\]](#best-estimator-theorem) mostra explicitamente um estimador melhor que $\delta$. Na prática isso costuma ser menos útil já que nem sempre calcular $\delta_{0}$ é uma tarefa fácil

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Limitações de uma Estatística Suficiente](limitacoes-de-uma-estatistica-suficiente/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Critério de Fatoração](../estatistica-suficiente/criterio-de-fatoracao/index.md)
- Próximo: [Limitações de uma Estatística Suficiente](limitacoes-de-uma-estatistica-suficiente/index.md)
