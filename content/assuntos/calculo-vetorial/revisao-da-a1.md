---
layout: "default"
title: "Revisão da A1"
tipo: "conteudo"
disciplina: "Cálculo Vetorial"
origem: "3 semestre/Cálculo Vetorial/Recaps/A2_recap.md"
trilha: "../../../trilhas/calculo-vetorial/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Arthur Rabello Oliveira"]
data_original: "27/09/2026"
ordem_na_trilha: 1
---

[Cálculo Vetorial](index.md)

<!-- wiki:original:inicio -->

<a id="section_revisao_a1"></a>

# Revisão da A1


<a id="section_integral_linha"></a>

## Integrais de Linha

<a id="section_integral_linha_escalar"></a>

### Integrais de Linha Escalares

Dada $f:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$ uma função escalar e $\gamma:\lbrack a,b\rbrack \rightarrow {\mathbb{R}}^{n}$ uma curva, a integral de $f$ sobre $\gamma$ é:

$$\int_{\gamma}fdS = \int_{a}^{b}f\left( \gamma(\varphi) \right) \cdot \left\| {\gamma'(\varphi)} \right\| d\varphi$$ <a id="equation_line_integral"></a>

<a id="section_integral_linha_vetorial"></a>

### Integrais de Linha Vetoriais

Se for $F:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}$ um campo vetorial:

$$\int_{\gamma}FdS = \int_{a}^{b}F\left( \gamma(\varphi) \right) \cdot \gamma'(\varphi)d\varphi$$ <a id="equation_line_integral_vectorial"></a>

<a id="section_line_integral_conservativo"></a>

### Integral de Linha de um Campo Conservativo

Se $F:{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{n}$ for conservativo, com $f::{\mathbb{R}}^{n} \rightarrow {\mathbb{R}}$, $\nabla f = F$ e $c:\lbrack a,b\rbrack \rightarrow {\mathbb{R}}^{n}$, temos:

$$\int_{c}FdS = f\left( c(b) \right) - f\left( c(a) \right)$$ <a id="equation_line_integral_conservativo"></a>

E são equivalentes:

1.  $F$ é conservativo

2.  $\int_{c}FdS = 0$ para todo caminho fechado $c$

3.  $\oint_{c}F = 0$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/calculo-vetorial/a2.md) · [Apresentação e contexto da fonte](../../trilhas/calculo-vetorial/a2.md#apresentacao-original)

- Próximo: [Integrais de Superfície](integrais-de-superficie.md)
