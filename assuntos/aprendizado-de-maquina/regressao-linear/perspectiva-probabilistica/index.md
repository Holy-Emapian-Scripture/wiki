---
layout: "default"
title: "Perspectiva Probabilística — Regressão Linear"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 9
---

[Aprendizado de Máquina](../../index.md) · [Regressão Linear](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-13"></a>

# Perspectiva Probabilística

Podemos obter o mesmo estimador de mínimos quadrados se assumirmos o seguinte modelo observacional para cada resposta dado sua respectiva entrada: $$y_{n}\vert x_{n} \sim N\left( \theta^{T}x_{n},\sigma^{2} \right)\forall n = 1,\ldots,N$$<a id="modelo-observacional"></a> podemos então procurar o estimador de máxima verossimilhança ${\hat{\theta}}_{\text{ML}}$ para $\theta$: $$\begin{aligned} \Rightarrow f_{n}\left( y\vert x,\theta \right) & = \prod_{n = 1}^{N}f\left( y_{n}\vert x_{n},\theta \right) = \left( \frac{1}{\left( \sqrt{2\pi\sigma^{2}} \right)^{N}} \right)\exp( - \sum_{n = 1}^{N}\frac{\left( y_{n} - \theta^{T}x_{n} \right)^{2}}{2\sigma^{2}}) \end{aligned}$$ $$\Rightarrow \log f_{n}\left( y\vert x,\theta \right) = - \frac{N}{2}\log(2\pi\sigma^{2}) - \frac{1}{2\sigma^{2}}\sum_{n = 1}^{N}\left( y_{n} - \theta^{T}x_{n} \right)^{2}$$ $$\Rightarrow {\hat{\theta}}_{\text{ML }} = \text{ argmax}_{\theta \in {\mathbb{R}}^{D + 1}}\log f_{n}\left( y\vert x,\theta \right) = \text{ argmin}_{\theta \in {\mathbb{R}}^{D + 1}}\underset{N \cdot \mathcal{l}(\theta)}{\underbrace{\sum_{n = 1}^{N}\left( y_{n} - \theta^{T}x_{n} \right)^{2}}}$$

ou seja, a estimativa que máximiza a verossimilhança do modelo descrito pela equação [\[modelo-observacional\]](#modelo-observacional) é equivalente à estimativa obtida minimizando a média dos erros quadrados. Mais importante, note que, quando fazemos regressão linear, estamos parametrizando um parâmetro (a média) do nosso modelo observacional como uma transformação linear do vetor de entrada.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [O Problema](../o-problema/index.md)
- Próximo: [Modelo com expansão de base](../modelo-com-expansao-de-base/index.md)
