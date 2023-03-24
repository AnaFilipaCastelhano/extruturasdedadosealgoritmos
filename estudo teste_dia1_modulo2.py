import numpy as np
import matplotlib.pyplot as plt
import math
import time
import random
import statistics as stat

# modulo 2

# 2. Considere as seguintes funções: 𝑦1 = 567 + 100𝑥 + 𝑥**2 e 𝑦2 = 0.5 − 1024 𝑥 + 𝑥**2 𝑒 𝑦3 =𝑥**2.
# a) Implemente estas funções em código Python e, de forma a que seja possível gerar os
# respetivos valores y de todas as funções. (Dica: Obtenha listas de valores de y1, y2 e y3 para
# x a variar no seguinte intervalo x ∈ [0, 10000]).

# x = np.linspace(0, 10000, 10000)
#
# y1 = 567 + (100 * x) + (x ** 2)
#
# y2 = 0.5 - (1024 * x) + (x ** 2)
#
# y3 = x ** 2
#
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# plt.show()

# 3. Implemente os seguintes algoritmos:
# a) Algoritmo de Pesquisa linear, que permite pesquisar/encontrar um dado valor numa
# coleção de valores.

inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30]


def pesquisa(x, lista):
    for elemento in lista:
        if elemento == x:
            return True


print(pesquisa(5,inteiros))


