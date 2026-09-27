---
layout: "default"
title: "Observações sequenciais e predições — Estatística Bayesiana"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A1.md"
trilha: "../../../../trilhas/inferencia-estatistica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 5
---

[Inferência Estatística](../../index.md) · [Estatística Bayesiana](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Observações sequenciais e predições

Porém, perceba que, até agora, eu vi o caso em que eu tenho todas as amostras de uma vez, porém se, por exemplo, eu quero descobrir se uma vacina é eficaz, isso é inviável, faz muito mas sentido eu ir atualizando minha distribuição conforme recebo mais informações, mas será que isso vai dar a mesma coisa?

Vamos fazer com duas observações condicionalmente independentes, para generalizar se faz analogamente. Como vimos, a posteriori de $\theta$ após eu observar o dado $x_{1}$ se dá como: $$f_{\theta}\left( \theta\vert x_{1} \right) \propto f_{X\vert \theta}\left( x_{1}\vert \theta \right)f_{\theta}(\theta)$$

Agora queremos obter $f_{\theta}\left( \theta\vert x_{1},x_{2} \right)$. Pelo teorema de bayes para várias condicionais, temos que: $$f_{\theta}\left( \theta\vert x_{1},x_{2} \right) \propto f_{\theta}\left( \theta\vert x_{1} \right)f_{X}\left( x_{2}\vert x_{1},\theta \right)$$

Porém, estamos assumindo que eles são condicionalmente independentes, ou seja: $$\begin{array}{r} f_{X}\left( x_{2}\vert \theta,x_{1} \right) = f_{X}\left( x_{2}\vert \theta \right) \\ \Rightarrow f_{\theta}\left( \theta\vert x_{1},x_{2} \right) \\ \propto f_{\theta}\left( \theta\vert x_{1} \right)f_{X}\left( x_{2}\vert \theta \right) \\ \propto f_{\theta}(\theta)f_{X\vert \theta}\left( x_{1}\vert \theta \right)f_{X}\left( x_{2}\vert \theta \right) \\ \propto f_{\theta}(\theta)f_{X\vert \theta}\left( x_{1},x_{2}\vert \theta \right) \end{array}$$

Ou seja, independentemente se eu estou recebendo dado após o outro ou se eu tenho todos de uma vez para trabalhar, o resultado final deve ser o mesmo.

Porém, se voltarmos na equação [\[finding-the-constant\]](../distribuicoes-priori-e-posteriori/index.md#finding-the-constant), podemos perceber algo interessante. Lembra da **Lei da Probabilidade Total**? $${\mathbb{P}}(A) = \sum_{i = 1}^{n}{\mathbb{P}}(B_{i}){\mathbb{P}}(A\vert B_{i})$$ Com $B_{i}$ sendo disjuntos. Porém, temos também a versão contínua do teorema: $$f_{X}(x) = \int_{\Omega}f_{X\vert Y}\left( x\vert y \right)f_{Y}(y)dy$$ Porém, se fizermos algumas substituições, nós obtemos: $$f\left( x_{k}\vert x_{1},\ldots,x_{k - 1} \right) = \int_{\vert \Theta\vert }f\left( x_{k}\vert \theta \right)\xi\left( \theta\vert x_{1},\ldots,x_{k - 1} \right)d\theta$$

Ou seja, podemos utilizar essa equação caso tenhamos $n$ observações e estamos interessados em prever o resultado da próxima observação.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/inferencia-estatistica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a1.md#apresentacao-original)

- Anterior: [Distribuições Priori e Posteriori](../distribuicoes-priori-e-posteriori/index.md)
- Próximo: [Distribuições à Priori Conjugadas](../distribuicoes-a-priori-conjugadas/index.md)
