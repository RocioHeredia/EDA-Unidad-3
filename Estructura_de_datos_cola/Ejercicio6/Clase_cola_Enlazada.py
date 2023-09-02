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


class cola:
    __cantidad=int
    __primero = None
    __ultimo = None

    def __init__(self):
        self.__ultimo = None
        self.__primero = None
        self.__cantidad = 0

    def vacia(self):
        return self.__cantidad == 0

    def insertar(self, elemento):
        nuevo = nodo(elemento)

        if self.__ultimo is None:
            self.__primero = nuevo
        else:
            self.__ultimo.setsig(nuevo)
        self.__ultimo = nuevo
        self.__cantidad += 1
        return self.__ultimo.getsig()

    def suprimir(self):
        if self.vacia():
            print('Cola vacia')

        else:
            aux = self.__primero
        elemento = self.__primero.getdato()
        self.__primero = self.__primero.getsig()
        self.__cantidad -= 1
        if self.vacia():
            self.__ultimo = None
        return elemento

    def getprimero(self):
        return self.__primero

    def recorrer(self, aux):
        if aux is not None:
            print(aux.getdato())
            self.recorrer(aux.getsig())


if __name__ == '__main__':
    cola = cola()
    cola.insertar(2)
    cola.insertar(4)
    cola.insertar(6)
    cola.insertar(7)
    cola.insertar(9)
    print('Antes de suprimir')
    cola.recorrer(cola.getprimero())
    cola.suprimir()
    cola.suprimir()
    cola.suprimir()
    print('Despues de suprimir')
    cola.recorrer(cola.getprimero())
    cola.insertar(99)
    cola.insertar(78)
    cola.recorrer(cola.getprimero())