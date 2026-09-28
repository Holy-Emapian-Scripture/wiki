---
layout: "default"
title: "Estabilidade de Algoritmos de Mínimos Quadrados"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 9
---

[Álgebra Linear Numérica](index.md)

<!-- wiki:original:inicio -->

<a id="secao-9"></a>

# Estabilidade de Algoritmos de Mínimos Quadrados


<a id="secao-10"></a>

## Primeira Etapa

Vamos fazer isso na prática. Vamos montar um cenário para a aplicação de cada um dos algoritmos. Vamos pegar $m$ pontos igualmente espaçados entre $0$ e $1$, montamos a <u>[matriz de vandermonde](https://en.wikipedia.org/wiki/Vandermonde_matrix)</u> desses pontos e aplicamos uma função que tentaremos prever com polinômios:

**CÓDIGO**

<a id="min-squared-algorithms-init"></a>

``` python
import numpy as np
m = 100
n = 15
t = np.linspace(0, 1, m)
A = np.vander(t, n, True)
b = np.exp(np.sin(4*t))/2.00678728e+03
```

Oxe, por que que tem essa divisão esquisita no final? Quando a gente não faz essa divisão, ao fazer a previsão dos coeficientes que aproximam a função, temos que o último coeficiente previsto ($x_{15}$) é igual a `2.00678728e+03`, então, nós dividimos $b$ por esse valor para que o último coeficiente seja igual a $1$ no caso matematicamente correto (Sem erros numéricos), assim poderemos fazer comparações apenas visualizando o último número dos coeficientes calculados.

<a id="secao-11"></a>

## Householder

O algoritmo padrão para [problemas de mínimos quadrados](problemas-de-minimos-quadrados.md). Vejamos:

**CÓDIGO**

``` python
Q, R = householder_qr(A)
x = np.linalg.solve(R, Q.T @ b)
print(1-x[-1])  # Erro relativo
```

**SAÍDA**

    1.9845992627054443e-09

Temos um erro de grandeza $10^{9}$, porém, no Python, trabalhamos com precisão IEEE 754 ($\varepsilon = 2.220446049250313e - 16$), o que nos mostra um erro de precisão MUITO grande (Ordem de $10^{7}$ de diferença). Porém, aqui nós calculamos $Q$ explicitamente e, no resumo 1, foi comentado que isso normalmente não acontece, então vamos ver se o erro muda ao trocarmos $Q$ por uma versão implícita

**CÓDIGO**

``` python
Q, R = householder_qr(np.c_[A, b])
print(R.shape)
Qb = R[0:n, n]
R = R[0:n, 0:n]
x = np.linalg.solve(R, Qb)
print(1-x[-1])
```

**SAÍDA**

    1.989168163518684e-09

Deu pra ver que da quase a mesma coisa do resultado anterior, ou seja, os erros da fatoração de $A$ são maiores que os de $Q$. Pode ser provado que essas duas variações são **backward stable**. O mesmo vale para uma terceira variação que utiliza do **pivotamento** de colunas (Não é discutido nem no livro, tampouco nesse resumo)

**Teorema**

Deixe um problema de mínimos quadrados em uma matriz de posto completo $A$ ser resolvida por fatoração **[Householder](triangularizacao-de-householder.md)** em um computador ideal. O algoritmo é **backward stable** tal que: $$\|(A + \delta A)\widetilde{x} - b\| = \min,\ \ \frac{\|\delta A\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$ para algum $\delta A \in {\mathbb{C}}^{m \times n}$.

<a id="ortogonalizacao-de-gram-schmidt"></a>
<a id="secao-12"></a>

## Ortogonalização de Gram-Schmidt

A gente também pode tentar resolver pelo método de Gram-Schmidt modificado, vamos ver o que a gente consegue:

**CÓDIGO**

``` python
Q, R = modified_gram_schmidt(A)
x = np.linalg.solve(R, Q.T @ b)
print(1-x[-1])
```

**SAÍDA**

    -0.01726542

Meu amigo, esse erro é **terrível**. O resultado obtido é tenebroso de ruim. O livro comenta também de outro método que envolve fazer umas manipulações em $Q$, mas como o próprio diz que envolve trabalho extra, desnecessário e não deveria ser usado na prática, nem vou comentar sobre aqui.

Mas a gente pode usar um método parecido com o que fizemos antes em unir $A$ e $b$ numa única matriz:

**CÓDIGO**

``` python
Q, R = modified_gram_schmidt(np.c_[A, b])
Qb = R[0:n, n]
R = R[0:n, 0:n]
x = np.linalg.solve(R, Qb)
print(1-x[-1])
```

**SAÍDA**

    -1.3274502852489434e-07

Olha só! Já deu uma melhorada no algoritmo!

**Teorema**

Solucionar o problema de mínimos quadrados de uma matriz $A$ com posto completo utilizando o algoritmo de Gram-Schmidt (Fazendo de acordo como o código anterior mostra em que $Q^{\ast}b$ é implícito) é **backward stable**

<a id="equacoes-normais"></a>
<a id="secao-13"></a>

## Equações Normais

A gente pode resolver por equações normais, que é o passo inicial para todos os outros métodos né? Vamos ver o que obtemos:

**CÓDIGO**

``` python
x = np.linalg.solve(A.T @ A, A.T @ b)
print(1-x[-1])
```

**SAÍDA**

    1.35207472

Meu amigo, esse erro é **TENEBROSO**, não chegou nem **PERTO** do resultado. Claramente as equações normais são um método **instável** de calcular mínimos quadrados. Vamos dar uma visualizada no porquê isso ocorre:

Suponha que nós temos um algoritmo **backward stable** para o problema de mínimos quadrados com uma matriz $A$ de posto-completo que retorna uma solução $\widetilde{x}$ satisfazendo $\|(A + \delta A)\widetilde{x} - b\| = \min$ para algum $\delta A$ com $\|\delta A\|/\| A\| = O\left( \varepsilon_{\text{machine}} \right)$. Pelo teorema da acurácia de algoritmos backward stable (Resumo 1) e o [condicionamento do problema de mínimos quadrados](condicionando-problemas-de-minimos-quadrados.md#conditioning-min-squared-problems) temos: $$\frac{\|\widetilde{x} - x\|}{\| x\|} = O\left( \left( \kappa + \frac{\kappa^{2}\tan(\theta)}{\eta} \right)\varepsilon_{\text{machine}} \right)$$<a id="normal-equation-algorithm-x-partialerence"></a>

Suponha que $A$ é mal-condicionada. Dependendo dos valores dos híperparâmetros, podem acontecer duas situações diferentes. Se $\tan(\theta)$ for de ordem $1$, então o lado direito da equação [erro no algoritmo das equações normais](#normal-equation-algorithm-x-partialerence) troca e fica $O\left( \kappa^{2}\varepsilon_{\text{machine}} \right)$. Porém, se $\tan(\theta)$ é próximo de 0, ou $\eta$ é próximo de $\kappa$, então então a equação muda para $O\left( \kappa\varepsilon_{\text{machine}} \right)$ (Usa um teorema mais la pra frente, mas é engraçado ver como tudo tá muito interconectado). Porém, a matriz $A^{\ast}A$ tem número de condicionamento ${\kappa(A)}^{2}$, então o máximo que podemos esperar do problema é $O\left( \kappa^{2}\varepsilon_{\text{machine}} \right)$

**Teorema**

A solução de um problema de mínimos quadrados com uma matriz $A$ de posto-completo utilizando de equações normais é **instável**. Porém a estabilidade pode ser alcançada ao restringir para uma classe de problemas onde $\kappa(A)$ é pequeno ou $\frac{\tan(\theta)}{\eta}$ é pequeno.

<a id="secao-14"></a>

## SVD

O último algoritmo a ser mencionado foi utilizando a [SVD](svd.md) de $A$, que nós vimos (no resumo 1) que parecia ser um algoritmo interessante:

**CÓDIGO**

``` python
U, S, Vh = np.linalg.svd(A, full_matrices=False)
S = np.diag(S)
x = (Vh.T * 1/S) @ (U.T @ b)
print(1-x[-1])
```

**SAÍDA**

    -2.3301211e-07

Olha só! Temos uma precisão ótima! (O algoritmo da SVD é o mais confiável e estável, mesmo que o erro mostrado seja maior do que alguns que obtivemos anteriormente)

**Teorema**

A solução do problema de mínimos quadrados com uma matriz $A$ de posto-completo utilizando o algoritmo de SVD é **backward stable**.

<a id="problemas-de-minimos-quadrados-com-posto-incompleto"></a>
<a id="secao-15"></a>

## Problemas de Mínimos Quadrados com Posto-Incompleto

A gente viu a aplicação de algoritmos em problemas de mínimos quadrados utilizando matrizes de posto-completo, mas pode ter outros casos de matrizes com $\text{posto } < n$, ou até $m < n$. Para essa classe de problemas, é necessário definirmos outro tipo de solução, já que nem todos tem o mesmo comportamento. As vezes precisamos restringir a solução com uma condição. Por conta disso, nem todo algoritmo que vimos ser estável até agora vai ser estável nesse tipo de problema, na verdade, apenas o de SVD será e o de Gram-Schmidt com pivotamento nas colunas.

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Condicionando Problemas de Mínimos Quadrados](condicionando-problemas-de-minimos-quadrados.md)
- Próximo: [Problemas de Autovalores](problemas-de-autovalores.md)
