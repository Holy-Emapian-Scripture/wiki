---
layout: "default"
title: "Definições — Variáveis Aleatórias Contínuas"
tipo: "conteudo"
disciplina: "Probabilidade"
origem: "3 semestre/Probabilidade/Recaps/A2_recap.md"
trilha: "../../../../trilhas/probabilidade/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 2
---

[Probabilidade](../../index.md) · [Variáveis Aleatórias Contínuas](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-2"></a>

# Definições

Definimos aqui o necessário sobre variáveis aleatórias contínuas para a compreensão dos conteúdos do teste:

<a id="definiticao_variavel_aleatoria_continua"></a>

**Definição**

(V.A Contínua)  
Uma v.a $X:\Omega \rightarrow {\mathbb{R}}$ é dita contínua se e somente se sua CDF $F_{X}$ for derivável

<a id="definicao_CDF"></a>

**Definição**

(Função de Distribuição - CDF)  
A função de distribuição de uma v.a contínua $X$ é dada por: $$F_{X}(\varphi) = P(X \leq \varphi)$$

**Definição**

(Função de Densidade - PDF)  
Calculamos a densidade de probabilidade calculando a probabilidade de $X$ estar num intervalo, e dividimos pelo tamanho do intervalo:

$$\frac{P\left( X \in I = \lbrack\psi,\psi + \varepsilon\rbrack \right)}{\left\| I \right\| = \varepsilon} = \frac{P(\psi \leq X \leq \psi + \varepsilon)}{\varepsilon} = \frac{F_{X}(\psi + \varepsilon) - F_{X}(\psi)}{\varepsilon}$$

Tomando o limite quando $\varepsilon \rightarrow 0$, obtemos a *função de densidade de probabilidade* PDF no ponto $\psi$:

$$\lim\limits_{\varepsilon \rightarrow 0}\frac{F_{X}(\psi + \varepsilon) - F_{X}(\psi)}{\varepsilon} = F'_{X}(\psi) = f_{X}(\psi)$$

É importante notar que a PDF não é uma probabilidade, mas sim uma densidade de probabilidade. Veja:

$$P(X \in I) = P(a \leq X \leq b) = F_{X}(b) - F_{X}(a)$$

Usamos a PDF e o teorema fundamental do cálculo para calcular a probabilidade de $X$ estar em um intervalo $I = \lbrack a,b\rbrack$:

$$P(X \in I) = F_{X}(b) - F_{X}(a) = \int_{a}^{b}f_{X}(\varphi)d\varphi$$

Logo a **a integral definida** da PDF é de fato uma probabilidade.

<a id="definicao_PDF"></a>

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/probabilidade/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/probabilidade/a2.md#apresentacao-original)

- Anterior: [Variáveis Aleatórias Contínuas](../index.md)
- Próximo: [Propriedades da CDF e PDF](../propriedades-da-cdf-e-pdf/index.md)
