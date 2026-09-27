---
layout: "default"
title: "Distribuições Impróprias — Análise Bayesiana de Amostras Normais"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 15
---

[Inferência Estatística](../../index.md) · [Análise Bayesiana de Amostras Normais](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Distribuições Impróprias

Utilizamos esses parâmetros mais por conveniência do que por qualquer outro motivo (Como uma convicção). Para a posteriori, utilizamos os seguintes hiperparâmetros: $$\alpha_{0} = - \frac{1}{2}\text{\quad\quad}\beta_{0} = 0\text{\quad\quad}\mu_{0} = 0\text{\quad\quad}\lambda_{0} = 0$$ assim, obtemos as seguintes pdf’s **a priori**: $$p(\mu) = 1\text{\quad\quad}p(\tau) = \frac{1}{2}\tau^{- 1}\text{\quad\quad}p(\mu,\tau) = \frac{1}{\tau}$$ Dessa forma, a posteriori fica: $$p(\mu,\tau) \propto \left\{ \tau^{\frac{1}{2}}\exp\left\lbrack \frac{- (n\pi)}{2}\left( \mu - {\overline{x}}_{n} \right)^{2} \right\rbrack \right\}\tau^{\frac{n - 1}{2} - 1}\exp\left\lbrack - \tau\frac{s_{n}^{2}}{2} \right\rbrack$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Marginais](../marginais/index.md)
- Próximo: [Estimadores não-viezados](../../estimadores-nao-viezados/index.md)
