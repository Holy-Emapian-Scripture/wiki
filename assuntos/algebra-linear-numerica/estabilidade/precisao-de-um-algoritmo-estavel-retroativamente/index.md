---
layout: "default"
title: "Precisão de um Algoritmo Estável Retroativamente — Estabilidade"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 50
---

[Álgebra Linear Numérica](../../index.md) · [Estabilidade](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-59"></a>

# Precisão de um Algoritmo Estável Retroativamente

Falamos de números de condição antes da estabilidade, vamos tentar associar ambos!

**Teorema**

Suponha que um algoritmo estável retroativamente $\widetilde{f}$ é aplicado para um problema $f:X \rightarrow Y$ com número de condição $\kappa$ em um computador que satisfaz [\[floating_point_conversion\]](../../aritmetica-de-ponto-flutuante/epsilon-maquina/index.md#floating_point_conversion) e [\[fundamental_axiom_of_floating_point_arithmetic\]](../../aritmetica-de-ponto-flutuante/aritmetica-de-ponto-flutuante/index.md#fundamental_axiom_of_floating_point_arithmetic), então, o erro relativo satisfaz: $$\frac{\|\widetilde{f}(x) - f\left( \widetilde{x} \right)\|}{\| f\left( \widetilde{x} \right)\|} = O\left( \kappa(x)\varepsilon_{\text{machine}} \right)$$

**Demonstração**

Por definição, temos $\widetilde{f}(x) = f(x + \delta x)$ com $\frac{\|\delta x\|}{\| x\|} = O\left( \varepsilon_{\text{machine}} \right)$. Usando [\[relative_condition_number\]](../../condicionamento-e-numeros-de-condicao/condicionamento-de-um-problema/index.md#relative_condition_number) (Número de Condição Relativo), temos que: $$\kappa(x) = \lim\limits_{\delta x \rightarrow 0}\left( \frac{\| f(x + \delta x) - f(x)\|}{\| f(x)\|} \right)\left( \frac{\| x\|}{\|\delta x\|} \right)$$ $$\kappa(x) = \lim\limits_{\delta x \rightarrow 0}\left( \frac{\|\widetilde{f}(x) - f(x)\|}{\| f(x)\|}\frac{\| x\|}{\|\delta x\|} \right)$$

Usando algumas definições formais (nem eu entendo, então se tentar explicar aqui, só perderei tempo, lol), podemos reescrever isso como: $$\frac{\|\widetilde{f}(x) - f(x)\|}{\| f(x)\|} \leq \left( \kappa(x) + o(1) \right)\frac{\|\delta x\|}{\| x\|}$$

Onde $o(1) \rightarrow 0$ quando $\varepsilon_{\text{machine }} \rightarrow 0$
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Estabilidade da Aritmética de Ponto Flutuante](../estabilidade-da-aritmetica-de-ponto-flutuante/index.md)
