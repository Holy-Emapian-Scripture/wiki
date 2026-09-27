---
layout: "default"
title: "Máxima Variância — Principal Component Analysis"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 7
---

[Aprendizado de Máquina](../../index.md) · [Principal Component Analysis](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# Máxima Variância

Seja $X \in {\mathbb{R}}^{N \times D}$ onde $x_{i}^{T}$ é a $i$-ésima linha de $X$, queremos projetar $X$ em um subespaço ${\mathbb{R}}^{M}$ com $M < D$ enquanto maximizamos a variância dos dados projetados.

Supondo que $M = 1$, pegamos $u_{1} \in {\mathbb{R}}^{D}$ tal que $u_{1}^{T}u_{1} = 1$ então pegamos quanto de $u_{1}$ compõe o vetor $x_{i}$ com $u_{1}^{T}x_{i}$ ([\[base-coefficients\]](../definicoes/index.md#base-coefficients)). Vamos definir a média dos dados projetados como $$u_{1}^{T}\overline{x} = \frac{1}{N}\sum_{i = 1}^{N}u_{1}^{T}x_{i}$$

e também definimos a variância deles como $$u_{1}^{T}Su_{1} = \frac{1}{N}\sum_{i = 1}^{N}\left( u_{1}^{T}x_{i} - u_{1}^{T}\overline{x} \right)^{2}$$

e $$S = \frac{1}{N}\sum_{n = 1}^{N}\left( x_{n} - \overline{x} \right)\left( x_{n} - \overline{x} \right)^{T}$$

Agora, queremos maximizar $u_{1}^{T}Su_{1}$ com respeito a $u_{1}$ com a restrição de $u_{1}^{T}u_{1} = 1$. Antes de fazermos isso mesmo, a lógica desse processo é que queremos entender qual a direção do espaço que mais contribui com a variância dos dados, ou seja, qual a direção que mais “espalha” os dados. Para isso, vamos utilizar o método de multiplicadores de Lagrange para maximizar $u_{1}^{T}Su_{1}$ com a restrição de $u_{1}^{T}u_{1} = 1$. Definimos a função lagrangiana como: $$\mathcal{L}(u_{1},\lambda) = u_{1}^{T}Su_{1} - \lambda\left( u_{1}^{T}u_{1} - 1 \right)$$

Realizando as contas necessárias, chegamos que $$Su_{1} = \lambda u_{1}$$

Ou seja, a direção que mais contribui com a variância dos dados é o autovetor de $S$ correspondente ao maior autovalor. Esse autovetor é chamado de *primeira componente principal*. Sabendo disso, podemos utilizar de **indução forte** para mostrar que a segunda componente principal é o autovetor de $S$ correspondente ao segundo maior autovalor, e assim por diante. Dessa forma, as $M$ primeiras componentes principais são os $M$ autovetores de $S$ correspondentes aos $M$ maiores autovalores.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Definições](../definicoes/index.md)
- Próximo: [Minimzando o Erro de Projeção](../minimzando-o-erro-de-projecao/index.md)
