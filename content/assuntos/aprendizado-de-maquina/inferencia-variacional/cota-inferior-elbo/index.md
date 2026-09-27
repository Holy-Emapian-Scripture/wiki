---
layout: "default"
title: "Cota Inferior (ELBO) — Inferência Variacional"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 22
---

[Aprendizado de Máquina](../../index.md) · [Inferência Variacional](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-35"></a>

# Cota Inferior (ELBO)

Normalmente estamos realizando inferência bayesiana, ou seja, queremos calcular a distribuição posterior $p\left( \theta\vert D \right)$, mas isso é difícil de fazer diretamente. Então, vamos usar a divergência KL para encontrar uma aproximação $q(\theta)$ para $p\left( \theta\vert D \right)$. Para isso, vamos minimizar a divergência KL reversa: $$\begin{aligned} \text{ KL}\left( q(\theta)\| p\left( \theta\vert D \right) \right) & = {\mathbb{E}}_{\theta \sim q(\theta)}\left\lbrack \ln\left\{ \frac{q(\theta)}{p\left( \theta\vert D \right)} \right\} \right\rbrack \\ & = {\mathbb{E}}_{\theta \sim q(\theta)}\left\lbrack \ln q(\theta) \right\rbrack - {\mathbb{E}}_{\theta \sim q(\theta)}\left\lbrack \ln p\left( \theta\vert D \right) \right\rbrack \\ & = {\mathbb{E}}_{\theta \sim q(\theta)}\left\lbrack \ln q(\theta) \right\rbrack - {\mathbb{E}}_{\theta \sim q(\theta)}\left\lbrack \ln\frac{p\left( D\vert \theta \right)p(\theta)}{p(D)} \right\rbrack \\ & = {\mathbb{E}}_{\theta \sim q(\theta)}\left\lbrack \ln q(\theta) \right\rbrack - {\mathbb{E}}_{\theta \sim q(\theta)}\left\lbrack \ln p(D,\theta) \right\rbrack + \ln p(D) \end{aligned}$$ Vamos definir $L(q)$ como: $$L(q) = {\mathbb{E}}_{\theta \sim q(\theta)}\left\lbrack \ln p(D,\theta) \right\rbrack - {\mathbb{E}}_{\theta \sim q(\theta)}\left\lbrack \ln q(\theta) \right\rbrack$$ então temos que a distribuição $q$ que minimiza a divergência KL seria: $$\begin{aligned} \hat{q} & = \text{ argmin}_{q}\text{ KL}\left( q(\theta)\| p\left( \theta\vert D \right) \right) \\ & = \text{ argmin}_{q}{\mathbb{E}}_{\theta \sim q(\theta)}\left\lbrack \ln q(\theta) \right\rbrack - {\mathbb{E}}_{\theta \sim q(\theta)}\left\lbrack \ln p(D,\theta) \right\rbrack + \ln p(D) \\ & = \text{ argmin}_{q} - L(q) + \ln p(D) \\ & = \text{ argmax}_{q}L(q) \end{aligned}$$

algo interessante de se ressaltar é que, como $\text{KL } \geq 0$, temos que: $$\ln p(D) - L(q) = \text{ KL } \geq 0 \Rightarrow L(q) \leq \ln p(D)$$ logo, $\ln p(D)$ (conhecido como evidência) é uma cota superior para $L(q)$, e como queremos maximizar $L(q)$, estamos na verdade tentando encontrar a melhor aproximação para a evidência. Por isso, chamamos $L(q)$ de **Evidence Lower Bound** (ELBO), ou cota inferior da evidência.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Propriedades da divergência de Kullback-Leibler](../propriedades-da-divergencia-de-kullback-leibler/index.md)
- Próximo: [Lidando com ELBO intratável](../lidando-com-elbo-intratavel/index.md)
