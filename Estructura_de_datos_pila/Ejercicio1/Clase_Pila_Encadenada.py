from Clase_Nodo_pila import nodo
class pila_enlazada:
    __tope = None

    def __init__(self):
        self.__tope = None

    def vacia(self):
        return self.__tope is None

    def insertar(self, dato):
        nuevo_nodo = nodo(dato)
        nuevo_nodo.setsig(self.__tope)
        self.__tope = nuevo_nodo
    def suprimir(self):
        if self.vacia():
            print ('La pila esta vacia')
            return None
        valor = self.__tope.getdato()
        self.__tope = self.__tope.getsig()
        return valor

    def tope(self):
        if self.vacia():
            return None
        return self.__tope.getdato()


    def mostrar(self):
        if self.vacia():
            print('Pila vacia')
        else:
            aux = self.__tope
            while aux:
                print(aux.getdato())
                aux = aux.getsig()
