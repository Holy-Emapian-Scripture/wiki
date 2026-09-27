---
layout: "default"
title: "Propriedades da divergência de Kullback-Leibler — Inferência Variacional"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A1.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 21
---

[Aprendizado de Máquina](../../index.md) · [Inferência Variacional](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-34"></a>

# Propriedades da divergência de Kullback-Leibler

**Teorema: Não-negatividade**

A divergência de Kullback-Leibler é não-negativa, ou seja, $\text{KL}\left( q\| p \right) \geq 0$

**Demonstração**

A desigualdade de Jensen fala que, para uma função convexa $f$ e uma variável aleatória $X$, temos que: $$f\left( {\mathbb{E}}\lbrack X\rbrack \right) \leq {\mathbb{E}}\left\lbrack f(X) \right\rbrack$$ sabemos que $- \ln(x)$ é uma função convexa, então, aplicando a desigualdade de Jensen, temos que: $$- \ln({\mathbb{E}}_{x \sim q}\left\lbrack \frac{p(x)}{q(x)} \right\rbrack) \leq {\mathbb{E}}_{x \sim q}\left\lbrack - \ln(\frac{p(x)}{q(x)}) \right\rbrack = {\mathbb{E}}_{x \sim q}\left\lbrack \ln(\frac{q(x)}{p(x)}) \right\rbrack = \text{ KL}\left( q\| p \right)$$ porém: $${\mathbb{E}}_{x \sim q}\left\lbrack \frac{p(x)}{q(x)} \right\rbrack = \int q(x)\left\{ \frac{p(x)}{q(x)} \right\} dx = \int p(x)dx = 1$$ logo: $$- \ln({\mathbb{E}}_{x \sim q}\left\lbrack \frac{p(x)}{q(x)} \right\rbrack) = - \ln(1) = 0$$ chegando à conclusão que: $$0 \leq \text{ KL}\left( q\| p \right)$$

**Teorema: Identidade**

$$\text{ KL}\left( q\| p \right) = 0 \Leftrightarrow q = p\text{ quase certamente }$$ ou seja, a divergência de Kullback-Leibler é zero se, e somente se, $q$ e $p$ são iguais

**Demonstração**

$\Longrightarrow )$ Se $q = p$, então: $$\text{ KL}\left( q\| p \right) = \int q(x)\ln\left\{ \frac{q(x)}{p(x)} \right\} dx = \int q(x)\ln\left\{ 1 \right\} dx = \int q(x)0dx = 0$$

$\Longleftarrow )$ Se $\text{KL}\left( q\| p \right) = 0$, então: $${\mathbb{E}}_{x \sim q}\left\lbrack \ln q(x) \right\rbrack = {\mathbb{E}}_{x \sim q}\left\lbrack \ln p(x) \right\rbrack$$ como $- \ln$ é uma função estritamente convexa, então, pela desigualdade de Jensen, temos que: $$0 \leq - {\mathbb{E}}_{x \sim q}\left\lbrack \ln(\frac{p(x)}{q(x)}) \right\rbrack$$ porém, a desiguldade de Jensen enuncia que: $${\mathbb{E}}\left\lbrack f(X) \right\rbrack = f\left( {\mathbb{E}}\lbrack X\rbrack \right) \Leftrightarrow X = c$$ ou seja, temos que $$\frac{p(x)}{q(x)} = c$$ entretanto ambas são densidades, assim: $$\int q(x)cdx = c = \int p(x)dx = 1 \Rightarrow c = 1 \Rightarrow \frac{p(x)}{q(x)} = 1 \Rightarrow p(x) = q(x)$$

**Teorema: KL e Entropia Cruzada**

A divergência de Kullback-Leibler pode ser escrita como a diferença entre a entropia cruzada e a entropia de $q$, ou seja: $$\text{ KL}\left( q\| p \right) = H(q,p) - H(q)$$ onde $H(q,p) = - {\mathbb{E}}_{x \sim q}\left\lbrack \ln p(x) \right\rbrack$ é a entropia cruzada entre $q$ e $p$ e $H(q) = - {\mathbb{E}}_{x \sim q}\left\lbrack \ln q(x) \right\rbrack$ é a entropia de $q$. Um ótimo vídeo que fala sobre isso é o [The Key Equation Behind Probability](https://youtu.be/KHVR587oW8I?si=HdtlJh1BHLMH7Has) do canal [Artem Kirsanov](https://www.youtube.com/@ArtemKirsanov)

**Demonstração**

$$\begin{aligned} \text{ KL}\left( q\| p \right) & = \int q(x)\ln\left\{ \frac{q(x)}{p(x)} \right\} dx \\ & = \int q(x)\ln\left\{ q(x) \right\} dx - \int q(x)\ln\left\{ p(x) \right\} dx \\ & = - H(q) + H(q,p) \\ & = H(q,p) - H(q) \end{aligned}$$

**Divergência KL *forward* vs *reverse***: É importante notar que, de forma geral, a divergência KL não é simétrica — i.e., $\text{KL}\left( q\| p \right) \neq \text{ KL}\left( p\| q \right)$. Na literatura de ML, é comum chamar $\text{KL}\left( q\| p \right)$ de divergência KL reversa. Conversamente, $\text{KL}\left( p\| q \right)$ é conhecida como a divergência forward. Empiricamente, é bem estabelecido que minimizar a divergência reversa costuma resultar em resultados que focam em alguma(s) modas. Por outro lado, minimizar a divergência forward costuma promover aproximações que cobrem melhor o suporte de $p$. A figura abaixo ilustra esse fenômeno com $p(\theta) = \frac{1}{2}\mathcal{N}(\theta\vert 3,1) + \frac{1}{2}\mathcal{N}(\theta\vert  - 3,\left( \frac{1}{2} \right)^{2})$ e $q$ sendo Gaussiana univariada

![](../../assets/kl_approximations.png)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/aprendizado-de-maquina/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a1.md#apresentacao-original)

- Anterior: [Introdução](../introducao/index.md)
- Próximo: [Cota Inferior (ELBO)](../cota-inferior-elbo/index.md)
