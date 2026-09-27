---
layout: "default"
title: "3.1 - Características relevantes: — 3. Ordenação"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 15
---

[Estrutura de Dados](../../index.md) · [3. Ordenação](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# 3.1 - Características relevantes:

A utilidade dos algoritmos de ordenação que vamos ver podem ser medidos através de:

- Complexidade de tempo de execução;

- Complexidade de espaço utilizado: quantidade de espaço adicional de memória necessária (além do array de entrada);

- Estabilidade: se mantém a ordem relativa dos elementos iguais na entrada;

  - Exemplo: No caso do exemplo do hospital, se cada elemento(pessoa) tem uma prioridade, é esperado que pessoas de mesma prioridade continuem na mesma ordem que chegaram. Portanto, ao ordenar pela prioridade, o algoritmo é estável se cada elemento de mesma prioridade se mantém na mesma ordem antes de ordenar.

- In-place vs Out-of-place:

  - In-place: Não requer memória extra significativa.

  - Out-of-place: Requer uma estrutura auxiliar para armazenar os elementos ordenados;

- Performance em diferentes tamanhos de entrada: Alguns algoritmos podem ser melhores que outros para quantidades pequenas ou grandes de dados.

Existem outros tipos de características relevantes, como adaptabilidade e paralelização, mas não serão abordados aqui. Legal, vamos para os algoritmos!

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [3. Ordenação](../index.md)
- Próximo: [3.2 Selection Sort](../selection-sort/index.md)
