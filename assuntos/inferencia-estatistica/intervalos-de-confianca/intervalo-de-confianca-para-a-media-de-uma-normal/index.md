---
layout: "default"
title: "Intervalo de Confiança para a média de uma Normal — Intervalos de Confiança"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 9
---

[Inferência Estatística](../../index.md) · [Intervalos de Confiança](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-9"></a>

# Intervalo de Confiança para a média de uma Normal

Dada a amostra $X_{1},\ldots,X_{n} \sim N\left( \mu,\sigma^{2} \right)$, sabemos que $U = \sqrt{n}(\overline{X} - \mu)/\sigma' \sim t_{n - 1}$. Eu gostaria de achar um intervalo no qual eu tenho uma chance boa de encontrar minha média, então eu gostaria de algo do tipo: $${\mathbb{P}}( - c < U < c) = \gamma$$<a id="normal-mean-conficence-interval"></a> O método mais comum é calcular diretamente o $c$ que torna a equação [\[normal-mean-conficence-interval\]](#normal-mean-conficence-interval) verdadeira. Isso é equivalente a dizer: $${\mathbb{P}}({\overline{X}}_{n} - \frac{c\sigma'}{\sqrt{n}} < \mu < {\overline{X}}_{n} + \frac{c\sigma'}{\sqrt{n}}) = \gamma$$ Vale ressaltar que essa probabilidade é referente a distribuição conjunta de ${\overline{X}}_{n}$ e $\sigma'$ para valores **fixos** de $\mu$ e $\sigma$ (Independentemente de sabermos eles ou não). Então vamos tentar achar o $c$ que satisfaz isso $${\mathbb{P}}( - c < U < c) = \gamma \Leftrightarrow T_{n - 1}(c) - T_{n - 1}( - c) = \gamma$$ Pela simetria de $t$ em $0$, posso reescrever como: $$2T_{n - 1}(c) - 1 = \gamma \Rightarrow c = T_{n - 1}^{- 1}\left( \frac{1 + \gamma}{2} \right)$$ Então, depois que descobrimos $c$, nosso intervalo de confiança vira: $$\begin{array}{r} A = {\overline{X}}_{n} - \sigma\frac{'}{\sqrt{n}}\ T_{n - 1}^{- 1}\left( \frac{1 + \gamma}{2} \right) \\ B = {\overline{X}}_{n} + \sigma\frac{'}{\sqrt{n}}\ T_{n - 1}^{- 1}\left( \frac{1 + \gamma}{2} \right) \end{array}$$

Dada essa noção inicial, vamos definir formalmente esses intervalos:

**Definição: Intervalo de confiança**

Seja $\underline{X} = \left( X_{1},\ldots,X_{n} \right)$ uma amostra de uma distribuição indexada pelo(s) parâmetro(s) $\theta$ e seja $g(\theta):\Omega \rightarrow {\mathbb{R}}$. Seja também $A$ e $B$ duas estatísticas $(A \leq B)$ que satisfazem: $${\mathbb{P}}(A < g(\theta) < B) \geq \gamma$$<a id="confidence-interval-property"></a> O intervalo aleatório $(A,B)$ é chamado de intervalo de confiança $\gamma$ para $g(\theta)$ ou de intervalo de confiança $100\gamma\%$ para $g(\theta)$. Depois que $X_{1},\ldots,X_{n}$ foi observado e o intervalo $A = a$ e $B = b$ foi computado, chamamos o valor observado do intervalo de **valor observado do intervalo de confiança**. Se a equação [\[confidence-interval-property\]](#confidence-interval-property) vale a igualdade $\forall c \in (A,B)$, então chamamos esse intervalo de **exato**

Aqui eu vou definir melhor a interpretação com relação a essa definição, que pode ser um pouco confusa. A interpretação do intervalo $A,B$ em si é bem direta, representa um intervalo **aleatório** que tem probabilidade $\gamma$ de conter $g(\theta)$. Porém, ao observamos as amostras e calcularmos $A = a$ e $B = b$, o intervalo $(a,b)$ **não necessariamente contém $g(\theta)$ com probabilidade $\gamma$**, como assim? Lembra que $(A,B)$ é um intervalo **aleatório**, enquanto $(a,b)$ é uma das muitas possíveis ocorrências desse intervalo! A interpretação correta é, que quanto mais repetimos o experimento e computamos $(a,b)$ e armazenamos esses valores observados de intervalo, uma fração $\gamma$ deles contém $g(\theta)$, porém, **não sabemos dizer quais contém e quais não contém**

**Teorema**

Dada a amostra $X_{1},\ldots,X_{n} \sim N\left( \mu,\sigma^{2} \right)$. $\forall\gamma \in \lbrack 0,1\rbrack$, o intervalo $(A,B)$ com seguintes pontos: $$\begin{array}{r} A = {\overline{X}}_{n} - \sigma\frac{'}{\sqrt{n}}\ T_{n - 1}^{- 1}\left( \frac{1 + \gamma}{2} \right) \\ B = {\overline{X}}_{n} + \sigma\frac{'}{\sqrt{n}}\ T_{n - 1}^{- 1}\left( \frac{1 + \gamma}{2} \right) \end{array}$$ é um intervalo de confiança $\gamma$-exato

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Intervalos de Confiança](../index.md)
- Próximo: [Intervalos de Confiança Unilaterais](../intervalos-de-confianca-unilaterais/index.md)
