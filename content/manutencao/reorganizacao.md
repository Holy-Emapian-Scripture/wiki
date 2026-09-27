---
layout: default
title: Registro da reorganização
nav_exclude: true
search_exclude: true
tipo: registro
---

# Registro da reorganização

## Escopo

- 35 documentos reorganizados em 35 percursos de leitura.
- 688 páginas de conteúdo, agrupadas em 19 disciplinas.
- 4 hubs de semestre e 2 hubs adicionais, Eletivas e Mestrado.
- 292 imagens e 2 arquivos de bibliografia preservados.

Os arquivos deixaram as pastas de semestre. Conteúdos e anexos ficam em `assuntos/`, percursos em `trilhas/` e os agrupamentos de origem em `semestres/`.

## O que mudou

- Títulos e subtítulos existentes definem a divisão das páginas; soluções de exercícios continuam com os enunciados.
- Os níveis dos títulos foram ajustados para cada página independente.
- Os sumários automáticos dos documentos foram substituídos pela navegação das trilhas e dos assuntos.
- Os destinos dos links internos, das referências e das imagens foram atualizados.
- A autoria disponível, as datas e o caminho de origem foram registrados nos metadados.
- Foram adicionados índices, links entre temas relacionados e navegação anterior/próximo fora dos trechos originais.

As explicações não foram traduzidas, resumidas, corrigidas ou completadas. Conteúdos semelhantes de fontes diferentes continuam separados.

## Particularidades preservadas

- A revisão de **Computação na Nuvem / A1**, em Eletivas, contém somente a apresentação. Sua capa informa “Modelagem Estatística”. A classificação segue a pasta recebida, e a capa original continua na trilha.
- As pastas `lecture_10` e `lecture_12` de Estrutura de Dados têm “Lecture 8 Exercises” na apresentação; `lecture_8` tem “Lecture 7 Exercises”. Os percursos usam o número da pasta, preservando o texto original da capa.
- Há trechos incompletos, títulos sem desenvolvimento e observações dos autores para trabalho futuro. Eles foram mantidos, incluindo seções de Séries Temporais e exercícios de listas.
- Alguns documentos não identificam autoria; nenhum autor foi atribuído por inferência.
- Datas da conversão, como `27/09/2026`, e anos de capa foram preservados. O agrupamento por semestre vem das pastas, não dessas datas.
- A documentação da conversão anterior menciona arquivos Typst e scripts do projeto de origem que não fazem parte deste acervo. Ela permanece como registro histórico.

## Auditoria

O [mapa da reorganização](reorganizacao.json) registra os caminhos, limites, hashes e alterações reversíveis da versão anterior à consolidação. Esse mapa é histórico: suas 688 páginas de conteúdo não correspondem aos arquivos atuais. O [verificador](verificar_wiki.py) audita os links e o alcance das páginas atuais separadamente. Com `--preservacao`, reconstrói os 35 documentos na revisão Git histórica `1fe4ea2`, sem exigir a recriação das pastas antigas no site.

```sh
python3 manutencao/verificar_wiki.py --preservacao

# Após compilar o Quartz na raiz do repositório:
python3 manutencao/verificar_wiki.py --site
```

Essa auditoria compara o conteúdo reconstruído com o hash integral dos 35 documentos. A comparação inclui fórmulas, blocos de código, textos, legendas e a apresentação original. Os 294 anexos são comparados byte a byte por hash.

A verificação de navegação confere links Markdown e wikilinks, âncoras, blocos de código e alcance das páginas publicadas a partir do início. `--site` confere os links internos e as imagens do HTML compilado. Nenhuma das duas verificações testa URLs externas.

O [resultado da verificação](validacao.json) registra a execução histórica ao final da reorganização; não representa uma auditoria da estrutura atual.

## Registros anteriores

- [Documentação da conversão para Markdown](conversao-original.md).
- [Relatório original de conversão](conversao-original.json), mantido com os caminhos históricos.

[Voltar à organização da wiki](../guias/organizacao-da-wiki.md)
