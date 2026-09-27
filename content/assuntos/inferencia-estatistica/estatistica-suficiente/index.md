---
layout: "default"
title: "Estatística Suficiente"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 18
---

[Inferência Estatística](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-18"></a>

# Estatística Suficiente

------------------------------------------------------------------------

A gente viu alguns métodos para fazer estimativas que consistiam no uso de distribuições priori e posteriori. Porém, há alguns métodos que estimam dos parâmetros apenas utilizando de distribuições condicionais de funções dos dados.

A gente viu antes que nem sempre os métodos de estimativa que a gente tem vão ser interessantes ou vão ser boas estimativas (Para melhor detalhes, pode conferir os exemplos do livro). Nesses casos, precisamos desenvolver métodos novos de estimativa para nossos parâmetros.

Imagina que nós temos uma amostra elatória $X_{1},\ldots,X_{n}$ e temos dois estatísticos, o $A$ e o $B$. Vamos supor que $A$ tem acesso a todos os valores de $X_{1},\ldots,X_{n}$, enquanto $B$ só pode saber sobre uma estimativa específica $T = r\left( X_{1},\ldots,X_{n} \right)$. Qual deles vai poder fazer melhores estimativas para $\theta$? Com certeza o mano estatístico $A$! Porém, entretudo, todavia, em alguns problemas, o estatístico $B$ pode fazer estimativas tão bem quanto o estatístico $A$, pois a função $T$ pode, de alguma forma, conter todas as informações relevantes e necessárias para que meu problema possa ser solucionado! Quando $T$ tem essa característica, chamamos ela de **estatística suficiente**

**Definição: Estatística Suficiente**

Seja $X_{1},\ldots,X_{n}$ uma amostra aleatória de uma distribuição indexada pelo parâmetro $\theta$ e $T$ uma estatística. Suponha também que, para todo $\theta$ e todo valor possível $t$ de $T$, a distribuição conjunta de $X_{1},\ldots,X_{n}\vert T = t,\theta$ depende apenas de $t$ e não de $\theta$. Ou seja, para cada $t$, a distribuição conjunta de $X_{1},\ldots,X_{n}\vert T = t,\theta$ é a mesma **para todo** $\theta$. Então dizemos que $T$ é uma **estatística suficiente para o parâmetro $\theta$**

A principal característica que separa estatísticas suficientes de não-suficientes é a dependência no valor de $\theta$. O livro traz um processo chamado **randomização auxiliar**, que consiste em simular variáveis $X'_{1},\ldots,X'_{n}$ com mesma distribuição que $X_{1},\ldots,X_{n}\vert \theta$, porém, essas variáveis simuladas são feitas baseando-se única e exclusivamente numa estatística suficiente $T$. Se a estatística $T$ não fosse suficiente, não conseguiriamos nem fazer a randomização auxiliar, pois necessariamente precisariamos saber qual seria o valor de $\theta$

Com esse processo fica fácil de ver agora o porquê de o estatístico $B$ conseguir se sair tão bem quanto o estatístico $A$. Se $A$ vai utilizar de um estimador $\delta(X_{1},\ldots,X_{n})$ para estimar $\theta$, se $B$ tiver acesso a estatística suficiente $T$, então ele pode criar variáveis auxiliares $X'_{1},\ldots,X'_{n}$ que tem mesma distribuição que as originais, então de $B$ utilizar o estimador $\delta$ porém aplicando as suas variáveis $\delta(X'_{1},\ldots,X'_{n})$, então a distribuição do estimador de $A$ é a mesma distribuição do estimador de $B$

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Critério de Fatoração](criterio-de-fatoracao/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Método dos Momentos](../metodo-dos-momentos/index.md)
- Próximo: [Critério de Fatoração](criterio-de-fatoracao/index.md)
