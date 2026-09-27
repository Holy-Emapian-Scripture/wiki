---
layout: "default"
title: "Caixas de Ancoragem (Anchor Boxes) — Redes de Estágio Único (Single-Shot): A Família YOLO"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 34
---

[Aprendizado Profundo](../../../index.md) · [Object Detection](../../index.md) · [Redes de Estágio Único (Single-Shot): A Família YOLO](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-40"></a>

# Caixas de Ancoragem (Anchor Boxes)

Para resolver o problema de múltiplos objetos cujos centros caiam na mesma célula ou objetos de proporções muito distintas (como uma pessoa alta e um carro largo), o YOLO utiliza **Anchor Boxes**. Cada célula da grade prevê múltiplos **bounding boxes** associados a modelos geométricos *pré-definidos* (**anchors**). Em vez de prever o formato absoluto da caixa do zero, a rede aprende deslocamentos (**offsets**) para ajustar a posição e a dimensão das **anchor boxes pré-definidas**

![Exemplo de caixas de ancoragem previstas pelo YOLO](../../../assets/A1/yolo-anchor-boxes.png)

*Figura 29. Exemplo de caixas de ancoragem previstas pelo YOLO*

Então nessa nova formulação, o vetor de saída para cada célula da grade se torna: $$y = \begin{pmatrix} \left\lbrack p_{\text{obj}},b_{x},b_{y},b_{h},b_{w},c_{1},c_{2},\ldots,c_{C} \right\rbrack_{anchor\ 1} \\ \left\lbrack p_{\text{obj}},b_{x},b_{y},b_{h},b_{w},c_{1},c_{2},\ldots,c_{C} \right\rbrack_{anchor\ 2} \\ \vdots \\ \left\lbrack p_{\text{obj}},b_{x},b_{y},b_{h},b_{w},c_{1},c_{2},\ldots,c_{C} \right\rbrack_{\text{anchor A}} \end{pmatrix}$$

Vale ressaltar que eu escrevi em forma de matriz, no entanto o mais comum é um vetor contínuo e separamos as anchor boxes pelo padrão da saída, que seria a cada $5 + C$ valores, onde $C$ é o número de classes. Por exemplo, se temos $3$ anchor boxes e $20$ classes, o vetor de saída para cada célula da grade terá tamanho $3 \times (5 + 20) = 75$.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Parametrização do vetor de saída](../parametrizacao-do-vetor-de-saida/index.md)
- Próximo: [Supressão Não-Máxima (Non-Maximum Suppression - NMS)](../supressao-nao-maxima-non-maximum-suppression-nms/index.md)
