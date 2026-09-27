---
layout: "default"
title: "Estabilidade da Triangularização de Householder"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 1
---

[Álgebra Linear Numérica](index.md)

<!-- wiki:original:inicio -->

<a id="secao-1"></a>

# Estabilidade da Triangularização de Householder


<a id="o-experimento"></a>
<a id="section_householder_stability_experiment"></a>

## O Experimento

O livro nos mostra um experimento no matlab para demonstrar a estabilidade em ação e alguns conceitos importantes, irei fazer o mesmo experimento, porém, utilizarei código em python e mostrarei meus resultados aqui.

Primeiro de tudo, mostraremos na prática que o algoritmo de **Householder** é **backwards stable**. Vamos criar uma matriz $A$ com a fatoração $QR$ conhecida, então vamos gerar as matrizes $Q$ e $R$. Aqui, temos que $\varepsilon_{\text{machine }} = 2.220446049250313 \times 10^{- 16}$:

<a id="hh-comparison"></a>

``` python
import numpy as np
np.random.seed(0)  # Ter sempre os mesmos resultados
## Crio R triangular superior (50 x 50)
R_1 = np.triu(np.random.random_sample(size=(50, 50)))
## Crio a matriz Q a partir de uma matriz aleatória
Q_1, _ = np.linalg.qr(np.random.random_sample(size=(100, 50)), mode='reduced')
## Crio a minha matriz com fatoração QR conhecida (A = Q_1 R_1)
A = Q_1 @ R_1
## Calculo a fatoração QR de A usando Householer
Q_2, R_2 = householder_qr(A)
```

Sabemos que, por conta de erros de aproximação, a matriz $A$ que temos no código não é **exatamente** igual a que obteríamos se tivéssemos fazendo $Q_{1}R_{1}$ na mão, mas é preciso o suficiente. Podemos ver aqui que elas são diferentes:

**CÓDIGO**

<a id="matrices-partialerences"></a>

``` python
print(np.linalg.norm(Q_1 - Q_2))
print(np.linalg.norm(R_1 - R_2))
```

**SAÍDA**

    7.58392995752057e-8
    8.75766271246312e-9

Perceba que é um erro muito grande, não é tão próximo de $0$ quanto eu gostaria, se eu printasse as matrizes $Q_{2}$ e $R_{2}$ eu veria que, as entradas que deveriam ser $0$, tem erro de magnitude $\approx 10^{17}$. Bem, se ambas tem um erro tão grande, então o resultado da multiplicação delas em comparação com $A$ também vai ser grande, correto?

**CÓDIGO**

<a id="partialerence-A"></a>

``` python
print(np.linalg.norm(A - Q_2 @ R_2))
```

**SAÍDA**

    3.8022328832723555e-14

Veja que, mesmo minhas matrizes $Q_{2}$ e $R_{2}$ tendo erros bem grandes com relação às matrizes $Q_{1}$ e $R_{2}$, conseguimos uma aproximação de $A$ bem precisa com ambas. Vamos agora dar um destaque nessa acurácia de $Q_{2}R_{2}$:

**CÓDIGO**

``` python
delta_Q_1 = np.random.random_sample(size=Q_1.shape)
delta_R_1 = np.random.random_sample(size=R_1.shape)
Q_3 = Q_1 + delta_Q_1 * 1e-4
R_3 = R_1 + delta_R_1 * 1e-4
print(np.linalg.norm(A - Q_3 @ R_3))
```

**SAÍDA**

    0.05197521348918455

Perceba o quão grande é esse erro, é **enorme**, então: $Q_{2}$ não é melhor que $Q_{3}$, $R_{2}$ não é melhor que $R_{3}$, mas $Q_{2}R_{2}$ é muito mais preciso do que $Q_{3}R_{3}$

<a id="teorema"></a>
<a id="section_householder_stability_theorem"></a>

## Teorema

Vamos ver que, de fato, o algoritmo de **Householder** é **backwards stable** para toda e qualquer matriz $A$. Fazendo a análise de backwards stable, nosso resultado precisa ter esse formato aqui: $$\widetilde{Q}\widetilde{R} = A + \delta A$$ com $\|\delta A\|/\| A\| = O\left( \varepsilon_{\text{machine}} \right)$. Ou seja, calcular a $QR$ de $A$ pelo algoritmo é o mesmo que calcular a $QR$ de $A + \delta A$ da forma matemática. Mas aqui temos uns adendos.

A matriz $\widetilde{R}$ é como imaginamos, a matriz triangular superior obtida pelo algoritmo, onde as entradas abaixo de 0 podem não ser exatamente 0, mas **muito próximas**.

Porém, $\widetilde{Q}$ **não é aproximadamente** ortogonal, ela é **perfeitamente** ortogonal, mas por quê? Pois no algoritmo de Householder, não calculamos essa matriz diretamente, ela fica “*implícita*” nos cálculos, logo, podemos assumir que ela é perfeitamente ortogonal, já que o computador não a calcula, ou seja, não há erros de arredondamento. Vale lembrar também que $\widetilde{Q}$ é definido por: $$\widetilde{Q} = {\widetilde{Q}}_{1}{\widetilde{Q}}_{2.}..{\widetilde{Q}}_{n}$$ De forma que $\widetilde{Q}$ é perfeitamente unitária e cada matriz ${\widetilde{Q}}_{j}$ é definida como o refletor de householder no vetor de floating point $\widetilde{v_{k}}$ (Olha a página 73 do livro pra você relembrar direitinho o que é esse vetor $\widetilde{v_{k}}$ no algoritmo). Lembrando que $\widetilde{Q}$ é perfeitamente ortogonal, já que eu não calculo ela no computador diretamente, se eu o fizesse, então ela não seria perfeitamente ortogonal, teriam pequenos erros.

**Teorema: Householder's Backwards Stability**

Deixe que a fatoração QR de $A \in {\mathbb{C}}^{m \times n}$ seja dada por $A = QR$ e seja computada pelo algoritmo de **Householder**, o resultado dessa computação são as matrizes $\widetilde{Q}$ e $\widetilde{R}$ definidas anterioremente. Então temos: $$\widetilde{Q}\widetilde{R} = A + \delta A$$ Tal que: $$\frac{\|\delta A\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$ para algum $\delta A \in {\mathbb{C}}^{m \times n}$

<a id="algoritmo-para-resolver-ax-b"></a>
<a id="section_householder_stability_solve"></a>

## Algoritmo para resolver $Ax = b$

Vimos que o algoritmo de householder é backwards stable, show! Porém, sabemos que não costumamos fazer essas fatorações só por fazer né, a gente faz pra resolver um sistema $Ax = b$, ou outros tipos de problemas. Certo, mas, se fizermos um algoritmo que resolve $Ax = b$ usando a fatoração QR obtida com householder, a gente precisa que $Q$ e $R$ sejam precisos? Ou só precisamos que $QR$ seja preciso? O bom é que precisamos apenas que $QR$ seja precisa! Vamos mostrar isso para a resolução de sistemas $m \times m$ não singulares.

<a id="solve-Axb-hh"></a>

1.  **function** ResolverSistema($A \in {\mathbb{C}}^{m \times n}$, $b \in {\mathbb{C}}^{m \times 1}$) {

    1.  $QR = \text{ Householder}(A)$

    2.  $y = Q^{\ast}b$

    3.  $x = R^{- 1}y$

    4.  **return** $x$

2.  }

*Figura 1. Algoritmo para calcular $Ax = b$*

Esse algoritmo é **backwards stable**, e é bem passo-a-passo já que cada passo dentro do algoritmo é **backwards stable**.

**Teorema**

O [\[solve-Axb-hh\]](#solve-Axb-hh) para solucionar $Ax = b$ é **backwards stable**, satisfazendo $$(A + \Delta A)\widetilde{x} = b$$ com $$\frac{\|\Delta A\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$ para algum $\Delta A \in {\mathbb{C}}^{m \times n}$

**Demonstração**

Quando computamos ${\widetilde{Q}}^{\ast}b$, por conta de erros de aproximação, não obtemos um vetor $y$, e sim $\widetilde{y}$. É possível mostrar (Não faremos) que esse vetor $\widetilde{y}$ satisfaz: $$\left( \widetilde{Q} + \delta Q \right)\widetilde{y} = b$$ satisfazendo $\frac{\|\delta Q\|}{\|\widetilde{Q}\|} = O\left( \varepsilon_{\text{machine}} \right)$

Ou seja, só pra esclarecer, aqui (nesse passo de $y$) a gente ta tratando o problema $f$ de calcular $Q^{\ast}b$, ou seja $f(Q) = Q^{\ast}b$, então usamos um algoritmo comum $\widetilde{f}(Q) = Q^{\ast}b$ (Não matematicamente, mas usando as operações de um computador), daí reescrevemos isso como $\widetilde{f}(Q) = (Q + \delta Q)^{\ast}b$, por isso podemos reescrever como a equação que falamos anteriormente.

No último passo, a gente usa **back substitution** pra resolver o sistema $x = R^{- 1}y$ e esse algoritmo é **backwards stable** (Isso vamos provar na próxima lecture). Então temos que: $$\left( \widetilde{R} + \delta R \right)\widetilde{x} = \widetilde{y}$$ satisfazendo $\frac{\|\delta R\|}{\|\widetilde{R}\|} = O\left( \varepsilon_{\text{machine}} \right)$

Agora podemos ir pro algoritmo em si, temos um problema $f(A):\text{ Resolver }Ax = b$, daí usamos $\widetilde{f}(A):\text{ Usando householder, resolve }Ax = b$. Então, se o algoritmo nos dá as matrizes perturbadas que citei anteriormente ($Q + \delta Q$ e $R + \delta R$), ao substituir isso por $A$, eu tenho que ter um resultado $A + \Delta A$ com $\frac{\|\Delta A\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$, vamos ver: $$b = \left( \widetilde{Q} + \delta Q \right)\left( \widetilde{R} + \delta R \right)\widetilde{x}$$ $$b = \left( A + \delta A + \widetilde{Q}(\delta R) + (\delta Q)\widetilde{R} + (\delta Q)(\delta R) \right)\widetilde{x}$$ $$b = (A + \Delta A)\widetilde{x} \Leftrightarrow \Delta A = \delta A + \widetilde{Q}(\delta R) + (\delta Q)\widetilde{R} + (\delta Q)(\delta R)$$

Como $\Delta A$ é a soma de 4 termos, temos que mostrar que cada um desses termos é pequeno com relação a $A$ (Ou seja, mostrar que $\frac{\| X\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$ onde $X$ é um dos 4 termos de $\Delta A$).

- $\delta A$: Pela própria definição que o algoritmo de householder é backwards stable nós sabemos que $\delta A$ satisfaz a condição de $O\left( \varepsilon_{\text{machine}} \right)$

- $(\delta Q)\widetilde{R}$:

$$\frac{\|(\delta Q)\widetilde{R}\|}{\| A\|} \leq \|(\delta Q)\|\frac{\|\widetilde{R}\|}{\| A\|}$$ Perceba que $$\frac{\|\widetilde{R}\|}{\| A\|} \leq \frac{\|{\widetilde{Q}}^{\ast (A + \delta A)}\|}{\| A\|} \leq \|{\widetilde{Q}}^{\ast}\|\frac{\| A + \delta A\|}{\| A\|}$$ Lembra que, quando trabalhamos com $O\left( \varepsilon_{\text{machine}} \right)$, a gente ta trabalhando com um limite implícito que, no caso, aqui é $\varepsilon_{\text{machine }} \rightarrow 0$. Ou seja, se temos que $\varepsilon_{\text{machine }} \rightarrow 0$, o erro de arredondamento diminui cada vez mais, certo? Então $\delta A \rightarrow 0$ ou seja: $$\frac{\|\widetilde{R}\|}{\| A\|} = O(1)$$ O que nos indica que $$\|\delta Q\|\frac{\|\widetilde{R}\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$

- $\widetilde{Q}(\delta R)$: Provamos de uma forma similar

$$
\frac{\|\widetilde{Q}(\delta R)\|}{\| A\|} \leq \|\widetilde{Q}\frac{\|\left( \|\delta R\| \right)}{\| A\|} = \|\widetilde{Q}\frac{\|\left( \|\delta R\| \right)}{\|\widetilde{R}\|}\frac{\|\widetilde{R}\|}{\| A\|} \leq \|\widetilde{Q}\frac{\|\left( \|\delta R\| \right)}{\|\widetilde{R}\|} = O\left( \varepsilon_{\text{machine}} \right)
$$

- $(\delta Q)(\delta R)$: Por último:

$$\frac{\|(\delta Q)(\delta R)\|}{\| A\|} \leq \|\delta Q\|\frac{\|\delta R\|}{\| A\|} = O\left( \varepsilon_{\text{machine}}^{2} \right)$$ Ou seja, todos os termos de $\Delta A$ são da ordem $O\left( \varepsilon_{\text{machine}} \right)$, ou seja, provamos que resolver $Ax = b$ usando householder é um algoritmo **backwards stable**. Se a gente junta alguns teoremas e temos que:

**Teorema**

A solução $\widetilde{x}$ computada pelo algoritmo satisfaz: $$\frac{\|\widetilde{x} - x\|}{\| x\|} = O\left( \kappa(A)\varepsilon_{\text{machine}} \right)$$

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Próximo: [Estabilidade da Back Substitution](estabilidade-da-back-substitution.md)
