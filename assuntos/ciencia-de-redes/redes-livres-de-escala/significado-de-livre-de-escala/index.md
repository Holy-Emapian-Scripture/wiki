---
layout: "default"
title: "Significado de Livre de Escala — Redes Livres de Escala"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A1.md"
trilha: "../../../../trilhas/ciencia-de-redes/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 17
---

[Ciência de Redes](../../index.md) · [Redes Livres de Escala](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-22"></a>

# Significado de Livre de Escala

Antes de entender o significado desse termo, vamos nos familiarizar com alguns conceitos. Vimos em probabilidade o conceito de **momentos**. O $n$-ésimo momento da distribuição dos graus (Levando em conta a variável aleatória $K$ que é o grau de um vértice aleatório) é: $${\mathbb{E}}\left\lbrack K^{n} \right\rbrack = \sum_{i = k_{\min}}^{\infty}k^{n} \cdot {\mathbb{P}}(K = k) = \int_{k_{\min}}^{\infty}k^{n}p(k)dk$$

Resolvendo a integral, vamos obter: $${\mathbb{E}}\left\lbrack K^{n} \right\rbrack = C\frac{k_{\max}^{n - \gamma + 1} - k_{\min}^{n - \gamma + 1}}{n - \gamma + 1}$$

Sabemos que, normalmente, $k_{\min}$ é fixo enquanto $k_{\max}$ aumenta confirme $N \rightarrow \infty$. Então vamos fazer uma análise mais detalhada sobre essa fórmula para o $n$-ésimo momento

- Se $n - \gamma + 1 \leq 0$, então $k_{\max}^{n - \gamma + 1} \rightarrow 0$ quando $N \rightarrow \infty$ (Ou $1$ quando a equação é igual a $0$). Então todos os momentos que satisfazem $n < \gamma - 1$ são **finitos**

- Do contrário, se $n - \gamma + 1 > 0$, então $k_{\max}^{n - \gamma + 1} \rightarrow \infty$ quando $N \rightarrow \infty$, então os momentos que satisfazem $n > \gamma - 1$ **divergem**

Agora a gente pode tentar entender melhor o que esse **sem escala** significa. Vamos pegar uma rede de Poisson, sabemos que ${\mathbb{E}}\lbrack K\rbrack = \hat{k}$ e que $\sigma_{k} = \sqrt{\hat{k}}$ (Desvio padrão dos graus). Pela desigualdade de Chebyshev: $${\mathbb{P}}(\vert K - \hat{k}\vert  \geq h\sigma_{k}) \leq \frac{1}{h^{2}}$$

Que que isso quer dizer? O que quero dizer é que, em redes de Poisson, a chance de os graus estárem a $h$ desvios padrões da média é **no máximo** $1/h^{2}$. Isso é um indicativo grande de que a média dos graus serve como uma “escala”, de forma que temos uma noção do quão longe desse valor podemos estar caso escolhemos um nó aleatório.

Porém, em redes livres de escala em que o segundo momento diverge? Isso significa que, quando eu pego um nó aleatoriamente nessa rede, eu não sei o que esperar, a diferença dele para a média pode ser arbitrariamente grande ou pequena, não temos como ter ideia, ou seja, **não há uma escala para comparação**

É claro que a divergência de ${\mathbb{E}}\left\lbrack K^{2} \right\rbrack$ só acontece no limite $N \rightarrow \infty$, mas isso ainda tem uma relevância para redes finitas. Vamos pegar o caso da rede de internet novamente, sabemos que a quantidade de documentos (Nós) está na casa dos bilhões ou trilhões, o que indica que temos uma variância MUITO GRANDE, ou seja, mesmo tendo uma variância finita e, no concreto, tenhamos uma escala, ela é quase irrelevante, já que, ao pegarmos um documento aleatório, ele pode estar sendo citado por apenas dois outros documentos, ou ser citado por bilhões de documentos (Como google, facebook, etc.)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Anterior: [Centros](../centros/index.md)
- Próximo: [Propriedade *Ultra Small*](../propriedade-ultra-small/index.md)
