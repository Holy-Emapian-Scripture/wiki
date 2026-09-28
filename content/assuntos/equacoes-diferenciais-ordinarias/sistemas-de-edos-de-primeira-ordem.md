---
layout: "default"
title: "Sistemas de EDO’s de Primeira Ordem"
tipo: "conteudo"
disciplina: "Equações Diferenciais Ordinárias"
origem: "3 semestre/EDO/RecapA2.md"
trilha: "../../../trilhas/equacoes-diferenciais-ordinarias/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 9
---

[Equações Diferenciais Ordinárias](index.md)

<!-- wiki:original:inicio -->

<a id="section_sistemas_de_edo_primeira_ordem"></a>

# Sistemas de EDO’s de Primeira Ordem


<a id="sistemas-lineares"></a>
<a id="section_sistemas_lineares"></a>

## Sistemas Lineares

Sistemas da forma:

$$Ax = x',A \in {\mathbb{R}}^{n \times n},x \in {\mathbb{R}}^{n}$$ <a id="system_ode_first_order"></a>

Têm solução constante em $x' = 0$.

Fazendo uma analogia em $\mathbb{R}$, temos $x' = ax \Rightarrow x = e^{at}x_{0}$. O mesmo vale para exponenciais de matrizes. Buscamos então soluções do [sistema de EDOs de primeira ordem](#system_ode_first_order) da forma:

$$
x(t) = ve^{\lambda t},v \in {\mathbb{R}}^{n},\lambda \in {\mathbb{R}}
$$

Ou seja:

$$
Ax = x' \Leftrightarrow Ave^{\lambda t} = \lambda ve^{\lambda t}
$$

Como $e^{\lambda t} \neq 0,\forall t \in {\mathbb{R}}$:

$$
Av = \lambda v
$$

É exatamente o problema de [autovalores](../algebra-linear-numerica/problemas-de-autovalores.md) da matriz de coeficientes $A$.

<a id="section_autovalores_reais_distintos"></a>

### Autovalores Reais e Distintos

Então seja $A \in {\mathbb{R}}^{2 \times 2}$, e $v_{i},\lambda_{i}$ o $i$-ésimo autovetor e autovalor de $A$, respectivamente. A solução geral do [sistema de EDOs de primeira ordem](#system_ode_first_order) é:

$$x(t) = c_{1}v_{1}e^{\lambda_{1}t} + c_{2}v_{2}e^{\lambda_{2}t}$$ <a id="general_solution_system"></a>

Onde $c_{i}$ é determinado pela condição inicial $x(0) = x_{0}$.

A Bebel não gosta da notação proposta na [solução geral do sistema](#general_solution_system), então vamos escrever a solução do jeito da patroa:

$$x(t) = X\Lambda X^{- 1} \cdot x_{0}$$ <a id="equation_bebel"></a>

Onde $X\Lambda X^{- 1}$ é a decomposição espectral de $A$ e:

$$
\Lambda = \begin{pmatrix} e^{\lambda_{1}t} & 0 \\ 0 & e^{\lambda_{2}t} \end{pmatrix}
$$

<a id="section_autovalores_reais_repetidos"></a>

### Autovalores Reais Repetidos

Seja $A \in {\mathbb{R}}^{2 \times 2}$ com autovalor $\lambda$ de multiplicidade $2$. Seja $v_{1}$ um autovetor associado. Para montar a solução da forma [equação da solução do sistema](#equation_bebel), precisamos de *2* autovetores. Vamos usar a matriz:

$$
B = \begin{pmatrix} \lambda & t \\ 0 & \lambda \end{pmatrix}
$$

**Propriedade**

Se $A$ possui autovalor $\lambda$ de multiplicidade 2 e apenas um autovetor $v_{1}$, escolha um vetor qualquer $v_{2}$ tal que $(A - \lambda I)v_{2} = v_{1}$.

A solução geral é

$$x(t) = e^{\lambda t} \cdot \left( c_{1}v_{1} + c_{2} \cdot \left( v_{2} + tv_{1} \right) \right)$$.

<a id="section_autovalores_complexos"></a>

### Autovalores Complexos

**Propriedade**

Para autovalores $\lambda_{\left\{ 1,2 \right\}} = \alpha \pm i\beta$ ($\beta \neq 0$) com autovetor complexo $v = u + iw$, obtém-se a solução real

$$
x(t) = e^{\alpha t}\left\lbrack c_{1} \cdot \left( u \cdot \cos(\beta t) - w \cdot \sin(\beta t) \right) + c_{2} \cdot \left( u \cdot \sin(\beta t) + w \cdot \cos(\beta t) \right) \right\rbrack.
$$

Classificação rápida:

- **Espiral estável**: $\alpha < 0$

- **Espiral instável**: $\alpha > 0$

- **Centro**: $\alpha = 0$

<a id="section_classificacao_pontos_criticos"></a>

### Classificação de Pontos Críticos (2 × 2)

**Propriedade**

Seja $A \in {\mathbb{R}}^{2 \times 2}$ com autovalores $\lambda_{1}$ e $\lambda_{2}$.

- **Nó estável**: $\lambda_{1} < 0$, $\lambda_{2} < 0$ (com $t \rightarrow \infty$ a porra toda vai pra $0$)

- **Nó instável**: $\lambda_{1} > 0$, $\lambda_{2} > 0$ (com algum autovalor positivo, $t \rightarrow \infty \Rightarrow$ a porra toda diverge)

- **Ponto de sela**: $\lambda_{1} \cdot \lambda_{2} < 0$ (se tiver um negativo e outro positivo, converge de ladinho e diverge de ladinho também)

- **Espiral estável**: $\alpha < 0$ e $\beta \neq 0$ (com $t \rightarrow \infty$ a porra toda vai pra $0$)

- **Espiral instável**: $\alpha > 0$ e $\beta \neq 0$ (com algum autovalor positivo, $t \rightarrow \infty \Rightarrow$ a porra toda diverge)

- **Centro**: $\alpha = 0$ e $\beta \neq 0$ (mó paz)

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/equacoes-diferenciais-ordinarias/a2.md) · [Apresentação e contexto da fonte](../../trilhas/equacoes-diferenciais-ordinarias/a2.md#apresentacao-original)

- Anterior: [Convolução](transformada-de-laplace.md#convolucao)
