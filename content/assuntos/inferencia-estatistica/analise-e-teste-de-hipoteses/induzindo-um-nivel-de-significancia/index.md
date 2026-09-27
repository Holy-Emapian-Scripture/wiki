---
layout: "default"
title: "Induzindo um nível de significância — Análise e Teste de Hipóteses"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 23
---

[Inferência Estatística](../../index.md) · [Análise e Teste de Hipóteses](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-23"></a>

# Induzindo um nível de significância

Nós queremos testar: $$\begin{array}{r} H_{0}:\theta \in \Omega_{0} \\ H_{1}:\theta \in \Omega_{1} \end{array}$$

Seja $T$ uma estatística e suponha que vamos rejeitar $H_{0}$ se $T \geq c$. Vamos supor que queremos que nosso teste tenha um nível específico de significância $\alpha_{0}$. Temos: $$\pi(\theta\vert \delta) = {\mathbb{P}}(T \geq c\vert \theta)\underset{\text{ Queremos}}{\underbrace{\rightarrow}}\sup\limits_{\theta \in \Omega_{0}}{\mathbb{P}}(T \geq c\vert \theta) \leq \alpha_{0}$$

perceba que o lado direito é não-crescente em $c$, então a desigualdade é satisfeita para altos valores de $c$, então devemos fazer $c$ o menor possível sem que a desigualdade seja desfeita, e também queremos que $\pi(\theta\vert \delta)$ seja o maior possível para $\theta \in \Omega_{1}$. Quando $T$ tem distribuição contínua, costuma ser fácil achar um $c$ apropriado

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Função de Poder e Tipos de Erro](../funcao-de-poder-e-tipos-de-erro/index.md)
- Próximo: [p-valor](../p-valor/index.md)
