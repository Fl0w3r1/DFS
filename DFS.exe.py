#Algorithmos DFS
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