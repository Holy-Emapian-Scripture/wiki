---
layout: "default"
title: "Loss Function — Redes de Estágio Único (Single-Shot): A Família YOLO"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 37
---

[Aprendizado Profundo](../../../index.md) · [Object Detection](../../index.md) · [Redes de Estágio Único (Single-Shot): A Família YOLO](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-45"></a>

# Loss Function

Não podemos falar de um modelo de rede sem discutir a loss por ela utilizada. A loss do YOLO é composta por três partes principais: a **loss de localização**, a **loss de confiança** e a **loss de classificação**. A **loss de localização** mede o quão bem a rede prevê as coordenadas da caixa delimitadora em relação à caixa real. A **loss de confiança** avalia a precisão da rede em prever se uma caixa contém um objeto ou não. A **loss de classificação** mede a precisão da rede em classificar corretamente o objeto dentro da caixa.

Vamos rapidamente definir que a **predição do modelo** é dada, para a célula $i \in \left\{ 1,\ldots,S^{2} \right\}$ e anchor box $j \in \left\{ 1,\ldots,B \right\}$: $$y_{ij} = \left\lbrack p_{\text{obj}}^{(ij)},b_{x}^{(ij)},b_{y}^{(ij)},b_{h}^{(ij)},b_{w}^{(ij)},c_{1}^{(ij)},c_{2}^{(ij)},\ldots,c_{C}^{(ij)} \right\rbrack$$ e vamos considerar o vetor **ground truth** como $$t_{ij} = \left\lbrack t_{0}^{(ij)},t_{x}^{(ij)},t_{y}^{(ij)},t_{h}^{(ij)},t_{w}^{(ij)},s_{1}^{(ij)},s_{2}^{(ij)},\ldots,s_{C}^{(ij)} \right\rbrack$$ então a loss da YOLO é dada por $$\begin{aligned} \mathcal{L}_{\text{YOLO }} & = \lambda_{\text{coord }}\underset{\text{ Loss de localização}}{\underbrace{\sum_{i = 0}^{S^{2}}\sum_{j = 0}^{B}t_{0}^{(ij)}\left( \left( t_{x}^{(ij)} - b_{x}^{(ij)} \right)^{2} + \left( t_{y}^{(ij)} - b_{y}^{(ij)} \right)^{2} + \left( t_{h}^{(ij)} - b_{h}^{(ij)} \right)^{2} + \left( t_{w}^{(ij)} - b_{w}^{(ij)} \right)^{2} \right)}} \\ \\ & + \lambda_{\text{noobj }}\underset{\text{ Loss de confiança}}{\underbrace{\sum_{i = 0}^{S^{2}}\sum_{j = 0}^{B}\left( 1 - t_{0}^{(ij)} \right)\left( - \log(1 - p_{\text{obj}}^{(ij)}) \right)}} \\ & + \underset{\text{ Loss de classificação}}{\underbrace{\sum_{i = 0}^{S^{2}}\sum_{j = 0}^{B}t_{0}^{(ij)}\left\lbrack - \log(p_{\text{obj}}^{(ij)}) + \sum_{k = 1}^{C}\text{ BCE}\left( c_{k}^{(ij)},s_{k}^{(ij)} \right) \right\rbrack}} \end{aligned}$$

Onde $S$ é a proporção que dividimos os grids da imagem, $B$ é o número de **anchor boxes** por célula, $C$ é o número de classes, $\lambda_{\text{nobj}}$ e $\lambda_{\text{coord}}$ são hiperparâmetros que controlam a importância relativa das diferentes partes da loss.

Vejamos como a loss se comporta. Se uma anchor box **não possui objeto**, então apenas a parte da **loss de confiança** é computada. Quando a probabilidade de que a caixa contenha um objeto é $0$, então a $\log(1 - 0) = 0$, não penalizando a rede, no entanto, se a rede classificou como existindo um objeto, então a loss será alta e irá penalizar a rede. Se uma anchor box **possui objeto**, então apenas as partes da **Loss de Localização** e **Loss de Classificação** são computadas. A **Loss de Localização** mede o quão bem a rede prevê as coordenadas da caixa delimitadora em relação à caixa real, e a **Loss de Classificação** mede a precisão da rede em classificar corretamente o objeto dentro da caixa.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Evolução Arquitetural](../evolucao-arquitetural/index.md)
- Próximo: [Redes de Dois Estágios e Segmentação de Instâncias: Mask R-CNN](../../redes-de-dois-estagios-e-segmentacao-de-instancias-mask-r-cnn/index.md)
