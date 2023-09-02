from Clase_Pila_Encadenada import pila_enlazada


def calcular_factorial(pila, num):
    if num < 0:
        return None

    resultado = 1
    pila.insertar(num)
    while not pila.vacia():
        actual = pila.suprimir()
        resultado *= actual
        if actual > 1:
            pila.insertar(actual-1)
    return resultado


if __name__ == '__main__':
    pila = pila_enlazada()
    num = int(input('Ingrese numero para calcular su factorial: '))
    factorial = calcular_factorial(pila, num)
    print(f'El factorial de {num} es {factorial}')
    