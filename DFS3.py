#1o Sxima
grafos = {
    "A":["B","D","G"],
    "B":["G","D","E"],
    "G":["D","E"],
    "D":["G","E"],
    "E":["A"]}

"""
#2o Sxima
grafos = {
    "A":["B","D","G","H","Θ"],
    "B":["G","D","E","Z","H","K"],
    "G":["D","E","Θ","I"],
    "D":["G","E"],
    "E":["A","Z","I","K"],
    "Z":["B","E"],
    "H":["A","B"],
    "Θ":["A","G"],
    "I":["G","E"],
    "K":["B","E"]}
"""

episkepsi = set()
def dfs(episkepsi,grafos,komvos):
    if komvos not in episkepsi:
        print(komvos)
        episkepsi.add(komvos)
        for geitona in grafos[komvos]:
            dfs(episkepsi,grafos,geitona)

print("Anazitisi kata vathos:")
dfs(episkepsi,grafos,"A") #Sti thesi t A mporoume na valoume opoiodipote key