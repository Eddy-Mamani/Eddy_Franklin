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

    def dequeue(self):
        if self.is_empty():
            print("La cola está vacía.")
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.longitud -= 1
        print("elemento eliminado:", valor)
        return valor