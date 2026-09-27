---
layout: "default"
title: "Singleton — Aula 3 - Builder e Singleton"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 12
---

[Engenharia de Software](../../index.md) · [Aula 3 - Builder e Singleton](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-12"></a>

# Singleton

Singleton parte de um problema oposto: em vez de facilitar criar vários objetos, ele impede que exista mais de um. Só podemos ter uma instância na aplicação, impossível ter um segundo objeto. A analogia dada em aula: é como colocar um assento onde só cabe uma pessoa. Um nome comum pra esse tipo de classe é `Config`, embora o exemplo em si não implemente nenhum método de negócio, só o mecanismo.

<a id="secao-13"></a>

## Singleton no `__new__`

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

## Singleton no decorador

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

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Notas de aula](../../../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Anterior: [Builder](../builder/index.md)
- Próximo: [Termos da Aula 3](../termos-da-aula-3/index.md)
