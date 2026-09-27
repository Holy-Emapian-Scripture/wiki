---
layout: "default"
title: "Métodos de mitigação — Treinamento e Problemas de Gradiente na RNN"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 51
---

[Aprendizado Profundo](../../../index.md) · [Recurrent Neural Networks (RNNs)](../../index.md) · [Treinamento e Problemas de Gradiente na RNN](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-59"></a>

# Métodos de mitigação

Para mitigar o problema de **exploding gradients** e **vanishing gradients**. A principal técnica utilizada é uma variação do BPTT.

**Truncated BPTT**: No BPTT original, para atualizar o pesos, eu faço o forward pass por TODOS os $T$ passos temporais e retropropago por eles novamente. Nessa versão simplificada, existem dois hiperparâmetros $k_{1}$ e $k_{2}$. Na parte do forward, a rede propaga por apenas $k_{1}$ passos temporais, e na parte do backward, a rede retropropaga por apenas $k_{2}$ passos temporais (obrigatoriamente $k_{2} < k_{2}$). Isso reduz a profundidade da rede e ajuda a evitar o problema de gradientes explosivos ou desvanecentes.

![Exemplo de Truncated BPTT com k1=3 e k2=2](../../../assets/A1/rnn-truncated-bptt.png)

*Figura 48. Exemplo de Truncated BPTT com k1=3 e k2=2*

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [A matemática dos gradientes explosivos ou desvanecentes](../a-matematica-dos-gradientes-explosivos-ou-desvanecentes/index.md)
- Próximo: [Limitações da RNN](../../limitacoes-da-rnn/index.md)
