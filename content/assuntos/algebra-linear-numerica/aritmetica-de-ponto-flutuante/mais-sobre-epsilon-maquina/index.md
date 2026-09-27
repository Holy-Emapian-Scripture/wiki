---
layout: "default"
title: "Mais sobre Épsilon Máquina — Aritmética de Ponto Flutuante"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 44
---

[Álgebra Linear Numérica](../../index.md) · [Aritmética de Ponto Flutuante](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-53"></a>

# Mais sobre Épsilon Máquina

Agora podemos redefinir $\varepsilon_{\text{machine}}$! Mas por quê? Bem, queremos torná-lo o menor possível, e às vezes aumentar a precisão não é uma opção:

**Definição**

$\varepsilon_{\text{machine}}$ é o menor valor tal que [\[floating_point_conversion\]](../epsilon-maquina/index.md#floating_point_conversion) e [\[fundamental_axiom_of_floating_point_arithmetic\]](../aritmetica-de-ponto-flutuante/index.md#fundamental_axiom_of_floating_point_arithmetic) são válidos

Isso implica que, para alguns computadores, $\varepsilon_{\text{machine}}$ pode ser ainda menor que $\frac{1}{2}\beta^{1 - t}$, o que é uma coisa **muito** boa!

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Aritmética de Ponto Flutuante](../aritmetica-de-ponto-flutuante/index.md)
- Próximo: [Estabilidade](../../estabilidade/index.md)
