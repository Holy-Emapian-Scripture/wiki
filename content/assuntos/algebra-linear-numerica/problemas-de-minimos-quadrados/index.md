---
layout: "default"
title: "Problemas de Mínimos Quadrados"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 34
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-34"></a>

# Problemas de Mínimos Quadrados


<a id="projecoes-ortogonais-e-as-equacoes-normais"></a>
<a id="secao-35"></a>

## Projeções Ortogonais e as Equações Normais

Faz sentido que a solução seja obtida por uma projeção de $b$ em $C(A)$, mas que tipo de projeção? Você pode imaginar um plano 3D, se visualizar $A$ como um plano, faz sentido que o $Ax$ que minimiza $\| b - Ax\|_{2}$, veja a imagem na próxima página:

![](../assets/Projection_Min_Squared.jpg)

Ok, parece correto, e podemos pensar nisso intuitivamente, mas está matematicamente correto?

**Teorema**

Seja $A \in {\mathbb{C}}^{m \times n}\ (m \geq n)$, $b \in {\mathbb{C}}^{m}$. $x$ minimiza $\| b - Ax\|_{2} \Leftrightarrow b - Ax \perp C(A)$

**Demonstração**

Primeiro, defina como $P$ um projetor ortogonal que projeta sobre $C(A)$ e $c = Pb$

Bem, sabemos que $c \perp b - Ax$ (veja a imagem anterior), então, como $c$ está em $C(A)$, podemos expressar $c = Ay$ para algum $y \in {\mathbb{C}}^{n} \neq 0$. Vamos escrever tudo: $$c^{\ast (b - Ax)} = 0 \Leftrightarrow y^{\ast}A^{\ast (b - Ax)} = 0$$ Sabemos que $y \neq 0$, isso significa $A^{\ast (b - Ax)} = 0$ $$A^{\ast (b - Ax)} = 0 \Leftrightarrow A^{\ast}b - A^{\ast}Ax = 0 \Leftrightarrow A^{\ast}b = A^{\ast}Ax$$ Queremos $x$ que satisfaça esta equação, se $A^{\ast}A$ é inversível, então $$x = \left( A^{\ast}A \right)^{- 1}A^{\ast}b$$ E observe que, se aplicarmos $A$ em $x$, isso me dá a fórmula exata da projeção ortogonal de $b$ sobre $A$: $$Ax = {A\left( A^{\ast}A \right)}^{- 1}A^{\ast}b$$

A equação $A^{\ast}b = A^{\ast}Ax$ é conhecida como “equação normal”, e usá-la nos permite obter alguns algoritmos diferentes para calcular a solução de mínimos quadrados!

<a id="secao-36"></a>

### Padrão

Se $A$ tem posto completo, isso significa que $A^{\ast}A$ é um sistema de equações quadrado, hermitiano e definido positivo com dimensão $n$. Então, podemos fazer a Fatoração de Cholesky de $A^{\ast}A$, obtendo $R^{\ast}R$ onde $R$ é triangular superior, então podemos fazer a redução: $$A^{\ast}b = A^{\ast}Ax \Leftrightarrow A^{\ast}b = R^{\ast}Rx$$ Então, podemos fazer o algoritmo:

1.  Formar a matriz $A^{\ast}A$ e $A^{\ast}b$

2.  Calcular a Fatoração de Cholesky de $A^{\ast}A$, $R^{\ast}R$

3.  Resolver o sistema triangular inferior $R^{\ast}w = A^{\ast}b$ para $w$

4.  Resolver o sistema triangular superior $Rx = w$ para $x$

<a id="secao-37"></a>

### Fatoração $QR$

Um método “moderno” usa a fatoração $QR$ reduzida. Usando o algoritmo de Householder, calculamos $A = \widehat{Q}\widehat{R}$ (Lembre-se que $\widehat{R}$ é quadrada e $\widehat{Q}$ é $m \times n$). Podemos então reescrever o projetor ortogonal $P = \left( A^{\ast}A \right)^{- 1}A$ como $P = \widehat{Q}{\widehat{Q}}^{\ast}$, porque $C(A) = C(Q)$. $$\widehat{Q}\widehat{R}x = \widehat{Q}{\widehat{Q}}^{\ast}b \Leftrightarrow \widehat{R}x = {\widehat{Q}}^{\ast}b$$ E se $R$ tem inversa, podemos multiplicá-lo por $R^{- 1}$ e ter $A^{+} = \widehat{R}{\widehat{Q}}^{\ast}$

1.  Calcular a fatoração $QR$ reduzida $A = \widehat{Q}\widehat{R}$

2.  Calcular o vetor ${\widehat{Q}}^{\ast}b$

3.  Resolver o sistema triangular superior $\widehat{R}x = {\widehat{Q}}^{\ast}b$ para $x$

<a id="secao-38"></a>

### S.V.D

Se obtivermos $A = \widehat{U}\widehat{\Sigma}V^{\ast}$ (Fatoração S.V.D reduzida), podemos reescrever $P$ como $P = \widehat{U}{\widehat{U}}^{\ast}$, porque $\widehat{U}$ é retangular com colunas ortonormais e $C(A) = C\left( \widehat{U} \right)$, então projetar ortogonalmente sobre $C(A)$ é o mesmo que projetar ortogonalmente sobre $C\left( \widehat{U} \right)$, análogo ao método $QR$, temos: $$\widehat{U}\widehat{\Sigma}V^{\ast}x = \widehat{U}{\widehat{U}}^{\ast}b \Leftrightarrow \widehat{\Sigma}V^{\ast}x = {\widehat{U}}^{\ast}b$$ Observe que podemos obter uma nova fórmula para $A^{+}$, que é $A^{+} = V{\widehat{\Sigma}}^{- 1}{\widehat{U}}^{\ast}$

1.  Calcular a S.V.D reduzida $A = \widehat{U}\widehat{\Sigma}V^{\ast}$

2.  Calcular o vetor ${\widehat{U}}^{\ast}b$

3.  Resolver o sistema diagonal $\widehat{\Sigma}w = {\widehat{U}}^{\ast}b$ para $w$

4.  Definir $x = Vw$

------------------------------------------------------------------------

<!-- wiki:original:fim -->


## Conteúdos relacionados

- [Regressão Linear — Aprendizado de Máquina](../../aprendizado-de-maquina/regressao-linear/index.md)


## Percurso de estudo

[Trilha: A1](../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Triangularização de Householder](../triangularizacao-de-householder/index.md)
- Próximo: [Condicionamento e Números de Condição](../condicionamento-e-numeros-de-condicao/index.md)
