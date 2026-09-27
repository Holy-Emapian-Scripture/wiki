---
layout: "default"
title: "Como um fato se organiza? — Data Warehouses"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A1.md"
trilha: "../../../../trilhas/modelagem-informacional/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 7
---

[Modelagem Informacional](../../index.md) · [Data Warehouses](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Como um fato se organiza?

Uma tabela de fatos tem:

- Chaves-estrangeiras conectando a tabela de fato para as tabelas de dimensões

- As medidas relacionadas ao sujeito da análise

![Exemplo do Esquema Estrela nas lojas zagi](../../assets/zagi-stores-star-schema.png)

*Figura 8. Exemplo do Esquema Estrela nas lojas zagi*

Os principais pontos a se destacar é que, no modelo estrela, nós não colocamos o **id** do modelo relacional como a chave-primária da dimensão. Por quê? Por conta que **não há normalização**, por conta disso, podem aparecer chaves-primárias repetidas, algo que **não pode acontecer**. Então criamos as **chaves substitutas** (Surrogate keys), que são chaves que não se repetem na tabela de dimensão (Não são as mesmas chaves do modelo transacional). Porém, o mesmo não acontece na tabela de fatos, ela não possui uma surrogate key, então o que diferencia um fato dos demais?

![Exemplo correto do modelo dimensional das lojas zagi](../../assets/zagi-store-correct-star-schema.png)

*Figura 9. Exemplo correto do modelo dimensional das lojas zagi*

Podemos ter algumas abordagens **arbitrárias** para identificar os fatos. Por exemplo, na imagem acima, nós diferenciamos dois fatos pelo **id da transação** e pela **surrogate key** do produto, já que um produto comprado só pode estar associado a **uma única transação**. Eu também poderia identificar um fato utilizando uma **chave composta** das **chaves-estrangeiras** das dimensões (Tem alguns problemas e questionamentos para esse exemplo em específico, mas vamos supor que não precisa de alterações a mais)

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/modelagem-informacional/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/modelagem-informacional/a1.md#apresentacao-original)

- Anterior: [Star Schema](../star-schema/index.md)
- Próximo: [Galáxia de Estrelas](../galaxia-de-estrelas/index.md)
