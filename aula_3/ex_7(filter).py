lista = [ 1, 2, 3, 4 ]

def somente_os_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

print(lista)
#lista2 = []
lista2 = somente_os_pares(lista)
print(lista2) 