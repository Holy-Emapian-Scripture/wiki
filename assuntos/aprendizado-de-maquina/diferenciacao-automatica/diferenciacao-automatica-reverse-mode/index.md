---
layout: "default"
title: "Diferenciação Automática reverse-mode — Diferenciação Automática"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 7
---

[Aprendizado de Máquina](../../index.md) · [Diferenciação Automática](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# Diferenciação Automática reverse-mode

Podemos pensar nessa implementação como uma generalização do processo de backpropagation. No modo forward, nós alimentamos cada variável intermediária $v_{i}$ com varáveis adicionais, nesses casos chamadas de **variáveis adjuntas**, denotadas por ${\overset{-}{v}}_{i}$. Considere novamente uma função de apenas $1$ output na forma $f:{\mathbb{R}}^{D} \rightarrow {\mathbb{R}}$. A variável adjunta ${\overset{-}{v}}_{i}$ é definida como: $${\overset{-}{v}}_{i} = \frac{\partial f}{\partial v_{i}}$$

Podemos calcular esse valor automaticamente com a regra da cadeia: $${\overset{-}{v}}_{i} = \frac{\partial f}{\partial v_{i}} = \sum_{j \in \text{ ch}\left( v_{i} \right)}\frac{\partial f}{\partial v_{j}} \cdot \frac{\partial v_{j}}{\partial v_{i}} = \sum_{j \in \text{ ch}\left( v_{i} \right)}{\overset{-}{v}}_{j} \cdot \frac{\partial v_{j}}{\partial v_{i}}$$

onde $\text{ch}\left( v_{i} \right)$ representa o conjunto de variáveis que dependem de $v_{i}$ (filhos do nó $v_{i}$). Considerando novamente o exemplo da função [\[funcao-exemplo-diferenciacao-automatica-forward\]](../diferenciacao-automatica-forward-mode/index.md#funcao-exemplo-diferenciacao-automatica-forward), podemos calcular as variáveis adjuntas ${\overset{-}{v}}_{i}$ para cada $v_{i}$: $$\begin{aligned} {\overset{-}{v}}_{7} & = 1 \\ {\overset{-}{v}}_{6} & = {\overset{-}{v}}_{7} \\ {\overset{-}{v}}_{5} & = {\overset{-}{v}}_{7} \\ {\overset{-}{v}}_{4} & = - {\overset{-}{v}}_{6} \\ {\overset{-}{v}}_{3} & = {\overset{-}{v}}_{5}v_{5} + {\overset{-}{v}}_{6} \\ {\overset{-}{v}}_{2} & = {\overset{-}{v}}_{2}v_{1} + {\overset{-}{v}}_{4}\cos(v_{2}) \\ {\overset{-}{v}}_{1} & = {\overset{-}{v}}_{3}v_{2} \end{aligned}$$

Observe que essas equações começam na saída (output) e fluem para trás através do grafo até as entradas (inputs). Mesmo com múltiplas entradas, apenas um único backward pass é necessário para calcular as derivadas.

Para uma função de erro de rede neural, as derivadas de $E$ em relação aos pesos e vieses (biases) são obtidas como as variáveis adjuntas (adjoint variables) correspondentes. Entretanto, se tivermos mais de uma saída, será necessário executar um backward pass separado para cada variável de saída.

O reverse mode costuma exigir mais memória do que o forward mode, porque todas as variáveis primais intermediárias (intermediate primal variables) precisam ser armazenadas para que estejam disponíveis quando for necessário calcular as variáveis adjuntas durante a passagem para trás.

Em contraste, no forward mode, as variáveis primais e tangentes são calculadas conjuntamente durante o forward pass, de modo que as variáveis podem ser descartadas assim que forem utilizadas.

Por isso, em geral, o forward mode também é mais simples de implementar do que o reverse mode.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Diferenciação Automática forward-mode](../diferenciacao-automatica-forward-mode/index.md)
- Próximo: [Exemplo em código](../exemplo-em-codigo/index.md)
