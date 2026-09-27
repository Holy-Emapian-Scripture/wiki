---
layout: "default"
title: "Estabilidade — Redução à forma de Hessenberg"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A2.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo", "Arthur Rabello Oliveira"]
ano_original: 2025
ordem_na_trilha: 36
---

[Álgebra Linear Numérica](../../index.md) · [Redução à forma de Hessenberg](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-36"></a>

# Estabilidade

Assim como o algoritmo de Householder, para a fatoração QR, esse algoritmo é **backward stable**. Seja $\widetilde{H}$ a matriz de Hessenberg computada pelo computador ideal, $\widetilde{Q}$ seja a matriz exatamente unitária que reflete os vetores $v_{k}$, então o resultado a seguir pode ser demonstrado:

<a id="householder-stability-and-precision"></a>

**Teorema**

Deixe a redução de Hessenberg $A = QTQ^{\ast}$ de uma matriz $A$ ser computada pelo [\[householder-reduction-to-hessenberg-form\]](../uma-boa-ideia/index.md#householder-reduction-to-hessenberg-form) em um computador ideal e sejam as matrizes $\widetilde{Q}$ e $\widetilde{H}$ definidas como falamos anteriormente, então: $$\widetilde{Q}\widetilde{H}{\widetilde{Q}}^{\ast} = A + \delta A,\text{ tal que  }\frac{\|\delta A\|}{\| A\|} = O\left( \varepsilon_{\text{machine}} \right)$$ para algum $\delta A \in {\mathbb{C}}^{m \times m}$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/algebra-linear-numerica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a2.md#apresentacao-original)

- Anterior: [Hermitiana](../hermitiana/index.md)
- Próximo: [Quociente de Rayleigh e Iteração Inversa](../../quociente-de-rayleigh-e-iteracao-inversa/index.md)
