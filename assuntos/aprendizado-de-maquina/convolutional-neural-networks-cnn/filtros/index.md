---
layout: "default"
title: "Filtros — Convolutional Neural Networks (CNN)"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 22
---

[Aprendizado de Máquina](../../index.md) · [Convolutional Neural Networks (CNN)](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-25"></a>

# Filtros

As CNNs são interessantes. Se tentássemos treinar uma rede neural comum usando uma imagem, seria inviável, pois a rede seria MUITO grande. Imagine uma imagem de, por exemplo, $1000 \times 1000$ pixels. Se tentássemos treinar uma rede neural comum usando essa imagem, teríamos $1.000.000$ de entradas (uma para cada pixel), além de que se for colorida, seria $3.000.000$. Isso resultaria em uma rede neural com milhões de parâmetros, tornando o treinamento extremamente difícil e propenso a overfitting. Para tentar contornar esse problema, as CNNs utilizam de diversas abordagens para, dentro da arquitetura, capturar propriedades específicas de imagens:

- **Hierarquia**: Elementos em imagens possuem uma hierarquia natural. Por exemplo, uma imagem de um rosto humano pode ser decomposta em partes como olhos, nariz e boca, que por sua vez podem ser decompostas em características mais simples, como bordas e texturas. As CNNs são projetadas para capturar essas hierarquias de características, permitindo que a rede aprenda representações cada vez mais complexas à medida que avança pelas camadas.

- **Localidade**: As CNNs exploram a localidade das imagens, ou seja, a ideia de que pixels próximos uns dos outros estão mais relacionados do que pixels distantes. Isso é feito através do uso de filtros convolucionais, que operam em pequenas regiões da imagem, permitindo que a rede capture padrões locais e invariantes a transformações.

- **Equivariância**: As CNNs são projetadas para serem equivariantes a translações, o que significa que se um objeto na imagem for deslocado, a rede ainda será capaz de reconhecê-lo. Isso é alcançado através do uso de operações de convolução e pooling, que permitem que a rede aprenda características independentes da posição do objeto na imagem.

- **Invariância**: As CNNs também podem ser projetadas para serem invariantes a certas transformações, como rotação e escala. Isso é feito através do uso de técnicas como data augmentation, que aumentam a diversidade do conjunto de treinamento, e camadas de pooling, que reduzem a sensibilidade da rede a pequenas variações na posição e tamanho dos objetos.

<a id="secao-26"></a>

## Capturando Localidade

Por simplicidade, no momento vamos assumir que nossas imagens estão na escala de cinza (são matrizes no ${\mathbb{R}}^{H \times W}$). Queremos, de alguma forma, capturar a localidade das imagens. Intuitivamente, podemos pensar em, de alguma forma, resumir uma região da imagem em um único valor. Por exemplo, podemos pegar uma região de $3 \times 3$ pixels e calcular a média dos valores dos pixels dessa região. Isso nos daria um único valor representando a intensidade média da região. No entanto, essa abordagem simples não captura padrões mais complexos, como bordas ou texturas

![Representação visual de como podemos capturar a localidade de uma imagem usando uma região de $3 \times 3$ pixels](../../assets/locality-cnn.png)

*Figura 4. Representação visual de como podemos capturar a localidade de uma imagem usando uma região de $3 \times 3$ pixels*

Uma forma mais interessante que reflete o que fizemos até o momento, é aplicar uma matriz de pesos à esses pixels. $$z = \text{ ReLU}\left( w^{T}x + w_{0} \right)$$ onde $x$ é o vetor de pixels da região, $w$ é o vetor de pesos e $w_{0}$ é o viés. Essa abordagem permite que a rede aprenda padrões mais complexos, como bordas ou texturas, ao invés de apenas calcular a média da região. Além disso, podemos aplicar diferentes matrizes de pesos a diferentes regiões da imagem, permitindo que a rede aprenda diferentes padrões em diferentes partes da imagem. Esses filtros também são chamados popularmente de **kernels** e são aplicados a toda a imagem, permitindo que a rede aprenda padrões invariantes à posição do objeto na imagem. A operação de aplicar um filtro a uma região da imagem é chamada de **convolução**, e é a base das CNNs.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Imagens como dados](../imagens-como-dados/index.md)
- Próximo: [Equivariância em Translação](../equivariancia-em-translacao/index.md)
