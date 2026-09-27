---
layout: "default"
title: "Diferenciação Automática forward-mode — Diferenciação Automática"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 6
---

[Aprendizado de Máquina](../../index.md) · [Diferenciação Automática](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-6"></a>

# Diferenciação Automática forward-mode

Considere a seguinte função: $$f\left( x_{1},x_{2} \right) = x_{1}x_{2} + e^{x_{1}x_{2}} - \sin(x_{2})$$<a id="funcao-exemplo-diferenciacao-automatica-forward"></a> quando implementado em código, podemos decompor a função em operações elementares que podem ser visualizadas em grafo

![Grafo de computação da função [\[funcao-exemplo-diferenciacao-automatica-forward\]](#funcao-exemplo-diferenciacao-automatica-forward)](../../assets/automatic-diff-forward.png)

*Figura 1. Grafo de computação da função [\[funcao-exemplo-diferenciacao-automatica-forward\]](#funcao-exemplo-diferenciacao-automatica-forward)*

essas operações são chamadas de *evaluation trace* $$\begin{aligned} & v_{1} = x_{1} \\ & v_{2} = x_{2} \\ & v_{3} = x_{1}x_{2} \\ & v_{4} = \sin(x_{2}) \\ & v_{5} = e^{v_{3}} \\ & v_{6} = v_{3} - v_{4} \\ & v_{7} = v_{5} + v_{6} \end{aligned}$$

Agora suponha que precisamos calcular o gradiente $\frac{\partial f}{\partial x_{1}}$. Nós definimos a **variável tangente** como ${\dot{v}}_{i} = \frac{\partial v_{i}}{\partial x_{1}}$. Podemos calcular essa variável automaticamente com a regra da cadeia: $${\dot{v}}_{i} = \frac{\partial v_{i}}{\partial x_{1}} = \sum_{j \in \text{ pa}\left( v_{i} \right)}\frac{\partial v_{i}}{\partial v_{j}} \cdot \frac{\partial v_{j}}{\partial x_{1}} = \sum_{j \in \text{ pa}\left( v_{i} \right)}\frac{\partial v_{i}}{\partial v_{j}} \cdot {\dot{v}}_{j}$$ onde $\text{pa}\left( v_{i} \right)$ é o conjunto de pais de $v_{i}$ no grafo de computação. Por exemplo, para $v_{3} = x_{1}x_{2}$, temos que $\text{pa}\left( v_{3} \right) = \left\{ v_{1},v_{2} \right\}$. Resolvendo de acordo com a equação acima, obtemos os valores de ${\dot{v}}_{i}$ para cada $v_{i}$: $$\begin{aligned} {\dot{v}}_{1} & = 1 \\ {\dot{v}}_{2} & = 0 \\ {\dot{v}}_{3} & = v_{1}{\dot{v}}_{2} + v_{2}{\dot{v}}_{1} \\ {\dot{v}}_{4} & = \cos(v_{2}){\dot{v}}_{2} \\ {\dot{v}}_{5} & = e^{v_{3}}{\dot{v}}_{3} \\ {\dot{v}}_{6} & = {\dot{v}}_{3} - {\dot{v}}_{4} \\ {\dot{v}}_{7} & = {\dot{v}}_{5} + {\dot{v}}_{6} \end{aligned}$$

Podemos resumir a **diferenciação automática** para este exemplo da seguinte forma:

Primeiro, escrevemos um código para implementar a avaliação das **variáveis primais** (**primal variables**), dadas pelas equações (8.50) a (8.56). As equações associadas e o código correspondente para avaliar as **variáveis tangentes** (**tangent variables**), dadas pelas equações (8.58) a (8.64), são gerados automaticamente.

Para calcular a derivada ($\frac{\partial f}{\partial x_{1}}$), fornecemos valores específicos para ($x_{1}$) e ($x_{2}$), e então o código executa as equações primais e tangentes, avaliando numericamente, em sequência, os pares ($\left( v_{i},{\dot{v}}_{i} \right)$) até obtermos ($\left( {\dot{v}}_{5} \right)$), que é a derivada desejada.

Agora considere o cenário onde temos uma função vetorial, onde a segunda saída é dada por: $$f_{2}\left( x_{1},x_{2} \right) = \left( x_{1}x_{2} - \sin(x_{2}) \right)\exp(x_{1}x_{2})$$<a id="funcao-exemplo-diferenciacao-automatica-forward-multidimensional"></a>

![Grafo de computação da função [\[funcao-exemplo-diferenciacao-automatica-forward\]](#funcao-exemplo-diferenciacao-automatica-forward) e [\[funcao-exemplo-diferenciacao-automatica-forward-multidimensional\]](#funcao-exemplo-diferenciacao-automatica-forward-multidimensional)](../../assets/automatic-diff-forward-multidimensional.png)

*Figura 2. Grafo de computação da função [\[funcao-exemplo-diferenciacao-automatica-forward\]](#funcao-exemplo-diferenciacao-automatica-forward) e [\[funcao-exemplo-diferenciacao-automatica-forward-multidimensional\]](#funcao-exemplo-diferenciacao-automatica-forward-multidimensional)*

Se quisermos calcular $\frac{\partial f_{2}}{\partial x_{1}}$, conseguimos fazer isso no mesmo forward pass do cálculo de $\frac{\partial f_{1}}{\partial x_{1}}$, apenas adicionando mais equações para as **variáveis primais** e **variáveis tangentes** correspondentes a $f_{2}$. No entanto, se quisermos calcular $\frac{\partial f_{1}}{\partial x_{2}}$, precisamos fazer um novo forward pass, pois a variável tangente ${\dot{v}}_{i}$ depende da variável de entrada que estamos diferenciando. Portanto, no geral, se temos uma função com $D$ inputs e $K$ outputs, então um único forward pass produz apenas uma coluna da matriz jacobiana $K \times D$ $$J = \begin{pmatrix} \frac{\partial f_{1}}{\partial x_{1}} & \ldots & \frac{\partial f_{1}}{\partial x_{D}} \\ \vdots & \vdots & \vdots \\ \frac{\partial f_{K}}{\partial x_{1}} & \ldots & \frac{\partial f_{K}}{\partial x_{D}} \end{pmatrix}$$

A diferenciação automática forward-mode é muito útil pricipalmente em casos onde temos muito mais outputs do que inputs ($K \gg D$). Entretanto, no contexto de machine learning, o mais comum é termos uma única função de erro $\mathcal{l}:{\mathbb{R}}^{D} \rightarrow {\mathbb{R}}$ que queremos minimizar com relação a milhões de parâmetros em cadeia dentro das redes neurais, então a implementação forward-mode fica ineficiente, para contornar isso, mudamos para outra abordagem

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Introdução](../introducao/index.md)
- Próximo: [Diferenciação Automática reverse-mode](../diferenciacao-automatica-reverse-mode/index.md)
