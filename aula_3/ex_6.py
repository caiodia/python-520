lista = [
    2,
    3
]

def multiplica(x):
    if x % 2 == 0:
        return x * 2
    else:
        return x * 3

nova_lista1 = []

# Maneira 1 de implementacao usando funcao
print(lista)
for numero in lista:
    nova_lista1.append(multiplica(numero))
print(nova_lista1)

# Maneira 2 de implementacao usando map e funcao
nova_lista2 = list(map(multiplica,lista))
print(nova_lista2)

# Maneira 3 de implementacao usando map com lambda e
# operador ternario
nova_lista3 = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3,lista))
print(nova_lista3)