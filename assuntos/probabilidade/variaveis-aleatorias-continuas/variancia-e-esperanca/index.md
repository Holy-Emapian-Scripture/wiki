---
layout: "default"
title: "Variância e Esperança — Variáveis Aleatórias Contínuas"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 5
---

[Probabilidade](../../index.md) · [Variáveis Aleatórias Contínuas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Variância e Esperança

<a id="definicao_esperanca"></a>

**Definição**

(Esperança)  
Dada uma v.a contínua $X$ com PDF $f_{X}(\varphi)$, a esperança de $X$ é dada por:

$$E(X) = \int_{- \infty}^{\infty}\varphi f_{X}(\varphi)d\varphi$$

**Definição**

(Variância, Desvio-Padrão)  
A variância de uma v.a contínua $X$ com PDF $f_{X}(\varphi)$ e esperança $\mu = E(X)$ é dada por:

$$V(X) = E\lbrack(X - {E(X)}^{2}\rbrack = \int_{- \infty}^{\infty}\lbrack\varphi - \mu\rbrack^{2}f_{X}(\varphi)d\varphi$$

O desvio padrão é:

$$\sigma(X) = \sqrt{V(X)}$$

<a id="definicao_variancia_desviopadrao"></a>

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [LOTUS (Law of The Unconscious Statistician)](../lotus-law-of-the-unconscious-statistician/index.md)
- Próximo: [Propriedades da Esperança e Variância](../propriedades-da-esperanca-e-variancia/index.md)
