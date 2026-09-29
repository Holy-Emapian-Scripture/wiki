---
layout: "default"
title: "Diagnóstico de Resíduos"
tipo: "conteudo"
disciplina: "Séries Temporais"
origem: "6 semestre/Séries Temporais/Recaps/A1.typ"
trilha: "../../../trilhas/series-temporais/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 34
---

[Séries Temporais](index.md)

<!-- wiki:original:inicio -->
<a id="secao-39"></a>

# Diagnóstico de Resíduos

## Introdução

O resíduo é a parte da observação que a previsão não explicou:

$$
e_t=Y_t-\hat Y_t.
$$

Em um modelo bem especificado, os resíduos devem se comportar como ruído branco: média zero e ausência de autocorrelação. Variância constante e normalidade aproximada também são desejáveis, especialmente para construir intervalos de previsão e fazer testes. Não rejeitar um teste de ruído branco significa apenas que não encontramos evidência suficiente de dependência; não prova que o modelo seja bom.

## Testes conjuntos de autocorrelação

Os testes *portmanteau* verificam simultaneamente os lags de 1 a $l$:

$$
H_0:\rho_e(1)=\cdots=\rho_e(l)=0,\qquad H_1:\text{algum }\rho_e(k)\ne0.
$$

Para os resíduos $e_1,\ldots,e_T$, a autocorrelação amostral no lag $k$ é

$$
r_k=\frac{\sum_{t=k+1}^{T}(e_t-\bar e)(e_{t-k}-\bar e)}{\sum_{t=1}^{T}(e_t-\bar e)^2}.
$$

Sob as condições assintóticas de ruído branco, $\sqrt T\,r_k$ se aproxima de uma normal padrão.

**Normalidade conjunta.** Para uma sequência i.i.d. com média zero, variância finita e quarto momento finito, e para um número fixo de lags $l$, o vetor $(\sqrt T\,r_1,\ldots,\sqrt T\,r_l)$ converge em distribuição para uma normal multivariada de média zero e matriz de covariância identidade. É essa aproximação que permite somar os quadrados das autocorrelações no teste.

### Teste de Box–Pierce

A estatística combina as autocorrelações dos primeiros $l$ lags:

$$
Q=T\sum_{k=1}^{l}r_k^2.
$$

Sob $H_0$, ela se aproxima de uma distribuição qui quadrado. A aproximação pode ser ruim para amostras finitas.

### Teste de Ljung–Box

Uma correção para o tamanho finito da amostra produz

$$
Q^*=T(T+2)\sum_{k=1}^{l}\frac{r_k^2}{T-k}.
$$

Essa é a versão geralmente preferida na prática. Quando se estimaram $K$ parâmetros no modelo, usa-se como aproximação uma distribuição qui quadrado com $d=l-K$ graus de liberdade, desde que $d>0$. Para uma baseline sem parâmetros ajustados, $K=0$. O número de lags deve ser escolhido antes de calcular o valor-p; regras práticas citadas no resumo são $l=10$ para dados não sazonais e $l=2m$ para sazonalidade de período $m$.

Ao nível de significância $\alpha$, rejeitamos $H_0$ se a estatística exceder o quantil $\chi^2_{d,1-\alpha}$, ou se o valor-p for menor que $\alpha$.

$$
c_{1-\alpha}=\chi^2_{d,1-\alpha},\qquad
p=1-F_{\chi^2_d}(Q),
$$

usando $Q^*$ no lugar de $Q$ para o teste de Ljung–Box. Um teste que não rejeita $H_0$ não garante que não haja outros problemas de modelagem.

![Ilustração do teste de Box–Pierce](assets/A1/box_pierce.png)

<a id="intervalos-de-previsao"></a>

## Intervalos de previsão

Se os erros forem normais, não correlacionados e tiverem variância constante, um intervalo de 95% para o horizonte $h$ pode ser construído como

$$
\hat Y_{T+h\mid T}\pm1{,}96\sqrt{\operatorname{Var}(Y_{T+h}-\hat Y_{T+h\mid T})}.
$$

O desvio padrão dos resíduos pode ser estimado por

$$
\hat\sigma=\sqrt{\frac{1}{T-K-M}\sum_{t=1}^{T}\hat e_t^2},
$$

onde $K$ e $M$ representam os ajustes de graus de liberdade adotados na fonte. O crescimento da incerteza depende do método de previsão:

- **Ingênuo:** $\hat\sigma_h=\sqrt h\,\hat\sigma$. ![Incerteza do método ingênuo](assets/A1/naive-std.png)
- **Média:** $\hat\sigma_h=\hat\sigma\sqrt{1+1/T}$. ![Incerteza do método da média](assets/A1/mean-std.png)
- **Ingênuo sazonal:** $\hat\sigma_h=\sqrt{K+1}\,\hat\sigma$, com $K=\lfloor(h-1)/m\rfloor$. ![Incerteza do método ingênuo sazonal](assets/A1/seasonal-naive-std.png)
- **Drift:** $\hat\sigma_h=\hat\sigma\sqrt{h(h+1)/(T-1)}$. ![Incerteza do método com drift](assets/A1/drift-std.png)

## Intervalo por bootstrap

Quando os resíduos são assimétricos ou têm caudas pesadas, um intervalo baseado na normalidade pode ficar mal calibrado. O procedimento do resumo é:

1. Extrair os resíduos observados de um passo, $\hat e_1,\ldots,\hat e_T$.
2. Para o primeiro horizonte, sortear um resíduo com reposição e somá-lo à previsão $\hat Y_{T+1\mid T}$.
3. Para cada horizonte seguinte, sortear outro resíduo e atualizar a previsão recursivamente usando a trajetória simulada.
4. Repetir o processo $B$ vezes e usar os quantis empíricos de 2,5% e 97,5% das previsões simuladas como limites do intervalo de 95%.

O bootstrap comum pressupõe resíduos sem autocorrelação: reamostrar choques dependentes como se fossem independentes não corrige um modelo que deixou memória na série.

![Trajetórias simuladas por bootstrap](assets/A1/bootstrap.png)

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../trilhas/series-temporais/a1.md) · [Apresentação e contexto da fonte](../../trilhas/series-temporais/a1.md#apresentacao-original)

- Anterior: [Previsão e Baselines](previsao-e-baselines.md)
- Próximo: [Métricas de Avaliação](metricas-de-avaliacao.md)
