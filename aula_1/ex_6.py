#dicionario

#nome = input('Digite o nome : ')
#idade = input('Digite sua idade : ')
#email = input('Digite seu email : ')

user = {
    'nome' : input('Digite o nome : '),
    'idade' : input('Digite sua idade : '),
    'email' : input('Digite seu email : ')
}

print(user)
print(user['nome'])

if user['idade'] >= '18':
    print("Bem vindo!")
else:
    print("*******Bloquado*****")