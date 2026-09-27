---
layout: "default"
title: "Expectation-Maximization (EM) para GMMs — Gaussian and Bernoulli Mixture Models"
tipo: "conteudo"
disciplina: "Aprendizado de Máquina"
origem: "5 semestre/Machine Learning/A3.md"
trilha: "../../../../trilhas/aprendizado-de-maquina/a3.md"
nav_exclude: true
render_with_liquid: false
semestre: 5
autores: ["João Pedro Jerônimo", "Eduardo Adame"]
ano_original: 2026
ordem_na_trilha: 12
---

[Aprendizado de Máquina](../../index.md) · [Gaussian and Bernoulli Mixture Models](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-12"></a>

# Expectation-Maximization (EM) para GMMs

Para facilitar o entendimento das contas, defina $N_{k} = \sum_{n = 1}^{N}\gamma(z_{nk})$

<a id="optimal-mean-k"></a>

**Teorema**

Fixando os parâmetros do modelo e variando apenas $\mu$, o valor ótimo de $\mu_{k}$ é dado por: $$\mu_{k} = \frac{\sum_{n = 1}^{N}\gamma(z_{nk})x_{n}}{\sum_{n = 1}^{N}\gamma(z_{nk})} = \frac{1}{N_{k}}\sum_{n = 1}^{N}\gamma(z_{nk})x_{n}$$

**Demonstração**

Para encontrar o valor ótimo de $\mu_{k}$, derivamos a função de log-verossimilhança em relação a $\mu_{k}$ e igualamos a zero: $$\frac{\partial\ln p\left( X~\vert ~\mu,\Sigma,\pi \right)}{\partial\mu_{k}} = \sum_{n = 1}^{N}\underset{\gamma(z_{nk})}{\underbrace{\frac{\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\sum_{j = 1}^{K}\pi_{j}N\left( x_{n}~\vert ~\mu_{j},\Sigma_{j} \right)}}}\frac{1}{N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}\frac{\partial N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\partial\mu_{k}} = 0$$ A derivada da densidade gaussiana em relação a $\mu_{k}$ é dada por: $$\frac{\partial N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\partial\mu_{k}} = N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)\Sigma_{k}^{- 1}\left( x_{n} - \mu_{k} \right)$$ Substituindo isso na equação anterior, obtemos: $$\sum_{n = 1}^{N}\gamma(z_{nk})\Sigma_{k}^{- 1}\left( x_{n} - \mu_{k} \right) = 0$$ Multiplicando ambos os lados por $\Sigma_{k}$, obtemos: $$\sum_{n = 1}^{N}\gamma(z_{nk})\left( x_{n} - \mu_{k} \right) = 0$$ Rearranjando os termos, obtemos: $$\mu_{k}\sum_{n = 1}^{N}\gamma(z_{nk}) = \sum_{n = 1}^{N}\gamma(z_{nk})x_{n}$$ Dividindo ambos os lados por $\sum_{n = 1}^{N}\gamma(z_{nk})$, obtemos a expressão desejada para $\mu_{k}$.

<a id="optimal-covariance-k"></a>

**Teorema**

Fixando os parâmetros do modelo e variando apenas $\Sigma$, o valor ótimo de $\Sigma_{k}$ é dado por: $$\Sigma_{k} = \frac{\sum_{n = 1}^{N}\gamma(z_{nk})\left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T}}{\sum_{n = 1}^{N}\gamma(z_{nk})} = \frac{1}{N_{k}}\sum_{n = 1}^{N}\gamma(z_{nk})\left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T}$$

**Demonstração**

Para encontrar o valor ótimo de $\Sigma_{k}$, derivamos a função de log-verossimilhança em relação a $\Sigma_{k}$ e igualamos a zero: $$\frac{\partial\ln p\left( X~\vert ~\mu,\Sigma,\pi \right)}{\partial\Sigma_{k}} = \sum_{n = 1}^{N}\underset{\gamma(z_{nk})}{\underbrace{\frac{\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\sum_{j = 1}^{K}\pi_{j}N\left( x_{n}~\vert ~\mu_{j},\Sigma_{j} \right)}}}\frac{1}{N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}\frac{\partial N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\partial\Sigma_{k}} = 0$$ A derivada da densidade gaussiana em relação a $\Sigma_{k}$ é dada por: $$\frac{\partial N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\partial\Sigma_{k}} = \frac{1}{2}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)\left( \Sigma_{k}^{- 1}\left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T}\Sigma_{k}^{- 1} - \Sigma_{k}^{- 1} \right)$$ Substituindo isso na equação anterior, obtemos: $$\sum_{n = 1}^{N}\gamma(z_{nk})\left( \Sigma_{k}^{- 1}\left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T}\Sigma_{k}^{- 1} - \Sigma_{k}^{- 1} \right) = 0$$ Multiplicando ambos os lados por $\Sigma_{k}$, obtemos: $$\sum_{n = 1}^{N}\gamma(z_{nk})\left( \left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T}\Sigma_{k}^{- 1} - I \right) = 0$$ Rearranjando os termos, obtemos: $$\sum_{n = 1}^{N}\gamma(z_{nk})\left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T} = \sum_{n = 1}^{N}\gamma(z_{nk})\Sigma_{k}$$ Dividindo ambos os lados por $\sum_{n = 1}^{N}\gamma(z_{nk})$, obtemos a expressão desejada para $\Sigma_{k}$.

<a id="optimal-mixing-coefficient-k"></a>

**Teorema**

Fixando os parâmetros do modelo e variando apenas $\pi$, o valor ótimo de $\pi_{k}$ é dado por: $$\pi_{k} = \frac{\sum_{n = 1}^{N}\gamma(z_{nk})}{N} = \frac{N_{k}}{N}$$

**Demonstração**

Sabendo que $\sum_{k}\pi_{k} = 1$, usamos de multiplicadores de lagrange para encontrar o valor ótimo de $\pi_{k}$. Definimos a função lagrangiana como: $$L(\pi,\lambda) = \ln p\left( X~\vert ~\mu,\Sigma,\pi \right) + \lambda\left( \sum_{k = 1}^{K}\pi_{k} - 1 \right)$$ Derivando em relação a $\pi_{k}$ e igualando a zero, obtemos: $$\frac{\partial L}{\partial\pi_{k}} = \frac{\gamma(z_{nk})}{\pi_{k}} + \lambda = 0$$ Isolando $\pi_{k}$, obtemos: $$\pi_{k} = - \frac{\lambda}{\gamma(z_{nk})}$$ Usando a condição de normalização $\sum_{k}\pi_{k} = 1$, podemos encontrar o valor de $\lambda$: $$\sum_{k = 1}^{K} - \frac{\lambda}{\gamma(z_{nk})} = 1$$ Resolvendo para $\lambda$, obtemos: $$\lambda = - \frac{1}{\sum_{k = 1}^{K}\frac{1}{\gamma(z_{nk})}}$$ Substituindo esse valor de $\lambda$ na expressão para $\pi_{k}$, obtemos: $$\pi_{k} = \frac{\gamma(z_{nk})}{\sum_{j = 1}^{K}\gamma(z_{nj})} = \frac{N_{k}}{N}$$

Vale ressaltar que o [\[optimal-mean-k\]](#optimal-mean-k), [\[optimal-covariance-k\]](#optimal-covariance-k) e [\[optimal-mixing-coefficient-k\]](#optimal-mixing-coefficient-k) não representam formas fechadas dos parâmetros do modelo, pois eles dependem de $\gamma(z_{nk})$, que por sua vez depende dos próprios parâmetros do modelo. Portanto, não podemos resolver essas equações diretamente. Em vez disso, usamos o algoritmo EM, que alterna entre calcular $\gamma(z_{nk})$ com os parâmetros atuais (passo E) e atualizar os parâmetros do modelo usando as fórmulas acima (passo M).

**Algoritmo EM**

1.  **function** *EM*($X$) {

    1.  **initialize** $\mu_{k},\Sigma_{k},\pi_{k}$

    2.  **// Passo E**

    3.  $\gamma(z_{nk}) = \frac{\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right)}{\sum_{j = 1}^{K}\pi_{j}N\left( x_{n}~\vert ~\mu_{j},\Sigma_{j} \right)}$

    4.  **// Passo M**

    5.  $N_{k} = \sum_{n = 1}^{N}\gamma(z_{nk})$

    6.  $\mu_{k} = \frac{1}{N_{k}}\sum_{n = 1}^{N}\gamma(z_{nk})x_{n}$

    7.  $\Sigma_{k} = \frac{1}{N_{k}}\sum_{n = 1}^{N}\gamma(z_{nk})\left( x_{n} - \mu_{k} \right)\left( x_{n} - \mu_{k} \right)^{T}$

    8.  $\pi_{k} = \frac{N_{k}}{N}$

    9.  **// Calcular a log-verossimilhança**

    10. $\ln p\left( X~\vert ~\mu,\Sigma,\pi \right) = \sum_{n = 1}^{N}\ln\left\{ \sum_{k = 1}^{K}\pi_{k}N\left( x_{n}~\vert ~\mu_{k},\Sigma_{k} \right) \right\}$

2.  }

<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A3](../../../../trilhas/aprendizado-de-maquina/a3.md) · [Apresentação e contexto da fonte](../../../../trilhas/aprendizado-de-maquina/a3.md#apresentacao-original)

- Anterior: [Máxima Verossimilhança](../maxima-verossimilhanca/index.md)
- Próximo: [Algoritmo EM Variacional](../algoritmo-em-variacional/index.md)
