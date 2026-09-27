---
layout: "default"
title: "Equivalência de testes e conjuntos de confiança — Análise e Teste de Hipóteses"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 26
---

[Inferência Estatística](../../index.md) · [Análise e Teste de Hipóteses](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-26"></a>

# Equivalência de testes e conjuntos de confiança

Os teoremas a seguir mostram a equivalência de intervalos e conjuntos de confiança (o nome é bem intuitivo). Intuitivamente, um intervalo de confiança é um tipo específico de conjunto de confiança (com um tipo específico de regra)

**Teorema**

Seja $\underline{X} = \left\lbrack X_{1},\ldots,X_{n} \right\rbrack$ uma amostra de uma distribuição indexada por um parâmetro $\theta$. Seja $g(\theta)$ uma função e suponha que para todo possível valor $g_{0}$ de $g(\theta)$, existe um teste $\delta_{g_{0}}$ de nível $\alpha_{0}$ da hipótese $$\begin{array}{r} H_{0,g_{0}}:g(\theta) = g_{0} \\ H_{1,g_{0}}:g(\theta) \neq g_{0} \end{array}$$ Para cada possível valor de $\underline{x}$ de $\underline{X}$, defina: $$\omega(\underline{x}) = \left\{ g_{0}\vert \delta_{g_{0}}\text{ não rejeita }H_{0,g_{0}}\text{ se }\underline{X} = \underline{x}\text{ é visto} \right\}$$ e seja $\gamma = 1 - \alpha_{0}$, então o conjunto aleatório $w\left( \underline{X} \right)$ satisfaz $${\mathbb{P}}(g\left( \theta_{0} \right) \in \omega(\underline{X})\vert \theta = \theta_{0}) \geq \gamma\text{\quad\quad}\forall\theta_{0} \in \Omega$$

**Demonstração**

Seja $\theta_{0} \in \Omega$ um elemento arbitrário e defina $g_{0} = g\left( \theta_{0} \right)$. Como $\delta_{g_{0}}$ é um teste de nível $\alpha_{0}$, sabemos que: $${\mathbb{P}}(\delta_{g_{0}}\text{ não rejeitar }H_{0,g_{0}}\vert \theta = \theta_{0}) \geq 1 - \alpha_{0} = \gamma$$ Para cada $\underline{x}$, $g\left( \theta_{0} \right) \in \omega(\underline{x}) \Leftrightarrow$ o teste $\delta_{g_{0}}$ não rejeitar $H_{0,g_{0}}$ quando $\underline{X} = \underline{x}$ é visto $$\Rightarrow {\mathbb{P}}(g\left( \theta_{0} \right) \in \omega(\underline{X})\vert \theta = \theta_{0}) = A$$

**Definição: Conjunto de confiança**

Se um conjunto aleatório $\omega(\underline{X})$ satisfaz $${\mathbb{P}}(g\left( \theta_{0} \right) \in \omega(\underline{X})\vert \theta = \theta_{0}) \geq \gamma\text{\quad\quad}\forall\theta_{0} \in \Omega$$ então o chamamos de conjunto de confiança com coeficiente $\gamma$ para $g(\theta)$. Se a desigualdade for igualdade, o chamamos de exato

**Teorema**

Seja $X_{1},\ldots,X_{n}$ uma amostra aleatória de uma distribuição indexada por $\theta$ e $g:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ e seja $\omega(\underline{X})$ um conjunto de confiança $\gamma$ para $g(\theta)$. Para cada possível valor $g_{0}$ de $g(\theta)$, construa o teste $\delta_{g_{0}}$: $\delta_{g_{0}}$ não rejeita $H_{0,g_{0}} \Leftrightarrow g_{0} \in \omega(\underline{X})$. Então $\delta_{g_{0}}$ é um teste de nível $\alpha_{0} = 1 - \gamma$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Calculando p-valores](../calculando-p-valores/index.md)
- Próximo: [Testes de razão de verossimilhança](../testes-de-razao-de-verossimilhanca/index.md)
