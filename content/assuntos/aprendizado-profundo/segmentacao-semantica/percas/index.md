---
layout: "default"
title: "Percas — Segmentação Semântica"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 18
---

[Aprendizado Profundo](../../index.md) · [Segmentação Semântica](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-24"></a>

# Percas

Agora vamos visualizar as losses que utilizamos para informar o modelo como aprender! Mas antes, vamos recaptular alguns pontos e definições.

Primeiramente, dado uma imagem $H \times W$, a saída dos nossos modelos deve ser uma matriz $H \times W$ onde cada elemento da matriz representa a classe do pixel correspondente na imagem (também pode ser um vetor com $N = H \cdot W$ elementos). Vamos considerar a abordagem de um único vetor de $N$ elementos com a classe de cada pixel. Definiremos também $t_{i}$ sendo a **classe verdadeira** do pixel $i$ (ground truth). Definimos também $p_{i}$ sendo a probabilidade que o modelo atribui para que $i$ seja da sua **classe verdadeira** (${\mathbb{P}}(\text{classe}(i) = t_{i})$). A partir disso, podemos definir as losses que utilizamos para treinar nossos modelos.

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Cross Entropy Loss](cross-entropy-loss/index.md)
2. [Balanced Cross Entropy Loss](balanced-cross-entropy-loss/index.md)
3. [Focal Loss](focal-loss/index.md)
4. [Balanced Focal Loss](balanced-focal-loss/index.md)
5. [Loss Function for Regression](loss-function-for-regression/index.md)

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Deeplab V3 & V3+](../arquiteturas/deeplab-v3-v3/index.md)
- Próximo: [Cross Entropy Loss](cross-entropy-loss/index.md)
