---
layout: "default"
title: "Grau Máximo e Grau Mínimo — Redes Aleatórias"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A1.md"
trilha: "../../../../trilhas/ciencia-de-redes/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 9
---

[Ciência de Redes](../../index.md) · [Redes Aleatórias](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-13"></a>

# Grau Máximo e Grau Mínimo

Dependendo do contexto analisado, pode ser de grande interesse saber os valores esperados do **maior grau** de uma rede e do **menor grau**. Para descobrir o **maior grau**, precisamos que, na rede, tenhamos **no máximo** um nó com grau maior que $k_{\text{max}}$. Isso significa que a área do gráfico da distribuição **em frente** a $k_{\max}$ é aproximadamente 1: $$\begin{array}{r} N \cdot {\mathbb{P}}(K \geq k_{\max}) \approx 1 \\ N \cdot \left( 1 - {\mathbb{P}}(K < k_{\max}) \right) \approx 1 \end{array}$$

E podemos usar um argumento análogo, afirmando que deveríamos ter, no máximo, apenas um nó com grau menor que $k_{\min}$, então teríamos: $$N \cdot {\mathbb{P}}(K \leq k_{\min} - 1) = 1$$ Assim resolvemos as duas equações para achar $k_{\min}$ e $k_{\max}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Anterior: [Coeficiente de Clustering](../coeficiente-de-clustering/index.md)
- Próximo: [Conclusão](../conclusao/index.md)
