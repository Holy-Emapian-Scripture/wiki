---
layout: "default"
title: "Introdução — Diferenciação Automática"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 5
---

[Aprendizado de Máquina](../../index.md) · [Diferenciação Automática](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Introdução

Aposto que, se você é alguém que, como eu, sempre teve interesse de ver esses algoritmos de machine learning e implementar eles do $0$, sentiu alguma dificuldade principalmente quando a sua implementação envolvia o cálculo de algum gradiente (principalmente algum gradiente difícil). Calcular o gradiente de uma função $g:{\mathbb{R}}^{D} \rightarrow {\mathbb{R}}$ com relação a $x \in {\mathbb{R}}^{D}$ é uma tarefa que pode ser extremamente trabalhosa, especialmente quando $g$ é uma função complexa, e justamente essa tarefa complexa é a base fundamental pra que nossas máquinas possam aprender.

Existem, essencialmente, $4$ formas de se calcular o gradiente de uma rede neural.

1.  Derivar as expressões analiticamente e implementá-las manualmente via software. Essa abordagem é extremamente trabalhosa, propensa a erros e não escalável para funções complexas. (Particularmente, exatamente o que eu sempre tentava fazer). Não só isso, mas as implementações dessas alternativas envolvem montar funções distintas para o forward pass e o backward pass, o que torna o processo ainda mais trabalhoso.

2.  Outro método é calcular o gradiente de forma aproximada: $$\frac{\partial f}{\partial x} \approx \frac{f(x + h) - f(x)}{h}\text{\quad\quad}h \approx 0$$ ele está bastante sujetio à erros numéricos, mas esse não é o principal problema, mas sim que ele escala muito mal com o tamanho da rede neural, mas ele é muito útil para verificar se a implementação do gradiente está correta (já que ele utiliza apenas o forward pass da rede neural).

3.  O terceiro método é o **symbolic differentiation**, que consiste em derivar a função simbolicamente e depois implementá-la. Essa abordagem é mais escalável do que a primeira, mas ainda assim pode ser trabalhosa e propensa a erros, especialmente para funções complexas. Por exemplo, considere uma função $f(x) = u(x) \cdot v(x)$, $$\frac{\partial f}{\partial x} = \frac{\partial u}{\partial x} \cdot v + u \cdot \frac{\partial v}{\partial x}$$ e se $u$ e $v$ forem funções complexas, a derivada de $f$ pode se tornar extremamente complicada. Além disso, o symbolic differentiation pode gerar expressões redundantes, o que pode levar a uma implementação ineficiente.

4.  O quarto e último método é o **automatic differentiation**, que é o método mais eficiente e escalável para calcular gradientes de funções complexas. Ele é baseado na regra da cadeia e na decomposição da função em operações elementares, permitindo calcular o gradiente de forma eficiente e precisa. Além disso, ele permite calcular o gradiente de funções complexas sem a necessidade de derivar manualmente as expressões analiticamente.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Diferenciação Automática](../index.md)
- Próximo: [Diferenciação Automática forward-mode](../diferenciacao-automatica-forward-mode/index.md)
