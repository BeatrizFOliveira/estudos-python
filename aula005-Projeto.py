import random

lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lista_simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Bem-vindo ao GERADOR DE SENHAS!')

qtd_letras = int(input('Quantas letras você deseja na sua senha? '))
qtd_num = int(input('Quantos números você deseja na sua senha? '))
qtd_simbolos = int(input('Quantos símbolos você deseja na sua senha? '))

senha = []

for i in range(qtd_letras):
    senha.append(random.choice(lista_letras))

for i in range(qtd_num):
    senha.append(random.choice(lista_num))

for i in range(qtd_simbolos):
    senha.append(random.choice(lista_simbolos))

random.shuffle(senha)

char_senha = ''
for i in senha:
    char_senha += i

print(char_senha)