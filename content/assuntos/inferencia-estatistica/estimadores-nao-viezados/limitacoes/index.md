---
layout: "default"
title: "Limitações — Estimadores não-viezados"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 18
---

[Inferência Estatística](../../index.md) · [Estimadores não-viezados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-18"></a>

# Limitações

- Muitas vezes os estimadores não-viezados possuem uma variância maior que os estimadores viezados, um bom exemplo é que ${\mathbb{V}}\left\lbrack {\hat{\sigma}}^{2} \right\rbrack \geq {\mathbb{V}}\left\lbrack {\hat{\sigma}}_{0}^{2} \right\rbrack$

- Não há garantia que estimadores não-viezados existam em toda situação. Um exemplo é que, se $X_{1},\ldots,X_{n} \sim \text{ Bern}(p)$, não existe estimador **não-viezado** de $\sqrt{p}$

- Estimadores inapropriados, mesmo sendo não-viezados. Por exemplo, se eu tenho uma sequência de bernoullis, e tentar estimar $p$ pela quantidade de erros até o primeiro sucesso $X$ (Geométrica). O estimador não viezado seria: $$\delta(X) = \begin{cases} 1\text{ se }X = 0 \\ 0\text{ se }X = 1 \end{cases}$$

- Os estimadores podem ignorar informações. Se você for medir a votlagem de um sistema com um multímetro, e ele retornar $2.5$, então podemos pensar que $\theta$ é $2.5$, mas e se o multímetro arredonda tudo que é maior que $3$ para $3$? Isso muda completamente a distribuição da informação

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Estimador não-viezado da Variância](../estimador-nao-viezado-da-variancia/index.md)
- Próximo: [Análise e Teste de Hipóteses](../../analise-e-teste-de-hipoteses/index.md)
