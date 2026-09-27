---
layout: "default"
title: "Calculando p-valores — Análise e Teste de Hipóteses"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 25
---

[Inferência Estatística](../../index.md) · [Análise e Teste de Hipóteses](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-25"></a>

# Calculando p-valores

Se nossos testes são da forma “Rejeite $H_{0}$ quando $T \geq c$” para uma única estatística de teste, tem um jeito direto de calcular p-valores. Para cada $t$, deixe $\delta_{t}$ o teste que rejeita $H_{0}$ quando $T \geq t$. Então o p-valor quando $T = t$ é observado é o tamanho do teste $\delta_{t}$, ou seja, o p-valor é: $$\sup\limits_{\theta \in \Omega_{0}}\pi(\theta\vert \delta_{t}) = \sup\limits_{\theta \in \Omega_{0}}{\mathbb{P}}(T \geq t\vert \theta)$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [p-valor](../p-valor/index.md)
- Próximo: [Equivalência de testes e conjuntos de confiança](../equivalencia-de-testes-e-conjuntos-de-confianca/index.md)
