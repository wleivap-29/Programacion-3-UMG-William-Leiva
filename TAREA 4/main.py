import csv
import os


# clase Nodo
# ----------------------
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


# CRUD de ABB 
# ----------------------
class ABB:
    def insertar(self, raiz, valor):
        if not raiz:
            return Nodo(valor)
        if valor < raiz.valor:
            raiz.izq = self.insertar(raiz.izq, valor)
        else:
            raiz.der = self.insertar(raiz.der, valor)
        return raiz

    def buscar(self, raiz, valor):
        if not raiz or raiz.valor == valor:
            return raiz
        if valor < raiz.valor:
            return self.buscar(raiz.izq, valor)
        return self.buscar(raiz.der, valor)

    def minimo(self, nodo):
        actual = nodo
        while actual.izq:
            actual = actual.izq
        return actual

    def eliminar(self, raiz, valor):
        if not raiz:
            return raiz
        if valor < raiz.valor:
            raiz.izq = self.eliminar(raiz.izq, valor)
        elif valor > raiz.valor:
            raiz.der = self.eliminar(raiz.der, valor)
        else:
            if not raiz.izq:
                return raiz.der
            elif not raiz.der:
                return raiz.izq
            temp = self.minimo(raiz.der)
            raiz.valor = temp.valor
            raiz.der = self.eliminar(raiz.der, temp.valor)
        return raiz


# Arbol AVL con funcionalidades de ABB
# ----------------------
class AVL(ABB):
    def altura(self, nodo):
        return nodo.altura if nodo else 0

    def balance(self, nodo):
        return self.altura(nodo.izq) - self.altura(nodo.der)

    def rotar_derecha(self, y):
        x = y.izq
        T2 = x.der

        x.der = y
        y.izq = T2

        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))

        return x

    def rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq

        y.izq = x
        x.der = T2

        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))

        return y

    def insertar(self, raiz, valor):
        raiz = super().insertar(raiz, valor)

        raiz.altura = 1 + max(self.altura(raiz.izq), self.altura(raiz.der))
        balance = self.balance(raiz)

        # Rotaciones
        if balance > 1 and valor < raiz.izq.valor:
            return self.rotar_derecha(raiz)
        if balance < -1 and valor > raiz.der.valor:
            return self.rotar_izquierda(raiz)
        if balance > 1 and valor > raiz.izq.valor:
            raiz.izq = self.rotar_izquierda(raiz.izq)
            return self.rotar_derecha(raiz)
        if balance < -1 and valor < raiz.der.valor:
            raiz.der = self.rotar_derecha(raiz.der)
            return self.rotar_izquierda(raiz)

        return raiz

    def eliminar(self, raiz, valor):
        raiz = super().eliminar(raiz, valor)

        if not raiz:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.izq), self.altura(raiz.der))
        balance = self.balance(raiz)

        if balance > 1 and self.balance(raiz.izq) >= 0:
            return self.rotar_derecha(raiz)
        if balance > 1 and self.balance(raiz.izq) < 0:
            raiz.izq = self.rotar_izquierda(raiz.izq)
            return self.rotar_derecha(raiz)
        if balance < -1 and self.balance(raiz.der) <= 0:
            return self.rotar_izquierda(raiz)
        if balance < -1 and self.balance(raiz.der) > 0:
            raiz.der = self.rotar_derecha(raiz.der)
            return self.rotar_izquierda(raiz)

        return raiz


# esta parte se crea el Graphviz
# ----------------------
def generar_dot(raiz, archivo="arbol.dot"):
    with open(archivo, "w") as f:
        f.write("digraph AVL {\n")

        def recorrer(nodo):
            if nodo:
                if nodo.izq:
                    f.write(f"    {nodo.valor} -> {nodo.izq.valor};\n")
                    recorrer(nodo.izq)
                if nodo.der:
                    f.write(f"    {nodo.valor} -> {nodo.der.valor};\n")
                    recorrer(nodo.der)

        recorrer(raiz)
        f.write("}\n")

    print(f"Archivo DOT creado: {archivo}")
    print("Abrir otra terminal y pegar este Mensaje: dot -Tpng arbol.dot -o arbol.png")

# aqui para agregar el csv
# ----------------------
def cargar_csv(ruta, arbol, raiz):
    try:
        with open(ruta, newline='') as f:
            reader = csv.reader(f)
            for fila in reader:
                for valor in fila:
                    raiz = arbol.insertar(raiz, int(valor))
        print("Datos cargados correctamente")
    except Exception as e:
        print("Error al cargar CSV:", e)
    return raiz

# ----------------------
# CLI
# ----------------------
def menu():
    arbol = AVL()
    raiz = None

    while True:
        print("\n MENU AVL ")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar CSV")
        print("5. Generar Graphviz")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            entrada = input("Ingrese los numeros separados por coma: ")

            try:
                numeros = [int(x.strip()) for x in entrada.split(",")]
                for valor in numeros:
                    raiz = arbol.insertar(raiz, valor)
            except:
                print("Entrada invalida")

        elif opcion == "2":
            valor = int(input("Buscar numero: "))
            resultado = arbol.buscar(raiz, valor)
            print("Encontrado" if resultado else "No encontrado")

        elif opcion == "3":
            valor = int(input("Eliminar numwro: "))
            raiz = arbol.eliminar(raiz, valor)

        elif opcion == "4":
            ruta = input("Ruta del CSV: ")
            raiz = cargar_csv(ruta, arbol, raiz)

        elif opcion == "5":
            generar_dot(raiz)

        elif opcion == "6":
            break

        else:
            print("esta opcion no vale")

if __name__ == "__main__":
    menu()
