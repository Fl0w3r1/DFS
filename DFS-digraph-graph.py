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