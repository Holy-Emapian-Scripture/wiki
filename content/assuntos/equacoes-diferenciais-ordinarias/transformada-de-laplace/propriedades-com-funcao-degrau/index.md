---
layout: "default"
title: "Propriedades com Função degrau — Transformada de Laplace"
tipo: "conteudo"
disciplina: "Equações Diferenciais Ordinárias"
origem: "3 semestre/EDO/RecapA2.md"
trilha: "../../../../trilhas/equacoes-diferenciais-ordinarias/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 5
---

[Equações Diferenciais Ordinárias](../../index.md) · [Transformada de Laplace](../index.md)

<!-- wiki:original:inicio -->
<a id="section_propriedades_com_funcao_degrau"></a>

# Propriedades com Função degrau

**Propriedade**

Se $F(s) = L\left\{ f(t) \right\}$ existe, dada $f:{\mathbb{R}} \rightarrow {\mathbb{R}}$, então:

$$L\left\{ u_{c}(t)f(t - c) \right\} = e^{- sc} \cdot F(s)$$

**Propriedade**

Se $F(s) = L\left\{ f(t) \right\}$ existe, dada $f:{\mathbb{R}} \rightarrow {\mathbb{R}}$, então:

$$L\left\{ e^{ct}f(t) \right\} = F(s - c)$$

Ou equivalentemente:

$$e^{ct}f(t) = L^{- 1}\left\{ F(s - c) \right\}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/equacoes-diferenciais-ordinarias/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/equacoes-diferenciais-ordinarias/a2.md#apresentacao-original)

- Anterior: [Função degrau](../funcao-degrau/index.md)
- Próximo: [Função Impulso](../funcao-impulso/index.md)
