lista = [
    47,
    80,
    50,
    69,
    41,
    50,
    5,
    14,
    14,
    88,
]



lista_secundaria = []

total = 0

for numero in lista:
	if numero % 2 == 0:
 		lista_secundaria = lista_secundaria + [numero * 2]
	else:
        	lista_secundaria = lista_secundaria + [numero * 3]

print (lista)
print (lista_secundaria)


                
         
