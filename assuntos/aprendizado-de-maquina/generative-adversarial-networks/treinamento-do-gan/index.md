---
layout: "default"
title: "Treinamento do GAN — Generative Adversarial Networks"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 24
---

[Aprendizado de Máquina](../../index.md) · [Generative Adversarial Networks](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-29"></a>

# Treinamento do GAN

Por mais que essa abordagem de treinamento seja interessante e gere ótimos resultados, ela possui algumas dificuldades por conta do aprenzidado adversarial.

Um desafio que pode surgir durante o treinamento é o **colapso do modo** (mode collapse). Isso ocorre quando o gerador aprende a produzir apenas um conjunto limitado de amostras, ignorando a diversidade presente nos dados reais. Como resultado, o gerador pode gerar imagens muito semelhantes entre si, mesmo que os dados reais sejam variados. Por exemplo, num dataset de digitos, o gerador pode aprender a gerar apenas o dígito “3”, mesmo que o dataset contenha todos os dígitos de 0 a 9. Isso indica que o gerador não está capturando a diversidade dos dados reais, resultando em uma representação limitada do espaço de entrada. Isso ocorre pois o gerador encontra um ponto ótimo local que engana o discriminador, mas não representa a distribuição real dos dados.

![](../../assets/gan-learning.png)

Essa imagem mostra um exemplo dos dados reais provindos da distribuição **fixa**, mas **desconhecida**, $p_{\text{Data }}(x)$ e os dados do gerador $p_{G}(x)$. Podemos ver que, como os dados são muito distintos, o discriminador consegue facilmente distinguir entre eles. No entanto, justamente por conta dos dados iniciais do gerador serem tão diferentes e o discriminador classificá-los tão bem, o treinamento do gerador não é eficiente, pois pequenas aleterações no seu processo de geração de amostras não vão enganar o discriminador. Para contornar isso, podemos utilizar de uma função discriminadora mais suave, na imagem representada por $\widetilde{d}(x)$

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Função de Custo](../funcao-de-custo/index.md)
- Próximo: [Referências](../../referencias-a3/index.md)
