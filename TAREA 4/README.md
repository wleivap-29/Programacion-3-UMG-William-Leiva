

Arbol Binario

Este proyecto consiste en la implementación de un ARBOL AVL en Python, extendiendo la funcionalidad de un Árbol Binario de Búsqueda (ABB) mediante el uso de **herencia**.

El programa permite al usuario interactuar a través de una Interfaz de Línea de Comandos (CLI) para realizar diferentes operaciones sobre el árbol, manteniendo siempre su balance automáticamente.

---

FUNCIONES

*  Insertar elementos en el árbol (con balanceo automático)
*  Buscar elementos
*  Eliminar elementos (con reequilibrio)
*  Cargar datos desde archivos CSV
*  Generar representación del árbol con Graphviz

---

Tener instalado en la PC

* Python 3.x
* Graphviz instalado

Como se ejecuta el programa

1. Clonar el repositorio:




2. Acceder a la carpeta:


cd tu-repositorio
```

3. Ejecutar el programa:

python main.py



Ejemplos para probar

```
Ingrese número: 10,45,85,78,14
Ingrese número: 20,30,40,50
Ingrese número: 30,15,7,3,1
```

---

Archivos CSV de ejemplo

### datos1.csv

10,20,30,40,50

### datos2.csv

15,5,25,3,8,20

### datos3.csv

7,2,9,1,5,8,10


---

## Comjo se ve con Graphviz

El programa genera un archivo:

```
arbol.dot


Para convertirlo a imagen:

Abrir otra terminar y colocar este Mensaje: dot -Tpng arbol.dot -o arbol.png


Luego abrir:

arbol.png


---

 Estructura del proyecto

```
proyecto-avl
│── main.py
│── arbol.dot
│── datos1.csv
│── datos2.csv
│── datos3.csv
│── README.md
```
Integrantes:
William Emmanuel Leiva Pérez 9490-23-3393   100%

