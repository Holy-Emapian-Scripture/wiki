---
layout: "default"
title: "Transformada de Laplace"
tipo: "conteudo"
disciplina: "Equações Diferenciais Ordinárias"
origem: "3 semestre/EDO/RecapA2.md"
trilha: "../../../trilhas/equacoes-diferenciais-ordinarias/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["jãopredo", "artu"]
data_original: "27/09/2026"
ordem_na_trilha: 1
---

[Equações Diferenciais Ordinárias](index.md)

<!-- wiki:original:inicio -->

<a id="section_transformada_de_laplace"></a>

# Transformada de Laplace


<a id="definicao"></a>
<a id="section_definicao_transformada_de_laplace"></a>

## Definição

**Definição**

(Transformada de Laplace)  
Dada $f:{\mathbb{R}} \rightarrow {\mathbb{R}}$ contínua por partes e $f \in O\left( e^{st} \right)$, definimos a Transformada de Laplace como

$$
L\left\{ f(t) \right\} = \int_{0}^{\infty}e^{- st}f(t)dt
$$

<a id="propriedades-com-derivada"></a>
<a id="section_propriedades_com_derivada"></a>

## Propriedades Com derivada

**Propriedade**

Se $f:{\mathbb{R}} \rightarrow {\mathbb{R}}$ é derivável, então:

$$
L\left\{ f'(t) \right\} = sL\left\{ f(t) \right\} - f(0)
$$

Analogamente:

$$
L\left\{ f''(t) \right\} = s^{2}L\left\{ f(t) \right\} - sf(0) - f'(0)
$$

E assim por diante.

Resolver EDO’s com a transformada de Laplace se restringe a algebricamente buscar a inversa de $L\left\{ f(t) \right\}$, justamente a função procurada.

<a id="funcao-degrau"></a>
<a id="section_funcao_degrau"></a>

## Função degrau

A função degrau $u_{c}$ é definida como:

$$
u_{c(t)} = \begin{cases} 0\text{ se }t < c \\ 1\text{ se }t \geq c \end{cases}
$$

<a id="propriedades-com-funcao-degrau"></a>
<a id="section_propriedades_com_funcao_degrau"></a>

## Propriedades com Função degrau

**Propriedade**

Se $F(s) = L\left\{ f(t) \right\}$ existe, dada $f:{\mathbb{R}} \rightarrow {\mathbb{R}}$, então:

$$
L\left\{ u_{c}(t)f(t - c) \right\} = e^{- sc} \cdot F(s)
$$

**Propriedade**

Se $F(s) = L\left\{ f(t) \right\}$ existe, dada $f:{\mathbb{R}} \rightarrow {\mathbb{R}}$, então:

$$
L\left\{ e^{ct}f(t) \right\} = F(s - c)
$$

Ou equivalentemente:

$$
e^{ct}f(t) = L^{- 1}\left\{ F(s - c) \right\}
$$

<a id="funcao-impulso"></a>
<a id="section_funcao_impulso"></a>

## Função Impulso

A função impulso $\delta$ satifaz:

$$
\begin{array}{r} \delta(t) = 0,t \neq 0 \\ \int_{- \infty}^{\infty}\delta(t)dt = 1 \end{array}
$$

<a id="propriedades-com-funcao-impulso"></a>
<a id="section_propriedades_com_funcao_impulso"></a>

## Propriedades com Função Impulso

A transformada de Laplace da função impulso é:

$$
L\left\{ \delta(t - c) \right\} = e^{- sc}
$$

E também vale:

$$
L\left\{ \delta(t - c)f(t) \right\} = f(c)e^{- sc}
$$

<a id="convolucao"></a>
<a id="section_convolucao"></a>

## Convolução

Dadas $F(s) = L\left\{ f(t) \right\}$ e $G(s) = L\left\{ g(t) \right\}$, a transformada do produto pode ser calculada como:

$$
H(s) = F(s)G(t) = L\left\{ h(t) \right\}
$$

Onde:

$$
h(t) = \int_{0}^{t}f(t - \tau)g(\tau)d\tau = \int_{0}^{t}f(\tau)g(t - \tau)d\tau
$$

A função $h$ é chamada de convolução de $f$ e $g$, denotada por $f \ast g$.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A2](../../trilhas/equacoes-diferenciais-ordinarias/a2.md) · [Apresentação e contexto da fonte](../../trilhas/equacoes-diferenciais-ordinarias/a2.md#apresentacao-original)

- Próximo: [Sistemas de EDO’s de Primeira Ordem](sistemas-de-edos-de-primeira-ordem.md)
