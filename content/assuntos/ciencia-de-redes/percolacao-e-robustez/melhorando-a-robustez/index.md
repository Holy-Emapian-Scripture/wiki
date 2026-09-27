---
layout: "default"
title: "Melhorando a Robustez — Percolação e Robustez"
tipo: "conteudo"
disciplina: "Ciência de Redes"
origem: "4 semestre/Ciência de Redes/Recaps/A2.md"
trilha: "../../../../trilhas/ciencia-de-redes/a2.md"
nav_exclude: true
render_with_liquid: false
semestre: 4
autores: ["João Pedro Jerônimo"]
ano_original: 2025
ordem_na_trilha: 11
---

[Ciência de Redes](../../index.md) · [Percolação e Robustez](../index.md)

<!-- wiki:original:inicio -->
<a id="secao-11"></a>

# Melhorando a Robustez

Certo, temos uma rede, é possível melhorar a sua tolerância, tanto a ataques, quanto a falhas aleatórias? Um primeiro pensamento que opdemos ter é conectar todos os nós periféricos em um hub, além de conectar eles entre si. Porém, na vida real, isso pode não ser aplicável, tendo em vista que, se cada aresta tem um custo para ser mantida, o custo de manutenção da rede pode exceder o viável

Da para maximizar a robustez para ataques e falhas aleatórias sem alterar o custo? Queremos aumentar o limite $f_{c}$, então temos que aumentar ${\mathbb{E}}\left\lbrack K^{2} \right\rbrack$ sem alterar o custo médio ${\mathbb{E}}\lbrack K\rbrack$. Isso vai ocorrer em uma distribuição **bimodal** onde todo nó tem grau $k_{\min}$ ou $k_{\max}$, seguindo a seguinte distribuição: $$p(k) = (1 - r)\delta(k - k_{\min}) + r\delta(k - k_{\max})$$

onde $r$ é a fração de nós com grau $k_{\max}$. Então vamos querer maximizar: $$f_{c}^{\text{tot}} = f_{c}^{\text{rand}} + f_{c}^{\text{targ}}$$

onde $f_{c}^{\text{rand}}$ é o limite crítico de falhas aleatórias e $f_{c}^{\text{targ}}$ o limite crítico dos ataques direcionados. Dado a distribuição bimodal citada anteriormente: $$\begin{aligned} {\mathbb{E}}\lbrack K\rbrack & = (1 - r)k_{\min} + rk_{\max} \\ {\mathbb{E}}\left\lbrack K^{2} \right\rbrack & = (1 - r)k_{\min}^{2} + rk_{\max}^{2} \end{aligned}$$

substituindo isso em $f_{c}^{\text{rand}}$ $$f_{c}^{\text{rand }} = 1 - \frac{1}{{\mathbb{E}}\frac{\left\lbrack K^{2} \right\rbrack}{\mathbb{E}}\lbrack K\rbrack - 1} = \frac{{\mathbb{E}}\lbrack K\rbrack^{2} - 2rk_{\max}{\mathbb{E}}\lbrack K\rbrack - 2(1 - r){\mathbb{E}}\lbrack K\rbrack + rk_{\max}^{2}}{{\mathbb{E}}\lbrack K\rbrack^{2} - 2rk_{\max}{\mathbb{E}}\lbrack K\rbrack - (1 - r){\mathbb{E}}\lbrack K\rbrack + rk_{\max}^{2}}$$

Agora, para achar $f_{c}^{\text{targ}}$, vamos fazer uma análise mais cuidadosa $$\begin{array}{r} f_{c}^{\text{targ}} > r \Rightarrow \text{ Todos os hubs foram removidos } \\ \Rightarrow f_{c}^{\text{targ}} = r + \frac{1 - r}{{\mathbb{E}}\lbrack K\rbrack - rk_{\max}}\left( {\mathbb{E}}\lbrack K\rbrack\frac{{\mathbb{E}}\lbrack K\rbrack - rk_{\max} - 2(1 - r)}{{\mathbb{E}}\lbrack K\rbrack - rk_{\max} - (1 - r)} - rk_{\max} \right) \end{array}$$ $$\begin{array}{r} f_{c}^{\text{targ}} < r \Rightarrow \text{ Sobrou alguns hubs } \\ \Rightarrow f_{c}^{\text{targ}} = \frac{{\mathbb{E}}\lbrack K\rbrack^{2} - 2r{\mathbb{E}}\lbrack K\rbrack k_{\max} + rk_{\max}^{2} - 2(1 - r){\mathbb{E}}\lbrack K\rbrack}{k_{\max}\left( k_{\max} - 1 \right)(1 - r)} \end{array}$$

E nós estamos procurando o valor de $k$ que maximiza $f_{c}^{\text{tot}}$. Usando as equações encontradas para $f_{c}^{\text{targ}}$ e $f_{c}^{\text{rand}}$, descobrimos que podemos aproximar $k_{\max}$ por: $$\begin{aligned} k_{\max} & \approx Ar^{- \frac{2}{3}} \\ A & = \left\lbrack \frac{2\left( {\mathbb{E}}\lbrack K\rbrack \right)^{2}\left( {\mathbb{E}}\lbrack K\rbrack - 1 \right)^{2}}{2{\mathbb{E}}\lbrack K\rbrack - 1} \right\rbrack^{\frac{1}{3}} \end{aligned}$$

então obtemos que, para $r$ pequeno: $$f_{c}^{\text{tot }} = 2 - \frac{1}{{\mathbb{E}}\lbrack K\rbrack - 1} - \frac{3{\mathbb{E}}\lbrack K\rbrack}{A^{2}}r^{\frac{1}{3}} + O\left( r^{\frac{2}{3}} \right)$$

Para uma rede com $N$ nós, o máximo de $f_{c}^{\text{tot}}$ ocorre com $r = \frac{1}{N}$ $$\Rightarrow k_{\max} = AN^{\frac{2}{3}}$$ ou seja, em redes em que apenas $1$ nó possui grau $k_{\max}$ enquanto o resto possui $k_{\min}$
<!-- wiki:original:fim -->

## Percurso de estudo

[Trilha: A2](../../../../trilhas/ciencia-de-redes/a2.md) · [Apresentação e contexto da fonte](../../../../trilhas/ciencia-de-redes/a2.md#apresentacao-original)

- Anterior: [Tolerância a Ataques](../tolerancia-a-ataques/index.md)
