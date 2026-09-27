---
layout: "default"
title: "Loja (exercício de correção) — Aula 1 - Documentação, Contratos e SRP"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 4
---

[Engenharia de Software](../../index.md) · [Aula 1 - Documentação, Contratos e SRP](../index.md)

<!-- wiki:original:inicio -->
<a id="cod-aula1"></a>

# Loja (exercício de correção)

O professor exemplifica a solução numa loja simplificada que faz somente o frete, produto e recibo, pra refatorar passo a passo. A etapa 1 comete o mesmo erro numa escala menor:

``` python
class Loja1:
    def processar(self, cliente, valor, peso_kg, centro):
        if centro == 'Sao Paulo':
            frete = 10.0 + 2.0 * peso_kg
        elif centro == 'Manaus':
            frete = 25.0 + 1.2 * peso_kg
        else:
            frete = 10.0 + 2.0 * peso_kg

        total = valor + frete
        return f'{cliente} pagou R$ {total:.2f} (envio de  {centro})'
```

A etapa 2 divide `Loja1` em peças, cada uma cuidando de uma única coisa — calcular o total, gerar o recibo, e decidir o custo do frete, com uma subclasse por tipo de frete:

``` python
class Frete(ABC):
    @abstractmethod
    def custo(self, peso_kg):
        ...

class FreteRodoviario(Frete):
    def custo(self, peso_kg):
        return 10.0 + 2.0 * peso_kg

class FreteFluvial(Frete):
    def custo(self, peso_kg):
        return 25.0 + 1.2 * peso_kg

class CalculadoraTotal:
    def total(self, valor, frete):
        return valor + frete

class Recibo:
    def gerar(self, cliente, total, centro):
        return f'{cliente} pagou R$ {total:.2f} (envio de  {centro})'


class Loja2:
    def __init__(self, calculadora, recibo):
        self.calculadora = calculadora
        self.recibo = recibo

    def processar(self, cliente, valor, peso_kg, centro):
        if centro == 'Sao Paulo':
            frete = FreteRodoviario()
        elif centro == 'Manaus':
            frete = FreteFluvial()
        else:
            frete = FreteRodoviario()

        total = self.calculadora.total(valor, frete.custo(peso_kg))

        return self.recibo.gerar(cliente, total, centro)
```

Agora, `Loja2` ainda tem um `if`, decidindo qual objeto usar, mas não faz mais o cálculo do frete nem monta o recibo. Rodando as duas etapas lado a lado, o resultado é o mesmo, mas a segunda já está pronta pra crescer sem precisar reescrever tudo de novo:

``` python
cliente = 'Ada'
valor = 100
peso_kg = 2

print('etapa 1 - tudo cagado')
loja1 = Loja1()
print(loja1.processar(cliente, valor, peso_kg, 'Sao Paulo'))
print(loja1.processar(cliente, valor, peso_kg, 'Manaus'))

print('etapa 2 - SRP dominado')
loja2 = Loja2(CalculadoraTotal(), Recibo())
print(loja2.processar(cliente, valor, peso_kg, 'Sao Paulo'))
print(loja2.processar(cliente, valor, peso_kg, 'Manaus'))
```

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: Notas de aula](../../../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Anterior: [Por que o `processar` deveria ser vários métodos (SRP)](../por-que-o-processar-deveria-ser-varios-metodos-srp/index.md)
- Próximo: [Termos da Aula 1](../termos-da-aula-1/index.md)
