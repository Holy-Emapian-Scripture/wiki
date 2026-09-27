---
layout: "default"
title: "Propriedades da Esperança e Variância — Variáveis Aleatórias Contínuas"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 6
---

[Probabilidade](../../index.md) · [Variáveis Aleatórias Contínuas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao_propriedades_esperanca_variancia"></a>

# Propriedades da Esperança e Variância

Dadas v.a’s contínuas $X,Y$ com PDF $f_{X}(\varphi),f_{Y}(\varphi)$ e $a,b \in {\mathbb{R}}$, temos:

<a id="propriedade_esperanca_variancia"></a>

**Propriedade**

$$\begin{array}{r} E(aX + b) = aE(X) + b \\ E(X + Y) = E(X) + E(Y) \\ V(aX + b) = a^{2}V(X) \end{array}$$

E caso $X,Y$ sejam independentes:

$$\begin{array}{r} E(XY) = E(X)E(Y) \\ V(X + Y) = V(X) + V(Y) \end{array}$$

**Propriedade**

Podemos calcular a variância de $X$ usando a esperança:

$$V(X) = E\left( X^{2} \right) - {E(X)}^{2}$$

<a id="propriedade_varianca_via_esperanca"></a>

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [Variância e Esperança](../variancia-e-esperanca/index.md)
- Próximo: [Distribuições Contínuas](../../distribuicoes-continuas/index.md)
