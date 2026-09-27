---
layout: "default"
title: "O Experimento — Estabilidade da Triangularização de Householder"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 2
---

[Álgebra Linear Numérica](../../index.md) · [Estabilidade da Triangularização de Householder](../index.md)

<!-- wiki:original:inicio -->
<a id="section_householder_stability_experiment"></a>

# O Experimento

O livro nos mostra um experimento no matlab para demonstrar a estabilidade em ação e alguns conceitos importantes, irei fazer o mesmo experimento, porém, utilizarei código em python e mostrarei meus resultados aqui.

Primeiro de tudo, mostraremos na prática que o algoritmo de **Householder** é **backwards stable**. Vamos criar uma matriz $A$ com a fatoração $QR$ conhecida, então vamos gerar as matrizes $Q$ e $R$. Aqui, temos que $\varepsilon_{\text{machine }} = 2.220446049250313 \times 10^{- 16}$:

<a id="hh-comparison"></a>

``` python
import numpy as np
np.random.seed(0)  # Ter sempre os mesmos resultados
# Crio R triangular superior (50 x 50)
R_1 = np.triu(np.random.random_sample(size=(50, 50)))
# Crio a matriz Q a partir de uma matriz aleatória
Q_1, _ = np.linalg.qr(np.random.random_sample(size=(100, 50)), mode='reduced')
# Crio a minha matriz com fatoração QR conhecida (A = Q_1 R_1)
A = Q_1 @ R_1
# Calculo a fatoração QR de A usando Householer
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

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Estabilidade da Triangularização de Householder](../index.md)
- Próximo: [Teorema](../teorema/index.md)
