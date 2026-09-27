---
layout: "default"
title: "Aula 3 - Builder e Singleton"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 10
---

[Engenharia de Software](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-10"></a>

# Aula 3 - Builder e Singleton


<a id="builder"></a>
<a id="secao-11"></a>

## Builder

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
## na vida real criamos objetos padrão
## muitas vezes vamos ter uma classe com todas as construções comuns que precisamos (configurações prontas)
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
## sql = 'SELECT * FROM pedidos WHERE tipo_entrega = %s AND total >= %s'
## parametros = ['DRONE', 100.0]
```

Um kwarg fixo não dá conta disso de forma limpa — teria que ser algo como `consultar(cliente=None, tipo_entrega=None, total_minimo=None)` com um `if` pra cada parâmetro checando se é `None` antes de colar no SQL, o que é exatamente a bagunça que o Builder organiza aqui. E de quebra, essa versão já resolve o problema de SQL injection apontado lá na Cacto: em vez de concatenar `pedido.cliente` direto na string, os valores viram parâmetros separados (`%s` + lista `parametros`), passados pro driver do banco em vez de virarem texto da query.

<a id="singleton"></a>
<a id="secao-12"></a>

## Singleton

Singleton parte de um problema oposto: em vez de facilitar criar vários objetos, ele impede que exista mais de um. Só podemos ter uma instância na aplicação, impossível ter um segundo objeto. A analogia dada em aula: é como colocar um assento onde só cabe uma pessoa. Um nome comum pra esse tipo de classe é `Config`, embora o exemplo em si não implemente nenhum método de negócio, só o mecanismo.

<a id="secao-13"></a>

### Singleton no `__new__`

A primeira forma de resolver isso funciona em qualquer linguagem orientada a objetos (existe outro jeito, mas só funciona em Python) e mexe direto no `__new__`:

``` python
from typing import ClassVar, Self


class SingletonNew:
    _instance: ClassVar[SingletonNew | None] = None

    def __new__(cls) -> Self:
        if cls._instance is None:
            print('[SingletonNew] Criando Nova instância')
            cls._instance = super().__new__(cls)
        else:
            print('[SingletonNew] Retornando instância existente!')

        return cls._instance

    def __init__(self):
        self.data: str = 'Shared Resource'


print(SingletonNew() is SingletonNew())
```

Essa solução também pode ser misturada com Builder e outros padrões — o código acima é só o esqueleto, poderia ter métodos de negócio como qualquer classe normal. Só que, como dito pelo Pinho, a solução não é boa: toda vez que você instancia `SingletonNew()`, o `__init__` roda de novo mesmo quando `__new__` está devolvendo a instância antiga — o estado se torna repetido sempre, mesmo sem criar um objeto novo. E pior: com herança, o Singleton se duplica. Se uma classe filha herda de uma classe mãe que já implementa esse `__new__`, a classe filha acaba pegando o singleton da classe mãe. Não dá pra usar essa estratégia no `__new__` de forma confiável quando existe hierarquia.

<a id="secao-14"></a>

### Singleton no decorador

A segunda forma tenta resolver isso com um decorador, guardando cada instância criada num dicionário — em vez de uma cadeira, um banco com vários lugares, um pra cada tipo de classe decorada:

``` python
from collections.abc import Callable
from typing import Any


def singleton_naive[T](cls: type[T]) -> Callable[..., T]:
    instances: dict[type[T], T] = {}

    def get_instance(*args: Any, **kwargs: Any) -> T:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton_naive
class SingletonNaive:
    '''Singleton sem uma preocupação terrível'''

    def __init__(self, rotulo: str = 'Sem algo que seria útil aqui') -> None:
        self.rotulo = rotulo


print(type(SingletonNaive))
print(SingletonNaive().__name__, SingletonNaive().__doc__)
```

O problema aqui é de outra natureza: `get_instance` deveria receber tudo que o construtor da classe original receberia, mas como o decorador funciona pra qualquer classe, ele não tem como saber de antemão o que cada uma espera. E tem um efeito colateral mais sério — depois do decorador, `SingletonNaive` deixa de ser uma classe e passa a ser uma função (`get_instance`, guardada como closure, com `cls` capturado como freevar no frame da função original). Isso significa que um `isinstance` contra `SingletonNaive` já não funciona mais do jeito esperado, porque você estaria comparando contra uma função, não contra um tipo. O singleton em si funciona perfeitamente, mas a classe não funciona mais perfeitamente como classe.

<a id="termos-da-aula-3"></a>
<a id="secao-15"></a>

## Termos da Aula 3

- **Builder** — padrão criacional que isola a lógica de montar um objeto complexo numa classe própria, com métodos encadeados.

- **Singleton** — padrão criacional que garante que uma classe tenha, no máximo, uma única instância na aplicação.

- **Closure** — função que “lembra” variáveis do escopo onde foi definida, mesmo depois que esse escopo termina de executar.

- **Freevar (variável livre)** — variável usada dentro de uma função mas definida fora dela, capturada pela closure.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: Notas de aula](../../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Anterior: [Termos da Aula 2](../aula-2-simple-factory-factory-method-e-ocp/index.md#termos-da-aula-2)
- Próximo: [Aula 4 - Abstract Factory](../aula-4-abstract-factory/index.md)
