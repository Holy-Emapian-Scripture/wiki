---
layout: "default"
title: "Números não em $F$ — Aritmética de Ponto Flutuante"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 41
---

[Álgebra Linear Numérica](../../index.md) · [Aritmética de Ponto Flutuante](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-50"></a>

# Números não em $F$

Quando tentamos representar um número que não está em $F$, o computador pode fazer 2 coisas:

1.  **Arredondar**: Obtemos $t + 1$ dígitos do número, e verificamos se o $(t + 1)$-ésimo dígito é maior ou igual a $\left\lceil \frac{\beta}{2} \right\rceil$, se for, excluímos o $(t + 1)$-ésimo dígito e somamos 1 ao $t$-ésimo dígito. Se o $(t + 1)$-ésimo dígito for menor que $\left\lceil \frac{\beta}{2} \right\rceil$, então apenas excluímos o $(t + 1)$-ésimo dígito

    **Exemplo**

    Arredonde 10324 sabendo que $F$ tem precisão $4$ e $e \in \lbrack - \infty, + \infty\rbrack$ e $\beta = 10$.

    Convertendo para a notação de mantissa e expoente: $10324 = 0,10324 \ast 10^{5}$, temos 5 dígitos, então vamos ver o $5$-ésimo. $4 \geq \left\lceil \frac{10}{2} \right\rceil \Leftrightarrow 4 \geq 5$? Não, então o número arredondado será $0,1032 \ast 10^{5}$

2.  **Truncar**: Se a mantissa do número passar de $t$ dígitos, removemos todos os dígitos após o $t$-ésimo

Sabendo disso, podemos finalmente entender o que é $\varepsilon_{\text{machine}}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Conjunto de Ponto Flutuante](../conjunto-de-ponto-flutuante/index.md)
- Próximo: [Épsilon Máquina](../epsilon-maquina/index.md)
