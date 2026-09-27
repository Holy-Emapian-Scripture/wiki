---
layout: "default"
title: "p-valor — Análise e Teste de Hipóteses"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 24
---

[Inferência Estatística](../../index.md) · [Análise e Teste de Hipóteses](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-24"></a>

# p-valor

**Definição: p-valor**

O p-valor é o menor nível $\alpha_{0}$ ao qual rejeitaríamos a hipótese nula no nível $\alpha_{0}$ **com os dados observados**. Também chamamos o p-valor de **nível de significância observado**

É o que, macho? Essa definição está muito objetiva e densa, então simplificando um pouco: p-valor é a **probabilidade** de se obter o padrão de resultados que encontramos no nosso estudo ou resultados mais extremos, **considerando a hipótese nula como verdadeira**. Vamos supor que observamos uma amostra $\underline{x}$ e não fixamos um valor $\alpha$ para rejeitarmos $H_{0}$, então nos perguntamos “Qual é o menor nível para o qual esses dados ainda seriam considerados extremos o suficiente para rejeitar $H_{0}$?”. Então o $p$-valor segue uma linha diferente do procedimento de teste estabelecido anteriormente. Original:

- Escolhemos um nível $\alpha$

- Define-se a **região crítica** associada a esse $\alpha$

- Calcula-se a estatística de teste

- Verificamos se ela cai na região crítica

Agora nós invertemos a lógica

- Em vez de fixar um $\alpha$, vamos perguntar “rejeito ou não?”

- Fixamos os dados

- Para quais valores de $\alpha$ eu rejeitaria? O menor desses será meu $p$-valor

Mas por que essa definição é útil? Usamos isso pois, se eu faço um teste em um nível $\alpha_{0}$ e rejeito $H_{0}$, simplesmente dizer que rejeitei $H_{0}$ no nível $\alpha_{0}$ parece vago. Isso não diz o quão perto estávamos de tomar a outra decisão.

Um experimentador que rejeita a hipótese nula $\Leftrightarrow$ o p-valor é no máximo $\alpha_{0}$, está usando um teste de significância $\alpha_{0}$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Induzindo um nível de significância](../induzindo-um-nivel-de-significancia/index.md)
- Próximo: [Calculando p-valores](../calculando-p-valores/index.md)
