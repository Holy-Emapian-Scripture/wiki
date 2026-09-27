---
layout: "default"
title: "Anexação Uniforme — Evoluções de Redes"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A1.md"
trilha: "../../../../trilhas/ciencia-de-redes/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 12
---

[Ciência de Redes](../../index.md) · [Evoluções de Redes](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-16"></a>

# Anexação Uniforme

Vamos imaginar uma **anexação uniforme**. Nesse caso, cada nó inserido sempre terá um grau de $m$. Ou seja, a **probabilidade** de um link do meu novo nó inserido se interligar ao vértice $v_{i}$ é igual a $m/i$ (A chance de ele se ligar com uma das arestas é $1/i$, logo, como eu posso me ligar com $m$ arestas diferentes, todas independentes entre si, a probabilidade total vai ser $m/i$), logo: $$\delta(v_{j},t = i) ≔ \text{ Grau de }v_{j}\text{ no momento }i$$ Com isso, podemos interpretar esse grau como uma **variável aleatória**. Temos que o grau de $v_{i}$ no momento inicial $i$ é fixa como $m$. Então a quantidade de arestas no momento $i + 1$ pode ser escrita como: $$\delta(v_{i},i + 1) = m + {\mathbb{I}}_{i + 1}(1) + {\mathbb{I}}_{i + 1}(2) + \ldots + {\mathbb{I}}_{i + 1}(m)$$ Onde ${\mathbb{I}}_{j}(k)$ é a variável indicadora que diz se, no momento $j$, a aresta $k$ do **novo nó que está sendo adicionado na rede** foi adicionado ou não no nosso nó. Podemos reescrever como a soma de uma única variável aleatória de distribuição binomial também. Você pode ter reparado que eu utilizei $i$ tanto no $v_{i}$ quanto no $i$. Vou utilizar isso pois eu estou supondo que, na nossa análise, estamos saindo do último nó adiconado (Uma aproximação razoável do modelo real, obviamente que nem todos os nós vão ser adicionados com essa anexação, já que antes de eu iniciar essa abordagem, já vai ter uma rede “preexistente”)

Porém, queremos ter uma **noção** de como isso vai ser ao longo prazo, podemos então tirar a esperança disso. $${\mathbb{E}}\left\lbrack \delta(v_{i},i + 1) \right\rbrack = m + \frac{m}{i}$$ Porém, isso é apenas para um único passo, queremos generalizar para vários passos. Vamos supor então que estamos saindo do $i$-ésimo nó adiconado e estamos no momento $t$: $$\delta(v_{i},t) = m + \sum_{k = i + 1}^{t}\sum_{j = 1}^{m}{\mathbb{I}}_{k}(j)$$ $$\begin{aligned} {\mathbb{E}}\left\lbrack \delta(v_{i},t) \right\rbrack & = m + \sum_{k = i + 1}^{t}\sum_{j = 1}^{m}{\mathbb{E}}\left\lbrack {\mathbb{I}}_{k}(j) \right\rbrack \\ & = m + \sum_{k = i + 1}^{t}\sum_{j = 1}^{m}\frac{j}{k - 1} \end{aligned}$$

$$\begin{array}{r} {\mathbb{E}}\left\lbrack \delta(v_{i},t) \right\rbrack = m \cdot \sum_{k = i + 1}^{t}\frac{1}{k - 1} \\ {\mathbb{E}}\left\lbrack \delta(v_{i},t) \right\rbrack \approx m + m\ln(\frac{t - 1}{i - 1}) \\ {\mathbb{E}}\frac{\left\lbrack \delta(v_{i},t) \right\rbrack}{m} - 1 \approx \ln(\frac{t - 1}{i - 1}) \\ \exp(\frac{{\mathbb{E}}\left\lbrack \delta(v_{i},t) \right\rbrack - m}{m}) \approx \frac{t - 1}{i - 1} \\ \exp(\frac{- \left( {\mathbb{E}}\left\lbrack \delta(v_{i},t) \right\rbrack - m \right)}{m}) \approx \frac{i - 1}{t - 1} \\ \exp(\frac{- \left( {\mathbb{E}}\left\lbrack \delta(v_{i},t) \right\rbrack - m \right)}{m}) \approx \frac{i}{t} \end{array}$$

No intervalo $\lbrack 0,t\rbrack$, temos a seguinte estruturação:

![Intervalo de $i/t$](../../assets/01-interval.png)

*Figura 5. Intervalo de $i/t$*

Então, o que encontramos foi a fração de nós que tem grau maior que $v_{i}$. Então temos que: $${\mathbb{P}}(\delta_{t}\left( v_{i} \right) \leq k) = 1 - e^{\frac{- (k - m)}{m}}$$ Logo, temos uma distribuição **Exponencial**

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../trilhas/ciencia-de-redes/a1.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a1.md#apresentacao-original)

- Anterior: [Evoluções de Redes](../index.md)
- Próximo: [Anexação Preferencial](../anexacao-preferencial/index.md)
