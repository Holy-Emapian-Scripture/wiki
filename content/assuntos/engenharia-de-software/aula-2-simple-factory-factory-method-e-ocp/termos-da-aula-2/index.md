---
layout: "default"
title: "Termos da Aula 2 — Aula 2 - Simple Factory, Factory Method e OCP"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 9
---

[Engenharia de Software](../../index.md) · [Aula 2 - Simple Factory, Factory Method e OCP](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-9"></a>

# Termos da Aula 2

- **Simple Factory** — classe cujo único trabalho é decidir qual objeto concreto criar, tirando essa decisão de quem consome o objeto.

- **Padrão de projeto (design pattern)** — solução clássica e já testada pra um problema recorrente de modelagem orientada a objetos; catalogados no livro do GoF (1994).

- **GoF (Gang of Four)** — apelido dos quatro autores do livro **Design Patterns** (1994).

- **Padrão criacional** — categoria de padrão de projeto que resolve “qual é a forma correta de criar um objeto” (Simple Factory, Factory Method, Builder, Singleton).

- **Factory Method** — cada subclasse decide, via método abstrato sobrescrito, qual objeto concreto criar; substitui o if por polimorfismo.

- **Polimorfismo** — objetos de subclasses diferentes respondem à mesma chamada de método, cada um à sua maneira.

- **OCP (Open/Closed Principle)** — uma classe deve estar fechada para modificação e aberta para extensão; o O do SOLID.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Notas de aula](../../../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Anterior: [Factory Method](../factory-method/index.md)
- Próximo: [Aula 3 - Builder e Singleton](../../aula-3-builder-e-singleton/index.md)
