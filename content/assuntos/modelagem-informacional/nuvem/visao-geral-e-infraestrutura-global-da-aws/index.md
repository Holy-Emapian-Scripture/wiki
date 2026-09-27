---
layout: "default"
title: "Visão Geral e Infraestrutura Global da AWS — Nuvem"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A2.md"
trilha: "../../../../trilhas/modelagem-informacional/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 13
---

[Modelagem Informacional](../../index.md) · [Nuvem](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-15"></a>

# Visão Geral e Infraestrutura Global da AWS

A infraestrutura global da AWS foi projetada para oferecer um ambiente de computação em nuvem **flexível, confiável, escalável e seguro**, com desempenho de rede global de alta qualidade.

<a id="secao-16"></a>

## Componentes da Infraestrutura

A infraestrutura é organizada nos seguintes níveis geográficos e técnicos:

1.  **Regiões da AWS (Regions):**

    - Áreas geográficas distintas que fornecem redundância total.

    - Cada Região contém duas ou mais **Zonas de Disponibilidade (AZs)**.

    - **Fatores de seleção:** Governança de dados/requisitos legais, proximidade com clientes (baixa latência), serviços disponíveis e custos.

2.  **Zonas de Disponibilidade (AZs):**

    - Partições totalmente isoladas da infraestrutura, projetadas para isolamento de falhas.

    - Consistem em **Datacenters** distintos e são interconectadas por redes privadas de alta velocidade.

    - A AWS recomenda a replicação de dados e recursos entre AZs para garantir resiliência.

3.  **Datacenters:**

    - Instalações físicas onde os dados residem e o processamento ocorre (50.000 a 80.000 servidores).

    - Projetados para segurança, com energia, redes e conectividade redundantes.

4.  **Pontos de Presença (PoPs):**

    - A rede global inclui **187 Pontos de Presença** (incluindo caches regionais).

    - Usados com o **Amazon CloudFront** (CDN) para armazenar conteúdo em cache próximo aos usuários, melhorando a performance e reduzindo a latência.

<a id="secao-17"></a>

## 1.2 Recursos da Infraestrutura

A arquitetura da AWS incorpora características essenciais:

- **Elasticidade e Escalabilidade**: Permitem a adaptação dinâmica da capacidade.

- **Tolerância a Falhas**: Continua funcionando corretamente na presença de falha devido à redundância.

- **Alta Disponibilidade**: Garante alto desempenho operacional com tempo de inatividade mínimo.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/modelagem-informacional/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/modelagem-informacional/a2.md#apresentacao-original)

- Anterior: [Modelos de Implantação](../modelos-de-implantacao/index.md)
- Próximo: [2. Categorias e Serviços Fundamentais da AWS](../categorias-e-servicos-fundamentais-da-aws/index.md)
