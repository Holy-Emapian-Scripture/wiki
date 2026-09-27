---
layout: "default"
title: "Formalismo Discreto — Redes Livres de Escala"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A1.md"
trilha: "../../../../trilhas/ciencia-de-redes/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 15
---

[Ciência de Redes](../../index.md) · [Redes Livres de Escala](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-19"></a>

# Formalismo Discreto

Para cálculos analíticos, é interessante deixar que os graus possam assumir qualquer tipo de valor real (Mesmo que apenas os naturais sejam possíveis). Seja $K$ a variável aleatória que indica o grau de um vértice escolhido aleatoriamente, temos que: $${\mathbb{P}}(K = k) = Ck^{- \gamma}$$

Normalizando, temos: $$\begin{array}{r} \int_{k_{\min}}^{\infty}{\mathbb{P}}(K = k)dk = 1 \\ \Rightarrow C = (\gamma - 1)k_{\min}^{\gamma - 1} \end{array}$$

Então temos que a distribuição segue a P.M.F: $${\mathbb{P}}(K = k) = (\gamma - 1)k_{\min}^{\gamma - 1}k^{- \gamma}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Anterior: [Redes Livres de Escala](../index.md)
- Próximo: [Centros](../centros/index.md)
