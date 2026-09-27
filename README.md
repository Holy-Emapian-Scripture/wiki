# Holy Emapian Wiki

Wiki acadêmica colaborativa desenvolvida para reunir conhecimentos, materiais de estudo e experiências dos cursos da FGV EMAp.

Publicada com **[Quartz 5](https://quartz.jzhao.xyz/)** no GitHub Pages:
👉 **[holy-emapian-scripture.github.io/wiki/](https://holy-emapian-scripture.github.io/wiki/)**

---

## 📂 Estrutura do Projeto

Todo o conteúdo em Markdown reside na pasta `content/`, organizada da seguinte forma:

- **`content/assuntos/`**: 19 disciplinas acadêmicas com tópicos consolidados em páginas completas, organizadas por seções (`##`) com âncoras para leitura contínua e índice automático (Table of Contents).
- **`content/trilhas/`**: Percursos de estudo organizados pela sequência de revisões (A1, A2, A3), notas de aula e listas de exercícios.
- **`content/semestres/`**: Hubs de navegação cronológica do 3º ao 6º semestre, além de Eletivas e Mestrado.
- **`content/guias/`**: Orientações para estudo, modelo de página e instruções de contribuição.
- **`content/manutencao/`**: Registros históricos da conversão e mapeamento estrutural.

Todas as explicações originais, fórmulas matemáticas em LaTeX, blocos de código, legendas e anexos foram integralmente preservados.

---

## ✍️ Edição no Obsidian

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

---

## 🚀 Publicação e Visualização Local (Quartz 5)

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

## 📜 Licença

Veja a [LICENSE](LICENSE) e consulte os [guias de contribuição](content/guias/como-contribuir.md).
