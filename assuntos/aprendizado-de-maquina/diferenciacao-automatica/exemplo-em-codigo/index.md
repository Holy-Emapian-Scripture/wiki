---
layout: "default"
title: "Exemplo em código — Diferenciação Automática"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A2.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 8
---

[Aprendizado de Máquina](../../index.md) · [Diferenciação Automática](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-8"></a>

# Exemplo em código

``` python
class SinLayer:
  def forward(self, x):
    self.x = x
    return np.sin(x)

  def backward(self, dout):
    dx = dout * np.cos(self.x)
    return dx


class SquaredLayer:
  def forward(self, x):
    self.x = x
    return x ** 2

  def backward(self, dout):
    dx = dout * 2 * self.x
    return dx


class ModuleList:
  def __init__(self, layers = None):
    self.layers = layers or []

  def forward(self, x):
    for layer in self.layers:
      x = layer.forward(x)
    return x

  def backward(self, dout):
    for layer in reversed(self.layers):
      dout = layer.backward(dout)
    return dout

import numpy as np

class SinLayer:
    def forward(self, x):
        self.x = x
        return np.sin(x)

    def backward(self, dout):
        return dout * np.cos(self.x)


class SquaredLayer:
    def forward(self, x):
        self.x = x
        return x ** 2

    def backward(self, dout):
        return dout * 2 * self.x


class ModuleList:
    def __init__(self, layers=None):
        self.layers = layers or []

    def forward(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def backward(self, dout=1):
        for layer in reversed(self.layers):
            dout = layer.backward(dout)
        return dout


# Função f representando sin^2(x)
f = ModuleList([
    SinLayer(),
    SquaredLayer()
])

x = 2

y = f.forward(x)
dy = f.backward()

print(y)   # 0.8268218104...
print(dy)  # -0.7568024953...
```

------------------------------------------------------------------------

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/aprendizado-de-maquina/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a2.md#apresentacao-original)

- Anterior: [Diferenciação Automática reverse-mode](../diferenciacao-automatica-reverse-mode/index.md)
- Próximo: [Processos Gaussianos](../../processos-gaussianos/index.md)
