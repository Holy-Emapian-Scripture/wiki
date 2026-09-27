---
layout: "default"
title: "Cutoffs — Correlação de Graus"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A2.md"
trilha: "../../../../trilhas/ciencia-de-redes/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 4
---

[Ciência de Redes](../../index.md) · [Correlação de Graus](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-4"></a>

# Cutoffs

A gente até agora ta assumindo que as redes analisadas são simples, ou seja, entre dois nós, só pode existir **no máximo** uma aresta. Porém, em algumas redes, quando calculamos o número esperado de arestas entre nós $${\mathbb{E}}_{kk'} = e_{kk'}{\mathbb{E}}\lbrack K\rbrack N$$

esse valor é **maior que $1$**. Então como fazemos para achar o valor de $k$ que faz com que esse valor seja $> 1$?

Primeiro, vamos definir $$r_{kk'} = \frac{E_{kk'}}{m_{kk'}}$$

onde $E_{kk'}$ é o número de arestas entre todos os nós de grau $k$ e de $k'$ e $m_{kk'} = \min\left\{ kN_{k},k'N_{k'},N_{k}N_{k'} \right\}$ é a maior quantidade **possível** de restas que ligam nós de grau $k$ e $k'$. Vou explicar o porquê dessa fórmula para $m_{kk'}$

- Cada nó com grau $k$ só pode se ligar a **no máximo** $k$ nós de grau $k'$, então:

$$E_{kk'} \leq kN_{k}$$

- O mesmo argumento vale para os nós de grau $k'$

$$E_{kk'} \leq k'N_{k'}$$

- Eu também não consigo ligar mais que o número máximo disponível de pares entre os dois grupos de graus

$$E_{kk'} \leq N_{k}N_{k'}$$

Ou seja, temos que $r_{kk'} \leq 1\ \forall k,k'$. Só que como mencionei anteriormente, por conta do valor esperado “não-esperado” de mais que uma aresta entre dois nós, pode ocorrer que $r_{kk'} > 1$, então queremos encontrar $k_{s}$ tal que: $$r_{k_{s}k_{s}} = 1$$

Mas antes de achar $k_{s}$, vamos reescrever $r_{kk'}$ de outra forma e fazer uma análise. Perceba que, quando $k > Np(k')$ ou $k' > Np(k)$, os efeitos das arestas múltiplas aparecem, transformando a expressão em: $$r_{kk'} = \frac{{\mathbb{E}}_{kk'}}{m_{kk'}} = \frac{{\mathbb{E}}\lbrack K\rbrack e_{kk'}}{Np(k)p(k')}$$

Para redes livre-de-escala, as condições são satisfeitas para $k,k' > \left( a\vert V\vert  \right)^{\frac{1}{\gamma + 1}}$ onde $a$ depende de $p(k)$. Só que esse valor é abaixo do cutoff natural, de forma que temos CERTEZA de que, se $k$ e $k'$ são maiores que isso, não podemos garantir que o valor esperado dos links será menor que 1. Olhando o caso específico das redes neutras, sabemos que: $$e_{kk'} = \frac{kk'p(k)p(k')}{{\mathbb{E}}\lbrack K\rbrack^{2}}$$

Logo $r_{kk'}$ vira: $$r_{kk'} = \frac{kk'}{{\mathbb{E}}\lbrack K\rbrack N}$$

Ou seja, chegamos que $k_{s} \propto \left( {\mathbb{E}}\lbrack K\rbrack N \right)^{\frac{1}{2}}$

Tendo isso em mente, conseguimos dividir as **redes livre-de-escala** em dois regimes ao compararmos $k_{\text{max}}$ e $k_{s}$ (Lembrando: $k_{\max} \propto N^{\frac{1}{\gamma - 1}}$)

- **Sem cutoff estrutural:** Para redes aleatórias e livre-de-escala com $\gamma \geq 3$, o expoente de $k_{\max} \leq \frac{1}{2} \Rightarrow k_{\max} \leq k_{s}$, logo os valores esperados dos links entre nós será **sempre** menor ou igual a 1

- **Dissassortividade estrutural:** Para redes livre-de-escala com $\gamma < 3$, temos $- \frac{1}{1 - \gamma} > \frac{1}{2}$, logo $k_{s}$ pode ser menor que $k_{\text{max}}$, logo, há nós entre $k_{s}$ e $k_{\max}$ que podem ter $E_{kk'} > 1$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/ciencia-de-redes/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a2.md#apresentacao-original)

- Anterior: [Average Next Neighbour Degree](../average-next-neighbour-degree/index.md)
- Próximo: [Percolação e Robustez](../../percolacao-e-robustez/index.md)
