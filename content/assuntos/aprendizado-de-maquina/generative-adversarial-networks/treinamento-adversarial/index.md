---
layout: "default"
title: "Treinamento Adversarial — Generative Adversarial Networks"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 22
---

[Aprendizado de Máquina](../../index.md) · [Generative Adversarial Networks](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-27"></a>

# Treinamento Adversarial

Vamos considerar um modelo generativo baseado numa transformação de uma variável latente $z$ para o espaço dos dados $x$. Por simplicidade, vamos definir $$p(z) = N(0,I)$$ juntamente de uma transformação não-linear $g(z,w)$ definida por uma rede neural profunda com parâmetros $w$ conhecida como **gerador**. Essas definições implicam que há uma distribuição de probabilidade sobre $x$ que queremos encaixar em cima dos nossos dados. No entanto, nós não conseguimos determinar $w$ maximizando a verossimilhança, já que em geral não tem forma fechada.

Como já explicamos, a ideia das GANs é introduzir uma segunda rede que vai ser treinada em conjunto com a rede **geradora**, a chamada **discriminadora**. Seu trabalho é distinguir entre amostras reais e amostras geradas. O discriminador é definido como uma rede neural profunda $d(x,\varphi)$ com parâmetros $\varphi$ que retorna a probabilidade de $x$ ser uma amostra real. O discriminador é treinado para maximizar a probabilidade de classificar corretamente as amostras reais e falsas, enquanto o gerador é treinado para fazer com que a probabilidade seja a mais próxima possível de $0.5$, ou seja, o gerador quer enganar o discriminador.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Introdução](../introducao/index.md)
- Próximo: [Função de Custo](../funcao-de-custo/index.md)
