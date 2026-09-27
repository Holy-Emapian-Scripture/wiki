---
layout: "default"
title: "Fundamentos do YOLO — Redes de Estágio Único (Single-Shot): A Família YOLO"
tipo: "conteudo"
disciplina: "Aprendizado Profundo"
origem: "6 semestre/Deep Learning/A1.md"
trilha: "../../../../../trilhas/aprendizado-profundo/a1.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["João Pedro Jerônimo"]
ano_original: 2026
ordem_na_trilha: 32
---

[Aprendizado Profundo](../../../index.md) · [Object Detection](../../index.md) · [Redes de Estágio Único (Single-Shot): A Família YOLO](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-38"></a>

# Fundamentos do YOLO

Um modelo YOLO (You Only Look Once) divide a imagem em uma grade de células, ele também recebe obrigatoriamente uma imagem quadrada, de lados $n \times n$. Cada célula da grade fica resposável por prever objetos cujo **ponto central** (mid point) caia dentro dos limites dessa célula. Como uma única passada na CNN processa todas as células simultaneamente, o YOLO é extremamente rápido e eficiente, tornando-o adequado para aplicações em tempo real.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A1](../../../../../trilhas/aprendizado-profundo/a1.md) · [Apresentação e contexto da fonte](../../../../../trilhas/aprendizado-profundo/a1.md#apresentacao-original)

- Anterior: [Redes de Estágio Único (Single-Shot): A Família YOLO](../index.md)
- Próximo: [Parametrização do vetor de saída](../parametrizacao-do-vetor-de-saida/index.md)
