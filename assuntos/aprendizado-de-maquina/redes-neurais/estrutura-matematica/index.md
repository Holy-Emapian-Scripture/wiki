---
layout: "default"
title: "Estrutura Matemática — Redes Neurais"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 16
---

[Aprendizado de Máquina](../../index.md) · [Redes Neurais](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-23"></a>

# Estrutura Matemática

Vamos agora formalizar a estrutura matemática das Redes Neurais. Pelo que você viu na imagem anterior, cada camada $j$ tem um número de neurônios $M_{j}$. O número de neurônios da camada de entrada é $M_{0} = D$ e o número de neurônios da camada de saída é $M_{K + 1} = L$. Para cada camada $j \in \left\{ 1,\ldots,K + 1 \right\}$, temos uma matriz de pesos $W^{(j)}$ de tamanho $M_{j - 1} \times M_{j}$ e um vetor de bias $b^{(j)}$ de tamanho $M_{j}$. Podemos escrever o resultado da última camada $Z^{K + 1}$ como: $$Z^{(3)} = h^{(3)}\left( h^{(2)}\left( h^{(1)}\left( XW^{(1)} + b^{(1)}\mathbb{1}^{T} \right)W^{(2)} + b^{(2)}\mathbb{1}^{T} \right)W^{(3)} + b^{(3)}\mathbb{1}^{T} \right)$$

(Exemplo com 3 camadas, 1 de entrada, 1 escondida e 1 de saída)

De forma que a $i$-ésima coluna de $W^{(j)}$ representa os pesos de todas as conexões que chegam no neurônio $i$ da camada $j$ e a $i$-ésima entrada de $b^{(j)}$ é o bias do neurônio $i$ da camada $j$. A função $h^{(j)}$ é a função de ativação da camada $j$, que é aplicada elemento a elemento

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Estrutura Inicial](../estrutura-inicial/index.md)
- Próximo: [Não-linearidade](../nao-linearidade/index.md)
