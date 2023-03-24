# exemplo de ilustração da herança múltipla
import numpy as np


class A:

    def A(self):
        print("I'm A")


class B:

    def A(self):
        print("I'm A in B")

    def B(self):
        print("I'm B")


class C(B,A):

    def C(self):
        print("I'm C")


if __name__ == '__main__':
    x = C() # tou a definir a variavel x cm uma instancia da class C q tá a ser declarada cm sendo filha de B e de A, quando mudo a orden BA ou AB o resultado será diferente, tanto que se o B foi o primeiro, tendo ele tb uma def A a class A nem seuqer vai ser chamada

    x.A()

    x.B()


# Exercicios
# Exercicio 1 implementar Queue usando uma lista

class Fila:

    def __init__(self, fila=[]):
        self.fila = fila
        #self.inicio = 0 # este vai tar sempre no indice zero, no entanto quando criamos umafila com uma lista não são necessários apontadores
        #self.fim = len(self.fila)-1
        #self.current = 0

    def show(self):
        for elemento in self.fila:
            print(elemento)

    def add(self, a):
        return self.fila.append(a)

    def first(self):
        print(self.fila[0])

    def remove(self):
        return self.fila.pop()

    def is_empty(self):
        if len(self.fila) == 0:
            print("A fila está vazia")
        else:
            print("Existem elementos na lista")

    def clear(self):
        return self.fila.clear()

    def qty(self):
        print(len(self.fila))

a = Fila([1,2,3,4,5,6,7,8,9])
a.add(10)
a.show()
a.first()
a.remove()
a.show()
a.is_empty()
a.qty()
a.clear()
a.is_empty()


class Queue:

    def __init__(self, dim):
        self.dim = dim
        self.__fila = np.zeros()
        self.inicio = 0
        self.fim = dim-1
        self.current = 0