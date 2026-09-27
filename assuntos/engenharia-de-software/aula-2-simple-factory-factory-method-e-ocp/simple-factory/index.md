---
layout: "default"
title: "Simple Factory — Aula 2 - Simple Factory, Factory Method e OCP"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 7
---

[Engenharia de Software](../../index.md) · [Aula 2 - Simple Factory, Factory Method e OCP](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-7"></a>

# Simple Factory

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

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Notas de aula](../../../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Anterior: [Aula 2 - Simple Factory, Factory Method e OCP](../index.md)
- Próximo: [Factory Method](../factory-method/index.md)
