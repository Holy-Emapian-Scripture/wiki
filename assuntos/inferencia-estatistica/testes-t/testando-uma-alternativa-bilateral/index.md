---
layout: "default"
title: "Testando uma alternativa bilateral — Testes $t$"
tipo: "conteudo"
disciplina: "Inferência Estatística"
origem: "4 semestre/Inferência Estatística/Recaps/A2.md"
trilha: "../../../../trilhas/inferencia-estatistica/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 32
---

[Inferência Estatística](../../index.md) · [Testes $t$](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-32"></a>

# Testando uma alternativa bilateral

**Exemplo**

Vamos retomar o [\[length-fibers-example\]](../propriedades-dos-testes-t/index.md#length-fibers-example), mas agora vamos alterar as hipóteses para: $$H_{0}:\mu = 5.2,\text{\quad\quad}H_{1}:\mu \neq 5.2$$

Assumiremos novamente que os comprimentos de 15 fibras são medidos, e que o valor de $U$, calculado a partir dos valores observados, é 1,833. Testaremos as hipóteses ao nível de significância $\alpha_{0} = 0.05$.

Como $\alpha_{0} = 0.05$, nosso valor crítico será o quantil $1 - \frac{0.05}{2} = 0.975$ da distribuição **$t$** com $14$graus de liberdade. Pela tabela das distribuições **$t$** deste livro, encontramos $$T_{14}^{- 1}(0.975) = 2.145.$$

Assim, o teste **t** especifica a rejeição de $H_{0}$ se $U \leq - 2.145$ ou se $U \geq 2.145$. Como $U = 1.833$, a hipótese $H_{0}$ **não** seria rejeitada.

Os valores numéricos nos exemplos enfatizam a importância de decidir se a hipótese alternativa apropriada em um dado problema é unilateral (**one-sided**) ou bilateral (**two-sided**). Quando as hipóteses do [\[length-fibers-example\]](../propriedades-dos-testes-t/index.md#length-fibers-example) foram testadas ao nível de significância $0.05$, a hipótese nula $H_{0}$, de que $\mu \leq 5.2$, foi rejeitada. Quando as hipóteses desse exemplo foram testadas ao mesmo nível de significância, utilizando os mesmos dados, a hipótese nula $H_{0}$, de que $\mu = 5.2$, não foi rejeitada.

**Teorema: Função de poder de testes $t$ bilaterais**

A função de poder do teste $\delta$ que rejeita $H_{0}:\mu = \mu_{0}$ quando $\vert U\vert  \geq c$, onde $c = T_{n - 1}^{- 1}\left( 1 - \alpha_{0}/2 \right)$ pode ser encontrada utilizando a distribuição $t$ não-central. Se $\mu \neq \mu_{0}$, então $U$ tem distribuição $t$ não-central com $n - 1$ graus de liberdade e parâmetro de não-centralidade $\psi = \sqrt{n}(\mu - \mu_{0})/\sigma$. A função de poder é: $$\pi(\mu,\sigma^{2}\vert \delta) = T_{n - 1}\left( - c\vert \psi \right) + 1 - T_{n - 1}\left( c\vert \psi \right)$$

**Teorema: $p$-valores de testes $t$ bilaterais**

Suponha que estamos testando as hipóteses bilaterais $H_{0}:\mu = \mu_{0}$, $H_{1}:\mu \neq \mu_{0}$. Seja $u$ o valor observado da estatística $U$ e seja $T_{n - 1}( \cdot )$ a cdf de uma $t_{n - 1}$. Então o $p$-valor é $2\left\lbrack 1 - T_{n - 1}\left( \vert u\vert  \right) \right\rbrack$

**Demonstração**

Deixe $T_{n - 1}^{- 1}( \cdot )$ denotar a função quantil da $t_{n - 1}$. Nós rejeitariamos a hipótese nula no nível $\alpha_{0}$ se, e somente se, $\vert u\vert  \geq T_{n - 1}^{- 1}\left( 1 - \alpha_{0}/2 \right)$ que é equivalente a $T_{n - 1}\left( \vert u\vert  \right) \geq 1 - \alpha_{0}/2$ que é equivalente a $\alpha_{0} \geq 2\left\lbrack 1 - T_{n - 1}\left( \vert u\vert  \right) \right\rbrack$

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/inferencia-estatistica/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/inferencia-estatistica/a2.md#apresentacao-original)

- Anterior: [Teste $t$ pareado](../teste-t-pareado/index.md)
- Próximo: [Testes $t$ como testes de razão de verossimilhança](../testes-t-como-testes-de-razao-de-verossimilhanca/index.md)
