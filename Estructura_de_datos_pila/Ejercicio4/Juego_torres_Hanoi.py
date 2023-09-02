from Clase_Pila_Encadenada import pila_enlazada

def hanoi(n, origen, auxiliar, destino):
    movimientos = 0  # Inicializamos el contador de movimientos
    if n == 1:
        disco = origen.Suprimir()
        destino.Insertar(disco)
        movimientos += 1
        print(f"Mueve disco {disco} de torre {origen} a torre {destino}")
    else:
        # Movemos n-1 discos de origen a auxiliar utilizando destino como auxiliar
        movimientos += hanoi(n - 1, origen, destino, auxiliar)
        # Movemos 1 disco de origen a destino
        movimientos += 1
        disco = origen.Suprimir()
        destino.Insertar(disco)
        print(f"Mueve disco {disco} de torre {origen} a torre {destino}")
        # Movemos n-1 discos de auxiliar a destino utilizando origen como auxiliar
        movimientos += hanoi(n - 1, auxiliar, origen, destino)
    return movimientos

if __name__ == "__main__":
    n = int(input("Ingrese el número de discos: "))

    torre1 = pila_enlazada()
    torre2 = pila_enlazada()
    torre3 = pila_enlazada()
    for disco in range(n, 0, -1):
        torre1.Insertar(disco)

    print("Estado inicial de las torres:")
    print("Torre 1:", torre1)
    print("Torre 2:", torre2)
    print("Torre 3:", torre3)

    movimientos = hanoi(n, torre1, torre2, torre3)

    print("\nJuego completado en", movimientos, "movimientos.")
    print("Número mínimo de movimientos:", (2 ** n) - 1)