---
layout: "default"
title: "Gradiente Proximal"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A2.md"
trilha: "../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 8
---

[Otimização para Ciência de Dados](index.md)

<!-- wiki:original:inicio -->
<a id="secao-8"></a>

# Gradiente Proximal

------------------------------------------------------------------------

Esses métodos resolvem naturalmente algumas limitações do método projetado. Um dos principais problemas é que, para conjuntos não triviais, calcular as projeções pode ser **muito** custoso, então o que fazer? Algo muito comum, é adicionar uma função de custo, que **penaliza** conforme a resposta de **afasta** do conjunto viável $C$. Então vamos considerar o novo problema: $$\min\limits_{x \in {\mathbb{R}}^{n}}f(x) + g(x)$$ para funções $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$, onde $f$ possui gradientes ou pelo menos subgradientes em todos os pontos e $g:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ convexa. Nós poderíamos tentar aplicar o [método do subgradiente](metodo-do-subgradiente.md) diretamente à $f + g$, só que essa função pode ser mais complexa e nem ser diferenciável, então utilizamos uma família de métodos onde mantemos $g$ preservada e usamos subgradientes apenas de $f$ $$x^{(t + 1)} = \text{ argmin}_{x \in {\mathbb{R}}^{n}}\left\{ f\left( x^{(t)} \right) + < g^{(t)},x - x^{(t)} > + g(x) + \frac{1}{2\alpha^{(t)}}\| x - x^{(t)}\|_{2}^{2} \right\}$$<a id="recursive-proximal-formula"></a> onde $g^{(t)}$ é o subgradiente de $f$ no ponto corrente $x^{(t)}$. Perceba que, ao adicionar $g(x)$ dentro do $\text{argmin}$, ele acaba por regularizar a função **dependendo** da escolha de $g(x)$

**Exemplo: Restrição por Penalização**

Uma penalização muito comum é transformar as condições de restrições de um conjunto viável em uma função, de forma que: $$I_{C}(x) = \begin{cases} 0\text{\quad\quad} & x \in C \\ + \infty\text{\quad\quad} & x \notin C \end{cases}$$ De forma que os problemas: $$\min\limits_{x \in C}f(x)\text{\quad\quad}\min\limits_{x \in {\mathbb{R}}^{n}}f(x) + I_{C}(x)$$ são equivalentes

Podemos fazer uma definição útil para expressar modularmente o algoritmo descrito anteriormente

**Definição: Operador Proximal**

O operador proximal de uma função **convexa** $g$ é o operador que, para cada $x \in {\mathbb{R}}^{n}$, associa o vetor: $$\text{ prox}_{g}(x) ≔ \text{ argmin}_{y \in {\mathbb{R}}^{n}}\left\{ g(y)\frac{1}{2}\| y - x\|_{2}^{2} \right\}$$

Com essa definição, é fácil ver que a equação [\[recursive-proximal-formula\]](#recursive-proximal-formula) é equivalente a: $$x^{(t + 1)} = \text{ prox}_{g}\left( x^{(t)} - \alpha^{(t)}g^{(t)} \right)$$

<a id="proximal-gradient"></a>

1.  **func** ProximalGradientMethod($f = g + r$) {

    1.  $x^{\left\{ (1) \right\}} \in {\mathbb{R}}^{n}$

    2.  $\left\{ \alpha^{(t)} \right\} \subset (0,\infty)$

    3.  **for** $t \in \lbrack T\rbrack$ **do** {

        1.  Compute $\nabla g\left( x^{(t)} \right)$

        2.  $z^{(t + 1)} = x^{(t)} - \alpha^{(t)}\nabla g\left( x^{(t)} \right)$

        3.  $x^{(t + 1)} = \text{ prox}_{\alpha^{(t)}r}\left( z^{(t + 1)} \right)$

    4.  }

    5.  **return** $${\overline{x}}^{(T)} ≔ \frac{\sum_{t = 1}^{T}\alpha^{(t)}x^{(t)}}{\sum_{t = 1}^{T}\alpha^{(t)}}$$

2.  }

*Figura 6. Método do Gradiente Proximal*

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../trilhas/otimizacao-para-ciencia-de-dados/a2.md) · [Apresentação e contexto da fonte](../../trilhas/otimizacao-para-ciencia-de-dados/a2.md#apresentacao-original)

- Anterior: [Gradiente Projetado](gradiente-projetado.md)
- Próximo: [Método de Newton](metodo-de-newton.md)
