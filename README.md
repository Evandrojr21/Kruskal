## Contextualização:
Augusto e seus amigos estão participando da Olimpíada brasileira de programação,
como desafio tiveram que criar uma árvore geradora mínima, utilizando como base os
municípios do estado do Rio de Janeiro e a distância entre eles. Eles escolheram o
algoritmo de Kruskal, já que ele funciona melhor em situações típicas (gráficos
esparsos), porque usa estruturas de dados mais simples. O único material que foi
fornecido para eles foi o mapa do estado do Rio de Janeiro, sendo assim, foi
necessário obter as distâncias entre os Municípios.
Para conseguir criar uma base de dados, optaram por desenvolver uma planilha
contendo cada município e seus limítrofes, juntamente com a respectiva distância
entre eles, a fim de formar um grafo e implementá-lo no algoritmo. Sendo assim,
cada município representa um nó do grafo, as conexões com seus limítrofes
representam as arestas e as distâncias representam os pesos do grafo.
Utilizando uma imagem do estado do Rio de Janeiro e seus municípios:

[Imagem do Rio de janeiro](http://www.hemorio.rj.gov.br/Html/Hemorrede_mapa.htm/)

Com isso, pegaram a distância de cada municipio para o seus municípios limítrofes
,a partir disto, foi possível formular uma planilha contendo os vértices
(municípios) de origem e destino, com seus respectivos pesos, que seriam
representados pela distância entre um município e outro.

[Acesso a planilha](https://docs.google.com/spreadsheets/d/e/2PACX-1vRIUrtwIgc5Q6mud0Ewy_yp2xDa-ifIYGSSDJk8diCs_UkqP8vwR8Fupqm6b0MViZ59MilRHt6NSwVV/pubhtml/)

E com isso, foi utilizado o site distâncias entre cidades para calcular a distância de um município para
o seu município limítrofe:

http://www.distanciascidades.com/pesquisa/

E levou em consideração a distância em linha reta. E a partir disso, fizeram a sua base de dados:

[Acesso a Base de dados](https://docs.google.com/document/d/1da6ISjLWCKuLpxcQTF3sdU7w0qIhW6Fii_tKTMWk5ms/edit?usp=sharing/)

## Implementação
Para resolver o problema, após a obtenção dos dados , sabendo que seria necessário obter uma árvore
geradora mínima, foi utilizado o algoritmo de Kruskal , visto que, tem um
desempenho de O(m log n) e em casos de gráficos mais esparsos se torna mais
favorável, quando comparado com o algoritmo de Prim, que também pode ser
utilizado para encontrar a árvore geradora mínima.
### 👨‍💻️ Tecnologia Utilizada
- [Python](https://www.python.org/)

## Grupo
- Alexandre de Souza Cabral
- Evandro de Souza Santos Júnior
- Gabrielle Almeida de Oliveira

### Mais detalhes sobre o Projeto
Segue um link para um vídeo com mais detalhes sobre a implementação e uma explicação mais detalhada
sobre o nosso projeto.

 [Video do nosso Projeto](https://www.youtube.com/watch?v=gxioIVE1ZII/)


