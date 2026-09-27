---
layout: "default"
title: "Distribuições Priori e Posteriori — Estatística Bayesiana"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 4
---

[Inferência Estatística](../../index.md) · [Estatística Bayesiana](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Distribuições Priori e Posteriori

Quando fazemos um experimento em que $\theta$ é uma V.A., é interessante chutar uma distribuição para ele antes de observar qualquer dado.

**Definição: Distribuição a priori**

Dado um modelo estatístico com parâmetro $\theta$, se $\theta$ for uma variável aleatória, a distribuição de $\theta$ antes de qualquer dado é chamada de distribuição a priori (Podemos denotar $\xi(\theta)$ ou $f_{\theta}(\theta)$).

Quando estamos trabalhando com observações $X_{1},\ldots,X_{k}$, denotamos a distribuição a priori dos dados como $X_{1},\ldots,X_{k}\vert \theta \sim \text{ Dist}(\theta)$ onde **Dist** representa qualquer distribuição, Ué, como que condicionamos $X_{j}$ em $\theta$? Qual o sentido disso? Imagine que cada experimento é o output de uma máquina industrial, porém, para que essa máquina funcione, alguém precisa passar algumas informações para ela, porém, o seu chefe não mandou você colocar as informações, então você não sabe quais são elas, mas você está vendo os resultados da máquina, e sabe que aqueles resultados só estão acontecendo porque aquela configuração foi colocada, então por mais que não sabemos o $\theta$, ele os valores de $X_{1},\ldots,X_{k}$ só sairam como estamos vendo porque o parâmetro da distribuição é $\theta$ (Que ainda queremos descobrir)

Assim como especificamos uma distribuição para θ antes de qualquer dado ser observado, podemos atualizar a distribuição conforme observamos dados.

**Definição: Função de verossimilhança**

A função de verossimilhança ${\mathbb{L}}(\theta)$ é definida por $${\mathbb{L}}(\theta) = f_{X\vert \theta}\left( x_{1},\ldots,x_{k} \mid \theta \right)$$ De forma que $f_{X\vert \theta}\left( \underline{x}\vert \theta \right)$ é a f.d.p de $X_{1},\ldots,X_{k}$

**Definição: Distribuição a posteriori**

Dado um modelo estatístico com variáveis aleatórias observáveis $X_{1},\ldots,X_{n}$, a distribuição de $X_{1},\ldots,X_{n}\vert \theta$ é chamada de distribuição a posteriori

E agora, com o teorema de bayes, podemos relacionar essas nossas definições

**Teorema: Bayes**

Suponha que $X_{1},\ldots,x_{k}$ são amostras de uma população com distribuição conhecida de parâmetro $\theta$ tal que sua f.d.p é $f_{X\vert \theta}\left( x_{1},\ldots,x_{k}\vert \theta \right)$. Suponha também que $\theta$ é desconhecido e a distribuição a priori de $\theta$ é tal que sua f.d.p é $f_{\theta}(\theta)$, então a posteriori de $\theta$ é tal que: $$f_{\theta}\left( \theta\vert x_{1},\ldots,x_{k} \right) = \frac{f_{X}\left( x_{1},\ldots,x_{k}\vert \theta \right)f_{\theta}(\theta)}{f_{X}\left( x_{1},\ldots,x_{k} \right)}$$ ou $$f_{\theta}\left( \theta\vert x_{1},\ldots,x_{k} \right) = \frac{{\mathbb{L}}(\theta)\xi(\theta)}{\int{\mathbb{L}}(\theta)\xi(\theta)d\theta}$$ Perceba porém, que o termo do denominador não depende de $\theta$, ou seja, podemos reescrever isso tudo como: $$f_{\theta}\left( \theta\vert x_{1},\ldots,x_{k} \right) \propto {\mathbb{L}}(\theta)\xi(\theta)$$

**Demonstração**

Usar teorema de Bayes

Por conta do teorema acima, todos os termos constantes que encontramos em nossa distribuição nós podemos pegar e jogar fora e, ao final, encontramos um termo constante geral, já que para descobrir essa constante $C$ basta fazer: $$\frac{1}{C} = \int_{\vert \Theta\vert }{\mathbb{L}}(\theta)\xi(\theta)d\theta$$<a id="finding-the-constant"></a>

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Introdução](../introducao/index.md)
- Próximo: [Observações sequenciais e predições](../observacoes-sequenciais-e-predicoes/index.md)
