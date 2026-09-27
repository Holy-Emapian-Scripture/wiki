---
layout: "default"
title: "Aula 4 - Abstract Factory"
tipo: "conteudo"
disciplina: "Engenharia de Software"
origem: "6 semestre/Engenharia de Software/Exp.md"
trilha: "../../../trilhas/engenharia-de-software/notas-de-aula.md"
nav_exclude: true
render_with_liquid: false
semestre: 6
autores: ["Thalis Ambrosim Falqueto"]
ano_original: 2026
ordem_na_trilha: 14
---

[Engenharia de Software](../index.md)

<!-- wiki:original:inicio -->

<a id="secao-16"></a>

# Aula 4 - Abstract Factory


<a id="abstract-factory"></a>
<a id="secao-17"></a>

## Abstract Factory

A solução pro problema de criar algo generalizável de acordo com o sistema é criar uma fábrica que produz, de uma vez, todos os widgets daquele sistema. Cada produto (calendário, clima) continua sendo decidido por um Factory Method, igual ao que já vimos, só que agora vários desses métodos moram juntos, na mesma fábrica:

``` python
from abc import ABC, abstractmethod

class UIFactory(ABC):
    @abstractmethod
    def create_calendar(self): ...

    @abstractmethod
    def create_weather(self): ...

class iPadOSFactory(UIFactory):
    def create_calendar(self):
        print("Factory da Plataforma iPadOS: Calendário")
        widget = iPadOSCalendarWidget()
        widget.create_calendar()
        return widget

    def create_weather(self):
        print("Factory da Plataforma iPadOS: Clima")
        widget = iPadOSWeatherWidget()
        widget.create_weather()
        return widget

class iOSFactory(UIFactory):
    def create_calendar(self):
        print("Factory da Plataforma iOS: Calendário")
        widget = iOSCalendarWidget()
        widget.create_calendar()
        return widget

    def create_weather(self):
        print("Factory da Plataforma iOS: Clima")
        widget = iOSWeatherWidget()
        widget.create_weather()
        return widget


class CalendarWidget(ABC):
    @abstractmethod
    def create_calendar(self): ...

class iPadOSCalendarWidget(CalendarWidget):
    def create_calendar(self):
        print("Criando um calendário para iPadOS")

class iOSCalendarWidget(CalendarWidget):
    def create_calendar(self):
        print("Criando um calendário para iOS")


class WeatherWidget(ABC):
    @abstractmethod
    def create_weather(self): ...

class iPadOSWeatherWidget(WeatherWidget):
    def create_weather(self):
        print("Criando um painel climático para iPadOS")

class iOSWeatherWidget(WeatherWidget):
    def create_weather(self):
        print("Criando um painel climático para iOS")


class ApplicationInterface:
    def get_factory(self, platform_type):
        if platform_type == "iPadOS":
            return iPadOSFactory()
        if platform_type == "iOS":
            return iOSFactory()

        raise ValueError("Esta plataforma não existe")


application_interface = ApplicationInterface()

print("***** iPadOS *****")
widget_factory = application_interface.get_factory("iPadOS")
widget_factory.create_calendar()
widget_factory.create_weather()

print("***** iOS *****")
widget_factory = application_interface.get_factory("iOS")
widget_factory.create_calendar()
widget_factory.create_weather()
```

(Reparo à parte: no material original da aula, `create_calendar` e `create_weather` da `UIFactory` criavam o widget e chamavam o método dele sem `return` — o widget criado era descartado, e `widget_factory.create_calendar()` sempre devolvia `None`. Funcionava pro demo porque tudo acontecia via `print`, mas quebrava o contrato usual de um Factory Method, que é devolver o produto pra quem pediu. Um `return` sozinho na frente da chamada não teria resolvido, porque o problema se repetia um nível abaixo — `iPadOSCalendarWidget().create_calendar()` também não tinha `return`. O código acima já está corrigido: cada método guarda o widget numa variável, chama o método dele pelo efeito colateral do `print`, e devolve o próprio widget — não o resultado de chamar `create_calendar()` nele. Assim `widget_factory.create_calendar()` devolve um `CalendarWidget` de verdade, que quem chamou pode guardar e usar depois. O exemplo de ciência de dados logo abaixo já seguia esse contrato desde o início: cada `create_X` devolve o objeto (`return PandasDatasetLoader()`), em vez de só imprimir e descartar.)

“Ao escolher uma fábrica, todo o restante do programa se adequa a ela”: quem pede um widget a `iPadOSFactory` nunca recebe, por engano, um widget de iOS — os dois métodos vivem na mesma classe, então saem garantidamente da mesma família. `ApplicationInterface.get_factory` é o ponto único de decisão — mesma forma do `FabricaDeFrete.criar`, um `if` que devolve objetos diferentes.

Isso é **Abstract Factory**: “um padrão de projeto criacional que permite produzir famílias de objetos relacionados ou dependentes sem especificar suas classes concretas”. E, como o próprio material registra, “as classes de Abstract Factory frequentemente são baseadas em um conjunto de Factory Methods” — `create_calendar` e `create_weather`, cada um isolado, já é um Factory Method; o Abstract Factory só os empacota juntos.

<a id="secao-18"></a>

### Herança vs. composição

A diferença entre os dois padrões não é a quantidade de métodos — é **como** a variação acontece. Factory Method varia por herança: pra trocar de família, você troca de classe. `CentroSaoPaulo` e `CentroManaus` são subclasses diferentes de `CentroDeDistribuicao`; a identidade da classe já carrega a decisão.

Abstract Factory varia por composição: a classe que usa a fábrica nunca muda. `ApplicationInterface` é uma classe só, do início ao fim — o que muda é qual objeto está guardado dentro dela (`iPadOSFactory()` ou `iOSFactory()`), recebido como retorno de um método, nunca por herança. É o mesmo mecanismo que já existia desde o Simple Factory (`Loja3` guardando `self.fabrica`, sem herdar de `FabricaDeFrete`) — só que agora a fábrica guardada tem vários métodos de criação em vez de um.

<a id="secao-19"></a>

### Por que se usa mais Abstract Factory do que Factory Method?

Fica a pergunta em aberto na aula: “se usa muito mais o abstract factory do que o factory method (porque?)”. A resposta é que sistemas reais raramente precisam criar uma coisa isolada — quase sempre precisam de várias coisas que têm que combinar entre si. O segundo exemplo de aula, um pipeline de ciência de dados, mostra isso com três produtos em vez de dois — “mais uma classe com 3 métodos, a fábrica cria as mesmas classes, com as funções definidas antes”:

``` python
from abc import ABC, abstractmethod

## ABSTRAÇÕES (produtos) - o cliente conhece apenas isso

class DatasetLoader(ABC):
    @abstractmethod
    def load(self) -> None: ...

class Model(ABC):
    @abstractmethod
    def train(self) -> None: ...

class Visualizer(ABC):
    @abstractmethod
    def plot(self) -> None: ...

## ABSTRAÇÃO DA FÁBRICA - contrato da família de produtos

class DataScienceFactory(ABC):
    @abstractmethod
    def create_dataset_loader(self) -> DatasetLoader: ...

    @abstractmethod
    def create_model(self) -> Model: ...

    @abstractmethod
    def create_visualizer(self) -> Visualizer: ...

## PRODUTOS CONCRETOS - Família Local (Pandas / Sklearn / Matplotlib)

class PandasDatasetLoader(DatasetLoader):
    def load(self) -> None:
        print("[PandasDatasetLoader] Lendo CSV local com pandas.read_csv(...). Amostras: 10_000")

class SklearnModel(Model):
    def train(self) -> None:
        print("[SklearnModel] Treinando LogisticRegression(solver=\"lbfgs\"). Acurácia de validação: 0.89")

class MatplotlibVisualizer(Visualizer):
    def plot(self) -> None:
        print("[MatplotlibVisualizer] Plotando curva ROC e matriz de confusão com Matplotlib.")

## PRODUTOS CONCRETOS - Família Distribuída (Spark / MLlib / Seaborn)

class SparkDatasetLoader(DatasetLoader):
    def load(self) -> None:
        print("[SparkDatasetLoader] Lendo dados no cluster: spark.read.parquet(\"s3://bucket/dataset\"). Linhas: 120_000_000")

class MLlibModel(Model):
    def train(self) -> None:
        print("[MLlibModel] Treinando RandomForestClassifier em cluster (MLlib). AUC de validação: 0.92")

class SeabornVisualizer(Visualizer):
    def plot(self) -> None:
        print("[SeabornVisualizer] Gerando pairplot e heatmap de correlação com Seaborn.")

## FÁBRICAS CONCRETAS - produzem uma FAMÍLIA coerente de produtos

class LocalPandasFactory(DataScienceFactory):
    """Família "local" para dados pequenos/medianos."""
    def create_dataset_loader(self) -> DatasetLoader:
        return PandasDatasetLoader()

    def create_model(self) -> Model:
        return SklearnModel()

    def create_visualizer(self) -> Visualizer:
        return MatplotlibVisualizer()

class DistributedSparkFactory(DataScienceFactory):
    """Família "distribuída" para grandes volumes de dados."""
    def create_dataset_loader(self) -> DatasetLoader:
        return SparkDatasetLoader()

    def create_model(self) -> Model:
        return MLlibModel()

    def create_visualizer(self) -> Visualizer:
        return SeabornVisualizer()

## "SELETOR" DE FÁBRICA - ponto único de decisão concreta

class ApplicationInterface:
    def get_factory(self, stack: str) -> DataScienceFactory:
        if stack == "local":
            return LocalPandasFactory()
        if stack == "distributed":
            return DistributedSparkFactory()
        raise ValueError("Stack inválida. Use \"local\" ou \"distributed\".")


app = ApplicationInterface()

print("\n===== Cenário A: Pipeline LOCAL (dados pequenos/medianos) =====")
factory = app.get_factory("local")        # cliente recebe a FÁBRICA (abstração)
loader = factory.create_dataset_loader()  # abstração DatasetLoader
modelo = factory.create_model()           # abstração Model
viz = factory.create_visualizer()         # abstração Visualizer
loader.load()
modelo.train()
viz.plot()

print("\n===== Cenário B: Pipeline DISTRIBUÍDO (big data) =====")
factory = app.get_factory("distributed")  # troca a família, sem mudar o cliente
loader = factory.create_dataset_loader()
modelo = factory.create_model()
viz = factory.create_visualizer()
loader.load()
modelo.train()
viz.plot()
```

O cliente “só precisa conhecer as abstrações das nossas fábricas” — nunca importa `SklearnModel` nem `SparkDatasetLoader` diretamente, só `DataScienceFactory`. Fica também a régua de quando é seguro mexer: “o que pode mudar à vontade é acrescentar classes; classe concreta você não pode mudar” sem quebrar quem já depende dela — trocar o modelo de dentro de `LocalPandasFactory` é seguro; mudar a assinatura de `DataScienceFactory` (a abstração) afeta todo mundo que já depende dela.

<a id="secao-20"></a>

### Voltando pra Loja

A aula fecha puxando de volta pro exemplo que já vínhamos construindo: “se eu quiser ter uma calculadora de frete e recibo diferente pra cada estado, o que fazer?” A resposta sugerida nas anotações é dar um Factory Method pra cada peça que precisa variar (`criar_frete`, `criar_calculadora`, `criar_recibo`) e empacotar as três dentro de um Abstract Factory por centro. Um jeito de fazer isso, seguindo os dois exemplos acima:

``` python
class ComponentesDeCentro(ABC):
    @abstractmethod
    def criar_frete(self): ...

    @abstractmethod
    def criar_calculadora(self): ...

    @abstractmethod
    def criar_recibo(self): ...


class ComponentesSaoPaulo(ComponentesDeCentro):
    def criar_frete(self):
        return FreteRodoviario()

    def criar_calculadora(self):
        return CalculadoraTotalSP()

    def criar_recibo(self):
        return ReciboSP()


class ComponentesManaus(ComponentesDeCentro):
    def criar_frete(self):
        return FreteFluvial()

    def criar_calculadora(self):
        return CalculadoraTotalAM()

    def criar_recibo(self):
        return ReciboAM()


class Loja4:
    def __init__(self, componentes):
        self.componentes = componentes

    def processar(self, cliente, valor, peso_kg, cidade):
        frete = self.componentes.criar_frete()
        calculadora = self.componentes.criar_calculadora()
        recibo = self.componentes.criar_recibo()
        total = calculadora.total(valor, frete.custo(peso_kg))
        return recibo.gerar(cliente, total, cidade)


loja = Loja4(ComponentesSaoPaulo())
print(loja.processar(cliente, valor, peso_kg, "Sao Paulo"))

loja = Loja4(ComponentesManaus())
print(loja.processar(cliente, valor, peso_kg, "Manaus"))
```

`CalculadoraTotalSP`/`CalculadoraTotalAM` e `ReciboSP`/`ReciboAM` são hipotéticos aqui — não existem nas classes já construídas, só ilustram a forma de como a alíquota de ICMS ou o layout de nota variariam por estado. `Loja4` nunca muda de classe entre um pedido de São Paulo e um de Manaus; o que muda é qual `Componentes` foi passado pro construtor.

E reaparece o OCP: “se a gente quiser colocar Belém no frete aéreo, pra fazer isso, teríamos que estender de `Frete`, sem precisar modificar, só estendendo — copia o `FreteFluvial` e bota `Aereo`” — a mesma `FreteAereo` que já ficou pronta, esperando, lá na Aula 2.

<a id="termos-da-aula-4"></a>
<a id="secao-21"></a>

## Termos da Aula 4

- **Abstract Factory** — padrão criacional que produz uma família inteira de objetos relacionados através de uma única fábrica, trocável por composição.

- **Composição** — relação “tem-um”: um objeto guarda uma referência a outro em vez de herdar dele; trocar o comportamento é trocar o objeto guardado, não a classe.

- **Família de produtos** — conjunto de objetos relacionados que precisam ser usados juntos e saem garantidamente compatíveis entre si, por virem da mesma fábrica concreta.

<!-- wiki:original:fim -->


## Percurso de estudo

[Trilha: Notas de aula](../../../trilhas/engenharia-de-software/notas-de-aula.md) · [Apresentação e contexto da fonte](../../../trilhas/engenharia-de-software/notas-de-aula.md#apresentacao-original)

- Anterior: [Termos da Aula 3](../aula-3-builder-e-singleton/index.md#termos-da-aula-3)
- Próximo: [Termos da Aula 4](#termos-da-aula-4)
