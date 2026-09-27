---
layout: "default"
title: "As generalizações do KKT — Otimização com restrições genéricas"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 18
---

[Otimização para Ciência de Dados](../../index.md) · [Otimização com restrições genéricas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-23"></a>

# As generalizações do KKT

Agora queremos generalizar totalmente o KKT, então vamos aos poucos. Lembre que, até que falemos o contrário, estamos considerando o problema [\[optimization-with-generic-restrictions\]](../index.md#optimization-with-generic-restrictions)

Antes de entrarmos diretamente no teorema KKT generalizado, vamos agora fazer uma definição que tem uma razão matemática, mas acaba por nos ajudar em alguns casos. Essa definição evita condições redundantes no nosso problema, ja que elas podem acabar nos atrapalhando. Faremos um exemplo para mostrar essa ajuda

<a id="licq"></a>

**Definição: Condições de qualificação de independência linear**

Sejam $g_{1},\ldots,g_{m}:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ e $h_{1},\ldots,h_{p}:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ continuamente diferenciáveis e $x^{\ast} \in {\mathbb{R}}^{n}$, defina: $$I\left( x^{\ast} \right) ≔ \left\{ i \in \lbrack m\rbrack:g_{i}\left( x^{\ast} \right) = 0 \right\}$$ Dizemos que LICQ (Linear Independent Condition Qualification) é satisfeita em $x^{\ast}$ para as funções $g_{1},\ldots,g_{m}$ e $h_{1},\ldots,h_{p}$ se $$\left\{ \nabla g_{i}\left( x^{\ast} \right):i \in I\left( x^{\ast} \right) \right\} \cup \left\{ \nabla h_{j}\left( x^{\ast} \right):j \in \lbrack p\rbrack \right\}\text{ é linearmente independente }$$

Definição feita, vamos enunciar o novo teorema KKT

<a id="generic-kkt"></a>

**Teorema: KKT**

Se $x^{\ast}$ é um ponto de mínimo local de $f(x)$ no problema [\[optimization-with-generic-restrictions\]](../index.md#optimization-with-generic-restrictions) e a [\[licq\]](#licq) é satisfeita em $x^{\ast}$, isso implica que: $$\begin{array}{r} \exists\lambda_{1},\ldots,\lambda_{m} \geq 0,\ \exists\mu_{1},\ldots,\mu_{p} \in {\mathbb{R}} \\ \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}\nabla g_{i}\left( x^{\ast} \right) + \sum_{j = 1}^{p}\mu_{j}\nabla h_{j}\left( x^{\ast} \right) = 0 \\ \lambda_{i}g_{i}\left( x^{\ast} \right) = 0\text{\quad\quad}i \in \lbrack m\rbrack \\ g_{i}\left( x^{\ast} \right) \leq 0\text{\quad\quad}i \in \lbrack m\rbrack \\ h_{j}\left( x^{\ast} \right) = 0\text{\quad\quad}j \in \lbrack p\rbrack \end{array}$$

**Exemplo: Utilidade da LICQ**

aaaaaaaaaaa preencher aqui aaaaaaaaaaaaa

Agora que vimos esses teoremas e condições, vamos fazer uma definição para facilitar em algumas terminologias:

**Definição: Ponto KKT**

Considere o problema [\[optimization-with-generic-restrictions\]](../index.md#optimization-with-generic-restrictions), onde $f$, $g_{1}$, …, $g_{m}$, $h_{1}$, …, $h_{p}$ são continuamente diferenciáveis no ${\mathbb{R}}^{n}$. Um ponto $x^{\ast}$ viável, ou seja, que satisfaz as condições do cojunto viável, é chamado de **ponto KKT** quando $\exists\lambda_{1},\ldots,\lambda_{m} \geq 0$ e $\exists\mu_{1},\ldots,\mu_{p} \in {\mathbb{R}}$ tais que: $$\begin{aligned} \nabla f\left( x^{\ast} \right) + \sum_{i = 1}^{m}\lambda_{i}\nabla g_{i}\left( x^{\ast} \right) + \sum_{j = 1}^{p}\mu_{j}\nabla h_{j}\left( x^{\ast} \right) & = 0 \\ \lambda_{i}g_{i\left( x^{\ast} \right)} & = 0\text{\quad\quad}i \in \lbrack m\rbrack \end{aligned}$$

Isso facilita um pouco a terminologia pois podemos resumir o [\[generic-kkt\]](#generic-kkt) em dizer que um ponto de LICQ não pode ser um ponto de mínimo se ele não for KKT

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Lagrangeano](../lagrangeano/index.md)
- Próximo: [Caso Convexo](../caso-convexo/index.md)
