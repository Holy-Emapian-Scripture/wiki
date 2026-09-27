---
layout: "default"
title: "Aula 1 - Documentação, Contratos e SRP"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 1
---

[Engenharia de Software](index.md)

<!-- wiki:original:inicio -->

<a id="secao-1"></a>

# Aula 1 - Documentação, Contratos e SRP


<a id="cacto"></a>
<a id="secao-2"></a>

## Cacto

A loja vende cactos — cada um com nome, preço e altura — e monta pedidos com vários itens:

``` python
class Cacto:
    def __init__(self, nome, preco, altura_cm):
        self.nome = nome
        self.preco = preco
        self.altura_cm = altura_cm


class ItemPedido:
    def __init__(self, cacto, quantidade):
        self.cacto = cacto
        self.quantidade = quantidade
```

Exemplo de **design by contract** citado em aula: o `__init__` de `ItemPedido` já declara, o que consome pra funcionar — um `cacto` e uma `quantidade`. Só que, como o próprio comentário no código admite, nada garante que `cacto` é de fato um `Cacto`. Documentar com docstring é pedir pra quem for usar a classe seguir o combinado: Python é fracamente tipado, então nada impede alguém de passar qualquer coisa ali. A saída ingênua seria verificar o tipo dentro do `__init__`, mas fazer esse tipo de verificação em todos os métodos e todos os parâmetros deixa o programa lento. Aí que entra o termo dito pelo Pinho: você declara o comportamento esperado e confia que quem chamou respeitou, em vez de reverificar tudo o tempo todo.

Na média, tudo que é interno ao sistema é tratado assim, e a verificação de fato só entra quando o sistema recebe algo de fora dele. Se um contrato não é respeitado, a consequência pode ser tão grave quanto o caso citado em aula do foguete da NASA que explodiu (não explodiu, mas **ver**).

Continuando o código, o pedido guarda os dados do cliente e a lista de itens:

``` python
class Pedido:
    def __init__(self, cliente, email, cep, tipo_entrega, cupom, numero_cartao):
        self.cliente = cliente
        self.email = email
        self.cep = cep
        self.tipo_entrega = tipo_entrega
        self.cupom = cupom
        self.numero_cartao = numero_cartao
        self.itens = []
```

E a entrega tem quatro formas possíveis, todas implementando o mesmo contrato abstrato:

``` python
class Entrega(ABC):
    @abstractmethod
    def calcular_frete(self, peso_kg, cep):
        ...

    @abstractmethod
    def prazo_em_dias(self, cep):
        ...

    @abstractmethod
    def codigo_rastreio(self):
        ...


class Sedex(Entrega):
    def calcular_frete(self, peso_kg, cep):
        base = 18.90 + peso_kg * 2.35
        if cep.startswith("6") or cep.startswith("7"):
            base = base * 1.4
        return base

    def prazo_em_dias(self, cep):
        return 2 if cep.startswith("0") else 5

    def codigo_rastreio(self):
        return "BR314159265BR"


class Drone(Entrega):
    def calcular_frete(self, peso_kg, cep):
        base = 49.90 + peso_kg * 8.0
        if peso_kg > 3.0:
            base = base + 60.0
        return base

    def prazo_em_dias(self, cep):
        return 1

    def codigo_rastreio(self):
        return "DRN-8080"


class PomboCorreio(Entrega):
    def calcular_frete(self, peso_kg, cep):
        return 4.50 + peso_kg * 0.75

    def prazo_em_dias(self, cep):
        return

    def codigo_rastreio(self):
        return "OLHE-PARA-O-CEU"


class CarrocaDeBoi(Entrega):
    def calcular_frete(self, peso_kg, cep):  # nao usa o cep
        return 9.90 + peso_kg * 0.40

    def prazo_em_dias(self, cep):  # nao usa o cep
        return 30

    def codigo_rastreio(self):
        return "BOI-0404"
```

Tudo isso converge pro método onde o professor usa os termos como **code smell** e **god class**: `ProcessadorDePedido.processar` calcula subtotal, aplica desconto, calcula peso, decide a entrega, calcula frete e imposto, valida cartão, grava em “banco”, manda e-mail, imprime nota fiscal e loga — tudo junto, num só lugar:

``` python
class ProcessadorDePedido:
    def processar(self, pedido):
        subtotal = 0
        for item in pedido.itens:
            subtotal = subtotal + item.cacto.preco * item.quantidade

        desconto = 0
        if pedido.cupom is not None:
            if pedido.cupom == "NULLSAFE10":
                desconto = subtotal * 0.10
            elif pedido.cupom == "OFFBYONE5":
                desconto = 5.0
            elif pedido.cupom == "HELLOWORLD":
                desconto = subtotal * 0.15
                if desconto > 40.0:  # if devia ta pra fora desse elif
                    desconto = 40.0

        peso_kg = 0
        for item in pedido.itens:
            peso_kg = peso_kg + item.quantidade * (item.cacto.altura_cm * 0.05)

        if pedido.tipo_entrega == "SEDEX":
            entrega = Sedex()
        elif pedido.tipo_entrega == "DRONE":
            entrega = Drone()
        elif pedido.tipo_entrega == "POMBO":
            entrega = PomboCorreio()
        elif pedido.tipo_entrega == "CARROCA":
            entrega = CarrocaDeBoi()
        else:
            entrega = Sedex()  # talvez o sedex n entregue nesse lugar, tem q verificar

        frete = entrega.calcular_frete(peso_kg, pedido.cep)
        base_imposto = subtotal - desconto
        imposto = base_imposto * 0.18
        total = base_imposto + frete + imposto

        if pedido.numero_cartao is None or len(pedido.numero_cartao) != 16:
            raise ValueError("cartao invalido")
        soma = 0
        for c in pedido.numero_cartao:
            if c < "0" or c > "9":
                raise ValueError("cartao invalido")
            soma = soma + int(c)
        if soma % 10 != 0:
            raise ValueError("cartao recusado")

        sql = (
            "INSERT INTO pedidos (cliente, cep, entrega, total) VALUES ('"
            + pedido.cliente + "', '" + pedido.cep + "', '" + pedido.tipo_entrega
            + "', " + f"{total:.2f}" + ")"
        )
        print("[BANCO] " + sql)
        for item in pedido.itens:
            print(
                "[BANCO] INSERT INTO itens (pedido_cliente, cacto, qtd) VALUES ('"
                + pedido.cliente + "', '" + item.cacto.nome + "', "
                + str(item.quantidade) + ")"
            )

        corpo = "<html><body>"
        corpo = corpo + "<h1>Obrigado, " + pedido.cliente + "!</h1>"
        corpo = corpo + "<p>Seus cactos foram compilados sem warnings e entraram na fila de deploy.</p><ul>"
        for item in pedido.itens:
            corpo = corpo + "<li>" + str(item.quantidade) + "x " + item.cacto.nome + "</li>"
        corpo = corpo + "</ul><p>Frete: R$ " + f"{frete:.2f}" + "</p>"
        corpo = corpo + "<p>Total: R$ " + f"{total:.2f}" + "</p>"
        corpo = corpo + "<p>Previsao de entrega: " + str(entrega.prazo_em_dias(pedido.cep)) + " dias</p>"
        corpo = corpo + "</body></html>"
        print("[SMTP] enviando para " + pedido.email)
        print(corpo)

        print("=== NOTA FISCAL ELETRONICA ===")
        print("DESTINATARIO: " + pedido.cliente)
        print("BASE DE CALCULO: " + f"{base_imposto:.2f}")
        print("ICMS 18%: " + f"{imposto:.2f}")
        print("VALOR TOTAL: " + f"{total:.2f}")
        print("==============================")

        print(
            "[LOG] pedido de " + pedido.cliente + " processado com "
            + str(len(pedido.itens)) + " itens, total " + f"{total:.2f}"
        )

        return total
```

Pinho também disse que ‘quanto mais você precisa dar scroll numa função, pior ela é’, ‘código longo com variáveis pouco significativas é ruim de manter” e é ‘pouco provável que você realmente precise de uma classe com $1000$ linhas” (fazendo referência a um código em produção real).

<a id="por-que-o-processar-deveria-ser-varios-metodos-srp"></a>
<a id="secao-3"></a>

## Por que o `processar` deveria ser vários métodos (SRP)

O problema dessa função é que ela tem várias (funções). Se listassemos, quem, na empresa, poderia pedir uma mudança em `ProcessadorDePedido.processar` — e apontando exatamente onde, dentro do método, cada um bateria:

- a **contabilidade** precisar mudar a alíquota — o `0.18` fixo em `imposto = base_imposto * 0.18`;

- o **marketing** criar um cupom novo — o bloco `if pedido.cupom == "NULLSAFE10": ...`

- o **marketing** precisar mudar o e-mail — o bloco que monta `corpo` em HTML e manda pro “SMTP”;

- o **gateway do cartão** mudar — a validação de `numero_cartao` (tamanho, dígitos, soma);

- o **DBA** precisar mudar uma coluna — o `sql = "INSERT INTO pedidos ..."` montado por concatenação de string (que, à parte da aula, também é uma porta aberta pra SQL injection, já que `pedido.cliente` entra direto na query sem tratamento nenhum);

- o **SEFAZ** mudar o layout da nota — o bloco `"=== NOTA FISCAL ELETRONICA ==="`;

- os **Correios** mudarem o modo de calcular o peso — a fórmula `peso_kg = peso_kg + item.quantidade * (item.cacto.altura_cm * 0.05)`;

- o **COO** querer oferecer outra forma de envio — o `if`/`elif` de `tipo_entrega`.

É esse problema que o Princípio de Responsabilidade Única (SRP) corrige: cada componente deve apresentar uma única responsabilidade. É o primeiro dos cinco princípios do SOLID.

<a id="loja-exercicio-de-correcao"></a>
<a id="cod-aula1"></a>

## Loja (exercício de correção)

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

<a id="termos-da-aula-1"></a>
<a id="secao-5"></a>

## Termos da Aula 1

- **Docstring, typehint** - Vocês já sabem isso;

- **Design by contract** — declarar o comportamento esperado de um componente (o que ele espera receber, o que garante devolver) e confiar nisso, em vez de reverificar tudo em tempo de execução.

- **Defeito (fault/bug)** — falha concreta e localizável no código-fonte, que existe independente de ser executada.

- **Falha (failure)** — comportamento incorreto observável quando o programa roda e um defeito é de fato acionado.

- **Code smell** — sintoma de que o design do código está ruim, mesmo funcionando sem erros; o “cheiro” de um problema estrutural.

- **God class** — classe (ou método) que sabe e faz coisas demais, concentrando responsabilidades que deveriam estar separadas.

- **SRP (Princípio de Responsabilidade Única)** — cada componente deve ter um único motivo pra mudar; o S do SOLID.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: Notas de aula](../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Próximo: [Aula 2 - Simple Factory, Factory Method e OCP](aula-2-simple-factory-factory-method-e-ocp.md)
