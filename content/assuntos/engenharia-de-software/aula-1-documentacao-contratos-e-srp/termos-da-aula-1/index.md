---
layout: "default"
title: "Termos da Aula 1 — Aula 1 - Documentação, Contratos e SRP"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 5
---

[Engenharia de Software](../../index.md) · [Aula 1 - Documentação, Contratos e SRP](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-5"></a>

# Termos da Aula 1

- **Docstring, typehint** - Vocês já sabem isso;

- **Design by contract** — declarar o comportamento esperado de um componente (o que ele espera receber, o que garante devolver) e confiar nisso, em vez de reverificar tudo em tempo de execução.

- **Defeito (fault/bug)** — falha concreta e localizável no código-fonte, que existe independente de ser executada.

- **Falha (failure)** — comportamento incorreto observável quando o programa roda e um defeito é de fato acionado.

- **Code smell** — sintoma de que o design do código está ruim, mesmo funcionando sem erros; o “cheiro” de um problema estrutural.

- **God class** — classe (ou método) que sabe e faz coisas demais, concentrando responsabilidades que deveriam estar separadas.

- **SRP (Princípio de Responsabilidade Única)** — cada componente deve ter um único motivo pra mudar; o S do SOLID.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Notas de aula](../../../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Anterior: [Loja (exercício de correção)](../loja-exercicio-de-correcao/index.md)
- Próximo: [Aula 2 - Simple Factory, Factory Method e OCP](../../aula-2-simple-factory-factory-method-e-ocp/index.md)
