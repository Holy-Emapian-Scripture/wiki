---
layout: "default"
title: "Critério de Molloy-Reed — Percolação e Robustez"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A2.md"
trilha: "../../../../trilhas/ciencia-de-redes/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 8
---

[Ciência de Redes](../../index.md) · [Percolação e Robustez](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-8"></a>

# Critério de Molloy-Reed

**Teorema: Critério de Molloy-Reed**

Dado que $K$ é a variável aleatória que representa o grau de um nó selecionado aleatoriamente dentro de uma rede $G(V,E)$. Para que uma componente gigante exista dentro dessa rede, ela deve satisfazer: $${\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack \geq 2$$

**Demonstração**

Para que minha rede tenha uma componente gigante, um nó **da componente** deve ter grau médio maior ou igual a $2$, já que caso contrário, quer dizer que muitos nós possuem apenas uma ou menos conexões. Defina ${\mathbb{P}}(\delta(v_{i}) = k_{i}\vert v_{i} \leftarrow > v_{j})$ como a probabilidade de que $v_{i}$ tem grau $k$ dado que ele se liga com $j$ **e $j$ está na componente gigante**. Por questões de simplificação de notação, chamemos a probabilidade antes definida como ${\mathbb{P}}(k_{i}\vert i \leftarrow > j)$. Temos que: $${\mathbb{E}}\left\lbrack K = k_{i}\vert i \leftarrow > j \right\rbrack = \sum_{k_{i}}k_{i}{\mathbb{P}}(k_{i}\vert i \leftarrow > j) \geq 2$$ Vamos calcular alguns termos. Sabemos que: $${\mathbb{P}}(k_{i}\vert i \leftarrow > j) = \frac{{\mathbb{P}}(i \leftarrow > j\vert k_{i}) \cdot {\mathbb{P}}(k_{i})}{{\mathbb{P}}(i \leftarrow > j)}$$ E também temos que: $${\mathbb{P}}(i \leftarrow > j) = \frac{\vert E\vert }{\begin{pmatrix} \vert V\vert  \\ 2 \end{pmatrix}} = {\mathbb{E}}\frac{\lbrack K\rbrack}{\vert V\vert  - 1}$$ Além de que: $${\mathbb{P}}(i \leftarrow > j\vert k_{i}) = \frac{k_{i}}{\vert V\vert  - 1}$$ Então, substituindo, vamos ter: $${\mathbb{E}}\left\lbrack K = k_{i}\vert i \leftarrow > j \right\rbrack = \sum_{k_{i}}k_{i}\frac{k_{i}p\left( k_{i} \right)}{{\mathbb{E}}\lbrack K\rbrack} = {\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack \geq 2$$

Olhando o caso específico de **redes aleatórias**, nós vamos obter que: $${\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack \geq 2 \Leftrightarrow {\mathbb{E}}\lbrack K\rbrack\frac{1 + {\mathbb{E}}\lbrack K\rbrack}{\mathbb{E}}\lbrack K\rbrack \geq 2 \Leftrightarrow {\mathbb{E}}\lbrack K\rbrack \geq 1$$

O que coincide com os resultados vistos no primeiro resumo

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/ciencia-de-redes/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a2.md#apresentacao-original)

- Anterior: [Robustez](../robustez/index.md)
- Próximo: [Limite Crítico](../limite-critico/index.md)
