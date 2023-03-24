# exercicio 1 a)
import numpy as np


class Stack:
    def __init__(self):
        self.__stack = []

    def add(self, a):
        self.__stack.append(a)

    def is_empty(self):
        return len(self.__stack) == 0

    def show_top_result(self):
        if self.is_empty():
            raise ValueError("Empty stack!")
        else:
            return self.__stack[-1]

    def remove(self):
        if self.is_empty():
            raise ValueError("Empty stack!")
        else:
            self.__stack.pop()

    def clear_stack(self):
        self.__stack.clear()

    def elements_number(self):
        return len(self.__stack)


# exercicio 2 a)
import numpy as np

class Pilha:

    def __init__(self,dim):
        self.dim = dim
        self.__pilha = np.zeros(dim) #np.array transforma uma lista com qq elementos desde q seja número num array
        self.inicio = 0
        self.fim = dim-1
        self.current = 0

    def is_empty(self):
        return self.current == self.inicio

    def is_full(self):
        return self.current == self.dim

    def add(self, a):
        if self.is_full() is False:
            self.__pilha[self.current] = a
            self.current += 1

    def remove(self):
        if self.is_empty() is False:
            self.current -= 1
            self.__pilha[self.current] = 0









