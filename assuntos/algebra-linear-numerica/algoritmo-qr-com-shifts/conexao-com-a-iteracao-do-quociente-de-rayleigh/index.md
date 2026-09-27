---
layout: "default"
title: "Conexão com a Iteração do Quociente de Rayleigh — Algoritmo QR com Shifts"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 52
---

[Álgebra Linear Numérica](../../index.md) · [Algoritmo QR com Shifts](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-52"></a>

# Conexão com a Iteração do Quociente de Rayleigh

Beleza, vimos que os shifts são bem poderosos para o cálculo das matrizes, mas aí tu pode tá se perguntando: “Q djabo eu faço pra escolher meus shift? Eu tenho q ser Mãe de Ná?”. E você está corretíssimo, precisamos de um método para escolher shifts interessantes para o algoritmo.

Faz sentido a gente tentar usar o quociente de Rayleigh pra isso. A gente quer tentar fazer com que a última coluna de ${\underline{Q}}^{(k)}$ converja. Então faz sentido a gente usar o Quociente de Rayleigh com essa última coluna né? $$\mu^{(k)} = \frac{\left( q_{m}^{(k)} \right)^{T}Aq_{m}^{(k)}}{{q_{m}^{(k)}}^{T}q_{m}^{(k)}} = \left( q_{m}^{(k)} \right)^{T}Aq_{m}^{(k)})$$

Se escolhermos esse valor, as estimativas $\mu^{(k)}$ (Estimativa de autovalor) e $q_{m}^{(k)}$ estimativa de autovetor são identicos àqueles computados pela iteração do quociente de rayleigh com o vetor inicial sendo $e_{m}$

Tem um negócio bem massa que a gente pode ver com isso. Que o valor $A_{mm}^{(k)}$ é igual a $r\left( q_{m}^{(k)} \right)$ ($r$ sendo a função do quociente de rayleigh), a gente pode visualizar assim: $$A_{mm}^{(k)} = e_{m}^{T}A^{(k)}e_{m} = e_{m}^{T}\left( {\underline{Q}}^{(k)} \right)^{T}A{\underline{Q}}^{(k)}e_{m} = {q_{m}^{(k)}}^{T}Aq_{m}^{(k)}$$

Ou seja, escolher $\mu^{(k)}$ como sendo o coeficiente de rayleigh de $q_{m}^{(k)}$ é a mesma coisa que escolher ele como sendo a última entrada de $A^{(k)}$. A gente chama isso de **Shift do Quociente de Rayleigh**.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Conexão com o Algoritmo de Iteração Reversa com Shifts](../conexao-com-o-algoritmo-de-iteracao-reversa-com-shifts/index.md)
- Próximo: [Wilkinson Shift](../wilkinson-shift/index.md)
