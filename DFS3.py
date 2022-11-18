grafos = {
    "A":["B","D","G"],
    "B":["G","D","E"],
    "G":["D","E"],
    "D":["G","E"],
    "E":["B","A"]
}

episkepsi = set()
def dfs(episkepsi,grafos,komvos):
    if komvos not in episkepsi:
        print(komvos)
        episkepsi.add(komvos)
        for geitona in grafos[komvos]:
            dfs(episkepsi,grafos,geitona)

print("Anazitisi kata vathos:")
dfs(episkepsi,grafos,"A") #Sti thesi t A mporoume na valoume opoiodipote key