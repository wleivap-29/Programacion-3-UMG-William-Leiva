from graphviz import Digraph

def generar_graphviz(arbol):
    dot = Digraph()

    def recorrer(nodo):
        if nodo:
            dot.node(str(nodo.valor))

            if nodo.izq:
                dot.edge(str(nodo.valor), str(nodo.izq.valor))
                recorrer(nodo.izq)

            if nodo.der:
                dot.edge(str(nodo.valor), str(nodo.der.valor))
                recorrer(nodo.der)

    recorrer(arbol.raiz)
    dot.render("arbol", format="png", view=True)
