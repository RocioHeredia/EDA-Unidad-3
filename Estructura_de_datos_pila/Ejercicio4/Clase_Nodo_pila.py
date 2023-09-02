class nodo:
    __dato = int
    __sig = None

    def __init__(self, dato):
        self.__dato = dato
        self.__sig = None

    def setsig(self, sig):
        self.__sig = sig

    def getsig(self):
        return self.__sig

    def getdato(self):
        return self.__dato
