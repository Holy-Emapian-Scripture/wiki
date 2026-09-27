---
layout: "default"
title: "Estrutura Inicial — Redes Neurais"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 15
---

[Aprendizado de Máquina](../../index.md) · [Redes Neurais](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-22"></a>

# Estrutura Inicial

As redes neurais são estruturadas com base em camadas de neurônios interconectados, de forma que cada camada tem sua própria quantidade de neurônios e cada neurônio é conectado a todos os neurônios da camada seguinte.

![Representação do neurônio $k$ da camada $j$. $\text{sum}(w,z) = b_{k}^{(j)} + \sum_{i = 1}^{D}w_{ik}^{(j - 1)}z_{i}^{(j - 1)}$](../../assets/neuron.png)

*Figura 9. Representação do neurônio $k$ da camada $j$. $\text{sum}(w,z) = b_{k}^{(j)} + \sum_{i = 1}^{D}w_{ik}^{(j - 1)}z_{i}^{(j - 1)}$*

Na primeira camada, $Z = X$. Mas antes de continuarmos vendo isso, vamos definir as camadas em si:

![Camadas de entrada, escondidas e de saída](../../assets/layers.png)

*Figura 10. Camadas de entrada, escondidas e de saída*

Então a estrutura de uma rede neural com $K$ camadas escondidas é, pegar o datapoint, joga na camada de entrada, ele é processado dentro de todas as camadas e finalmente chega na camada de saída, onde é feita a predição.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Redes Neurais](../index.md)
- Próximo: [Estrutura Matemática](../estrutura-matematica/index.md)
