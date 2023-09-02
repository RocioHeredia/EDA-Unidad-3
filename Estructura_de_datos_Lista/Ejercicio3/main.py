from ListaEnalazadaPorContenido import ListaEnlazadaPorContenido
import csv
from Superficie import superficie
if __name__ == '__main__':
    archivo = open('superficie.csv', encoding='utf-8-sig')
    reader = csv.reader(archivo, delimiter=';')
    primero = True
    for fila in reader:
        if primero:
            mi_lista_incendio = ListaEnlazadaPorContenido()
            primero = False
        else:
            if fila[6]:
                mi_lista_incendio.Insertar(superficie(fila[3], float(fila[6])))
            else:
                mi_lista_incendio.Insertar(superficie(fila[3], 0))
    mi_lista_incendio.Ordenar()
    print('LISTA DESPUES DE ORDENAR:')
    mi_lista_incendio.Recorrer()