idade = input("Digite sua idade: ")
 
lista = [ '0','1','2','3','4','5','6','7','8','9']

for valor in  idade:
    if valor in lista:
    	print("Voce digitou apenas numeros")
    else:
    	print("Voce digitou uma letra")


