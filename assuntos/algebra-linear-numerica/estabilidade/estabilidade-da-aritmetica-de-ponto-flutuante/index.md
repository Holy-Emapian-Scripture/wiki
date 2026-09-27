---
layout: "default"
title: "Estabilidade da Aritmética de Ponto Flutuante — Estabilidade"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 49
---

[Álgebra Linear Numérica](../../index.md) · [Estabilidade](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-58"></a>

# Estabilidade da Aritmética de Ponto Flutuante

**Teorema**

As operações $\oplus$, $\ominus$, $\otimes$ e $⨸$ são **estáveis retroativamente**

**Demonstração**

Defina $\circledast$ como qualquer uma das 4 operações mostradas antes. Dado um problema $f:X \rightarrow Y$ que está calculando $x_{1} \ast x_{2}$, o algoritmo $\widetilde{f}$ para resolver esse problema é $\widetilde{f}(x) = \text{ fl}\left( x_{1} \right) \circledast \text{ fl}\left( x_{2} \right)$ onde $x = \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix}$.

Temos que: $$\widetilde{f}(x) = \text{ fl}\left( x_{1} \right) \circledast \text{ fl}\left( x_{2} \right)$$ $$= \left( \text{fl}\left( x_{1} \right) \ast \text{ fl}\left( x_{2} \right) \right)\left( 1 + \varepsilon_{3} \right)$$ $$= \left( x_{1}\left( 1 + \varepsilon_{1} \right) \ast x_{2}\left( 1 + \varepsilon_{2} \right) \right)\left( 1 + \varepsilon_{3} \right)$$ $$= x_{1}\left( 1 + \varepsilon_{1} \right)\left( 1 + \varepsilon_{3} \right) \ast x_{2}\left( 1 + \varepsilon_{2} \right)\left( 1 + \varepsilon_{3} \right)$$ $$= x_{1}\left( 1 + \varepsilon_{4} \right) \ast x_{2}\left( 1 + \varepsilon_{5} \right)$$

Onde $\varepsilon_{4} = O\left( \varepsilon_{\text{machine}} \right)$ e $\varepsilon_{5} = O\left( \varepsilon_{\text{machine}} \right)$. Calculamos $\widetilde{f}(x)$, agora vamos ver $f\left( \widetilde{x} \right)$. Primeiro, vamos definir: $$\widetilde{x} = \begin{pmatrix} x_{1}\left( 1 + \varepsilon_{4} \right) \\ x_{2}\left( 1 + \varepsilon_{5} \right) \end{pmatrix}$$

Se definirmos $\widetilde{x}$ assim, podemos ver claramente que $$f\left( \widetilde{x} \right) = x_{1}\left( 1 + \varepsilon_{4} \right) + x_{2}\left( 1 + \varepsilon_{5} \right) = \widetilde{f}(x)$$

Mas a condição $\frac{\|\widetilde{x} - x\|}{\| x\|} = O\left( \varepsilon_{\text{machine}} \right)$ é satisfeita? $$\frac{\|\widetilde{x} - x\|}{\| x\|} = \frac{\|\begin{pmatrix} x_{1}\left( 1 + \varepsilon_{4} \right) \\ x_{2}\left( 1 + \varepsilon_{5} \right) \end{pmatrix} - \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix}\|}{\|\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix}\|} = \frac{\|\begin{pmatrix} x_{1}\varepsilon_{4} \\ x_{2}\varepsilon_{5} \end{pmatrix}\|}{\|\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix}\|}$$ Usando a norma 1 $$\frac{x_{1}\varepsilon_{4} + x_{2}\varepsilon_{5}}{x_{1} + x_{2}} = \frac{x_{1}O\left( \varepsilon_{\text{machine}} \right) + x_{2}O\left( \varepsilon_{\text{machine}} \right)}{x_{1} + x_{2}} = \frac{\left( x_{1} + x_{2} \right)O\left( \varepsilon_{\text{machine}} \right)}{x_{1} + x_{2}} = O\left( \varepsilon_{\text{machine}} \right)$$

Isso mostra que $\oplus$, $\ominus$, $\otimes$ e $⨸$ são **estáveis retroativamente**

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Independência da Norma](../independencia-da-norma/index.md)
- Próximo: [Precisão de um Algoritmo Estável Retroativamente](../precisao-de-um-algoritmo-estavel-retroativamente/index.md)
