#PROJETO FORCA
#Criar um jogo da forca com o auxílio de strings, in e not in.

import random

asciiForca = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

#GERAR UMA PALAVRA ALEATÓRIA
listaPalavras = [
    "abacaxi", "abacate", "acerola", "amora", "banana", 
    "caju", "caqui", "carambola", "cereja", "coco", 
    "cupuacu", "figo", "framboesa", "goiaba", "graviola", 
    "jabuticaba", "jaca", "kiwi", "laranja", "limao", 
    "maca", "mamao", "manga", "maracuja", "melancia", 
    "melao", "morango", "pera", "pessego", "uva"
]
palavraEscolhida = random.choice(listaPalavras)

#GERAR UMA SEQUENCIA DE TRAÇOS DO TAMANHO DA PALAVRA
palavraTracejada = ""
for i in palavraEscolhida:
    palavraTracejada += "_"

print(palavraTracejada)


palavraDescoberta = []
game_over = False
vida = 6

while not game_over:
    #PEDIR PARA O USUÁRIO ADVINHAR UMA LETRA
    letraEscolhida = input("\n\nDigite uma letra: ").lower()

    display = ""

    for letra in palavraEscolhida:

        #SE A LETRA ESTIVER NA PALAVRA
        if letra == letraEscolhida:

            #TROCAR O ESPAÇO EM BRANCO PELA LETRA
            display += letra
            palavraDescoberta.append(letra)
        
        #SE A LETRA JÁ FOI DESCOBERTA
        elif letra in palavraDescoberta:
            display += letra
        
        #SE A LETRA NÃO ESTIVER NA PALAVRA
        else:
            display += "_"

    print(display)

    if letraEscolhida not in palavraEscolhida:
        vida -= 1
        

    #SE TODAS AS VIDAS ACABARAM
    if vida == 0:
        game_over = True
        #IMPRIMIR VOCÊ PERDEU
        print("\n\nVOCÊ PERDEU")


    print(asciiForca[vida])

    #SE TODAS AS LETRAS FORAM PREENCHIDAS
    if "_" not in display:
        game_over = True

        #IMPRIMIR VOCÊ VENCEU
        print("VOCÊ GANHOU!")

    
        
        
            