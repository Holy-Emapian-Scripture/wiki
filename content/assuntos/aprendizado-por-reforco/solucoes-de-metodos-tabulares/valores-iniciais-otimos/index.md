---
layout: "default"
title: "Valores Iniciais Ótimos — Soluções de métodos tabulares"
tipo: "conteudo"
disciplina: "Aprendizado por Reforço"
origem: "Mestrado/Aprendizado por Reforço/Recap.md"
trilha: "../../../../trilhas/aprendizado-por-reforco/revisao-geral.md"
nav_exclude: true
render_with_liquid: false
grupo: "Mestrado"
autores: ["Thalis Ambrosim Falqueto", "João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 15
---

[Aprendizado por Reforço](../../index.md) · [Soluções de métodos tabulares](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Valores Iniciais Ótimos

Todos os métodos discutidos até agora tem uma forte dependência nas estimativas iniciais de recompensa $Q_{1}(a)$. Na linguagem estatística, esses métodos são chamados de $\text{enviesados}$ por suas estimativas iniciais de recompensa. Para métodos que calculam a estimativa pela [\[mediaamostral\]](../implementacao-incremental/index.md#mediaamostral) usando $\alpha_{n}(a) = \frac{1}{n}$, chegamos na fórmula [\[umsobreeni\]](../implementacao-incremental/index.md#umsobreeni), e, após a primeira estimativa, nosso $Q_{n}(a)$ não depende mais diretamente de $Q_{1}$, ou seja, ele não é mais enviesado. Já com outro $\alpha$, no caso, chegamos na fórmula [\[alpha\]](../monitorando-um-problema-nao-estacionario/index.md#alpha), que é diretamente enviesado por $Q_{1}$.

Um enviesamento pode ser bom ou ruim. Suponha que em vez de iniciar a estimativa inicial $Q_{1}(a) = 0$, como fazemos anteriormente, considere que colocaremos todos como $+ 5$(lembre que estávamos usando $q \ast (a) \sim {\mathbb{N}}(0,1)$, ou seja, uma estimativa desse tamanho é bem otimista). Esse otimismo encoraja o agente a explorar, já que de início, todas as estimativas são mais altas do que qualquer valor real da ação. Então, ao escolher certa ação, o agente recebe uma recompensa menor do que o esperado, ficando desapontado e diminuindo o valor da recompensa esperada. Ao escolher a próxima ação, todas as outras têm uma estimativa maior do que a primeira selecionada. Assim, o sistema fará explorará todas as ações, mesmo se sempre selecionarmos a mais gananciosa sempre.

Nós chamamos essa estratégia de Valores Iniciais Ótimos. Vamos comparar esse método com o método $\varepsilon$-greedy explicados anteriormente:

![Efeito da inicialização otimista do valor da ação no banco de teste de 10 braços. Ambos usaram o step-size $\alpha = 0.1$](../../assets/acaootimista.png)

*Figura 5. Efeito da inicialização otimista do valor da ação no banco de teste de 10 braços. Ambos usaram o step-size $\alpha = 0.1$*

Note como o método otimista começa pior, pois o agente fica inicialmente apenas explorando várias ações, mas eventualmente performa melhor porque acaba parando de explorar. Essa estratégia pode ser boa às vezes, mas não é a mais adequada em casos não estacionários(valor das ações muda) pois a exploração de outras ações é temporário. Em geral, qualquer método que depende fortemente de condições iniciais não são muito bons para métodos não estacionários.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Revisão geral](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-por-reforco/revisao-geral.md#apresentacao-original)

- Anterior: [Monitorando um problema não estacionário](../monitorando-um-problema-nao-estacionario/index.md)
- Próximo: [Seleção de Ação por Nível Superior de Confiança](../selecao-de-acao-por-nivel-superior-de-confianca/index.md)
