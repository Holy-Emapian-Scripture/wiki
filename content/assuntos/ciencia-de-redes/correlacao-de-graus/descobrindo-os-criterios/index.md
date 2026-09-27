---
layout: "default"
title: "Descobrindo os Critérios — Correlação de Graus"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A2.md"
trilha: "../../../../trilhas/ciencia-de-redes/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 2
---

[Ciência de Redes](../../index.md) · [Correlação de Graus](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-2"></a>

# Descobrindo os Critérios

Dado uma rede $G(V,E)$, vamos supor que conhecemos a distribuição dos graus dessa rede (${\mathbb{P}}(\delta(v_{i}) = k) = p(k)$ para simplificação de notação), queremos ver se o grau do nó tem alguma influência em como eles se ligam. Então temos que ver a probabilidade de que um nó de grau $k'$ se ligue com um de grau $k$, ou seja: $${\mathbb{P}}(\left\{ v_{i},v_{j} \right\} \in E~\vert ~\delta(v_{i}) = k,\delta(v_{j}) = k') = p\left( \left\{ k,k' \right\} \in E \right)$$ Vamos escrever dessa forma para simplificar notação. Vamos ter que: $$p\left( \left\{ k,k' \right\} \in E \right) = \frac{kk'}{2\vert E\vert }$$ Onde $k'/2L$ é a probabilidade do meu nó com grau $k$ se ligar com um nó de grau $k'$ e eu multiplico por $k$ pois meu nó possui $k$ arestas ligadas a ele. Essa probabilidade indica que nós com graus maiores tem mais probabilidade de se ligar com outros nós de grau grande

**Definição: Matriz de Correlação por Grau**

A matriz de correlação por grau é a matriz que a entrada $e_{ij}$ é a probabilidade de encontrar nós de graus $i$ e $j$ nas pontas de uma aresta selecionada aleatoriamente

Essa matriz nos tráz informações diretas da relação **linear** entre os nós. Podemos dividir e classificar as redes de 3 formas de acordo com a relação entre seus graus

- **Rede Assortativa:** Nós com graus parecidos intelrigam entre si

- **Redes Neutras:** Os nós não apresentam um padrão para intelirgarem entre si

- **Redes Desassortativas:** Nós com graus maiores se ligam com graus menores e vice-versa

Podemos então avalisar a matriz de covariância ou a correlação entre os dados. Porém a relação entre esses pontos pode não ser linear, o que pode dar falsas impressões sobre a correlação

![Matriz de covariância de graus com 3 redes. A primeira é assortativa, a segunda é neutra e a última é desassortativa](../../assets/degrees-correlation.png)

*Figura 1. Matriz de covariância de graus com 3 redes. A primeira é assortativa, a segunda é neutra e a última é desassortativa*

A matriz de correlação acaba por representar uma distribuição conjunta em $i$ e $j$ de forma que: $$\sum_{i,j}e_{ij} = 1$$

então definindo um pouco melhor essa probabilidade, defina $K$ como a bariável aleatória que representa o grau de um nó selecionado aleatoriamente. Seja também $\left\{ v_{i},v_{j} \right\} \in E$ uma aresta escolhida aleatoriamente dentre todas as do conjunto $E$. Para simplificar notações, também definimos $A = \delta(v_{i})$ e $B = \delta(v_{j})$. Então vamos ter que: $$e_{ij} = {\mathbb{P}}(A = i,B = j) = {\mathbb{P}}(A = i\vert B = j) \cdot {\mathbb{P}}(B = j) = {\mathbb{P}}(B = j\vert A = i) \cdot {\mathbb{P}}(A = i)$$

vamos então calcular cada um desses termos (Até onde for possível). Primeiro vamos calcular ${\mathbb{P}}(A = i)$ $${\mathbb{P}}(A = i) = \frac{iN_{i}}{2\vert E\vert } \times \frac{\frac{1}{N}}{\frac{1}{N}} = \frac{ip(i)}{{\mathbb{E}}\lbrack K\rbrack}$$

onde $N_{i}$ é a quantidade de nós com grau $i$ e eu multiplico por $i$ pois eu posso escolher qualquer uma das $i$ arestas presentes no nó que eu gostaria que fosse escolhido (O de grau $i$). E divido isso pela quantidade total de nós. Eu posso ainda, dividir o termo de cima e o de baixo por $N$, obtendo então a expressão na direita

Se os eventos $A$ e $B$ **não são independentes**, seria necessário saber a distribuição entre eles dois para calcular ${\mathbb{P}}(A = i\vert B = j)$. Porém, se $A$ e $B$ são independentes, então ${\mathbb{P}}(A = i\vert B = j) = {\mathbb{P}}(A = i) \cdot {\mathbb{P}}(B = j)$, então, no caso de $A$ e $B$ independentes, obtemos: $${\mathbb{P}}(A = i\vert B = j) = {\mathbb{P}}(A = i) \cdot {\mathbb{P}}(B = j) = \frac{ip(i)jp(j)}{\left( {\mathbb{E}}\lbrack K\rbrack \right)^{2}}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/ciencia-de-redes/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a2.md#apresentacao-original)

- Anterior: [Correlação de Graus](../index.md)
- Próximo: [Average Next Neighbour Degree](../average-next-neighbour-degree/index.md)
