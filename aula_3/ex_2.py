def calcular_media(lista_de_notas):
    resultado = 0
    contador = 0
    for nota in lista_de_notas:
        resultado = resultado + nota
        contador = contador + 1
    return resultado / contador

precos_da_laranja = [ 8 , 4, 8, 3, 7, 2]
media = calcular_media(precos_da_laranja)
print(media)