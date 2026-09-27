---
layout: "default"
title: "Região Crítica e Testes Estatísticos — Análise e Teste de Hipóteses"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 21
---

[Inferência Estatística](../../index.md) · [Análise e Teste de Hipóteses](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-21"></a>

# Região Crítica e Testes Estatísticos

Considere o problema de testar as hipóteses: $$H_{0}:\theta \in \Omega_{0}\text{\quad\quad}H_{1}:\theta \in \Omega_{1}$$ Seja $\underline{X} = \left\lbrack X_{1},\ldots,X_{n} \right\rbrack$ uma amostra indexada por $\theta$ desconhecido e $S$ o conjunto de **todas as saídas possíveis de** $\underline{X}$. Um estatístico pode especificar um procedimento de teste particionando $S$ em dois grupos, onde $S_{1}$ contém os valores de $\underline{X}$ onde $H_{0}$ será rejeitada e $S_{0}$ os valores que $H_{0}$ não é rejeitada

**Definição: Região Crítica**

O conjunto $S_{1}$ é chamado de **região crítica**

Na maioria dos problemas, $S_{1}$ é definido usando uma estatística $T = r\left( \underline{X} \right)$

**Definição: Estatística de Teste e Região de Rejeição**

Seja $T = r\left( \underline{X} \right)$ uma estatística e $R \subset {\mathbb{R}}$. Suponha que o procedimento de teste das hipóteses seja de forma “Rejeite $H_{0}$ se $T \in R$”, então $T$ é uma **estatística de teste** e $R$ é a **região de rejeição**

Se definirmos o teste em termos de $T$ e $R$ como na definição, então a região crítica é: $$S_{1} ≔ \left\{ \underline{x}\vert r\left( \underline{x} \right) \in R \right\}$$

**Exemplo**

Ainda na linha de raciocínio do exemplo da atividade física pro combate na depressão, vamos supor que definimos o procedimento $\delta$ como:

“Rejeite $H_{0}$ (Correr não afeta os sintomas da depressão) se o número de pessoas com os sintomas afetados for maior que um valor $c$”

Então podemos definir a estatística de teste como $\overline{X}$ e a região de rejeição é $R \subset {\mathbb{R}}$ com os valores reais maiores que $c$. Logo, a região crítica é dada por: $$S_{1} ≔ \left\{ \underline{x}\vert \overline{X} \in R \right\}$$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Hipóteses Nula e Alternativa](../hipoteses-nula-e-alternativa/index.md)
- Próximo: [Função de Poder e Tipos de Erro](../funcao-de-poder-e-tipos-de-erro/index.md)
