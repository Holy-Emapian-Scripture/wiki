---
layout: "default"
title: "2.8 Comparação entre arrays e listas encadeadas — 2. Tipos Abstratos de Dados"
tipo: "conteudo"
disciplina: "Estrutura de Dados"
origem: "3 semestre/Estrutura de Dados/Recap/A1.md"
trilha: "../../../../trilhas/estrutura-de-dados/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2025
ordem_na_trilha: 13
---

[Estrutura de Dados](../../index.md) · [2. Tipos Abstratos de Dados](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-13"></a>

# 2.8 Comparação entre arrays e listas encadeadas

Após todo esse código, podemos fazer uma breve comparação entre listas encadeadas e arrays:

- Arrays são uma boa escolha quando há uma estimativa da quantidade de elementos a serem inseridos e permitem acesso rápido a qualquer elemento via índice, mas inserções e remoções no meio são custosas, pois exigem deslocamento de elementos .

- Listas encadeadas são boa escolha quando a quantidade de elementos pode variar significativamente e inserções e remoções são eficientes, pois não exigem deslocamento de elementos, porém, acesso a elementos individuais é mais lento, pois requerem percorrer a lista.

Além disso, embora listas encadeadas sejam flexíveis e eficientes para inserção e remoção, elas possuem algumas desvantagens:

1.  Maior uso de memória por elemento (devido aos ponteiros adicionais);

2.  Não é possivel acessar uma posição aleatória da lista de forma eficiente;

Uma ideia que possibilita o acesso a uma posição aleatória de forma eficiente e melhora a busca linear é ordenar a lista. Mas como fazer isso?

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/estrutura-de-dados/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/estrutura-de-dados/a1.md#apresentacao-original)

- Anterior: [2.7 Lista duplamente encadeada](../lista-duplamente-encadeada/index.md)
- Próximo: [3. Ordenação](../../ordenacao/index.md)
