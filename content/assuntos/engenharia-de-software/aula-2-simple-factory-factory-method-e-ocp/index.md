---
layout: "default"
title: "Aula 2 - Simple Factory, Factory Method e OCP"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 6
---

[Engenharia de Software](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-6"></a>

# Aula 2 - Simple Factory, Factory Method e OCP


<a id="factory-method"></a>
<a id="secao-8"></a>

## Factory Method

O Simple Factory ainda tem um `if` central, só que concentrado num único lugar. Em vez de uma fábrica perguntar “qual centro é esse?”, cada centro de distribuição sabe, por si mesmo, qual frete criar — quem entrega essa decisão ao código passa a ser a própria classe do centro de distribuição. Isso é feito com um método abstrato que cada subclasse implementa à sua maneira, uma por centro (faz isso importando o decorador e passando o decorador a função e a classe a própria factory - é um método declarado sem corpo ou código de execução, que serve como uma regra obrigatória para que as classes filhas criem sua própria implementação). Vejamos no exemplo:

``` python
class CentroDeDistribuicao(ABC):
    def __init__(self, cidade, calculadora, recibo):
        self.cidade = cidade
        self.calculadora = calculadora
        self.recibo = recibo

    @abstractmethod
    def criar_frete(self):
        ...

    def despachar(self, cliente, valor, peso_kg):
        frete = self.criar_frete()
        total = self.calculadora.total(valor, frete.custo(peso_kg))
        return self.recibo.gerar(cliente, total, self.cidade)


class CentroSaoPaulo(CentroDeDistribuicao):
    def __init__(self, calculadora, recibo):
        super().__init__("São Paulo", calculadora, recibo)

    def criar_frete(self):
        return FreteRodoviario()


class CentroManaus(CentroDeDistribuicao):
    def __init__(self, calculadora, recibo):
        super().__init__("Manaus", calculadora, recibo)

    def criar_frete(self):
        return FreteFluvial()


class CentroBelem(CentroDeDistribuicao):
    def __init__(self, calculadora, recibo):
        super().__init__("Belém", calculadora, recibo)

    def criar_frete(self):
        return FreteFluvial()
```

Agora, Belém tem, por conta própria, o frete fluvial certo — sem precisar tocar em nenhum `if`. O restante do fluxo (calcular total, gerar recibo) fica implementado uma única vez, no método concreto `despachar` da classe-base — as subclasses só precisam dizer qual frete usar. O polimorfismo (significa “muitas formas” (no caso, a função criar_frete é a polimórfica)) substitui o `if`: quando o código chama `self.criar_frete()`, quem responde já é o objeto do centro certo, decidido no momento em que a classe foi escolhida (a instanciação), não dentro de um `if` em tempo de execução. Essa é a etapa 4:

``` python
print("ETAPA 4")
sao_paulo = CentroSaoPaulo(CalculadoraTotal(), Recibo())
manaus = CentroManaus(CalculadoraTotal(), Recibo())
belem = CentroBelem(CalculadoraTotal(), Recibo())
print(sao_paulo.despachar(cliente, valor, peso_kg))
print(manaus.despachar(cliente, valor, peso_kg))
print(belem.despachar(cliente, valor, peso_kg))
```

O mesmo raciocínio vale pra produtos: pra cada produto novo que precise de fábrica própria, o padrão pede duas classes, o produto e a fábrica do produto (aqui, o “produto” é o `Frete`, e a “fábrica” é o próprio `CentroDeDistribuicao`).

Comparado ao Simple Factory, adicionar um centro de distribuição novo passa a significar **criar** uma subclasse, e não editar nenhuma existente: nada do código antigo precisou mudar pra isso, nem o `CentroDeDistribuicao` já existente precisou ser tocado pra nascer um tipo novo. Esse é, literalmente, o enunciado do Open/Closed Principle, o O do SOLID: uma classe deve estar fechada para modificação e aberta para extensão.

<a id="simple-factory"></a>
<a id="secao-7"></a>

## Simple Factory

Simple Factory resolve o problema das classes: tira o `if` de dentro da loja e concentra numa única classe. A ideia, resumida em aula, é simplesmente mudar o if de lugar:

``` python
class FabricaDeFrete:
    def criar(self, centro):
        if centro == 'Sao Paulo':
            return FreteRodoviario()
        elif centro == 'Manaus':
            return FreteFluvial()
        else:
            return FreteRodoviario()


class SimuladorDeFrete:
    def __init__(self, fabrica):
        self.fabrica = fabrica

    def simular(self, centro, peso_kg):
        return self.fabrica.criar(centro).custo(peso_kg)


class Loja3:
    def __init__(self, fabrica, calculadora, recibo):
        self.fabrica = fabrica
        self.calculadora = calculadora
        self.recibo = recibo

    def processar(self, cliente, valor, peso_kg, centro):
        frete = self.fabrica.criar(centro)
        total = self.calculadora.total(valor, frete.custo(peso_kg))
        return self.recibo.gerar(cliente, total, centro)
```

Agora, a loja não precisa mais entender de frete. O ganho aparece em isolar o if do resto do código: o acoplamento entre `Loja` e a lógica de frete diminui. Pinho disse isso numa frase: ‘toda vez que uma mudança no código não obriga o `main` a mudar junto, o design melhorou’. De fato, a etapa 3 do `main` só precisa montar a fábrica e injetá-la:

``` python
print("ETAPA 3 - SRP simple factory")
fabrica = FabricaDeFrete()
loja3 = Loja3(fabrica, CalculadoraTotal(), Recibo())
print(loja3.processar(cliente, valor, peso_kg, 'Sao Paulo'))
print(loja3.processar(cliente, valor, peso_kg, 'Manaus'))
custo = SimuladorDeFrete(fabrica).simular("Belém", peso_kg)

print("Simulação Belém", custo)
```

Note que essa última linha ainda esconde o mesmo bug do `else`. Como `FabricaDeFrete.criar` só reconhece `'Sao Paulo'` e `'Manaus'`, simular pra “Belém” cai no `else` e devolve `FreteRodoviario`, o que pode não ser o certo pro caso.

Nesse ponto a aula sai do código e coloca o Simple Factory dentro de um vocabulário maior de arquitetura. O professor ajuda a definir alguns termos, que vou definir melhor aqui, não exatamente do jeito dito: um **padrão de projeto** é uma saída clássica, já testada, para um problema recorrente de modelagem; a referência dada foi o livro de 1994 do **GoF** (Gang of Four).

O GoF organiza os 23 padrões do livro de 1994 em três famílias: **padrões criacionais** (como criar objetos — Factory Method, Abstract Factory, Builder, Prototype, Singleton), **padrões estruturais** (como compor classes e objetos — Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy) e **padrões comportamentais** (como objetos interagem e distribuem responsabilidade — Observer, Strategy, State, Template Method, entre outros). O Simple Factory é um idioma didático, usado como degrau pra chegar no Factory Method — esse sim um dos criacionais reconhecidos pelo GoF.

<a id="termos-da-aula-2"></a>
<a id="secao-9"></a>

## Termos da Aula 2

- **Simple Factory** — classe cujo único trabalho é decidir qual objeto concreto criar, tirando essa decisão de quem consome o objeto.

- **Padrão de projeto (design pattern)** — solução clássica e já testada pra um problema recorrente de modelagem orientada a objetos; catalogados no livro do GoF (1994).

- **GoF (Gang of Four)** — apelido dos quatro autores do livro **Design Patterns** (1994).

- **Padrão criacional** — categoria de padrão de projeto que resolve “qual é a forma correta de criar um objeto” (Simple Factory, Factory Method, Builder, Singleton).

- **Factory Method** — cada subclasse decide, via método abstrato sobrescrito, qual objeto concreto criar; substitui o if por polimorfismo.

- **Polimorfismo** — objetos de subclasses diferentes respondem à mesma chamada de método, cada um à sua maneira.

- **OCP (Open/Closed Principle)** — uma classe deve estar fechada para modificação e aberta para extensão; o O do SOLID.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: Notas de aula](../../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Anterior: [Termos da Aula 1](../aula-1-documentacao-contratos-e-srp/index.md#termos-da-aula-1)
- Próximo: [Aula 3 - Builder e Singleton](../aula-3-builder-e-singleton/index.md)
