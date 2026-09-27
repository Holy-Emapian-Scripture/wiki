---
layout: "default"
title: "Por que o `processar` deveria ser vários métodos (SRP) — Aula 1 - Documentação, Contratos e SRP"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 3
---

[Engenharia de Software](../../index.md) · [Aula 1 - Documentação, Contratos e SRP](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-3"></a>

# Por que o `processar` deveria ser vários métodos (SRP)

O problema dessa função é que ela tem várias (funções). Se listassemos, quem, na empresa, poderia pedir uma mudança em `ProcessadorDePedido.processar` — e apontando exatamente onde, dentro do método, cada um bateria:

- a **contabilidade** precisar mudar a alíquota — o `0.18` fixo em `imposto = base_imposto * 0.18`;

- o **marketing** criar um cupom novo — o bloco `if pedido.cupom == "NULLSAFE10": ...`

- o **marketing** precisar mudar o e-mail — o bloco que monta `corpo` em HTML e manda pro “SMTP”;

- o **gateway do cartão** mudar — a validação de `numero_cartao` (tamanho, dígitos, soma);

- o **DBA** precisar mudar uma coluna — o `sql = "INSERT INTO pedidos ..."` montado por concatenação de string (que, à parte da aula, também é uma porta aberta pra SQL injection, já que `pedido.cliente` entra direto na query sem tratamento nenhum);

- o **SEFAZ** mudar o layout da nota — o bloco `"=== NOTA FISCAL ELETRONICA ==="`;

- os **Correios** mudarem o modo de calcular o peso — a fórmula `peso_kg = peso_kg + item.quantidade * (item.cacto.altura_cm * 0.05)`;

- o **COO** querer oferecer outra forma de envio — o `if`/`elif` de `tipo_entrega`.

É esse problema que o Princípio de Responsabilidade Única (SRP) corrige: cada componente deve apresentar uma única responsabilidade. É o primeiro dos cinco princípios do SOLID.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Notas de aula](../../../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Anterior: [Cacto](../cacto/index.md)
- Próximo: [Loja (exercício de correção)](../loja-exercicio-de-correcao/index.md)
