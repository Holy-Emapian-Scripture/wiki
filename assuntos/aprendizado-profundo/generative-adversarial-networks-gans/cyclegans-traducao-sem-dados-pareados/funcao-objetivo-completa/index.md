---
layout: "default"
title: "Função objetivo completa — CycleGANs (Tradução sem dados pareados)"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 71
---

[Aprendizado Profundo](../../../index.md) · [Generative Adversarial Networks (GANs)](../../index.md) · [CycleGANs (Tradução sem dados pareados)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-81"></a>

# Função objetivo completa

Nas cycle GANs, existem algumas losses que vão se agregar, cada uma garantindo que o modelo se comporte como esperamos, vamos passar por cada uma, mostrar o que elas fazem e como se comportam e mostrar a função objetivo final

Mas antes, por que a loss original não garante o comportamento esperado? Acontece que utilizando a perca original, ela sozinha não conseguiria garantir a **correspondência**, ou seja, se eu passar uma imagem de cavalo, ele poderia retornar **qualquer imagem de zebra aleatória**, e não a zebra correspondente àquela pose, iluminação, etc. Então precisamos de uma **loss adicional** que garanta essa correspondência.

<a id="secao-82"></a>

## Adversarial Loss

Introduzimos a loss clássica, só que aplicada para **cada uma das transformações**

$$\mathcal{L}_{\text{GAN}}\left( G,D_{Y},X,Y \right) = {\mathbb{E}}_{y \sim p_{\text{data}(y)}}\left\lbrack \log D_{Y}(y) \right\rbrack + {\mathbb{E}}_{x \sim p_{\text{data }}(x)}\left\lbrack \log(1 - D_{Y}\left( G(x) \right)) \right\rbrack$$ $$\mathcal{L}_{\text{GAN}}\left( F,D_{X},Y,X \right) = {\mathbb{E}}_{x \sim p_{\text{data}(x)}}\left\lbrack \log D_{X}(x) \right\rbrack + {\mathbb{E}}_{y \sim p_{\text{data }}(y)}\left\lbrack \log(1 - D_{X}\left( F(y) \right)) \right\rbrack$$

<a id="secao-83"></a>

## Consistency Loss

Outra característica que as cycle GANs devem manter é a consistência, ou seja, se meu modelo gerou uma imagem de cavalo $x$, então o gerador $F$ deve ser capaz de pegar a imagem gerada e transformar de volta na imagem original de cavalo $x$. $$\begin{array}{r} G\left( F(y) \right) \approx y,\forall y \in Y \\ F\left( G(x) \right) \approx x,\forall x \in X \end{array}$$

![Exemplo de consistência em CycleGANs](../../../assets/A1/cycle-consistency.png)

*Figura 61. Exemplo de consistência em CycleGANs*

A loss de consistência é dada por $$\mathcal{L}_{\text{consistency}}(G,F) = {\mathbb{E}}_{y \sim p_{\text{data }}(y)}⟦\vert G\left( F(y) \right) - y\|_{1}\rbrack + {\mathbb{E}}_{x \sim p_{\text{data }}(x)}⟦\vert F\left( G(x) \right) - x\|_{1}\rbrack$$

<a id="secao-84"></a>

## Identity Loss

Também queremos que a rede seja capaz de manter a identidade da imagem, ou seja, se eu passar uma imagem de zebra para o gerador de zebra, ele deve retornar a mesma imagem de zebra, e não uma imagem de cavalo ou uma imagem de zebra alterada. Isso é importante para garantir que a rede não altere imagens que já estão no domínio desejado.

A loss de identidade é dada por $$\mathcal{L}_{\text{identity}}(G,F) = {\mathbb{E}}_{y \sim p_{\text{data }}(y)}⟦\vert G(y) - y\|_{1}\rbrack + {\mathbb{E}}_{x \sim p_{\text{data }}(x)}⟦\vert F(x) - x\|_{1}\rbrack$$

<a id="secao-85"></a>

## Loss completa

Reunindo todas as loss juntas, vamos obter a função objetivo completa das CycleGANs, que é uma combinação ponderada das três losses mencionadas: $$\begin{aligned} \mathcal{L}(G,F,D_{X},D_{Y}) = & \lambda_{\text{GAN }}\left\lbrack \mathcal{L}_{\text{GAN}}\left( G,D_{Y},X,Y \right) + \mathcal{L}_{\text{GAN}}\left( F,D_{X},Y,X \right) \right\rbrack \\ & + \lambda_{\text{consistency }}\mathcal{L}_{\text{consistency}}(G,F) \\ & + \lambda_{\text{identity }}\mathcal{L}_{\text{identity}}(G,F) \end{aligned}$$

Dessa forma, podemos reescrever o aprendizado da nossa cycle GAN como $$\min\limits_{G,F}\max\limits_{D_{X},D_{Y}}\mathcal{L}(G,F,D_{X},D_{Y})$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Estrutura de pareamento duplo](../estrutura-de-pareamento-duplo/index.md)
- Próximo: [Arquitetura de CycleGANs](../arquitetura-de-cyclegans/index.md)
