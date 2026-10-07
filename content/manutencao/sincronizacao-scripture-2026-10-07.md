---
title: "Sincronização da Scripture — 07/10/2026"
tags:
  - manutencao
  - sincronizacao
nav_exclude: true
search_exclude: true
---

# Sincronização da Scripture — 07/10/2026

Origem: `../holy-emapian-scripture`, revisão `4f783b8793ec4aa244de3125434be4e596132c58`. Comparação com a revisão `c81812d`, utilizada na sincronização anterior da Wiki (commit `1f7bf94`). A origem permaneceu sem alterações.

## Conteúdos incorporados

- **Probabilidade / A1:** Combinatória; Primeiros passos em Probabilidade; Probabilidade Condicional; Variáveis Aleatórias Discretas; Esperança; Medidas de Dispersão; Quantificadores de Independência; Distribuições de Variáveis Aleatórias Discretas.
- **Séries Temporais / A1:** revisões dos capítulos existentes, incluindo métricas pontuais e distribucionais, Box-Cox, diferenciação, AR/PACF e MA/invertibilidade; novos capítulos de ARIMA, estimação e critérios de informação (AIC, AICc, BIC, KPSS e busca automática) e SARIMA.
- **Navegação:** hubs das disciplinas, catálogo, trilhas e percurso anterior/próximo. A revisão anterior de Probabilidade permanece em `trilhas/probabilidade/a1-anterior.md`, com as páginas e os endereços anteriores preservados.
- **Imagens:** 15 novos arquivos (2 de Probabilidade e 13 de Séries Temporais), com hashes conferidos contra a origem.

## Adaptação e pendências da origem

A conversão foi executada em uma cópia temporária com Pandoc 3.8.3. As equações em bloco receberam delimitadores em linhas isoladas; referências Typst foram adaptadas para links entre as páginas correspondentes. Âncoras históricas da Wiki foram preservadas.

Os dois links de vídeo com destino `_` e rótulo `[PREENCHER]` na fonte foram mantidos como texto **[PREENCHER — link pendente na origem]**, em Probabilidade Condicional e Medidas de Dispersão.

## Validação

- Conversão: releitura das fórmulas e códigos, tradução para MathML, referências internas e hashes das imagens aprovados nos dois documentos.
- Após dividir os documentos: 1.011 expressões matemáticas em Probabilidade e 1.170 em Séries Temporais, idênticas às da conversão completa sem o sumário; nenhuma expressão ausente ou extra. As contagens incluem matemática em títulos, legendas e textos alternativos.
- Build: `node quartz/bootstrap-cli.mjs build` concluído, com 278 páginas e 974 arquivos emitidos.
- Navegação: `python3 content/manutencao/verificar_wiki.py --site` verificou 278 páginas, 3377 links locais e 2879 links publicados, sem erros.
- Nenhum elemento `katex-error` no HTML das duas disciplinas. Avisos de caracteres Unicode foram emitidos pelo build.
- Prévia: equações, tabela e sumário de Combinatória; equações e carregamento das imagens de SARIMA.
- `git diff --check` aprovado.
