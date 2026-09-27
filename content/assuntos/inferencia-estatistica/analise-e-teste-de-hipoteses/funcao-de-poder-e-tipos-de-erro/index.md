---
layout: "default"
title: "Função de Poder e Tipos de Erro — Análise e Teste de Hipóteses"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 22
---

[Inferência Estatística](../../index.md) · [Análise e Teste de Hipóteses](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-22"></a>

# Função de Poder e Tipos de Erro

Seja $\delta$ um procedimento de teste como definimos antes

<a id="power-function"></a>

**Definição: Função de Poder**

A função $\pi(\theta\vert \delta)$ é chamada de **função de poder**. Se $S_{1}$ é a região crítica de $\delta$, então: $$\pi(\theta\vert \delta) = {\mathbb{P}}(\underline{X} \in S_{1}\vert \theta)\text{ ou }{\mathbb{P}}(T \in R\vert \theta)$$

Ou seja, é a probabilidade de que a minha amostra esteja na região crítica dado os meus parâmetros, ou seja, a probabilidade de que vou rejeitar $H_{0}$. A função de poder especial é aquela que: $$\begin{array}{r} \pi(\theta\vert \delta) = 0\text{\quad\quad}\forall\theta \in \Omega_{0} \\ \pi(\theta\vert \delta) = 1\text{\quad\quad}\forall\theta \in \Omega_{1} \end{array}$$

Lembrando: Para cada valor $\theta \in \Omega_{0}$, rejeitar $H_{0}$ é uma decisão **incorreta** e o mesmo para cada valor $\theta \in \Omega_{1}$ e não rejeitar $H_{0}$

**Definição: Tipos de Erro**

A decisão errônea de rejeitar uma hipótese nula **verdadeira** é de **Tipo I** (ou primeira ordem). Uma decisão errônea de **não rejeitar** uma hipótese nula **falsa** é chamada de **Tipo II** (ou segunda ordem)

|  | **Aceitar a hipótese nula** | **Rejeitar a hipótese nula** |
|----|----|----|
| **Hipótese nula é verdadeira** | ✅ | Erro de Tipo I |
| **Hipótese nula é falsa** | Erro de Tipo II | ✅ |

Se $\theta \in \Omega_{0}$, $\pi(\theta\vert \delta)$ é a probabilidade de cometermos um erro de Tipo I, já que ele representa a probabilidade de que a amostra esteja na região crítica (rejeitar $H_{0}$) e, se $\theta \in \Omega_{1}$, $1 - \pi(\theta\vert \delta)$ é a probabilidade de cometermos um erro de Tipo II. No geral, queremos achar $\delta$ tal que $\pi(\theta\vert \delta)$ seja baixo para $\theta \in \Omega_{0}$ e alto para $\theta \in \Omega_{1}$, já que isso representa diminuir a probabilidade de cometer cada um dos erros.

Um método muito usado é escolher $\alpha_{0} \in (0,1\rbrack$ tal que: $$\pi(\theta\vert \delta) \leq \alpha_{0}\text{\quad\quad}\forall\theta \in \Omega_{0}$$<a id="level"></a> e depois procurar o teste que **maximiza** $\pi(\theta\vert \delta)$ satisfazendo a condição (para $\theta \in \Omega_{1}$)

**Definição: Tamanho de um Teste**

Um teste que satisfaz a equação [\[level\]](#level) é chamado de **teste de nível $\alpha_{0}$** e que o teste tem nível de significância $\alpha_{0}$. O tamanho $\alpha(\delta)$ de um teste $\delta$ é definido por: $$\alpha(\delta) = \sup\limits_{\theta \in \Omega_{0}}\pi(\theta\vert \delta)$$

Ou seja, o tamanho de um teste é a maior probabilidade de cometermos um erro de **Tipo I** possível (já que fazemos o supremo dentre todos os valores de $\Omega_{0}$) e um teste ter nível de significância $\alpha_{0}$ significa que, independente de qual parâmetro de $H_{0}$ seja o verdadeiro da distribuição, a chance de cometermos um erro de **Tipo I** sempre será menor que $\alpha_{0}$

**Corolário**

Um teste $\delta$ é de nível $\alpha_{0} \Leftrightarrow \alpha(\delta) \leq \alpha_{0}$

Se a hipótese nula é simples ($H_{0}:\theta = \theta_{0}$), então $\alpha(\delta) = \pi(\theta_{0}\vert \delta)$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Região Crítica e Testes Estatísticos](../regiao-critica-e-testes-estatisticos/index.md)
- Próximo: [Induzindo um nível de significância](../induzindo-um-nivel-de-significancia/index.md)
