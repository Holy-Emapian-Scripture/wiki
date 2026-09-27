---
layout: "default"
title: "Caso Convexo — Método do Gradiente"
tipo: "conteudo"
disciplina: "Otimização para Ciência de Dados"
origem: "4 semestre/Otimização para CD/Recaps/A2.md"
trilha: "../../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 4
---

[Otimização para Ciência de Dados](../../index.md) · [Método do Gradiente](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Caso Convexo

Antes, não assumimos nada além da suavidade da função, agora vamos mostrar que, assumindo que $f$ é convexa, o algoritmo converge para uma solução global. Primeiro, nós sabemos que: $$\begin{aligned} x^{(t + 1)} & = x^{(t)} - \alpha\nabla f\left( x^{(t)} \right) \\ \Leftrightarrow x^{(t + 1)} - x^{\ast} & = x^{(t)} - x^{\ast} - \alpha\nabla f\left( x^{(t)} \right) \\ \Leftrightarrow \| x^{(t + 1)} - x^{\ast}\|_{2}^{2} & = \| x^{(t)} - x^{\ast} - \alpha\nabla f\left( x^{(t)} \right)\|_{2}^{2} \end{aligned}$$

Pelas propriedades da convexidade: $$\left( x^{\ast} - x^{(t)} \right)^{T}\nabla f\left( x^{(t)} \right) \leq f\left( x^{\ast} \right) - f\left( x^{(t)} \right)$$

e pelo que vimos na equação [\[iterated-aproximation\]](../caso-global/index.md#iterated-aproximation), se $\alpha \in \left( 0,\frac{2}{L} \right)$, podemos chegar que: $$\| x^{(t + 1)} - x^{\ast}\|_{2}^{2} \leq \| x^{(t)} - x^{\ast}\|_{2}^{2} - \alpha\left( 2 - \frac{1}{1\frac{- (\alpha L)}{2}} \right)\left( f\left( x^{(t)} \right) - f^{\ast} \right)$$

ou seja, a distância do próximo iterado pro ponto ótimo é menor a distância atual, menos um termo proporcional a distância dos resultados de $x^{(t)}$ e do ponto ótimo. Vamos usar isso para provar a convergência global do resultado

**Teorema: Convergência Convexa do Método do Gradiente**

Suponha que $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ é $L$-suave e convexa e tome qualquer passo $$\alpha = \frac{\beta}{L}$$ para algum $\beta \in (0,1)$, então: $$f\left( x^{(T)} \right) - f^{\ast} \leq \frac{1}{T}\sum_{t = 1}^{T}\left( f\left( x^{t} \right) - f^{\ast} \right) \leq \frac{\beta^{- 1} - \frac{1}{2}}{1 - \beta}\frac{L\| x^{(1)} - x^{\ast}\|_{2}^{2}}{T}$$

**Demonstração**

Somando-se em $tin\lbrack T\rbrack$ a recorrência: $$\alpha(2 - \frac{1}{1 - \alpha\frac{L}{2}}\left( f\left( x^{t} \right) - f^{\ast} \right) \leq \| x^{(t)} - x^{\ast}\|_{2}^{2} - \| x^{(t + 1)} - x^{\ast}\|_{2}^{2}$$

obtemos novamente uma soma telescópica: $$\begin{aligned} \alpha\left( \frac{1 - \alpha L}{1 - \alpha\frac{L}{2}} \right)\sum_{t = 1}^{T}\left( f\left( x^{(t)} \right) - f^{\ast} \right) & \leq \sum_{t = 1}^{T}\left( \| x^{(t)} - x^{\ast}\|_{2}^{2} - \| x^{(t + 1)} - x^{\ast}\|_{2}^{2} \right) \\ & \leq \| x^{(1)} - x^{\ast}\|_{2}^{2} - \| x^{(T + 1)} - x^{\ast}\|_{2}^{2} \\ & \leq \| x^{1} - x^{\ast}\|_{2}^{2.} \end{aligned}$$

Dividindo-se por $\alpha\left( \frac{1 - \alpha L}{1 - \alpha\frac{L}{2}} \right)T$, e lembrando que, pelo , a sequência $\left\{ f\left( x^{(t)} \right) \right\}$ é decrescente: $$f\left( x^{(T)} \right) - f^{\ast} \leq \frac{1}{T}\sum_{\left\{ t = 1 \right\}}^{T}\left( f\left( x^{(t)} \right) - f^{\ast} \right) \leq \frac{\alpha^{- 1}\left( 1 - \alpha\frac{L}{2} \right)}{T}\| x^{1} - x^{\ast}\|_{2}^{2.}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/otimizacao-para-ciencia-de-dados/a2.md#apresentacao-original)

- Anterior: [Caso Global](../caso-global/index.md)
- Próximo: [Interpretação via regularização](../interpretacao-via-regularizacao/index.md)
