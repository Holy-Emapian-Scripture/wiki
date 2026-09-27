---
layout: "default"
title: "Análise Bayesiana de Amostras Normais"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 12
---

[Inferência Estatística](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-12"></a>

# Análise Bayesiana de Amostras Normais

------------------------------------------------------------------------

Nesse capítulo, vamos fazer uma análise bayesiana completa quando o problema trata de amostras de uma distribuição **Normal**. Para facilitar algumas contas, vamos trocar a definição usual com variância para a definição com **precisão**

**Definição: Precisão**

A precisão de uma distribuição $N\left( \mu,\sigma^{2} \right)$ é $$\tau = \frac{1}{\sigma^{2}}$$

**Teorema: Densidade da Normal**

Seja $X \sim N(\mu,\tau)$, temos que a **função de densidade probabilística** de $X$ é: $$f\left( x\vert \mu,\tau \right) = \left( \frac{\tau}{2\pi} \right)^{\frac{1}{2}}\exp( - \frac{\tau}{2}(x - \mu)^{2})$$

**Corolário: Likelihood**

Sejam $X_{1},\ldots,X_{n}\vert \mu,\tau \sim N(\mu,\tau)$, temos que a função de verossimilhança é dada por: $$f\left( \underline{x}\vert \mu,\tau \right) = \left( \frac{\tau}{2\pi} \right)^{\frac{n}{2}}\exp( - \frac{1}{2}\tau\sum_{i = 1}^{n}\left( x_{i} - \mu \right)^{2})$$

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Família de Conjugados](familia-de-conjugados/index.md)
2. [Marginais](marginais/index.md)
3. [Distribuições Impróprias](distribuicoes-improprias/index.md)

## Percurso de estudo

[Trilha: A2](../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Intervalo de confiança para outros parâmetros](../intervalos-de-confianca/intervalo-de-confianca-para-outros-parametros/index.md)
- Próximo: [Família de Conjugados](familia-de-conjugados/index.md)
