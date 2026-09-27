---
layout: "default"
title: "O Papél do Expoente do Grau — Redes Livres de Escala"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A1.md"
trilha: "../../../../trilhas/ciencia-de-redes/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 19
---

[Ciência de Redes](../../index.md) · [Redes Livres de Escala](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-28"></a>

# O Papél do Expoente do Grau

Se pararmos para analisar redes na vida real, vamos perceber que $\gamma$ varia de rede para rede, isso nos leva a intuitivamente querer saber como $\gamma$ influencia nas redes reais. Na maioria das redes reais, temos que $\gamma > 2$, o que também gera a pergunta: Por quê?

![Regimes de $\gamma$](../../assets/gamma-regimes.png)

*Figura 10. Regimes de $\gamma$*

<a id="secao-29"></a>

## Regime Anômalo ($\gamma \leq 2$)

Nesse regime, o expoente $1/(\gamma - 1)$ é maior que $1$, ou seja, o número de links conectados ao maior hub cresce **mais rápido que o próprio número de links em si**, além de que ${\mathbb{E}}\lbrack K\rbrack$, sendo K a variável aleatória do grau dos nós, também diverge. O que isso indica? Isso mostra que, redes livre de escala **sem links múltiplos**, ou seja, a existência de várias arestas que ligam os mesmos dois nós, **não podem existir**

<a id="secao-30"></a>

## Regime Livre de Escala ($2 < \gamma < 3$)

Aqui, o primeiro momento converge enquanto o segundo diverge, o que faz a gente cair na situação que ja comentei anteriormente de os graus serem arbitrariamente grandes, porém, que a distância entre dois nós cresce **muito** devagar, os já mencionado **Ultra Small Worlds**

<a id="secao-31"></a>

## Regime de Rede Aleatória ($\gamma > 3$)

Como indicado relação [\[average-path-distance-ultra-small-networks\]](../propriedade-ultra-small/index.md#average-path-distance-ultra-small-networks), e por motivos práticos também, nesse regime, as propriedades das redes livres de escala não são muito diferentes das propriedades das redes aleatórias. Isso pois, como ja comentado, o grau dos nós decaem rapido o suficiente para que os hubs, mesmo os maiores, não sejam tão numerosos ao ponto de que afetem muito a distância média entre os nós

Na prática, costuma-se observar que, para que os hubs venham a influenciar na distância média, $k_{\max}$ tem que ser, pelo menos, umas $10^{2}$, $10^{3}$ vezes maior que $k_{\min}$. Na prática a gente pode reformular a relação [\[biggest-hub-relation\]](../centros/index.md#biggest-hub-relation) como: $$N = \left( \frac{k_{\max}}{k_{\min}} \right)^{\gamma - 1}$$

E isso daria uma relação de quantos nós precisamos para que começássemos a registrar a propriedade da rede livre de escala. Por exemplo, vamos supor que queremos saber quantos nós precisamos para começar a ver essa propriedade em redes de $\gamma = 5$ (E, por exemplo, $k_{\min} = 1$ e $k_{\max} = 10^{2}$), então deveríamos ter $N > 10^{8}$, e são poucas as redes, na prática, com um tamanho absurdo desses!

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Anterior: [Propriedade *Ultra Small*](../propriedade-ultra-small/index.md)
- Próximo: [Modelo Biaconi-Barabási](../../modelo-biaconi-barabasi/index.md)
