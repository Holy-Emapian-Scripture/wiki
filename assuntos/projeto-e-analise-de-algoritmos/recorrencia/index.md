---
layout: "default"
title: "Recorrência"
tipo: "conteudo"
disciplina: "Projeto e Análise de Algoritmos"
origem: "4 semestre/Projeto e Análise de Algoritmos/Recaps/A1.md"
trilha: "../../../trilhas/projeto-e-analise-de-algoritmos/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
revisao: "Thalis Ambrosim Falqueto"
ano_original: 2025
ordem_na_trilha: 2
---

[Projeto e Análise de Algoritmos](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-2"></a>

# Recorrência

------------------------------------------------------------------------

Alguns algoritmos são fáceis de terem suas complexidades calculadas, porém, existem casos onde uma função utiliza ela mesma dentro de sua chamada, chamadas de **recursões**.

**Exemplo**

``` cpp
int fatorial(int n) {
  if (n == 1) {
      return 1;
  }
  return n * fatorial(n - 1);
}
```

Aqui, temos um $T(n)$ que chama $T(n - 1)$, até que se chegue no caso base de $n = 1$, como calcular a complexidade disso?

Temos 4 métodos de resolver esse problema:

- **Método da substituição**

- **Método da árvore de recursão**

- **Método da iteração**

- **Método mestre**

<!-- wiki:original:fim -->

## Tópicos desta página

1. [Método da substituição](metodo-da-substituicao/index.md)
2. [Método da árvore de recursão](metodo-da-arvore-de-recursao/index.md)
3. [Método da Recorrência](metodo-da-recorrencia/index.md)
4. [Método mestre](metodo-mestre/index.md)

## Percurso de estudo

[Trilha: A1](../../../trilhas/projeto-e-analise-de-algoritmos/a1.md) · [Apresentação e contexto da fonte](../../../trilhas/projeto-e-analise-de-algoritmos/a1.md#apresentacao-original)

- Anterior: [Notação Assintótica](../notacao-assintotica/index.md)
- Próximo: [Método da substituição](metodo-da-substituicao/index.md)
