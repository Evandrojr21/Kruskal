class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.conectados = {} #recebe os destinos

    def add_adjacente(self, municipio_destino, peso_total=0):
        self.conectados[municipio_destino] = peso_total

class Grafo:
    def __init__(self):
        self.dicionario_vertices = {}

    def addvertice(self, name):
        self.dicionario_vertices[name] = Vertice(name)

    def addaresta(self, origem, destino, peso_total):
        if origem not in self.dicionario_vertices:
            self.addvertice(origem)
        if destino not in self.dicionario_vertices:
            self.addvertice(destino)
        self.dicionario_vertices[origem].add_adjacente(destino, peso_total)

class Kruskal:
    def __init__(self, grafo):
        self.arestas = {}
        self.sets = {}

        for x in grafo.dicionario_vertices.keys():
            conexoes = grafo.dicionario_vertices[x].conectados # listar as adjacencia entre os municipios
            #listar as conexoes , de cada vertice
            for y in conexoes.keys():
                nome_aresta = x + '-' + y
                inverso = y + '-' + x
                # atribuir o valor dos pesos a aresta
                if inverso not in self.arestas.keys():
                    self.arestas[nome_aresta] = conexoes[y]

        self.arestas = sorted(self.arestas.items(), key=lambda x: (x[1], x[0]))

        for n in grafo.dicionario_vertices.keys(): #criar um conjunto em forma de dupla para cada vértice e assim receber depois
            self.sets[n] = [n, 1]

    # busca uma subarvore que contenha filho
    def findSetParent(self, filho):
        if (self.sets[filho][0] == filho):
            return filho
        else:
            return self.findSetParent(self.sets[filho][0])

    # fazer a união do vertice u e do vertice v
    def union(self, u, v):  # conectar as duas subarvores, uma contem o nó de u e a outra o nó de v
        # encontra a subarvore e comparar e conectar a menor a uma maior
        if (self.sets[self.findSetParent(u)][1] > self.sets[self.findSetParent(v)][1]):
            self.sets[v][0] = self.sets[u][0]
        elif (self.sets[self.findSetParent(u)][1] > self.sets[self.findSetParent(v)][1]):
            self.sets[u][0] = self.sets[v][0]
        else:
            self.sets[self.findSetParent(u)][0] = self.sets[v][0]
            self.sets[self.findSetParent(v)][1] += 1

    def mst(self, grafo):
        T = []
        lista_km = []
        for x in self.arestas:
            u, v = x[0].split('-')
            # verififcar se os conjuntos são disjuntos , se estão diferentes
            if self.findSetParent(u) != self.findSetParent(v):
                T.append(x)
                self.union(u, v)
                #fazer a união

        peso_total = 0
        arestas_string = ''
        for x in T:
            peso_total += x[1]
            arestas_string += x[0] + ', '
            percorrido = str(x[1])
            lista_km.append(percorrido +' km')

        arestas_string = arestas_string[:len(arestas_string) - 2]
        print(" A árvore Geradora mínima encontrada, foi a seguinte: " + arestas_string)
        print("---------------------------------------------------------------------------------------------"
              "------------------------------------------------------\nobs: lembrando que cada numeração presente no resultado final corresponde aos municípios especificados acima\n")
        print(f"Respectivas distancias percorridas de cada elemento da árvore: {lista_km}")


g = Grafo()
dados = open("Base_dados", "r")
with dados:
    for linha in dados:
        municipio_origem, destino, distancia = linha.split()
        g.addaresta(municipio_origem, destino, float(distancia))

print('especificações dos municípios:\n1:porciuncula\n2:VARRE-SAI\n3:NATIVIDADE\n4:BOM JESUS ITABAPOANA\n5:ITAPERUNA\n6:CAMPO DOS GOYTACAZES\n7:ITALVA\n8:CAMBUCI\n9:SÃO JOSÉ DE UBÁ\n10:LAJE DO MURIAÉ\n11:MIRACEMA\n12:CARDOSO MOREIRA\n13:SÃO FIDELIS\n14:SANTA MARIA MADALENA\n15:SÃO JOÃO DA BARRA\n16:SÃO FRANCISCO DE ITABAPOANA\n17:QUISSAMÃ\n18:CONCEIÇÃO DE MACABU\n19:ITAOCARA\n20:APERIBÉ\n21:SANTO ANTONIO DE PÁDUA\n22:TRAJANO DE MORAES\n23:SÃO SEBASTIÃO DO ALTO\n24:CARAPEBUS'
    '\n25:MACAÉ\n26:CANTAGALO\n27:NOVA FRIBURGO\n28:BOM JARDIM\n29:CORDEIRO\n30:MACUCO\n31:CASIMIRO DE ABREU\n32:RIO DAS OSTRAS\n33:DUAS BARRAS\n34:CARMO\n35:SILVA JARDIM\n36:CACHOEIRAS DE MACACU\n37:TERESOPOLIS\n38:CABO FRIO\n39:SUMIDOURO\n40:SAPUCAIA\n41:ARARUAMA\n42:RIO BONITO\n43:ITABORAI\n44:GUAPIMIRIM\n45:PETRÓPOLIS\n46:S JOSE DO VALE DO RIO PRETO\n47:SÃO PEDRO DA ALDEIA\n48:ARRAIAL DO CABO\n49:ARMAÇÃO DE BUZÍOS'
    '\n50:TRÊS RIOS\n51:IGUABA GRANDE\n52:SAQUAREMA\n53:TANGUÁ\n54:MARICÁ\n55:S.GONÇALO\n56:MAGÉ\n57:DUQUE DE CAXIAS\n58:MIGUEL PEREIRA\n59:PATY DOS ALFERES\n60:PARAIBA DO SUL\n61:AREAL\n62:COM.LEVY GASPARIAN\n63:NITEROI\n64:BELFORT ROXO\n65:NOVA IGUAÇU\n66:JAPERI\n67:PARACAMBI\n'
    '68:ENG PAULO DE FRONTIN\n69:VASSOURAS\n70:RIO DAS FLORES\n71:S JOÃO DE MERITI\n72:NILÓPOLIS\n73:QUEIMADOS\n74:MESQUITA \n75:RIO DE JANEIRO\n76:SEROPEDICA\n77:MENDES\n78:PIRAÍ\n79:BARRA DO PIRAÍ\n80:VALENÇA\n81:ITAGUAÍ\n82:RIO CLARO\n83:PINHEIRAL\n84:VOLTA REDONDA\n85:BARRA MANSA\n86:QUATIS\n87:MANGARATIRA\n88:ANGRA DOS REIS\n89:PORTO REAL\n90:RESENDE\n91:PARATI\n92:ITATIAIA'
    '\n---------------------------------------------------------------------------------------------------------------------------------------------------')

k = Kruskal(g)
k.mst(g)