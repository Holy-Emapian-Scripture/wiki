---
layout: "default"
title: "Convoluções com Stride — Convolutional Neural Networks (CNN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 25
---

[Aprendizado de Máquina](../../index.md) · [Convolutional Neural Networks (CNN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-29"></a>

# Convoluções com Stride

Além do padding, outra técnica importante em CNNs é o **stride**, que é o passo. O stride define quantos pixels o filtro se move a cada aplicação da convolução. Por exemplo, se o stride for $1$, o filtro se move um pixel de cada vez, enquanto se o stride for $2$, o filtro se move dois pixels de cada vez. O uso do stride permite que a rede aprenda padrões em diferentes escalas e resoluções, além de reduzir o tamanho da feature map resultante. Se minha imagem $I$ tem dimensões $H \times W$ e o filtro $K$ tem dimensões $M \times M$, e eu aplico o mesmo passo $S$ tanto verticalmente quanto horizontalmente, e eu apliquei um **padding completo**, então a dimensão do feature map será: $$\left\lfloor {\frac{H + 2P - M}{S} - 1} \right\rfloor \times \left\lfloor {\frac{W + 2P - M}{S} - 1} \right\rfloor$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Padding](../padding/index.md)
- Próximo: [Convolução Multidimensional](../convolucao-multidimensional/index.md)
