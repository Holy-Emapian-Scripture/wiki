---
layout: "default"
title: "Factory Method — Aula 2 - Simple Factory, Factory Method e OCP"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 8
---

[Engenharia de Software](../../index.md) · [Aula 2 - Simple Factory, Factory Method e OCP](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-8"></a>

# Factory Method

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

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Notas de aula](../../../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Anterior: [Simple Factory](../simple-factory/index.md)
- Próximo: [Termos da Aula 2](../termos-da-aula-2/index.md)
