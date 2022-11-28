class Graph:
    def __init__(self,arithmos_komvon,kateuthinomenos = True):
        self.arithmos_komvon2 = arithmos_komvon
        self.komvoi = range(self.arithmos_komvon2)

        self.kateuthinomenos2 = kateuthinomenos

        self.lista_geitniasis = {node: set() for node in self.komvoi}

    def add_akmi(self,komvos1,komvos2,varos = 1):
        self.lista_geitniasis[komvos1].add((komvos2,varos))

    def ektiposi(self):
        for key in self.lista_geitniasis.keys():
            print("Komvos", key, ": ", self.lista_geitniasis[key])
#--------------------------------------------------------------------
    def dfs(self,arxi,telos,monopati = [],episkepsi = set()):
        monopati.append(arxi)
        episkepsi.add(arxi)
        if arxi == telos:
            return monopati
        for (geitona,varos) in self.lista_geitniasis[arxi]:
            if geitona not in episkepsi:
                apotelesma = self.dfs(geitona,telos,monopati,episkepsi)
                if apotelesma is not None:
                    return apotelesma
        monopati.pop()
        return None

grafos = Graph(6,kateuthinomenos = False)

#1o Sxima
grafos.add_akmi(1,2)
grafos.add_akmi(1,3)
grafos.add_akmi(1,4)
grafos.add_akmi(2,4)
grafos.add_akmi(2,3)
grafos.add_akmi(2,5)
grafos.add_akmi(3,4)
grafos.add_akmi(3,5)
grafos.add_akmi(4,5)
grafos.add_akmi(5,1)

"""
#2o Sxima
grafos.add_akmi(1,2)
grafos.add_akmi(1,3)
grafos.add_akmi(1,4)
grafos.add_akmi(1,7)
grafos.add_akmi(1,8)
grafos.add_akmi(2,4)
grafos.add_akmi(2,3)
grafos.add_akmi(2,5)
grafos.add_akmi(2,6)
grafos.add_akmi(2,7)
grafos.add_akmi(2,10)
grafos.add_akmi(3,4)
grafos.add_akmi(3,5)
grafos.add_akmi(3,8)
grafos.add_akmi(3,9)
grafos.add_akmi(4,5)
grafos.add_akmi(5,1)
grafos.add_akmi(5,6)
grafos.add_akmi(5,9)
grafos.add_akmi(5,10)
grafos.add_akmi(6,2)
grafos.add_akmi(6,5)
grafos.add_akmi(7,1)
grafos.add_akmi(7,2)
grafos.add_akmi(8,1)
grafos.add_akmi(8,3)
grafos.add_akmi(9,3)
grafos.add_akmi(9,5)
grafos.add_akmi(10,2)
grafos.add_akmi(10,5)
"""

"""
#Ipomnima
grafos.add_akmi(0,1)
grafos.add_akmi(0,2)
grafos.add_akmi(1,3)
grafos.add_akmi(2,3)
grafos.add_akmi(3,4)
"""
#grafos.ektiposi()

lista_diadromon = []
lista_diadromon = grafos.dfs(0,3)
print(lista_diadromon)