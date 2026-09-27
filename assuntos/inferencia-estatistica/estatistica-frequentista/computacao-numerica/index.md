---
layout: "default"
title: "Computação Numérica — Estatística Frequentista"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 16
---

[Inferência Estatística](../../index.md) · [Estatística Frequentista](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-16"></a>

# Computação Numérica

Muitos problemas possuem um EVM $\hat{\theta}$ de um parâmetro $\theta$, porém esses não podem ser computados com fórmulas fechadas. Nesses casos, precisamos utilizar de métodos numéricos para aproximações. Existem **inúmeros** métodos de aproximação numérica de funções, porém, aqui vamos abordar brevemente apenas um

**Definição: Método de Newton**

Seja $f(\theta)$ uma função real de uma variável e suponha que nós desejamos resolver a equação $f(\theta) = 0$. Seja $\theta_{0}$ um chute inicial da solução e $\theta_{t}$ o valor obtido na $t$-ésima iteração do programa. O método de Newton atualiza nossa resposta da seguinte forma: $$\theta_{t + 1} = \theta_{t} - \frac{f\left( \theta_{t} \right)}{f'\left( \theta_{t} \right)}$$

Se pararmos para interpretar, o que o algoritmo faz é checar se eu tenho que mexer $\theta_{t}$ para frente ou para trás dependendo do sinal e da inclinação de $f$. Quando $f\left( \theta_{t} \right)$ é negativo e $f'\left( \theta_{t} \right)$ é positivo, então eu preciso mover para a direita para poder chegar próximo a raíz, e aí vai

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Propriedades](../propriedades/index.md)
- Próximo: [Método dos Momentos](../../metodo-dos-momentos/index.md)
