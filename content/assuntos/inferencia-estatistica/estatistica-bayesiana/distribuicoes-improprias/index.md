---
layout: "default"
title: "Distribuições Impróprias — Estatística Bayesiana"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 7
---

[Inferência Estatística](../../index.md) · [Estatística Bayesiana](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# Distribuições Impróprias

**Definição: Distribuição Imprópria**

Seja $\xi:C \rightarrow {\mathbb{R}}$ uma função não-negativa cujo domínio inclui o espaço paramétrico ($\Omega \subset C$) de um modelo estatístico. Suponha também que: $$\int_{C}\xi(\theta)d\theta = \infty$$ Se nós imaginarmos que $\xi$ é a f.d.p à priori de $\theta$, então $\xi$ é uma **distribuição imprória** de $\theta$

Um bom exemplo é utilizar a distribuição **beta** assumindo que $\alpha = \beta = 0$. Mesmo que isso viole a condição da distribuição beta, o resultado da posteriori ainda sim é uma distribuição beta. Porém, existem diversos métodos para se escolher uma distribuição imprópria para $\theta$. O mais comum é se utilizar de uma família de conjugados para o modelo estatístico, e forma a adaptarmos seus parâmetros para obter uma distribuição imprópria.

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Distribuições à Priori Conjugadas](../distribuicoes-a-priori-conjugadas/index.md)
- Próximo: [Estimadores de Bayes](../../estimadores-de-bayes/index.md)
