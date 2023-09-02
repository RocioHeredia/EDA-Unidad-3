from Clase_cola_Enlazada import cola
from random import randint
if __name__ == '__main__':
    cola = cola()
    reloj = 0
    tiempo_maximo = 0
    while reloj < 30:
        if reloj % 2 == 0:
            numero_random = randint(1, 2)
            if numero_random == 2:
                cola.insertar(reloj)

        if reloj % 5 == 0:
            if not cola.vacia():
                aux = cola.suprimir()
                if reloj-aux > tiempo_maximo:
                    tiempo_maximo = reloj-aux

        reloj += 1
    print(f'TIEMPO MAXIMO DE ESPERA {tiempo_maximo} MINUTOS')