---
layout: "default"
title: "Lidando com ELBO intratável — Inferência Variacional"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 23
---

[Aprendizado de Máquina](../../index.md) · [Inferência Variacional](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-36"></a>

# Lidando com ELBO intratável

Com relação à escolha de $Q$, costuma-se adotar uma família de distribuições paramétricas. Deste modo, podemos maximizar $L$ sobre um espaço de parâmetros $\Omega$. Por exemplo, se $Q$ é o conjunto das distribuições Gaussianas univariadas, $\Omega = {\mathbb{R}} \times R^{+}$ e $\omega \in \Omega$ é um par média/variância. De maneira geral, os termos envolvidos no ELBO podem ser intratáveis e, até meados da década passada, desenvolver soluções customizadas para posterioris diferentes era considerado uma contribuição técnica em ML.

Atualmente, existem metodologias genéricas, que viabilizam inferência variacional quase como uma tecnologia *off-the-shelf*. A mais famosa dentre essas, é o truque reparametrização. Essa técnica assume que é possível descrever a amostragem de $\theta \sim q$ a partir de uma transformação g de uma variável aleatória auxiliar $\varepsilon$. Além disso, precisamos que g seja diferenciável com respeito aos parâmetros $\omega$ de $q$. Por exemplo, se q é uma distribuição normal com parâmetros $\omega = \left( \mu,\sigma^{2} \right)$, podemos obter uma amostra $\theta \sim q$ definindo $\theta = g(\varepsilon;\omega) = \sigma\varepsilon + \mu$ e amostrando $\varepsilon$ de numa gaussiana padrão — i.e., com média zero e variância um.

Com isso, podemos aproximar os termos do ELBO amostrando M variáveis auxiliares $\varepsilon(1),...,\varepsilon(M)$ e estimar o gradiente de $L(q)$ com respeito a $\omega$ como:

$$\nabla_{\omega}L(q) = \nabla_{\omega}\frac{1}{M}\sum_{m = 1}^{M}\ln p\left( D\vert \theta^{(m)} \right) + \ln p\left( \theta^{(m)} \right) - \ln q\left( \theta^{(m)};\omega \right)$$

Note que, na notação acima, $q$ também depende diretamente de $\omega$. Em posse dessa estimativa, podemos utilizar nosso algoritmo de gradiente preferido para otimizar o ELBO. Naturalmente, essa aproximação deve ser refeita com novas amostras a cada passo de gradiente. Para evitar incluir restrições explícitas para garantir que parâmetros restritos sejam válidos (e.g., variâncias devem ser não-negativas), nós também as modelamos como a transformação de uma variável real. No caso citado acima, podemos ter $\omega = \left( \mu,\sigma^{2} = u(z) \right)$ com $u(z) = e^{z}$ ou $u(z) = \beta^{- 1}\ln(1 + e^{\beta z})$ para algum $\beta > 0$.
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Cota Inferior (ELBO)](../cota-inferior-elbo/index.md)
