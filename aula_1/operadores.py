# Operacoes entre numeros

a = 2.5
b = 10

print(a + b) #soma
print(a - b) #subtracao
print(a * b) #multiplicacao
print(a / b) #divisao
print(a % b) #modulo
print(a ** b) #exponenciacao

#Operacoes entre booleanos

x = True
y = False

print(x and y)
print(x or y)
print(not x) # so funciona com 1 elemento

#maior_de_idade = user['age'] > 18

#Operacao Strings

first_name = 'Bruno'
last_name = 'Dias'

#Concatenacao
print(first_name + ' ' + last_name)

#Interpolacao
#.format("informar o que desejo substituir")
mensagem = 'Ola, {}, seja bem vindo'.format(first_name)
print(mensagem)
