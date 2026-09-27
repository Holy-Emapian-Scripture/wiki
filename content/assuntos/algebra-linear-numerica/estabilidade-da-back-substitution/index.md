---
layout: "default"
title: "Estabilidade da Back Substitution"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 5
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-5"></a>

# Estabilidade da Back Substitution


<a id="teorema-da-estabilidade-retroativa-backward-stability"></a>
<a id="secao-6"></a>

## Teorema da Estabilidade Retroativa (Backward Stability)

A gente viu no último tópico (Estabilidade de Householder) que a **back substitution** era um dos passos para chegar no resultado final, porém, nós apenas assumimos que ela era **backward stable**, mas a gente **não** provou isso! Porém, antes de provarmos isso, vamos estabelecer que as subtrações serão feitas da esquerda para a direita (Sim, isso pode influenciar). Mas, como o livro não explica muito bem o porquê de isso influenciar, vou dar uma breve explicação e exemplificação:

Quando realizamos uma sequência de subtrações pela **direita**, caso os números sejam muito próximos, pode ocorrer o chamado **cancelamento catastrófico**, que é a perca de muitos dígitos significativos, veja um exemplo:

**CÓDIGO**

``` python
a = 1e16
b = 1e16
c = 1
print((a-b)-c)
```

**SAÍDA**

    -1.0

O que parece correto! Mas veja o que acontece se invertermos a ordem e executarmos $a - (b - c)$

**CÓDIGO**

``` python
a = 1e16
b = 1e16
c = 1
print(a-(b-c))
```

**SAÍDA**

    0.0

Veja que houve um problema no arredondamento! Então os sistemas, por convenção, utilizam o esquema de subtrações pela esquerda.

Voltando ao algoritmo de **back substitution**, temos o seguinte teorema:

**Teorema**

Deixe o [\[back-substitution\]](../index.md#back-substitution) ser aplicado a um problema de $Rx = b$ com $R$ triangular superior em um **computador ideal**. Esse algoritmo é **backward stable**, ou seja, a solução $\widetilde{x}$ computada satisfaz: $$(R + \Delta R)\widetilde{x} = b$$ para alguma triangular superior $\Delta R \in {\mathbb{C}}^{m \times m}$ satisfazendo $$\frac{\|\Delta R\|}{\| R\|} = O\left( \varepsilon_{\text{machine}} \right)$$

**Demonstração**

Essa prova não será muito rigorosa matematicamente, vamos montar a prova para matrizes $1 \times 1$, $2 \times 2$ e $3 \times 3$, de forma que o raciocínio que aplicarmos poderá ser aplicado para matrizes de tamanhos maiores.

- **$1 \times 1$**: Nesse caso, $R$ é um único número escalar e, pelo **[\[back-substitution\]](../index.md#back-substitution)**, temos que: $$\widetilde{x_{1}} = b_{1} ⨸ r_{11}$$ E nós **já sabemos** que essa divisão é backward stable, mas vamos analisar melhor. Queremos manter $b$ fixo, então temos que expressar $\widetilde{x_{1}}$ como o $r_{11}$ original vezes uma leve perturbação. Expressamos então $$\widetilde{x_{1}} = \frac{b_{1}}{r_{11}}\left( 1 + \varepsilon_{1} \right)$$ Se definirmos $\varepsilon_{1}' = \frac{- \varepsilon_{1}}{1 + \varepsilon_{1}}$, podemos reescrever a equação assim: $$\begin{array}{r} \widetilde{x_{1}} = \frac{b_{1}}{r_{11}\left( 1 + \varepsilon_{1}' \right)} \Leftrightarrow \widetilde{x_{1}} = \frac{b_{1}}{r_{11}\left( 1 - \frac{\varepsilon_{1}}{1 + \varepsilon_{1}} \right)} \Leftrightarrow \widetilde{x_{1}} = \frac{b_{1}}{r_{11}\frac{1 + \varepsilon_{1} - \varepsilon_{1}}{1 + \varepsilon_{1}}} \\ \Leftrightarrow \widetilde{x_{1}} = \frac{b_{1}}{r_{11}\frac{1}{1 + \varepsilon_{1}}} \Leftrightarrow \widetilde{x_{1}} = \frac{b_{1}}{r_{11}}\left( 1 + \varepsilon_{1} \right) \end{array}$$ Se fizermos a expansão de taylor de $\varepsilon_{1}'$, conseguimos ver: $$- \frac{\varepsilon_{1}}{1 + \varepsilon_{1}} = - \varepsilon_{1} + \varepsilon_{1}^{2} - \varepsilon_{1}^{3} + \varepsilon_{1}^{4} - \ldots$$ Ou seja, $- \varepsilon_{1} + O\left( \varepsilon_{1}^{2} \right)$, o que mostra que $1 + \varepsilon_{1}'$ é uma perturbação válida para o teorema da estabilidade backwards, o que nos mostra também que $$\left( r_{11} + \delta r_{11} \right)\widetilde{x_{1}} = b_{1}$$ Com $$\frac{\|\delta r_{11}\|}{\| r_{11}\|} \leq \varepsilon_{\text{machine }} + O\left( \varepsilon_{\text{machine}}^{2} \right)$$

- **$2 \times 2$**: Beleza, no caso $2 \times 2$, o primeiro passo do algoritmo nós já vimos que é **backwards stable**, vamos para o segundo passo: $$\widetilde{x_{1}} = \left( b_{1} \ominus \left( \widetilde{x_{2}} \otimes r_{12} \right) \right) ⨸ r_{22}$$ Ai meu Deus, fórmula grande do djabo :(. Relaxa, vamo transformar em fórmulas normais com umas perturbações pra gente falar de matemática normal né $$\widetilde{x_{1}} = \frac{\left( b_{1} - \widetilde{x_{2}}r_{12}\left( 1 + \varepsilon_{2} \right) \right)\left( 1 + \varepsilon_{3} \right)}{r_{22}}\left( 1 + \varepsilon_{4} \right)$$ Aqui eu não iniciei os epsilons em $\varepsilon_{1}$ porque eu estou tomando intrínseco que esse $\varepsilon_{1}$ ta no $\widetilde{x_{2}}$ que a gente computa antes de computar o $\widetilde{x_{1}}$ (A gente computa igual o caso $1 \times 1$)

  Podemos definir $\varepsilon_{3}' = - \frac{\varepsilon_{3}}{1 + \varepsilon_{3}}$ e $\varepsilon_{4}' = - \frac{\varepsilon_{4}}{1 + \varepsilon_{4}}$, assim, podemos reescrever: $$\widetilde{x_{1}} = \frac{b_{1} - \widetilde{x_{2}}r_{12}\left( 1 + \varepsilon_{2} \right)}{r_{22}\left( 1 + \varepsilon_{3}' \right)\left( 1 + \varepsilon_{4}' \right)}$$ (Mesmo racicocínio que usamos no caso $1 \times 1$). A gente viu em alguns exercícios da lista que $\left( 1 + O\left( \varepsilon_{\text{machine}} \right) \right)\left( 1 + O\left( \varepsilon_{\text{machine}} \right) \right) = 1 + O\left( \varepsilon_{\text{machine}} \right)$, com isso em mente, podemos reescrever a equação como $$\widetilde{x_{1}} = \frac{b_{1} - \widetilde{x_{2}}r_{12}\left( 1 + \varepsilon_{2} \right)}{r_{22}\left( 1 + 2\varepsilon_{5}' \right)}$$ Esse $2\varepsilon_{5}$ se dá pois, como vimos no caso $1 \times 1$: $$\begin{array}{r} 1 + \varepsilon_{3}' = 1 - \varepsilon_{3} + O\left( \varepsilon_{3}^{2} \right) \\ 1 + \varepsilon_{4}' = 1 - \varepsilon_{4} + O\left( \varepsilon_{4}^{2} \right) \\ \Rightarrow \left( 1 + \varepsilon_{3}' \right)\left( 1 + \varepsilon_{4}' \right) = \left( 1 - \varepsilon_{3} + O\left( \varepsilon_{3}^{2} \right) \right)\left( 1 - \varepsilon_{4} + O\left( \varepsilon_{4}^{2} \right) \right) \\ \Rightarrow 1 - \varepsilon_{4} + O\left( \varepsilon_{4}^{2} \right) - \varepsilon_{3} + \varepsilon_{3}\varepsilon_{4} - \varepsilon_{3}O\left( \varepsilon_{4}^{2} \right) + O\left( \varepsilon_{3}^{2} \right) - \varepsilon_{4}O\left( \varepsilon_{3}^{2} \right) + O\left( \varepsilon_{4}^{2} \right)O\left( \varepsilon_{3}^{2} \right) \end{array}$$ Os termos diferentes de $1$, $\varepsilon_{3}$ e $\varepsilon_{4}$ são irrelevantes, pois são **MUITO** pequenos, o que nos dá $$1 - \varepsilon_{4} - \varepsilon_{3} = 1 - 2\varepsilon_{5}$$ Voltando ao foco, acabamos de mostrar que, se $r_{11}$, $r_{12}$ e $r_{22}$ fossem perturbados por fatores $2\varepsilon_{5}$, $\varepsilon_{2}$ e $\varepsilon_{1}$ **respectivamente**, a conta feita para calcular $b_{1}$, no computador, seria **exata**. Podemos expressar isso na forma $$(R + \delta R)\widetilde{x_{1}} = b_{1}$$ De forma que $$\delta R = \begin{pmatrix} 2\vert \varepsilon_{5}\vert  & \vert \varepsilon_{2}\vert  \\ & \vert \varepsilon_{1}\vert \end{pmatrix}$$

- **A Indução**: Suponha que, no ($j - 1$)-ésimo passo do algoritmo, eu sei que o ${\widetilde{x}}_{j - 1}$ é gerado com um algoritmo backward stable. Nós já mostramos, pelos casos bases, que os primeiros dois passos são backward stable. Vamos relembrar o [\[back-substitution\]](../index.md#back-substitution) para $m$ colunas: $${\widetilde{x}}_{j} = \left( b_{j} \ominus \sum_{k = j + 1}^{m}x_{k} \otimes r_{jk} \right) ⨸ r_{jj}$$ Usando o **Axioma Fundamental do Ponto Flutuante**: $${\widetilde{x}}_{j} = \frac{\left( b_{j} - \sum_{k = j + 1}^{m}x_{k}r_{jk}\left( 1 + \varepsilon_{k} \right) \right)\left( 1 + \varepsilon_{m + 1} \right)}{r_{jj}}\left( 1 + \varepsilon_{m + 2} \right)$$ Definindo $\varepsilon_{m + 1}'$ e $\varepsilon_{m + 2}'$ de forma análoga a que fizemos anteriormente: $${\widetilde{x}}_{j} = \frac{b_{j} - \sum_{k = j + 1}^{m}x_{k}r_{jk}\left( 1 + \varepsilon_{k} \right)}{r_{jj}\left( 1 + \varepsilon_{m + 1}' \right)\left( 1 + \varepsilon_{m + 2}' \right)}$$ Novamente, estamos expressando ${\widetilde{x}}_{j}$ como operações em $x_{k}$ e $b_{j}$ e com entradas **perturbadas** de $R$, mostrando que o algoritmo do **back substitution** é sim **backward stable**

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Estabilidade da Triangularização de Householder](../estabilidade-da-triangularizacao-de-householder/index.md)
- Próximo: [Condicionando Problemas de Mínimos Quadrados](../condicionando-problemas-de-minimos-quadrados/index.md)
