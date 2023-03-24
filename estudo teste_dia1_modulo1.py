import math
import pandas as pd


# modulo1
# 1. Um tuplo (tuple) é uma sequência imutável de elementos ou uma sequência de elementos imutáveis? Ilustre a sua resposta com exemplos em código Python.
# Um tupulo é uma sequência imutável de elementos. se criarmos um tuplo = (1,2,3,4,5), não conseguimos fazer nenhuma operação que altere os objetos que lá estão dentro, conseguimos porém obter por exemplo o tamanho do tuplo, obter elementos dado um indice, percorrer os elementos do tuplo. Mas nunca alterar o que lá está dentro.

# 2. Criar funções para executar as seguintes operações.
# Documentação sobre o tipo de dados tuple do Python (sugestão): https://www.tutorialspoint.com/python/python_tuples.htm
# a) Calcular a distância Euclidiana entre dois pontos ponto1 = (x1, y1) e ponto 2= (x2, y2).
# Recorde que a distância Euclidiana entre dois pontos é dada pela fórmula:
# √((x2 − x1)^2 + (𝑦2 − 𝑦1)^2)
#
# b) Converter coordenadas cartesianas para coordenadas polares. A função recebe o tuplo (x,y) e devolve o tuplo (r,θ).

class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


def euclidian_distance(a1, a2):
    return float((((a2.x - a1.x) ** 2) + ((a2.y + a1.y) ** 2)) ** (1 / 2))


p1 = Point(1, 2)
p2 = Point(3, 4)


def cartesian_to_polar(a):
    r = math.sqrt((a.x ** 2) + (a.y ** 2))
    ro = math.atan(a.y / a.x)
    return (r, ro)


# 3. Criar funções para executar as seguintes operações.
# Documentação sobre o tipo de dados list do Python (sugestão):
# https://www.tutorialspoint.com/python/python_lists.htm
# a) Dada uma lista de números inteiros e dois números inteiros i e s, que definem um intervalo [i,
# s], contar quantos números da lista pertencem ao intervalo.
# i. sem usar comprehension
# ii. usando comprehension.


inteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30]


def conta_numeros(a, b):
    conta = 0
    for inteiro in inteiros:
        if a <= inteiro <= b:
            conta += 1
    return conta


def conta_numeros2(a, b):
    return sum([1 for inteir in inteiros if a <= inteir <= b])


# b) Devolver uma lista de resultados de divisões de pares (x, y), sendo os pares dados através
# de uma lista de tuplos. Deve evitar a divisão por zero e só deve dividir caso a divisão seja
# maior ou igual a 1.
# Exemplo:
# list_res_div((82, 40), (23, 4), (12, 3), (15, 3), (1, 2), (20, 0)) → [2.05, 5.75, 4.0, 5.0, 0.5, None]
# i. sem usar comprehension
# ii. usando comprehension.

list_res_div = ((82, 40), (23, 4), (12, 3), (15, 3), (1, 2), (20, 0))


def divide(pares):
    lista = []
    for par in pares:
        if par[1] == 0 or (par[0] / par[1]) < 1:
            lista = lista
        else:
            lista.append(par[0] / par[1])
    return lista


def divide2(pares):
    return [par[0] / par[1] if par[1] else None for par in pares]


# c) Dadas duas listas, devolver uma lista de pares, juntando cada elemento da 1.ª lista com o
# elemento da 2.ª na mesma posição, ordenada pelo segundo elemento. Exemplo:
# lst_triplos([1, 5, 2, 3], [20, 56, 10, 22]) → [(2, 10), (1, 20), (3, 22), (5, 56)]

lst1 = [1, 5, 2, 3]
lst2 = [20, 56, 10, 22]


def junta(lista1, lista2):
    nova_lista = []
    for i1, i2 in zip(lista1, lista2):
        nova_lista.append((i1, i2))
    return nova_lista


def ordena_segundo(lista):
    return sorted(lista, key=lambda x: x[1])


# 4. Criar funções para executar as seguintes operações.
# Documentação do tipo de dados set do Python (sugestão):
# https://www.w3schools.com/python/python_sets.asp
# a) Devolver os elementos comuns entre dois tuplos dados. Exemplo: tuple_intersect((-5, -1, 4), (-
# 5, -2, 4, 5)) → {-5, 4}
# i. sem usar comprehension
# ii. usando comprehension.

tp1 = (-5, -1, 4)
tp2 = (-5, -2, 4, 5)


def devolve_comuns(tup1, tup2):
    for i in tup1:
        for i2 in tup2:
            if i == i2:
                print(i)


def devolve_comuns2(tup1, tup2):
    return set([i for i in tup1 if i in tup2])


# b) Remover duplicados de uma dada lista. Exemplo: para l1 = [4, 5] e l2 = [3, 4], remove_duplicates(l1, l2) → [3, 5]

l1 = [4, 5]
l2 = [3, 4]


def remove_comuns(lst1, lst2):
    for i in lst1:
        for i2 in lst2:
            if i == i2:
                lst1.remove(i)
                lst2.remove(i)
    return lst1 + lst2


# 5. Criar funções para executar as seguintes operações.
# Documentação do tipo de dados dict do Python (sugestão):
# https://www.tutorialspoint.com/python/python_dictionary.htm
# a) Dada uma string s, por exemplo um texto relativo a uma notícia, contar o número de
# ocorrências de cada palavra num dicionário. A chave do dicionário deve ser a palavra em
# causa, e o valor, a sua respetiva frequência no texto


noticia = "Os casos desta infeção oportunista causada pelo superfungo Candida auris duplicaram em 2021 - " \
          "de 756 para 1.471, diz o relatório do CDC. Este fungo é particularmente perigoso para pessoas com o " \
          "sistema imunitário comprometido – ou que usam dispositivos médicos como ventiladores ou cateteres. O CDC " \
          "diz que se trata de uma ameaça urgente de resistência antimicrobiana. A infeção pode espalhar-se pelo " \
          "contacto com pacientes afetados e superfícies ou equipamentos contaminados, disse o CDC que adianta que " \
          "os sintomas mais comuns são febre e calafrios que não melhoram após o tratamento. Um em cada três pacientes " \
          "com infeções invasivas morre, mas pode ser difícil avaliar o papel exato que a Candida auris desempenha " \
          "em pacientes vulneráveis, disse a epidemiologista do CDC Meghan Lyman, principal autora do relatório " \
          "que é citado pela BBC. A Candida auris foi identificada pela primeira vez em 2009, na secreção do ouvido " \
          "de um paciente Japonês. Nos Estados Unidos, a primeira deteção ocorreu em 2016. O aumento mais " \
          "rápido de casos foi de 2020 a 2021, de acordo com dados do CDC publicados no Annals of Internal Medicine."


def str_to_list(a):
    return a.split(" ")


def count_words(lista):
    count = pd.Series(lista).value_counts()
    return count


def count_words2(lista):
    count = {}
    for elemento in lista:
        if elemento not in count:
            count[elemento] = 1
        else:
            count[elemento] += 1
    return count


# b) Dado o seguinte dicionário:
# i. Devolver a idade do Bob.
# ii. Devolver o conjunto das diferentes ocupações das pessoas.
# iii. Remover do dicionário todas as pessoas com idades inferiores a 30 anos.
# iv. Devolver a média de todas as idades, após a remoção das pessoas com idades inferiores
# a 30.


people_dict = {"Alice": {"age": 35, "sex": "female", "occupation": "teacher"},
               "Bob": {"age": 42, "sex": "male", "occupation": "engineer"},
               "Charlie": {"age": 28, "sex": "male", "occupation": "scientist"},
               "Diana": {"age": 31, "sex": "female", "occupation": "doctor"},
               "Eva": {"age": 26, "sex": "female", "occupation": "artist"},
               "Frank": {"age": 38, "sex": "male", "occupation": "writer"},
               "Grace": {"age": 40, "sex": "female", "occupation": "programmer"},
               "Henry": {"age": 33, "sex": "male", "occupation": "musician"},
               "Isabelle": {"age": 29, "sex": "female", "occupation": "designer"},
               "John": {"age": 45, "sex": "male", "occupation": "businessman"}}

print(len(people_dict))


# print(people_dict["Bob"]["age"])

def ocupacao(dicionario):
    lista = set()
    for name in dicionario:
        lista.add(dicionario[name]["occupation"])
    return lista


def remover_menos_30(dicionario):
    novo_dicionario = {}
    for name in dicionario:
        if dicionario[name]["age"] >= 30:
            novo_dicionario[name] = dicionario[name]
    dicionario = novo_dicionario
    return dicionario


def retorna_media_idades(dicionario):
    count = len(dicionario)
    soma_idades = 0
    for name in dicionario:
        soma_idades = soma_idades + dicionario[name]["age"]
    return soma_idades/count


print(retorna_media_idades(remover_menos_30(people_dict)))


