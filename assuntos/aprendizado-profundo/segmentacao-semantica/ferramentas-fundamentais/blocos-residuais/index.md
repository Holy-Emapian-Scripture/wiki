---
layout: "default"
title: "Blocos Residuais — Ferramentas Fundamentais"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 9
---

[Aprendizado Profundo](../../../index.md) · [Segmentação Semântica](../../index.md) · [Ferramentas Fundamentais](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Blocos Residuais

Normalmente, redes neurais são straight-to-the-point, nós temos a entrada $x$ e a partir disso a rede modela uma função complexa $F$ tal que $$y = F(x)$$

no entanto, pode existir casos em que $y$ é MUITO parecido com $x$ com leves ajustes, e isso, surpreendentemente, pode dificultar muito o aprendizado da rede. Para consertar isso, os chamados **blocos residuais** foram introduzidos, de forma que a rede não aprende a relação direta entre $x$ e $y$, mas sim a **diferença** entre eles (o quão diferente $y$ é de $x$), ou seja, a rede aprende uma função $F$ tal que $$y = F(x) + x$$

O principal motivo dessa abordagem é o **gradiente no backpropagation**. Em redes comuns de deep-learning, o gradiente pode se tornar muito pequeno (ou até mesmo zero) à medida que é propagado para trás, dificultando o aprendizado. Com os blocos residuais, o gradiente pode fluir diretamente através da conexão de atalho, permitindo que a rede aprenda mais facilmente.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Convoluções Eficientes](../convolucoes-eficientes/index.md)
- Próximo: [Arquiteturas](../../arquiteturas/index.md)
