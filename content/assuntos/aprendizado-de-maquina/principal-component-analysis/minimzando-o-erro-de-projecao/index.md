---
layout: "default"
title: "Minimzando o Erro de Projeção — Principal Component Analysis"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 8
---

[Aprendizado de Máquina](../../index.md) · [Principal Component Analysis](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-8"></a>

# Minimzando o Erro de Projeção

Pegamos um set $\left\{ u_{1},u_{2},\ldots,u_{D} \right\}$ de vetores otornomais em ${\mathbb{R}}^{D}$. Pelo [\[base-coefficients\]](../definicoes/index.md#base-coefficients), sabemos que $$x_{n} = \sum_{i = 1}^{D}\left( x_{n}^{T}u_{i} \right)u_{i}$$

Porém, queremos aproximar $x_{n}$ usando um conjunto de só $M < D$ variáveis. Escrevemos então: $${\hat{x}}_{n} = \sum_{i = 1}^{M}\underset{\text{ Depende de }x_{n}}{\underbrace{z_{ni}}}u_{i} + \sum_{i = M + 1}^{D}\underset{\text{ Constante em }x_{n}}{\underbrace{b_{i}}}u_{i}$$

E queremos então minimizar $$J = \frac{1}{N}\sum_{n = 1}^{N}\| x_{n} - {\hat{x}}_{n}\|^{2}$$

Derivando essa função de custo com relação a $z_{ni}$ e $b_{i}$ e igualando a zero e usando das condições de ortogonalidade, chegamos que $$z_{ni} = x_{n}^{T}u_{i}$$ $$b_{i} = {\overline{x}}^{T}u_{i}$$

substituindo, obtemos então: $$x_{n} - {\hat{x}}_{n} = \sum_{i = M + 1}^{D}\left\{ \left( x_{n}^{T} - {\overline{x}}^{T} \right)u_{i} \right\} u_{i}$$

com isso, conseguimos achar uma fórmula para $J$ $$J = \frac{1}{N}\sum_{n = 1}^{N}\sum_{i = M + 1}^{D}\left\{ \left( x_{n}^{T} - {\overline{x}}^{T} \right)u_{i} \right\}^{2} = \sum_{i = M + 1}^{D}u_{i}^{T}Su_{i}$$

Agora, só nos falta otimizar $J$ com relação à $u_{i}$ e aplicar a otimização com as condições de ortogonalidade. Vamos primeiro considerar o caso $M = 1$, temos que a função de lagrange é dada por $$\mathcal{L}(u_{1},\lambda) = \sum_{i = 2}^{D}u_{i}^{T}Su_{i} - \sum_{i = 2}^{D}\lambda_{i}\left( u_{i}^{T}u_{i} - 1 \right)$$

derivando essa função e aplicando as regras de otimização restrita, chegamos que $$Su_{i} = \lambda_{i}u_{i}$$

Novamente, chegamos na conclusão de que os autovetores de $S$ são as direções que minimizam o erro de projeção. E, novamente, podemos utilizar de indução forte para mostrar que os autovetores correspondentes aos maiores autovalores são as direções que minimizam o erro de projeção.

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Máxima Variância](../maxima-variancia/index.md)
- Próximo: [Gaussian and Bernoulli Mixture Models](../../gaussian-and-bernoulli-mixture-models/index.md)
