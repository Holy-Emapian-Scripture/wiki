---
layout: "default"
title: "Formulação da Loss — GANs Condicionais (cGANs)"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 66
---

[Aprendizado Profundo](../../../index.md) · [Generative Adversarial Networks (GANs)](../../index.md) · [GANs Condicionais (cGANs)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-74"></a>

# Formulação da Loss

Vamos definir nossa condição genérica como $c$, que pode ser um vetor de rótulos, uma imagem ou qualquer outra informação relevante. A função objetivo da cGAN é então modificada para incorporar essa condição: $$\min\limits_{\omega}\max\limits_{\varphi}\left\lbrack {\mathbb{E}}_{(c,y) \sim p_{\text{data}}}\left\lbrack \log D_{\varphi}(c,y) \right\rbrack + {\mathbb{E}}_{z \sim p_{\text{synthetic}}}\left\lbrack \log(1 - D_{\varphi}\left( c,G_{\omega}(c,z) \right)) \right\rbrack \right\rbrack$$

assim, o discriminador sabe a informação de qual classe a imagem pertence, e o gerador sabe qual classe ele deve gerar. Isso permite que o gerador produza amostras específicas de acordo com a condição fornecida.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [GANs Condicionais (cGANs)](../index.md)
- Próximo: [Arquitetura Clássica](../arquitetura-classica/index.md)
