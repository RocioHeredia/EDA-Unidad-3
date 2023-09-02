class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def getdato(self):
        return self.__dato

    def setsiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getsiguiente(self):
        return self.__siguiente

    def setdato(self, dato):
        self.__dato = dato

class ListaEnlazadaPorContenido:
    def __init__(self):
        self.__primero = None

    def Insertar(self, elemento):
        nuevo_nodo = Nodo(elemento)
        nuevo_nodo.setsiguiente(self.__primero)
        self.__primero = nuevo_nodo

    def Suprimir(self, elemento):
        actual = self.__primero
        anterior = None

        while actual is not None and actual.getdato() != elemento:
            anterior = actual
            actual = actual.getsiguiente()

        if actual is not None:
            if anterior is None:
                self.__primero = actual.getsiguiente()
            else:
                anterior.setsiguiente(actual.getsiguiente())
        else:
            print("Elemento no encontrado")

    def Recuperar(self, elemento):
        actual = self.__primero
        while actual is not None and actual.getdato() != elemento:
            actual = actual.getsiguiente()
        if actual is not None:
            return actual.getdato()
        else:
            print("Elemento no encontrado")
            return None

    def Buscar(self, elemento):
        actual = self.__primero
        contador = 0
        while actual is not None:
            if actual.getdato().getcargo() == elemento:
                return contador
            actual = actual.getsiguiente()
            contador += 1
        return -1


    def Primer_elemento(self):
        if self.__primero is not None:
            return self.__primero


    def Ultimo_elemento(self):
        if self.__primero is None:
            return None
        actual = self.__primero
        while actual.getsiguiente() is not None:
            actual = actual.getsiguiente()
        return actual.getdato()

    def Siguiente(self, elemento):
        actual = self.__primero
        while actual is not None and actual.getdato() != elemento:
            actual = actual.getsiguiente()
        if actual is not None and actual.getsiguiente() is not None:
            siguiente_nodo = actual.getsiguiente()
            return siguiente_nodo.getdato()


    def Anterior(self, elemento):
        actual = self.__primero
        anterior = None

        while actual is not None and actual.getdato() != elemento:
            anterior = actual
            actual = actual.getsiguiente()

        if actual is not None and anterior is not None:
            return anterior.getdato()
        else:
            print("Elemento no encontrado")
            return None

    def Recorrer(self):
        actual = self.__primero
        while actual is not None:
            print(actual.getdato())
            actual = actual.getsiguiente()



'''
# Ejemplo de uso
mi_lista = ListaEnlazadaPorContenido()
mi_lista.Insertar(1)
mi_lista.Insertar(2)
mi_lista.Insertar(3)

print("Recorrido de la lista:")
mi_lista.Recorrer()

print("Recuperar elemento 2:", mi_lista.Recuperar(2))
print("Buscar elemento 3:", mi_lista.Buscar(3))
print("Siguiente a 2:", mi_lista.Siguiente(2))
print("Anterior a 3:", mi_lista.Anterior(3))
'''