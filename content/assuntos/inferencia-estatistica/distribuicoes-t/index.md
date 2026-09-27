---
layout: "default"
title: "Distribuições $t$"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 6
---

[Inferência Estatística](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-6"></a>

# Distribuições $t$

------------------------------------------------------------------------

$$\frac{\sqrt{n}\left( {\overline{X}}_{n} - \mu \right)}{\sigma} \sim N(0,1)$$ Porém, podemos não saber $\sigma$ e queremos substituir, por exemplo, por seu EMV, então qual seria a distribuição de $$\frac{\sqrt{n}({\overline{X}}_{n} - \mu)}{\hat{\sigma}}$$

**Definição: Distribuição $t$ com $m$ graus de liberdade**

Se $Z \sim N(0,1)$ e $Y \sim Χ_{m}^{2}$, então $$X = \frac{Z}{\sqrt{\frac{Y}{m}}} \sim t_{m}$$ onde dizemos $t$ com $m$ graus de liberdade

**Teorema: PDF**

A pdf de $X \sim t_{m}$ é: $$f_{X}(x) = \frac{\Gamma(\frac{m + 1}{2})}{(m\pi)^{\frac{1}{2}}\Gamma(\frac{m}{2})}\left( 1 + \frac{x^{2}}{m} \right)^{- (m + 1)/2}$$

**Demonstração**

Lembrando: $Y \sim Χ_{m}^{2}$ e $Z \sim N(0,1)$. Vamos aplicar as transformações! Sabemos que: $$f_{XW}(x,w) = f_{YZ}(y,z)\frac{~\vert ~\left( \partial(y,z) \right)}{\partial(x,w)}~\vert ~$$ então denotando $W = Y$, temos: $$Z = {X\left( \frac{W}{m} \right)}^{\frac{1}{2}}\text{\quad\quad}Y = W$$ Então vamos ter que: $$\frac{\partial y}{\partial x} = 0\text{\quad\quad}\frac{\partial y}{\partial w} = 1\frac{\begin{array}{r} \\ (\partial z) \end{array}}{\partial x} = \left( \frac{w}{m} \right)^{\frac{1}{2}}$$ então vamos ter que $$\frac{~\vert ~\left( \partial(y,z) \right)}{\partial(x,w)}~\vert ~ = {- \left( \frac{w}{m} \right)}^{\frac{1}{2}}$$ $$\begin{aligned} f_{XW}(x,w) & = f_{WZ}(w,z)\left( \frac{w}{m} \right)^{\frac{1}{2}} \\ & = f_{W}(w)f_{Z}(z)\left( \frac{w}{m} \right)^{\frac{1}{2}}\text{\quad\quad}\left( \text{Independência de Y e Z} \right) \\ & = f_{W}(w)f_{Z}\left( x\left( \frac{w}{m} \right)^{\frac{1}{2}} \right)\left( \frac{w}{m} \right)^{\frac{1}{2}} \\ & = \underset{f_{W}(w)}{\underbracket{\frac{\left( \frac{1}{2} \right)^{\frac{m}{2}}}{\Gamma(\frac{m}{2})}w^{\frac{m}{2} - 1}e^{- \frac{1}{2}w}}}\ \underset{f_{Z}(z)}{\underbracket{\frac{1}{\sqrt{2\pi}}e^{\frac{- x^{2}w}{2m}}}}\left( \frac{w}{m} \right)^{\frac{1}{2}} \end{aligned}$$

reescrevendo para ficar algo mais limpo e unir os termos comuns: $$f_{XW}(x,w) = \frac{\left( \frac{1}{2} \right)^{\frac{m}{2}}}{\Gamma(\frac{m}{2})\sqrt{2\pi m}}w^{\frac{m - 1}{2}}\exp\left\{ - \frac{1}{2}\left( 1 + \frac{x^{2}}{m} \right)w \right\}$$ Agora, para obtermos a marginal de $X$, precisamos integrar isso tudo com relação a $w$. Porém, basta integrarmos aquilo que é em função apenas de $w$, as constantes nós podemos adicionar novamente depois, então: $$f_{X}(x) \propto \int_{0}^{\infty}w^{\frac{m - 1}{2}}\exp\left\{ - \frac{1}{2}\left( 1 + \frac{x^{2}}{m} \right)w \right\} dw$$ Se definirmos $\alpha = \frac{m + 1}{2}$ e $\beta = \frac{1}{2}\left( 1 + \frac{x^{2}}{m} \right)$, então a integral equivale a: $$f_{X}(x) \propto \int_{0}^{\infty}w^{\alpha - 1}e^{- \beta w}dw = \frac{\Gamma(\alpha)}{\beta^{\alpha}} = \frac{\Gamma(\frac{m + 1}{2})}{\left( \frac{1}{2}\left\lbrack 1 + \frac{x^{2}}{m} \right\rbrack \right)^{(m + 1)/2}}$$ $$\Rightarrow f_{X}(x) = \frac{\left( \frac{1}{2} \right)^{\frac{m}{2}}}{\Gamma(\frac{m}{2})\sqrt{2\pi m}}\Gamma(\frac{m + 1}{2})\left( \frac{1}{2}\left\lbrack 1 + \frac{x^{2}}{m} \right\rbrack \right)^{- (m + 1)/2}$$ juntando tudo, temos: $$f_{X}(x) = \frac{\Gamma(\frac{m + 1}{2})}{\sqrt{m\pi}\ \Gamma(\frac{m}{2})}\left( 1 + \frac{x^{2}}{m} \right)^{- (m + 1)/2}$$

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Propriedades](propriedades/index.md)

## Percurso de estudo

[Trilha: A2](../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Independência da Média e Variância Amostrais](../distribuicao-conjunta-da-media-e-variancia-amostral/independencia-da-media-e-variancia-amostrais/index.md)
- Próximo: [Propriedades](propriedades/index.md)
