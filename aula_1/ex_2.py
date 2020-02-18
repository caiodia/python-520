
# Tipos primitivos
# text = 'Bruno Caio'
# inteiro = 27
# decimais = 1.80
# booleano = True #False
# complexo = complex(2, 3)

# exercicio
# solicitar ao usuario as informacoese
# - nome
# - idade
# - email
# e armazenar os valores em variaveis
# [escolham bem os nomes]

print("Ola forneca seus dados para nosso cadastro")

nome  = input("digite seu nome : ")
idade = input("digite a idade : ")
email = input("digite seu email : ")

print(nome)
print(idade)
print(email)

if idade >= '18':
    print("Bem vindo!")
else:
    print("*******Bloquado*****")