---
layout: "default"
title: "Builder — Aula 3 - Builder e Singleton"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 11
---

[Engenharia de Software](../../index.md) · [Aula 3 - Builder e Singleton](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-11"></a>

# Builder

O padrão de criação Builder fala sobre esconder a complexidade de montar um (ou vários (do mesmo)) objeto. O exemplo dado foi fazer uma requisição HTTP (você precisa de url, header, token, body), ou uma consulta SQL via ORM, com schema, select, from, where: linhas e mais linhas só pra montar uma chamada, o que não é gerenciável e dificulta a leitura pra quem lê depois.

Para resolver isso, cria-se uma classe específica só pra construir objetos de um tipo (nomeada normalmente como `{Produto}Builder`), onde cada decisão de criação complexa fica dentro dessa classe, e o objetivo é fazer decisões encadeadas (retornando o self a cada método do Builder).

O exemplo de aula foi montar um computador:

``` python
class Computador:
    def __init__(self):
        self.processador = None
        self.memoria_gb = None
        self.armazenamento_gb = None
        self.placa_video = None

    def __str__(self):
        return f'Processador: {self.processador}, Memória: {self.memoria_gb}, Armazenamento: {self.armazenamento_gb} e Placa de Vídeo {self.placa_video}'


class ComputadorBuilder:
    def __init__(self):
        self.computador = Computador()

    def com_processador(self, processador):
        self.computador.processador = processador
        return self

    def com_memoria_gb(self, memoria_gb):
        self.computador.memoria_gb = memoria_gb
        return self

    def com_armazenamento_gb(self, armazenamento_gb):
        self.computador.armazenamento_gb = armazenamento_gb
        return self

    def com_placa_video(self, placa_video):
        self.computador.placa_video = placa_video
        return self

    def construir(self):
        return self.computador


computador_gamer = (
    ComputadorBuilder()
    .com_processador('Intel I7')
    .com_memoria_gb('16 GB RAM')
    .com_armazenamento_gb('1024')
    .com_placa_video('Nvd 5070')
    .construir()
)
```

Cada propriedade de construção difícil vira um método que devolve `self`, enquanto o resto fica no `__init__` de `Computador`. Todos os métodos do builder fazem isso, com exceção do `.construir()`, que é quem devolve o produto final já pronto. Na vida real você raramente monta um computador atributo por atributo toda vez: normalmente existe uma classe com as construções comuns já prontas (configurações padrão), reaproveitando o mesmo builder por baixo:

``` python
# na vida real criamos objetos padrão
# muitas vezes vamos ter uma classe com todas as construções comuns que precisamos (configurações prontas)
class InfoCentro:
    def montar_computador_basico(self):
        return (
            ComputadorBuilder()
            .com_processador('Intel I3')
            .com_memoria_gb('8 GB RAM')
            .com_armazenamento_gb('256')
            .com_placa_video('Integrada')
            .construir()
        )

    def montar_computador_gamer(self):
        return (
            ComputadorBuilder()
            .com_processador('Intel I7')
            .com_memoria_gb('16 GB RAM')
            .com_armazenamento_gb('1024')
            .com_placa_video('Nvd 5070')
            .construir()
        )
```

Para esse exemplo, fiquei com a dúvida: qual a utilidade do Builder se eu podia simplesmente instanciar `Computador` passando as especificações direto (ou, se precisasse, colocar a classe `Computador` diretamente dentro de uma classe principal (como a `InfoCentro`))? Nesse caso, a resposta é: nenhuma, ou quase. `Computador(processador='Intel I7', memoria_gb='16 GB RAM', armazenamento_gb='1024', placa_video='Nvd 5070')` faz exatamente o mesmo que as cinco linhas encadeadas do `ComputadorBuilder`, com menos código e sem precisar de uma classe extra. O motivo é que o Builder clássico nasceu pra resolver o problema do construtor telescópico, em que pular um parâmetro opcional te obrigava a passar `null` pra todos os anteriores na ordem certa. Nós não conseguimos enxergar esse problema pois o Python já resolve isso de fábrica com `kwargs` e parâmetros nomeados (colocar `parametro = valor_padrao`).

O Builder só ganha da alternativa direta quando o que está sendo montado não é só um punhado de campos escalares: é o caso dos dois exemplos que abriram a aula, montar um request HTTP ou uma query SQL, onde você vai **acumulando** uma quantidade variável de coisas (headers, cláusulas `where`) em vez de preencher campos fixos, ou quando um passo depende do resultado de outro (validar se a fonte de energia aguenta a placa de vídeo escolhida, por exemplo), ou quando você quer impedir que um objeto pela metade escape pro resto do código.

Um exemplo concreto onde o Builder faz sentido, voltando pro domínio da Cacto: montar a consulta de pedidos com um número variável de filtros, onde cada `.com_X()` só entra na query se o chamador realmente pedir aquele filtro.

``` python
class ConsultaPedidosBuilder:
    def __init__(self):
        self.tabela = "pedidos"
        self.condicoes = []
        self.parametros = []

    def com_cliente(self, cliente):
        self.condicoes.append("cliente = %s")
        self.parametros.append(cliente)
        return self

    def com_tipo_entrega(self, tipo_entrega):
        self.condicoes.append("tipo_entrega = %s")
        self.parametros.append(tipo_entrega)
        return self

    def com_total_minimo(self, total_minimo):
        self.condicoes.append("total >= %s")
        self.parametros.append(total_minimo)
        return self

    def construir(self):
        sql = f"SELECT * FROM {self.tabela}"
        if self.condicoes:
            sql += " WHERE " + " AND ".join(self.condicoes)
        return sql, self.parametros


sql, parametros = (
    ConsultaPedidosBuilder()
    .com_tipo_entrega("DRONE")
    .com_total_minimo(100.0)
    .construir()
)
# sql = 'SELECT * FROM pedidos WHERE tipo_entrega = %s AND total >= %s'
# parametros = ['DRONE', 100.0]
```

Um kwarg fixo não dá conta disso de forma limpa — teria que ser algo como `consultar(cliente=None, tipo_entrega=None, total_minimo=None)` com um `if` pra cada parâmetro checando se é `None` antes de colar no SQL, o que é exatamente a bagunça que o Builder organiza aqui. E de quebra, essa versão já resolve o problema de SQL injection apontado lá na Cacto: em vez de concatenar `pedido.cliente` direto na string, os valores viram parâmetros separados (`%s` + lista `parametros`), passados pro driver do banco em vez de virarem texto da query.

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Notas de aula](../../../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Anterior: [Aula 3 - Builder e Singleton](../index.md)
- Próximo: [Singleton](../singleton/index.md)
