---
layout: "default"
title: "Teste $t$ pareado — Testes $t$"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 31
---

[Inferência Estatística](../../index.md) · [Testes $t$](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-31"></a>

# Teste $t$ pareado

Em vários experimentos, podemos desejar comparar a mesma variável em condições distintas na mesma amostra, então estaríamos interessados em comparar qual condição possui maior média. Nesses casos é comum fazer a subtração entre os valores de cada condição e tratar como uma variável aleatória normal

**Exemplo:**

O **National Transportation Safety Board** coleta dados de testes de colisão referentes à quantidade e à localização dos danos em bonecos (**dummies**) colocados nos carros testados. Em uma série de testes, um boneco foi colocado no banco do motorista e outro no banco do passageiro dianteiro de cada carro. Uma das variáveis medidas foi o grau de lesão na cabeça de cada boneco. Entre outros aspectos, há interesse em saber se, e/ou em que medida, a quantidade de lesão na cabeça difere entre o banco do motorista e o banco do passageiro.

Sejam $\left( X_{1},\ldots,X_{n} \right)$ as diferenças entre os logaritmos das medidas de lesão na cabeça do lado do motorista e do lado do passageiro. Podemos modelar $\left( X_{1},\ldots,X_{n} \right)$ como uma amostra aleatória de uma distribuição normal com média ( $\mu$ ) e variância ( $\sigma^{2}$ ). Suponha que desejamos testar a hipótese nula ( $H_{0}:\mu \leq 0$ ) contra a alternativa ( $H_{1}:\mu > 0$ ), ao nível de significância ( $\alpha_{0} = 0.01$ ).

Há $n = 164$ carros. O teste consiste em rejeitar ( $H_{0}$ ) se $$U \geq T_{163}^{- 1}(0.99) = 2.35.$$

A média das diferenças é ${\overline{x}}_{n} = 0.2199$. O valor de $\sigma'$ é $0.5342$. A estatística $U$ é então igual a $5.271$. Esse valor é maior que $2.35$, e a hipótese nula seria rejeitada ao nível de $0.01$. De fato, o **p-valor** é menor que $1.0 \cdot 10^{- 6}$.

Suponha também que estamos interessados na função poder sob $H_{1}$ do teste de nível $0.01$. Suponha que a diferença média entre os logaritmos das lesões na cabeça do lado do motorista e do lado do passageiro seja $\frac{\sigma}{4}$. Então, o parâmetro de não centralidade é $\frac{(164)^{\frac{1}{2}}}{4} = 3.20$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Propriedades dos testes $t$](../propriedades-dos-testes-t/index.md)
- Próximo: [Testando uma alternativa bilateral](../testando-uma-alternativa-bilateral/index.md)
