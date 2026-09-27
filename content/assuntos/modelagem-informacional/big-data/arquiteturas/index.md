---
layout: "default"
title: "Arquiteturas — Big Data"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A2.md"
trilha: "../../../../trilhas/modelagem-informacional/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 8
---

[Modelagem Informacional](../../index.md) · [Big Data](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-8"></a>

# Arquiteturas

Aqui eu falei e falei sobre Data Lakes, que eles são desestruturados e muitas outras características. Então um data lake é um banco sem nenhuma estrutura e com um monte de dado jogado? Negativo. Se isso ocorre, ele pode virar um **Data Swamp**

**Definição: Data Swamp**

Um **Data Swamp** é um Data Lake que não teve uma arquitetura para lidar com os dados, seja a falta de pré-processamento, falta total de metadados, entre outras características

Então imagine um Data Swamp como um Data Lake em que não da pra fazer nada. Imagine, por exemplo, um Data Lake com vários registros bancários, porém, os arquivos não tem nome padronizado, fica IMPOSSÍVEL de, por exemplo, pegar os registros entre os anos $x$ e $y$, na verdade é praticamente impossível pegar qualquer informação, então já virou um Data Swamp.

Para evitar esse tipo de problema, surgem alguns autores com sugestões de infrestrutura para os bancos:

<a id="secao-9"></a>

## Modelo Zaloni (Zonas)

A abordagem recomenda organizar o data lake em quatro zonas e uma sandbox. Em todas as zonas, os dados são rastreados, validados, catalogados, os metadados atribuídos e refinados. Esses recursos e as zonas em que ocorrem os processamentos ajudam os usuários e moderadores a entender em que estágio os dados estão e quais medidas foram aplicadas a eles até o momento. Os usuários podem acessar os dados em qualquer uma dessas zonas, desde que tenham acesso baseado em função apropriada. Ou seja, essa arquitetura foca na **limpeza e curadoria** dos dados

1.  **Zona de Landing (Landing Zone / Brutalidade)**

    - Propósito: Recebe os dados de todas as fontes em seu formato bruto (original).

    - Característica: Armazenamento temporário. Os dados não são limpos ou transformados neste estágio e medidas de segurança são aplicadas.

2.  **Zona Bruta (Raw Zone / Bronze)**

    - Propósito: Armazenamento permanente dos dados brutos e originais.

    - Característica: Os dados são imutáveis. Serve como fonte de verdade (Source of Truth) para qualquer reprocessamento futuro. Governança de Metadados (catalogação) se inicia aqui.

3.  **Zona de Curadoria (Curated Zone / Silver)**

    - Propósito: Transformação, limpeza, padronização e enriquecimento dos dados.

    - Característica: Aplicação do pré-processamento. Os dados estão prontos para análise.

4.  **Zona de Serviço (Service Zone / Gold)**

    - Propósito: Preparação final para consumo, muitas vezes com modelagem dimensional (como a de um Data Warehouse).

    - Característica: Otimizada para desempenho de consulta. Usada por ferramentas de BI e aplicações finais.

<a id="secao-10"></a>

## Arquitetura Inmon (Dados)

Antes, precisamos contextualizar o cenário, Inmon dizia que em um Data Lake puro, apenas Cientistas de Dados (Profissionais escassos) conseguem extrair algum tipo de valor, o que os torna muito requisitados, até mesmo depois de contratados, por questões internas. Então que tal montar uma arquitetura em que todos conseguem gerar algum tipo de valor? Para isso, precisamos de alguns ingredientes:

- **Metadados**: Usado para decifrar os dados encontrados no Data Lake.

- **Mapa de integração**: Demonstra como os dados podem ser integrados no Data Lake. Como vencer os “silos” isolados de dados.

- **Contexto**: A capacidade de estabelecer relações entre os diversos tipos de dados depende de um contexto.

- **“Metaprocesso”**: A credibilidade dos dados depende, em parte, da capacidade de rastrear tudo o que for pertinente à geração dos dados.

Então, de acordo com esses ingredientes, temos duas categorizaçẽos dos dados:

- **Dados analógicos**: Dados de telemetria (e.g. GPS), dados gerados por máquinas. Desde log de reatores nucleares até o uso de CPU de um celular. Em geral, são dados volumosos e repetitivos. Tipicamente, apenas os outliers são alvo de interesse.

- **Dados de aplicação**: São os dados gerados a partir da execução de uma aplicação ou transação, e enviados ao Data Lake. Quando qualquer evento relevante ao negócio ocorre, o evento é medido através da aplicação e o dado é criado. Estrutura uniforme. E.g. prever separação do casal.

- **Dados textuais**: Também está ligado a aplicação, contudo não possui estrutura uniforme. Esse dado é chamado de “não-estruturado” porque pode assumir qualquer forma. Algumas ferramentas: GATE e Doccano.

e quanto a repetição

- **Dados não-repetitivos**: Não possuem um padrão específico de fácil identificação (Exemplo: Imagens)

- **Dados repetitivos**: Podem facilmente ser classificados e absorvidos a medida que são conhecidos

A partir dessas definições e categorizações, criamos os **Lagos** (**Data Ponds**), que são containers que separam os dados:

![Esquema vizual dos lagos](../../assets/data-ponds.png)

*Figura 5. Esquema vizual dos lagos*

Então podemos ver as características comuns a todas as lagoas

- **Pond descriptor**: Contém uma descrição do conteúdo recebido: frequência de atualização, descrição da origem, volume de dados, critérios de seleção, critérios de sumarização, critérios de organização e descrição dos relacionamentos entre os dados.

- **Pond target**: Trata-se do tema que irá moldar os dados para atingir objetivos de negócio, e.g. “perfil de cliente”, “registros de vendas”, “análise de click stream”. É o meio pelo qual é estabelecida a relação com o tema de negócio.

- **Pond data**: Trata do mecanismo de armazenamento do pond. É comum usar “schema-on-read”, no entanto é bom observar o trade-off: facilidade gravar vs facilidade de ler os dados.

- **Pond metadata**: Características físicas dos dados no pond. Esse metadado é dependente do meio físico nativo do dado. E.g. se o dado veio de um SGBD, muitas dessas características serão herdadas no pond, tais como, chaves e índices.

- **Pond metaprocess**: Descrição da transformação que é realizada nos dados brutos, para que tornem-se úteis aos analistas de negócio. Também pode-se descrever processos que ocorreram antes do dado chegar no pond.

- **Pond transformation criteria**: Descrição dos critérios usados no processo de transformação. No caso dos dados analógicos poderia ser: “se a temperatura do tanque for maior do que 50°C, capture o registro”, por exemplo.

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Conteúdos relacionados

- [Arquiteturas — Aprendizado de Máquina](../../../aprendizado-de-maquina/convolutional-neural-networks-cnn/arquiteturas/index.md)
- [Arquiteturas — Aprendizado Profundo](../../../aprendizado-profundo/segmentacao-semantica/arquiteturas/index.md)

## Percurso de estudo

[Trilha: A2](../../../../trilhas/modelagem-informacional/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/modelagem-informacional/a2.md#apresentacao-original)

- Anterior: [Os SGBDs](../os-sgbds/index.md)
- Próximo: [Nuvem](../../nuvem/index.md)
