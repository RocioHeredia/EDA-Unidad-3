
from Clase_Pila_Encadenada import pila_enlazada


def decimal_a_binario(num, pila):

    while num > 0:
        resto = num % 2
        pila.insertar(resto)
        num //= 2

    if pila.vacia():
        return '0'
    binario = ''
    while not pila.vacia():
        binario += str(pila.suprimir())
    return binario

if __name__ == '__main__':
    pila = pila_enlazada()
    numero = int(input('Ingrese numero: '))
    binario = decimal_a_binario(numero, pila)
    print(f'El numero {numero} en decimal es: {binario}')






'''class nodo:
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
            print('La pila esta vacia')
            return None
        valor = self.__tope.getdato()
        self.__tope = self.__tope.getsig()
        return valor

    def mostrar(self):
        if self.vacia():
            print('Pila vacia')
        else:
            aux = self.__tope
            while aux:
                print(aux.getdato())
                aux = aux.getsig()


def decimal_a_binario(num):
    pila2 = pila_enlazada()
    while num > 0:
        resto = num % 2
        pila2.insertar(resto)
        num //= 2

    if pila2.vacia():
        return '0'
    binario = ''
    while not pila2.vacia():
        binario += str(pila2.suprimir())
    return binario


numero = int(input('Ingrese numero: '))
binario = decimal_a_binario(numero)
print(f'El numero {numero} en decimal es: {binario}')'''