---
layout: "default"
title: "Bernoulli Mixture Models — Gaussian and Bernoulli Mixture Models"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 14
---

[Aprendizado de Máquina](../../index.md) · [Gaussian and Bernoulli Mixture Models](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-14"></a>

# Bernoulli Mixture Models

Agora que vimos os GMMs e como derivar o algoritmo de resolução do problema, que tal analisarmos o caso de variáveis com distribuições discretas? Vamos considerar o caso de variáveis binárias, que podem ser modeladas com distribuições de Bernoulli. Esse modelo também é conhecido como **Análise de Classe Latentes**

**Definição: Vetor Bernoulli**

Considere um conjunto de $D$ variáveis aleatórias binárias $X = \left\{ x_{1},x_{2},\ldots,x_{D} \right\}$, onde cada variável $x_{i}$ segue uma distribuição de Bernoulli com parâmetro $\mu_{i}$, ou seja, ${\mathbb{P}}(x_{i} = 1) = \mu_{i}$ e ${\mathbb{P}}(x_{i} = 0) = 1 - \mu_{i}$. O vetor aleatório $x$ é chamado de vetor Bernoulli e sua função de probabilidade conjunta é dada por: $$p\left( x\vert \mu \right) = \prod_{i = 1}^{D}\mu_{i}^{x_{i}}\left( 1 - \mu_{i} \right)^{1 - x_{i}}$$ onde $x \in {\mathbb{R}}^{D}$ e $\mu \in {\mathbb{R}}^{D}$

**Teorema: Validade da distribuição**

Seja $p\left( x\vert \mu \right)$ um Modelo de Mistura de Bernoulli. Então, $p\left( x\vert \mu \right)$ é uma distribuição de probabilidade válida, ou seja, $p\left( x\vert \mu \right) \geq 0$ para todo $x$ e $\sum_{x \in \left\{ 0,1 \right\}^{D}}p\left( x\vert \mu \right) = 1$.

**Demonstração**

Para mostrar que $p\left( x\vert \mu \right) \geq 0$, note que cada termo na multiplicação é não-negativo, pois $\mu_{i}^{x_{i}} \geq 0$ e $\left( 1 - \mu_{i} \right)^{1 - x_{i}} \geq 0$. Portanto, $p\left( x\vert \mu \right) \geq 0$ para todo $x$.

Para mostrar que a soma de $p\left( x\vert \mu \right)$ sobre todos os possíveis vetores binários de dimensão $D$ é igual a 1, usamos a propriedade da distribuição de Bernoulli: $$\sum_{x \in \left\{ 0,1 \right\}^{D}}p\left( x\vert \mu \right) = \sum_{x \in \left\{ 0,1 \right\}^{D}}\prod_{i = 1}^{D}\mu_{i}^{x_{i}}\left( 1 - \mu_{i} \right)^{1 - x_{i}}$$ Como cada termo na multiplicação é independente dos outros termos, podemos reescrever a soma como um produto de somas: $$= \prod_{i = 1}^{D}\sum_{x_{i} \in \left\{ 0,1 \right\}}\mu_{i}^{x_{i}}\left( 1 - \mu_{i} \right)^{1 - x_{i}}$$ Cada soma interna é igual a 1, pois: $$\sum_{x_{i} \in \left\{ 0,1 \right\}}\mu_{i}^{x_{i}}\left( 1 - \mu_{i} \right)^{1 - x_{i}} = \mu_{i} + \left( 1 - \mu_{i} \right) = 1$$ Portanto, temos: $$\sum_{x \in \left\{ 0,1 \right\}^{D}}p\left( x\vert \mu \right) = \prod_{i = 1}^{D}1 = 1$$

Conseguimos ver também que: $$\begin{aligned} {\mathbb{E}}\lbrack x\rbrack & = \mu \\ \text{Cov}\lbrack x\rbrack & = \text{ diag}\left( \mu_{i}\left( 1 - \mu_{i} \right) \right) \end{aligned}$$

**Definição: Modelo de Mistura de Bernoulli**

Um Modelo de Mistura de Bernoulli é definido como: $$p\left( x\vert \mu,\pi \right) = \sum_{k = 1}^{K}\pi_{k}p\left( x\vert \mu_{k} \right) = \sum_{k = 1}^{K}\pi_{k}\prod_{i = 1}^{D}\mu_{ki}^{x_{i}}\left( 1 - \mu_{ki} \right)^{1 - x_{i}}$$ onde $\pi_{k}$ são os pesos dos clusters, que satisfazem $\sum_{k = 1}^{K}\pi_{k} = 1$, e $\mu_{ki}$ são os parâmetros da distribuição de Bernoulli para o cluster $k$.

**Teorema: Validade da distribuição**

Seja $p\left( x\vert \mu,\pi \right)$ um Modelo de Mistura de Bernoulli com $K$ componentes. Então, $p\left( x\vert \mu,\pi \right)$ é uma distribuição de probabilidade válida, ou seja, $p\left( x\vert \mu,\pi \right) \geq 0$ para todo $x$ e $\sum_{x \in \left\{ 0,1 \right\}^{D}}p\left( x\vert \mu,\pi \right) = 1$.

**Demonstração**

Para mostrar que $p\left( x\vert \mu,\pi \right) \geq 0$, note que cada termo na soma é não-negativo, pois $\pi_{k} \geq 0$ e $p\left( x\vert \mu_{k} \right) \geq 0$. Portanto, $p\left( x\vert \mu,\pi \right) \geq 0$ para todo $x$.

Para mostrar que a soma de $p\left( x\vert \mu,\pi \right)$ sobre todos os possíveis vetores binários de dimensão $D$ é igual a 1, usamos a linearidade da soma: $$\sum_{x \in \left\{ 0,1 \right\}^{D}}p\left( x\vert \mu,\pi \right) = \sum_{x \in \left\{ 0,1 \right\}^{D}}\sum_{k = 1}^{K}\pi_{k}p\left( x\vert \mu_{k} \right)$$ Podemos trocar a ordem das somas: $$= \sum_{k = 1}^{K}\pi_{k}\sum_{x \in \left\{ 0,1 \right\}^{D}}p\left( x\vert \mu_{k} \right)$$ Cada soma interna é igual a 1, pois $p\left( x\vert \mu_{k} \right)$ é uma distribuição de probabilidade válida. Portanto, temos: $$= \sum_{k = 1}^{K}\pi_{k} \ast 1 = \sum_{k = 1}^{K}\pi_{k} = 1$$

A média e covariância dessa distribuição de mistura é dada por: $$\begin{aligned} {\mathbb{E}}\lbrack x\rbrack & = \sum_{k = 1}^{K}\pi_{k}\mu_{k} \\ \text{Cov}\lbrack x\rbrack & = \sum_{k = 1}^{K}\pi_{k}\left( \Sigma_{k} + \mu_{k}\mu_{k}^{T} \right) - {\mathbb{E}}\lbrack x\rbrack{\mathbb{E}}\lbrack x\rbrack^{T} \end{aligned}$$

onde $\Sigma_{k} = \text{ diag}\left( \mu_{ki}\left( 1 - \mu_{ki} \right) \right)$. Dado um conjunto de dados $X = \left\{ x_{1},\ldots,x_{N} \right\}$ que segue o modelo de mistura de Bernoulli, a função de log-verossimilhança é dada por: $$\ln p\left( X~\vert ~\mu,\pi \right) = \sum_{n = 1}^{N}\ln p\left( x_{n}~\vert ~\mu,\pi \right) = \sum_{n = 1}^{N}\ln\left\{ \sum_{k = 1}^{K}\pi_{k}p\left( x_{n}~\vert ~\mu_{k} \right) \right\}$$

vemos novamente a mesma dificuldade de maximizar a verossimilhança diretamente, então vamos encontrar as fórmulas de atualização para o algoritmo EM aplicado ao modelo de mistura de Bernoulli.

Para isso, definimos, assim como no caso de mistura de gaussianas, a variável latente $z_{n}$ que indica de qual cluster o ponto $x_{n}$ foi gerado. A distribuição condicional de $x_{n}$ dado $z_{n}$ é dada por: $$p\left( x_{n}\vert z_{n},\mu \right) = \prod_{k = 1}^{K}{p\left( x\vert \mu_{k} \right)}^{z_{nk}}$$ e priori aqui é a mesma usada no caso de mistura de gaussianas: $$p\left( z_{n}\vert \pi \right) = \prod_{k = 1}^{K}\pi_{k}^{z_{nk}}$$

Antes de enunciarmos os teoremas com os valores ótimos, precisamos escrever a função de log-verossimilhança do dataset completo, que é dada por: $$\ln p\left( X,Z~\vert ~\mu,\pi \right) = \sum_{n = 1}^{N}\sum_{k = 1}^{K}z_{nk}\left\{ \ln\pi_{k} + \sum_{i = 1}^{D}\left\lbrack x_{ni}\ln\mu_{ki} + \left( 1 - x_{ni} \right)\ln\left( 1 - \mu_{ki} \right) \right\rbrack \right\}$$

E a esperança da log-verossimilhança do dataset completo sobre a distribuição posteriori de $Z$ dado $X$ é: $${\mathbb{E}}_{Z \sim p\left( Z\vert X,\mu,\pi \right)}\left\lbrack \ln p\left( X,Z~\vert ~\mu,\pi \right) \right\rbrack = \sum_{n = 1}^{N}\sum_{k = 1}^{K}\gamma(z_{nk})\left. \begin{array}{r} \{\ln\pi_{k} \\ + \sum_{i = 1}^{D}\left\lbrack x_{ni}\ln\mu_{ki} + \left( 1 - x_{ni} \right)\ln\left( 1 - \mu_{ki} \right) \right\rbrack\} \end{array} \right.$$ onde $\gamma(z_{nk})$ é a probabilidade de $z_{nk} = 1$ sob a distribuição posteriori. No passo **E** do algoritmo, isso é calculado com o teorema de bayes: $$\gamma(z_{nk}) = \frac{p\left( z_{nk} = 1 \right)p\left( x_{n}~\vert ~z_{nk} = 1,\mu_{k} \right)}{p\left( x_{n}~\vert ~\mu,\pi \right)} = \frac{\pi_{k}p\left( x_{n}~\vert ~\mu_{k} \right)}{\sum_{j = 1}^{K}\pi_{j}p\left( x_{n}~\vert ~\mu_{j} \right)}$$

**Teorema: Valor ótimo de $\mu$**

Fixando os parâmetros do modelo e variando apenas $\mu$, o valor ótimo de $\mu_{ki}$ é dado por: $$\mu_{ki} = \frac{\sum_{n = 1}^{N}\gamma(z_{nk})x_{ni}}{\sum_{n = 1}^{N}\gamma(z_{nk})} = \frac{1}{N_{k}}\sum_{n = 1}^{N}\gamma(z_{nk})x_{ni}$$ ou $$\mu_{k} = \frac{\sum_{n = 1}^{N}\gamma(z_{nk})x_{n}}{\sum_{n = 1}^{N}\gamma(z_{nk})} = \frac{1}{N_{k}}\sum_{n = 1}^{N}\gamma(z_{nk})x_{n}$$

**Demonstração**

Para encontrar o valor ótimo de $\mu_{ki}$, derivamos a função de log-verossimilhança em relação a $\mu_{ki}$ e igualamos a zero: $$\frac{\partial\ln p\left( X,Z~\vert ~\mu,\pi \right)}{\partial\mu_{ki}} = \sum_{n = 1}^{N}\gamma(z_{nk})\frac{x_{ni} - \mu_{ki}}{\mu_{ki}\left( 1 - \mu_{ki} \right)} = 0$$ Rearranjando os termos, obtemos: $$\sum_{n = 1}^{N}\gamma(z_{nk})x_{ni} = \mu_{ki}\sum_{n = 1}^{N}\gamma(z_{nk})$$ Dividindo ambos os lados por $\sum_{n = 1}^{N}\gamma(z_{nk})$, obtemos a expressão desejada para $\mu_{ki}$.

**Teorema: Valor ótimo de $\pi$**

Fixando os parâmetros do modelo e variando apenas $\pi$, o valor ótimo de $\pi_{k}$ é dado por: $$\pi_{k} = \frac{\sum_{n = 1}^{N}\gamma(z_{nk})}{N} = \frac{N_{k}}{N}$$

**Demonstração**

Sabendo que $\sum_{k}\pi_{k} = 1$, usamos de multiplicadores de lagrange para encontrar o valor ótimo de $\pi_{k}$. Definimos a função lagrangiana como: $$L(\pi,\lambda) = \ln p\left( X,Z~\vert ~\mu,\pi \right) + \lambda\left( \sum_{k = 1}^{K}\pi_{k} - 1 \right)$$ Derivando em relação a $\pi_{k}$ e igualando a zero, obtemos: $$\frac{\partial L}{\partial\pi_{k}} = \frac{\gamma(z_{nk})}{\pi_{k}} + \lambda = 0$$ Isolando $\pi_{k}$, obtemos: $$\pi_{k} = - \frac{\lambda}{\gamma(z_{nk})}$$ Usando a condição de normalização $\sum_{k}\pi_{k} = 1$, podemos encontrar o valor de $\lambda$: $$\sum_{k = 1}^{K} - \frac{\lambda}{\gamma(z_{nk})} = 1$$ Resolvendo para $\lambda$, obtemos: $$\lambda = - \frac{1}{\sum_{k = 1}^{K}\frac{1}{\gamma(z_{nk})}}$$ Substituindo esse valor de $\lambda$ na expressão para $\pi_{k}$, obtemos: $$\pi_{k} = \frac{\gamma(z_{nk})}{\sum_{j = 1}^{K}\gamma(z_{nj})} = \frac{N_{k}}{N}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Algoritmo EM Variacional](../algoritmo-em-variacional/index.md)
- Próximo: [Singularidades e Identificabilidade](../singularidades-e-identificabilidade/index.md)
