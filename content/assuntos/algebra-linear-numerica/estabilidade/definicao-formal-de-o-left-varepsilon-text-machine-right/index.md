---
layout: "default"
title: "Definição Formal de $O\\left( \\varepsilon_{\\text{machine}} \\right)$ — Estabilidade"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 46
---

[Álgebra Linear Numérica](../../index.md) · [Estabilidade](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-55"></a>

# Definição Formal de $O\left( \varepsilon_{\text{machine}} \right)$

Vou escrever a definição aqui e explicar o que significa logo depois

**Definição**

Dadas as funções $\varphi(t)$ e $\psi(t)$, a sentença $$\varphi(t) = O\left( \psi(t) \right)$$ significa que $\exists C > 0$ tal que $\forall t$ suficientemente próximo de um limite conhecido (por exemplo, $t \rightarrow 0$, $t \rightarrow \infty$), é válido que: $$\varphi(t) \leq C\psi(t)$$

O que isso significa? Significa que, se escrevemos $\varphi(t) = O\left( \psi(t) \right)$, e sabemos para onde $t$ está indo, existe $C > 0$ tal que os valores de $\varphi(t)$ nunca serão maiores que $C\psi(t)$. Na maioria das vezes, eu nem me importo com o que é $C$, só me importo com sua existência!

Falando sobre como estamos tratando $\varepsilon_{\text{machine}}$, o limite implícito aqui é $\varepsilon_{\text{machine }} \rightarrow 0$, e escrever que $\varphi(t) = O\left( \varepsilon_{\text{machine}} \right)$ significa que temos uma constante que limita o erro a uma quantidade de $\varepsilon_{\text{machine}}$, ou seja, o erro nunca será maior que, por exemplo, $3$ vezes $\varepsilon_{\text{machine}}$, $2$ e meio vezes $\varepsilon_{\text{machine}}$.

Podemos fazer uma definição formal mais forte (mas mais confusa) para a notação $O$

**Definição**

Dado $\varphi(s,t)$, temos que: $$\varphi(s,t) = O\left( \psi(t) \right)\text{ uniformemente em }s$$ garante que $\exists!C > 0$ tal que: $$\varphi(s,t) \leq C\psi(t)$$ e isso é válido para qualquer $s$ que eu escolher

É uma definição semelhante, estou apenas adicionando uma variável que posso escolher e que não mudará nada.

Em computadores reais, $\varepsilon_{\text{machine}}$ é um número fixo, então quando estamos trabalhando com o limite implícito $\varepsilon_{\text{machine }} \rightarrow 0$, estamos selecionando uma família **ideal** de computadores!

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Estabilidade](../index.md)
- Próximo: [Dependência de $m$ e $n$](../dependencia-de-m-e-n/index.md)
