---
layout: "default"
title: "Aplicações das cGANs — GANs Condicionais (cGANs)"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 68
---

[Aprendizado Profundo](../../../index.md) · [Generative Adversarial Networks (GANs)](../../index.md) · [GANs Condicionais (cGANs)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-76"></a>

# Aplicações das cGANs

<a id="secao-77"></a>

## Sensoriamento remoto

**Problema**: Imagens ópticas de satélite sofrem com cobertura de nuvens, enquanto dados de Radar de Abertura Sintética (SAR) penetram nuvens e funcionam em qualquer condição meteorológica, mas são difíceis de interpretar

**Solução**: O modelo recebe a imagem SAR como condição $x$ e sintetiza a imagem óptica correspondente $G(x)$, permitindo a observação contínua da superfície terrestre mesmo com interferência atmosférica

![Exemplo de aplicação de cGANs em sensoriamento remoto](../../../assets/A1/cgan-sar.png)

*Figura 59. Exemplo de aplicação de cGANs em sensoriamento remoto*

<a id="secao-78"></a>

## Síntese Controlável de Lesões de Pele para Aumento de Dados

**Desafio**: Falta de dados rotulados e diversidade de formas/texturas para treinar redes de segmentação de câncer de pele.

**Abordagem cGAN**: Utiliza **Curvas de Bézier aleatórias** para gerar a máscara de formato da lesão. Tira retalhos de textura (**texture patches**) para áreas de pele e de lesão. A cGAN sintetiza dermoscopias altamente realistas combinando a forma geométrica e as texturas\[4\].

**Resultado**: O uso dessas amostras sintéticas no treinamento elevou significativamente a acurácia de modelos como U-Net, PSPNet e DeepLabv3

![Exemplo de aplicação de cGANs em síntese controlável de lesões de pele](../../../assets/A1/cgan-skin-lesion.png)

*Figura 60. Exemplo de aplicação de cGANs em síntese controlável de lesões de pele*

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Arquitetura Clássica](../arquitetura-classica/index.md)
- Próximo: [CycleGANs (Tradução sem dados pareados)](../../cyclegans-traducao-sem-dados-pareados/index.md)
