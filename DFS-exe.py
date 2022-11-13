class Node(object):
    def __init__(self, onoma):
        self.onoma = onoma    
    def get_name(self):
        return self.onoma
    def __str__(self):
        return self.onoma

class Edge(object):
    def __init__(self,pigi,proorismos):
        self.pigi = pigi
        self.proorismos = proorismos
    def get_source(self):
        return self.pigi
    def get_destination(self):
        return self.proorismos
    def __str__(self):
        return self.pigi.get_name() + "->" + self.proorismos.get_name()

class Weighted_ege(Edge):
    def __init__(self,pigi,proorismos,varos = 1.0):
        self.pigi = pigi
        self.proorismos = proorismos
        self.varos = varos
    def get_weight(self):
        return self.varos
    def __str__(self):
        return (f"{self.pigi.get_name()}->({self.varos})" + f"{self.proorismos.get_name()}")
#-------------------------------------------------------------------------------------------
class Digraph(object):
    def __init__(self):
        self.komvoi = []
        self.akmes = {}
    
    def add_node(self,komvos):
        if komvos in self.komvoi:
            raise ValueError("O komvos eiparxei eidi")
        else:
            self.komvoi.append(komvos)
            self.akmes[komvos] = []
    
    def add_edge(self,akmi):
        pigi = akmi.get_source()
        proorismos = akmi.get_dest()
        if not (pigi in self.komvoi and proorismos in self.komvoi):
            raise ValueError("O komvos den anikei sto grafima")
        self.akmes[pigi].append(proorismos)

    def children_of(self,komvos):
        return self.akmes[komvos]

    def has_node(self,komvos):
        return komvos in self.komvoi

    def __str__(self):
        apotelesma = ""
        for pigi in self.komvoi:
            for proorismos in self.akmes[pigi]:
                apotelesma = (apotelesma + pigi.get_name() + "->" + proorismos.get_name() + "\n")
        return apotelesma[:-1]

class Graph(Digraph):
    def add_edge(self,akmi):
        Digraph.add_edge(self,akmi) #return super().add_edge(akmi)
        rvs = Edge(akmi.get_destination(),akmi.get_source())
        Digraph.add_edge(self,rvs)
#------------------------------------------------------------------------------------------------
def print_path(monopati):
    apotelesma = ""
    for i in range(len(monopati)):
        apotelesma = apotelesma + str(monopati[i])
        if i != len(monopati) - 1:
            apotelesma = apotelesma + "->"
    return apotelesma

def DFS(grafos, ekkinisi, termatismos, monopati, sintomotero, ektiposi = False):
    monopati = monopati + [ekkinisi]
    if ektiposi:
        print("Trexousa diadromi DFS: ",print_path(monopati))
    if ekkinisi == termatismos:
        return monopati
    for komvos in grafos.children_of(ekkinisi):
        if komvos not in monopati:
            if sintomotero == None or len(monopati) < len(sintomotero):
                neo_monopati = DFS(grafos, komvos, termatismos, monopati, sintomotero, ektiposi)
                if neo_monopati != None:
                    sintomotero = neo_monopati
    return sintomotero

def sintomotero_monopati(grafos, ekkinisi, termatismos, ektiposi = False):
    return DFS(grafos, ekkinisi, termatismos, [], None, ektiposi)

#Ektelesi
def ektelesi():
    komvoi = []
    for onoma in range(5): #Dimiourgia 5 komvon
        komvoi.append(Node(str(onoma)))
    g = Digraph()
    for n in komvoi:
        g.add_node(n)
    g.add_edge(Edge(komvoi["A"],komvoi["B"]))
    g.add_edge(Edge(komvoi["A"],komvoi["D"]))
    g.add_edge(Edge(komvoi["A"],komvoi["G"]))
    g.add_edge(Edge(komvoi["B"],komvoi["D"]))
    g.add_edge(Edge(komvoi["D"],komvoi["G"]))
    g.add_edge(Edge(komvoi["B"],komvoi["E"]))
    g.add_edge(Edge(komvoi["D"],komvoi["E"]))
    g.add_edge(Edge(komvoi["G"],komvoi["E"]))
    g.add_edge(Edge(komvoi["B"],komvoi["G"]))
    g.add_edge(Edge(komvoi["E"],komvoi["A"]))
    sd = sintomotero_monopati(g, komvoi["A"], komvoi["E"], ektiposi = True)
    print("Sintomoteri diadromi p vreike i DFS: ",print_path(sd))