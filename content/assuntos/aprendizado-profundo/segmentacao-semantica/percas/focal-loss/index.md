---
layout: "default"
title: "Focal Loss — Percas"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 21
---

[Aprendizado Profundo](../../../index.md) · [Segmentação Semântica](../../index.md) · [Percas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-27"></a>

# Focal Loss

Essa loss serve para resolver um problema sutíl. A loss anterior resolve o problema de desbalanceamento de classes, mas não resolve o problema de **hard examples**, ou seja, exemplos que são difíceis de classificar e quais são esses pixeis? São justamente os que estão cada vez mais próximos das bordas do elemento. No entanto, os pixeis fáceis costumam ser os mais presentes, e a soma do gradiente de sua contribuição pode atrapalhar no aprendizado dos pixeis mais difíceis. A **focal loss** resolve esse problema, diminuindo a contribuição dos pixeis fáceis para o gradiente, permitindo que a rede foque nos pixeis mais difíceis. $$\text{ FL } = - \frac{1}{N}\sum_{i = 1}^{N}\left( 1 - p_{i} \right)^{\gamma}\log(p_{i})$$

- **Comportamento do pixel fácil**: Consideremos $p_{i} = 0.95$ e $\gamma = 2$, então o fator de peso fica $0.0025$, a perda desse pixel é reduzida em $99.75\%$, fazendo com que ele quase não afete o treinamento

- **Comportamento do pixel difícil**: Consideremos $p_{i} = 0.2$ e $\gamma = 2$, então o fator de peso fica $0.64$, a perda desse pixel é mantida relevante

$\gamma$ é o parâmetro focal, quanto maior ele é, mais severa é a penalidade aplicada aos pixels fáceis, e quanto menor ele é, mais leve é a penalidade aplicada aos pixels fáceis. O valor padrão de $\gamma$ é $2$, mas ele pode ser ajustado dependendo do problema e do dataset.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Balanced Cross Entropy Loss](../balanced-cross-entropy-loss/index.md)
- Próximo: [Balanced Focal Loss](../balanced-focal-loss/index.md)
