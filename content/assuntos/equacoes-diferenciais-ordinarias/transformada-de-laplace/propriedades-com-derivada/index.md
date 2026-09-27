---
layout: "default"
title: "Propriedades Com derivada — Transformada de Laplace"
tipo: "conteudo"
disciplina: "Equações Diferenciais Ordinárias"
origem: "3 semestre/EDO/RecapA2.md"
trilha: "../../../../trilhas/equacoes-diferenciais-ordinarias/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 3
---

[Equações Diferenciais Ordinárias](../../index.md) · [Transformada de Laplace](../index.md)

<!-- wiki:original:inicio -->
<a id="section_propriedades_com_derivada"></a>

# Propriedades Com derivada

**Propriedade**

Se $f:{\mathbb{R}} \rightarrow {\mathbb{R}}$ é derivável, então:

$$L\left\{ f'(t) \right\} = sL\left\{ f(t) \right\} - f(0)$$

Analogamente:

$$L\left\{ f''(t) \right\} = s^{2}L\left\{ f(t) \right\} - sf(0) - f'(0)$$

E assim por diante.

Resolver EDO’s com a transformada de Laplace se restringe a algebricamente buscar a inversa de $L\left\{ f(t) \right\}$, justamente a função procurada.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/equacoes-diferenciais-ordinarias/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/equacoes-diferenciais-ordinarias/a2.md#apresentacao-original)

- Anterior: [Definição](../definicao/index.md)
- Próximo: [Função degrau](../funcao-degrau/index.md)
