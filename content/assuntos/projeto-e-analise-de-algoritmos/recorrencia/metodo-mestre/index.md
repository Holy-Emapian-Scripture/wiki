---
layout: "default"
title: "Método mestre — Recorrência"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A1.md"
trilha: "../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
revisao: "Thalis Ambrosim Falqueto"
ano_original: 2025
ordem_na_trilha: 6
---

[Projeto e Análise de Algoritmos](../../index.md) · [Recorrência](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-6"></a>

# Método mestre

Esse teorema é uma decoreba. Ele te dá um caso geral e vários casos de resultado dependendo dos valores na estrutura de $T(n)$

**Teorema: Teorema Mestre**

Dada uma recorrência da forma $$T(n) = aT\left( \frac{n}{b} \right) + f(n)$$ Considerando $a \geq 1$, $b > 1$ e $f(n)$ assintoticamente positiva

- Se $f(n) = O\left( n^{\log_{b}(a) - \varepsilon} \right)$ para alguma constante $\varepsilon > 0$, então **$T(n) = \Theta(n^{\log_{b}(a)})$**

- Se $f(n) = \Theta(n^{\log_{b}(a)})$, então **$T(n) = \Theta(f(n)\log(n))$**

- Se $f(n) = \Omega(n^{\log_{b}(a) + \varepsilon})$ para alguma constante $\varepsilon > 0$ e atender a uma condição de regularidade $af\left( \frac{n}{b} \right) \leq cf(n)$ para alguma constante positiva $c < 1$ e para todo $n$ suficientemente grande, então **$T(n) = \Theta(f(n))$**

**Exemplo: Primeiro caso**

$$T(n) = 9T\left( \frac{n}{3} \right) + n$$ Então $a = 9$, $b = 3$ e $f(n) = n$, calculamos então: $$n^{\log_{b}(a)} = n^{\log_{3}(9)} = n^{2}$$ Ou seja, conseguimos escolher $\varepsilon = 1$ de forma que $$f(n) = O\left( n^{2 - 1} \right) = O(n)$$ Ou seja, $T(n) = \Theta(n^{2})$

**Exemplo: Segundo caso**

$$T(n) = T\left( \frac{2n}{3} \right) + 1$$ Então $a = 1$, $b = \frac{3}{2}$ e $f(n) = 1$, calculamos então: $$n^{\log_{b}(a)} = n^{\log_{\frac{3}{2}}(1)} = 1$$ Ou seja, $f(n) = \Theta(n^{\log_{b}(a)})$, e isso quer dizer que $T(n) = \Theta(n^{\log_{\frac{3}{2}}(1)\log(n)}) = \Theta(\log(n))$

**Exemplo: Terceiro caso**

$$T(n) = 3T\left( \frac{n}{4} \right) + n\log(n)$$ Então $a = 3$, $b = 4$ e $f(n) = n\log(n)$, calculamos então: $$n^{\log_{b}(a)} = n^{\log_{4}3} \approx n^{0.79}$$ Temos então que $f(n) = \Omega(n^{\log_{4}3 + \varepsilon})$ para um $\varepsilon \approx 0.2$. Então agora vamos analisar a condição de regularidade: $$\begin{array}{r} af\left( \frac{n}{b} \right) \leq cf(n) \\ 3\left( \frac{n}{4}\log(\frac{n}{4}) \right) \leq cn\log(n) \Rightarrow c \geq \frac{3}{4} \end{array}$$ Ou seja, $T(n) = \Theta(n\log(n))$

**Exemplo: Exemplo que não funciona**

$$T(n) = 2T\left( \frac{n}{2} \right) + n\log(n)$$ Para agilizar, isso se encaixa no caso em que $f(n) = \Omega(n^{\log_{b}(a) + \varepsilon})$. Vamos então checar a regularidade: $$\begin{array}{r} af\left( \frac{n}{b} \right) \leq cf(n) \\ 2\frac{n}{2}\log(\frac{n}{2}) \leq cn\log(n) \\ \Leftrightarrow c \geq 1 - \frac{1}{\log(n)} \end{array}$$ **Impossível!** Já que $c < 1$

Esse método pode ser simplificado para uma categoria específica de funções

**Teorema: Teorema mestre simplificado**

Dada uma recorrência do tipo: $$T(n) = aT\left( \frac{n}{b} \right) + \Theta(n^{k})$$ Considerando $a \geq 1$, $b > 1$ e $k \geq 0$:

- Se $a > b^{k}$, então **$T(n) = \Theta(n^{\log_{b}a})$**

- Se $a = b^{k}$, então **$T(n) = \Theta(n^{k}\log n)$**

- Se $a < b^{k}$, então **$T(n) = \Theta(n^{k})$**

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Método da Recorrência](../metodo-da-recorrencia/index.md)
- Próximo: [Algoritmos de busca](../../algoritmos-de-busca/index.md)
