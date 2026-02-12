#Projeto FORCA

'''
Docstring for aula007-Projeto
1. O programa escolhe uma palavra
2. O usuário escolhe uma letra
3. O programa verifica se a palavra possui a letra.
4. Se houver a letra, então acrescenta a letra na palavra.
5. Se não houver a letra, o contador de pontos diminui.
6. Se ainda houver pontos e todas a ainda faltar letras para serem descobertas, então volte no passo 2
7. Se não houver mais pontos então imprimir "você perdeu" e encerrar o programa.
8. Se todas as letras forem descobertas, então imprimir "você venceu" e encerrar o programa.
'''

palavra = "palavra"
palavraDescoberta = []
vida = 6
qtdDescoberta = 0

for i in range(len(palavra)):
    palavraDescoberta.append("_")
    print(palavraDescoberta[i], end = " ")


while vida > 0:
    aux = 0

    letraEscolhida = input("\n\nEscolha uma letra: ")
    for i in range(len(palavra)):
        if palavra[i] == letraEscolhida:
            aux += 1
            qtdDescoberta += 1
            palavraDescoberta[i] = letraEscolhida

    if aux == 0:
        vida -= 1
    
    if qtdDescoberta == len(palavra):
        print("VOCÊ VENCEU!")
        break

    for i in palavraDescoberta:
        print(i, end = " ")

if vida == 0:
    print("\n\nVOCÊ PERDEU!")
