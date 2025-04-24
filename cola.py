class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.longitud = 0

    def is_empty(self):
        return self.frente is None

    def enqueue(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.is_empty():
            self.frente = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.longitud += 1
        print(f" Elemento encolado: {valor}")

    def dequeue(self):
        if self.is_empty():
            print(" La cola está vacía.")
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.longitud -= 1
        print(f" Elemento eliminado: {valor}")
        return valor

    def peek(self):
        if self.is_empty():
            print(" La cola está vacía.")
            return None
        return self.frente.valor

    def size(self):
        return self.longitud

def main():
    cola = Cola()

    while True:
        print("\n Menú de Cola con Nodos")
        print("1. Encolar (agregar)")
        print("2. Desencolar (eliminar)")
        print("3. Ver frente de la cola")
        print("4. Ver tamaño de la cola")
        print("5. ¿Está vacía la cola?")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            valor = input("Ingrese el valor a encolar: ")
            cola.enqueue(valor)

        elif opcion == "2":
            cola.dequeue()

        elif opcion == "3":
            frente = cola.peek()
            if frente is not None:
                print(f" Frente de la cola: {frente}")

        elif opcion == "4":
            print(f" Tamaño de la cola: {cola.size()}")

        elif opcion == "5":
            print(" La cola está vacía." if cola.is_empty() else " La cola no está vacía.")

        elif opcion == "6":
            print(" Saliendo del programa.")
            break

        else:
            print(" Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()