---
layout: "default"
title: "Condições para soluções globais — Otimização Irrestrita"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A1.md"
trilha: "../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 7
---

[Otimização para Ciência de Dados](../../index.md) · [Otimização Irrestrita](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# Condições para soluções globais

<a id="sufficient-condition-global-minimum"></a>

**Teorema**

Seja $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ duas vezes continuamente diferenciável. Suponha que: $$\nabla^{2}f(x) \succeq 0,\ \forall x \in {\mathbb{R}}^{n}$$ Então, em todo ponto estacionário de $f$, esse ponto é um mínimo global

**Demonstração**

Pelo [\[linear-approximation\]](../definicoes-e-revisoes-de-calculo/index.md#linear-approximation), seja $x^{\ast} \in {\mathbb{R}}^{n}$ um ponto estacionário em $f$ e $\forall x \in {\mathbb{R}}^{n}$: $$f(x) - f\left( x^{\ast} \right) = \frac{1}{2}\left( x - x^{\ast} \right)^{T}\nabla^{2}f(\xi)\left( x - x^{\ast} \right)$$ Porém, vale que $\forall x,\ \nabla^{2}f(\xi) \succeq 0$. Temos então que: $$\forall x \in {\mathbb{R}}^{n},\ f(x) \geq f\left( x^{\ast} \right)$$ Logo, $x^{\ast}$ é ponto de mínimo global em $f$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/otimizacao-para-ciencia-de-dados/a1.md#apresentacao-original)

- Anterior: [Existência de pontos ótimos](../existencia-de-pontos-otimos/index.md)
- Próximo: [Funções quadráticas](../funcoes-quadraticas/index.md)
