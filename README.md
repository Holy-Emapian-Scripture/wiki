# Holy Emapian Wiki (WIP)

Wiki acadêmica colaborativa desenvolvida para reunir conhecimentos, materiais de estudo e experiências dos cursos da FGV EMAp.

Publicada com **[Quartz 5](https://quartz.jzhao.xyz/)** no GitHub Pages:
👉 **[holy-emapian-scripture.github.io/wiki/](https://holy-emapian-scripture.github.io/wiki/)**

---

## Estrutura do Projeto e Boas Práticas

Todo o conteúdo em Markdown reside na pasta `content/`, organizada da seguinte forma:

- **`content/assuntos/`**: 19 disciplinas acadêmicas com tópicos consolidados em páginas completas (`index.md`), organizadas por seções (`##`) com âncoras explícitas para leitura contínua e índice automático (Table of Contents).
- **`content/trilhas/`**: Percursos de estudo organizados pela sequência didática de revisões (A1, A2, A3), notas de aula e listas de exercícios.
- **`content/semestres/`**: Hubs de navegação cronológica do 3º ao 6º semestre, além de Eletivas e Mestrado.
- **`content/guias/`**: Orientações para estudo, modelo de página e instruções de contribuição.
- **`content/manutencao/`**: Registros históricos da conversão e mapeamento estrutural.

Todas as explicações originais, fórmulas matemáticas em LaTeX, blocos de código, legendas e anexos foram integralmente preservados.

### Diretrizes Recentes de Organização e Formatação

1. **Granularidade Consolidada:**
   - Evita-se a dispersão em micro-arquivos. Os subtópicos de um mesmo assunto são reunidos no arquivo `index.md` do tópico, cada um iniciado com `## Subtópico` e sua respectiva âncora `<a id="slug"></a>`.
2. **Ordenação Canônica:**
   - A ordenação das anotações e dos subtópicos internos reflete estritamente o percurso cronológico/pedagógico das trilhas e revisões originais (PDFs).
3. **Formatação Matemática (KaTeX):**
   - **Inline:** Fórmulas no corpo do texto utilizam `$f(x)$` sem quebras de linha.
   - **Bloco:** Equações destacadas utilizam delimitadores `$$` em linhas próprias separadas por linhas em branco, com centralização automática.
4. **Navegação de Percurso:**
   - Cada página consolida ao final a seção `## Percurso de estudo` com links sequenciais para o tópico `Anterior` e `Próximo`.
5. **Tipografia e Estilo:**
   - Tipografia acadêmica serifada (**EB Garamond** no corpo e títulos, e **IBM Plex Mono** em códigos), garantindo leitura agradável e estética de publicação científica.

---

### Aviso 1 - Sobre a Wiki

Esta wiki foi construída sobre as anotações existentes no [Holy Emapian Scripture](https://github.com/Holy-Emapian-Scripture/holy-emapian-scripture) original, sendo adaptado para o formato markdown e organizado com auxílio de ferramentas de IA. Por isso, alguns tópicos podem estar com uma organização inconsistente, bagunçada, ou que simplesmente poderia ser feita melhor. 

Caso encontre algum erro ou algo que poderia ser melhorado, não hesite de abrir uma issue no repositório (comunicando devidamente a sugestão e local) OU editando você mesmo caso tenha permissão.

### Aviso 2 - Sobre o Holy Emapian Scripture

Esses materiais são majoritariamente criados enquanto quem escreveu está vendo a matéria e ninguém é um profissional de escrita, então podem existir erros tanto de conteúdo, quanto de português. Fazemos o máximo para evitar ambos, mas sempre podemos deixar algum detalhe passar.

# Achei um erro!

Se por acaso você encontrar um erro de lógica, escrita, formatação de documento etc. Não tenha vergonha e abra um issue relatando o problema! Toda contribuição e correção será muito bem-vinda

---

## Leitura e Edição no Obsidian

Você pode abrir a pasta raiz ou diretamente a pasta `content/` como um cofre (vault) no **Obsidian**:

1. **Wikilinks e Links Relativos:** Suporte total à sintaxe de Wikilinks do Obsidian (`[[...]]`) e a links Markdown tradicionais.
2. **Referência a Capítulos/Seções:** Para linkar para uma seção ou subtópico específico dentro de uma página:
   ```markdown
   [[assuntos/aprendizado-profundo/segmentacao-semantica/arquiteturas#Deeplab V3 & V3+|Deeplab V3 & V3+]]
   ```
3. **Transclusão / Embed:** Para embutir o conteúdo de um subtópico diretamente em outra nota:
   ```markdown
   ![[assuntos/aprendizado-profundo/segmentacao-semantica/arquiteturas#Deeplab V3 & V3+]]
   ```
4. **Anexos e Imagens:** Mantenha as imagens na pasta `assets/` correspondente da disciplina.

Contribuições são bem-vindas para enriquecer o repositório. Veja como você pode contribuir:

* **Adicionar Novos Materiais**: Envie anotações, listas de exercícios ou resumos de diferentes semestres.
* **Melhorar Conteúdo Existente:** Refine os materiais atuais para maior clareza e precisão.
* **Organização:** Por favor mantenha a estrutura atual do repositório, seguindo o padrão observado nos nomes de pastas, arquivos e formatação de documentos.

Para contribuir, faça um fork do repositório, faça suas alterações e envie um pull request. Será um prazer revisar e aceitar suas contribuições!

Nesse repositório só serão aceitas anotações feitas em formato **Markdown**, e toda anotação nova deve possuir algum caminho (ou seja, sequência de arquivos linkados) para o `content/index.md`. Consulte mais informações nos [guias de contribuição](content/guias/como-contribuir.md).


---

## Publicação e Visualização Local (Quartz 5)

### Pré-requisitos
- **Node.js**: v22 ou superior
- **npm**: v10.9 ou superior

### Comandos Principais

* **Visualizar localmente (com live reload):**
  ```bash
  npx quartz build --serve
  ```
  Acesse no navegador: `http://localhost:8080`.

* **Compilar para produção:**
  ```bash
  npx quartz build
  ```

### Deploy Contínuo
O deploy para o GitHub Pages ocorre automaticamente a cada `git push origin main` através do workflow do GitHub Actions em `.github/workflows/deploy.yaml`.

---

## Licença

Veja a [LICENSE](LICENSE) para mais detalhes.
