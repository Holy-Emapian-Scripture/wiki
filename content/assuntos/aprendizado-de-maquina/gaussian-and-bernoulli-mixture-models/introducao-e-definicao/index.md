---
layout: "default"
title: "Introdução e Definição — Gaussian and Bernoulli Mixture Models"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 10
---

[Aprendizado de Máquina](../../index.md) · [Gaussian and Bernoulli Mixture Models](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-10"></a>

# Introdução e Definição

No k-means, cada ponto é atribuído a um único cluster, o que significa que a fronteira entre os clusters é rígida. No entanto, em muitos casos, pode ser mais apropriado permitir que cada ponto tenha uma probabilidade de pertencer a cada cluster. Isso nos leva aos Modelos de Mistura Gaussiana (GMMs), que é uma generalização do K-means.

Aqui, nós supomos que cada ponto **pode** ter saído de um dos $K$ clusters, mas não sabemos de qual, cada cluster esse sendo representado por uma distribuição gaussiana. Cada cluster $k$ é caracterizado por uma média $\mu_{k}$ e uma matriz de covariância $\Sigma_{k}$. Além disso, cada cluster tem um peso $\pi_{k}$, que representa a proporção de pontos que pertencem a esse cluster.

**Definição: Modelo de Mistura Gaussiana**

Um Modelo de Mistura Gaussiana é definido como: $$p(x) = \sum_{k = 1}^{K}\pi_{k}N\left( x~\vert ~\mu_{k},\Sigma_{k} \right)$$ onde $N\left( x~\vert ~\mu_{k},\Sigma_{k} \right)$ é a densidade da distribuição gaussiana com média $\mu_{k}$ e covariância $\Sigma_{k}$, e $\pi_{k}$ são os pesos dos clusters, que satisfazem $\sum_{k = 1}^{K}\pi_{k} = 1$.

**Teorema: Validade da distribuição**

Seja $p(x)$ um Modelo de Mistura Gaussiana com $K$ componentes. Então, $p(x)$ é uma distribuição de probabilidade válida, ou seja, $p(x) \geq 0$ para todo $x$ e $\int p(x)dx = 1$.

**Demonstração**

Para mostrar que $p(x) \geq 0$, note que cada termo na soma é não-negativo, pois $\pi_{k} \geq 0$ e $N\left( x~\vert ~\mu_{k},\Sigma_{k} \right) \geq 0$. Portanto, $p(x) \geq 0$ para todo $x$.

Para mostrar que a integral de $p(x)$ sobre todo o espaço é igual a 1, usamos a linearidade da integral: $$\begin{aligned} \int p(x)dx & = \int\sum_{k = 1}^{K}\pi_{k}N\left( x~\vert ~\mu_{k},\Sigma_{k} \right)dx \\ & = \sum_{k = 1}^{K}\pi_{k}\int N\left( x~\vert ~\mu_{k},\Sigma_{k} \right)dx \\ & = \sum_{k = 1}^{K}\pi_{k} \ast 1 \\ & = \sum_{k = 1}^{K}\pi_{k} \\ & = 1 \end{aligned}$$

Vamos também introduzir o conceito de **variável latente**. Intuitivamente, uma variável latente é uma variável que não observamos diretamente, mas que influencia os dados que observamos. Por exemplo, a classe de um documento em uma análise de tópicos, já que podemos não saber que um documento fala sobre biologia, mas ele influencia nosso modelo a aprender sobre o assunto.

No caso dos GMMs, podemos introduzir uma variável latente $z_{n}$ para cada ponto $x_{n}$, que indica de qual cluster o ponto foi gerado. Especificamente, $z_{n}$ é um vetor one-hot de dimensão $K$, onde $z_{nk} = 1$ se o ponto $x_{n}$ foi gerado pelo cluster $k$, e $z_{nj} = 0$ para $k \neq j$.

Vamos definir a distribuição conjunta de $x_{n}$ e $z_{n}$ como: $$p\left( x_{n},z_{n} \right) = p\left( z_{n} \right)p\left( x_{n}~\vert ~z_{n} \right)$$

a distribuição marginal de $z_{n}$ é definida em termo dos coeficientes de mistura $\pi_{k}$: $${\mathbb{P}}(z_{nk} = 1) = \pi_{k}$$

de forma que $\pi_{k} \geq 0$ e $\sum_{k = 1}^{K}\pi_{k} = 1$ para que $p\left( z_{n} \right)$ seja uma distribuição de probabilidade válida. Por conta da forma que definimos $z_{n}$ como vetor one-hot, podemos reescrever sua distribuição como: $$p\left( z_{n} \right) = \prod_{k = 1}^{K}\pi_{k}^{z_{nk}}$$

Similarmente, a distribuição condicional de $x_{n}$ dado $z_{nk} = 1$ é definida como: $$p\left( x_{n}~\vert ~z_{nk} = 1 \right) = N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)$$

que também pode ser escrita na forma: $$p\left( x_{n}~\vert ~z_{n} \right) = \prod_{k = 1}^{K}{N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}^{z_{nk}}$$

A distribuição conjunta é escrita então como $p\left( z_{n} \right)p\left( x_{n}~\vert ~z_{n} \right)$ e a marginal sobre $x$ é obtida somando sobre todas as possíveis configurações de $z_{n}$: $$p\left( x_{n} \right) = \sum_{z_{n}}p\left( x_{n},z_{n} \right) = \sum_{z_{n}}p\left( z_{n} \right)p\left( x_{n}~\vert ~z_{n} \right) = \sum_{k = 1}^{K}\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)$$

Pode até parecer que, representando a distribuição de $x_{n}$ como uma mistura de gaussianas, estamos apenas complicando as coisas, mas a introdução da variável latente $z_{n}$ nos permite trabalhar com a conjunta (que vai se mostrar ser bem mais fácil de lidar) e também nos dá uma interpretação probabilística do modelo.

Outra quantidade que será importante é a probabilidade posterior de $z_{n}$ dado $x_{n}$ (chamaremos de $\gamma(z_{nk})$), que é dada pelo Teorema de Bayes: $$\begin{aligned} \gamma(z_{nk}) & = {\mathbb{P}}(z_{nk} = 1~\vert ~x_{n}) \\ & = \frac{p\left( z_{nk} = 1 \right)p\left( x_{n}~\vert ~z_{nk} = 1 \right)}{p\left( x_{n} \right)} \\ & = \frac{\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\sum_{j = 1}^{K}\pi_{j}N\left( x_{n}~\vert ~\mu_{j},\Sigma_{j} \right)} \end{aligned}$$

Vamos interpretar $\pi_{k}$ como a probabilidade de que o ponto $x_{n}$ tenha sido gerado pelo cluster $k$ **a posteriori** e $\gamma(z_{nk})$ como a probabilidade de que o ponto $x_{n}$ pertença ao cluster $k$ **a posteriori**. Também podemos chamar $\gamma(z_{nk})$ de *responsabilidade* do cluster $k$ pelo ponto $x_{n}$, pois ela indica o quanto o cluster $k$ é responsável por gerar o ponto $x_{n}$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Gaussian and Bernoulli Mixture Models](../index.md)
- Próximo: [Máxima Verossimilhança](../maxima-verossimilhanca/index.md)
