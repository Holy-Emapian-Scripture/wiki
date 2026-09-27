---
layout: "default"
title: "Estrutura de pareamento duplo — CycleGANs (Tradução sem dados pareados)"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 70
---

[Aprendizado Profundo](../../../index.md) · [Generative Adversarial Networks (GANs)](../../index.md) · [CycleGANs (Tradução sem dados pareados)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-80"></a>

# Estrutura de pareamento duplo

Para realizar a tradução bidirecional entre dois domínios $X$ e $Y$, a arquitetura utiliza **dois geradores** e **dois discriminadores**

- Gerador $G:X \rightarrow Y$ e Discriminador $D_{Y}$: O gerador $G$ aprende a mapear imagens do domínio $X$ para o domínio $Y$, enquanto o discriminador $D_{Y}$ avalia a autenticidade das imagens geradas em relação às imagens reais do domínio $Y$ (por exemplo, se $X$ são imagens de cavalos e $Y$ são imagens de zebras, $G$ tenta gerar imagens de zebras a partir das de cavalos e $D_{Y}$ avalia se as imagens geradas são realmente imagens **reais** de **zebras**).

- Gerador $F:Y \rightarrow X$ e Discriminador $D_{X}$: O gerador $F$ aprende a mapear imagens do domínio $Y$ para o domínio $X$, enquanto o discriminador $D_{X}$ avalia a autenticidade das imagens geradas em relação às imagens reais do domínio $X$ (por exemplo, se $Y$ são imagens de zebras e $X$ são imagens de cavalos, $F$ tenta gerar imagens de cavalos a partir das de zebras e $D_{X}$ avalia se as imagens geradas são realmente imagens **reais** de **cavalos**).

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [CycleGANs (Tradução sem dados pareados)](../index.md)
- Próximo: [Função objetivo completa](../funcao-objetivo-completa/index.md)
