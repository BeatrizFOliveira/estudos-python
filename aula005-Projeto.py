import random

lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lista_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lista_simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Bem-vindo ao GERADOR DE SENHAS!')

qtd_letras = int(input('Quantas letras você deseja na sua senha? '))
qtd_num = int(input('Quantos números você deseja na sua senha? '))
qtd_simbolos = int(input('Quantos símbolos você deseja na sua senha? '))

qtd_total = qtd_letras + qtd_num + qtd_simbolos

senha = []
letras = 0
num = 0
simbolos = 0
posicao = 0

for caractere in range(qtd_total + 1):

    while posicao == 0:

        posicao = random.randint(1, 3)
        print(posicao)

        if posicao == 1: 
            letras += 1
            if letras > qtd_letras:
                posicao = 0
            else:
                posicao = random.choice(lista_letras)
        elif posicao == 2: 
            num += 1
            if num > qtd_num:
                posicao = 0
            else:
                posicao = random.choice(lista_num)
        elif posicao == 3: 
            simbolos += 1
            if simbolos > qtd_simbolos:
                posicao = 0
            else:
                posicao = random.choice(lista_simbolos)

    senha.append(posicao)
    

print('Senha: ', senha)