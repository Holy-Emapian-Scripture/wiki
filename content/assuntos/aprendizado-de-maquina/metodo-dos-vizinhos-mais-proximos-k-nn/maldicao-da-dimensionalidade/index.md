---
layout: "default"
title: "Maldição da Dimensionalidade — Método dos Vizinhos mais próximos (k-NN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 6
---

[Aprendizado de Máquina](../../index.md) · [Método dos Vizinhos mais próximos (k-NN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-9"></a>

# Maldição da Dimensionalidade

A expressão maldição da dimensionalidade foi introduzida por Bellman (1957) e é comumente usada para descrever problemas causados pelo aumento exponencial do volume associado em função da dimensionalidade em espaços euclidianos. No caso do k-NN, esse aumento implica na esparsidade dos exemplos de treino, fazendo com que os k-vizinhos que procuramos estejam muito distantes.

Para ilustrar tal efeito, suponha que a distribuição ${\mathbb{P}}_{x}$ sobre os vetores de entrada $x_{1},\ldots,x_{N}$ seja uniforme sobre uma hiperbola $D$-dimensional $S_{D}$ centrada na origem e com raio unitário (Ou seja, todo ponto dentro dessa bola é uniformemente provável de ser escolhida para ser um vetor de entrada). Suponha também que queremos classificar o vetor de origem $z = (0,\ldots,0)^{T}$. Defina $r$ como o raio da hiperbola $S'_{D} \subseteq S_{D}$ que **contém os k vizinhos mais próximos de $z$**. Em esperança, o quão grande devemos esperar que $r$ seja? Antes, é intuitivo notar que ${\mathbb{P}}\left( x_{i} \in S'_{D} \right)$ é a razão dos volumes de $S'_{D}$ e $S_{D}$, ou seja: $${\mathbb{P}}\left( x_{i} \in S'_{D} \right) = {\mathbb{E}}_{x_{i} \sim {\mathbb{P}}_{x}}\left\lbrack {\mathbb{I}}_{x_{i} \in S'_{D}} \right\rbrack = \frac{\pi^{\frac{D}{2}}r^{D}}{\pi^{\frac{D}{2}}1^{D}} = r^{D}$$ Segue então que o número esperado de amostra, dentre as $N$ que possuímos, dentro de $S'_{D}$ é: $$\sum_{i = 1}^{N}{\mathbb{P}}\left( x_{i} \in S'_{D} \right) = Nr^{D}$$ Então, para que tenhamos, em esperança, $k$ vizinhos dentro de $S'_{D}$, devemos escolher $r$ tal que $r = \left( \frac{k}{N} \right)^{\frac{1}{D}}$, e a medida que $D$ cresce, temos: $$\lim\limits_{D \rightarrow \infty}r = \lim\limits_{D \rightarrow \infty}\left( \frac{k}{N} \right)^{\frac{1}{D}} = 1$$ Ou seja, quanto maior é a dimensão, maior é o raio de $S'_{D}$, o que mostra que a propriedade de “vizinhos próximos tem propriedades parecidas” é quebrada em altas dimensões, o que é um grande problema para o método k-NN.

<a id="secao-10"></a>

## Manifolds de baixa dimensão.

Na prática, não é incomum ver k-NN sendo utilizado em espaços de alta dimensão, como de imagens, e atingindo boas taxas de acurácia. Uma explicação para esse fenômeno é que os dados não estão uniformemente distribuídos e, na verdade, residem em um subespaço de baixa dimensão. Por exemplo, suponha que $\mathcal{X} \subset {\mathbb{R}}^{256 \times 256 \times 3}$ é o espaço de imagens de tamanho $256 \times 256$ com três canais de cores — red, green, and blue (RGB) — que contém um gato. Nós esperamos que ${\mathbb{P}}_{x}$ aloque massa zero para fotos de paisagens, obras de arte, etc

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Qual distância escolher?](../qual-distancia-escolher/index.md)
- Próximo: [Regressão Linear](../../regressao-linear/index.md)
