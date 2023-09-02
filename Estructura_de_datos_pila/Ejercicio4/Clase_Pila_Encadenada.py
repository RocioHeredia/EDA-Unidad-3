from Clase_Nodo_pila import nodo
class pila_enlazada:
    __tope = None

    def __init__(self):
        self.__tope = None

    def vacia(self):
        return self.__tope is None

    def Insertar(self, dato):
        nuevo_nodo = nodo(dato)
        nuevo_nodo.setsig(self.__tope)
        self.__tope = nuevo_nodo
    def Suprimir(self):
        if self.vacia():
            print('La pila esta vacia')
            return None
        valor = self.__tope.getdato()
        self.__tope = self.__tope.getsig()
        return valor

    def mostrar(self):
        if self.vacia():
            print("La pila está vacía.")
        else:
            actual = self.__tope
            while actual:
                print(actual.getdato())
                actual = actual.getSiguiente()
