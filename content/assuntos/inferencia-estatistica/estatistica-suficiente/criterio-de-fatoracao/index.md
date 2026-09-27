---
layout: "default"
title: "Critério de Fatoração — Estatística Suficiente"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 19
---

[Inferência Estatística](../../index.md) · [Estatística Suficiente](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-19"></a>

# Critério de Fatoração

Agora nos é apresentado um método de identificar estatísticas suficientes (Um teorema bem interessante) desenvolvido por R. A. Fisher em 1922, J. Neyman em 1935 e P. R. Halmos e L. J. Savage em 1949

**Teorema: Critério da Fatoração**

Sejam $X_{1},\ldots,X_{n}$ uma amostra aleatória de uma distribuição contínua ou discreta para qual a p.d.f ou a p.f é $f\left( x\vert \theta \right)$, onde o valor de $\theta$ é desconhecido e pertence a um espaço paramétrico $\Omega$. Uma estatística $T = r\left( X_{1},\ldots,X_{n} \right)$ é **suficiente** para $\theta$ **se, e somente se,** a função de densidade ou de massa conjunta $f\left( \underline{x}\vert \theta \right)$ de $X_{1},\ldots X_{n}$ pode ser fatorada, para todos os valores de $x = \left( x_{1},\ldots,x_{n} \right) \in {\mathbb{R}}^{n}$ e para todos os valores de $\theta \in \Omega$, da seguinte forma: $$f\left( \underline{x}\vert \theta \right) = u\left( \underline{x} \right)v\left( r\left( \underline{x} \right),\theta \right)$$ Onde $u$ e $v$ são não-negativas. $u$ pode depender em $\underline{x}$ mas não em $\theta$ e $v$ pode depende em $\theta$ e na estatística $t$

**Demonstração**

Vamos fazer a prova só para o caso que $X$ tem uma distribuição discreta, ou seja: $$f\left( \underline{x}\vert \theta \right) = {\mathbb{P}}(X_{1} = x_{1},\ldots,X_{n} = x_{n}\vert \theta)$$ Primeiro vamos fazer a volta. Então vamos supor que $f\left( \underline{x}\vert \theta \right)$ pode ser fatorado daquela forma. Para cada valor possível $t$ da estatística $T$, denote $A(t)$ como sendo o conjunto de todos os pontos $\underline{x} \in {\mathbb{R}}^{n}$ tal que $r\left( \underline{x} \right) = t$. Para cada valor de $\theta \in \Omega$, nós vamos determinar a distribuição condicional de $\underline{X}$ dado $T = t$, então para todo ponto $\underline{x} \in A(t)$: $${\mathbb{P}}(\underline{X} = \underline{x}\vert T = t,\theta) = \frac{{\mathbb{P}}(\underline{X} = \underline{x}\vert \theta)}{{\mathbb{P}}(T = t\vert \theta)} = \frac{f\left( \underline{x}\vert \theta \right)}{\sum_{\underline{y} \in A(t)}f\left( \underline{y}\vert \theta \right)}$$ Como $r\left( \underline{y} \right) = t$ para todo ponto $\underline{y} \in A(t)$ e como $\underline{x} \in A(t)$, então vamos ter que: $${\mathbb{P}}(\underline{X} = \underline{x}\vert T = t,\theta) = \frac{u\left( \underline{x} \right)}{\sum_{\underline{y} \in A(t)}u\left( \underline{y} \right)}$$ Finalmente, para todo ponto $\underline{x} \notin A(t)$: $${\mathbb{P}}(\underline{X} = \underline{x}\vert T = t,\theta) = 0$$ Conseguimos ver, então, que a distribuição conjunta de $X$ não depende de $\theta$, mas somente de $T$. Logo, por definição, $T$ é uma estatística suficiente

Agora para fazer a ida, vamos supor que $T$ é uma estatística suficiente. Então para todo valor dado $t$ de $T$, todo ponto $\underline{x} \in A(t)$ e todo valor $\theta \in \Omega$ a probabiidade condicional ${\mathbb{P}}(\underline{X} = \underline{x}\vert T = t,\theta)$ não vai depender de $\theta$ (Como vimos anteriormente), então vai ser da forma: $${\mathbb{P}}(\underline{X} = \underline{x}\vert T = t,\theta) = h\left( \underline{x} \right)$$ Se chamarmos ${\mathbb{P}}(T = t\vert \theta) = v(t,\theta)$, então temos: $$\begin{aligned} {\mathbb{P}}(\underline{X} = \underline{x}\vert \theta) & = {\mathbb{P}}(\underline{X} = \underline{x}\vert T = t,\theta){\mathbb{P}}(T = t\vert \theta) \\ & = u\left( \underline{x} \right)v(t,\theta) \end{aligned}$$ Assim, provamos (Para o caso discreto) que o teorema é válido (Também é válido para o caso contínuo, mas requer métodos diferentes e não será abordado)

Nós vimos anteriormente que, ao calcular a posteriori, ela era proporcional única e excluisivamente ao valor de $\theta$, de forma que tudo que não era relacionado a $\theta$ podia ser movido para a constante de proporcionalidade. Algo parecido ocorre aqui!

**Corolário**

Uma estatística $T = r\left( \underline{X} \right)$ é suficiente **se, e somente se,** não importa qual seja a distribuição a priori, a distribuição a posteriori de $\theta$ depende dos dados única e exclusivamente através do valor de $T$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Estatística Suficiente](../index.md)
- Próximo: [Melhorando um Estimador](../../melhorando-um-estimador/index.md)
