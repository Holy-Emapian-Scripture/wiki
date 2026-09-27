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


<a id="dinamica"></a>
<a id="secao-33"></a>

## Dinâmica

Imagine o vértice $v_{i}$ fixamente, ele está presente desde o começo (No grafo inicial). A cada passo $t$ um novo nó é inserido. Vamos então definir o grau do nosso vértice $v_{i}$ em função do tempo: $$k_{i} = \delta_{t}\left( v_{i} \right) ≔ \text{ Grau do vértice }v_{i}\text{ no momento }t$$

Temos que a variação de $k_{i}$ em relação ao tempo é: $$\frac{dk_{i}}{dt} = m\frac{\eta_{i}k_{i}}{\sum_{j}\eta_{j}k_{j}}$$

Isso ocorre pois, a cada unidade de tempo, eu vou adicionar $m$ links no meu grafo. Então minha mudança média no grau do meu nó é $m$ (Número de nós adicionados) ponderado pela probabilidade de cada link se ligar a $v_{i}$ que é como definimos antes

A gente vai assumir que o tempo de evolução de $\delta(v_{i})$ segue uma lei de potência dependente da aptidão (Ou seja, cresce exponencialmente em relação a $\eta_{i}$). Então: $$k\left( t,t_{i},\eta_{i} \right) = m\left( \frac{t}{t_{i}} \right)^{\beta(\eta_{i})}$$

Onde $t$ é o momento atual e $t_{i}$ é o momento de chegada de $v_{i}$ na rede. Fazendo alguns cálculos especificados no livro do Barabási, chegamos que: $$\beta(\eta) = \frac{\eta}{C}$$ de forma que: $$C = \int\rho(\eta)\frac{\eta}{1 - \beta(\eta)}d\eta$$

<a id="distribuicao-dos-graus"></a>
<a id="secao-34"></a>

## Distribuição dos Graus

Também involve cálculos mais complicados, então vou apenas mostrar a fórmula. Quando houver tempo, colocarei os cálculos nesse resumo: $$p_{k} \approx C\int\frac{\rho(\eta)}{\eta}\left( \frac{m}{k} \right)^{\frac{C}{\eta} + 1}d\eta$$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Anterior: [O Papél do Expoente do Grau](../redes-livres-de-escala/index.md#o-papel-do-expoente-do-grau)
- Próximo: [Distribuição dos Graus](#distribuicao-dos-graus)
