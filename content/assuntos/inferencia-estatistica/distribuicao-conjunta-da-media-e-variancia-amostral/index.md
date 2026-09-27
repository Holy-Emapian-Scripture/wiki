---
layout: "default"
title: "Distribuição Conjunta da Média e Variância Amostral"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 4
---

[Inferência Estatística](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Distribuição Conjunta da Média e Variância Amostral

------------------------------------------------------------------------

Vamos supor que estamos fazendo um experimento e coletamos amostras de uma distribuição normal com média $\mu$ e variância $\sigma^{2}$, porém, não sabemos nenhum dos dois, então queremos estimá-los! Podemos escolher vários estimadores, por exemplo, o EVM: $$\hat{\mu} = \frac{1}{n}\sum_{i = 1}^{n}X_{i}\text{\quad\quad}\hat{\sigma^{2}} = \frac{1}{n}\sum_{i = 1}^{n}\left( X_{i} - \hat{\mu} \right)^{2}$$ Porém, como vimos na primeira parte, eles são variáveis aleatórias com distribuições próprias, então podemos utilizar técnicas para saber o quão bem eles aproximam $\mu$ e $\sigma^{2}$, mas antes, temos que descobrir suas distribuições amostrais! Acontece que a distribuição de $\hat{\mu}$ depende de $\sigma^{2}$, porém, veremos que a distribuição conjunta de $\hat{\mu}$ e $\hat{\sigma^{2}}$ nos permite inferir $\mu$ sem referenciar $\sigma$

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Independência da Média e Variância Amostrais](independencia-da-media-e-variancia-amostrais/index.md)

## Percurso de estudo

[Trilha: A2](../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Propriedades](../distribuicao-chi-quadrado/propriedades/index.md)
- Próximo: [Independência da Média e Variância Amostrais](independencia-da-media-e-variancia-amostrais/index.md)
