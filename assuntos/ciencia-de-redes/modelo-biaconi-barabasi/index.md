---
layout: "default"
title: "Modelo Biaconi-Barabási"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A1.md"
trilha: "../../../trilhas/ciencia-de-redes/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 20
---

[Ciência de Redes](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-32"></a>

# Modelo Biaconi-Barabási

------------------------------------------------------------------------

Nesse capítulo vamos trabalhar no contexto de redes de negócios. No nosso modelo anterior, o de anexação preferencial (Ou Barabási-Albert), nós tinhamos que o primeiro nó **sempre** seria o nó com maior grau (Ou na maioria das vezes), mas os nós mais antigos sempre teriam mais links que os mais novos. Porém, em redes de negócio isso não é bem verdade. Basta olharmos a Netflix por exemplo, que chegou bem depois da Blockbuster e quem está de pé até hoje? (Mesmo que com pernas bambas). Pois é, então temos que desenvolver um modelo melhor para esse tipo de situações.

Aqui nós vamos fazer uma definição mais intuitiva e depois introduzí-la no nosso modelo matemático. Vamos chamar a **chance** de uma **empresa** criar um vínculo **permanente** com um cliente a partir de um encontro aleatório desse cliente com a empresa de **fitness** (Ou aptidão). E dependendo do contexto analisado essa fitness pode ser mensurada de formas diferentes

Se o contexto de negócios não parece muito intuitivo, basta pensar também no contexto social, onde cada pessoa vai ser amiga de outra dependendo de um encontro aleatório baseado em seus costumes, suas crenças, seus preconceitos, etc. Agora vamos definir melhor o nosso novo modelo.

Começamos com uma rede inicial $G(V,E)$, e introduzimos um novo vértice $v_{j}$ onde $v_{j}$ vai se ligar a $m$ outros vértices ($\delta(v_{j}) = m$) e meu vértice $v_{j}$ tem uma aptidão $\eta_{j}$. Essa aptidão pode ser escolhida da forma que bem entender, por enquanto, vamos assumir que ela é escolhida aleatoriamente a partir de uma distribuição $p(\eta)$ (Também assuma que todos os nós em $V$ também tem uma aptidão de antemão)

A probabilidade de que um link do meu novo nó $v_{j}$ se conecte com algum nó $v_{i} \in V$ é proporcional a sua aptidão. Podemos fazer isso definindo: $$p_{i} = {\mathbb{P}}(\left\{ v_{j},v_{i} \right\} \in E) = \frac{\eta_{i}\delta(v_{i})}{\sum_{v_{k} \in V}\eta_{k}\delta(v_{k})}$$

Perceba que a dependência de $p_{i}$ em $\delta(v_{i})$ mostra essencialmente que quanto maior o grau de $v_{i}$ maior a chance de $v_{j}$ se conectar a ele (Pense naquele amigo que conhece várias pessoas, ele costuma ser alguém agradável para que tanta gente goste dele, então você tende a gostar dele também)

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Dinâmica](dinamica/index.md)
2. [Distribuição dos Graus](distribuicao-dos-graus/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Anterior: [O Papél do Expoente do Grau](../redes-livres-de-escala/o-papel-do-expoente-do-grau/index.md)
- Próximo: [Dinâmica](dinamica/index.md)
