---
layout: "default"
title: "Convolução — Transformada de Laplace"
tipo: "conteudo"
disciplina: "Equações Diferenciais Ordinárias"
origem: "3 semestre/EDO/RecapA2.md"
trilha: "../../../../trilhas/equacoes-diferenciais-ordinarias/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 8
---

[Equações Diferenciais Ordinárias](../../index.md) · [Transformada de Laplace](../index.md)

<!-- wiki:original:inicio -->
<a id="section_convolucao"></a>

# Convolução

Dadas $F(s) = L\left\{ f(t) \right\}$ e $G(s) = L\left\{ g(t) \right\}$, a transformada do produto pode ser calculada como:

$$H(s) = F(s)G(t) = L\left\{ h(t) \right\}$$

Onde:

$$h(t) = \int_{0}^{t}f(t - \tau)g(\tau)d\tau = \int_{0}^{t}f(\tau)g(t - \tau)d\tau$$

A função $h$ é chamada de convolução de $f$ e $g$, denotada por $f \ast g$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/equacoes-diferenciais-ordinarias/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/equacoes-diferenciais-ordinarias/a2.md#apresentacao-original)

- Anterior: [Propriedades com Função Impulso](../propriedades-com-funcao-impulso/index.md)
- Próximo: [Sistemas de EDO’s de Primeira Ordem](../../sistemas-de-edos-de-primeira-ordem/index.md)
