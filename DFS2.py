def dfs(grafos,arxi,episkepsi = None):
    if episkepsi is None:
        episkepsi = set()
    episkepsi.add(arxi)

    print(arxi)

    for epomeno in grafos[arxi] - episkepsi:
        dfs(grafos, epomeno, episkepsi)
    return episkepsi

#1o Sxima
grafos = {
    "A":set(["B","D","G"]),
    "B":set(["G","D","E"]),
    "G":set(["D","E"]),
    "D":set(["G","E"]),
    "E":set(["A"])}

"""
#2o Sxima
grafos = {
    "A":set(["B","D","G","H","Θ"]),
    "B":set(["G","D","E","Z","H","K"]),
    "G":set(["D","E","Θ","I"]),
    "D":set(["G","E"]),
    "E":set(["A","Z","I","K"]),
    "Z":set(["B","E"]),
    "H":set(["A","B"]),
    "Θ":set(["A","G"]),
    "I":set(["G","E"]),
    "K":set(["B","E"])}
"""

"""
#Ipomnima
grafos = {"0":set(["1","2"]),
        "1":set(["0","3","4"]),
        "2":set(["0"]),
        "3":set(["1"]),
        "4":set(["2","3"])}
"""
dfs(grafos,"A") #Sti thesi t A mporoume na valoume opoiodipote key