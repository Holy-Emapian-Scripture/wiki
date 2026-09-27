---
layout: "default"
title: "Average Next Neighbour Degree — Correlação de Graus"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A2.md"
trilha: "../../../../trilhas/ciencia-de-redes/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 3
---

[Ciência de Redes](../../index.md) · [Correlação de Graus](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-3"></a>

# Average Next Neighbour Degree

É interessante fazer o gráfico de uma matriz de covariância, porém, por ela perder essas informações antes mencionadas, as vezes ela pode ser ineficiente ou ser de difícil leitura se houver muitos vértices, então criamos a seguinte definição:

**Definição: Average Next Neighbour Degree**

Seja $G(V,E)$ uma rede, $A$ a matriz de adjacência da mesma e $v_{i} \in V$, então: $$k_{\text{nn }}\left( v_{i} \right) ≔ \frac{1}{\delta(v_{i})}\sum_{j = 1}^{\vert V\vert }A_{ij}\delta(v_{j})$$

Essa definição é o $k_{\text{nn}}$ para um vértice específico, mas e se quisermos o valor médio dessa medida para nós de grau $k$? $$k_{\text{nn }}(k) = {\mathbb{E}}\left\lbrack B\vert A = k \right\rbrack = \sum_{k'}k'{\mathbb{P}}(B = k'\vert A = k)$$

Podemos ver o que acontece com essa medida quando $A$ e $B$ são independentes, logo, analisar o caso das **redes neutras** $$k_{\text{nn }} = \sum_{k'}k'{\mathbb{P}}(B = k') = \sum_{k'}k'\frac{k'p(k')}{\mathbb{E}}\lbrack K\rbrack = {\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack$$

Perceba que, quando consideramos o caso das redes neutras, **a média dos vizinhos de um nó não depende em quantos nós ele tem ou de informações sobre como o nó se relaciona com os outros, mas única e exclusivamente de características globais da rede**. A mesma lógica vale para as redes assortativas e desassortativas:

![](../../assets/knn-predictions.png)

- **Assortativas:** A medida tende a crescer conforme aumentamos os valores de $k$ já que quanto maior o grau, maior a probabilidade de os graus se interligarem

- **Desassortativas:** Nós de grau menor tendem a interligar com nós de grau maior, o que acaba por fazer com que as probabilidades sejam altas em valores de $k$ muito pequenos, isso faz com que conforme aumentamos o $k$, o valor da medida diminua

O livro aponta que, de acordo com o gráfico mostrado anteriormente, que podemos aproximar a medida do $k_{\text{nn}}$ como: $$k_{\text{nn }}(k) = \beta k^{\mu}$$

de forma que:

- $\mu > 0 \Rightarrow$ Rede assortativa

- $\mu \approx 0 \Rightarrow$ Rede neutra

- $\mu < 0 \Rightarrow$ Rede desassortativa

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/ciencia-de-redes/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a2.md#apresentacao-original)

- Anterior: [Descobrindo os Critérios](../descobrindo-os-criterios/index.md)
- Próximo: [Cutoffs](../cutoffs/index.md)
