def encontrar_o_maior_numero(lista_de_numeros):
    numero_auxiliar = lista_de_numeros[0]

    for numero in lista_de_numeros:
        maior_numero = maior(numero, numero_auxiliar)
        numero_auxiliar = maior_numero

    return maior_numero   
    
def maior(a, b):
    if a > b:
        return a
    else:
        return b

lista_de_numeros = [ -7 , -100, -3, -4, -20, -5]
maior_numero = encontrar_o_maior_numero(lista_de_numeros)
print(maior_numero)