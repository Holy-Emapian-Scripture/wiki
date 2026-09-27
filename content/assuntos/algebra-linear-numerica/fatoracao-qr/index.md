---
layout: "default"
title: "Fatoração QR"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 20
---

[Álgebra Linear Numérica](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-20"></a>

# Fatoração QR

------------------------------------------------------------------------

A assustadora, a parte em que ninguém sabe de nada! Vamos nos acalmar e ver tudo com paciência.

Como funciona essa fatoração? Queremos expressar $A$ como: $$A = QR$$

Com $Q$ sendo uma matriz ortogonal e $R$ uma matriz triangular superior. Mas por que eu gostaria de fazer tal coisa? O principal motivo é resolver sistemas lineares! Vamos pegar o sistema $b = Ax$, reescrevemo-lo como $$b = QRx \Leftrightarrow Q^{\ast}b = Rx \Leftrightarrow c = Rx$$ Temos um sistema equivalente, e este é um sistema **triangular**, ou seja, um sistema trivial para nós e para um computador resolverem!

<!-- wiki:original:fim -->

## Tópicos desta página

1. [A ideia da fatoração reduzida](a-ideia-da-fatoracao-reduzida/index.md)
2. [Fatoração QR completa](fatoracao-qr-completa/index.md)
3. [Ortonormalização de Gram-Schmidt](ortonormalizacao-de-gram-schmidt/index.md)
4. [Existência e unicidade](existencia-e-unicidade/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Projeção em base arbitrária](../projetores/projecao-em-base-arbitraria/index.md)
- Próximo: [A ideia da fatoração reduzida](a-ideia-da-fatoracao-reduzida/index.md)
