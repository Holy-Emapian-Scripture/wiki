---
layout: "default"
title: "Usos de GNNs — Graph Neural Networks"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 16
---

[Aprendizado de Máquina](../../index.md) · [Graph Neural Networks](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-19"></a>

# Usos de GNNs

**Classificação de nós**. Seja $\mathcal{Y} = \left\{ 1,\ldots,L \right\}$ um conjunto finito de classes, $G = (V,E)$ um grafo e $V_{l} \subseteq V$ um subconjunto de nós anotados com classes em $\mathcal{Y}$. Classificacão de nós consiste no problema de classificar os nós em $V_{l}^{c} = V\backslash V_{l}$. Como exemplo, sistemas de detecção de fraude na Internet objetivam verificar a legitimidade da identidade de usuários; para isso, esses sistemas binariamente classificam como legítimo ou fraudulento os nós de uma rede de pessoas que interagem com alguma interface on-line. Existem duas diferenças essenciais entre classificação de nós em um grafo e os cenários canônicos de classificação em problemas de aprendizado supervisionado. Primeiro, supomos que o grafo, e logo seus nós/amostras, é inteiramente observado e que apenas não conhecemos as classes de algum subconjunto dos nós; em contraste, métodos convencionais de classificação não permitem a classificação de amostras não observadas durante o treinamento do modelo —i.e., classificação de nós costuma ser uma tarefa transdutiva, enquanto métodos convencionais focam em aprendizado indutivo. Segundo, as amostras em um grafo são intrinsecamente correlacionadas e então descumprem a típica suposição de independência distribucional assumida pelos métodos historicamente relevantes de classificação - como os modelos lineares; essa inconsistência explica a efetiva inutilidade destes métodos à classificação de nós em grafos e, no passado, incentivou o desenvolvimento de procedimentos que incorporam a estrutura correlacional das amostras em seus mecanismos de inferência. Circunstancialmente, as GNNs exploram a correlação induzida nas amostras pelo seu grafo subjacente e as informações não estruturais para classificar os nós não anotados em um grafo.

**Inferência relacional (predição de aresta)**. Seja $G = (V,E)$ um grafo e suponha que observamos o grafo parcial $\hat{G} = \left( V,\hat{E} \right)$ com $\hat{E} \subset E$; o objetivo da inferência relacional é identificar as arestas (relações) não observadas $\begin{array}{r} E \\ \hat{E} \end{array}$. Por exemplo, a estimativa da probabilidade de que um par de indivíduos se conhece em uma mídia social é crucial para aumentar o engajamento dos usuários com a plataforma e corresponde a uma instanciação do problema de inferência relacional. Em outra direção, a descrição de como as diferentes proteínas interagem para permitir o desenvolvimento de um organismo é um dos problemas fundacionais de biologia molecular e é equivalente à predição de arestas no grafo de interação entre proteínas (chamado de interatoma). Enfaticamente, a inferência relacional, como a classificação de nós, transcende as fronteiras dos algoritmos tradicionais de aprendizagem de máquina ao exigir o tratamento de amostras correlacionadas para identificar as arestas prováveis em um espaço combinatoriamente grande de arestas possíveis. Em contraste, as GNNs eficientemente utilizam a topologia da rede e os atributos dos nós para precisamente inferir a existência de arestas de G não observadas em $\hat{G}$.

**Classificação e regressão de grafos**. Alguns problemas exigem o tratamento de bases de dados relacionais em que as instâncias são objetos representados como grafos. O químico que almeja enumerar os efeitos colaterais de determinado medicamento, por exemplo, está tipicamente equipado com um conjunto de outros medicamentos com efeitos colaterais metabolicamente reconhecíveis; e cada medicamento é epistemicamente representado por uma estrutura molecular equivalente a um grafo. Esta categoria de problemas de inferência em grafos é a mais similar e receptiva à abordagem tradicional de aprendizagem de máquina; neste caso, cada grafo corresponde a uma amostra independente e presumivelmente identicamente distribuída as outras. A dificuldade incide na geração de representações vetoriais suficientemente informativas dos grafos para maximizar a eficácia de procedimentos de classificação e de regressão subsequentemente aplicados a estas representações. Notadamente, as redes neurais para grafos naturalmente aprendem representações latentes dos nós que podem ser sucessivamente agregadas e então exploradas em algoritmos de inferência canônicos de aprendizagem de máquina.

![Representação visual de cada um dos três usos de GNNs discutidos](../../assets/gnn-uses.png)

*Figura 3. Representação visual de cada um dos três usos de GNNs discutidos*

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Notações](../notacoes/index.md)
- Próximo: [Passagem de Mensagem](../passagem-de-mensagem/index.md)
