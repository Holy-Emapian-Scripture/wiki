---
layout: "default"
title: "Mundos pequenos — Redes Aleatórias"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A1.md"
trilha: "../../../../trilhas/ciencia-de-redes/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 7
---

[Ciência de Redes](../../index.md) · [Redes Aleatórias](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-11"></a>

# Mundos pequenos

Mundos pequenos (Small worlds) são grafos em que, independente da quantidade de vértices, a distância entre dois nós aleatórios costuma ser muito pequeno. Um exemplo é um modelo que cada nó representa todas as pessoas do mundo e as arestas indicam se elas já interagiram e se conhecem ou não (Impressionantemente), tanto que existe a teoria dos 6 graus de distância entre as pessoas

[*Vídeo sobre o assunto (Clique aqui)*](https://youtu.be/TcxZSmzPw8k?si=jXPDJE_SWwNys4YM)

E se quisermos ter uma noção de o quão **não-relacionadas** duas pessoas são em uma rede social? Podemos calcular sua distância, obviamente, mas alguns algoritmos ficam computacionalmente inviáveis. Podemos então estimar uma distância média entre dois nós selecionados aleatoriamente no grafo.

Tendo uma rede $G(V,E)$ com grau médio $\hat{k} = {\mathbb{E}}\lbrack K\rbrack$, é intuitivo pensar que cada nó tem, em média: $$\begin{aligned} & \hat{k}\text{ nós a }1\text{ unidade de distância } \\ & {\hat{k}}^{2}\text{ nós a }2\text{ unidades de distância } \\ & \vdots \\ & {\hat{k}}^{d}\text{ nós a }d\text{ unidades de distância } \end{aligned}$$ Então é plausível dizer que a quantidade média de nós presentes até uma distância $d$ de um nó qualquer é expresso como: $$N(d) = \sum_{i = 0}^{d}{\hat{k}}^{i} = \frac{{\hat{k}}^{d + 1} - 1}{\hat{k} - 1}$$

Sabemos que esse valor não pode ter valores arbitrários, ele não passa de $\vert V\vert  = N$, então podemos encontrar o grau médio que satisfaz esse o valor. Assim, fazemos: $$\frac{{\hat{k}}^{d + 1} - 1}{\hat{k} - 1} \approx N$$

Assumindo que $\hat{k} \gg 1$, podemos desprezar os termos $- 1$, assim vamo obter que: $$d_{\text{max }} \approx \frac{\ln(N)}{\ln(\hat{k})}$$

Que é a representação matemática do problema dos minimundos. Porém, isso também traz uma interpretação muito interessante.

Porém, aqui a gente ta vendo o **diâmetro** da rede, e nós comentamos anteriormente sobre **a distância entre dois nós aleatórios**. Impressionantemente, essa aproximação também é válida para essa ocasião. Denotando essa distância média, temos que a característica dos minimundos é: $$\hat{d} \approx \frac{\ln(N)}{\ln(\hat{k})}$$

Mas por que isso acontece? Falando de um jeito mais intuitivo, essa aproximação de $d_{\text{max}}$ costuma funcionar mais para a média do caminho entre dois nós aleatórios pois, em redes reais, o $d_{\text{max}}$ é dado por um único caminho ou pouquissimos caminhos daquele tamanho, enquanto $\hat{d}$ é ponderado em todos os nós. Além de que essa fórmula traz algumas intuições interessantes. Ela mostra que a distância média entre os nós aumenta conforme aumentamos o tamanho da rede, mesmo que não linearmente ou exponencialmente. E mostra também com o termo $1/\ln(\hat{k})$ que, quanto mais densa é minha rede, menor vai ser a distância média

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Anterior: [Distribuição de tamanhos de Cluster](../distribuicao-de-tamanhos-de-cluster/index.md)
- Próximo: [Coeficiente de Clustering](../coeficiente-de-clustering/index.md)
