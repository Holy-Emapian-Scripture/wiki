---
layout: "default"
title: "2. Categorias e Serviços Fundamentais da AWS — Nuvem"
tipo: "conteudo"
disciplina: "Modelagem Informacional"
origem: "4 semestre/Modelagem Informacional/Recaps/A2.md"
trilha: "../../../../trilhas/modelagem-informacional/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 14
---

[Modelagem Informacional](../../index.md) · [Nuvem](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-18"></a>

# 2. Categorias e Serviços Fundamentais da AWS

Os serviços da AWS são agrupados em categorias principais.

|  |  |
|:--:|:--:|
| **Categoria Principal** | **Serviços Fundamentais (Exemplos)** |
| Computação | Amazon EC2, AWS Lambda, Amazon ECS/EKS/Fargate, AWS Elastic Beanstalk |
| Armazenamento | Amazon S3, Amazon EBS, Amazon EFS, Amazon S3 Glacier |
| Bancos de Dados | Amazon RDS, Amazon Aurora, Amazon DynamoDB, Amazon Redshift |
| Redes e Entrega de Conteúdo | Amazon VPC, Elastic Load Balancing, AWS Direct Connect, Amazon CloudFront, Amazon Route 53 |
| Segurança, Identidade e Conformidade | AWS IAM, AWS KMS, AWS Shield, Amazon Cognito |
| Gerenciamento e Governança | AWS Management Console, Amazon CloudWatch, AWS Trusted Advisor, AWS Config |

<a id="secao-19"></a>

## 2.1 Detalhamento dos Serviços Principais

|  |  |  |
|:--:|:--:|:--:|
| **Serviço** | **Conceito** | **Funcionalidade Principal** |
| Amazon EC2 | **IaaS (Computação em Nuvem)** | Instâncias de máquinas virtuais configuráveis para executar aplicações com controle total do sistema operacional e infraestrutura. |
| AWS Lambda | **Computação Sem Servidor (FaaS)** | Executa funções acionadas por eventos, sem necessidade de provisionar servidores. Pagamento apenas pelo tempo de execução. |
| Amazon ECS | **Orquestração de Contêineres** | Gerencia contêineres Docker em clusters altamente escaláveis e integrados com outros serviços da AWS. |
| Amazon EKS | **Kubernetes Gerenciado** | Executa e gerencia clusters Kubernetes com alta disponibilidade, segurança e integração nativa com AWS. |
| AWS Fargate | **Execução Serverless para Contêineres** | Permite rodar contêineres sem gerenciar servidores ou clusters. O usuário define apenas recursos de CPU e memória. |
| AWS Elastic Beanstalk | **PaaS (Plataforma Gerenciada)** | Implanta e gerencia automaticamente aplicações (EC2, ELB, autoscaling) sem necessidade de configurar infraestrutura manualmente. |
| Amazon S3 | **Armazenamento de Objetos** | Armazenamento durável e escalável para qualquer tipo de dado, com 99.999999999% de durabilidade. |
| Amazon EBS | **Armazenamento em Bloco** | Volumes persistentes anexáveis a instâncias EC2, com suporte a snapshots, alta performance e criptografia. |
| Amazon EFS | **Sistema de Arquivos NFS Gerenciado** | Sistema de arquivos elástico e distribuído, acessado simultaneamente por múltiplas instâncias EC2. |
| Amazon S3 Glacier | **Arquivamento de Baixo Custo** | Armazenamento extremamente barato para dados acessados raramente, com tempos de recuperação variáveis. |
| Amazon RDS | **Banco de Dados Relacional Gerenciado** | Automatiza backup, patching, escalabilidade e manutenção para SGBDs como MySQL, PostgreSQL, MariaDB, Oracle e SQL Server. |
| Amazon Aurora | **Banco Relacional de Alta Performance** | Compatível com MySQL e PostgreSQL, com performance superior e replicação distribuída. |
| Amazon DynamoDB | **Banco NoSQL (Chave-Valor e Documento)** | Banco de baixa latência, totalmente gerenciado e escalável automaticamente. |
| Amazon Redshift | **Data Warehouse** | Armazena e analisa dados em larga escala com processamento analítico massivamente paralelo (MPP). |
| Amazon VPC | **Rede Virtual Isolada** | Permite criar redes privadas dentro da AWS, com controle de sub-redes, rotas, segurança e IPs. |
| Elastic Load Balancing (ELB) | **Balanceamento de Carga** | Distribui tráfego automaticamente entre múltiplas instâncias e zonas de disponibilidade. |
| AWS Direct Connect | **Conexão Dedicada** | Cria uma conexão privada entre o data center do cliente e a AWS, reduzindo latência e aumentando segurança. |
| Amazon CloudFront | **CDN (Content Delivery Network)** | Entrega conteúdo globalmente com baixa latência e alta velocidade através de edge locations. |
| Amazon Route 53 | **DNS Gerenciado** | Serviço de registro, roteamento e verificação de saúde de domínios altamente disponível e escalável. |
| AWS IAM | **Gerenciamento de Identidade e Acessos** | Define permissões e autenticação para usuários, grupos, funções e serviços. |
| AWS KMS | **Gerenciamento de Chaves Criptográficas** | Cria e controla chaves de criptografia para proteger dados em repouso e em trânsito. |
| AWS Shield | **Proteção DDoS** | Protege aplicações contra ataques DDoS automaticamente, com camadas Standard e Advanced. |
| Amazon Cognito | **Gerenciamento de Autenticação de Usuários** | Cria autenticação e gerenciamento de usuários para apps web e mobile (sign-up, sign-in, MFA). |
| AWS Management Console | **Interface de Gerenciamento** | Console web para gerenciar todos os recursos da AWS de forma centralizada. |
| Amazon CloudWatch | **Monitoramento e Observabilidade** | Coleta métricas, logs e eventos para monitoramento de recursos e aplicações. |
| AWS Trusted Advisor | **Otimização de Recursos** | Analisa a conta e recomenda melhorias de custo, segurança, performance e tolerância a falhas. |
| AWS Config | **Governança e Conformidade** | Monitora configurações dos recursos e avalia conformidade em relação a regras definidas. |
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/modelagem-informacional/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/modelagem-informacional/a2.md#apresentacao-original)

- Anterior: [Visão Geral e Infraestrutura Global da AWS](../visao-geral-e-infraestrutura-global-da-aws/index.md)
