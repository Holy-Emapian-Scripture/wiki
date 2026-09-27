---
layout: "default"
title: "Interpretação via regularização — Método do Gradiente"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A2.md"
trilha: "../../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 5
---

[Otimização para Ciência de Dados](../../index.md) · [Método do Gradiente](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Interpretação via regularização

Outra formas que podemos ver e interpretar o algoritmo do gradiente é resolver a seguinte fórmula: $$x^{(t + 1)} = \text{ argmin}_{x \in {\mathbb{R}}^{n}}\left( \underset{\text{ Aproximação Linear }}{\underbrace{f\left( x^{(t)} \right) + \left( x - x^{(t)} \right)^{T}\nabla f\left( x^{(t)} \right)}} + \underset{\text{ Regularização Proximal }}{\underbrace{\frac{1}{2\alpha^{(t)}}\| x - x^{(t)}\|_{2}^{2}}} \right)$$

Ou seja, eu vou pegar qual que é o valor que minimiza a aproximação linear regularizada por um termo quadrático

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md#apresentacao-original)

- Anterior: [Caso Convexo](../caso-convexo/index.md)
- Próximo: [Método do Subgradiente](../../metodo-do-subgradiente/index.md)
