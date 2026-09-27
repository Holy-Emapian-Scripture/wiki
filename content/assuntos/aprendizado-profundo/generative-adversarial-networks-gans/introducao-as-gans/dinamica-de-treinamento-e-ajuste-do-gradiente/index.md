---
layout: "default"
title: "Dinâmica de Treinamento e Ajuste do Gradiente — Introdução às GANs"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 63
---

[Aprendizado Profundo](../../../index.md) · [Generative Adversarial Networks (GANs)](../../index.md) · [Introdução às GANs](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-71"></a>

# Dinâmica de Treinamento e Ajuste do Gradiente

O treinamento fica alterando entre atualizar os pesos do **discriminador** e os pesos do **gerador**

**Treinamento de uma GAN**

1.  **function** trainGan($G$, $D$) {

    1.  **for each** *epoch* {

        1.  **for** $k$ **do** {

            1.  $\left\{ z^{(1)},\ldots,z^{(m)} \right\} \sim p_{z}$

            2.  $\left\{ x^{(1)},\ldots,x^{(m)} \right\} \sim p_{\text{data}}$

            3.  $\nabla_{\varphi}\frac{1}{m}\sum_{i = 1}^{m}\left\lbrack \log D_{\varphi}\left( x^{(i)} \right) + \log\left( 1 - D_{\varphi}\left( G\left( z^{(i)} \right) \right) \right) \right\rbrack$

        2.  }

        3.  $\left\{ z^{(1)},\ldots,z^{(m)} \right\} \sim p_{z}$

        4.  $\nabla_{\omega}\frac{1}{m}\sum_{i = 1}^{m}\left\lbrack \log\left( 1 - D_{\varphi}\left( G\left( z^{(i)} \right) \right) \right) \right\rbrack$

    2.  }

2.  }

No entanto, essa abordagem precisa de um pequeno ajuste. Acontece que a função $\log(1 - D\left( G(z) \right))$ possui uma região extremamente plana quando $D\left( G(z) \right) \approx 0$, o que faz com que, no inicio do treinamento, o aprendizado seja **extremamente lento**.

Para contornar esse problema, em vez de minimizarmos $\log(1 - D\left( G(z) \right))$, maximizamos $\log(D\left( G(z) \right))$ com Gradient Ascent, fornecendo gradientes fortes para o gerador no início do treinamento, quando ele ainda está produzindo amostras de baixa qualidade.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Função objetivo](../funcao-objetivo/index.md)
- Próximo: [Evolução Arquitetural e uso em inferência](../evolucao-arquitetural-e-uso-em-inferencia/index.md)
