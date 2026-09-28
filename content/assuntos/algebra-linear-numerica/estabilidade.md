---
layout: "default"
title: "Estabilidade"
tipo: "conteudo"
disciplina: "Álgebra Linear Numérica"
origem: "3 semestre/Álgebra Linear Numérica/Recaps/A1.md"
trilha: "../../../trilhas/algebra-linear-numerica/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 3
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 45
---

[Álgebra Linear Numérica](index.md)

<!-- wiki:original:inicio -->

<a id="secao-54"></a>

# Estabilidade


<a id="definicao-formal-de-o-left-varepsilon-text-machine-right"></a>
<a id="secao-55"></a>

## Definição Formal de $O\left( \varepsilon_{\text{machine}} \right)$

Vou escrever a definição aqui e explicar o que significa logo depois

**Definição**

Dadas as funções $\varphi(t)$ e $\psi(t)$, a sentença $$\varphi(t) = O\left( \psi(t) \right)$$ significa que $\exists C > 0$ tal que $\forall t$ suficientemente próximo de um limite conhecido (por exemplo, $t \rightarrow 0$, $t \rightarrow \infty$), é válido que: $$\varphi(t) \leq C\psi(t)$$

O que isso significa? Significa que, se escrevemos $\varphi(t) = O\left( \psi(t) \right)$, e sabemos para onde $t$ está indo, existe $C > 0$ tal que os valores de $\varphi(t)$ nunca serão maiores que $C\psi(t)$. Na maioria das vezes, eu nem me importo com o que é $C$, só me importo com sua existência!

Falando sobre como estamos tratando $\varepsilon_{\text{machine}}$, o limite implícito aqui é $\varepsilon_{\text{machine }} \rightarrow 0$, e escrever que $\varphi(t) = O\left( \varepsilon_{\text{machine}} \right)$ significa que temos uma constante que limita o erro a uma quantidade de $\varepsilon_{\text{machine}}$, ou seja, o erro nunca será maior que, por exemplo, $3$ vezes $\varepsilon_{\text{machine}}$, $2$ e meio vezes $\varepsilon_{\text{machine}}$.

Podemos fazer uma definição formal mais forte (mas mais confusa) para a notação $O$

**Definição**

Dado $\varphi(s,t)$, temos que: $$\varphi(s,t) = O\left( \psi(t) \right)\text{ uniformemente em }s$$ garante que $\exists!C > 0$ tal que: $$\varphi(s,t) \leq C\psi(t)$$ e isso é válido para qualquer $s$ que eu escolher

É uma definição semelhante, estou apenas adicionando uma variável que posso escolher e que não mudará nada.

Em computadores reais, $\varepsilon_{\text{machine}}$ é um número fixo, então quando estamos trabalhando com o limite implícito $\varepsilon_{\text{machine }} \rightarrow 0$, estamos selecionando uma família **ideal** de computadores!

<a id="dependencia-de-m-e-n"></a>
<a id="secao-56"></a>

## Dependência de $m$ e $n$

Na prática, quando falamos de erros de arredondamento, a estabilidade de algoritmos envolvendo uma matriz $A$ não depende da própria $A$, mas de $m$ e $n$ (suas dimensões). Podemos ver isso analisando o seguinte problema:

Suponha que eu tenha um algoritmo para resolver um sistema não singular $m \times m$ $Ax = b$ para $x$ e garantimos que a solução $\widetilde{x}$ dada pelo algoritmo satisfaz $$\frac{\|\widetilde{x} - x\|}{\| x\|} = O\left( \kappa(A)\varepsilon_{\text{machine}} \right)$$ Isso significa que existe uma constante $C$ que satisfaz $$\|\widetilde{x} - x\| \leq C\kappa(A)\varepsilon_{\text{machine }}\| x\|$$ Isso mostra que, mesmo $C$ não dependendo nem de $A$ nem de $b$, acaba dependendo das dimensões de $A$ porque, se mudarmos $m$ ou $n$, os dados passados para o problema mudam, o que significa que teremos um **novo** problema porque estamos mudando seu domínio e $\kappa(A)$ também mudará se alterarmos suas dimensões!

<a id="independencia-da-norma"></a>
<a id="secao-57"></a>

## Independência da Norma

Você pode ter notado que, quando estamos definindo coisas em estabilidade com normas, denotamos $\| \cdot \|$ como **qualquer** tipo de norma, mas, se escolhermos uma certa norma, a definição pode não ser válida, certo? Como, pode ser válida para $\| \cdot \|_{2}$, mas não para $\| \cdot \|_{3}$, certo? Na verdade, errado! Podemos mostrar que **precisão**, **estabilidade** e **estabilidade retroativa** mantêm suas propriedades para **qualquer** tipo de norma! Isso significa que, quando escolhemos uma norma, podemos escolher uma que facilite os cálculos!

**Teorema**

Para problemas $f$ e seus algoritmos $\widetilde{f}$ em espaços normados de dimensão finita $X$ e $Y$, as propriedades de **precisão**, **estabilidade** e **estabilidade retroativa** são válidas ou não independentemente de qual norma eu escolher para fazer a análise

**Demonstração**

Se provarmos que, se $\| \cdot \|$ e $\| \cdot \|'$ são duas normas em $X$ e $Y$, então $\exists c_{1},c_{2}$ tais que: $$c_{1}\| x\| \leq \| x\|' \leq c_{2}\| x\|$$ então o teorema mostrado antes é válido, porque isso mostra:

1.  Se uma sequência converge ou é muito pequena em uma norma, ela será em todas as outras normas também

2.  Pequenos erros em uma norma serão pequenos em todas as outras normas também

Mas precisamos provar a afirmação anterior, certo? Vamos fazer isso! (O livro apenas diz que é fácil, lol)

Primeiro, vamos reduzir o problema a uma esfera unitária das normas, vamos definir: $$S = \left\{ x \in {\mathbb{C}}^{n}/\| x\| = 1 \right\}$$ esse conjunto é **fechado** porque a norma é **contínua** e é **limitado** (uma esfera, lol). Agora vamos definir a função $f(x) = \| x\|'$, porque $f(x)$ é contínua em ${\mathbb{C}}^{n}$ e $S$ é fechado e limitado, podemos encontrar o **máximo** e o **mínimo** valor de $f$ em $S$, vamos definir:

1.  $m = \min\limits_{x \in S}\| x\|'$

2.  $M = \max\limits_{x \in S}\| x\|'$

$m > 0$ porque $0 \notin S$. Agora, vamos tentar generalizar em ${\mathbb{C}}^{n}$. Se queremos generalizar para todo $x \neq 0 \in {\mathbb{C}}^{n}$, vamos escrever: $$x = \| x\|\left( \frac{x}{\| x\|} \right)$$ Você pode ver claramente que $\frac{x}{\| x\|} \in S$ porque $\|\frac{x}{\| x\|}\| = 1$. Então, vamos ver o que acontece se tomarmos $\| x\|'$: $$\| x\|' = \|\| x\|\left( \frac{x}{\| x\|} \right)\|' = \| x\|\|\frac{x}{\| x\|}\|'$$ Se você olhar de perto, $\frac{x}{\| x\|}$ é um vetor em $S$, isso significa que $\|\frac{x}{\| x\|}\|' \in \lbrack m,M\rbrack$ e, por causa de $\| x\|$ (número escalar positivo), podemos ver que $$\| x\|\|\frac{x}{\| x\|}\|' \in \left\lbrack \| x\| m,\| x\| M \right\rbrack$$ Podemos reescrever isso como $$m\| x\| \leq \| x\|' \leq M\| x\|$$ Isso significa que essas duas constantes existem e provam o teorema estabelecido antes

<a id="estabilidade-da-aritmetica-de-ponto-flutuante"></a>
<a id="secao-58"></a>

## Estabilidade da Aritmética de Ponto Flutuante

**Teorema**

As operações $\oplus$, $\ominus$, $\otimes$ e $⨸$ são **estáveis retroativamente**

**Demonstração**

Defina $\circledast$ como qualquer uma das 4 operações mostradas antes. Dado um problema $f:X \rightarrow Y$ que está calculando $x_{1} \ast x_{2}$, o algoritmo $\widetilde{f}$ para resolver esse problema é $\widetilde{f}(x) = \text{ fl}\left( x_{1} \right) \circledast \text{ fl}\left( x_{2} \right)$ onde $x = \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix}$.

Temos que: $$\widetilde{f}(x) = \text{ fl}\left( x_{1} \right) \circledast \text{ fl}\left( x_{2} \right)$$ $$= \left( \text{fl}\left( x_{1} \right) \ast \text{ fl}\left( x_{2} \right) \right)\left( 1 + \varepsilon_{3} \right)$$ $$= \left( x_{1}\left( 1 + \varepsilon_{1} \right) \ast x_{2}\left( 1 + \varepsilon_{2} \right) \right)\left( 1 + \varepsilon_{3} \right)$$ $$= x_{1}\left( 1 + \varepsilon_{1} \right)\left( 1 + \varepsilon_{3} \right) \ast x_{2}\left( 1 + \varepsilon_{2} \right)\left( 1 + \varepsilon_{3} \right)$$ $$= x_{1}\left( 1 + \varepsilon_{4} \right) \ast x_{2}\left( 1 + \varepsilon_{5} \right)$$

Onde $\varepsilon_{4} = O\left( \varepsilon_{\text{machine}} \right)$ e $\varepsilon_{5} = O\left( \varepsilon_{\text{machine}} \right)$. Calculamos $\widetilde{f}(x)$, agora vamos ver $f\left( \widetilde{x} \right)$. Primeiro, vamos definir: $$\widetilde{x} = \begin{pmatrix} x_{1}\left( 1 + \varepsilon_{4} \right) \\ x_{2}\left( 1 + \varepsilon_{5} \right) \end{pmatrix}$$

Se definirmos $\widetilde{x}$ assim, podemos ver claramente que $$f\left( \widetilde{x} \right) = x_{1}\left( 1 + \varepsilon_{4} \right) + x_{2}\left( 1 + \varepsilon_{5} \right) = \widetilde{f}(x)$$

Mas a condição $\frac{\|\widetilde{x} - x\|}{\| x\|} = O\left( \varepsilon_{\text{machine}} \right)$ é satisfeita? $$\frac{\|\widetilde{x} - x\|}{\| x\|} = \frac{\|\begin{pmatrix} x_{1}\left( 1 + \varepsilon_{4} \right) \\ x_{2}\left( 1 + \varepsilon_{5} \right) \end{pmatrix} - \begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix}\|}{\|\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix}\|} = \frac{\|\begin{pmatrix} x_{1}\varepsilon_{4} \\ x_{2}\varepsilon_{5} \end{pmatrix}\|}{\|\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix}\|}$$ Usando a norma 1 $$\frac{x_{1}\varepsilon_{4} + x_{2}\varepsilon_{5}}{x_{1} + x_{2}} = \frac{x_{1}O\left( \varepsilon_{\text{machine}} \right) + x_{2}O\left( \varepsilon_{\text{machine}} \right)}{x_{1} + x_{2}} = \frac{\left( x_{1} + x_{2} \right)O\left( \varepsilon_{\text{machine}} \right)}{x_{1} + x_{2}} = O\left( \varepsilon_{\text{machine}} \right)$$

Isso mostra que $\oplus$, $\ominus$, $\otimes$ e $⨸$ são **estáveis retroativamente**

<a id="precisao-de-um-algoritmo-estavel-retroativamente"></a>
<a id="secao-59"></a>

## Precisão de um Algoritmo Estável Retroativamente

Falamos de números de condição antes da estabilidade, vamos tentar associar ambos!

**Teorema**

Suponha que um algoritmo estável retroativamente $\widetilde{f}$ é aplicado para um problema $f:X \rightarrow Y$ com número de condição $\kappa$ em um computador que satisfaz [teorema da conversão para ponto flutuante](aritmetica-de-ponto-flutuante.md#floating_point_conversion) e [axioma fundamental da aritmética de ponto flutuante](aritmetica-de-ponto-flutuante.md#fundamental_axiom_of_floating_point_arithmetic), então, o erro relativo satisfaz: $$\frac{\|\widetilde{f}(x) - f\left( \widetilde{x} \right)\|}{\| f\left( \widetilde{x} \right)\|} = O\left( \kappa(x)\varepsilon_{\text{machine}} \right)$$

**Demonstração**

Por definição, temos $\widetilde{f}(x) = f(x + \delta x)$ com $\frac{\|\delta x\|}{\| x\|} = O\left( \varepsilon_{\text{machine}} \right)$. Usando [número de condição relativo](condicionamento-e-numeros-de-condicao.md#relative_condition_number) (Número de Condição Relativo), temos que: $$\kappa(x) = \lim\limits_{\delta x \rightarrow 0}\left( \frac{\| f(x + \delta x) - f(x)\|}{\| f(x)\|} \right)\left( \frac{\| x\|}{\|\delta x\|} \right)$$ $$\kappa(x) = \lim\limits_{\delta x \rightarrow 0}\left( \frac{\|\widetilde{f}(x) - f(x)\|}{\| f(x)\|}\frac{\| x\|}{\|\delta x\|} \right)$$

Usando algumas definições formais (nem eu entendo, então se tentar explicar aqui, só perderei tempo, lol), podemos reescrever isso como: $$\frac{\|\widetilde{f}(x) - f(x)\|}{\| f(x)\|} \leq \left( \kappa(x) + o(1) \right)\frac{\|\delta x\|}{\| x\|}$$

Onde $o(1) \rightarrow 0$ quando $\varepsilon_{\text{machine }} \rightarrow 0$

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: A1](../../trilhas/algebra-linear-numerica/a1.md) · [Apresentação e contexto da fonte](../../trilhas/algebra-linear-numerica/a1.md#apresentacao-original)

- Anterior: [Aritmética de Ponto Flutuante](aritmetica-de-ponto-flutuante.md)
