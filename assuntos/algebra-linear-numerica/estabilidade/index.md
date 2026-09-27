---
layout: "default"
title: "Estabilidade"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 45
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-54"></a>

# Estabilidade

------------------------------------------------------------------------

Quando falamos de **estabilidade**, estamos tentando verificar se um algoritmo tem fidelidade no computador! Isso significa, se os arredondamentos que o computador faz nas entradas e saídas não mudarão o resultado para algo muito diferente do original. Mas primeiro, precisamos definir matematicamente o que é um algoritmo!

**Definição**

Seja um problema $f:X \rightarrow Y$ e um computador com sistema de ponto flutuante que satisfaz [\[fundamental_axiom_of_floating_point_arithmetic\]](../aritmetica-de-ponto-flutuante/aritmetica-de-ponto-flutuante/index.md#fundamental_axiom_of_floating_point_arithmetic) fixado. O algoritmo de $f$, $\widetilde{f}:X \rightarrow F^{n} \subset Y$, é uma função que representa uma série de passos e suas implementações no computador dado com o objetivo de resolver o problema $f$

**Nota:** $F^{n} \subset Y$ apenas representa que tenho um vetor de números que podem ser representados por $F$ e esse vetor está em $Y$

Bem, sabemos que, se passarmos $x \in X$ para esse algoritmo, o resultado $\widetilde{f}(x)$ pode ser afetado por erros de arredondamento! Na maioria dos casos, $\widetilde{f}$ não é uma função contínua, mas o algoritmo precisa aproximar $f(x)$ da melhor forma possível.

Vamos fazer uma definição para um algoritmo **estável** também! Primeiro, vamos definir a **precisão** de um algoritmo

**Definição: Precisão do Algoritmo**

Um algoritmo $\widetilde{f}$ é preciso se: $$\frac{\|\widetilde{f}(x) - f(x)\|}{\| f(x)\|} = O\left( \varepsilon_{\text{machine}} \right)$$

O QUÊ? O QUE DIABOS $O\left( \varepsilon_{\text{machine}} \right)$ SIGNIFICA??? Calma, calma, farei uma definição formal mais tarde, por agora, você pode entender que um algoritmo é preciso se o erro entre a saída do algoritmo e a saída original não ultrapassa $\varepsilon_{\text{machine}}$

Em algoritmos mal-condicionados, a igualdade mostrada na definição é muito ambiciosa, porque erros de arredondamento são inevitáveis, nesse tipo de algoritmos, esse arredondamento pode causar grandes erros, ultrapassando os erros desejados que queríamos

Agora podemos definir um algoritmo **estável**

<a id="stable_algorithm"></a>

**Definição: Algoritmo Estável**

Um algoritmo $\widetilde{f}$ para um problema $f$ é estável se $$\forall x\text{ é válido que }\frac{\|\widetilde{f}(x) - f\left( \widetilde{x} \right)\|}{\| f\left( \widetilde{x} \right)\|} = O\left( \varepsilon_{\text{machine}} \right)$$ $$\text{ para um }\widetilde{x}\text{ com }\frac{\|\widetilde{x} - x\|}{\| x\|} = O\left( \varepsilon_{\text{machine}} \right)$$

Espere, o quê? O que essa definição significa?

Significa que, todos os dados semelhantes aos meus dados originais passados para o meu algoritmo retornarão saídas muito semelhantes às soluções corretas (isso é mostrado com $\varepsilon_{\text{machine}}$, ou seja, a diferença entre as soluções dadas pelo algoritmo e as soluções reais não ultrapassará $\varepsilon_{\text{machine}}$)

Existe outro tipo de **estabilidade**, muito poderoso:

**Definição: Estabilidade Retroativa**

Um algoritmo $\widetilde{f}$ para $f$ é **estável retroativamente** se: $$\forall x \in X\text{ é válido que }\exists\widetilde{x}\text{ com }\frac{\|\widetilde{x} - x\|}{\| x\|} = O\left( \varepsilon_{\text{machine}} \right)\text{ tal que }\widetilde{f}(x) = f\left( \widetilde{x} \right)$$

Isso significa que, se eu passar os dados para o algoritmo, posso encontrar uma perturbação muito pequena $\widetilde{x}$ tal que a solução do problema se eu passar essa perturbação é a **mesma** que se eu passar os dados originais para o algoritmo!

**Exemplo**

Dado o dado $x \in {\mathbb{C}}$, verifique se o algoritmo $x \oplus x$ para calcular o problema de somar dois números iguais (solução é $2x$) é estável retroativamente:

Temos que $$f(x) = x + xe\widetilde{f}(x) = x \oplus x$$ Isso significa $$\widetilde{f}(x) = (2x)(1 + \varepsilon)$$ Vamos verificar se esse algoritmo é **estável**. Primeiro, defina $\widetilde{x} = x(1 + \varepsilon)$, sabemos que $\varepsilon = O\left( \varepsilon_{\text{machine}} \right)$, vamos verificar se o erro relativo entre $x$ e $\widetilde{x}$ é $O\left( \varepsilon_{\text{machine}} \right)$: $$\frac{\|\widetilde{x} - x\|}{\| x\|} = \frac{\| x(1 + \varepsilon) - x\|}{\| x\|} = \frac{\| x(1 + \varepsilon - 1)\|}{\| x\|} = \vert \varepsilon\vert  = O\left( \varepsilon_{\text{machine}} \right)$$ Então $x(1 + \varepsilon)$ é uma definição **válida** para $\widetilde{x}$, deixando isso claro, vamos verificar se $\widetilde{f}$ é estável $$\frac{\|\widetilde{f}(x) - f\left( \widetilde{x} \right)\|}{\| f\left( \widetilde{x} \right)\|} = \frac{\| 2x(1 + \varepsilon) - 2x(1 + \varepsilon)\|}{\| f\left( \widetilde{x} \right)\|} = 0 = O\left( \varepsilon_{\text{machine}} \right)$$ Isso significa que $\widetilde{f}$ é estável, mas é **estável retroativamente**? Precisamos de uma definição de $\widetilde{x}$ que ainda satisfaça a condição de $x$ definida em [\[stable_algorithm\]](#stable_algorithm). Vamos verificar se nossa definição satisfaz, já verificamos que a condição é válida, mas ela satisfaz $f\left( \widetilde{x} \right) = \widetilde{f}(x)$? $$\widetilde{f}(x) = 2x(1 + \varepsilon)$$ $$f\left( \widetilde{x} \right) = 2x(1 + \varepsilon)$$ Isso significa que esse algoritmo **É** de fato **estável retroativamente**

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Definição Formal de $O\left( \varepsilon_{\text{machine}} \right)$](definicao-formal-de-o-left-varepsilon-text-machine-right/index.md)
2. [Dependência de $m$ e $n$](dependencia-de-m-e-n/index.md)
3. [Independência da Norma](independencia-da-norma/index.md)
4. [Estabilidade da Aritmética de Ponto Flutuante](estabilidade-da-aritmetica-de-ponto-flutuante/index.md)
5. [Precisão de um Algoritmo Estável Retroativamente](precisao-de-um-algoritmo-estavel-retroativamente/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Mais sobre Épsilon Máquina](../aritmetica-de-ponto-flutuante/mais-sobre-epsilon-maquina/index.md)
- Próximo: [Definição Formal de $O\left( \varepsilon_{\text{machine}} \right)$](definicao-formal-de-o-left-varepsilon-text-machine-right/index.md)
