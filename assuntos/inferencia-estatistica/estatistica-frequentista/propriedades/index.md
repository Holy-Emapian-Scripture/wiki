---
layout: "default"
title: "Propriedades — Estatística Frequentista"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 15
---

[Inferência Estatística](../../index.md) · [Estatística Frequentista](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Propriedades

**Teorema**

Se $\hat{\theta} \in \Omega$ é o Estimador de Máxima Verossimilhança (EMV) de $\theta$ e $g$ é uma função bijetiva, então $g\left( \hat{\theta} \right)$ é o EMV de $g(\theta)$

**Demonstração**

Seja $\Gamma$ o novo espaço paramétrico, ou seja, $g:\Omega \rightarrow \Gamma$. Vamos definir $h$ como sendo a função inversa, ou seja $\theta = h(\psi)$. Se expressarmos a p.d.f em função de $\psi$, vamos obter $f\left( x\vert h(\psi) \right)$ e a função de verossimilhança será $f\left( \underline{x}\vert h(\psi) \right)$.

Sabemos que o EMV $\hat{\psi}$ de $\psi$ é vai ser o valor de $\psi$ que maximiza $f\left( \underline{x}\vert h(x) \right)$. Como $f\left( x\vert \theta \right)$ é maximizada quando $\theta = \hat{\theta}$, então $h(\psi) = \hat{\theta}$ maximiza a verossimilhança. Porém, aplicando $g$ em ambos os lados, obtemos que: $$\hat{\psi} = g\left( \hat{\theta} \right)$$

Essa propriedade é algo ótimo! Tendo em vista que no método anterior, o estimador de Bayes de $1/\theta$ podia ser diferente de $1/\hat{\theta}$. Porém, podemos estender esse teorema para casos em que a função $g$ não é bijetiva. Vamos então definir o **estimador de uma função**

**Definição: MVE de uma Função**

Seja $g(\theta)$ uma função arbitrária do parâmetro com $g:\Omega \rightarrow G$. Para cada $t \in G$, defina $G_{t} ≔ \left\{ \theta:g(\theta) = t \right\}$ e $L^{\ast \left( \hat{t} \right)} ≔ \max\limits_{\theta \in G_{t}}\log f\left( \underline{x}\vert \theta \right)$, defina então o EMV de $g(\theta)$ como $\hat{t}$ como: $$L^{\ast \left( \hat{t} \right)} = \max\limits_{t \in G_{t}}L^{\ast (t)}$$

**Teorema**

Dado $\hat{\theta}$ sendo o EMV de $\theta$ e $g:\Omega \rightarrow G$, então: $$\hat{g(\theta)} = g\left( \hat{\theta} \right)$$

**Demonstração**

Como $L^{\ast (t)}$ é o máximo de $\log f\left( \underline{x}\vert \theta \right)$ em $\theta$ num subconjunto de $\Omega$, e como $\log f\left( \underline{x}\vert \hat{\theta} \right)$ é o máximo sob todos os $\theta$, então sabemos que $L^{\ast (t)} \leq \log f\left( \underline{x}\vert \theta \right)\ \forall t \in G$. Denote $\hat{t} = g\left( \hat{\theta} \right)$. Perceba que $\hat{\theta} \in G_{\hat{t}}$. Como $\hat{\theta}$ maximiza $f\left( \underline{x}\vert \theta \right)$ em todos $\theta$, então ele também maximiza $f\left( \underline{x}\vert \theta \right)$ sob todos os $\theta \in G_{\hat{t}}$. Por isso, $L^{\ast \left( \hat{t} \right)} = \log f\left( \underline{x}\vert \hat{\theta} \right)$ e $\hat{t} = g\left( \hat{\theta} \right)$ é um EVM de $g(\theta)$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Estimadores/Estimações de Máxima Verossimilhança](../estimadores-estimacoes-de-maxima-verossimilhanca/index.md)
- Próximo: [Computação Numérica](../computacao-numerica/index.md)
