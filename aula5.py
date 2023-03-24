# exercicio 2

# por recursividade
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# por prog dinâmica

def fib1(n):
    lista = [0, 1]
    while len(lista) != n:
        valor = lista[-2] + lista[-1]
        lista.append(valor)
    return lista[n - 1]


print(fib1(5))


# exercicio 3

# por prog dinâmica
def exponencial(x, n):
    resultado = x
    contador = 1
    while contador != n:
        resultado = resultado * x
        contador += 1
    return resultado


print(exponencial(2, 3))


# por prog recursiva

def exponencial2(x, n):
    if n == 0:
        return 1
    else:
        return exponencial2(x, n - 1)


# exercicio 4

# por prog dinâmica

def inverte(a):
    lista = a
    nova_lista = []
    while len(a) != 0:
        nova_lista.append(lista[-1])
        lista.pop()
    return nova_lista

print(inverte([1,2,3,4,5]))

#programação recursiva

def inverter_lista(lista):
    if len(lista) == 0:
        return []
    else:
        return [lista[-1]] + inverter_lista(lista[:-1])

