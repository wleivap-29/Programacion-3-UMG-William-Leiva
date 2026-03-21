import csv
from abb import ABB
from graphviz_export import generar_graphviz

arbol = ABB()

def cargar_csv(ruta):
    try:
        with open(ruta, newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                for valor in fila:
                    arbol.insertar(int(valor))
        print("se cargo el archivo correctamente")
    except Exception as e:
        print("Error:", e)


def menu():
    while True:
        print("\n---Menu interactivo---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar desde CSV")
        print("5. Generar Graphviz")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            entrada = input("Ingrese número(s) separados por coma: ")
            valores = entrada.split(",")
            for v in valores:
                arbol.insertar(int(v.strip()))
            #valor = int(input("Ingrese numero: "))
            #arbol.insertar(valor)

        elif opcion == "2":
            valor = int(input("Buscar numero: "))
            print("Encontrado" if arbol.buscar(valor) else "No encontrado")

        elif opcion == "3":
            valor = int(input("Eliminar numero: "))
            arbol.eliminar(valor)

        elif opcion == "4":
            ruta = input("Ruta del archivo CSV: ")
            cargar_csv(ruta)

        elif opcion == "5":
            generar_graphviz(arbol)

        elif opcion == "6":
            break

        else:
            print("Opcion invalida")


if __name__ == "__main__":
    menu()
