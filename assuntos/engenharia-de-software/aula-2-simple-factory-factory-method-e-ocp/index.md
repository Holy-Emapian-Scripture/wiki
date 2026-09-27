---
layout: "default"
title: "Aula 2 - Simple Factory, Factory Method e OCP"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 6
---

[Engenharia de Software](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-6"></a>

# Aula 2 - Simple Factory, Factory Method e OCP

A solução da `Loja2` ([\[cod-aula1\]](../aula-1-documentacao-contratos-e-srp/loja-exercicio-de-correcao/index.md#cod-aula1)) resolveu o SRP, mas o `if centro == ...` continua dentro de `processar`, decidindo qual `Frete` instanciar ainda hardcoded, ainda fazendo verificação de string, o que ainda é problema mesmo depois do SRP resolvido (Professor disse que deixar essas verificações em string é um crime, mas não vem ao caso). Some a isso uma regra de negócio nova: a loja quer simular o frete antes da compra, não só calculá-lo depois que o cliente já decidiu comprar, e passa a atender mais centros de distribuição. Dessa forma, agora, vários lugares diferentes vão precisar da mesma lógica de “qual frete usar para este centro”, e ela está presa dentro de `Loja2`.

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Simple Factory](simple-factory/index.md)
2. [Factory Method](factory-method/index.md)
3. [Termos da Aula 2](termos-da-aula-2/index.md)

## Percurso de estudo

[Trilha: Notas de aula](../../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Anterior: [Termos da Aula 1](../aula-1-documentacao-contratos-e-srp/termos-da-aula-1/index.md)
- Próximo: [Simple Factory](simple-factory/index.md)
