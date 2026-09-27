---
layout: "default"
title: "Testando Hipóteses sobre a Média de uma Normal quando a Variância é Desconhecida — Testes $t$"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 29
---

[Inferência Estatística](../../index.md) · [Testes $t$](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-29"></a>

# Testando Hipóteses sobre a Média de uma Normal quando a Variância é Desconhecida

Consideremos $X_{1},\ldots,X_{n}$ uma amostra de uma distribuição normal com média $\mu$ e variância $\sigma^{2}$ desconhecidas, e também que trabalhamos com as hipóteses: $$\begin{array}{r} H_{0}:\mu \leq \mu_{0} \\ H_{1}:\mu > \mu_{0} \end{array}$$<a id="t-test-mu-hypothesis-1"></a>

O espaço paramétrico $\Omega$ suprime todo vetor bidimensiona $\left( \mu,\sigma^{2} \right)$ com $\mu \in ( - \infty,\infty)$ e $\sigma^{2} > 0$. Aqui, definimos a estatística de teste $U$ como: $$U = \sqrt{n} \cdot \frac{{\overline{X}}_{n} - \mu_{0}}{\sigma}'$$<a id="u-statistic"></a> onde o teste rejeita $H_{0}$ se $U \geq c$. Sabemos que a distribuição de $U$ é uma $t$ com $n - 1$ graus de liberdade, por isso os testes que utilizam de $U$ são chamados de **testes $t$**. Quando invertemos as hipóteses: $$\begin{array}{r} H_{0}:\mu \geq \mu_{0} \\ H_{1}:\mu < \mu_{0} \end{array}$$<a id="t-test-mu-hypothesis-2"></a> o teste vira da forma “rejeite $H_{0}$ quando $U \leq c$”

**Exemplo**

No [\[hospital-example-t-test\]](../index.md#hospital-example-t-test), se a gente quisesse um teste de tamanho $\alpha_{0}$, a gente poderia usar o teste $t$ que rejeita $H_{0}$ se a estatística $U$ for menor ou igual a um $c$ (escolhemos $c$ de forma a fazer o teste ter tamanho $\alpha_{0}$)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Testes $t$](../index.md)
- Próximo: [Propriedades dos testes $t$](../propriedades-dos-testes-t/index.md)
