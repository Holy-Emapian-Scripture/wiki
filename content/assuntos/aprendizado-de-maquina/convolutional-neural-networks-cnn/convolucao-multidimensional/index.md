---
layout: "default"
title: "Convolução Multidimensional — Convolutional Neural Networks (CNN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 26
---

[Aprendizado de Máquina](../../index.md) · [Convolutional Neural Networks (CNN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-30"></a>

# Convolução Multidimensional

Até o momento, falamos das operações em matrizes bidimensionais ($2$ valores), porém, a maioria das imagem são coloridas, então teríamos 3 matrizes, uma para cada canal de cor. Expandir essa operação para múltiplos canais é relativamente simples. Se minha imagem $I$ tem dimensões $H \times W \times C$ (altura, largura e quantidade de canais) e o filtro $K$ tem dimensões $M \times M \times C$, eu vou utilizar cada feature map $M \times M$ com seu respectivo canal da imagem, e somar os resultados. A feature map resultante terá dimensões $(H - M + 1) \times (W - M + 1)$, e cada valor de ativação representará a presença de um padrão específico na região correspondente da imagem, considerando todos os canais de cor. Essa operação é chamada de **convolução multidimensional** e é fundamental para o processamento de imagens coloridas em CNNs.

![Representação visual da operação de convolução multidimensional](../../assets/multidimensional-convolution.png)

*Figura 7. Representação visual da operação de convolução multidimensional*

No entanto, essa feature map que formamos, é capaz de detectar apenas um certo padrão de formatos. Por exemplo, ela só pode detectar olhos, mas não pode detectar narizes. Para resolver esse problema, podemos utilizar múltiplos filtros, cada um capaz de detectar um padrão diferente. Dessa forma, dado uma imagem de tamanho $H \times W \times C$, o filtro agora terá tamanho $M \times M \times C \times C_{\text{OUT}}$ onde $C_{\text{OUT}}$ é a quantidade de feature maps resultantes. Cada feature map possui seu próprio bias, dessa forma, o número total de parâmetros do modelo será $C_{\text{OUT }}\left( M^{2}C + 1 \right)$.

<a id="secao-31"></a>

## Pooling

Nós vimos anteriormente como obter equivariância à translação, porém, em certas aplicações, queremos que a mesma imagem, mesmo que transladada, seja classificada da mesma forma. Para isso, podemos utilizar uma operação chamada **pooling**, que é uma operação de downsampling que reduz a dimensionalidade da feature map, mantendo as informações mais importantes. Existem diferentes tipos de pooling, como **max pooling**, **average pooling** e **global pooling**.

<a id="max-pooling"></a>

![Operação de max-pooling em um feature map $4 \times 4$ com uma janela de $2 \times 2$ e stride de $2$, resultando em um feature map $2 \times 2$. A operação de $\max$ pega o valor máximo da janela de pooling](../../assets/max-pooling.png)

*Figura 8. Operação de max-pooling em um feature map $4 \times 4$ com uma janela de $2 \times 2$ e stride de $2$, resultando em um feature map $2 \times 2$. A operação de $\max$ pega o valor máximo da janela de pooling*

Seguindo o exemplo da [\[max-pooling\]](#max-pooling), podemos ver que a operação de pooling reduz a dimensionalidade da feature map, mantendo as informações mais importantes. A operação de pooling é importante em CNNs, pois permite que a rede aprenda padrões invariantes à posição do objeto na imagem, além de reduzir o número de parâmetros do modelo e evitar overfitting. Além de max-pooling, também podemos utilizar **average pooling**, que calcula a média dos valores da janela de pooling, e **global pooling**, que calcula a média ou o máximo de toda a feature map. A escolha do tipo de pooling depende da aplicação e do problema em questão.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Convoluções com Stride](../convolucoes-com-stride/index.md)
- Próximo: [Arquiteturas](../arquiteturas/index.md)
