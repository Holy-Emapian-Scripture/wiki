---
layout: "default"
title: "Intervalos de Confiança Unilaterais — Intervalos de Confiança"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 10
---

[Inferência Estatística](../../index.md) · [Intervalos de Confiança](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-10"></a>

# Intervalos de Confiança Unilaterais

Nós vimos como encontrar intervalos aleatórios $(A,B)$ que tem probabilidade $\gamma$ de conter o parâmetro $\theta$, porém, podem acontecer situações que apenas obter um limite superior ou inferior seja suficiente para nós

Dados $\gamma_{1}$ e $\gamma_{2}$ com $\gamma_{2} > \gamma_{1}$ e $\gamma_{2} - \gamma_{1} = \gamma$, então: $${\mathbb{P}}(T_{n - 1}^{- 1}\left( \gamma_{1} \right) < U < T_{n - 1}^{- 1}\left( \gamma_{1} \right)) = \gamma$$ E então obtemos que, perante todos os intervalos aleatórios possíveis, o intervalo de confiança $\gamma$ com o menor tamanho é o simétrico $$\gamma_{1} = 1 - \gamma_{2}$$ Porém, há casos que um intervalo não-simétrico é útil (Como mencionei o caso anterior de apenas limites superiores ou intefiores)

**Definição: Intervalo de Confiança Generalizado**

Seja $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ uma amostra de uma distribuição parametrizada por $\theta$. Seja $g(\theta):\Omega \rightarrow {\mathbb{R}}$ e seja $A$ uma estatística tal que: $${\mathbb{P}}(A < g(\theta)) \geq \gamma\text{\quad\quad}\forall\theta$$ Então o intervalo aleatório $(A, + \infty)$ é chamado de intervalo de confiança unilateral $\gamma$ de limite inferior $A$. A mesma definição vale para a estatística $B$ tal que: $${\mathbb{P}}(g(\theta) < B) \geq \gamma$$ Então o intervalo aleatório $( - \infty,B)$ é chamado de intervalo de confiança unilateral $\gamma$ de limite superior $B$. Se a desigualdade “$\geq \gamma$” é uma igualdade para todo $\theta$, então tanto o intervalo quanto os limites são chamados de exatos

**Teorema: Intervalo unilateral da média da normal**

Seja $X_{1},\ldots,X_{n} \sim N\left( \mu,\sigma^{2} \right)$, as estatísticas a seguir são, respectivamente, limites inferior e superior exatos com coeficiente $\gamma$ para $\mu$: $$\begin{array}{r} A = {\overline{X}}_{n} - T_{n - 1}^{- 1}(\gamma)\sigma\frac{'}{\sqrt{n}} \\ B = {\overline{X}}_{n} + T_{n - 1}^{- 1}(\gamma)\sigma\frac{'}{\sqrt{n}} \end{array}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Intervalo de Confiança para a média de uma Normal](../intervalo-de-confianca-para-a-media-de-uma-normal/index.md)
- Próximo: [Intervalo de confiança para outros parâmetros](../intervalo-de-confianca-para-outros-parametros/index.md)
