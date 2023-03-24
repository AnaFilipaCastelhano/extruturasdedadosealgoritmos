import math


def distancia_euclideana(x1, y1, x2, y2):
    return math.sqrt(((x2-x1)**2)+(y2-y1)**2)

#print(distancia_euclideana(2,5,6,9))


def coordenadas_polares(x, y):
    r = math.sqrt((x**2)+(y**2))
    θ = math.atan(y/x)
    theta = 180*(θ/math.pi)
    return (r,theta)

#print(coordenadas_polares(2,4))


def lista(i, s, lst):
    count = 0
    for n in lst:
        if i <= n <= s:
            count +=1
    return count

#print(lista(2,5,[1,2,3,4,5,6,7,8,9,10,11]))


def divisao(lst):
    for tuplo in lst:
        if tuplo[1] != 0:
            print(tuplo[0]/tuplo[1])
        else:
            print(None)

# divisao([(82, 40), (23, 4), (12, 3), (15, 3), (1, 2), (20, 0)])


def last(n):
    return n[-1]

def lst_triplos(a,b):
    list = []
    count = 0
    for i in a:
        list.append((i, b[count]))
        count += 1
    return sorted(list, key=last)

#https://www.geeksforgeeks.org/python-program-to-sort-a-list-of-tuples-in-increasing-order-by-the-last-element-in-each-tuple/
#print(lst_triplos([1, 5, 2, 3], [20, 56, 10, 22]))


# lst = [1,1,1,1,1,2]
# xpto = set(lst)
# print(xpto)


def tuple_intersect(a, b):
    a = set(a)
    b = set(b)
    return a.intersection(b)

#print( tuple_intersect((-5, -1, 4), (-5, -2, 4, 5)))


def remove_duplicates(a, b):
    list = a+b
    return set(list)

#print(remove_duplicates([4,5],[3,4]))
#print(remove_duplicates((-5, -1, 4), (-5, -2, 4, 5)))
