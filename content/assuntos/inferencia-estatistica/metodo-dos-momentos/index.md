---
layout: "default"
title: "Método dos Momentos"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 17
---

[Inferência Estatística](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-17"></a>

# Método dos Momentos

------------------------------------------------------------------------

Lembra que estimamos o primeiro momento ${\mathbb{E}}\lbrack X\rbrack \approx 1/n \cdot \sum_{i = 1}^{n}X_{i}$? Será que da pra estimar os outros momentos de uma forma parecida? Na verdade sim! É bem intuitivo:

<a id="method-of-moments"></a>

**Definição: Método dos Momentos**

Suponha que $X_{1},\ldots,X_{n}$ formam uma amostra aleatória de uma distribuição indexada por um parâmetro $k$-dimensional $\theta$ e que tem, pelo menos, $k$ momentos finitos. Para $j = 1,\ldots,k$, deixe $\mu_{j}(\theta) = {\mathbb{E}}\left\lbrack X_{1}^{j}~\vert ~\theta \right\rbrack$. Suponha que a função $\mu(\theta) = \left( \mu_{1}(\theta),\ldots,\mu_{k}(\theta) \right)$ é uma função bijetiva de $\theta$. Seja $M\left( \mu_{1},\ldots,\mu_{k} \right)$ a função inversa, ou seja, para todo $\theta$ é válido que: $$\theta = M\left( \mu_{1}(\theta),\ldots,\mu_{k}(\theta) \right)$$ Defina os *momentos amostrais* como: $$m_{j} = \frac{1}{n}\sum_{i = 1}^{n}\left( X_{i} \right)^{j}$$ Para $j = 1,\ldots,k$. O *método do estimador de momentos* de $\theta$ é $M\left( m_{1},\ldots,m_{j} \right)$

O método mais usual de se implementar esse método é resolvendo todas as equações $m_{j} = \mu_{j}(\theta)$ e então resolver para $\theta$

**Teorema: Consistência**

Suponha que $X_{1},X_{2},\ldots$ são i.i.d com uma distribuição indexada por um parâmetro $k$-dimensional $\theta$. Suponha também que o os primeiros $k$ momentos da distribuição são finitos e existem para todo $\theta$. Suponha também que a função inversa $M$ é definida como na [\[method-of-moments\]](#method-of-moments) e é contínua. Então a sequência de estimadores pelo método dos momentos baseada em $X_{1},\ldots,X_{n}$ é uma sequência consistente de estimadores de $\theta$

**Demonstração**

A Lei dos Grandes Números diz que os momentos amostrais convergem em probabilidade para os momentos $\mu_{1}(\theta),\mu_{2}(\theta),\ldots,\mu_{k}(\theta)$. Isso implica que, ao generalizar isso para funções de $k$ variáveis isso implica que $M$, nos momentos amostrais, converge em probabilidade para $\theta$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Estatística Frequentista](../estatistica-frequentista/index.md)
- Próximo: [Estatística Suficiente](../estatistica-suficiente/index.md)
