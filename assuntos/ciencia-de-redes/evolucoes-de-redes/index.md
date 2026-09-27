---
layout: "default"
title: "Evoluções de Redes"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A1.md"
trilha: "../../../trilhas/ciencia-de-redes/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 11
---

[Ciência de Redes](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Evoluções de Redes

------------------------------------------------------------------------

Vimos as redes aleatórias onde os graus dos nós tinham distribução de Poisson. Mas e se eu quisesse fazer uma rede com distribuição diferente? Muitos pacotes de grafos e redes utilizam de **configuration models**, que são funções que recebem a quantidade de nós da rede e um **vetor** que representa a **função de distribuição** dos graus dos nós

Voltando ao assunto sobre **evoluções**, eu estou interessado em pensar um jeito intuitivo/natural de como as redes vão evoluir com o passar do tempo.

Então vamos imaginar o seguinte cenário. Eu tenho uma rede inicial $G_{0}\left( V_{0},E_{0} \right)$ e a cada unidade de tempo $t$ eu vou ter uma nova rede $G_{t}\left( V_{t},E_{t} \right)$, de forma que a cada unidade de tempo, eu vou adicionar um novo nó em $V_{t - 1}$ e novas arestas em $E_{t - 1}$. Qual é a distribuição do grau médio desses nós? O que podemos inferir dessa rede?

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Anexação Uniforme](anexacao-uniforme/index.md)
2. [Anexação Preferencial](anexacao-preferencial/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Anterior: [Conclusão](../redes-aleatorias/conclusao/index.md)
- Próximo: [Anexação Uniforme](anexacao-uniforme/index.md)
