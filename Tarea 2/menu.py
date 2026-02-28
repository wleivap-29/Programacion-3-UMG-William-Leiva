#Tarea No 2 
#William Leiva

# 1. Convertir a Binario
def convertir_a_binario(n):
    if n < 2:
        return str(n)
    return convertir_a_binario(n // 2) + str(n % 2)


# 2. Contar Dígitos
def contar_digitos(n):
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)


# 3. Raíz Cuadrada Entera
def calcular_raiz_cuadrada(n, i=0):
    if i * i > n:
        return i - 1
    return calcular_raiz_cuadrada(n, i + 1)

def raiz_cuadrada_entera(n):
    return calcular_raiz_cuadrada(n)


# 4. Convertir de Romano a Decimal
def convertir_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}

    if len(romano) == 1:
        return valores[romano]

    if valores[romano[0]] < valores[romano[1]]:
        return convertir_a_decimal(romano[1:]) - valores[romano[0]]
    else:
        return valores[romano[0]] + convertir_a_decimal(romano[1:])


# 5. Suma de Números Enteros
def suma_numeros_enteros(n):
    if n == 0:
        return 0
    return n + suma_numeros_enteros(n - 1)



# MENÚ PRINCIPAL

def menu():
    while True:
        print("\n--- MENU DE OPCIONES ---")
        print("1. Convertir a Binario")
        print("2. Contar Digitos")
        print("3. Riz Cuadrada Entera")
        print("4. Convertir a Decimal desde Romano")
        print("5. Suma de Números Enteros")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            n = int(input("Ingrese un nuero entero: "))
            print("Binario:", convertir_a_binario(n))

        elif opcion == "2":
            n = int(input("Ingrese un numero entero: "))
            print("Cantidad de dígitos:", contar_digitos(abs(n)))

        elif opcion == "3":
            n = int(input("Ingresse un numero entero positivo: "))
            print("Raíz cuadrada entera:", raiz_cuadrada_entera(n))

        elif opcion == "4":
            romano = input("Ingrese un numero romano: ").upper()
            print("Decimal:", convertir_a_decimal(romano))

        elif opcion == "5":
            n = int(input("Ingrese un numero entero positvo: "))
            print("Suma:", suma_numeros_enteros(n))

        elif opcion == "6":
            print("Fin")
            break

        else:
            print("Opción inválida, intente de nuevo.")


menu()