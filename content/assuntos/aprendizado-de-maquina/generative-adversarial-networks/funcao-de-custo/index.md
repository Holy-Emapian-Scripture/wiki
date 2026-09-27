---
layout: "default"
title: "Função de Custo — Generative Adversarial Networks"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 23
---

[Aprendizado de Máquina](../../index.md) · [Generative Adversarial Networks](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-28"></a>

# Função de Custo

Para definir isso precisamente, vamos definir uma variável binária: $$t = \begin{cases} 1\text{ se }x\text{ é real} \\ 0\text{ se }x\text{ é sintética } \end{cases}$$

a rede discriminadora possui um único output com uma ativação sigmoidal. Esse output representa a probabilidade de $x$ ser real, ou seja $$d(x,\varphi) = {\mathbb{P}}(t = 1\vert x,\varphi)$$

nós treinamos a rede discriminadora usando a clássica função cross-entropy $$E(w,\varphi) = - \frac{1}{N}\sum_{n = 1}^{N}\left\{ t_{n}\ln d\left( x_{n},\varphi \right) + \left( 1 - t_{n} \right)\ln\left( 1 - d\left( x_{n},\varphi \right) \right) \right\}$$

O dataset utilizado tem tanto as amostras reais $x_{n}$ quanto as sintéticas $z_{n}$ geradas pelo gerador. Então podemos separar o dataset $D$ em $D_{\text{real}}$ e $D_{\text{sintético}}$. Dessa forma, como definimos que $t = 1$ para amostras reais e $t = 0$ para amostras sintéticas, podemos reescrever a função de custo como: $$E(w,\varphi) = - \frac{1}{N_{\text{real}}}\sum_{n \in D_{\text{real}}}\ln d\left( x_{n},\varphi \right) - \frac{1}{N_{\text{sintético}}}\sum_{n \in D_{\text{sintético}}}\ln\left( 1 - d\left( z_{n},\varphi \right) \right)$$<a id="gan-cost-function"></a>

onde (normalmente) $N_{\text{real }} = N_{\text{sintético}}$, ou seja, o dataset é balanceado. O interessante desse método é que podemos otimizar a função com base no gradiente, no entanto, nós a minimizamos com relação a $\varphi$ e **maximizamos** com relação a $w$. Ou seja, o gerador quer maximizar a função de custo, enquanto o discriminador quer minimizar. Isso é conhecido como **jogo de soma zero**.

O modo de treino que apresentamos até o momento faz com que o gerador aprenda distribuições não-condicionais $p(x)$. Por exemplo, se ele for treinado com imagens de cachorros, ele vai aprender a gerar imagens de cachorros. No entanto, podemos criar GANs condicionais, onde o gerador aprende uma distribuição $p\left( x\vert c \right)$ onde $c$ pode, por exemplo, representar um vetor que especifica a raça do cachorro.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Treinamento Adversarial](../treinamento-adversarial/index.md)
- Próximo: [Treinamento do GAN](../treinamento-do-gan/index.md)
