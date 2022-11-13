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