---
layout: "default"
title: "Quociente de Rayleigh — Quociente de Rayleigh e Iteração Inversa"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 39
---

[Álgebra Linear Numérica](../../index.md) · [Quociente de Rayleigh e Iteração Inversa](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-39"></a>

# Quociente de Rayleigh

**Definição: Quociente de Rayleigh**

O Quociente de Rayleigh de um vetor $x \in {\mathbb{R}}^{m}$ é o escalar $$r(x) = \frac{x^{T}Ax}{x^{T}x}$$

Perceba que se $x$ é um autovetor de $A$ com autovalor $\lambda$ associado, então $r(x) = \lambda$. Uma motivação para essa fórmula é pensarmos no seguinte: Dado um $x$, qual escalar $\alpha$ “mais se comporta como um autovalor” no sentido de minimizar $\| Ax - \alpha x\|$? Isso é um problema de mínimos quadrados $m \times 1$ da forma $\alpha x \approx Ax$. Se escrevermos as equações normais: $$x^{T}\alpha x = x^{T}Ax \Rightarrow \alpha = r(x)$$ A gente pode fazer essas ideias mais quantitativas se tomarmos $r(x):{\mathbb{R}}^{m} \rightarrow {\mathbb{R}}$, então podemos tomar interesse no comportamento local de $r(x)$ quando $x$ está perto de um autovalor. A gente pode calcular as derivadas parciais para isso: $$\begin{array}{r} \frac{\partial r(x)}{\partial x_{j}} = \frac{\frac{\partial}{\partial x_{j}}\left( x^{T}Ax \right)}{x^{T}x}\frac{- \left( \left( x^{T}Ax \right)\frac{\partial}{\partial x_{j}}\left( x^{T}x \right) \right)}{\left( x^{T}x \right)^{2}} \\ = \frac{2(Ax)_{j}}{x^{T}x} - \frac{\left( x^{T}Ax \right)2x_{j}}{\left( x^{T}x \right)^{2}} = \frac{2}{x^{T}x}\left( Ax - r(x)x \right)_{j} \end{array}$$ Podemos então expressar o gradiente como: $$\nabla r(x) = \frac{2}{x^{T}x}\left( Ax - r(x)x \right)$$ É bem fácil de ver que, se a gente tem $\nabla r(x) = 0$, com $x \neq 0$ então $x$ é um autovetor de $A$ (Tenta fazer mentalmente e lembra que $r(x) \in {\mathbb{R}}$) e o inverso também, se $x$ é autovetor de $A$ então $\nabla r(x) = 0$.

Expressando geometricamente, os autovetores de $A$ são pontos estacionários (pontos críticos) de $r(x)$ e os autovalores de $A$ são os valores de $r(x)$ nesses pontos críticos.

<a id="rayleigh-coefficient-example"></a>

![$r(x)$ em função dos vetores no ${\mathbb{R}}^{2}$ para a matriz $\begin{pmatrix} 5 & 4 \\ 0 & 3 \end{pmatrix}$](../../assets/r%28x%29-example.png)

*Figura 7. $r(x)$ em função dos vetores no ${\mathbb{R}}^{2}$ para a matriz $\begin{pmatrix} 5 & 4 \\ 0 & 3 \end{pmatrix}$*

Mas algo interessante que podemos perceber é que, aparentemente, não há apenas **um** ponto crítico nessa função, mas uma **reta**. Ué, mas por quê? O que acontece se, dado que $Ax = \lambda x$, eu pego um múltiplo $\mu x$ de $x$? $$A(\mu x) = \lambda(\mu x)$$ $\mu x$ **ainda é autovetor de $A$**. O que isso quer dizer? Quer dizer que, se um vetor $x$ faz com que $r(x)$ seja igual a um autovalor de $A$, então $\alpha x$ também o fará $\forall\alpha \in {\mathbb{R}}$. Não acredita em mim? Veja por conta própria: $$\begin{array}{r} \text{ Dado que }Ax = \lambda x \\ r(\alpha x) = \frac{(\alpha x)^{T}A(\alpha x)}{(\alpha x)^{T}(\alpha x)} = \frac{\alpha^{2}x^{T}Ax}{\alpha^{2}x^{T}Ax} = \frac{\lambda x^{T}x}{x^{T}x} = \lambda \end{array}$$ Mas podemos contornar isso **limitando** o domínio de $r(x)$. Podemos fazer isso fazendo com $r(x):{\mathbb{R}}^{m} \rightarrow {\mathbb{R}}\text{ tal que }\| x\| = 1$, dessa forma, limitamos a $m$-esfera unitária em ${\mathbb{R}}^{m}$ (No exemplo da [\[rayleigh-coefficient-example\]](#rayleigh-coefficient-example), seria uma circunferência em ${\mathbb{R}}^{2}$). Dessa forma, em vez de serem retas com infinitos valores possíveis para zerar $\nabla r(x)$, temos pontos isolados **na** esfera.

![Mesma função da [\[rayleigh-coefficient-example\]](#rayleigh-coefficient-example) limitada dentro do cilíndro $x^{2} + y^{2} \leq 1$. Só não coloquei $= 1$ pois o Geogebra não conseguia fazer a plotagem](../../assets/r%28x%29-unit-sphere.png)

*Figura 8. Mesma função da [\[rayleigh-coefficient-example\]](#rayleigh-coefficient-example) limitada dentro do cilíndro $x^{2} + y^{2} \leq 1$. Só não coloquei $= 1$ pois o Geogebra não conseguia fazer a plotagem*

Seja $q_{j}$ um autovetor de $A$, do fato que $\nabla r\left( q_{j} \right) = 0$ nós chegamos que: $$r(x) - r\left( q_{j} \right) = O\left( \| x - q_{j}\|^{2} \right),x \rightarrow q_{j}$$ Não precisamos entender o passo-a-passo até chegar nesse resultado, o importante dele é que o quociente de Rayleigh é uma **ótima** aproximação dos autovalores de $A$.

Um jeito mais explícito de vermos isso é expressar $x$ como uma combinação linear dos autovetores de $A$ (A gente pode fazer isso já que todos os autovetores de uma matriz são L.I), ou seja: $x = \sum_{j = 1}^{m}a_{j}q_{j}$, o que significa que $r(x) = \sum_{j = 1}^{m}a_{j}^{2}\lambda_{j}/\sum_{j = 1}^{m}a_{j}^{2}$, que é uma média ponderada dos autovalores de $A$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Restrição à matrizes reais e simétricas](../restricao-a-matrizes-reais-e-simetricas/index.md)
- Próximo: [Iteração por Potências](../iteracao-por-potencias/index.md)
