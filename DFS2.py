def dfs(grafos,arxi,episkepsi = None):
    if episkepsi is None:
        episkepsi = set()
    episkepsi.add(arxi)

    print(arxi)

    for epomeno in grafos[arxi] - episkepsi:
        dfs(grafos, epomeno, episkepsi)
    return episkepsi

grafos = {
    "A":set(["B","D","G"]),
    "B":set(["G","D","E"]),
    "G":set(["D","E"]),
    "D":set(["G","E"]),
    "E":set(["B","A"])
}
"""
grafos = {"0":set(["1","2"]),
        "1":set(["0","3","4"]),
        "2":set(["0"]),
        "3":set(["1"]),
        "4":set(["2","3"])}
"""
dfs(grafos,"A") #Sti thesi t A mporoume na valoume opoiodipote key