---
layout: "default"
title: "Tipos de mapeamento sequencial — Simple RNN (Vanilla RNN)"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 47
---

[Aprendizado Profundo](../../../index.md) · [Recurrent Neural Networks (RNNs)](../../index.md) · [Simple RNN (Vanilla RNN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-55"></a>

# Tipos de mapeamento sequencial

- **Many-to-many**: Existem duas variações, a primeira é quando a entrada e a saída são sequências de comprimentos iguais. Por exemplo, os momentos de um vídeo e a categoria que aquele momento se encaixa (drama, terror, etc.)

  ![Exemplo de mapeamento many-to-many](../../../assets/A1/rnn-many-to-many-1.png)

  *Figura 43. Exemplo de mapeamento many-to-many*

  A segunda variação é quando a entrada e a saída são sequências de comprimentos diferentes. Por exemplo, uma frase em inglês e sua tradução em português.

  ![Exemplo de mapeamento many-to-many](../../../assets/A1/rnn-many-to-many-2.png)

  *Figura 44. Exemplo de mapeamento many-to-many*

- **One-to-many**: Quando o modelo recebe uma única entrada e gera uma sequência de saídas. Por exemplo, uma imagem e a legenda que descreve a imagem.

  ![Exemplo de mapeamento one-to-many](../../../assets/A1/rnn-one-to-many.png)

  *Figura 45. Exemplo de mapeamento one-to-many*

- **Many-to-one**: Quando o modelo recebe uma sequência de entradas e gera uma única saída. Por exemplo, uma sequência de palavras e a classificação da sentença.

  ![Exemplo de mapeamento many-to-one](../../../assets/A1/rnn-many-to-one.png)

  *Figura 46. Exemplo de mapeamento many-to-one*

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [RNN Unroling](../rnn-unroling/index.md)
- Próximo: [Treinamento e Problemas de Gradiente na RNN](../../treinamento-e-problemas-de-gradiente-na-rnn/index.md)
