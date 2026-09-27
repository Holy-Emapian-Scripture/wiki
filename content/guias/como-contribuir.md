---
layout: default
title: Como contribuir
parent: Guias
nav_order: 1
---

# Como contribuir

Uma contribuição pode ser pequena: corrigir uma explicação, acrescentar uma referência, incluir um exemplo resolvido ou sanar uma imprecisão técnica já faz uma enorme diferença para quem está estudando.

---

## Estrutura e Granularidade das Anotações

Para evitar uma proliferação de micro-arquivos excessivamente curtos e manter uma leitura contínua e agradável, a wiki adota uma estrutura consolidada por temas:

1. **Agrupamento por Tema Principal:**
   - Em vez de criar um arquivo isolado para cada pequeno subtópico, reunimos as anotações de um mesmo tema em um único arquivo de índice temático: `content/assuntos/<disciplina>/<tema>/index.md` (por exemplo, `assuntos/aprendizado-profundo/segmentacao-semantica/arquiteturas/index.md`).
2. **Subtópicos e Âncoras Explícitas:**
   - Cada subtópico dentro do documento é introduzido por um título de nível 2 (`## Nome do Subtópico`) acompanhado por uma âncora HTML explícita:
     ```markdown
     <a id="u-net"></a>
     ## U-Net
     ```
   - Isso permite referenciar diretamente qualquer subtópico a partir de outras páginas (`[U-Net](../arquiteturas/index.md#u-net)`) ou fazer transclusão no Obsidian (`![[arquiteturas#U-Net]]`).
3. **Índice Automático (TOC):**
   - O Quartz e o tema da wiki geram automaticamente um sumário na barra lateral direita com todos os subtópicos da página (`##`), facilitando a navegação rápida.
4. **Ordem Pedagógica e Canônica:**
   - A sequência dos subtópicos dentro do arquivo deve respeitar estritamente o percurso didático dos materiais originais (aulas e documentos de revisão dos cursos), em vez de uma ordenação alfabética arbitrária.

---

## Como Criar ou Expandir uma Página

1. **Consulte o Modelo:**
   - Veja o [`modelo-de-pagina.md`](modelo-de-pagina.md) para a estrutura padrão recomendada.
2. **Local do Arquivo:**
   - Salve a nova página em `content/assuntos/<disciplina>/<tema>/index.md`. Use nomes curtos em minúsculas e separados por hífen (kebab-case).
3. **Cabeçalho (Frontmatter):**
   - No topo do arquivo, defina os metadados entre `---`:
     ```yaml
     ---
     title: "Nome do Assunto ou Tema"
     tags:
       - disciplina
       - assunto
     ---
     ```
4. **Navegação de Percurso (`## Percurso de estudo`):**
   - Ao final do documento, inclua sempre os links para o tópico anterior e seguinte da matéria/trilha:
     ```markdown
     ## Percurso de estudo

     - **Anterior:** [Tópico Anterior](../topico-anterior/index.md)
     - **Próximo:** [Próximo Tópico](../proximo-topico/index.md)
     ```

---

## Formatação Matemática (LaTeX / KaTeX)

A wiki utiliza **KaTeX** para renderização rápida e precisa de fórmulas matemáticas. Para garantir a renderização perfeita tanto no Quartz quanto no Obsidian, siga rigorosamente as duas regras abaixo:

### 1. Fórmulas em linha (inline math)
- Delimite com um único cifrão colado ao texto: `$f(x) = \sin(x)$`.
- **Nunca insira quebras de linha** dentro dos cifrões de matemática em linha.
- Exemplo: `A probabilidade condicional $P(A \mid B)$ satisfaz a regra do produto.`

### 2. Equações destacadas em bloco (display/block math)
- Delimite com `$$` em linhas isoladas, precedidas e sucedidas por uma linha em branco:
  ```markdown
  A média amostral converge quase certamente para o valor esperado:

  $$
  \lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^n X_i = \mathbb{E}[X]
  $$

  conforme garantido pela Lei Forte dos Grandes Números.
  ```
- **Atenção:** Nunca coloque `$$...$$` no meio de uma linha de texto contínuo. As equações em bloco devem ficar isoladas para que o KaTeX possa aplicar a centralização estética correta.

---

## Links, Anexos e Obsidian

A wiki foi projetada para funcionar perfeitamente tanto como site publicado (Quartz 5) quanto como vault local no **Obsidian**:

1. **Tipos de Links:**
   - Links Markdown relativos tradicionais (`[Texto](../outro-topico/index.md)`) e Wikilinks (`[[outro-topico]]` ou `[[arquiteturas#U-Net|U-Net]]`) são totalmente suportados.
2. **Imagens e Anexos:**
   - Salve as imagens na pasta `assets/` da disciplina correspondente: `content/assuntos/<disciplina>/assets/nome-da-imagem.png`.
   - Insira no Markdown usando caminho relativo:
     ```markdown
     ![Diagrama da arquitetura U-Net](../assets/u-net-diagrama.png)
     ```
3. **Blocos de Código:**
   - Especifique sempre a linguagem para syntax highlighting (ex.: ````python`, ````bash`, ````latex`).

---

## Testando Suas Alterações Localmente

Antes de enviar suas contribuições via Pull Request, você pode visualizar exatamente como o site ficará:

1. **Instale as dependências** (caso ainda não tenha feito):
   ```bash
   npm install
   ```
2. **Inicie o servidor de testes do Quartz:**
   ```bash
   npx quartz build --serve
   ```
3. Abra seu navegador em `http://localhost:8080`.
4. Verifique se os links funcionam, se as equações estão centralizadas e se o sumário lateral exibe corretamente os subtópicos.

[Voltar aos guias](index.md)
